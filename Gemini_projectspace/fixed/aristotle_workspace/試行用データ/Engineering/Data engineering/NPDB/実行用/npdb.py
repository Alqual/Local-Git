
import json
import time
import math
import random
from datetime import datetime
from typing import Dict, List, Any, Optional

class Synapse:
    """
    ニューロン間の接続（シナプス）。
    重み（Weight）を持ち、可塑性（強化・減衰）を管理する。
    """
    def __init__(self, target_id: str, weight: float = 0.5):
        self.target_id = target_id
        self.weight = weight
        self.last_activated = time.time()

    def strengthen(self, amount: float = 0.1):
        """ヘッブ学習：結合を強化する"""
        self.weight = min(1.0, self.weight + amount)
        self.last_activated = time.time()

    def decay(self, decay_rate: float):
        """忘却：時間経過により結合を弱める"""
        # 単純な減算ではなく、現在の重みに比例して減衰させる
        self.weight *= (1.0 - decay_rate)

class Neuron:
    """
    データの格納単位（ニューロン）。
    データ本体と、他のニューロンへのシナプス結合を持つ。
    """
    def __init__(self, _id: str, content: Dict[str, Any]):
        self.id = _id
        self.content = content
        # target_id -> Synapse
        self.synapses: Dict[str, Synapse] = {}
        self.activation_level = 0.0

    def connect(self, target_id: str, initial_weight: float = 0.3):
        if target_id not in self.synapses:
            self.synapses[target_id] = Synapse(target_id, initial_weight)
        else:
            self.synapses[target_id].strengthen()

    def prune_synapses(self, threshold: float = 0.1):
        """閾値を下回った弱い結合を削除する（忘却の実装）"""
        to_remove = [tid for tid, syn in self.synapses.items() if syn.weight < threshold]
        for tid in to_remove:
            del self.synapses[tid]

class NeuroPlasticDB:
    """
    Neuro-Plastic Database (NPDB) Engine.
    """
    def __init__(self, decay_rate: float = 0.05, prune_threshold: float = 0.1):
        self.neurons: Dict[str, Neuron] = {}
        self.decay_rate = decay_rate
        self.prune_threshold = prune_threshold
        self.logs = []

    def log(self, message: str):
        timestamp = datetime.now().strftime("%H:%M:%S")
        self.logs.append(f"[{timestamp}] {message}")
        print(f"[{timestamp}] {message}")

    def insert(self, _id: str, content: Dict[str, Any]):
        """データを挿入（ニューロン生成）"""
        if _id in self.neurons:
            self.log(f"Update existing neuron: {_id}")
            self.neurons[_id].content = content
        else:
            self.neurons[_id] = Neuron(_id, content)
            self.log(f"Created neuron: {_id}")

    def query(self, query_key: str, query_value: Any, auto_connect: bool = True) -> List[Dict]:
        """
        検索を行い、結果に関連するニューロン間の結合を強化する。
        """
        self.log(f"Querying: {query_key} = {query_value}")
        
        # 1. 直接マッチするニューロンを探す（リレーショナル層的な検索）
        fired_neurons = []
        for nid, neuron in self.neurons.items():
            if neuron.content.get(query_key) == query_value:
                fired_neurons.append(neuron)

        # 2. 関連性検索（Spreading Activation: 活性化拡散）
        # ヒットしたニューロンから強く結合しているニューロンも「連想」として引き出す
        associated_neurons = []
        for neuron in fired_neurons:
            # 自身の活性化
            neuron.activation_level = 1.0
            
            # シナプス経由で拡散
            for target_id, synapse in neuron.synapses.items():
                if synapse.weight > 0.5: # 強い結合のみ連想する
                    target = self.neurons.get(target_id)
                    if target and target not in fired_neurons:
                        associated_neurons.append(target)
                        self.log(f"  -> Associated found: {target.id} (Weight: {synapse.weight:.2f})")

        # 3. ヘッブ学習 (Hebbian Learning)
        # 今回のクエリで同時に発火した（検索ヒットした）ニューロン同士を結合する
        if auto_connect and len(fired_neurons) > 1:
            self.log("Hebbian Learning triggered: Strengthening connections between fired neurons.")
            for i in range(len(fired_neurons)):
                for j in range(i + 1, len(fired_neurons)):
                    n1 = fired_neurons[i]
                    n2 = fired_neurons[j]
                    n1.connect(n2.id)
                    n2.connect(n1.id)

        # 結果をまとめる
        results = [n.content for n in fired_neurons] + [n.content for n in associated_neurons]
        
        # 重複排除のみ（辞書のリストなので簡易的に）
        # 実用レベルではID管理するが、ここでは簡易化
        unique_results = []
        seen_ids = set()
        for r in results:
            if r['id'] not in seen_ids:
                unique_results.append(r)
                seen_ids.add(r['id'])

        return unique_results

    def sleep_cycle(self):
        """
        睡眠サイクル（メンテナンス処理）。
        全体の減衰（忘却）と剪定（Pruning）を行う。
        """
        self.log("Starting Sleep Cycle (Consolidation & Forgetting)...")
        initial_synapse_count = sum(len(n.synapses) for n in self.neurons.values())
        
        for neuron in self.neurons.values():
            for synapse in neuron.synapses.values():
                synapse.decay(self.decay_rate)
            neuron.prune_synapses(self.prune_threshold)
            
        final_synapse_count = sum(len(n.synapses) for n in self.neurons.values())
        pruned_count = initial_synapse_count - final_synapse_count
        self.log(f"Sleep Cycle finished. Pruned {pruned_count} weak connections.")

    def visualize_stats(self):
        """現在のDBの統計情報を表示"""
        total_neurons = len(self.neurons)
        total_synapses = sum(len(n.synapses) for n in self.neurons.values())
        avg_synapses = total_synapses / total_neurons if total_neurons > 0 else 0
        
        print("\n--- NPDB Status ---")
        print(f"Total Neurons: {total_neurons}")
        print(f"Total Synapses: {total_synapses}")
        print(f"Avg Connectivity: {avg_synapses:.2f}")
        print("-------------------")

