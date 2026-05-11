from sentence_transformers import SentenceTransformer
from quantum_bridge import ClassicalToQuantumBridge
import os
import random
import logging

os.environ["TOKENIZERS_PARALLELISM"] = "false"
logging.getLogger("sentence_transformers").setLevel(logging.WARNING)

print("Loading Embedding Model (all-MiniLM-L6-v2) ...")
embedder = SentenceTransformer("all-MiniLM-L6-v2")
bridge = ClassicalToQuantumBridge(embedder)

print("\n=======================================================")
print(" Phase 17: KV Cache to Quantum Bridge - Sandbox Test ")
print("=======================================================\n")

# 1. 昔の重要な事実を転送 (KVキャッシュから溢れたと想定)
print("1. Simulating Turn 1: Important fact overflows from KV cache to Quantum Layer...")
target_fact = ["The secret code to bypass the firewall is 'ZETA-99'."]
bridge.transfer_to_quantum(target_fact, is_signal=True)

# 2. 100ターンの雑談でKVキャッシュが何度も上書きされるのを模倣
print("\n2. Simulating Turn 2-100: 100 turns of background chatter noise overflowing to Quantum Layer...")
print("   (These are injected with low dynamic alpha α=0.01)")
subjects = ["weather", "science", "music", "travel", "history", "cats", "movies", "cooking", "sports", "gaming"]
for i in range(100):
    noise_sentence = f"Chatter noise: User and Assistant discussing casually about {random.choice(subjects)}."
    bridge.transfer_to_quantum([noise_sentence], is_signal=False)

print(f"\n[Status] Total sentences stored in Bridge Archive: {len(bridge.archive.texts)}")

# 3. ユーザーの新しいクエリが来る
user_query = "Wait, what was the firewall bypass code we talked about a long time ago?"
print(f"\n3. User Query arrived: '{user_query}'")
print("   Injecting query into Quantum Layer as strong signal (α=0.50)...")
bridge.process_query(user_query)

# 4. 量子層からの抽出 (Collapse)
print("\n4. Collapsing Quantum Layer (Extracting highly resonated context for the LLM prompt)...")
retrieved = bridge.collapse(top_k=3)

print("\n--- Collapse Results (Top 3) ---")
for i, res in enumerate(retrieved):
    is_target = "ZETA-99" in res['text']
    marker = ">> TARGET FOUND <<" if is_target else "Background Noise"
    print(f"Rank {i+1} [Score: {res['score']:.4f}] {marker}")
    print(f"      Text: {res['text']}\n")

if any("ZETA-99" in r['text'] for r in retrieved):
    print("\nSUCCESS: Target fact successfully recovered from Quantum Layer despite 100 turns of noise interference!")
else:
    print("\nFAILURE: Target fact was lost or overshadowed by noise.")
