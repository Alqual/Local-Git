# Phase 17: 古典・量子ブリッジ（KV Cache to Quantum）実装計画

## Goal Description
これまでの実験で完成した「量子層（Langevin連続アトラクタモデル）」と「Dynamic Alpha機構」を利用し、既存のステートレスLLM（古典層）から溢れたテキスト情報を量子ベクトル空間へ無損失で移譲・抽出する**「ブリッジ層（Classical-to-Quantum Bridge）」**のプロトタイプを実装します。

## アーキテクチャの統一設計（Collapseのメカニズム）
量子状態ベクトル（S）を用いた「情報の取り出し（Collapse）」機構を以下のように設計・実装します。

1. **Archive（文脈の保存）**
   古典層（KVキャッシュ）から溢れた過去の会話履歴を「文単位」に分割し、原文テキストとベクトルペアとしてブリッジ内のArchiveに保存します。
2. **Quantum Injection（量子層への注入）**
   抽出された文ベクトルを、S へ注入します。このとき、直近のユーザープロンプトなどは α_signal=0.5、過去の溢れた雑話は α_noise=0.01 としてDynamic Alphaを適用します。
3. **Collapse（量子からの文脈抽出）**
   ユーザーから新しいクエリが来た際、そのクエリを S に α_signal で注入します。
   この瞬間、S は**「最新のクエリの意図」と「過去1000ターンの壮大な文脈」が美しく重なり合った最強の検索ベクトル（アトラクタ）**へと変化します。
   この S と Archive 内の全テキストベクトルのコサイン類似度を計算し、Top-Kのテキストを抽出（Collapse）して、LLMのプロンプトに復元（RAG的注入）します。

## Proposed Changes

### `retrieval_lm/experiments/phase17_bridge/` フォルダの作成
このフォルダ直下に、ブリッジ接続の最小動作プロトタイプを実装します。

#### [NEW] `quantum_bridge.py`
以下のクラス群を実装します。
*   `QuantumLayer` : フェーズ16で完成した `DynamicLangevinState` のラッパー。
*   `BridgeArchive` : 溢れたテキストとその埋め込みベクトルをインデックス化して保持するストレージ。
*   `ClassicalToQuantumBridge` :
    *   `transfer(text, is_signal)`: テキストを文分割してArchiveに保存し、QuantumLayerへ注入する。
    *   `collapse(top_k)`: 現在のQuantumLayerの状態ベクトル S とArchive群を照合し、最も類似度が高い上位K件のテキストを返す。

#### [NEW] `bridge_simulation_test.py`
古典層のトークン溢れを模倣したシミュレーションスクリプト。
1.  KVキャッシュに収まりきらない大量のダミー会話（ノイズ）や事実（シグナル）をブリッジへ継続的に転送する。
2.  その後、LLMへの新しいユーザー入力（クエリ）が発生したと仮定し、クエリを量子層へ注入。
3.  `bridge.collapse(K=3)` を呼び出し、過去にKVキャッシュから追い出されて「消滅したはずの重要な事実（Target A等）」が、状態ベクトルSの引力によって見事にサルベージ（復元）されることをテスト・証明する。

## Verification Plan
1. `bridge_simulation_test.py` を実行する。
2. 100ターンのノイズ対話を転送した後でも、「クエリに関連する遥か昔のTurn 1の事実」が、Collapse抽出の上位に正確に浮上してくるか（= Lossless Contextの達成）をコンソール出力にて確認・証明する。
