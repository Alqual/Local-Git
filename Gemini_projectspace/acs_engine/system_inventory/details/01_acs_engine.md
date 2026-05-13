# Component 1: ACS (Autonomous Calculation Server) Engine

## Component Mission
To autonomously solve, formalize, and verify mathematical problems by bridging natural language reasoning with formal machine-verified logic (Lean 4).

## Internal Logic Flow: The Reflection Loop
1.  **Ingestion**: Picks a problem from `jp_exams_raw` JSONL.
2.  **Inference**: Sends problem + system instructions to the Reasoning Model (Gemini/Leanstral).
3.  **Cross-Node Execution**:
    - Alma node creates a temp Lean file.
    - `scp` transfers it to Ubuntu.
    - `ssh` triggers `lake env lean` on Ubuntu.
4.  **Error Parsing**: Stderr is captured and analyzed for specific Lean errors (e.g., `unknown identifier`).
5.  **Reflection**: If compilation fails, the error is fed back to the model for attempt $N+1$.
6.  **Persistence**: On success, the file is moved to `final_successes/`.

## Key Dependencies
- **Lean 4 (Lake/Elan)**: Must be installed and configured in the environment on the Ubuntu node.
- **Mathlib4**: The core library for mathematical definitions; its version must match the model's training data for high success rates.

## System-Level Challenges & Outlook
- **Tactic Hallucination**: The model assumes high-level tactics exist that are not yet in Mathlib.
- **Library Discrepancy**: The Ubuntu node's Mathlib version might differ from what the model "thinks" is current.
- **Outlook**: "Knowledge-Injected Reasoning". Before the model starts, the system will automatically inject relevant Mathlib function signatures into the prompt.
