# Prototyping Policy: Advanced R&D Standards

This policy governs the **Precedent Research and Development (先行研究開発)** phases of the Lossless AI project. Its primary goal is not "system stability," but the **"Discovery of Principles"** and **"Mapping of Physical Limits (TRL 1-3)."**

---

## 1. TRL-Based Stage Management (成熟度段階管理)

We manage all experimental activities according to **Technology Readiness Levels (TRL)** to ensure theoretical rigor before implementation.

*   **TRL 0**: External theory discovered and verified in sandbox ([RESEARCH_PROTOCOL.md](file:///home/tack-mit/デスクトップ/Gemini_projectspace/fixed/meta_management/l3_semantic/RESEARCH_PROTOCOL.md)).
*   **TRL 1**: Basic principles observed and reported (Mathematical axioms).
*   **TRL 2**: Technology concept and application formulated (Phase 20 Design).
*   **TRL 3**: Analytical and experimental proof of concept/principle (Current Phase).

**Rule**: No prototype shall jump to TRL 1 without passing a TRL 0 Gate. No prototype shall jump to TRL 3 without passing a TRL 2 Gate.
**Incremental Preservation Rule**: Each TRL stage has independent value. Upon completion of a TRL stage, the resulting code and reports MUST be moved from `workspace/` to `fixed/` (e.g., `fixed/l2_episodic_dock/TRL_Archive/`) before proceeding to the next stage.

---

## 2. Fidelity Matching (問外不一致の回避)

The fidelity of a prototype must strictly match the research question being asked. **Over-engineering at early stages is a risk to scientific clarity.**

| Research Tier | Target Question | Prototype Fidelity | Data Type |
| :--- | :--- | :--- | :--- |
| **Tier A (PoP)** | Does the physical law hold? | **Low (Analytical)** | Synthetic orthogonal vectors. |
| **Tier B (PoC)** | Does language fit the law? | **Mid (Logic)** | Small semantic clusters (10-20 sentences). |
| **Tier C (Integn)** | Can the agent use it? | **High (System)** | Full Model Inference Loop. |

### 🛑 Rule of Negative Results (ネガティブ・リザルトの許容)
A proven physical limit (knowing why it breaks) is a successful discovery. **DO NOT silently brute-force parameters to force a success.**
*   **Scientific Discipline**: If an experiment fails at a specific Tier, document the exact mathematical or logical failure as a "Negative Result."
*   **Operational Protocol**: Refer to [AI_USE_POLICY.md](file:///home/tack-mit/デスクトップ/Gemini_projectspace/fixed/meta_management/l3_semantic/AI_USE_POLICY.md) for iterative limits and escalation procedures.

---

## 3. Evaluation Harness First (計測器先導型開発)

In advanced R&D, the **Measurement Device** is as important as the **Experiment**.

*   **Rule**: Before executing a new prototype, we must establish or refine the **Evaluation Harness**.
*   **Harness Requirements**:
    *   Standardized metrics (SNR, Cluster Distance, Memory Entropy).
    *   Automated plotting of "Breaking Points" (Failure Mapping).
    *   Reproducible data input buffers.
*   **🎯 Harness Calibration Rule**: Before running the real experiment, the Harness MUST be calibrated using a "Trivial Baseline" (e.g., completely random vectors, or perfectly identical vectors). If the Harness cannot accurately measure this baseline, the experiment cannot proceed.
*   **Goal**: Ensure that results are objective and comparable across different phases, avoiding "one-off" success.

---

## 4. Sandbox Isolation & Scrutiny (Gatekeeper Loop)

### 🟦 Sandbox Isolation
*   Never modify "Fixed" core libraries during a prototyping phase.
*   Work in `workspace/sandbox/phaseXX/` with standalone or local copies of libraries.

### 🟦 Scrutiny Package
The Agent must present the following for User Scrutiny **before** any execution:
1.  **Hypothesis**: What principle are we testing?
2.  **The Harness**: How will we measure failure?
3.  **The Code**: Logic and hard-coded parameters ($\tau, K, \mu$).
4.  **TRL Target**: Which maturity level are we aiming for?

---

## 5. Settlement: The 3-Layer Output Model (収束プロトコル)

Once a prototype experiment is finalized, we must transition from the "Sandbox State" to the "Settled State." This is a high-rigor process focused on **Non-Reversibility (非可逆性)** and **Asset Generation (資産化)**.

### 🟦 5.1 Semantic Anchoring (知見の定着)
*   **Action**: Update Knowledge Items (KIs) in L3.
*   **Goal**: Capture mathematical invariants and the "Why." Ensure "Re-constructibility" (theory documented so the system can be rebuilt from scratch if code is lost).

### 🟦 5.2 Episodic Archiving (履歴の永久保存)
*   **Action**: Seal the `RESEARCH_WORKFLOW_XX.md` Audit Log and Scrutiny Packages into L2.
*   **Goal**: Provide an immutable evidence chain to prevent future re-work or task meltdown.

### 🟦 5.3 Functional Hardening (機能の硬化と資産化)
*   **Action**:
    1.  Transition verified `proto` code to the core library (e.g., `hybrid_models.py`).
    2.  Execute **Regression Scrutiny**: Ensure new logic doesn't degrade previous Phase milestones.
*   **Goal**: Turn "disposable code" into a "Stable Project Asset."

### 🟦 5.4 Final Settlement Scrutiny (最終妥当性精査)
*   **Action**: Present the updated 3-Layer state to the User for the "Golden Approval."
*   **Requirement**: Explicit USER sign-off is required before the Phase is considered "CLOSED."