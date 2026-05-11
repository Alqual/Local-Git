import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import uuid

class QuantumLayer:
    def __init__(self, dim=384, mu=0.001, sigma=0.01):
        self.state = np.zeros(dim)
        self.mu = mu
        self.sigma = sigma
    
    def update(self, v_in, alpha):
        drift = -self.mu * self.state
        diffusion = np.random.normal(0, self.sigma, self.state.shape)
        self.state += (drift + diffusion)
        self.state += alpha * v_in
        norm = np.linalg.norm(self.state)
        if norm > 0:
            self.state /= norm

class BridgeArchive:
    def __init__(self):
        self.texts = []
        self.vectors = []
        self.ids = []

    def add(self, text, vector):
        self.texts.append(text)
        self.vectors.append(vector)
        self.ids.append(str(uuid.uuid4()))

class ClassicalToQuantumBridge:
    def __init__(self, embedder):
        self.quantum_layer = QuantumLayer(dim=384, mu=0.001, sigma=0.01)
        self.archive = BridgeArchive()
        self.embedder = embedder

    def transfer_to_quantum(self, sentences, is_signal=False):
        """
        古典層(KV cache)から溢れた文を受け取り、Archiveへ保存しつつ、
        量子層(Quantum Layer)の背景へ同化させる。
        """
        # Dynamic Alpha: シグナルなら0.50、ノイズなら0.01
        alpha = 0.50 if is_signal else 0.01
        for sentence in sentences:
            if not sentence.strip(): continue
            vector = self.embedder.encode([sentence])[0]
            self.archive.add(sentence, vector)
            self.quantum_layer.update(vector, alpha=alpha)

    def process_query(self, query):
        """
        ユーザーからの新規クエリを受け取った際、強いシグナルとして量子層へ注入する。
        これにより、状態ベクトルSが「最新の意図」に大きく傾いたアトラクタに変化する。
        """
        vector = self.embedder.encode([query])[0]
        self.quantum_layer.update(vector, alpha=0.50)

    def collapse(self, top_k=3):
        """
        現在の量子層の状態ベクトルS群を用いて、Archive内のテキスト群と波動関数の干渉（類似度計算）を行い、
        親和性の高い文脈（過去の記憶）をTop-K抽出して古典層へ返す。
        """
        if not self.archive.vectors:
            return []
            
        state_vec = [self.quantum_layer.state]
        similarities = cosine_similarity(state_vec, self.archive.vectors)[0]
        
        top_indices = np.argsort(similarities)[-top_k:][::-1]
        
        results = []
        for idx in top_indices:
            results.append({
                "text": self.archive.texts[idx],
                "score": float(similarities[idx])
            })
        return results
