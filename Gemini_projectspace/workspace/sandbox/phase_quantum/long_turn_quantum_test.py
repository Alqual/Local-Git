import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import random
import time

class QuantumState:
    def __init__(self, vector_dim=384):
        self.state_vector = np.zeros(vector_dim)
        
    def update(self, input_vector):
        # 純粋な重ね合わせ（足しあわせて正規化、減衰無しモデル）
        self.state_vector = self.state_vector + input_vector
        norm = np.linalg.norm(self.state_vector)
        if norm > 0:
            self.state_vector = self.state_vector / norm
            
    def get_state(self):
        return self.state_vector

print("=== Phase 6: 1000回連続更新に対する過干渉（ホワイトノイズ化）検証 ===")
print("\n【実験概要】")
print("LLMを利用せず、テキストから抽出された「状態ベクトル（Working Memory）」だけに")
print("1000ターンのあいだランダムな対話（ノイズ）のベクトルを加算し続けます。")
print("最後に代名詞「彼」を用いた質問ベクトルを干渉させ、1ターン目の人物情報に")
print("リンクできるか（抽出確率が保たれるか、それともホワイトノイズとして崩壊するか）を調査します。\n")

start_time = time.time()
print("[*] Loading Quantizer (Embedding Model)...")
quantizer = SentenceTransformer("all-MiniLM-L6-v2")
q_state = QuantumState(vector_dim=quantizer.get_sentence_embedding_dimension())

print("[*] Preparing Massive Knowledge Space (Long-term Memory)...")
knowledge_space = [
    "東京タワーの高さは333メートルです。",
    "TackはPythonとAIアーキテクチャに熱心な優秀なエンジニアです。",
    "Tackの大好物は焼肉です。",
    "富士山は日本で最高峰です。"
]
# 長期記憶側にも1000以上のフェイク知識を入れておく
for i in range(1000):
    knowledge_space.append(f"ダミー事実{i}: 世界の様々な歴史と記録について記載したアーカイブ。")
knowledge_vectors = quantizer.encode(knowledge_space)
print(f"    -> 完了 (DBサイズ: {len(knowledge_space)})")

print("\n--- Turn 1: 重要な記憶の注入 ---")
turn1_input = "Tackとはどのようなエンジニアですか？"
print(f"Input: {turn1_input}")
q_state.update(quantizer.encode([turn1_input])[0])

print(f"\n--- Turn 2 〜 1000: 大量の日常的な雑談ノイズの連続注入 ---")
subjects = ["天気", "スポーツ", "映画", "料理", "歴史", "科学", "音楽", "旅行", "宇宙", "文学"]
print("ベクトルの重ね合わせをシミュレート中...")
for i in range(2, 1001):
    random_noise = f"今日の{random.choice(subjects)}についてですが、とても興味深い事実が判明しました。記録その{i}。"
    noise_vector = quantizer.encode([random_noise])[0]
    q_state.update(noise_vector)

print("    -> 1000回の対話コンテキスト更新が完了しました。")

print("\n--- Turn 1001: 曖昧な質問（干渉の検証） ---")
target_question = "彼の大好物はなんでしたっけ？"
print(f"Input: {target_question}")
q_state.update(quantizer.encode([target_question])[0])

print("\n[*] 測定 (Measurement & Collapse) を実行...")
current_state = q_state.get_state()
similarities = cosine_similarity([current_state], knowledge_vectors)[0]
top_indices = similarities.argsort()[-5:][::-1]

print("\n[抽出結果（Collapse State）: Top 5]")
for rank, idx in enumerate(top_indices, 1):
    score = similarities[idx]
    if score > 0.2:
        print(f" {rank}位 | スコア: {score:.4f} | テキスト: {knowledge_space[idx]}")
    else:
        print(f" {rank}位 | スコア: {score:.4f} | テキスト: (Scoreが0.2未満のため無視) {knowledge_space[idx]}")

print("\n[実験考察]")
if top_indices[0] == 2: # "Tackの大好物は焼肉です。"
    print("なんと、1000回のノイズが重なっても「Tackは焼肉が好き」という関係性が抽出されました！")
    print("状態ベクトルの重ね合わせが1000回の干渉に耐えたことを示します。")
else:
    print("1ターンの「Tack」の波形は、1000回の別文脈（ノイズ）の波形加算によって希釈され")
    print("（ホワイトノイズ化）、代名詞「彼」の干渉から正しい記憶を抽出できなくなりました。")
    print("これがまさに、単純加算アプローチにおける「過干渉の限界」です。")

elapsed = time.time() - start_time
print(f"\n実験完了。所要時間: {elapsed:.2f}秒")
