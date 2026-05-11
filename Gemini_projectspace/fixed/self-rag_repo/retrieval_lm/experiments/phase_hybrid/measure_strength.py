import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import os

os.environ["TOKENIZERS_PARALLELISM"] = "false"
quantizer = SentenceTransformer("all-MiniLM-L6-v2")

subjects = ["天気", "科学", "音楽", "旅行", "歴史", "猫", "映画", "料理", "スポーツ", "ゲーム"]
noise_pool = [quantizer.encode([f"雑談ノイズ：今日の{s}について。"])[0] for s in subjects]

texts = {
    "P1": "Tackは焼肉が好き",          
    "P2": "新しいAI構造を設計中",    
    "F1": "富士山は日本一高い山",       
    "F2": "水は摂氏100度で沸騰する",      
    "A1": "時間は一方向にしか進まない",   
    "A2": "自由とは責任を伴う概念である", 
    "N1": "あいうえおかきくけこ",       
    "N2": "xyz abc pqr 123",        
}

encoded = {k: quantizer.encode([v])[0] for k, v in texts.items()}

print(f"{'Key':<4} | {'Sim to Noise_Avg':<18} | {'Distinctness (1 - Sim)':<25}")
print("-" * 55)

for k, v in encoded.items():
    noise_sims = cosine_similarity([v], noise_pool)[0]
    avg_noise_sim = np.mean(noise_sims)
    distinctness = 1.0 - avg_noise_sim
    print(f"{k:<4} | {avg_noise_sim:<18.4f} | {distinctness:<25.4f}")
