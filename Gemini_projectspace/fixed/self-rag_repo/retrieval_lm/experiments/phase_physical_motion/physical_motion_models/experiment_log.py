"""
experiment_log.py  （physical_motion_models 専用版）
実験結果をJSONインデックス + Markdownファイルで記録・管理する。
"""
import json
import os
import datetime

RESULTS_DIR = os.path.join(os.path.dirname(__file__), "experiment_results")
INDEX_FILE  = os.path.join(RESULTS_DIR, "index.json")


def _ensure_dir():
    os.makedirs(RESULTS_DIR, exist_ok=True)


def _load_index():
    if not os.path.exists(INDEX_FILE):
        return []
    with open(INDEX_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def _save_index(index):
    with open(INDEX_FILE, "w", encoding="utf-8") as f:
        json.dump(index, f, ensure_ascii=False, indent=2)


def log_experiment(model_name: str, description: str, params: dict, results: list, conclusion: str) -> str:
    _ensure_dir()
    index = _load_index()
    version = len(index) + 1
    ts = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{model_name.replace(' ', '_')}_v{version:03d}_{ts}.md"
    filepath = os.path.join(RESULTS_DIR, filename)

    lines = [
        f"# {model_name}",
        f"\n**記録日時**: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}  |  **v{version:03d}**\n",
        "## 実験の目的・手法\n", description + "\n",
        "## パラメータ\n```json", json.dumps(params, ensure_ascii=False, indent=2), "```\n",
        "## 計測結果\n",
        f"| {'Turn B':<8} | {'Score_A':>10} | {'Score_B':>10} | {'Ratio B/A':>10} |",
        f"|{'-'*10}|{'-'*12}|{'-'*12}|{'-'*12}|",
    ]
    for r in results:
        sA, sB = r.get("score_A", 0), r.get("score_B", 0)
        ratio = sB / sA if sA != 0 else float("inf")
        lines.append(f"| {str(r.get('label','')):<8} | {sA:>10.6f} | {sB:>10.6f} | {ratio:>10.4f} |")

    lines += ["", "## 考察・結論\n", conclusion + "\n"]

    with open(filepath, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    index.append({"version": version, "model": model_name, "timestamp": ts, "filename": filename})
    _save_index(index)
    print(f"[ExperimentLog] ✅ saved → {filepath}")
    return filepath


def list_experiments():
    index = _load_index()
    if not index:
        print("まだ記録はありません。")
        return
    print(f"\n{'Ver':<5} | {'モデル名':<40} | 記録日時")
    print("-" * 70)
    for e in index:
        ts = datetime.datetime.strptime(e["timestamp"], "%Y%m%d_%H%M%S").strftime("%Y-%m-%d %H:%M")
        print(f"v{e['version']:<4} | {e['model']:<40} | {ts}")
