# 関連論文・技術資料 サーベイ（拡充版）
# ハイブリッド型無損失AIアーキテクチャ研究

**作成日**: 2026-04-10 | **最終更新**: 2026-04-10（拡充）
**調査数**: 約35本（各カテゴリ4〜7本）

---

## カテゴリ A：長文コンテキスト・階層記憶管理（古典層の関連研究）

### A1. MemGPT: Towards LLMs as Operating Systems
- **著者**: Packer et al. (Stanford)
- **発表**: 2023年10月 / arXiv: **2310.08560**
- **URL**: https://arxiv.org/abs/2310.08560
- **概要**: LLMのコンテキスト管理をOSの仮想メモリに見立て、「メインコンテキスト（短期）」と「外部ストレージ（長期）」の2層でページングを行う。LLM自身が関数呼び出しでメモリのページングを制御する。進化版プロジェクト名は **Letta**。
- **本研究との関係**: 2層構造の先行研究。ただし長期記憶層が構造化DBであり、連続的な意味的散逸（ベクトル空間）ではない。

### A2. Infini-Attention: Leave No Context Behind
- **著者**: Munkhdalai, Faruqui, Gopal (Google)
- **発表**: 2024年4月 / arXiv: **2404.07143**
- **URL**: https://arxiv.org/abs/2404.07143
- **概要**: Transformerの1ブロック内に「ローカル注意（標準KV）」+「長期線形注意（圧縮メモリ行列）」を組み合わせたハイブリッド注意機構。固定サイズ状態で無限長コンテキストを処理。1Mトークンのパスキー検索に成功。
- **本研究との関係**: **⭐最重要**。溢れた情報を固定サイズ記憶に転送する点がブリッジ設計と直接対応する。

### A3. Titans: Learning to Memorize at Test Time
- **著者**: Behrouz et al. (Google)
- **発表**: 2025年1月 / arXiv: **2501.00663**
- **URL**: https://arxiv.org/abs/2501.00663
- **概要**: テスト時にも勾配更新が行われる「ニューラル長期記憶」を持つ3層アーキテクチャ（短期・長期・永続記憶）。
- **本研究との関係**: テスト時更新型記憶のアイデア。ただし確率的物理散逸ではなく勾配法を使用。

### A4. LongMem: Augmenting Language Models with Long-Term Memory
- **著者**: Wang et al. (Microsoft / UCSB)
- **発表**: 2023年 / arXiv: **2306.07174**
- **URL**: https://arxiv.org/abs/2306.07174
- **概要**: 凍結されたバックボーンLLM（記憶エンコーダ）と、軽量SideNet（記憶リーダー・取り出し器）を分離した「デカップル型記憶設計」。65kトークン規模のキャッシュバンクから過去情報を検索して融合する。
- **本研究との関係**: 「推論エンジンと記憶層を切り離す」という本研究の設計思想と一致。記憶がキーバリューDBであるが検索・融合の仕組みはブリッジB4設計の参考になる。

### A5. Compressive Transformer for Long-Range Sequence Modelling
- **著者**: Rae et al. (DeepMind)
- **発表**: 2019年 / arXiv: **1911.05507**
- **URL**: https://arxiv.org/abs/1911.05507
- **概要**: 過去のアクティベーションを压縮してメモリバンクに蓄積するTransformer拡張。古いメモリは自動的に圧縮（平均プーリング・MLPなど）されながら保持される。
- **本研究との関係**: 「古い情報を圧縮して長期記憶に転送する」という本研究のブリッジのコアアイデアに最も近い古典的先行研究。

### A6. StreamingLLM: Efficient Streaming Language Models with Attention Sinks
- **著者**: Xiao et al. (MIT / Meta)
- **発表**: 2023年 / arXiv: **2309.17453**
- **URL**: https://arxiv.org/abs/2309.17453
- **概要**: LLMのAttentionが「初期トークン（Attention Sink）」に高いスコアを与える現象を活用し、初期トークンと最近のトークンのみを保持して実質無限長の推論を実現。4Mトークン以上での安定動作を確認。
- **本研究との関係**: 「観測限界の不連続消滅」の対処法として参考になる。ただし意味論的な保存ではなく構造的なハックによる解決策。

