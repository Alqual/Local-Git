import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import random
import sys, os

sys.path.insert(0, os.path.dirname(__file__))
from experiment_log import log_experiment

# ======================================================
# 楕円回転モデル (Elliptical Rotation)
#
# 円形回転 R(θ) = [[cos θ, -sin θ],
#                  [sin θ,  cos θ]]  は a=b=1 の円に沿った回転。
#
# 楕円回転では長軸スケール a・短軸スケール b を導入し、
# 点を楕円形の軌跡に沿って動かす：
#
#   x' = a * cos θ * x - b * sin θ * y
#   y' = a * sin θ * x + b * cos θ * y
#
# つまり行列は：
#   E(θ) = [[a·cos θ, -b·sin θ],
#            [a·sin θ,  b·cos θ]]
#
# 次元ペアごとに（a_i, b_i）を変えることで、
# 各2次元部分空間が異なる楕円軌跡を描き、
# 高周波次元（小さいθ）と低周波次元（大きいθ）が
# 異なる「伸縮」を体験する。
#
# 期待効果: 
#   円形回転では全次元が同じ半径の円を等速で回るため、
#   蓄積した状態との相対位相差がノイズに埋もれた。
#   楕円回転では各次元ペアが異なる「楕円の形」を持つため、
#   各ターンでの「どこにいるか」の指紋が次元ごとに異なる形状となる。
# ======================================================

class EllipticalQuantumState:
    def __init__(self, vector_dim=384, base=10000.0, a_range=(0.8, 1.2), b_range=(0.6, 1.4)):
        self.state_vector = np.zeros(vector_dim)
        self.dim = vector_dim
        self.base = base
        half = vector_dim // 2
        rng = np.random.default_rng(seed=42)
        # 各次元ペアに固有の楕円軸スケール（a=長軸, b=短軸）をランダムに割り当て
        # a_range: 長軸成分の分布 (1.0より大きい次元は伸長、小さいと収縮)
        # b_range: 短軸成分の分布 (非対称)
        self.a_scales = rng.uniform(a_range[0], a_range[1], size=half)
        self.b_scales = rng.uniform(b_range[0], b_range[1], size=half)

    def _build_ellipse_rotation(self) -> np.ndarray:
        """単位時間(1ターン)分の楕円回転行列を構築する。"""
        R = np.eye(self.dim)
        half = self.dim // 2
        for i in range(half):
            # RoPEと同じ周波数でθを決定
            theta = 1.0 / (self.base ** (2 * i / self.dim))
            cos_t, sin_t = np.cos(theta), np.sin(theta)
            a = self.a_scales[i]
            b = self.b_scales[i]
            # 楕円行列 [[a·cos, -b·sin], [a·sin, b·cos]]
            R[2*i,   2*i]   =  a * cos_t
            R[2*i,   2*i+1] = -b * sin_t
            R[2*i+1, 2*i]   =  a * sin_t
            R[2*i+1, 2*i+1] =  b * cos_t
        return R

    def update(self, input_vector: np.ndarray):
        # 既存の状態を楕円変換（回転+スケール変形）する
        R = self._build_ellipse_rotation()
        self.state_vector = R @ self.state_vector + input_vector
        norm = np.linalg.norm(self.state_vector)
        if norm > 0:
            self.state_vector = self.state_vector / norm

    def get_state(self):
        return self.state_vector


print("=== Phase 12: 楕円回転モデル（Elliptical Rotation）実験 ===")
print("次元ペアごとに異なる楕円軌跡（長軸a, 短軸b）を割り当て、状態の非均一な変形を確認します。\n")

print("[*] Loading Quantizer...")
quantizer = SentenceTransformer("all-MiniLM-L6-v2")
vec_A = quantizer.encode(["Tackは焼肉が好き"])[0]
vec_B = quantizer.encode(["富士山は日本一高い山"])[0]

def run_ellipse_sweep(turn_B, total_turns=1000):
    q_state = EllipticalQuantumState(384)
    random.seed(42)
    subjects = ["天気", "スポーツ", "映画", "料理", "歴史", "科学", "音楽", "旅行", "宇宙", "文学"]
    
    noise_vectors = []
    for i in range(1, total_turns + 1):
        t = f"雑談ノイズ:今日の{random.choice(subjects)}。記録{i}。"
        noise_vectors.append(quantizer.encode([t])[0])
    
    for i in range(1, total_turns + 1):
        if i == 1:
            q_state.update(vec_A)
        elif i == turn_B:
            q_state.update(vec_B)
        else:
            q_state.update(noise_vectors[i-1])

    final = q_state.get_state()
    sA = cosine_similarity([final], [vec_A])[0][0]
    sB = cosine_similarity([final], [vec_B])[0][0]
    return sA, sB

print("計測中...\n")
print(f"{'Turn B':<8} | {'Score A (Turn 1)':<20} | {'Score B (Turn B)':<20} | {'Ratio B/A':<10}")
print("-" * 75)

results_for_log = []
for turn_b in range(50, 1000, 100):
    sA, sB = run_ellipse_sweep(turn_b)
    ratio = sB / sA if sA != 0 else float("inf")
    print(f"{turn_b:<8} | {sA:.6f}             | {sB:.6f}             | {ratio:.4f}")
    results_for_log.append({"label": f"Turn B={turn_b}", "score_A": float(sA), "score_B": float(sB)})

sA_last, sB_last = run_ellipse_sweep(999)
ratio_last = sB_last / sA_last
print("-" * 75)
print(f"{999:<8} | {sA_last:.6f}             | {sB_last:.6f}             | {ratio_last:.4f}")
results_for_log.append({"label": "Turn B=999 (直近)", "score_A": float(sA_last), "score_B": float(sB_last)})

conclusion = (
    f"楕円回転（a∈[0.8,1.2], b∈[0.6,1.4]）を適用した結果、"
    f"Turn B=50〜950 のスコア: A={results_for_log[0]['score_A']:.4f}, B={results_for_log[0]['score_B']:.4f} "
    f"(Ratio={results_for_log[0]['score_B']/results_for_log[0]['score_A']:.4f}), "
    f"Turn B=999: A={sA_last:.4f}, B={sB_last:.4f} (Ratio={ratio_last:.4f})。"
    "[考察はスクリプト実行後に追記する]"
)

log_experiment(
    phase=12,
    title="楕円回転モデル（Elliptical Rotation）",
    description=(
        "円形回転（a=b=1）では全次元が同一の軌跡を描き、"
        "時間情報が位相差として有効に符号化されなかった。"
        "楕円回転ではaとbを次元ペアごとに異なる値に設定することで、"
        "各次元ペアが固有の楕円形の軌跡を持つ。"
        "状態の『変形』が一様でなくなるため、異なる時刻に足された"
        "ベクトルが与える指紋がより区別可能になるか検証する。"
    ),
    params={
        "モデル": "all-MiniLM-L6-v2 (384次元)",
        "長軸a_range": "[0.8, 1.2]（次元ペアごとにseed=42で均一分布から選択）",
        "短軸b_range": "[0.6, 1.4]（asと独立に選択）",
        "周波数計算": "θ_i = 1 / 10000^(2i/d)（RoPE準拠）",
        "ノイズ量": "998ターン / 1000ターン中",
        "Target A": "Tackは焼肉が好き（Turn 1固定）",
        "Target B": "富士山は日本一高い山（可変）"
    },
    results=results_for_log,
    conclusion=conclusion
)

print("\n[✅ 実験ログ保存済み] experiment_results/ を確認してください")
