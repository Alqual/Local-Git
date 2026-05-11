import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import random
import sys, os

sys.path.insert(0, os.path.dirname(__file__))
from experiment_log import log_experiment

# ======================================================
# 時間性付きRoPE KVキャッシュ型アーキテクチャ (Phase 13)
#
# 前実験（Phase 11）の根本的な問題点：
#   _build_rotation_matrix(1) をループするだけでは
#   「処理時間 t」が回転行列に反映されず、
#   全てのターンが同じ速度で等速回転するため
#   時間的な区別が生まれない。
#
# 本実装での修正：
#   1. 各入力ベクトルを保管する際、そのターン t の
#      「絶対位置回転行列 R(t)」を掛けてから格納する。
#      （これがRoPEにおける「Key/Valueの位置符号化」に相当）
#
#   2. クエリ時（検索時）も同様に「クエリのターン t_q」で
#      R(t_q) を掛けてから内積を計算する。
#      （これがRoPEにおける「Queryの位置符号化」に相当）
#
#   3. 内積 <R(t_q)·q, R(t_k)·k> の値は、実際には
#      q と k の間の「相対的な位相差 (t_q - t_k)」に応じて変化する。
#      （RoPEの本質的な数学的特性 = 相対位置の保存）
#
#   →「古いKey（処理時間が遠い）」はqとの位相差が大きくなり、
#     内積スコアが自然に下がる（時間的な忘却が現れる）。
# ======================================================

def build_rotation_matrix(t: int, vector_dim: int = 384, base: float = 10000.0) -> np.ndarray:
    """
    絶対処理時間 t に対応するRoPE回転行列を構築する。
    θ_i = t / base^(2i/d)
    """
    R = np.eye(vector_dim)
    half = vector_dim // 2
    for i in range(half):
        theta = t / (base ** (2 * i / vector_dim))
        cos_t, sin_t = np.cos(theta), np.sin(theta)
        R[2*i,   2*i]   =  cos_t
        R[2*i,   2*i+1] = -sin_t
        R[2*i+1, 2*i]   =  sin_t
        R[2*i+1, 2*i+1] =  cos_t
    return R


class TemporalRoPEMemory:
    """
    時間性を持つKVキャッシュ型ベクトルメモリ。
    各ターンの入力ベクトルを R(t) で回転させて保管し、
    クエリ時には相対位相差で類似度を計算する。
    """
    def __init__(self, vector_dim: int = 384):
        self.dim = vector_dim
        self.keys = []    # List of (t, R(t)·v)
    
    def store(self, t: int, vector: np.ndarray):
        """ターン t の入力ベクトルを時間符号化して保管する。"""
        Rt = build_rotation_matrix(t, self.dim)
        rotated = Rt @ vector
        self.keys.append((t, rotated))
    
    def query(self, t_q: int, query_vector: np.ndarray, top_k: int = 1) -> list:
        """
        クエリベクトルを t_q で回転させ、内積スコアが高いキーを返す。
        相対位相差 (t_q - t_k) が大きい（昔の記憶）ほどスコアが下がる。
        """
        Rtq = build_rotation_matrix(t_q, self.dim)
        rotated_query = Rtq @ query_vector
        
        scores = [(t_k, np.dot(rotated_query, v_k)) for t_k, v_k in self.keys]
        scores.sort(key=lambda x: -x[1])
        return scores[:top_k]
    
    def score_for(self, t_q: int, query_vector: np.ndarray, target_vector: np.ndarray) -> float:
        """特定のターゲットベクトルとのスコアを直接計算する（評価用）。"""
        Rtq = build_rotation_matrix(t_q, self.dim)
        rq = Rtq @ query_vector
        # target_vectorはどのターンに保管されたかが不明なので
        # 加算平均のスコアで比較する（評価指標として）
        scores = [np.dot(rq, v_k) for _, v_k in self.keys]
        return float(np.max(scores))


# ============================
# 実験 Phase 13
# ============================

print("=== Phase 13: 時間性付きRoPE KV型アーキテクチャ実験 ===")
print("各ターンの入力ベクトルを R(t) で時間符号化して保管し,")
print("クエリ時の相対位相差で『古い記憶ほどスコアが下がる』かを検証します。\n")