### A7. Recurrent Memory Transformer (RMT)
- **著者**: Bulatov, Kuratov, Burtsev
- **発表**: 2022年7月 / arXiv: **2207.06881**、2023年 arXiv: **2304.11062**
- **URL**: https://arxiv.org/abs/2207.06881
- **概要**: 特殊な「メモリトークン」をインプット/アウトプットに付加してセグメント間で情報を伝達する再帰型Transformer。前処理済みTransformerへのプラグイン適用が可能で2Mトークン処理を実証。
- **本研究との関係**: セグメント間の「記憶の橋渡し」という設計はB1トリガー設計に参考になる。

### A8. KV Cache Compression サーベイ（2024年）
- **主要サーベイ**: arXiv: **2412.19442**「KV Cache Management Survey」
- **評価論文**: arXiv: **2407.01527**「KV Cache Compression Benchmark」
- **概要**: トークン退避（H2O, SAGE-KV, NACL）・量子化（KIVI, ZipCache）・マージ（CaM, ChunkKV）の3方向。Attentionスコアに基づく選択的削除が主流。
- **本研究との関係**: B2「何を転送するか」の設計でトークン重要度判断に応用可能。

### A9. Longformer / BigBird: Sparse Attention for Long Documents
- **Longformer**: Beltagy et al. (AllenAI) / arXiv: **2004.05150**
- **BigBird**: Zaheer et al. (Google) / arXiv: **2007.14062**
- **概要**: O(n²)の全注意の代わりに、ローカル注意・グローバル注意・ランダム注意を組み合わせてO(n)で長文を処理するスパース注意機構。
- **本研究との関係**: 長文コンテキスト管理の代表的アーキテクチャとして参考。本研究のLayer 1の設計オプションの一つ。

---

## カテゴリ B：状態空間モデル・再帰型（古典層の軽量代替案）

### B1. S4: Efficiently Modeling Long Sequences with Structured State Spaces
- **著者**: Gu, Goel, Ré (Stanford)
- **発表**: 2021年 / ICLR 2022 Outstanding Paper
- **URL**: https://arxiv.org/abs/2111.00396
- **概要**: HiPPO（最適多項式射影による記憶）理論に基づく状態行列の初期化で長期記憶を保持。DPLR（対角線プラス低ランク）パラメータ化によりFFT畳み込みで効率的な計算を実現。
- **本研究との関係**: Mambaの前身。物理的に動機付けられた状態空間（HiPPO＝L2最適近似）が量子層の理論的基盤と共鳴する。

### B2. Mamba: Linear-Time Sequence Modeling with Selective State Spaces
- **著者**: Gu, Dao (CMU / TogetherAI)
- **発表**: 2023年12月 / arXiv: **2312.00752**
- **URL**: https://arxiv.org/abs/2312.00752
- **概要**: S4に「選択機構」を導入し、入力に応じてパラメータを動的に変化させることで選択的な保持・忘却を実現。線形計算量でTransformerの性能に匹敵。
- **本研究との関係**: **⭐最重要**。固定サイズ隠れ状態でコンテキストを保持する設計が量子層と最も近い。「選択機構」はHebb的ゲートの先行実装として参考になる。

### B3. RetNet: Retentive Network – A Successor to Transformer
- **著者**: Sun et al. (Microsoft)
- **発表**: 2023年7月 / arXiv: **2307.08621**
- **URL**: https://arxiv.org/abs/2307.08621
- **概要**: 学習並列性・O(1)推論コスト・高性能の「不可能三角形」を同時実現する保持（Retention）機構。指数的減衰（γ^(m-n)）でトークン距離に応じた重み付けが自然に生じる。
- **本研究との関係**: RetNetのγ（保持係数）は本研究の減衰係数αに相当。実装の参考例。

