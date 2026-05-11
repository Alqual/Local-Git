import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import random
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'physical_motion_models')))
try:
    from experiment_log import log_experiment
except ImportError:
    def log_experiment(**kwargs): pass

class LangevinState:
    def __init__(self, dim=384, mu=0.2, sigma=0.05):
        self.state = np.zeros(dim)
        self.mu = mu
        self.sigma = sigma
        
    def update(self, v_in):
        drift = -self.mu * self.state
        diffusion = np.random.normal(0, self.sigma, self.state.shape)
        self.state += (drift + diffusion)
        self.state += v_in
        norm = np.linalg.norm(self.state)
        if norm > 0:
            self.state /= norm

def run_test(v_A, v_B, noise_pool):
    state = LangevinState(384, mu=0.2, sigma=0.05)
    # 乱数シードを固定し、ノイズの発生をすべてのテストで完全に一致させる
    random.seed(42)
    np.random.seed(42)
    
    for i in range(1, 1001):
        if i == 1:
            state.update(v_A)
        elif i == 900:
            state.update(v_B)
        else:
            state.update(random.choice(noise_pool))
            
    final_vec = state.state
    sA = cosine_similarity([final_vec], [v_A])[0][0]
    sB = cosine_similarity([final_vec], [v_B])[0][0]
    return sA, sB

def main():
    print("=== Phase 15.5: 入力トークン意味空間の変動による初頭効果の普遍性テスト ===")
    print("パラメータ: mu=0.2, sigma=0.05")
    print("Target A: Turn 1, Target B: Turn 900, 全1000ターン\\n")
    
    # 警告非表示のための環境変数
    os.environ["TOKENIZERS_PARALLELISM"] = "false"
    quantizer = SentenceTransformer("all-MiniLM-L6-v2")
    
    # 汎用ノイズプール（背景となる話題）
    subjects = ["天気", "科学", "音楽", "旅行", "歴史", "猫", "映画", "料理", "スポーツ", "ゲーム"]
    noise_pool = [quantizer.encode([f"雑談ノイズ：今日の{s}について。"])[0] for s in subjects]
    
    # テスト対象の文（複数のカテゴリ）
    texts = {
        "P1": "Tackは焼肉が好き",          # パーソナル
        "P2": "新しいAI構造を設計中",    # パーソナル
        "F1": "富士山は日本一高い山",       # 事実
        "F2": "水は摂氏100度で沸騰する",      # 事実
        "A1": "時間は一方向にしか進まない",   # 抽象
        "A2": "自由とは責任を伴う概念である", # 抽象
        "N1": "あいうえおかきくけこ",       # ノイズ的
        "N2": "xyz abc pqr 123",        # 記号的
    }
    
    print(f"{'Target A (Turn 1)' :<30} | {'Target B (Turn 900)' :<30} | {'Score A':<8} | {'Score B':<8} | {'Ratio B/A':<10}")
    print("-" * 95)
    
    test_keys = ["P1", "P2", "F1", "F2", "A1", "A2", "N1", "N2"]
    encoded = {k: quantizer.encode([v])[0] for k, v in texts.items()}
    
    results = []
    
    for k_a in test_keys:
        for k_b in test_keys:
            v_A = encoded[k_a]
            v_B = encoded[k_b]
            sA, sB = run_test(v_A, v_B, noise_pool)
            ratio = sB / sA if sA != 0 else float('inf')
            
            # ラベル整形
            label_A = f"[{k_a}] {texts[k_a][:12]}"
            label_B = f"[{k_b}] {texts[k_b][:12]}"
            print(f"{label_A:<30} | {label_B:<30} | {sA:<8.4f} | {sB:<8.4f} | {ratio:.4f}")
            results.append({"A": k_a, "B": k_b, "ratio": ratio, "sA": sA, "sB": sB})
            
    print("\\n[傾向分析]")
    avg_ratio = sum(r['ratio'] for r in results) / len(results)
    min_r = min(results, key=lambda x: x['ratio'])
    max_r = max(results, key=lambda x: x['ratio'])
    
    count_A_wins = sum(1 for r in results if r['ratio'] < 1.0)
    count_B_wins = sum(1 for r in results if r['ratio'] > 1.0)
    
    print(f"全 {len(results)} パターン中の勝敗: A(初期)が強い={count_A_wins}回, B(直近)が強い={count_B_wins}回")
    print(f"全体平均 Ratio B/A: {avg_ratio:.4f}")
    print(f"最小 Ratio (Aが圧倒的): {min_r['ratio']:.4f} (A:{min_r['A']} vs B:{min_r['B']})")
    print(f"最大 Ratio (Bが圧倒的): {max_r['ratio']:.4f} (A:{max_r['A']} vs B:{max_r['B']})")

if __name__ == '__main__':
    main()
