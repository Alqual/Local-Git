# Self-RAG Low-Level アーキテクチャ図解 (System & Memory Layer)

先ほどの構成図は「意味的なデータの流れ（High-level）」に寄りすぎていました。
ここではシステムエンジニア・組込（ECU）の視点に落とし込み、**「どのメモリ（RAM/VRAM）に何が格納され、どこで同期待ち（ブロッキング）が発生し、状態（ステート）がどう遷移するか」**という、実コード（Low-level）のシーケンスとステートマシンとして描き直しました。

---

## 1. Low-level シーケンスダイアグラム (関数とメモリのやり取り)

LLMの推論の本質は、「文字列」ではなく「整数配列（`List[int]`）」の操作と、GPU上のKVキャッシュメモリへの連続的な書き込みに過ぎません。外部通信（RAG）は、この同期的なWhileループへの割り込み（Interrupt / Halt）として実装されています。

```mermaid
sequenceDiagram
    autonumber
    participant State as System Buffer (RAM)<br/>`str` / `List[int]`
    participant Tokenizer as Tokenizer (CPU)<br/>Byte-Pair Encoding
    participant Engine as vLLM / GPU Engine<br/>Tensor & KV Cache (VRAM)
    participant Router as Main Script<br/>Python `while` Synchronous Loop
    participant Faiss as FAISS Index (RAM)<br/>L2 Distance Array

    Note over State, Engine: --- Bootstrap Phase ---
    State->>Tokenizer: input_string (User q)
    Tokenizer-->>State: `input_ids` = [1, 5634, ...] (int array)
    State->>Engine: input_ids を転送 (KV Cache メモリ領域確保)

    Note over State, Engine: --- Auto-Regressive Token Loop ---
    loop Until `next_token_id` == EOS
        Engine-->>Router: Forward Pass 完了 -> Logits [Vocab_size] 確率配列
        Router->>Router: argmax(Logits) -> `next_token_id` 確定
        
        alt `next_token_id` == `[Retrieval]` (特殊ID: 32001)
            Router->>Router: [割り込み] 推論ループを強制Halt (WAIT_RETRIEVAL)
            Router->>Faiss: 現在の文脈ベクトルで L2_Search(QueryText)
            Faiss-->>Router: Top-K のドキュメント文字列を返却
            Router->>State: 元の入力 + 検索結果文字列をバインド (format_prompt)
            State->>Tokenizer: 新しい長文を 再エンコード
            Tokenizer-->>State: 新生 `new_input_ids` 配列
            Router->>Engine: KV Cache を破棄し、新しい配列で再スケジュール (Re-allocate)
            
        else `next_token_id` == `[Relevant]` / `[Fully supported]` 等
            Router->>Router: [評価記録] 該当スコアを変数ログに蓄積
            Router->>State: `next_token_id` をバッファ末尾に Append
            State->>Engine: GPUに対して「1トークン分インクリメント」指示 (KV Cache更新)
            
        else 通常の言語トークン（Word ID）
            Router->>State: `next_token_id` をバッファ末尾に Append
            State->>Engine: GPUに対して「1トークン分インクリメント」指示 (KV Cache更新)
        end
    end
    
    Note over State, Tokenizer: --- Finalize Phase ---
    Router-->>State: `final_token_ids` 配列完成
    State->>Tokenizer: デコード処理 (int -> UTF-8 String)
    Tokenizer-->>State: Final Response (Text)
```

### Low-level 視点での重要ポイント
- **情報は完全にステートレス**: LLM自体（Engine）は過去の「記憶」を一切持ちません。全ては毎ターン更新される `KV Cache` という行列メモリと、常にSystem Buffer（RAM）側で管理されている `input_ids` の配列状態に依存しています。
- **検索の正体は「コンテキストの再構築（破壊的変更）」**: `[Retrieval]` が発生すると、GPU側の計算を一度捨ててでも、System Buffer（State）側で配列構造を組み直し、再度GPUに流し込んでいることがわかります。

---

## 2. 実装移植用 状態遷移マシン（State Flow）

フロントエンド（React / TypeScript）やバックエンド（Node.js / Rust）へ移植し、情報損失を完全にコントロールする層を作る場合、構築すべき状態遷移（ステートマシン）は以下の設計となります。

```mermaid
stateDiagram-v2
    [*] --> INIT_BUFFER: ユーザー入力受付
    
    state "Tokenization (UTF-8 to Int)" as TOKENIZATION
    state "GPU Forward Pass Matrix Calc" as GPU_CALC
    state "Logits Evaluation (argmax)" as EVAL_LOGITS
    
    INIT_BUFFER --> TOKENIZATION: バッファ転送
    TOKENIZATION --> GPU_CALC: KV Cache確保
    
    GPU_CALC --> EVAL_LOGITS: 1 Step(Token)完了
    
    state EVAL_LOGITS {
        direction LR
        Check_ID: Check `token_id`
    }
    
    EVAL_LOGITS --> UPDATE_CACHE: Word ID (通常)
    EVAL_LOGITS --> LOG_CRITIQUE: Critique ID ([Relevant] 等)
    EVAL_LOGITS --> HALT_RETRIEVAL: Retrieval ID (検索要請)
    EVAL_LOGITS --> DECODE_OUTPUT: EOS ID (終了判定)
    
    UPDATE_CACHE --> GPU_CALC: ステップ再帰 (Auto-regressive)
    LOG_CRITIQUE --> UPDATE_CACHE: 状態ログ更新後、再帰
    
    state "Halt & External Access" as HALT_RETRIEVAL
    HALT_RETRIEVAL --> UPDATE_BUFFER: FAISSからベクトル引当
    
    state "Buffer Re-Formatting" as UPDATE_BUFFER
    UPDATE_BUFFER --> TOKENIZATION: Context配列の上書き
    
    DECODE_OUTPUT --> [*]: クライアントへ送信
```

### なぜこれが入出力制御（損失制御）の最適化に繋がるのか？
- このLow-levelなフローから見えてくるのは、**「いつ、どのタイミングで、どの情報をバッファ（Buffer）に混ぜるか・捨てるか」**という主導権は、完全に外側の `Router (State Machine)` 側にあるという事実です。
- LLMの内部アルゴリズムには手を加えずとも、この外側の状態遷移マシンを「厳格に型付け・制御する」だけで、LLMに不要な情報を削ぎ落とし、本当に評価してほしいベクトルだけを注入する（損失を最適化する）ことが可能になる構造です。
