import numpy as np
import random

# --- Tensor Structured Memory ---
class TensorContextMemory:
    def __init__(self, num_slots, dim, mu=0.01, momentum=0.9):
        self.num_slots = num_slots
        self.dim = dim
        self.slots = np.zeros((num_slots, dim))
        self.velocities = np.zeros((num_slots, dim))
        self.mu = mu
        self.momentum = momentum
        
    def update(self, v_in, alpha):
        # 1. Find the most relevant slot (Attention-like)
        similarities = np.dot(self.slots, v_in)
        target_slot = np.argmax(similarities)
        
        # If the best similarity is too low, we might need a new slot 
        # (For this experiment, we just update the best match or use a simple rotation)
        
        # 2. Update the specific slot with Momentum
        drift = -self.mu * self.slots[target_slot]
        self.velocities[target_slot] = self.momentum * self.velocities[target_slot] + alpha * v_in
        self.slots[target_slot] += drift + self.velocities[target_slot]
        
        # Normalize the updated slot
        norm = np.linalg.norm(self.slots[target_slot])
        if norm > 0: self.slots[target_slot] /= norm

    def get_global_state(self):
        # Weighted sum of slots (for overall context)
        combined = np.mean(self.slots, axis=0)
        norm = np.linalg.norm(combined)
        return combined / norm if norm > 0 else combined

# --- Experiment Setup ---
DIM = 384
NUM_SLOTS = 10
np.random.seed(42)

def get_vector():
    v = np.random.normal(0, 1, DIM)
    return v / np.linalg.norm(v)

# Generate 10 distinct topics
TOPICS = [get_vector() for _ in range(10)]

def run_experiment(use_tensor):
    if use_tensor:
        memory = TensorContextMemory(num_slots=NUM_SLOTS, dim=DIM)
    else:
        # Baseline: Single slot memory (equivalent to our previous experiments)
        memory = TensorContextMemory(num_slots=1, dim=DIM)
        
    # Inject 10 topics sequentially
    for i, v in enumerate(TOPICS):
        # 5 steps of flow injection for each topic
        for _ in range(5):
            memory.update(v, alpha=0.1)
            
    # Final check: How many topics are still "recognizable"?
    found_count = 0
    print(f"{'Topic':<10} | {'Max Slot Sim':<15} | {'Global Sim':<15}")
    print("-" * 45)
    
    for i, target_v in enumerate(TOPICS):
        if use_tensor:
            # Check all slots
            max_sim = np.max(np.dot(memory.slots, target_v))
        else:
            max_sim = np.dot(memory.slots[0], target_v)
            
        global_sim = np.dot(memory.get_global_state(), target_v)
        
        print(f"Topic {i:2d}   | {max_sim:14.4f} | {global_sim:14.4f}")
        if max_sim > 0.5: found_count += 1
        
    return found_count

# --- Run ---
print("=== Experiment: Single Vector Memory (Baseline) ===")
count_base = run_experiment(use_tensor=False)
print(f"\nRecognizable Topics: {count_base} / 10\n")

print("=== Experiment: Tensor Structured Memory (10 Slots) ===")
count_tensor = run_experiment(use_tensor=True)
print(f"\nRecognizable Topics: {count_tensor} / 10\n")
