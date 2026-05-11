"""
model4_lindblad.py
==================
Lindblad (散逸的シュレーディンガー) モデル

量子マスター方程式 (Lindblad形式)：
  dρ/dt = -i[H, ρ] + Σ_k (L_k·ρ·L_k† - ½{L_k†L_k, ρ})
        = ユニタリ進化  +  散逸（デコヒーレンス）

AIベクトルへの近似マッピング：
  ρ → 状態ベクトル v（密度行列の主固有ベクトル方向として近似）
  H  → 角振動数 Ω による回転作用（RoPE的）
    -i[H, v] ≈ Ω·v  （スキュー対称行列での回転）
  L_k→ デコヒーレンス作用子 — ここでは「振幅の減衰」として近似：
    Σ_k (L_k·v·L_k† - ½{L_k†L_k, v}) ≈ -γ_deco · v
  u(t) → 外部制御入力（新しい情報の注入）

離散化：
  v[t+1] = v[t]
           + Ω·v[t]·dt           (ユニタリ部分：回転)
           - γ_deco·v[t]·dt      (散逸部分：デコヒーレンス減衰)
           + u[t]                 (外部入力)

直感的解釈：
  「状態ベクトルは量子的に回転（コヒーレンス）しながら、
   同時に環境との相互作用によって振幅を失っていく（デコヒーレンス）。
   時間的非対称性は【回転の向き】と【散逸の両方向で生じる】。」
"""
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from shared_utils import prepare_vectors, sweep, print_table, DIM, TOTAL_TURNS
from experiment_log import log_experiment

GAMMA_DECO = 0.03   # デコヒーレンス強度
THETA_UNIT = 0.01   # ユニタリ部分の単位角速度
DT = 1.0

def _build_skew(dim, theta):
    """スキュー対称行列 Ω を構築（単純な2次元ペア回転の積み重ね）。"""
    Omega = np.zeros((dim, dim))
    half = dim // 2
    for i in range(half):
        freq = theta / (10000 ** (2 * i / dim))
        Omega[2*i,   2*i+1] = -freq
        Omega[2*i+1, 2*i]   =  freq
    return Omega

_Omega = _build_skew(DIM, THETA_UNIT)


class LindbladState:
    def __init__(self, dim=DIM):
        self.v = np.zeros(dim)

    def update(self, input_vec):
        # ユニタリ部分（回転）
        unitary = _Omega @ self.v * DT
        # 散逸部分（デコヒーレンス）
        dissipation = -GAMMA_DECO * self.v * DT
        self.v = self.v + unitary + dissipation + input_vec
        norm = np.linalg.norm(self.v)
        if norm > 0:
            self.v = self.v / norm

    def get_state(self):
        return self.v


def run(vec_A, vec_B, noise_pool, turn_B):
    state = LindbladState()
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
    print("=== Model 4: Lindbladモデル（散逸的シュレーディンガー方程式の近似） ===")
    print(f"γ_deco={GAMMA_DECO}, θ_unit={THETA_UNIT}, dt={DT}\n")
    vec_A, vec_B, noise_pool = prepare_vectors()
    results = sweep(run, vec_A, vec_B, noise_pool)
    print_table(results)
    log_experiment(
        model_name="Model4_Lindblad",
        description=(
            "Lindblad量子マスター方程式をベクトル近似。"
            "v[t+1] = v[t] + Ω·v·dt（回転）- γ_deco·v·dt（散逸）+ u[t]（入力）。"
            "コヒーレントな回転と非コヒーレントな散逸の競合を模倣。"
        ),
        params={"gamma_deco": GAMMA_DECO, "theta_unit": THETA_UNIT, "dt": DT, "total_turns": TOTAL_TURNS},
        results=results,
        conclusion="[実行後に追記]"
    )
