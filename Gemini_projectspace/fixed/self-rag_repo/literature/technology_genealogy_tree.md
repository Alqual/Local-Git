# AI記憶・コンテキスト管理技術の系譜ツリー

**作成日**: 2026-04-12

---

## 図1：基礎理論層 → Transformerの台頭（〜2019）

```mermaid
flowchart TD
    HEBB["Hebbの学習則\n1949"]
    HOPFIELD["ホップフィールドネット\n1982"]
    HRR["HRR ベクトル象徴記憶\n1995"]
    LSTM["LSTM ゲート再帰学習\n1997"]
    LINDBLAD["Lindbladマスター方程式\n1976"]
    SGLD["SGLD 確率的Langevin\n2011"]
    NTM["Neural Turing Machine\n2014"]
    DNC["DNC 時間順序付き外部記憶\n2016"]
    ATTN["Attention is All You Need\n2017 ★"]
    TXLFORMER["Transformer-XL\nセグメント間KV再利用\n2019"]
    COMPRESS["Compressive Transformer\n圧縮メモリ\n2019"]

    HEBB --> LSTM
    HOPFIELD --> NTM
    HRR --> NTM
    LSTM --> ATTN
    LINDBLAD --> SGLD
    NTM --> DNC
    DNC --> NTM
    ATTN --> TXLFORMER
    TXLFORMER --> COMPRESS
```

---

## 図2：長文・記憶への挑戦（2020〜2022）

```mermaid
flowchart TD
    COMPRESS["Compressive Transformer\n2019"]
    HIPPO["HiPPO 最適多項式射影記憶\n2020"]
    LONGFORMER["Longformer / BigBird\nスパース注意\n2020"]
    MODERN_HOP["Modern Hopfield Networks\nAttention=連想記憶\n2021"]
    S4["S4 構造化状態空間モデル\n2022 ICLR Outstanding"]
    ROPE["RoPE 回転位置埋め込み\n2021"]
    ALIBI["ALiBi 線形バイアス位置符号化\n2022"]
    SCORE_SDE["Score-Based SDE\nLangevin+スコア統一\n2021 ICLR Oral"]
    RMT["Recurrent Memory Transformer\nメモリトークン 2Mトークン\n2022"]

    COMPRESS --> HIPPO
    HIPPO --> S4
    LONGFORMER --> S4
    ROPE --> ALIBI
    SCORE_SDE --> MODERN_HOP
    MODERN_HOP --> S4
    S4 --> RMT
```

---

## 図3：次世代高速アーキテクチャ（2023）

```mermaid
flowchart TD
    S4["S4\n2022"]
    ROPE["RoPE\n2021"]
    DNC["DNC\n2016"]
    COMPRESS["Compressive Transformer\n2019"]

    MAMBA["Mamba 選択的SSM\n2023 ★"]
    RETNET["RetNet 3形式保持機構\nMicrosoft 2023"]
    RWKV["RWKV RNN/Transformer両立\n2023"]
    MEMGPT["MemGPT / Letta\nOS型2層記憶 Stanford 2023"]
    STREAM["StreamingLLM\nAttention Sink 無限推論\n2023"]
    LONGMEM["LongMem / SideNet\nデカップル型記憶バンク\n2023"]
    YARN["YaRN RoPE拡張\n2023"]

    S4 --> MAMBA
    S4 --> RETNET
    MAMBA --> RWKV
    DNC --> MEMGPT
    COMPRESS --> LONGMEM
    ROPE --> STREAM
    ROPE --> YARN
```

---

## 図4：現代AIエージェント（2024〜2025）と本研究

```mermaid
flowchart TD
    MAMBA["Mamba 2023"]
    RETNET["RetNet 2023"]
    MEMGPT["MemGPT 2023"]
    COMPRESS["Compressive Transformer 2019"]
    LONGMEM["LongMem 2023"]
    SGLD["SGLD 2011"]
    LINDBLAD["Lindblad方程式\n1976"]
    ROPE["RoPE 2021"]
    MODERN_HOP["Modern Hopfield\n2021"]
    HRR["HRR 1995"]

    INFINI["Infini-Attention\nGoogle 2024 ★"]
    GRIFFIN["Griffin / Hawk\nDeepMind 2024"]
    TITANS["Titans テスト時更新3層記憶\nGoogle 2025"]
    KV_COMP["KV Cache圧縮技術群\nH2O/KIVI/ChunkKV 2024"]
    AGENT["現代AIエージェント\nClaude / GPT-4o / Gemini\n+ Memory系ツール 2024〜"]

    HYBRID["🔭 本研究（進行中）\nハイブリッド型無損失AIアーキテクチャ\n古典層＋量子層ブリッジ"]

    COMPRESS --> INFINI
    LONGMEM --> INFINI
    RETNET --> GRIFFIN
    MAMBA --> TITANS
    MEMGPT --> TITANS
    INFINI --> AGENT
    TITANS --> AGENT
    GRIFFIN --> AGENT
    KV_COMP --> AGENT
    MEMGPT --> AGENT

    INFINI -->|ブリッジ設計参照| HYBRID
    MAMBA -->|選択ゲート設計| HYBRID
    SGLD -->|Langevin散逸モデル| HYBRID
    LINDBLAD -->|量子散逸モデル| HYBRID
    HRR -->|ベクトル重ね合わせ| HYBRID
    ROPE -->|時間符号化設計| HYBRID
    MODERN_HOP -->|アトラクタ長期記憶| HYBRID
    KV_COMP -->|重要度フィルタ設計| HYBRID
```

---

## タイムライン早見表

| 年代 | 主要論文 | 技術革新 |
|---|---|---|
| 1949 | Hebbの学習則 | 共起強化による接続重み更新 |
| 1976 | Lindbladマスター方程式 | 量子散逸の数学的記述 |
| 1982 | 古典ホップフィールドネット | エネルギー最小化・連想記憶 |
| 1995 | HRR | 固定サイズベクトル重ね合わせ記憶 |
| 1997 | LSTM | ゲートによる選択的忘却 |
| 2011 | SGLD | 確率的Langevin勾配降下 |
| 2014/16 | NTM/DNC | 外部メモリ付きニューラルネット |
| 2017 ★ | Attention is All You Need | Self-Attention・Transformer誕生 |
| 2019 | Compressive Transformer | 古い記憶の段階的圧縮 |
| 2020 | HiPPO | 多項式最適射影による記憶保持 |
| 2021 ★ | S4・RoPE・Modern Hopfield | SSM・回転位置符号化・Attention=連想記憶 |
| 2023 ★ | Mamba・MemGPT | 選択的SSM・OS型2層記憶エージェント |
| 2024 ★ | Infini-Attention・Griffin | ブリッジ型圧縮記憶・ゲート線形再帰 |
| 2025 | Titans | テスト時更新型3層記憶 |
| 進行中 | **本研究** | 古典層+量子層ハイブリッド |
