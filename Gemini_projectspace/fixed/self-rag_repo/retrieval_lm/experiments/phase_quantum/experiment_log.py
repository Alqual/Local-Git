"""
experiment_log.py
==================
量子化コントローラ実験のバージョン管理ライブラリ。
実験ごとに結果をJSON + Markdownで記録・参照・一覧表示する。
"""

import json
import os
import datetime

RESULTS_DIR = os.path.join(os.path.dirname(__file__), "experiment_results")
INDEX_FILE = os.path.join(RESULTS_DIR, "index.json")

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

def log_experiment(phase: int, title: str, description: str, params: dict, results: list[dict], conclusion: str) -> str:
    """
    実験結果をファイルとして記録する。

    Parameters
    ----------
    phase       : フェーズ番号 (例: 11)
    title       : 実験タイトル
    description : 実験の目的・手法
    params      : 使用したパラメータ (dict)
    results     : 計測結果のリスト。各要素は {"label": ..., "score_A": ..., "score_B": ...} 形式
    conclusion  : 考察・結論

    Returns
    -------
    保存したMarkdownファイルのパス
    """
    _ensure_dir()
    index = _load_index()
    
    version = len(index) + 1
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"phase{phase:02d}_v{version:03d}_{timestamp}.md"
    filepath = os.path.join(RESULTS_DIR, filename)
    
    # Markdownレポートを作成
    lines = []
    lines.append(f"# Phase {phase} — {title}")
    lines.append(f"\n**記録日時**: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append(f"**バージョン**: v{version:03d}\n")
    lines.append("## 実験の目的・手法\n")
    lines.append(description + "\n")
    lines.append("## パラメータ\n")
    lines.append("```json")
    lines.append(json.dumps(params, ensure_ascii=False, indent=2))
    lines.append("```\n")
    lines.append("## 計測結果\n")
    lines.append(f"| {'対象':<20} | {'Score A':>10} | {'Score B':>10} | {'Ratio B/A':>10} |")
    lines.append(f"|{'-'*22}|{'-'*12}|{'-'*12}|{'-'*12}|")
    for r in results:
        label = r.get("label", "")
        sA = r.get("score_A", 0.0)
        sB = r.get("score_B", 0.0)
        ratio = sB / sA if sA != 0 else float("inf")
        lines.append(f"| {label:<20} | {sA:>10.6f} | {sB:>10.6f} | {ratio:>10.4f} |")
    lines.append("")
    lines.append("## 考察・結論\n")
    lines.append(conclusion + "\n")
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    
    # indexに追記
    index.append({
        "version": version,
        "phase": phase,
        "title": title,
        "timestamp": timestamp,
        "filename": filename
    })
    _save_index(index)
    
    print(f"[ExperimentLog] ✅ 結果を保存しました → {filepath}")
    return filepath


def list_experiments(phase: int = None):
    """記録された実験の一覧を表示する。phase を指定するとフィルタリングできる。"""
    index = _load_index()
    if not index:
        print("[ExperimentLog] まだ記録された実験はありません。")
        return
    
    filtered = [e for e in index if phase is None or e["phase"] == phase]
    print(f"\n{'Ver':<5} | {'Phase':<6} | {'タイトル':<40} | {'記録日時'}")
    print("-" * 80)
    for e in filtered:
        ts = datetime.datetime.strptime(e["timestamp"], "%Y%m%d_%H%M%S").strftime("%Y-%m-%d %H:%M")
        print(f"v{e['version']:<4} | Phase {e['phase']:<2} | {e['title']:<40} | {ts}")


def read_experiment(version: int) -> str:
    """バージョン番号を指定して実験レポートの内容を返す。"""
    index = _load_index()
    entry = next((e for e in index if e["version"] == version), None)
    if not entry:
        print(f"[ExperimentLog] バージョン v{version} は見つかりません。")
        return ""
    filepath = os.path.join(RESULTS_DIR, entry["filename"])
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    print(content)
    return content
