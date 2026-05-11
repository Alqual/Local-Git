import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import random
import os
import matplotlib.pyplot as plt
from hybrid_models import LangevinMemory, LevyFlightMemory, KuramotoMemory, HopfieldMemory, HybridCognitiveMemory

os.environ["TOKENIZERS_PARALLELISM"] = "false"
print("Loading Model...")
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

def run_test_for_model(model_class, v_A, v_B):
    model = model_class(dim=384)
    random.seed(42)
    np.random.seed(42)
    for i in range(1, 1001):
        if i == 1: 
            model.update(v_A, alpha=0.50)
        elif i == 900: 
            model.update(v_B, alpha=0.50)
        else: 
            model.update(random.choice(noise_pool), alpha=0.01)
    return cosine_similarity([model.state], [v_A])[0][0], cosine_similarity([model.state], [v_B])[0][0]

def experiment(model_class, name):
    print(f"Running 64 tests for {name}...")
    keys = list(texts_v1.keys())
    encoded = {k: quantizer.encode([v])[0] for k, v in texts_v1.items()}
    sims = {k: np.mean(cosine_similarity([encoded[k]], noise_pool)[0]) for k in keys}
    xs_A, ys_sA, xs_B, ys_sB = [], [], [], []
    
    for k_a in keys:
        for k_b in keys:
            sA, sB = run_test_for_model(model_class, encoded[k_a], encoded[k_b])
            xs_A.append(sims[k_a]); ys_sA.append(sA)
            xs_B.append(sims[k_b]); ys_sB.append(sB)
            
    fig, ax1 = plt.subplots(1, 1, figsize=(10, 8))
    ax1.scatter(xs_A, ys_sA, label='Target A (Turn 1 | α=0.5)', color='red', alpha=0.6, s=60)
    ax1.scatter(xs_B, ys_sB, label='Target B (Turn 900 | α=0.5)', color='blue', marker='^', alpha=0.6, s=60)
    
    zA = np.polyfit(xs_A, ys_sA, 1); pA = np.poly1d(zA)
    zB = np.polyfit(xs_B, ys_sB, 1); pB = np.poly1d(zB)
    x_range = np.linspace(min(xs_A+xs_B), max(xs_A+xs_B), 100)
    ax1.plot(x_range, pA(x_range), "r--", linewidth=2)
    ax1.plot(x_range, pB(x_range), "b-", linewidth=2)
    
    ax1.axhline(0, color='gray', linestyle='--')
    ax1.set_xlabel('Base Similarity to Background Noise')
    ax1.set_ylabel('Final Memory Score')
    ax1.set_title(f'{name} Mechanism: Target A vs Target B')
    ax1.legend(loc="best")
    ax1.grid(True, linestyle=":", alpha=0.7)
    
    out_dir = '/home/tack-mit/デスクトップ/Gemini_projectspace/self-rag_repo/retrieval_lm/experiments/phase18_hybrid_physics'
    plt.savefig(os.path.join(out_dir, f'{name}_results.png'), dpi=300, bbox_inches='tight')
    plt.close()

models = [
    (LangevinMemory, "1_Langevin"),
    (LevyFlightMemory, "2_LevyFlight"),
    (KuramotoMemory, "3_Kuramoto"),
    (HopfieldMemory, "4_Hopfield"),
    (HybridCognitiveMemory, "5_Hybrid")
]
for mod, name in models:
    experiment(mod, name)
print("\nAll 5 experiments completed successfully.")
