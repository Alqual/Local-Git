import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import random
import time

class QuantumState:
    def __init__(self, vector_dim=384):
        self.state_vector = np.zeros(vector_dim)
        
    def update(self, input_vector):
        # 足し合わせて都度正規化する。
        # 実は都度正規化を行うことで、古いベクトルほど割り算の回数が増え、
        # 物理的に「時間的手前にあるほど減衰する」という天然の時間特性(Time Decay)が発生する。
        self.state_vector = self.state_vector + input_vector
        norm = np.linalg.norm(self.state_vector)
        if norm > 0:
            self.state_vector = self.state_vector / norm
            
    def get_state(self):
        return self.state_vector

print("=== Phase 7: 複数時点・複数ベクトル間の干渉と時間的距離の特性検証 ===")
print("【実験目的】")
print("異なる時間（ターン）に入力された2つの情報（Target A, Target B）が、")
print("「時間的な距離」や「意味の類似性」によってどう干渉し、残存するかを定量的に調べます。\n")

print("[*] Loading Quantizer (Embedding Model)...")
quantizer = SentenceTransformer("all-MiniLM-L6-v2")

def run_experiment(turn_A, desc_A, turn_B, desc_B, total_turns=1000):
    q_state = QuantumState(384)
    # 同じシードでノイズの影響を平等にする
    random.seed(42)
    subjects = ["天気", "スポーツ", "映画", "料理", "歴史", "科学", "音楽", "旅行"]
    
    vec_A = quantizer.encode([desc_A])[0]
    vec_B = quantizer.encode([desc_B])[0]
    
    for i in range(1, total_turns + 1):
        if i == turn_A:
            q_state.update(vec_A)
        elif i == turn_B:
            q_state.update(vec_B)
        else:
            noise = f"雑談ノイズ: 今日の{random.choice(subjects)}は興味深いですね。記録{i}。"
            q_state.update(quantizer.encode([noise])[0])
            
    # 直接入力ベクトルとのコサイン類似度を比較し、
    # 最終的な状態空間に「Target A」「Target B」の波形がどれくらい残存しているかスコア化する
    final_state = q_state.get_state()
    score_A = cosine_similarity([final_state], [vec_A])[0][0]
    score_B = cosine_similarity([final_state], [vec_B])[0][0]
    
    return score_A, score_B

# 検証パターンの定義
experiments = [
    {"name": "実験1: 時間距離が遠く、意味も異なる (T1とT900)", "tA": 1, "dA": "Tackは焼肉が好き", "tB": 900, "dB": "富士山は日本一高い山"},
    {"name": "実験2: 時間距離が近く、意味も異なる (T500とT501)", "tA": 500, "dA": "Tackは焼肉が好き", "tB": 501, "dB": "富士山は日本一高い山"},
    {"name": "実験3: 時間距離が遠く、意味が似ている (T1とT900)", "tA": 1, "dA": "Tackは焼肉が好き", "tB": 900, "dB": "Tackは寿司も大好きだ"},
    {"name": "実験4: 時間距離が近く、意味が似ている (T500とT501)", "tA": 500, "dA": "Tackは焼肉が好き", "tB": 501, "dB": "Tackは寿司も大好きだ"}
]

print("大規模シミュレーションを開始します... (各1000ターン)")
for exp in experiments:
    sA, sB = run_experiment(exp["tA"], exp["dA"], exp["tB"], exp["dB"])
    print(f"\n{exp['name']}")
    print(f" -> Target A (Turn {exp['tA']:3d}): 残存振幅スコア = {sA:.4f} ('{exp['dA']}')")
    print(f" -> Target B (Turn {exp['tB']:3d}): 残存振幅スコア = {sB:.4f} ('{exp['dB']}')")