### B4. RWKV: Reinventing RNNs for the Transformer Era
- **著者**: Peng et al.
- **発表**: 2023年5月 / arXiv: **2305.13048** (EMNLP 2023)
- **URL**: https://arxiv.org/abs/2305.13048
- **概要**: 線形注意機構でTransformerとして学習し、RNNとして推論する唯一無二のアーキテクチャ。14Bパラメータまでスケール実証。学習時の並列性と推論時の定数メモリを両立。
- **本研究との関係**: 「学習時はTransformer、推論時はRNN」という設計の実現例。ブリッジの実装でRuntime切り替えシステムを設計する際の参考に。

### B5. Griffin: Mixing Gated Linear Recurrences with Local Attention
- **著者**: De et al. (Google DeepMind)
- **発表**: 2024年2月 / arXiv: **2402.19427**
- **URL**: https://arxiv.org/abs/2402.19427
- **概要**: 「ゲート線形再帰（RG-LRU）」と「局所注意」を混合したハイブリッドモデル。純RNN版「Hawk」もMambaを上回る性能。14Bパラメータに対応。
- **本研究との関係**: 再帰層と注意層のハイブリッドは本研究のLayer 1（古典）とLayer 2（量子）の接続に近いアーキテクチャとして参考になる。

---

## カテゴリ C：位置符号化・時間性の表現

### C1. RoFormer: Enhanced Transformer with Rotary Position Embedding (RoPE)
- **著者**: Su, Lu, Pan, Wen, Liu
- **発表**: 2021年4月 / arXiv: **2104.09864**、Neurocomputing誌 2024年掲載
- **URL**: https://arxiv.org/abs/2104.09864
- **概要**: θ_i = pos / base^(2i/d) の回転を各2次元ペアに適用。内積が相対位置差のみに依存するよう設計。LLaMA, PaLM, Mistralなどの業界標準位置符号化。
- **本研究との関係**: Phase 11〜13で直接実装・実験した回転行列の元論文。

### C2. ALiBi: Train Short, Test Long
- **著者**: Press, Smith, Lewis (AllenAI / UW)
- **発表**: ICLR 2022 / arXiv: **2108.12409**
- **URL**: https://arxiv.org/abs/2108.12409
- **概要**: 位置埋め込みを使わず、Attentionスコアにトークン距離に比例した線形バイアスを引くだけ。短い文脈で学習して長い文脈に汎化できる。
- **本研究との関係**: 「距離が遠いほどスコアが下がる」という性質は本研究のPhase 13（時間性RoPE）の目指した動作と同根のアイデア。

### C3. YaRN: Yet Another RoPE Extension Method
- **著者**: Peng et al. (Nous Research)
- **発表**: 2023年 / arXiv: **2309.00071**
- **URL**: https://arxiv.org/abs/2309.00071
- **概要**: RoPEの高周波数次元は外挿（extrapolation）、低周波数次元は内挿（interpolation）という「NTK-by-parts」戦略でコンテキストを64k〜128kに拡張。10倍少ないトークンで効率的な拡張が可能。
- **本研究との関係**: Phase 11〜12の楕円回転で「次元ペアごとに異なる扱いをする」というアイデアとYaRNの「高周波/低周波を分けた処理」は同じ着想から生まれている。

### C4. Transformer-XL: Attentive Language Models Beyond a Fixed-Length Context
- **著者**: Dai et al. (Carnegie Mellon / Google)
- **発表**: 2019年 / arXiv: **1901.02860** (ACL 2019)
- **URL**: https://arxiv.org/abs/1901.02860
- **概要**: セグメント間でKVキャッシュを再利用（Stop Gradient）するとともに、相対位置エンコーディングに切り替えてセグメント間でも整合性を保つ。RNNよりも長い依存性を学習可能。
- **本研究との関係**: セグメント間でKVを引き継ぐという「ブリッジ的な移送」の先駆的実装例。

---

## カテゴリ D：確率的・物理的散逸モデル（量子層の理論基盤）

