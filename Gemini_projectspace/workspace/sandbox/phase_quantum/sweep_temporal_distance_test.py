import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import random

class QuantumState:
    def __init__(self, vector_dim=384):
        self.state_vector = np.zeros(vector_dim)
        
    def update(self, input_vector):
        self.state_vector = self.state_vector + input_vector
        norm = np.linalg.norm(self.state_vector)
        if norm > 0:
            self.state_vector = self.state_vector / norm
            
    def get_state(self):
        return self.state_vector

print("=== Phase 8: ターン距離とベクトル干渉の大規模スウィープ実験 ===")
print("Target Aを常にTurn 1に固定し、Target Bの挿入ターンを50ずつずらした時、")
print("Turn 1000時点での両者の残存スコアがどう推移するかを計測します。\n")

quantizer = SentenceTransformer("all-MiniLM-L6-v2")
vec_A = quantizer.encode(["Tackは焼肉が好き"])[0]
vec_B = quantizer.encode(["富士山は日本一高い山"])[0]

def run_sweep_experiment(turn_B, total_turns=1000):
    q_state = QuantumState(384)
    # ノイズのランダム性を完全に揃えるため毎度同じseedを使用し、
    # 挿入タイミングだけの純粋な物理的影響を測る
    random.seed(42)
    subjects = ["天気", "スポーツ", "映画", "料理", "歴史", "科学", "音楽", "旅行", "宇宙", "文学"]
    
    # 1000ターン分すべてのノイズを事前生成して順番を固定する
    noise_vectors = []
    for i in range(1, total_turns + 1):
        noise_text = f"雑談ノイズ: 今日の{random.choice(subjects)}は興味深いですね。記録{i}。"
        noise_vectors.append(quantizer.encode([noise_text])[0])
    
    # タイムラインに沿ってベクトルの重ね合わせを実行
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
    sA, sB = run_sweep_experiment(turn_b, total_turns=1000)
    print(f"{turn_b:<8} | {sA:.6f}             | {sB:.6f}             | {sB/sA:.4f}")

# 最後に近距離のチェックも行う
sA_last, sB_last = run_sweep_experiment(999, total_turns=1000)
print(f"{999:<8} | {sA_last:.6f}             | {sB_last:.6f}             | {sB_last/sA_last:.4f}")
