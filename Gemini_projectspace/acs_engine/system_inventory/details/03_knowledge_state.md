# Component 3: Knowledge & State Management (SSoT)

## Component Mission
To maintain a consistent, synchronized "Single Source of Truth" across all nodes and throughout the project's history.

## State Synchronization Mechanism
1.  **Code (GitHub)**:
    - Central repository on GitHub acts as the authoritative source for all scripts and logic.
    - Alma node pulls from GitHub and distributes to Ubuntu.
2.  **Activity (JSONL Logs)**:
    - `reflection_history.jsonl` acts as the persistent "Memory" of reasoning attempts.
    - It is kept on the Alma node's local filesystem to avoid Git bloat but is indexed for UI visualization.
3.  **Research (Activity Reports)**:
    - `activity_report.md` and `RESEARCH_STATE.md` provide human-readable state tracking.

## Resilience Features
- **Append-Only Logging**: Using JSONL ensures that even if a process is killed mid-write, previous logs remain intact.
- **Node-Local Backups**: Utility scripts are backed up to `/sentinel_core/local_git_scripts_backup/` to prevent accidental loss during Git operations.

## System-Level Challenges & Outlook
- **Log Bloat**: As the project scales, single JSONL files will exceed several gigabytes.
- **Sync Latency**: Keeping Ubuntu and Alma code perfectly in sync during rapid development cycles.
- **Outlook**: "Distributed State Database". Transitioning from JSONL files to a lightweight distributed database (like Redis or SQLite-over-NFS) for sub-millisecond state updates across the cluster.
