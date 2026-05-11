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
        
    def update(self, v_in):
        drift = -self.mu * self.state
        diffusion = np.random.normal(0, self.sigma, self.state.shape)
        self.state += (drift + diffusion)
        self.state += v_in
        norm = np.linalg.norm(self.state)
        if norm > 0:
            self.state /= norm

def run_test(v_A, v_B, noise_pool, mu, sigma):
    state = LangevinState(384, mu=mu, sigma=sigma)
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
    
    mu_list = [0.0001, 0.001, 0.01, 0.1]
    sigma = 0.01
    
    report = "# Phase 15.6: ドリフト項（μ）に関するスウィープ検証レポート\n\n"
    report += "**作成日**: 2026-04-12  \n"
    report += "**目的**: 健忘症を起こした前回（μ=0.2）の反省から、減衰速度を微小（0.0001）から中程度（0.1）までの4パターンで振り、真に「過去の記憶が防衛されつつ、最近の記憶の方が強く残存する」適切な減衰バランスを特定する。\n"
    report += "**固定パラメータ**: Σ(sigma: 熱揺らぎ) = 0.01, 長さ=1000ターン, Target A(Turn 1), Target B(Turn 900)\n\n"
    
    for mu in mu_list:
        report += f"## μ = {mu} の検証結果\n"
        results = []
        for k_a in test_keys:
            for k_b in test_keys:
                v_A = encoded[k_a]
                v_B = encoded[k_b]
                sA, sB = run_test(v_A, v_B, noise_pool, mu, sigma)
                ratio = sB / sA if sA != 0 else float('inf')
                results.append({"A": k_a, "B": k_b, "ratio": ratio, "sA": sA, "sB": sB})
                
        ratio_p2_n2 = next(r for r in results if r["A"]=="P2" and r["B"]=="N2")
        ratio_n2_p2 = next(r for r in results if r["A"]=="N2" and r["B"]=="P2")
        ratio_p2_p2 = next(r for r in results if r["A"]=="P2" and r["B"]=="P2")
        
        # 1.05と0.95で勝敗を定義
        count_A = sum(1 for r in results if r["ratio"] < 0.95)
        count_B = sum(1 for r in results if r["ratio"] > 1.05)
        count_Tie = sum(1 for r in results if 0.95 <= r["ratio"] <= 1.05)
        
        avg_sA = np.mean([r["sA"] for r in results])
        avg_sB = np.mean([r["sB"] for r in results])
        avg_ratio = np.mean([r["ratio"] for r in results])
        
        report += f"- **A(初期)の勝利/残存**: {count_A}回\n"
        report += f"- **B(直近)の勝利/残存**: {count_B}回\n"
        report += f"- **引き分け(ほぼ同等)**: {count_Tie}回\n"
        report += f"- **平均スコア**: Score A = {avg_sA:.4f}, Score B = {avg_sB:.4f} (平均比率: {avg_ratio:.4f})\n\n"
        
        report += "### 注目の組み合わせ比較\n"
        report += "| A(Turn 1) | B(Turn 900) | Score A | Score B | Ratio(B/A) | 意味合い |\n"
        report += "|---|---|---|---|---|---|\n"
        report += f"| P2(意味強) | P2(意味強) | {ratio_p2_p2['sA']:.4f} | {ratio_p2_p2['sB']:.4f} | **{ratio_p2_p2['ratio']:.4f}** | 【純粋な時間対決】同じ文の時系列差 |\n"
        report += f"| P2(意味強) | N2(無意味) | {ratio_p2_n2['sA']:.4f} | {ratio_p2_n2['sB']:.4f} | **{ratio_p2_n2['ratio']:.4f}** | 【Aの防衛力】ノイズへの耐性 |\n"
        report += f"| N2(無意味) | P2(意味強) | {ratio_n2_p2['sA']:.4f} | {ratio_n2_p2['sB']:.4f} | **{ratio_n2_p2['ratio']:.4f}** | 【Bの書換力】ノイズを塗り替える力 |\n\n"

    out_file = "/home/tack-mit/.gemini/antigravity/brain/6d626d06-a76f-4c1f-81f1-612d5069732c/report_phase15_6_mu_sweep.md"
    with open(out_file, 'w', encoding='utf-8') as f:
        f.write(report)
    print(f"Report saved to {out_file}")

if __name__ == '__main__':
    main()
