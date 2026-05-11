"""
run_all.py
==========
4つの物理運動モデルを一括実行し、結果を比較する統合スクリプト。
実行：
    CUDA_VISIBLE_DEVICES="" HF_HUB_OFFLINE=1 \\
    ../.venv_39/bin/python physical_motion_models/run_all.py
"""
import sys, os
import numpy as np

sys.path.insert(0, os.path.dirname(__file__))
from shared_utils import prepare_vectors, sweep, print_table, DIM, TOTAL_TURNS
import model1_damped_oscillator as m1
import model2_langevin         as m2
import model3_fokker_planck    as m3
import model4_lindblad         as m4

BANNER = "=" * 65

def run_model(name, run_fn, vec_A, vec_B, noise_pool):
    print(f"\n{BANNER}")
    print(f"  {name}")
    print(BANNER)
    results = sweep(run_fn, vec_A, vec_B, noise_pool)
    print_table(results)
    return results


if __name__ == "__main__":
    print("\n📦 ベクトルとノイズプールを準備中...")
    vec_A, vec_B, noise_pool = prepare_vectors()

    all_results = {}
    all_results["Model1_DampedOscillator"] = run_model(
        "Model 1: 減衰振動子 (Damped Harmonic Oscillator)", m1.run, vec_A, vec_B, noise_pool)
    all_results["Model2_Langevin"] = run_model(
        "Model 2: Langevin方程式", m2.run, vec_A, vec_B, noise_pool)
    all_results["Model3_FokkerPlanck"] = run_model(
        "Model 3: Fokker-Planck（離散近似）", m3.run, vec_A, vec_B, noise_pool)
    all_results["Model4_Lindblad"] = run_model(
        "Model 4: Lindbladモデル（散逸的シュレーディンガー）", m4.run, vec_A, vec_B, noise_pool)

    # 比較サマリー（Turn B=999 のみ）
    print(f"\n{BANNER}")
    print("  📊 比較サマリー（Turn B=999 = 最も最近の記憶）")
    print(BANNER)
    print(f"{'モデル':<35} | {'Score A (Turn1)':>16} | {'Score B (Turn999)':>17} | {'Ratio':>7}")
    print("-" * 80)
    for model_name, results in all_results.items():
        r = results[-1]  # 最後が Turn B=999
        sA, sB = r["score_A"], r["score_B"]
        ratio = sB / sA if sA != 0 else float("inf")
        print(f"{model_name:<35} | {sA:>16.6f} | {sB:>17.6f} | {ratio:>7.4f}")

    print(f"\n✅ 全モデル実験完了。experiment_results/ の各Markdownをご参照ください。")
