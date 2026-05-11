"""
model3_fokker_planck.py
=======================
Fokker-Planck方程式（離散近似）モデル

本来のFokker-Planck方程式：
  ∂p/∂t = -∂/∂v [F(v)·p] + D·∂²p/∂v²

これは確率分布 p(v, t) の時間発展を記述するPDE。
各ターンで「現在の確率分布」が更新されていく。

近似的なアプローチ：
  状態ベクトルを「確率分布の期待値（重み付き平均）」として扱い、
  各ターンで新しい入力が到達した際に指数移動平均（EMA）で更新する。

  v[t+1] = α·v[t] + (1-α)·u[t]   (平滑化)
  + D·(v_ref - v[t])·dt           (拡散：基準状態への引き戻し項)

直感的解釈：
  「確率雲の重心が、新しい情報の方向へゆっくりシフトし、
   同時に拡散項によってゆっくりと均一（entropy増大）に向かう。
   これが情報の〈自然な忘却〉の物理的なメカニズム。」
"""
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from shared_utils import prepare_vectors, sweep, print_table, DIM, TOTAL_TURNS
from experiment_log import log_experiment

ALPHA = 0.97    # EMA平滑化係数（過去の保持率）
D     = 0.003   # 拡散係数
DT    = 1.0

class FokkerPlanckState:
    def __init__(self, dim=DIM):
        self.v = np.zeros(dim)
        self.v_ref = np.zeros(dim)   # 拡散の「引力中心」（初期は原点）

    def update(self, input_vec):
        # EMA更新（新しい情報へのドリフト）
        self.v = ALPHA * self.v + (1 - ALPHA) * input_vec
        # 拡散項（v_refに向けてゆっくり揺り戻し）
        self.v = self.v + D * (self.v_ref - self.v) * DT
        norm = np.linalg.norm(self.v)
        if norm > 0:
            self.v = self.v / norm

    def get_state(self):
        return self.v


def run(vec_A, vec_B, noise_pool, turn_B):
    state = FokkerPlanckState()
    for i in range(1, TOTAL_TURNS + 1):
        if i == 1:
            state.update(vec_A)
        elif i == turn_B:
            state.update(vec_B)
        else:
            state.update(noise_pool[i-1])
    final = state.get_state()
    return (cosine_similarity([final], [vec_A])[0][0],
            cosine_similarity([final], [vec_B])[0][0])


if __name__ == "__main__":
    print("=== Model 3: Fokker-Planck方程式（離散近似） ===")
    print(f"α={ALPHA}, D={D}, dt={DT}\n")
    vec_A, vec_B, noise_pool = prepare_vectors()
    results = sweep(run, vec_A, vec_B, noise_pool)
    print_table(results)
    log_experiment(
        model_name="Model3_FokkerPlanck",
        description=(
            "EMA + 拡散項でFokker-Planck PDEを近似。"
            "v[t+1] = α·v[t] + (1-α)·u[t] + D·(v_ref - v[t])·dt。"
            "確率分布の重心が新しい情報へドリフトしながら、拡散で均一化されていく。"
        ),
        params={"alpha": ALPHA, "D": D, "dt": DT, "total_turns": TOTAL_TURNS},
        results=results,
        conclusion="[実行後に追記]"
    )
