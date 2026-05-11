import sys
import time
from small_lm_engine import StatelessSmallLM

class LosslessStateMachine:
    def __init__(self):
        # 外部で完全な状態を管理するためのバッファ（情報の欠落を許さないLosslessな管理）
        self.context_buffer = []
        self.engine = StatelessSmallLM()
        
        # モックの外部ナレッジ（DB）
        self.dummy_db = {
            "東京タワー": "東京タワーの高さは333メートルです。",
            "宇宙の年齢": "宇宙の年齢は約138億年と推定されています。",
            "Tack": "Tackは非常に優秀なエンジニアです。"
        }

        # システムプロンプトによるSLMへの指示。知識になければ <RETRIEVAL> と必ず出力するよう強制。
        self.system_prompt = (
            "You are a helpful and truthful assistant. "
            "CRITICAL INSTRUCTION: If you do not know the exact factual answer immediately, "
            "you MUST output exactly and only '<RETRIEVAL>' to request help from the external system. "
            "Do not guess or try to make up an answer."
            "If context is provided, use it to form your answer. Respond concisely."
        )

    def interact(self, user_input: str):
        print(f"\n--- [Controller] User Event: {user_input} ---")
        
        # 1. ユーザー入力を情報を失わずにバッファへ追加
        self.context_buffer.append({"role": "user", "content": user_input})
        
        # 2. バッファ全体からプロンプトを構築
        prompt = self._build_prompt_from_buffer()
        print("[Controller] State securely synced. Sending combined exact prompt to Engine...")
        
        # 3. エンジン(SLM)による推論（1回目）
        response = self.engine.generate_response(prompt, system_prompt=self.system_prompt, max_new_tokens=150)
        response = response.strip()
        print(f"[Engine Output]: {response}")
        
        # 4. 割り込み条件のチェック (フェーズ3のモック部分: 外部システムへの制御の委譲)
        if "<RETRIEVAL>" in response:
            print(f"[Controller] 🚨 Intercepted '<RETRIEVAL>' token. Engine requested external state. Pausing...")
            
            # 外部データベースへのモック検索
            knowledge = self._mock_retrieve(user_input)
            print(f"[Controller] 📡 External Knowledge retrieved: {knowledge}")
            
            # 検索結果をバッファに追加 (コントローラ側でのLosslessなコンテキスト注入)
            self.context_buffer.append({"role": "system", "content": f"EXTERNAL_KNOWLEDGE_INJECTION: {knowledge}"})
            
            # 注入後の状態をもとに再推論
            prompt = self._build_prompt_from_buffer()
            print("[Controller] Resending updated explicit state to Engine...")
            response = self.engine.generate_response(prompt, system_prompt=self.system_prompt, max_new_tokens=150)
            response = response.strip()
            print(f"[Engine Final Output]: {response}")

        # 5. アシスタントの最終回答を状態バッファに保存
        self.context_buffer.append({"role": "assistant", "content": response})

    def _build_prompt_from_buffer(self) -> str:
        # すべての文脈を損失なく平文化し、ひとつの巨大なユーザー入力としてエンジンに投げる
        text = "This is the exact history of our interaction so far:\n\n"
        for item in self.context_buffer:
            if item["role"] == "user":
                text += f"User: {item['content']}\n"
            elif item["role"] == "assistant":
                text += f"Assistant previously answered: {item['content']}\n"
            elif item["role"] == "system":
                text += f"System Inject: {item['content']}\n"
        
        text += "\nNow, provide your next Assistant answer. If you need external knowledge, output <RETRIEVAL>."
        return text

    def _mock_retrieve(self, query: str) -> str:
        for key, value in self.dummy_db.items():
            if key in query:
                return value
        return "情報が見つかりませんでした。"


if __name__ == "__main__":
    print("=== Initializing Lossless Controller ===")
    
    start = time.time()
    controller = LosslessStateMachine()
    
    print("\n================ TIER 2 & 3: LOSSLESS CONTROLLER EXPERIMENT ================")
    
    print("\n>>> Turn 1: 一般的な挨拶 (自己解決可能)")
    controller.interact("Hello! I am Tack. Are you ready to work?")
    
    print("\n>>> Turn 2: 未知の知識を要求する質問 (Retrieval トリガーテスト)")
    controller.interact("東京タワーの高さはどれくらいですか？")
    
    print("\n>>> Turn 3: 以前の文脈の参照 (Lossless Stateの堅牢性検証)")
    controller.interact("私の名前を覚えていれば教えてください。また、さっき調べた東京タワーの高さも教えて。")
    
    print("\n=== End of Test ===")
    print(f"\n[Final Controller Core Memory State (Lossless Buffer)]:\n")
    for i, item in enumerate(controller.context_buffer):
        print(f"[{i}] {item}")
