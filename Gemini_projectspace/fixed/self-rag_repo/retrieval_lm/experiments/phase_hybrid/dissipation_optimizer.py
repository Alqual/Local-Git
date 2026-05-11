import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import itertools
import random
import sys
import os

# ログツールのパス調整
# 既存の experiment_log.py がある retrieval_lm ディレクトリへのパス
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'physical_motion_models')))
try:
    from experiment_log import log_experiment
except ImportError:
    def log_experiment(**kwargs):
        print("[Log Stub] 実験ログ機能が読み込めませんでした。")

class LangevinOptimizerState:
    """
    パラメータ最適化用のLangevin散逸状態管理モジュール
    """
    def __init__(self, dim=384, mu=0.01, sigma=0.01):
        self.state = np.zeros(dim)
        self.mu = mu
        self.sigma = sigma
    
    def update(self, v_in):
        # 1. 散逸ステップ (Langevin方程式: Drift + Diffusion)
        # ドリフト項（過去情報の全体的な薄れ）
        drift = -self.mu * self.state
        # 拡散項（ランダムな熱揺らぎによる記憶の確率的削れ）
        diffusion = np.random.normal(0, self.sigma, self.state.shape)
        
        self.state += (drift + diffusion)
        
        # 2. 吸収ステップ (HRR的な情報を重ねる)
        self.state += v_in
        
        # 3. ノーマライズ
        norm = np.linalg.norm(self.state)
        if norm > 0:
            self.state /= norm

def test_parameters(quantizer, mu, sigma, turn_b=900, total_turns=1000):
    v_A = quantizer.encode(["Tackは焼肉が好き"])[0]
    v_B = quantizer.encode(["富士山は日本一高い山"])[0]
    
    # ノイズのランダムシード固定で条件を同一化
    random.seed(42)
    np.random.seed(42)
    subjects = ["天気", "科学", "音楽", "旅行", "歴史", "猫", "映画"]
    
    # 処理負荷削減のため固有のノイズは10種を事前計算してループ
    noise_pool = [quantizer.encode([f"雑談ノイズ：今日の{s}について。"])[0] for s in subjects]
    
    state = LangevinOptimizerState(384, mu, sigma)
    
    for i in range(1, total_turns + 1):
        if i == 1:
            state.update(v_A)
        elif i == turn_b:
            state.update(v_B)
        else:
            state.update(random.choice(noise_pool))
            
    final_vec = state.state
    # Collapse性能の模擬測定（Cosine Similarity）
    score_A = cosine_similarity([final_vec], [v_A])[0][0]
    score_B = cosine_similarity([final_vec], [v_B])[0][0]
    return score_A, score_B

def run_sweep():
    print("=== Phase 15: 量子層(Langevin)の散逸パラメータ最適化 ===")
    print("モデルの初期動作確認およびハイパーパラメータ・グリッドサーチ\n")
    
    quantizer = SentenceTransformer("all-MiniLM-L6-v2")
    
    mus = [0.005, 0.01, 0.05, 0.1, 0.2]
    sigmas = [0.0, 0.001, 0.005, 0.01, 0.05]
    
    print(f"{'mu':<6} | {'sigma':<6} | {'Score_A(Old)':<14} | {'Score_B(New)':<14} | {'Ratio B/A':<10}")
    print("-" * 65)
    
    results = []
    for mu, sigma in itertools.product(mus, sigmas):
        sA, sB = test_parameters(quantizer, mu, sigma, turn_b=900, total_turns=1000)
        ratio = sB / sA if sA != 0 else float("inf")
        print(f"{mu:<6} | {sigma:<6} | {sA:<14.6f} | {sB:<14.6f} | {ratio:.4f}")
        results.append({
            "mu": mu, "sigma": sigma, "sA": sA, "sB": sB, "ratio": ratio
        })
    
    print("\n--- 最適パラメータの考察 ---")
    # Score B がある程度残っている(>=0.05)中で、Ratioが一番高いものを抽出
    valid_res = [r for r in results if r["sB"] > 0.05]
    if valid_res:
        best = max(valid_res, key=lambda x: x["ratio"])
        print(f"最適な自然法則(時間区別最強): mu={best['mu']}, sigma={best['sigma']}")
        print(f" -> Ratio: {best['ratio']:.4f} (Score A: {best['sA']:.4f}, Score B: {best['sB']:.4f})")
    
    print("\n[実験完了]")

if __name__ == '__main__':
    run_sweep()
