
from npdb_v2 import NeuroPlasticDB_V2, run_benchmark
import time
import random

def run_test_small():
    print("Initializing DB...")
    db = NeuroPlasticDB_V2()
    
    # 1. Access Insert
    print("Inserting 500 items...")
    t0 = time.time()
    for i in range(500):
        uid = f"item_{i}"
        cat = "A" if i % 2 == 0 else "B"
        db.insert(uid, {"id": uid, "cat": cat, "val": i})
    print(f"Insertion done in {time.time()-t0:.4f}s")

    # 2. Query Speed (In-Memory Index)
    print("Querying cat='A'...")
    t0 = time.time()
    res = db.query("cat", "A")
    print(f"Query found {len(res)} items in {(time.time()-t0)*1000:.4f}ms")
    
    # 3. LTM Test
    print("Sleeping to force Memory Consolidation (STM -> LTM)...")
    # Force expiry by setting timestamps to old
    for nid in db.stm:
        db.stm[nid].last_accessed = time.time() - 100
    
    db.sleep_cycle(ttl_seconds=1.0)
    
    print(f"STM size after sleep: {len(db.stm)} (Should be 0)")
    
    # 4. Recall Test
    print("Recalling item_0 from LTM...")
    t0 = time.time()
    item = db._get_neuron("item_0")
    print(f"Recall time: {(time.time()-t0)*1000:.4f}ms")
    print(f"Recalled Data: {item.content}")

if __name__ == "__main__":
    run_test_small()
