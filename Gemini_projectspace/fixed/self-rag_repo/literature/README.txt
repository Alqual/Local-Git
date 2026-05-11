README
======

このフォルダには、ハイブリッド型無損失AIアーキテクチャ研究に
関連する論文・技術資料のサーベイ資料が格納されています。

ファイル一覧
-----------
literature_survey.md   - 全10トピックの論文サーベイ（推奨読破順付き）

調査トピック
-----------
A. 長文コンテキスト・階層記憶（古典層）
   - MemGPT (arXiv:2310.08560)
   - Infini-Attention (arXiv:2404.07143) ★最重要
   - Titans (arXiv:2501.00663)
   - KVキャッシュ圧縮サーベイ (arXiv:2412.19442)

B. 状態空間モデル・再帰型（古典層の軽量代替）
   - Mamba (arXiv:2312.00752) ★最重要
   - RetNet (arXiv:2307.08621)

C. 位置符号化・時間性の表現
   - RoPE / RoFormer (arXiv:2104.09864)

D. 確率的・物理的散逸モデル（量子層の理論基盤）
   - Stochastic Gradient Langevin Dynamics (Welling & Teh, ICML 2011)
   - Lindblad マスター方程式（量子開放系理論）

E. ベクトル象徴記憶（量子層の関連概念）
   - Holographic Reduced Representations / Hyperdimensional Computing
