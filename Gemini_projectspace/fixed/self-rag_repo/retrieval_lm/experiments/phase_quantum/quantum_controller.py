import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from small_lm_engine import StatelessSmallLM

class QuantumState:
    def __init__(self, vector_dim=384):
        self.state_vector = np.zeros(vector_dim)
        
    def update(self, input_vector, alpha=0.5):
        # 以前の減衰モデルだと20回の対話で古い記憶が消えてしまう（指数関数的崩壊）ため、
        # 量子論的な「純粋な重ね合わせ（足し合わせと正規化）」に切り替え、
        # 長期コンテキストに対しても情報が等価に残存するように改定します。
        self.state_vector = self.state_vector + input_vector
        
        norm = np.linalg.norm(self.state_vector)
        if norm > 0:
            self.state_vector = self.state_vector / norm
            
    def get_state(self):
        return self.state_vector

class QuantumController:
    def __init__(self, embed_model_name="all-MiniLM-L6-v2"):
        print("[*] Loading Quantum Components (Embedding)...")
        self.quantizer = SentenceTransformer(embed_model_name)
        self.q_state = QuantumState(vector_dim=self.quantizer.get_sentence_embedding_dimension())
        self.engine = StatelessSmallLM()
        
        # 実験用: 意図的に巨大なナレッジ/履歴空間を用意（古典的LLMならAttentionが死ぬレベル）
        self.knowledge_space = [
            "東京タワーの高さは333メートルです。",
            "宇宙の年齢は約138億年と推定されています。",
            "TackはPythonとAIアーキテクチャに熱心な優秀なエンジニアです。",
            "Tackの大好物は焼肉です。",
            "富士山は日本で最も高い山で、標高は3776メートルです。"
        ]
        # 大量のノイズ（意味論的な邪魔）を追加注入
        for i in range(1, 51):
            self.knowledge_space.append(f"ダミーの無関係な事実その{i}: ペンギンは空を飛べないが海を泳ぐ速度は時速30kmに達することがある。")
            self.knowledge_space.append(f"ダミー事実{i}B: 太陽系第{i % 8 + 1}惑星についての観測データファイル。")
            
        print(f"[*] Quantizing Massive Knowledge Space ({len(self.knowledge_space)} entries)...")
        self.knowledge_vectors = self.quantizer.encode(self.knowledge_space)

    def interact(self, user_input: str):
        print(f"\n--- [Quantum Controller] User Event: '{user_input}' ---")
        
        input_vector = self.quantizer.encode([user_input])[0]
        self.q_state.update(input_vector, alpha=1.0) # alphaは不使用に変更
        
        # 観測 (Measurement)
        current_state = self.q_state.get_state()
        similarities = cosine_similarity([current_state], self.knowledge_vectors)[0]
        
        # 最も確率の高い情報を上位2つだけ抽出
        top_k_indices = similarities.argsort()[-2:][::-1]
        
        collapsed_context = ""
        for idx in top_k_indices:
            # 巨大なリストからピンポイントで抽出されるか確認
            collapsed_context += f"- {self.knowledge_space[idx]}\n"
                
        # SLMへ渡すプロンプト長は「常に固定かつ超短文」に保たれる
        prompt = f"Collapsed Knowledge State:\n{collapsed_context}\nUser Input: {user_input}\nAssistant: "
            
        system_prompt = (
            "You are an assistant connected to a quantum-semantic memory space. "
            "Use ONLY the 'Collapsed Knowledge State' to answer the User Input. "
            "Keep the answer very short."
        )
        
        print("\n[Quantum Controller] --------- Measurement ----------")
        print(f"SLMに送信される確定プロンプト（長さは一切増大しない）:\n{prompt.strip()}")
        print("---------------------------------------------------")
        
        response = self.engine.generate_response(prompt, system_prompt=system_prompt, max_new_tokens=50)
        response = response.strip()
        print(f"\n[Engine Output]: {response}")
        
        answer_vector = self.quantizer.encode([response])[0]
        self.q_state.update(answer_vector, alpha=1.0)

if __name__ == "__main__":
    print("=== Initializing Quantum Controller Prototype ===")
    controller = QuantumController()
    
    print("\n================ PHASE 5: MASSIVE CONTEXT TEST ================")
    
    print("【実験背景】")
    print("古典的ステートマシンでは、100個以上の無関係なやり取り（ノイズ）があれば")
    print("LLMへ渡すテキストバッファが数万トークンに膨れ上がり、Attention崩壊を起こします。")
    print("今回は100以上のダミーノイズプールを持つ空間で、状態ベクトルが破綻せずに")
    print("固定サイズの超短文プロンプトとして意味をCollapse（抽出）できるか検証します。")
    
    print("\n>>> Turn 1: 遠い過去のノイズに埋もれた情報を質問")
    controller.interact("Tackとはどのようなエンジニアですか？")
    
    print("\n>>> Turn 2: あいまいな代名詞での抽出テスト")
    controller.interact("彼の大好物はなんでしたっけ？")
