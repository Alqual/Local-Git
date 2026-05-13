# Section 2: Sentinel Monitoring System

## Design Philosophy
Sentinel is designed as a **"Hierarchical Immune System"** for distributed compute clusters. It operates on the philosophy that a system must be self-aware of its resource limits and capable of autonomous intervention (interlocks) to prevent catastrophic failure (OOM, lockups). It separates the "Observer" (Sub-Sentinel) from the "Judge" (Main-Sentinel).

## Key Code Features & Implementation Details

### `sentinel.py`
- **Internal Structure**: A continuous-loop Python agent that "tails" the session logs.
- **Key Logic**:
    - `get_latest_conversation_id()`: Dynamically scans `/home/tack_fr/.gemini/antigravity/brain` to find the active session by modification time.
    - `check_risk(action_text)`: **The AI Judge**. Calls Gemini (model `gemini-3-flash-preview`) with the current `security_policy.md` as context to evaluate every `run_command` or `write_to_file` call found in the logs.
    - `intervene(risk_level, reason)`: **The Executioner**. If `risk_level == "DANGER"`, it executes `pkill -f antigravity` to halt the system and writes to `SECURITY_ALERT.md`.
- **Characteristic**: Uses `f.seek(0, os.SEEK_END)` to implement a high-performance `tail -f` equivalent, ensuring it only analyzes new actions.

### `remote_main_sentinel.py`
- **Purpose**: Runs on the Mac "Judge" node.
- **Mechanism**: Connects to the Alma/Ubuntu nodes via SSH to poll `ps` and `free -m` output. It acts as a fail-safe in case the local `sentinel.py` is killed by an OOM event.

### `sentinel_reliability_test.py`
- **Implementation**:
    - Uses `chaos_stresser.py` to spawn controlled "leak" processes.
    - Records the time between "Stress Start" and "Sentinel Kill" to calculate the **Response Latency**.
    - Outputs results to `reliability_history.jsonl` for dashboard visualization.

## Configuration & Constants
- `BASE_DIR`: Path to the Antigravity session brain.
- `RISK_LEVELS`: `SAFE`, `WARNING`, `DANGER`.
- `pkill -f antigravity`: The hard-stop command for intervention.

## Current Challenges & Future Outlook

### Challenges
- **Compilation vs. Zombie Detection**: Lean compilation spikes CPU and Memory similarly to a runaway process; Sentinel needs to know the "context" of a task to avoid killing a legitimate 5-minute proof compilation.
- **Reflection Load**: High-frequency reflection loops (10+ attempts) can cause sustained resource pressure that triggers aggressive interlocks.

### Outlook
- **Task-Aware Signaling**: ACS Engine should send a "Heavy Task Start" signal to Sentinel to temporarily relax thresholds for specific PIDs.
- **Predictive Interlocks**: Using log history to predict how much memory a specific problem *should* take and intervening only if it exceeds that historical bound.