### D1. Stochastic Gradient Langevin Dynamics (SGLD)
- **著者**: Welling, Teh
- **発表**: ICML 2011
- **URL**: https://www.ics.uci.edu/~welling/publications/papers/stoclangevin_v6.pdf
- **概要**: 確率的勾配降下にGaussianノイズを加えることでLangevin MCMCサンプリングを実現。ニューラルネットの重みの事後分布からサンプリング可能。本研究のModel 2（Langevin）の原点論文。
- **本研究との関係**: 確率的揺らぎが時間的非対称性を生む本研究の核心知見の理論基盤。

### D2. Score-Based Generative Modeling through Stochastic Differential Equations
- **著者**: Song et al.
- **発表**: ICLR 2021 (Oral) / arXiv: **2011.13456**
- **URL**: https://arxiv.org/abs/2011.13456
- **概要**: 拡散モデルをSDEの枠組みで統一。フォワードSDE（データ→ノイズ）とリバースSDE（ノイズ→データ）の両方向の過程を記述。Langevin動力学でスコア関数を使ったサンプリングを実現。
- **本研究との関係**: 「ノイズを加える過程の逆をたどって元の状態を復元する」という拡散モデルの思想は、本研究の「散逸した記憶をクエリ時に逆向きに引き出す（Collapse）」という操作の数学的基盤と親和性が高い。

### D3. Lindblad Master Equation（量子開放系理論）
- **著者**: Lindblad, G. (1976) / Gorini, Kossakowski, Sudarshan (GKS-L)
- **参照**: Phys. Rev. Lett. 48, 119 (1976)
- **概要**: 量子系が環境と相互作用する際の密度行列の時間発展を記述する量子マスター方程式。`dρ/dt = -i[H,ρ] + Σ(L_k ρ L_k† - ½{L_k†L_k, ρ})`の形で表され、ユニタリ部（回転・コヒーレント進化）と非ユニタリ部（散逸・デコヒーレンス）に分解できる。
- **本研究との関係**: Phase 14 Model 4（Lindblad）の理論基盤。「回転（RoPE的時間符号化）」+「散逸（確率的忘却）」の統一的記述。

### D4. Modern Hopfield Networks is All You Need
- **著者**: Ramsauer et al. (JKU Linz)
- **発表**: ICLR 2021 / arXiv: **2008.02217**
- **URL**: https://arxiv.org/abs/2008.02217
- **概要**: 古典ホップフィールドネットワークを連続値・超線形容量版に拡張。更新則がTransformerのAttentionと数学的に等価であることを証明。指数的記憶容量を実現するアトラクタ動力学。
- **本研究との関係**: 「意味空間内に『引力の谷（アトラクタ）』を作り、重要な情報をその谷に収束させる」という本研究の量子層高度化（Step 5以降）で参考となる。Attentionとの等価性は理論的裏付けになる。

### D5. Bayesian Deep Learning: MC Dropout and Uncertainty Estimation
- **参照**: Gal & Ghahramani (2016) "Dropout as a Bayesian Approximation" (ICML)
- **概要**: Dropout有効推論の複数回実行がVariational Inferenceの近似であることを証明。予測分布の分散から不確かさを推定できる。アンサンブル法も不確かさ推定の代表手法として併用される。
- **本研究との関係**: Model 2（Langevin）での確率的揺らぎの不確かさ管理と関係。「記憶の確信度」を不確かさとして表現する実装への橋渡しとなる。

---

## カテゴリ E：ベクトル象徴記憶・連想記憶（量子層の関連概念）

### E1. Holographic Reduced Representations (HRR)
- **著者**: Plate, T. A.
- **発表**: IEEE Transactions on Neural Networks (1995)
- **概要**: 円形畳み込み（Binding）とベクトル加算（Bundling）で構造的な知識を固定サイズベクトルに符号化し、逆畳み込み（Unbinding）で取り出す手法。固定メモリで複数の事実を重ね合わせ可能なことを証明。
- **本研究との関係**: 本研究の量子層（ベクトル加算による意味の重ね合わせ）の理論的祖先に相当。

