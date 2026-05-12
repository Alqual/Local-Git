# Cost Category 1: LLM Token & API Optimization

## Component Mission
To maximize mathematical reasoning depth while minimizing the financial "burn rate" associated with high-parameter LLM APIs.

## 1. LLM Pricing Matrix (Actual Rates)
Based on current API benchmarks (as of mid-2025), the following rates are used for budget calculations.

| Model Tier | Identifier | Input Cost ($/1M) | Output Cost ($/1M) | Context Threshold |
| :--- | :--- | :--- | :--- | :--- |
| **Gemini 1.5 Flash** | `gemini-1.5-flash` | $0.075 | $0.30 | ≤ 128K |
| **Gemini 2.0 Flash** | `gemini-2.0-flash` | $0.10 | $0.40 | - |
| **Gemini 1.5 Pro** | `gemini-1.5-pro` | $1.25 | $5.00 | ≤ 128K |
| **Mistral Large 2** | `mistral-large-2407` | $2.00 | $6.00 | - |

> [!IMPORTANT]
> For **Gemini 1.5 Pro**, if the prompt length exceeds **128K tokens**, the costs double to **$2.50 (Input)** and **$10.00 (Output)** per million tokens.

---

## 2. Optimization Strategies

### A. Context Compression Logic (The $O(N^2)$ to $O(N)$ Fix)
- **Mechanism**: The `get_reflection_prompt` function in `lean_translator_v4_smart.py` implements a sliding-window history. It keeps only the latest compiler error in full, while summarizing previous $N-1$ attempts.
- **Financial Impact**: A typical 15-attempt reflection loop without compression would cost ~10x more than a compressed one.

### B. Hierarchical Model Escalation
- **Phase 1 (The Workhorse)**: `Gemini 1.5 Flash` is used for the first 5 attempts. At $0.075/1M, it allows for virtually "free" syntax exploration.
- **Phase 2 (The Expert)**: If Flash fails 5 times, the system switches to `Gemini 1.5 Pro` or `Leanstral`. At $1.25/1M, we limit the number of attempts here to prevent budget spikes.

---

## 3. Cost-Per-Problem Simulation
Target: **$1.00 per verified proof** (Average).

| Scenario | Model Sequence | Total Token Estimate | Estimated Cost |
| :--- | :--- | :--- | :--- |
| **Simple Success** | 1x Flash (Attempt 1) | 5,000 | **$0.001** |
| **Normal Retry** | 5x Flash (Attempt 5) | 25,000 | **$0.005** |
| **Hard Proof** | 5x Flash + 3x Pro | 40,000 | **$0.125** |
| **Critical Failure** | 5x Flash + 10x Pro | 80,000 | **$0.450** |

**Conclusion**: Within a $1.00 per problem budget, the system can afford over **15 attempts with Pro** if necessary, provided the context remains under the 128K double-billing threshold.

---

## 4. Challenges & Outlook
- **Zombie Quota Blocks**: Free-tier Gemini 3 Flash (Preview) has a legacy RPD (Requests Per Day) limit of 20, which can halt the pipeline.
- **Outlook**: "Cache-Aware Prompting". Using Gemini's context caching ($0.025/1M read) to store large Mathlib definitions that are reused across every translation attempt.
