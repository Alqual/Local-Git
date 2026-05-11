"""
shared_utils.py
===============
物理運動モデル実験共通ユーティリティ。
- SentenceTransformerのロード（1回のみ）
- 基準ベクトルと1000ターン分のノイズベクトルの準備
- スウィープ評価
"""
import numpy as np
from sentence_transformers import SentenceTransformer
import random

DIM = 384
TOTAL_TURNS = 1000

_quantizer = None

def get_quantizer():
    global _quantizer
    if _quantizer is None:
        _quantizer = SentenceTransformer("all-MiniLM-L6-v2")
    return _quantizer


def prepare_vectors():
    """基準ベクトルとノイズプールを生成して返す。"""
    q = get_quantizer()
    vec_A = q.encode(["Tackは焼肉が好き"])[0]
    vec_B = q.encode(["富士山は日本一高い山"])[0]
    
    random.seed(42)
    subjects = ["天気", "スポーツ", "映画", "料理", "歴史", "科学", "音楽", "旅行", "宇宙", "文学"]
    noise_pool = []
    for i in range(1, TOTAL_TURNS + 1):
        t = f"雑談ノイズ:今日の{random.choice(subjects)}は面白いですよね。記録{i}。"
        noise_pool.append(q.encode([t])[0])
    
    return vec_A, vec_B, noise_pool


def sweep(model_fn, vec_A, vec_B, noise_pool, turn_Bs=None):
    """
    model_fn: (vec_A, vec_B, noise_pool, turn_B) -> (score_A, score_B)
    各 turn_B について score を計測し、結果のリストを返す。
    """
    if turn_Bs is None:
        turn_Bs = list(range(50, TOTAL_TURNS, 100)) + [TOTAL_TURNS - 1]
    results = []
    for turn_b in turn_Bs:
        sA, sB = model_fn(vec_A, vec_B, noise_pool, turn_b)
        results.append({"label": str(turn_b), "score_A": float(sA), "score_B": float(sB)})
    return results


def print_table(results):
    print(f"{'Turn B':<8} | {'Score A':>10} | {'Score B':>10} | {'Ratio':>8}")
    print("-" * 50)
    for r in results:
        sA, sB = r["score_A"], r["score_B"]
        ratio = sB / sA if sA != 0 else float("inf")
        print(f"{r['label']:<8} | {sA:>10.6f} | {sB:>10.6f} | {ratio:>8.4f}")