### E2. Hyperdimensional Computing (HDC) / Vector Symbolic Architectures Survey
- **参照**: arXiv: **2111.06077** "A Survey on Hyperdimensional Computing aka Vector Symbolic Architectures" (2022)
- **概要**: HDCの包括的サーベイ。バインディング・バンドリング・パーミュテーションの3演算で高次元ベクトル空間上でシンボル計算を実行する脳型計算モデル。耐ノイズ性・フォールトトレランスが優れる。
- **本研究との関係**: 高次元ベクトルの重ね合わせとノイズ耐性の理論的裏付け。本研究のPhase 5〜8で観察した「ノイズ1000件に対しても記憶が残存する」現象のHDC的な説明を与える。

### E3. Memory-Augmented Neural Networks (MANN) / Neural Turing Machine
- **著者**: Graves et al. (DeepMind)
- **発表**: 2014年 / arXiv: **1410.5401** (NeurIPS 2014)
- **URL**: https://arxiv.org/abs/1410.5401
- **概要**: アドレス可能な外部メモリバンクを持つニューラルネットワーク（Neural Turing Machine）。コンテンツベースと位置ベースの読み書きヘッドで記憶を操作する。
- **本研究との関係**: 「推論エンジン（LLM）が外部状態ストア（量子層）を読み書きする」という本研究の設計とアーキテクチャ的に対応する先駆的研究。

### E4. Differentiable Neural Computers (DNC)
- **著者**: Graves et al. (DeepMind)
- **発表**: 2016年 / Nature: 538, 471–476
- **URL**: https://www.nature.com/articles/nature20101
- **概要**: NTMを発展させ、メモリへの動的割り当て・解放・リンクドリスト的な時間的順序管理を持つ外部記憶付きニューラルネット。グラフ問題・系列問題で人間に近い汎化性能を示した。
- **本研究との関係**: 「記憶に時間的な順序関係を持たせる」という本研究のPhase 13（時間性KV型）と方向性が一致する。読み書きの選択的アクセスはHebb的ゲートの設計に参考になる。

### E5. Selective State Space Models for Cognitive-Inspired Sequence Modeling
- **概要**: 記憶の選択的保存・忘却・回想という認知科学的な特性をSSMで模倣する研究潮流。Mambaの「選択機構」は工学的にHebbの学習則に対応する部分がある点について、複数の論文で考察されている。
- **本研究との関係**: 「重要なシグナルだけを揺らぎから保護する」というStep 6のHebb的ゲート設計の認知科学的・実装的基盤となる。

---

## 論文優先読破リスト（実装前チェックリスト）

| 優先度 | 論文 | 理由 |
|---|---|---|
| ⭐⭐⭐ | Infini-Attention (2404.07143) | ブリッジ設計の直接的先行実装 |
| ⭐⭐⭐ | Mamba (2312.00752) | 選択機構付き固定サイズ隠れ状態の最良実装例 |
| ⭐⭐⭐ | Score-Based SDE (2011.13456) | Collapse設計の数学的基盤 |
| ⭐⭐ | MemGPT (2310.08560) | 2層記憶管理のシステム設計参考 |
| ⭐⭐ | Compressive Transformer (1911.05507) | 古い記憶を圧縮して転送する先行実装 |
| ⭐⭐ | RoPE (2104.09864) | 時間符号化設計の数学的基盤 |
| ⭐⭐ | Modern Hopfield Networks (2008.02217) | アトラクタ型長期記憶の理論 |
| ⭐⭐ | SGLD (Welling & Teh, 2011) | Langevin散逸の基礎理論 |
| ⭐ | Titans (2501.00663) | テスト時更新型記憶の設計参考 |
| ⭐ | S4 / HiPPO | 物理的に動機付けられた状態空間の数学的詳細 |
| ⭐ | RWKV (2305.13048) | Train=Transformer / Infer=RNNの実装例 |
| ⭐ | Neural Turing Machine (1410.5401) | 外部ストア型記憶の古典的設計 |
| ⭐ | HRR (Plate, 1995) | ベクトル重ね合わせの理論的正当化 |
| ⭐ | KV Cache Survey (2412.19442) | 重要度フィルタ（B2設計）の参考 |
| ⭐ | YaRN (2309.00071) | 次元ごとの異なる周波数扱いの設計参考 |