print("[*] Loading Quantizer...")
quantizer = SentenceTransformer("all-MiniLM-L6-v2")
vec_A = quantizer.encode(["Tackは焼肉が好き"])[0]
vec_B = quantizer.encode(["富士山は日本一高い山"])[0]

def run_temporal_rope_sweep(turn_B: int, total_turns: int = 1000):
    """
    Target A (Turn 1), Target B (Turn turn_B) を保管し、
    Turn total_turns でクエリした際のスコアを返す。
    """
    memory = TemporalRoPEMemory(384)
    random.seed(42)
    subjects = ["天気", "スポーツ", "映画", "料理", "歴史", "科学", "音楽", "旅行", "宇宙", "文学"]
    
    noise_vectors = []
    for i in range(1, total_turns + 1):
        t = f"雑談ノイズ: 今日の{random.choice(subjects)}。記録{i}。"
        noise_vectors.append(quantizer.encode([t])[0])
    
    # 全ターンを時間符号化して保管
    for i in range(1, total_turns + 1):
        if i == 1:
            memory.store(i, vec_A)
        elif i == turn_B:
            memory.store(i, vec_B)
        else:
            memory.store(i, noise_vectors[i-1])
    
    # クエリ: Turn total_turns+1 の時点で「Tackの情報」を問い合わせる
    t_query = total_turns + 1
    Rq = build_rotation_matrix(t_query, 384)
    rq = Rq @ vec_A   # 「焼肉の波形」でクエリ

    # 保管されたターン1（Target A）とターン turn_B（Target B）のスコアを個別に取得
    Rt_A = build_rotation_matrix(1, 384)
    Rt_B = build_rotation_matrix(turn_B, 384)
    score_A = float(np.dot(rq, Rt_A @ vec_A))
    score_B = float(np.dot(rq, Rt_B @ vec_B))
    
    return score_A, score_B

print("計測中...\n")
print(f"{'Turn B':<8} | {'Score A (Turn 1)':<20} | {'Score B (Turn B)':<20} | {'Ratio B/A':<10}")
print("-" * 75)

results_for_log = []
for turn_b in range(50, 1000, 100):
    sA, sB = run_temporal_rope_sweep(turn_b)
    ratio = sB / sA if sA != 0 else float("inf")
    print(f"{turn_b:<8} | {sA:.6f}             | {sB:.6f}             | {ratio:.4f}")
    results_for_log.append({"label": f"Turn B={turn_b}", "score_A": round(sA, 6), "score_B": round(sB, 6)})

sA_last, sB_last = run_temporal_rope_sweep(999)
ratio_last = sB_last / sA_last
print("-" * 75)
print(f"{999:<8} | {sA_last:.6f}             | {sB_last:.6f}             | {ratio_last:.4f}")
results_for_log.append({"label": "Turn B=999 (直近)", "score_A": round(sA_last, 6), "score_B": round(sB_last, 6)})

log_experiment(
    phase=13,
    title="時間性付きRoPE KV型アーキテクチャ実験",
    description=(
        "Phase 11の反省点（R(1)の定常回転）を解消し、"
        "各入力ベクトルを保管時に絶対ターン番号 t の R(t) で回転させる方式を実装。"
        "クエリ時も t_q での R(t_q) を使い、"
        "相対位相差 (t_q - t_k) が内積スコアに現れるかを検証する。"
    ),
    params={
        "モデル": "all-MiniLM-L6-v2 (384次元)",
        "回転方式": "絶対位置 R(t) = 各ターンの絶対番号を使用（Phase 11は定常 R(1)）",
        "クエリ時刻": "t_query = total_turns + 1 = 1001",
        "クエリ内容": "vec_A = 'Tackは焼肉が好き' を R(1001) で回転してから内積",
        "Target A": "Tackは焼肉が好き（Turn 1固定）",
        "Target B": "富士山は日本一高い山（50〜999ターン可変）"
    },
    results=results_for_log,
    conclusion=(
        "各ターンのスコアが【ターン距離（t_q - t_k）が大きいほど】"
        "変化しているかを確認する。変化が現れれば"
        "RoPEの相対位置符号化が有効に機能している証拠となる。"
        "[Run後に数値を確認して追記]"
    )
)

print("\n[✅ 実験ログ保存済み]")
