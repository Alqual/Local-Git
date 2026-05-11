import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import random

class HeterogeneousQuantumState:
    def __init__(self, vector_dim=384):
        self.state_vector = np.zeros(vector_dim)
        
        # 不均一な粘性層（異方性減衰）の構築
        # 半分の次元(192次元)には「強い忘却(0.95)」を与え、短期記憶として振る舞わせる
        # 残り半分の次元(192次元)には「極めてゆるやかな忘却(0.999)」を与え、情報の定常性(長期記憶)を持たせる
        decay_fast = np.ones(192) * 0.95
        decay_slow = np.ones(192) * 0.999
        self.decay_vector = np.concatenate([decay_fast, decay_slow])
        
    def update(self, input_vector):
        # 均一なスカラー値ではなく、次元ごとに異なる減衰率(ベクトル)を掛け合わせる
        self.state_vector = (self.state_vector * self.decay_vector) + input_vector
        
        norm = np.linalg.norm(self.state_vector)
        if norm > 0:
            self.state_vector = self.state_vector / norm
            
    def get_state(self):
        return self.state_vector

print("=== Phase 10: 異方性減衰（不均一な粘性層）の適用実験 ===")
print("次元によって粘性（減衰係数）が異なるモデルを検証します。")
print("前半192次元は「減衰0.95（短期記憶・水のようにサラサラ）」")
print("後半192次元は「減衰0.999（長期記憶・蜂蜜のようにドロドロ）」\n")

print("[*] Loading Quantizer (Embedding Model)...")
quantizer = SentenceTransformer("all-MiniLM-L6-v2")
vec_A = quantizer.encode(["Tackは焼肉が好き"])[0]
vec_B = quantizer.encode(["富士山は日本一高い山"])[0]

def run_heterogeneous_sweep(turn_B, total_turns=1000):
    q_state = HeterogeneousQuantumState(384)
    random.seed(42)
    subjects = ["天気", "スポーツ", "映画", "料理", "歴史", "科学", "音楽", "旅行", "宇宙", "文学"]
    
    noise_vectors = []
    for i in range(1, total_turns + 1):
        noise_text = f"雑談ノイズ: 今日の{random.choice(subjects)}は興味深いですね。記録{i}。"
        noise_vectors.append(quantizer.encode([noise_text])[0])
    
    for i in range(1, total_turns + 1):
        if i == 1:
            q_state.update(vec_A)
        elif i == turn_B:
            q_state.update(vec_B)
        else:
            q_state.update(noise_vectors[i-1])

    final_state = q_state.get_state()
    score_A = cosine_similarity([final_state], [vec_A])[0][0]
    score_B = cosine_similarity([final_state], [vec_B])[0][0]
    
    return score_A, score_B

print("計測中...\n")
print(f"{'Turn B':<8} | {'Score A (Turn 1)':<20} | {'Score B (Turn B)':<20} | {'Ratio B/A':<10}")
print("-" * 75)

for turn_b in range(50, 1000, 100):
    sA, sB = run_heterogeneous_sweep(turn_b, total_turns=1000)
    print(f"{turn_b:<8} | {sA:.6f}             | {sB:.6f}             | {sB/sA:.4f}")

# 最新ターンのチェック
sA_last, sB_last = run_heterogeneous_sweep(999, total_turns=1000)
print("-" * 75)
print(f"{999:<8} | {sA_last:.6f}             | {sB_last:.6f}             | {sB_last/sA_last:.4f}")
