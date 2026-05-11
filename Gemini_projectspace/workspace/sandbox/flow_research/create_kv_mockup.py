import numpy as np
import json
import os

# --- 1. KVキャッシュのメタデータ作成 (JSON) ---
# 実際のモデルでは、どの位置にどのトークンの記憶があるかを管理するインデックスが必要
metadata = {
    "model_info": {
        "name": "mock-transformer-v1",
        "layers": 2,
        "heads": 4,
        "dim_per_head": 64
    },
    "tokens": [
        {"id": 0, "text": "今日", "position": 0},
        {"id": 1, "text": "の", "position": 1},
        {"id": 2, "text": "朝食", "position": 2},
        {"id": 3, "text": "は", "position": 3},
        {"id": 4, "text": "目玉焼き", "position": 4}
    ],
    "storage_format": "float32"
}

with open("kv_cache_metadata.json", "w", encoding="utf-8") as f:
    json.dump(metadata, f, indent=2, ensure_ascii=False)

# --- 2. KVキャッシュの生データ作成 (Numpy / Binary) ---
# 各レイヤー、各トークンに対して Key(K) と Value(V) のベクトルを生成
num_tokens = len(metadata["tokens"])
num_layers = metadata["model_info"]["layers"]
dim = metadata["model_info"]["heads"] * metadata["model_info"]["dim_per_head"] # 256

# [Layers, 2(K and V), Tokens, Dimension] という巨大なテンソル
kv_data = np.random.randn(num_layers, 2, num_tokens, dim).astype(np.float32)

# バイナリとして保存
np.savez_compressed("kv_cache_data.npz", cache=kv_data)

# --- 3. 人間が見るためのプレビューファイル (JSON) ---
# バイナリの中身を少しだけテキスト化したもの
preview = {
    "sample_entry": {
        "token": "目玉焼き",
        "layer": 0,
        "key_vector_start": kv_data[0, 0, 4, :5].tolist(), # 先頭5要素のみ
        "value_vector_start": kv_data[0, 1, 4, :5].tolist()
    }
}

with open("kv_cache_preview.json", "w", encoding="utf-8") as f:
    json.dump(preview, f, indent=2, ensure_ascii=False)

print("疑似KVキャッシュファイルを作成しました:")
print("- kv_cache_metadata.json (構造の定義)")
print("- kv_cache_data.npz (生の数値データ - バイナリ)")
print("- kv_cache_preview.json (中身の一部プレビュー)")
