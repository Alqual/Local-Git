# 3-Tier Memory Management Architecture

This document formalizes the memory management protocol for {{PROJECT_NAME}}, designed to maintain continuity and optimize project state management.

---

## 🏗 Memory Layers

### 1. Working Memory (L1) - Functional
*   **Focus**: Active Development & Live Experimentation.
*   **Content**: 
    *   Unconfirmed code snippets and trial-and-error scripts.
    *   Current session objective and immediate next steps.
*   **Storage**: `RESEARCH_STATE.md` (Root) and active working directories.

### 2. Episodic Memory (L2) - Historical
*   **Focus**: Fixed Results & Historical Context.
*   **Content**:
    *   Finalized reports documenting project milestones.
    *   Chronological index of achievements and failures.
*   **Storage**: `l2_episodic_dock/PROJECT_STORY.md` and related archival files.

### 3. Semantic Memory (L3) - Theoretical
*   **Focus**: Theory, Explanations, & Distilled Knowledge.
*   **Content**:
    *   Mathematical proofs and theoretical derivations.
    *   General architectural principles and protocols.
*   **Storage**: Distilled spec documents in `meta_management/l3_semantic/` and Knowledge Items.

---

## 🔄 Lifecycle & Transitions

1.  **Exploration**: New ideas start in **Working Memory (L1)**.
2.  **Solidification**: Once verified, progress is moved to **Episodic Memory (L2)** (archiving reports and freezing code).
3.  **Distillation**: Universal principles discovered are abstracted into **Semantic Memory (L3)** as theories or protocols.

---

## 🛠 Usage in Antigravity
At the start of each session, the Agent should:
1.  **Read L1**: Understand the immediate working state.
2.  **Reference L2**: Lookup historical results only when context is missing.
3.  **Inherit L3**: Follow established theoretical principles and protocols.
