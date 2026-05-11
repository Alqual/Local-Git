"""
model2_langevin.py
==================
Langevin方程式モデル

運動方程式：
  dv/dt = -μ·v + σ·ξ(t) + u(t)

  -μ·v  : ドリフト（勾配降下・摩擦）—— 状態を原点に引き戻す
  σ·ξ(t): 拡散ノイズ（熱的揺らぎ）—— ブラウン運動の模倣
  u(t)  : 制御入力（新しいベクトル）

離散化：
  v[t+1] = v[t] - μ·v[t]·dt + σ·√dt·ξ[t] + u[t]

直感的解釈：
  「状態ベクトルは常にゆっくり原点へ向かって引き寄せられ（摩擦）、
   かつ常にランダムな揺らぎを受けている（熱的ノイズ）。
   外部入力が来たときだけ、その方向へ大きく揺れる。」
  → 統計力学的な定常分布（Boltzmann分布類似）への収束が起こる。
"""
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from shared_utils import prepare_vectors, sweep, print_table, DIM, TOTAL_TURNS
from experiment_log import log_experiment

MU    = 0.05   # ドリフト係数（摩擦の強さ）
SIGMA = 0.02   # 拡散係数（熱的ノイズの強さ）
DT    = 1.0

class LangevinState:
    def __init__(self, dim=DIM, seed=0):
        self.v = np.zeros(dim)
        self.rng = np.random.default_rng(seed)

    def update(self, input_vec):
        noise = self.rng.standard_normal(len(self.v))
        self.v = (self.v
                  - MU * self.v * DT
                  + SIGMA * np.sqrt(DT) * noise
                  + input_vec)
        norm = np.linalg.norm(self.v)
        if norm > 0:
            self.v = self.v / norm

    def get_state(self):
        return self.v


def run(vec_A, vec_B, noise_pool, turn_B):
    state = LangevinState()
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
    print("=== Model 2: Langevin方程式 ===")
    print(f"μ={MU}, σ={SIGMA}, dt={DT}\n")
    vec_A, vec_B, noise_pool = prepare_vectors()
    results = sweep(run, vec_A, vec_B, noise_pool)
    print_table(results)
    log_experiment(
        model_name="Model2_Langevin",
        description=(
            "dv/dt = -μv + σξ(t) + u(t) を離散化。"
            "摩擦（ドリフト）と熱的ノイズ（拡散）の競合が生じる確率的運動モデル。"
        ),
        params={"mu": MU, "sigma": SIGMA, "dt": DT, "total_turns": TOTAL_TURNS},
        results=results,
        conclusion="[実行後に追記]"
    )
