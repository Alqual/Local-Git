# AI Use Policy: Optimization & Ethics

This policy governs the behavior, resource usage, and role assignment of AI agents participating in the Lossless AI project. It aims to maximize research fidelity while maintaining strict quota and context discipline.

---

## 1. Multi-Model Role Assignment (モデルの役割分担)

To optimize cost and reasoning depth, tasks are assigned to specific model tiers based on their complexity.

| Unit Type | Target Models | Responsibility | Primary Metrics |
| :--- | :--- | :--- | :--- |
| **Execution Unit** | Gemini Flash | Refactoring, testing, metadata sync, repetitive coding, documentation. | Tokens Per Second (TPS), Accuracy. |
| **Thinking Unit** | Gemini 3.1 Pro / Sonnet 4.6 | Analytical reasoning, theoretical synthesis, failure log diagnosis, strategic planning. | Reasoning Depth, Context Fidelity. |

---

## 2. Escalation Protocol (エスカレーション規律)

The Execution Unit must not attempt to "brute-force" solutions to unforeseen errors or theoretical contradictions.

1.  **Iterative Limit**: A maximum of **3 iterative attempts** are allowed for a single code fix or bug resolution.
2.  **Diagnostic Trigger**: Upon the 3rd failure, the Execution Unit must:
    -   **HALT** all write operations immediately.
    -   **Package State**: Create a "Diagnostic Package" containing the failed code, the complete error trace, and the hypothesized cause.
    -   **Escalate**: Request a Thinking Unit (or User Scrutiny) to analyze the package before any further attempts.
3.  **Cross-Mode Transition**: Moving from "Execution Mode" to "Thinking Mode" requires a dedicated "State Reflection Step" to avoid carry-over of incorrect assumptions.

---

## 3. Token Governance & Context Hygiene (トークン統治と衛生)

We maintain a "Lean Context" to prevent token bloat and maintain the Signal-to-Noise Ratio (SNR).

### 3.1 Model-Specific Performance (モデル別性能特性)

各モデル層の物理的・論理的限界を理解し、タスクを割り当てる。

| モデル層 | コンテクスト容量 | クオータ制約 (TPM) | SNR特性 | 推奨タスク |
| :--- | :--- | :--- | :--- | :--- |
| **Execution (Flash)** | 高 (1M+) | **低** (高速・多量) | **低** (肥大化で精度低下) | Light 〜 Medium |
| **Thinking (Pro)** | 極高 (2M+) | **高** (低速・少量) | **高** (大容量でも高品質) | Medium 〜 Heavy |

### 3.2 Token Lifespan Estimation (トークン消費の目安と制限)

| タスクの重み | 推定トークン量 | ターゲットモデル | 限界時のリスク |
| :--- | :--- | :--- | :--- |
| **Light** (同期法) | ~10k | Flash | リスクなし |
| **Medium** (修正) | ~50k | Flash | **SNR低下**: 連続実行で精度が落ちる |
| **Heavy** (解析) | 200k〜500k | Pro | **クオータ枯渇**: 数回の実行で API 制限 |

*   **Selective Reading**: Do not read binary files or non-essential library code (e.g., `local_libs/`) unless explicitly required.
*   **Log Externalization**: Experimental logs exceeding 50 lines must be summarized for the active context, with the full log moved to external storage (L2 or AWS/DB).
*   **Predictive Budgeting**: For high-risk operations (Browser research, large file processing), the Agent must state a "Token Budget" before execution.

---

## 4. Ethical Standards & Scrutiny

*   **Transparency**: Every AI-generated theory or significant architectural change must be accompanied by its "TRL Status" (see PROTOTYPING_POLICY.md).
*   **Non-Reversibility**: AI agents must ensure that all destructive operations (deleting code, overwriting history) are reversible or backed up in L2 before execution.
*   **The Golden Sign-off**: No major version increment or core library merge is final without explicit User approval.

---
*Last Updated: 2026-04-20*
