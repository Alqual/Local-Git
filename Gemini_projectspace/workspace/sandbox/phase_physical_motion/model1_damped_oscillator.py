"""
model1_damped_oscillator.py
============================
減衰振動子モデル (Damped Harmonic Oscillator)

運動方程式：
  dv/dt = w  (speedベクトル)
  dw/dt = -γ·w - ω²·v + u(t)  (力=減衰力+復元力+入力)

離散化 (Euler法)：
  w[t+1] = w[t] - γ·w[t]·dt - ω²·v[t]·dt + u[t]
  v[t+1] = v[t] + w[t]·dt

直感的解釈：
  「状態ベクトルはバネ（復元力）で原点付近に引き戻され、
   粘性（γ）によってエネルギーを失いながら振動する。
   新しい入力は外力として波を押し起こす。」
  → 駆動力のない次元は指数減衰しながら振動して消える（非対称・非可逆）。
"""
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from shared_utils import prepare_vectors, sweep, print_table, DIM, TOTAL_TURNS
from experiment_log import log_experiment

GAMMA = 0.05   # 減衰係数（大きいほど早く忘れる）
OMEGA2 = 0.01  # 復元力の強さ（大きいほど激しく振動）
DT = 1.0       # 離散時間ステップ

class DampedOscillatorState:
    def __init__(self, dim=DIM):
        self.v = np.zeros(dim)   # 位置（状態ベクトル）
        self.w = np.zeros(dim)   # 速度ベクトル

    def update(self, input_vec):
        # Euler積分：速度を先に更新してから位置を更新
        self.w = self.w - GAMMA * self.w * DT - OMEGA2 * self.v * DT + input_vec
        self.v = self.v + self.w * DT
        norm = np.linalg.norm(self.v)
        if norm > 0:
            self.v = self.v / norm

    def get_state(self):
        return self.v


def run(vec_A, vec_B, noise_pool, turn_B):
    state = DampedOscillatorState()
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
    print("=== Model 1: 減衰振動子 (Damped Harmonic Oscillator) ===")
    print(f"γ={GAMMA}, ω²={OMEGA2}, dt={DT}\n")
    vec_A, vec_B, noise_pool = prepare_vectors()
    results = sweep(run, vec_A, vec_B, noise_pool)
    print_table(results)
    log_experiment(
        model_name="Model1_DampedOscillator",
        description=(
            "dv/dt=w, dw/dt=-γw-ω²v+u(t) をEuler法で離散化。"
            "バネ（復原力）と粘性（減衰）の組み合わせで状態を振動させながら忘却させる。"
        ),
        params={"gamma": GAMMA, "omega_sq": OMEGA2, "dt": DT, "total_turns": TOTAL_TURNS},
        results=results,
        conclusion="[実行後に追記]"
    )
