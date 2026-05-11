import numpy as np
import random

# --- Physics Engine (Inertial Langevin) ---
class LangevinMemory:
    def __init__(self, dim, mu=0.01, sigma=0.005, momentum=0.9):
        self.dim = dim
        self.state = np.zeros(dim)
        self.velocity = np.zeros(dim)
        self.mu = mu
        self.sigma = sigma
        self.momentum = momentum
    
    def update(self, v_in, alpha):
        drift = -self.mu * self.state
        diffusion = np.random.normal(0, self.sigma, self.dim)
        self.velocity = self.momentum * self.velocity + alpha * v_in
        self.state += drift + diffusion + self.velocity
        self._normalize()
        
    def _normalize(self):
        norm = np.linalg.norm(self.state)
        if norm > 0: self.state /= norm

# --- Semantic Space Setup ---
DIM = 384
np.random.seed(42)

def get_vector():
    v = np.random.normal(0, 1, DIM)
    return v / np.linalg.norm(v)

# 3 Distinct Contexts
CONTEXTS = {
    "A (Science)": get_vector(),
    "B (Cooking)": get_vector(),
    "C (Space)  ": get_vector()
}
NOISE_POOL = [get_vector() for _ in range(20)]

# --- Multi-Context Experiment ---
def run_multi_context_test(momentum_val):
    memory = LangevinMemory(DIM, momentum=momentum_val)
    results = []
    
    # Timeline
    # Step 0-9: Inject A
    # Step 10-19: Inject B
    # Step 20-29: Inject C
    # Step 30-100: Noise only
    
    for t in range(101):
        if 0 <= t < 10:
            memory.update(CONTEXTS["A (Science)"], alpha=0.1)
        elif 10 <= t < 20:
            memory.update(CONTEXTS["B (Cooking)"], alpha=0.1)
        elif 20 <= t < 30:
            memory.update(CONTEXTS["C (Space)  "], alpha=0.1)
        else:
            memory.update(random.choice(NOISE_POOL), alpha=0.01)
            
        # Record similarities to all 3 contexts
        sims = {name: np.dot(memory.state, v) for name, v in CONTEXTS.items()}
        results.append(sims)
        
    return results

# --- Main ---
print("Running Multi-Context Balance Experiment...")
print(f"Testing two cases: Low Momentum (0.0) vs High Momentum (0.9)\n")

for m_val in [0.0, 0.9]:
    print(f"=== Momentum: {m_val} ===")
    history = run_multi_context_test(m_val)
    
    print("Step | Context A | Context B | Context C | Status")
    print("-----|-----------|-----------|-----------|-------")
    # Sampling key timestamps
    checkpoints = [9, 19, 29, 50, 100]
    for t in checkpoints:
        s = history[t]
        status = ""
        if t == 9: status = "After A"
        if t == 19: status = "After B"
        if t == 29: status = "After C"
        if t == 100: status = "Final"
        print(f"{t:4d} | {s['A (Science)']:9.4f} | {s['B (Cooking)']:9.4f} | {s['C (Space)  ']:9.4f} | {status}")
    print("\n")

