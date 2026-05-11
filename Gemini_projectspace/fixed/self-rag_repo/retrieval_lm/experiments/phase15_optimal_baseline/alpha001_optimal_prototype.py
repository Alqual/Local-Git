import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import random
import os

class LangevinState:
    def __init__(self, dim=384, mu=0.001, sigma=0.01):
        self.state = np.zeros(dim)
        self.mu = mu
        self.sigma = sigma
    
    def update(self, v_in, alpha=1.0):
        drift = -self.mu * self.state
        diffusion = np.random.normal(0, self.sigma, self.state.shape)
        
        # 既存の状態に時間経過(Scatter)を適用
        self.state += (drift + diffusion)
        
        # 新しい情報を「スケール(alpha)を掛けてから」足す
        self.state += alpha * v_in
        
        # 正規化によるアトラクタへの引き込み
        norm = np.linalg.norm(self.state)
        if norm > 0:
            self.state /= norm

def run_test(v_A, v_B, noise_pool, alpha, mu=0.001, sigma=0.01):
    state = LangevinState(384, mu=mu, sigma=sigma)
    random.seed(42)
    np.random.seed(42)
    
    for i in range(1, 1001):
        if i == 1:
            state.update(v_A, alpha)
        elif i == 900:
            state.update(v_B, alpha)
        else:
            state.update(random.choice(noise_pool), alpha)
            
    final_vec = state.state
    sA = cosine_similarity([final_vec], [v_A])[0][0]
    sB = cosine_similarity([final_vec], [v_B])[0][0]
    return sA, sB

def main():
    os.environ["TOKENIZERS_PARALLELISM"] = "false"
    quantizer = SentenceTransformer("all-MiniLM-L6-v2")
    
    subjects = ["天気", "科学", "音楽", "旅行", "歴史", "猫", "映画", "料理", "スポーツ", "ゲーム"]
    noise_pool = [quantizer.encode([f"雑談ノイズ：今日の{s}について。"])[0] for s in subjects]
    
    texts = {
        "P1": "Tackは焼肉が好き",          
        "P2": "新しいAI構造を設計中",    
        "F1": "富士山は日本一高い山",       
        "F2": "水は摂氏100度で沸騰する",      
        "A1": "時間は一方向にしか進まない",   
        "A2": "自由とは責任を伴う概念である", 
        "N1": "あいうえおかきくけこ",       
        "N2": "xyz abc pqr 123",        
    }
    
    test_keys = ["P1", "P2", "F1", "F2", "A1", "A2", "N1", "N2"]
    encoded = {k: quantizer.encode([v])[0] for k, v in texts.items()}
    
    alpha_list = [0.001, 0.01, 0.1, 1.0]
    mu = 0.001
    sigma = 0.01
    
    report = "# Phase 15.7: 入力重み（α）に関するスウィープ検証レポート\n\n"
    report += "**作成日**: 2026-04-12  \n"
    report += "**目的**: \nLangevin更新において新しい情報を状態ベクトルに加算する際の吸収力（α）を調整し、記憶が致命的忘却を起こさず、且つ直近の記憶（B）が過去の記憶（A）より強く残る適正なバランスを探索する。\n\n"
    report += f"**固定パラメータ**: μ(自己減衰) = {mu}, σ(熱揺らぎ) = {sigma}, 長さ=1000ターン\n\n"
    
    for alpha in alpha_list:
        report += f"## α = {alpha} の検証結果\n"
        results = []
        for k_a in test_keys:
            for k_b in test_keys:
                v_A = encoded[k_a]
                v_B = encoded[k_b]
                sA, sB = run_test(v_A, v_B, noise_pool, alpha, mu, sigma)
                ratio = sB / sA if sA != 0 else float('inf')
                results.append({"A": k_a, "B": k_b, "ratio": ratio, "sA": sA, "sB": sB})
                
        # 注目の組み合わせ
        ratio_p2_n2 = next(r for r in results if r["A"]=="P2" and r["B"]=="N2")
        ratio_n2_p2 = next(r for r in results if r["A"]=="N2" and r["B"]=="P2")
        ratio_p2_p2 = next(r for r in results if r["A"]=="P2" and r["B"]=="P2")
        
        count_A = sum(1 for r in results if r["ratio"] < 0.99)
        count_B = sum(1 for r in results if r["ratio"] > 1.01)
        count_Tie = sum(1 for r in results if 0.99 <= r["ratio"] <= 1.01)
        
        avg_sA = np.mean([r["sA"] for r in results])
        avg_sB = np.mean([r["sB"] for r in results])
        avg_ratio = np.mean([r["ratio"] for r in results])
        
        report += f"- **A(Turn1)の実質的勝利**: {count_A}回\n"
        report += f"- **B(Turn900)の実質的勝利**: {count_B}回\n"
        report += f"- **引き分け(ほぼ同等)**: {count_Tie}回\n"
        report += f"- **全体平均**: Score A = {avg_sA:.4f}, Score B = {avg_sB:.4f} (平均比率 B/A: {avg_ratio:.4f})\n\n"
        
        report += "### 詳細抜粋（注目すべき意味の強さ対決）\n"
        report += "| Target A(T1) | Target B(T900) | Score A | Score B | Ratio(B/A) | 意味合い |\n"
        report += "|---|---|---|---|---|---|\n"
        report += f"| P2(意味強) | P2(意味強) | {ratio_p2_p2['sA']:.4f} | {ratio_p2_p2['sB']:.4f} | **{ratio_p2_p2['ratio']:.4f}** | 【時系列対決】同じ強度の文の時系列差 |\n"
        report += f"| P2(意味強) | N2(無意味) | {ratio_p2_n2['sA']:.4f} | {ratio_p2_n2['sB']:.4f} | **{ratio_p2_n2['ratio']:.4f}** | 【Aの防衛力】無意味なノイズの攻撃への耐性 |\n"
        report += f"| N2(無意味) | P2(意味強) | {ratio_n2_p2['sA']:.4f} | {ratio_n2_p2['sB']:.4f} | **{ratio_n2_p2['ratio']:.4f}** | 【Bの上書き】強固な意味によるパラダイムシフト |\n\n"

    out_file = "/home/tack-mit/.gemini/antigravity/brain/6d626d06-a76f-4c1f-81f1-612d5069732c/report_phase15_7_alpha_sweep.md"
    with open(out_file, 'w', encoding='utf-8') as f:
        f.write(report)
    print(f"Report saved to {out_file}")

if __name__ == '__main__':
    main()
