import numpy as np
import random

class DynamicTensorMemory:
    def __init__(self, dim, max_slots=10, threshold=0.4, mu=0.01, momentum=0.9):
        self.dim = dim
        self.max_slots = max_slots
        self.threshold = threshold
        self.mu = mu
        self.momentum = momentum
        
        self.slots = [] # List of vectors
        self.velocities = [] # List of momentum vectors
        self.last_used = [] # Timestamps or usage count
        
    def update(self, v_in, alpha, current_time):
        if not self.slots:
            self._add_slot(v_in, alpha, current_time)
            return
            
        similarities = [np.dot(s, v_in) for s in self.slots]
        max_sim = np.max(similarities)
        best_idx = np.argmax(similarities)
        
        if max_sim > self.threshold:
            # Update existing slot
            self._update_slot(best_idx, v_in, alpha)
            self.last_used[best_idx] = current_time
        else:
            # Too different -> Create new slot
            if len(self.slots) < self.max_slots:
                self._add_slot(v_in, alpha, current_time)
            else:
                # Memory full -> Evict the "weakest" slot
                energies = [np.linalg.norm(v) for v in self.velocities]
                evict_idx = np.argmin(energies)
                self._replace_slot(evict_idx, v_in, alpha)
                self.last_used[evict_idx] = current_time
                
    def _add_slot(self, v_in, alpha, current_time):
        self.slots.append(np.zeros(self.dim))
        self.velocities.append(alpha * v_in)
        self.slots[-1] = self.velocities[-1] / np.linalg.norm(self.velocities[-1])
        self.last_used.append(current_time)
        
    def _update_slot(self, idx, v_in, alpha):
        drift = -self.mu * self.slots[idx]
        self.velocities[idx] = self.momentum * self.velocities[idx] + alpha * v_in
        self.slots[idx] += drift + self.velocities[idx]
        norm = np.linalg.norm(self.slots[idx])
        if norm > 0: self.slots[idx] /= norm
        
    def _replace_slot(self, idx, v_in, alpha):
        # Reset velocity and set new direction
        self.velocities[idx] = alpha * v_in
        self.slots[idx] = v_in # Hard replace

# --- Experiment: Scaling to 20 Topics with only 5 Slots ---
DIM = 384
MAX_SLOTS = 5
TOPICS_COUNT = 20
np.random.seed(42)

def get_vector():
    v = np.random.normal(0, 1, DIM)
    return v / np.linalg.norm(v)

TOPICS = [get_vector() for _ in range(TOPICS_COUNT)]
memory = DynamicTensorMemory(DIM, max_slots=MAX_SLOTS)

print(f"Injecting {TOPICS_COUNT} topics into {MAX_SLOTS} slots dynamically...\n")

for i, v in enumerate(TOPICS):
    # Inject each topic for 5 steps
    for _ in range(5):
        memory.update(v, alpha=0.1, current_time=i)

# Evaluation
print(f"{'Topic':<10} | {'Max Slot Sim':<15} | {'Status'}")
print("-" * 40)
found = 0
for i, target_v in enumerate(TOPICS):
    sims = [np.dot(s, target_v) for s in memory.slots]
    max_sim = np.max(sims)
    status = "RETAINED" if max_sim > 0.6 else "LOST"
    if status == "RETAINED": found += 1
    print(f"Topic {i:2d}   | {max_sim:14.4f} | {status}")

print(f"\nFinal Capacity Result: {found} / {TOPICS_COUNT} topics retained in {MAX_SLOTS} slots.")
