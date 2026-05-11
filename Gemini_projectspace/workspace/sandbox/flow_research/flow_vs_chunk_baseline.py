import numpy as np

# --- Physics Engine (Phase 18 Langevin Baseline) ---
class LangevinMemory:
    def __init__(self, dim, mu=0.01, sigma=0.01, momentum=0.9):
        self.dim = dim
        self.state = np.zeros(dim)
        self.velocity = np.zeros(dim)
        self.mu = mu
        self.sigma = sigma
        self.momentum = momentum
    
    def update(self, v_in, alpha):
        # Drift towards origin (Forgetting)
        drift = -self.mu * self.state
        # Diffusion (Noise)
        diffusion = np.random.normal(0, self.sigma, self.dim)
        
        # Injection affects Velocity first (Inertia)
        self.velocity = self.momentum * self.velocity + alpha * v_in
        
        # Update State using Velocity
        self.state += drift + diffusion + self.velocity
        self._normalize()
        
    def _normalize(self):
        norm = np.linalg.norm(self.state)
        if norm > 0:
            self.state /= norm

# --- Mock Semantic Space ---
np.random.seed(42)
DIM = 384

def get_random_vector():
    v = np.random.normal(0, 1, DIM)
    return v / np.linalg.norm(v)

# Target meaning (The fact we want to keep)
TARGET_V = get_random_vector()
# Background noise (Random topics)
NOISE_POOL = [get_random_vector() for _ in range(50)]

# --- Experiment Simulation ---
def run_experiment(method="chunk", steps=100):
    memory = LangevinMemory(DIM, mu=0.01, sigma=0.005)
    history = []
    
    # 1. Initial Injection of Target
    if method == "chunk":
        # One big injection
        memory.update(TARGET_V, alpha=0.5)
        history.append(np.dot(memory.state, TARGET_V))
    else:
        # Flow: 5 small continuous injections (representing a stream of thought)
        for _ in range(5):
            memory.update(TARGET_V, alpha=0.1)
            history.append(np.dot(memory.state, TARGET_V))
            
    # 2. Noise Injection (The "Regression" Phase)
    for i in range(steps):
        noise_v = NOISE_POOL[np.random.randint(0, 50)]
        memory.update(noise_v, alpha=0.01)
        history.append(np.dot(memory.state, TARGET_V))
        
    return history

# --- Main Execution ---
print("Starting Flow vs Chunk Experiment...")

steps = 100
history_chunk = run_experiment(method="chunk", steps=steps)
history_flow = run_experiment(method="flow", steps=steps)

# Output summary to console
print("\n--- Experiment Results ---")
print(f"Final Retention (Chunk): {history_chunk[-1]:.4f}")
print(f"Final Retention (Flow):  {history_flow[-1]:.4f}")

# Simple ASCII Chart
print("\nRetention Trend (every 20 steps):")
print("Step | Chunk  | Flow")
print("-----|--------|-------")
for i in range(0, steps + 1, 20):
    c = history_chunk[i] if i < len(history_chunk) else history_chunk[-1]
    f = history_flow[i] if i < len(history_flow) else history_flow[-1]
    print(f"{i:4d} | {c:.4f} | {f:.4f}")

if history_flow[-1] > history_chunk[-1]:
    print("\nResult: Flow method shows better retention stability!")
else:
    print("\nResult: Chunk method is dominant in this baseline.")