# テスト用実行ブロック
if __name__ == "__main__":
    db = NeuroPlasticDB(decay_rate=0.2, prune_threshold=0.3)

    # データ投入
    print("\n[Phase 1] Data Injection")
    db.insert("apple", {"id": "apple", "scent": "fruity", "color": "red", "category": "fruit"})
    db.insert("banana", {"id": "banana", "scent": "fruity", "color": "yellow", "category": "fruit"})
    db.insert("cherry", {"id": "cherry", "scent": "fruity", "color": "red", "category": "fruit"})
    db.insert("fire_truck", {"id": "fire_truck", "scent": "diesel", "color": "red", "category": "vehicle"})
    
    # 検索1: 'red' を検索
    # apple, cherry, fire_truck がヒットするはず。これらは互いに結合される。
    print("\n[Phase 2] Query 'red' (Learning Context)")
    db.query("color", "red")
    db.visualize_stats()

    # 検索2: 'fruit' を検索
    # apple, banana, cherry がヒット。
    print("\n[Phase 3] Query 'fruit' (Learning Context)")
    db.query("category", "fruit")
    db.visualize_stats()

    # ここで 'apple' は 'cherry' と2回共起している（red, fruit）ので結合が強いはず
    # 'apple' と 'fire_truck' は1回（red）のみ
    
    # 時間経過（忘却）
    print("\n[Phase 4] Sleep Cycle (Forgetting)")
    db.sleep_cycle()
    db.visualize_stats()

    # 検索3: 連想テスト
    # 'apple' を指定して、何もクエリ条件なしで「関連するもの」が出るか？（ID検索のエミュレーション）
    # ※本実装では簡易的に connect メソッドの結果を見る
    print("\n[Phase 5] Inspecting 'apple' connections")
    apple = db.neurons["apple"]
    for target_id, synapse in apple.synapses.items():
        print(f"  - Linked to {target_id}: Strength {synapse.weight:.2f}")

