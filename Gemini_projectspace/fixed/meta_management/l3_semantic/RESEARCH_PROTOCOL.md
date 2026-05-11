# Research Protocol: From Theory to Artifact (研究プロトコル)

本プロトコルは、外部研究（論文・技術文献）の**発見・抽出・検証・統合**を統制する方針文書である。
目的は、プロジェクトに導入されるすべての理論が**再現可能**かつ**科学的に精査済み**であることを保証することにある。

> [!IMPORTANT]
> 本プロトコルは [PROTOTYPING_POLICY.md](file:///home/tack-mit/デスクトップ/Gemini_projectspace/meta_management/l3_semantic/PROTOTYPING_POLICY.md) の **TRL 1（原理観測）の前段階**に位置する。
> 論文から得た知見は、本プロトコルの全ステップを通過して初めてTRL 1としてプロトタイピング対象となる。

---

## 1. 収集戦略 (Collection Strategy)

### 1.1 収集の3モード

論文探索は「故障を直す」ためだけに行うものではない。以下の3つの動機を明示的に区別する。

| モード | 動機 | 起点 | 例 |
| :--- | :--- | :--- | :--- |
| **Mode A: 探索 (Exploration)** | 我々の根本的な問いに、他分野はどう答えているか？ | プロジェクトの核心的問い | 情報理論における忘却、神経科学における記憶固定化、熱力学的コンピューティング |
| **Mode B: 深化 (Deepening)** | 既に採用した理論の源流・最新発展は何か？ | 採用済みKIの原論文 | 蔵本モデルの有限サイズ効果、ランジュバン方程式と最適輸送理論の接続 |
| **Mode C: 対策 (Countermeasure)** | 特定フェーズで観測された故障の原因と解決策は何か？ | 失敗ログ・FAILURE_MODES.md | 高密度時のクラスター崩壊、コンテキストスイッチ遅延 |

### 1.2 引用グラフ遡行 (Citation Graph Traversal)

すべてのモードの主軸は **「Seed論文の引用グラフを辿る」** ことにある。

*   **Mode A**: 関連分野のレビュー論文をSeedとし、引用を**2-3ホップ遡行**して源流の物理法則に到達する。
*   **Mode B**: 採用済みKIの原論文から**被引用（Cited-by）を順方向に辿り**、最新の発展を追跡する。
*   **Mode C**: 故障に関連するキーワードで直接検索し、解決策を含む論文をSeedとする。

#### 枝刈りルール (Pruning Rules)

引用グラフの指数的爆発を制御するため、以下のフィルタを適用する。

| ルール | 基準 | 効果 |
| :--- | :--- | :--- |
| **被引用数フィルタ** | 被引用 100+ のノードのみ追跡 | 影響力の低い枝を除去 |
| **分野フィルタ** | 物理学・数学・計算機科学に限定 | 無関係な分野を除去 |
| **深度制限** | 最大3ホップ | 探索空間を有限に制限 |
| **ユーザー選別** | 各ホップ後に候補リストを提示 | 人間の直感で方向を制御 |

#### 選別スコアリング

候補論文は以下の3軸で評価する。

| 軸 | 問い | 判定方法 |
| :--- | :--- | :--- |
| **新規性** | 我々がまだ持っていないKIに相当する原理を含むか？ | 既存KIとの重複度チェック |
| **独創性** | この論文はアイデアの「源流」か「派生」か？ | 引用グラフ上の入次数/出次数比 |
| **再現性** | 数式・コード・データが揃っているか？ | タイトル・要旨での予備判定 |

### 1.3 漏斗型プロセス (Funnel Process)

一度に深く潜るのではなく、段階的にフィルタリングしてコストを抑える。

```
Step 0: ユーザー指示 (コスト: 0)
  │  収集モード（A/B/C）とテーマをユーザーが指定。
  ↓
Step 1: 表層スキャン (コスト: 低 ≈ 5-10k tokens)
  │  search_web / Semantic Scholar でタイトル・要旨のみ収集。候補リスト生成。
  ↓
Step 2: ユーザー選別 (コスト: 0)
  │  ユーザーが候補リストから「深掘り対象」を選択（2-3本）。
  ↓
Step 3: 精査マトリクス記入 (コスト: 中 ≈ 30-50k tokens / 論文)
  │  read_url_content / Elicit で本文を取得し、精査マトリクスを埋める。
  ↓
Step 4: 外部化 (コスト: 低)
  │  結果を research_ledger/ にファイルとして書き出し、コンテキストから排出。
  ↓
Step 5: 次サイクル判定 (コスト: 0)
     ユーザーが「この論文を新たなSeedとして子探索するか」を判断。
```

> [!WARNING]
> **1セッションの上限**: 1セッション = 1モード × 最大3論文の精査。
> これを超える場合は、セッションを分割し、探索台帳で進捗を引き継ぐ。

---

## 2. 外部ツールスタック (External Tool Stack)

「発見・整理」は既存の無料ツールに委譲し、我々は「検証・統合」に集中する。

| ツール | 役割 | コスト | URL |
| :--- | :--- | :--- | :--- |
| **Research Rabbit** | Seedベースの継続探索・推薦 | 無料 (50 seed) | researchrabbit.ai |
| **Connected Papers** | 厳選した論文の引用近傍を視覚化 | 無料 (月5グラフ) | connectedpapers.com |
| **Elicit** | 候補論文の要約・構造化抽出 | 無料 (基本機能) | elicit.com |
| **Semantic Scholar** | API経由のメタデータ・引用グラフ取得 | 無料 (API Key推奨) | semanticscholar.org |
| **NASA/ADS** | 1970年代以前の物理学古典論文 | 無料 (全文スキャン) | ui.adsabs.harvard.edu |
| **Google Scholar** | 汎用検索・PDF直リンク | 無料 | scholar.google.com |

### ツール選択ガイドライン

*   **表層スキャン (Step 1)**: Semantic Scholar API または search_web
*   **引用近傍の可視化**: Connected Papers（月5回の枠を厳選して使用）
*   **継続的な推薦**: Research Rabbit（コレクション機能で再帰的探索を管理）
*   **論文内容の抽出**: Elicit（Paper Chat機能で精査マトリクスの項目を問い合わせ）
*   **古典論文の全文取得**: NASA/ADS（物理系）、Google Scholar（汎用）

---

## 3. 精査マトリクス (Scrutiny Matrix)

論文から抽出した情報は、以下のマトリクス形式で `research_ledger/` 内の個別ファイルに記録する。

### 3.1 マトリクス・テンプレート

```markdown
# 精査マトリクス: [論文タイトル]

**著者**: 
**年**: 
**発見経路**: (例: seed:self_rag_2024 → hop:2)
**収集モード**: A / B / C

## スコアリング
| 軸 | スコア (1-5) | 根拠 |
| :--- | :--- | :--- |
| 新規性 | | |
| 独創性 | | |
| 再現性 | | |

## 抽出内容

| カテゴリ | 項目 | 内容 | 備考 |
| :--- | :--- | :--- | :--- |
| **数理的不変量** | コア方程式 | | 理論の核心 |
| | 安定性条件 | | 発散防止の閾値等 |
| **パラメータ** | 臨界変数 | | 微小変動で結果が激変するもの |
| | 頑健変数 | | 広い範囲で機能するもの |
| **境界条件** | 限界密度 | | 崩壊点（ベクトル数、次元数等） |
| | ノイズ耐性 | | 許容SNRの最小値 |
| **実装要件** | 依存ライブラリ | | バージョン依存等 |
| | 計算量 | | O(N^2) 等のスケール特性 |
| **負の知見** | 論文内の失敗例 | | 最も価値のある情報 |
| | 著者が認めた限界 | | 将来課題・未解決問題 |

## TRL 0 検証への移行判定
- [ ] コア方程式が抽出済みか？
- [ ] パラメータの臨界値が特定されているか？
- [ ] 合成データでの再現が可能な程度に情報が揃っているか？
- [ ] ユーザーが TRL 0 検証への進行を承認したか？
```

### 3.2 「負の知見」の優先抽出

> [!TIP]
> 論文内で「うまくいかなかったケース」や「将来の課題」として挙げられている内容は、
> 我々のフェーズ設計において**最も価値のある情報**である。優先的に抽出すること。

---

## 4. サンドボックス検証 (TRL 0 Verification)

精査マトリクスが完成し、ユーザーの承認を得た論文に対して、**本流コードに一切手を加えずに**理論の核心を再現する。

### 4.1 検証環境

```
research_ledger/
└── verifications/
    └── [paper_id]/
        ├── verify_[paper_id].py    ← 独立した検証スクリプト
        ├── results.json            ← 検証結果
        └── VERIFICATION_REPORT.md  ← Gap Analysis
```

### 4.2 検証ルール

1.  **合成データのみ使用**: 直交ベクトル、ランダムベクトル等の合成データで論文のコア主張を再現する。
2.  **我々の環境での再現**: 論文の報告値と、我々のサンドボックスでの結果の差異（Gap）を定量的に記録する。
3.  **ノイズ耐性テスト**: Phase 20で発見した「0.15ノイズフロア」に対する耐性を確認する。
4.  **独立実行**: `hybrid_models.py` および既存のフェーズコードへの依存を**一切持たない**。

### 4.3 検証結果の判定

| 結果 | 判定 | 次のアクション |
| :--- | :--- | :--- |
| 論文の主張が合成データで再現された | **PASS** | Transfer Pathway（セクション5）へ進行 |
| 再現されたが、我々の環境で性能が劣化する | **CONDITIONAL** | 劣化原因を精査マトリクスに追記。ユーザー判断を仰ぐ |
| 再現されない | **FAIL** | 「負の知見」として記録。再挑戦しない |

---

## 5. 転用経路 (Transfer Pathway)

TRL 0検証をPASSした理論を、プロジェクトのフェーズ管理に統合する。

### 5.1 フェーズ・フォーク (Phase Forking)

1.  新規フェーズディレクトリ `experiments/phase_XX_[名称]/` を作成。
2.  TRL 0 の検証スクリプトを基盤として、プロジェクト固有のデータ・ハーネスに接続する。
3.  [PROTOTYPING_POLICY.md](file:///home/tack-mit/デスクトップ/Gemini_projectspace/meta_management/l3_semantic/PROTOTYPING_POLICY.md) のTRLゲートに従い、TRL 1 → TRL 2 → TRL 3 と段階的に検証する。

### 5.2 TRL遷移チェックリスト

TRL 0 (本プロトコル) → TRL 1 (PROTOTYPING_POLICY) への遷移条件：

- [ ] 精査マトリクスが完全に記入されている
- [ ] TRL 0 サンドボックス検証が PASS である
- [ ] 探索台帳の当該エントリが `status: adopted` に更新されている
- [ ] ユーザーの明示的な承認がある
- [ ] KI（Knowledge Item）のドラフトが準備されている

---

## 6. 探索台帳 (Research Ledger)

論文の発見・評価・採用をセッションをまたいで追跡する永続的なレジストリ。

### 6.1 ディレクトリ構成

```
research_ledger/
├── ledger.json              ← 全論文の索引（状態管理）
├── seeds/                   ← 起点となった論文の精査マトリクス
│   └── [paper_id].md
├── candidates/              ← 発見されたが未評価の論文
│   └── [paper_id].md
├── adopted/                 ← 採用済み（KIに昇格した論文）
│   └── [paper_id].md        → KIへのリンクを含む
└── verifications/           ← TRL 0 検証の成果物
    └── [paper_id]/
```

### 6.2 ledger.json スキーマ

```json
{
  "papers": [
    {
      "id": "kuramoto_1975",
      "title": "Self-entrainment of a population of coupled nonlinear oscillators",
      "authors": ["Y. Kuramoto"],
      "year": 1975,
      "discovered_via": "seed:self_rag_2024 → hop:2",
      "collection_mode": "B",
      "scores": {
        "novelty": 5,
        "originality": 5,
        "reproducibility": 3
      },
      "status": "adopted",
      "ki_link": "sync_threshold_theory",
      "child_exploration": "completed",
      "trl0_result": "PASS",
      "last_updated": "2026-04-22"
    }
  ],
  "exploration_frontier": [
    {
      "next_seed": "hopfield_1982",
      "reason": "Associative memory model - potential integration with state-space",
      "priority": "high"
    }
  ]
}
```

### 6.3 ライフサイクル

```
discovered → scored → candidate → [ユーザー承認] → TRL 0 検証
                                                        │
                                          PASS ─────────┼───── FAIL
                                            │                    │
                                        adopted              「負の知見」
                                            │                  として記録
                                      KI化・フェーズ統合
                                            │
                                    新しいSeedとして
                                    子探索サイクル開始
```

### 6.4 セッション間の引き継ぎ

*   各セッションの開始時に `ledger.json` の `exploration_frontier` を確認し、未完の探索を提示する。
*   `child_exploration: "not_started"` のエントリは、次回セッションの候補として自動的に提案される。

---

## 7. トークン予算 (Token Budget)

本プロトコルの各ステップにおける推定トークン消費量。
[AI_USE_POLICY.md](file:///home/tack-mit/デスクトップ/Gemini_projectspace/meta_management/l3_semantic/AI_USE_POLICY.md) のトークン統治ルールに準拠する。

| 活動 | 推定コスト | 推奨モデル |
| :--- | :--- | :--- |
| Step 1: 表層スキャン | ~5-10k tokens | Execution (Flash) |
| Step 2: ユーザー選別 | 0 | - |
| Step 3: 精査マトリクス記入（1論文） | ~30-50k tokens | Execution (Flash) / Thinking |
| Step 4: 外部化 | ~5k tokens | Execution (Flash) |
| TRL 0 検証（1論文） | ~20-30k tokens | Execution (Flash) |
| **1サイクル合計（1論文）** | **~60-95k tokens** | |
| **1セッション上限（3論文）** | **~200-300k tokens** | |

---

*Last Updated: 2026-04-22*
*Status: DRAFT - ユーザー承認待ち*
