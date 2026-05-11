# Implementation Plan: 無損失層のモック開発とSLM実験

本計画は、「LLMを記憶のない単発のステートレス・エンジンとみなし、外部のPythonステートマシンが全ての情報（損失制御）を管理する」という無損失層アーキテクチャのプロトタイプを構築するためのロードマップです。

## User Review Required
> [!IMPORTANT]
> この計画では、Self-RAGの公式コードを一度離れ、全く新しいスクラッチの制御スクリプト（モック）を作成します。VRAM 6GB環境で完結させるため、非常に軽量なモデル（TinyLlamaやQwen1.5-1.8B等）をHuggingFaceからダウンロードして使用します。この独立開発アプローチでの進行でよろしいか、承認をお願いいたします。

## 1. 開発フェーズと実装ファイル

### フェーズ1：ステートレス・エンジンの構築（SLMの導入）
VRAM 6GB以下で余裕に動作する1B〜2Bクラスの軽量モデルを導入し、「入力された文字列を受け取り、回答を返すだけ」の純粋な推論モジュールを作成します。
#### [NEW] `small_lm_engine.py` (配置先: `retrieval_lm/` 直下)
- `transformers` ライブラリを使用して `TinyLlama/TinyLlama-1.1B-Chat-v1.0` または同等の軽量モデルをロード。
- `def generate_response(prompt: str) -> str:` という単発の関数のみを露出させ、関数内部には一切の対話履歴（ステート）を持たせない設計とする。

### フェーズ2：無損失コントローラー（Lossless State Machine）の構築
LLMを呼び出し、過去の会話履歴や検索結果のバッファ配列を厳密に管理する「外側のループシステム」を作成します。
#### [NEW] `lossless_controller.py` (配置先: `retrieval_lm/` 直下)
- 内部変数列 `context_buffer = []` を持ち、ユーザーからの入力や外部情報をLosslessに配列に積んでいく。
- 配列をひとつの強力なプロンプト文字列に結合（Format）し、フェーズ1の `small_lm_engine.py` に投げるロジックを実装。

### フェーズ3：状態遷移（割込み）のモック実験
Self-RAGの評価機構（Critique）の構造を模倣し、単純な文字列出力によるステートマシンの割り込み実験（疑似Retrieval）を行います。
- コントローラーからSLMに「答えがわからない場合は絶対に `<RETRIEVAL>` とだけ出力せよ」とシステムプロンプトで命令。
- `lossless_controller.py` 側で、SLMの返答が `<RETRIEVAL>` だった場合、コンソールの出力を一時停止。
- ダミーの辞書（PythonのDict等）から情報を引っぱり出し、`context_buffer` に注入して再推論（Re-prompt）させる。

---

## 2. 検証計画 (Verification Plan)

### Automated tests / Command Executions
1. `python small_lm_engine.py` を実行し、モデルのロードと単発の推論がVRAM OOM（メモリ不足）を起こさず高速に完了するかを検証。
2. `python lossless_controller.py` を実行し、意図的な「わからない質問」を投げた際、SLMが `<RETRIEVAL>` を出力し、Pythonコード側が正規表現等でそれをキャッチして検索モードの `Print` 文（状態遷移）へと移行できるかを検証。

### Manual Verification
- コントローラー側で「どのテキスト配列をLLMに渡したか」を毎ターン強制的にデバッグ出力（Print）させ、**「情報がLLMのブラックボックスの中で消えていないか（ロスレスであるか）」**を人間の目で完全トレース・監視します。
