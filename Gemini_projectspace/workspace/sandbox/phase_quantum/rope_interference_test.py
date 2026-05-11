import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import random
import sys
import os

# ====== 実験ログライブラリのインポート ======
sys.path.insert(0, os.path.dirname(__file__))
from experiment_log import log_experiment, list_experiments

# ======================================================
# RoPE（Rotary Position Embedding）インスパイアの
# 時間干渉行列を使った状態ベクトルの実装
#
# 核心アイデア：
#   新しい入力ベクトルを足す前に、「現在の状態ベクトルを
#   時間tに応じた角度θだけ回転させる」。
#   これにより、過去の波形と現在の波形の「位相（角度）」が
#   互いにずれていき、どの時点の情報かが空間的に区別可能になる。
#
#   RoPEでは複素平面(2次元ペア)でtheta = t * base^(-2i/d) を使う。
#   ここでは簡略化して、連続した2次元ペアを時刻tで回転させる
#   回転行列 R(t) を構築する。
# ======================================================

class RoPEQuantumState:
    def __init__(self, vector_dim=384, base=10000.0):
        self.state_vector = np.zeros(vector_dim)
        self.dim = vector_dim
        self.base = base
        self.t = 0  # 現在のターン（時刻）

    def _build_rotation_matrix(self, t: int) -> np.ndarray:
        """
        RoPE式の回転行列を構築する。
        ベクトルの各2次元ペア (d_0, d_1), (d_2, d_3), ... に対し
        θ_i = t / base^(2i / dim) の角度で回転させる。
        """
        R = np.eye(self.dim)
        half = self.dim // 2
        for i in range(half):
            theta = t / (self.base ** (2 * i / self.dim))
            cos_t, sin_t = np.cos(theta), np.sin(theta)
            # 2次元ペア (2i, 2i+1) に回転行列を適用
            R[2*i,   2*i]   =  cos_t
            R[2*i,   2*i+1] = -sin_t
            R[2*i+1, 2*i]   =  sin_t
            R[2*i+1, 2*i+1] =  cos_t
        return R

    def update(self, input_vector: np.ndarray):
        self.t += 1
        # ステップ1: 現在の状態ベクトルを時刻tだけ「老化回転」させる（相対的な時間距離を空間で表現）
        R = self._build_rotation_matrix(1)   # 1ターン分の微小回転
        self.state_vector = R @ self.state_vector
        
        # ステップ2: 新しい入力ベクトルをそのまま足す（新鮮な情報は回転させない）
        self.state_vector = self.state_vector + input_vector
        
        # 正規化
        norm = np.linalg.norm(self.state_vector)
        if norm > 0:
            self.state_vector = self.state_vector / norm

    def get_state(self):
        return self.state_vector


# ====== 実験 Phase 11 ======

print("=== Phase 11: RoPE干渉行列による時間符号化（位相回転）モデル ===")
print("状態ベクトルを毎ターン微小回転させることで、時間経過を「空間的な位相差」として表現します。\n")

quantizer = SentenceTransformer("all-MiniLM-L6-v2")
vec_A = quantizer.encode(["Tackは焼肉が好き"])[0]
vec_B = quantizer.encode(["富士山は日本一高い山"])[0]

def run_rope_sweep(turn_B, total_turns=1000):
    q_state = RoPEQuantumState(384)
    random.seed(42)
    subjects = ["天気", "スポーツ", "映画", "料理", "歴史", "科学", "音楽", "旅行", "宇宙", "文学"]
    
    noise_vectors = []
    for i in range(1, total_turns + 1):
        noise_text = f"雑談ノイズ:今日の{random.choice(subjects)}は興味深いですね。記録{i}。"
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

results_for_log = []
for turn_b in range(50, 1000, 100):
    sA, sB = run_rope_sweep(turn_b, total_turns=1000)
    ratio = sB / sA if sA != 0 else float("inf")
    print(f"{turn_b:<8} | {sA:.6f}             | {sB:.6f}             | {ratio:.4f}")
    results_for_log.append({"label": f"Turn B={turn_b}", "score_A": sA, "score_B": sB})

sA_last, sB_last = run_rope_sweep(999, total_turns=1000)
print("-" * 75)
print(f"{999:<8} | {sA_last:.6f}             | {sB_last:.6f}             | {sB_last/sA_last:.4f}")
results_for_log.append({"label": "Turn B=999 (直近)", "score_A": sA_last, "score_B": sB_last})

# ====== 実験ログへの記録 ======
log_experiment(
    phase=11,
    title="RoPE干渉行列による時間符号化（位相回転）モデル",
    description=(
        "均一・不均一粘性モデルでは「時間の概念」が生じなかった課題を受け、"
        "RoPE（Rotary Position Embedding）を参照した回転行列を導入。"
        "毎ターン状態ベクトル全体を微小角θ(=1ターン分)だけ回転させることで、"
        "古い情報と新しい情報を空間上で「位相がずれた（角度が異なる）波」として区別できないか検証する。\n"
        "Target A をTurn 1、Target B を50〜999ターン目の位置に入れ、1000ターン後のスコアを観測。"
    ),
    params={
        "モデル": "all-MiniLM-L6-v2 (384次元)",
        "回転base定数": 10000.0,
        "単位回転量": "1ターン毎にR(1)を適用（2次元ペアごとθ_i = 1/base^(2i/d)）",
        "ノイズ量": "1000ターン中998ターン（無関係なランダムトピック）",
        "Target A": "Tackは焼肉が好き（Turn 1固定）",
        "Target B": "富士山は日本一高い山（50〜999ターン可変）"
    },
    results=results_for_log,
    conclusion=(
        "後述。実験実行後に結果を参照して記述。"
    )
)

print("\n[実験ログを experiment_results/ ディレクトリに保存しました]")
print("[リスト確認コマンド: python -c \"from experiment_log import list_experiments; list_experiments()\"]")
