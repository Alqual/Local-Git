import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import random
import os
import matplotlib.pyplot as plt

class DynamicLangevinState:
    def __init__(self, dim=384, mu=0.001, sigma=0.01):
        self.state = np.zeros(dim)
        self.mu = mu
        self.sigma = sigma
    
    def update(self, v_in, is_signal=False):
        """
        Dynamic Alpha:
        is_signal=True -> user query / distinct context -> high alpha (0.5)
        is_signal=False -> background noise -> low alpha (0.01)
        """
        alpha = 0.50 if is_signal else 0.01
        drift = -self.mu * self.state
        diffusion = np.random.normal(0, self.sigma, self.state.shape)
        self.state += (drift + diffusion)
        self.state += alpha * v_in
        norm = np.linalg.norm(self.state)
        if norm > 0:
            self.state /= norm

os.environ["TOKENIZERS_PARALLELISM"] = "false"
quantizer = SentenceTransformer("all-MiniLM-L6-v2")
subjects = ["weather", "science", "music", "travel", "history", "cats", "movies", "cooking", "sports", "gaming"]
noise_pool = [quantizer.encode([f"Chatter noise: about today's {s}."])[0] for s in subjects]

texts_v1 = {
    "P1": "Tack loves eating BBQ.",          
    "P2": "Currently designing a new AI architecture.",    
    "F1": "Mount Fuji is the tallest mountain in Japan.",       
    "F2": "Water boils at one hundred degrees Celsius.",      
    "A1": "Time flows strictly in one single direction.",   
    "A2": "Freedom is a concept that inherently requires responsibility.", 
    "N1": "abcd efgh ijkl mnop qrst",       
    "N2": "xyz abc pqr 123",        
}

texts_v2 = {
    "S1": "I am talking about today's weather and sports.",
    "S2": "Chatter noise: about today's politics and fashion.",
    "S3": "Let's discuss recent movies and gaming.",
    "O1": "Space exploration requires massive rocket propulsion.",
    "O2": "Machine learning algorithms optimize mathematical loss functions.",
    "P1_v2": "The fundamental rights of citizens are protected by the constitution.",
    "N1_v2": "hjkl yiop nmvc xzsd",
    "N2_v2": "9876 5432 1098 7654"
}

def run_dynamic_test(v_A, v_B, noise_pool):
    state = DynamicLangevinState(384, mu=0.001, sigma=0.01)
    random.seed(42)  # For consistent noise
    np.random.seed(42)
    for i in range(1, 1001):
        if i == 1: 
            state.update(v_A, is_signal=True)
        elif i == 900: 
            state.update(v_B, is_signal=True)
        else: 
            state.update(random.choice(noise_pool), is_signal=False)
            
    return cosine_similarity([state.state], [v_A])[0][0], cosine_similarity([state.state], [v_B])[0][0]

def get_dynamic_data(texts_dict):
    keys = list(texts_dict.keys())
    encoded = {k: quantizer.encode([v])[0] for k, v in texts_dict.items()}
    sims = {k: np.mean(cosine_similarity([encoded[k]], noise_pool)[0]) for k in keys}
    xs_A, ys_sA, xs_B, ys_sB = [], [], [], []
    
    for k_a in keys:
        for k_b in keys:
            sA, sB = run_dynamic_test(encoded[k_a], encoded[k_b], noise_pool)
            xs_A.append(sims[k_a])
            ys_sA.append(sA)
            xs_B.append(sims[k_b])
            ys_sB.append(sB)
    return xs_A, ys_sA, xs_B, ys_sB

print("Running 128 tests for Dynamic Alpha Prototype...")
v1_xA, v1_yA, v1_xB, v1_yB = get_dynamic_data(texts_v1)
v2_xA, v2_yA, v2_xB, v2_yB = get_dynamic_data(texts_v2)

all_xA = v1_xA + v2_xA
all_yA = v1_yA + v2_yA
all_xB = v1_xB + v2_xB
all_yB = v1_yB + v2_yB

fig, ax1 = plt.subplots(1, 1, figsize=(10, 8))

ax1.scatter(all_xA, all_yA, label='Target A (Turn 1 | sig_α=0.5)', color='red', alpha=0.6, s=60, edgecolor='k')
ax1.scatter(all_xB, all_yB, label='Target B (Turn 900 | sig_α=0.5)', color='blue', marker='^', alpha=0.6, s=60, edgecolor='k')

zA = np.polyfit(all_xA, all_yA, 1)
pA = np.poly1d(zA)
x_range = np.linspace(min(all_xA+all_xB), max(all_xA+all_xB), 100)
ax1.plot(x_range, pA(x_range), "r--", linewidth=2, label="Target A Trend")

zB = np.polyfit(all_xB, all_yB, 1)
pB = np.poly1d(zB)
ax1.plot(x_range, pB(x_range), "b-", linewidth=2, label="Target B Trend")

ax1.axhline(0, color='gray', linestyle='--', alpha=0.5)
ax1.set_xlabel('Base Similarity to Background Noise (X)')
ax1.set_ylabel('Final Memory Score (Y)')
ax1.set_title('Dynamic Alpha Mechanism: Perfect Target A vs Target B Separation')
ax1.legend(loc='upper left')
ax1.grid(True, linestyle=":", alpha=0.7)

out_dir = '/home/tack-mit/デスクトップ/Gemini_projectspace/self-rag_repo/retrieval_lm/experiments/phase16_dynamic_alpha'
os.makedirs(out_dir, exist_ok=True)
out_path = os.path.join(out_dir, 'dynamic_alpha_results.png')
plt.savefig(out_path, dpi=300, bbox_inches='tight')
print(f"Plot saved to {out_path}")

out_path_brain = '/home/tack-mit/.gemini/antigravity/brain/6d626d06-a76f-4c1f-81f1-612d5069732c/dynamic_alpha_results.png'
plt.savefig(out_path_brain, dpi=300, bbox_inches='tight')
