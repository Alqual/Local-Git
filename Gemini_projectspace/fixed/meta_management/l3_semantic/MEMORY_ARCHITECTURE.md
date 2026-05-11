# 3-Tier Memory Management Architecture

This document formalizes the memory management protocol for the Lossless AI project, designed to maintain continuity while optimizing computational and context quota.

---

## 🏗 Memory Layers

### 1. Working Memory (L1)
*   **Focus**: Active Prototyping & Live Experimentation.
*   **Content**: 
    *   Unconfirmed code snippets and trial-and-error scripts.
    *   Current session objective and immediate next steps.
    *   State of the most recent experiment (e.g., current Phase 20 files).
*   **Storage**: `RESEARCH_STATE.md` (Root) and active `experiments/` subdirectories.

### 2. Episodic Memory (L2)
*   **Focus**: Fixed Results & Historical Context.
*   **Content**:
    *   Finalized reports documenting successful (or productively failed) experiments.
    *   Chronological index of project milestones.
    *   Snapshots of the code at specific milestones.
*   **Storage**: `docs/PROJECT_STORY.md` and related `.md` files in the `docs/` directory.

### 3. Semantic Memory (L3)
*   **Focus**: Theory, Explanations, & Distilled Knowledge.
*   **Content**:
    *   Mathematical proofs and theoretical derivations (e.g., Orthogonality Theory).
    *   Discovered "Laws of Physics" for the embedding space (e.g., optimal thresholds).
    *   General architectural principles.
*   **Storage**: `.gemini/antigravity/knowledge/` (Knowledge Items) and formal spec documents.

---

## 🔄 Lifecycle & Transitions

1.  **Exploration**: New ideas start in **Working Memory**.
2.  **Solidification**: Once an experiment is verified, it is moved to **Episodic Memory** (a report is written and the code is "fixed").
3.  **Distillation**: Universal principles discovered during Episodic solidification are abstracted into **Semantic Memory** as theories or Knowledge Items.

---

## 🛠 Usage in Antigravity
At the start of each fresh session, the Agent should:
1.  **Read L1**: Understand the immediate working state from `RESEARCH_STATE.md`.
2.  **Reference L2**: Lookup historical results only when a "Memory Gap" is identified.
3.  **Inherit L3**: Automatically receive summaries of Semantic KIs to maintain foundational understanding.
