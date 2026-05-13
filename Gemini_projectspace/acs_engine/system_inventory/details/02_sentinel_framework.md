# Component 2: Sentinel Monitoring Framework

## Component Mission
To ensure the security and stability of the autonomous cluster by detecting risky actions and resource exhaustion before they cause system-wide failure.

## Monitoring Hierarchy

### Level 1: Local Watchdog (`sentinel.py`)
- **Location**: Runs locally on Alma/Ubuntu.
- **Role**: Immediate response. It reads the raw log files of the AI agent and assesses risk using a dedicated, low-latency LLM.
- **Intervention**: Can kill local processes instantly.

### Level 2: Remote Judge (`remote_main_sentinel.py`)
- **Location**: Runs on Mac.
- **Role**: Cluster health. It looks for "Silence" (heartbeat loss) or "Cluster-wide Spikes" (multi-node memory exhaust).
- **Intervention**: Can remotely reboot nodes or trigger global "Stop" signals.

## Risk Assessment Logic
1.  **Event**: A command like `rm -rf /` is detected in the session log.
2.  **Analysis**: The action is sent to the Sentinel AI (Gemini 3 Flash).
3.  **Policy Check**: The AI compares the action against `security_policy.md`.
4.  **Verdict**: `SAFE`, `WARNING`, or `DANGER`.
5.  **Action**: If `DANGER`, the "interlock" fires, killing the agent.

## System-Level Challenges & Outlook
- **Interlock Sensitivity**: High-load translation attempts can look like "Denial of Service" attacks to a naive monitor.
- **Outlook**: "Task-Contextual Monitoring". The ACS Engine will "announce" its resource-heavy phases to Sentinel, allowing for temporary threshold relaxation.
