# Meta-Memory Management Policy

This policy defines the structural integrity, storage lifecycle, and synchronization rules for the 3-Tier Memory Architecture (L1, L2, L3). It ensures information is preserved with maximum fidelity while optimizing prompt context.

---

## 1. Information Lifecycle (情報のライフサイクル)

Data must flow through the layers based on its maturity and relevance.

| Layer | Type | Retention | Transition Rule |
| :--- | :--- | :--- | :--- |
| **L1 (Working)** | Volatile | Transient (Session-bound) | Move to L2/L3 upon session closure or phase settlement. |
| **L2 (Episodic)** | Stable | Persistent (Immutable History) | Archive successful prototypes and failure logs from L1. |
| **L3 (Semantic)** | Evolving | Persistent (Theory/Specs) | Distill universal principles from L2 into KIs or architectural specs. |

---

## 2. Lossless Externalization (状態の外部化)

To maintain a "Lossless" environment without bloating the LLM prompt, we utilize **External Reference Pointers**.

1.  **Trigger Limits**:
    -   **Logs**: >1,000 lines must be moved to `fixed/l2_episodic_dock/logs/` or external DB (AWS).
    -   **Code Snapshots**: Large intermediate versions should be stored in `workspace/sandbox/` or `fixed/l2_episodic_dock/TRL_Archive/` and referenced by URI.
2.  **Pointer Protocol**:
    -   When data is externalized, L1 must maintain a "Metadata Handle" (URI + Checksum + 3-sentence Summary).
    -   The agent must be able to "Re-hydrated" the context by reading the URI only when specific detailed analysis is required.

---

## 3. Multi-Model Handover Protocol

When transitioning between Execution and Thinking units (or sessions), context must be preserved using a **Hierarchical Briefing**.

-   **Structure**: 
    -   `Goal`: The current high-level objective.
    -   `State Map`: URIs to active working files.
    -   `Constraint Delta`: Any new constraints discovered in the current session.
    -   `Next Action`: The immediate next atomic step.
-   **Lossless Requirement**: Do not summarize away edge cases or "unsolved errors"; these must be passed as "Open Items."

---

## 4. The Golden Sign-off (ファイナライズ)

A research phase is only considered "SETTLED" when:
1.  **Registry Sync**: `registry.json` is updated via `L2Archiver`.
2.  **Theory Anchoring**: L3 Spec files are updated to reflect the new state.
3.  **User Scrutiny**: The user has provided explicit approval (Golden Sign-off) after reviewing the settlement report.

---
*Last Updated: 2026-04-20*
