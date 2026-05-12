# Session Initialization Template

This template ensures the agent starts with the correct context and objectives. Using this at the beginning of a session minimizes investigation overhead and prevents task drift.

---

## [SESSION GOAL DECLARATION]

### 1. Primary Objective
*   **Goal**: (e.g., Finalize the math reasoning loop implementation)
*   **Success Criteria**: (e.g., Successfully verify 3 sample problems in Lean 4)

### 2. Context & Memory Focus
*   **Relevant Files**: (e.g., `acs_engine/core/reasoning.py`)
*   **Previous Session ID/Topic**: (e.g., "The discussion about Flash-to-Pro hierarchy from yesterday")
*   **Current State**: (e.g., "I just pushed from Ubuntu, need to sync to Alma")

### 3. Operational Constraints
*   **Scope**: (e.g., ONLY touch documentation, do not modify logic files yet)
*   **Authority**: (e.g., Autonomous investigation allowed for Git sync; all edits require approval)
*   **Budget/Tokens**: (e.g., Use Gemini 1.5 Flash for routine tasks; reserve Pro for final verification)

### 4. Preferred Output Format
*   **Reporting**: (e.g., Update `task.md` and provide a concise summary at each step)
*   **Communication**: (e.g., Keep responses brief and technical)

---

## Agent Usage Guide
When an agent receives this template:
1.  **Acknowledge the Goal**: Confirm understanding of the primary objective.
2.  **Verify Context**: Immediately run the [Multi-Node Sync Investigation Protocol](file:///home/tack_fr/デスクトップ/Local-Git/agent_inventory/details/01_sync_investigation_protocol.md) if multi-node sync is implied.
3.  **Establish Baseline**: Report on the current state of "Relevant Files" to confirm parity with the user's mental model.
4.  **Execution Strategy**: Propose an initial micro-plan based on the stated constraints.
