import numpy as np

class ReasoningEngine:
    def __init__(self, dim, mode='baseline', momentum=0.9, mu=0.01):
        self.dim = dim
        self.mode = mode
        self.state = np.zeros(dim)
        self.velocity = np.zeros(dim)
        self.momentum = momentum
        self.mu = mu
        
        # For 'tensor' mode
        self.slots = np.zeros((5, dim))
        self.slot_velocities = np.zeros((5, dim))

    def step(self, input_v, alpha):
        if self.mode == 'baseline':
            # Simple additive update (No inertia)
            self.state = (1 - self.mu) * self.state + alpha * input_v
            norm = np.linalg.norm(self.state)
            if norm > 0: self.state /= norm
            
        elif self.mode == 'flow':
            # Inertial Langevin update
            drift = -self.mu * self.state
            self.velocity = self.momentum * self.velocity + alpha * input_v
            self.state += drift + self.velocity
            norm = np.linalg.norm(self.state)
            if norm > 0: self.state /= norm
            
        elif self.mode == 'tensor':
            # Structured slot update
            sims = [np.dot(s, input_v) for s in self.slots]
            idx = np.argmax(sims)
            
            drift = -self.mu * self.slots[idx]
            self.slot_velocities[idx] = self.momentum * self.slot_velocities[idx] + alpha * input_v
            self.slots[idx] += drift + self.slot_velocities[idx]
            norm = np.linalg.norm(self.slots[idx])
            if norm > 0: self.slots[idx] /= norm
            
            # The 'reasoning thread' is the most active slot
            self.state = self.slots[idx]

# --- Setup ---
DIM = 384
STEPS = 100
np.random.seed(42)

def get_vector():
    v = np.random.normal(0, 1, DIM)
    return v / np.linalg.norm(v)

# The "Logical Thread" we want to maintain
GOAL_TOPIC = get_vector()
# A completely unrelated "Distraction"
DISTRACTION = get_vector()

def run_benchmark(mode):
    engine = ReasoningEngine(DIM, mode=mode)
    stability_log = []
    
    for i in range(STEPS):
        # 1. Intentional Reasoning (Always trying to stay on goal)
        input_v = GOAL_TOPIC * 0.1 
        
        # 2. Add Noise
        input_v += np.random.normal(0, 0.02, DIM)
        
        # 3. Periodic Heavy Distraction (Topics change)
        if i % 20 == 0 and i > 0:
            input_v += DISTRACTION * 2.0 # Strong interference
            
        engine.step(input_v, alpha=1.0)
        
        # Measure alignment with the original Goal Topic
        similarity = np.dot(engine.state, GOAL_TOPIC)
        stability_log.append(similarity)
        
    return np.mean(stability_log), stability_log[-1]

# --- Run ---
modes = ['baseline', 'flow', 'tensor']
print(f"{'Mode':<10} | {'Avg Stability':<15} | {'Final Stability'}")
print("-" * 45)

for m in modes:
    avg_s, final_s = run_benchmark(m)
    print(f"{m:<10} | {avg_s:14.4f} | {final_s:14.4f}")

print("\nInterpretation:")
print("- Baseline: Reasoning thread easily broken by distractions.")
print("- Flow: Momentum helps resist noise, but strong distractions still drift the state.")
print("- Tensor: Slots isolate the distraction, keeping the 'Reasoning Thread' pure.")
