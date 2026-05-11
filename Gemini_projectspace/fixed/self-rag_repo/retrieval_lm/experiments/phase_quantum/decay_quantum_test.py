import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import random

class QuantumState:
    def __init__(self, vector_dim=384, decay=0.99):
        # 状態空間（海面上）に生じている波形群と、海の「粘り気」の強さ
        self.state_vector = np.zeros(vector_dim)
        self.decay = decay
        
    def update(self, input_vector):
        # 「粘性」を生じさせる：新しい波を足す前に、今まで存在していた波全体を少し沈める
        self.state_vector = (self.state_vector * self.decay) + input_vector
        
        norm = np.linalg.norm(self.state_vector)
        if norm > 0:
            self.state_vector = self.state_vector / norm
            
    def get_state(self):
        return self.state_vector

print("=== Phase 9: 状態ベクトルへの減衰係数（水の粘性）の適用実験 ===")
print("減衰係数 decay=0.99 をベクトル空間全体に適用し、毎ターン古い波形が少しずつ沈む世界をシミュレートします。")
print("Target Aを常にTurn 1に固定し、Target Bの挿入ターンを50ずつずらして1000ターン目の観測結果の変化を見ます。\n")

quantizer = SentenceTransformer("all-MiniLM-L6-v2")
vec_A = quantizer.encode(["Tackは焼肉が好き"])[0]
vec_B = quantizer.encode(["富士山は日本一高い山"])[0]

def run_decay_sweep(turn_B, total_turns=1000):
    q_state = QuantumState(384, decay=0.99)
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

for turn_b in range(50, 1000, 50):
    sA, sB = run_decay_sweep(turn_b, total_turns=1000)
    # Ratio B/A を通して、「最近の記憶（B）」が「遥か過去の記憶（A）」よりどれくらい強くなっているかを比較
    print(f"{turn_b:<8} | {sA:.6f}             | {sB:.6f}             | {sB/sA:.4f}")

# 最後に、1回目と999回目の比較
sA_last, sB_last = run_decay_sweep(999, total_turns=1000)
print("-" * 75)
print(f"{999:<8} | {sA_last:.6f}             | {sB_last:.6f}             | {sB_last/sA_last:.4f}")
