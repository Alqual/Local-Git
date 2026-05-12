# Section 3: Environment & Maintenance

## Design Philosophy
This section follows the **"Clean Hands"** principle. By moving session-specific "grime" (cookies, temp logs, dashboard data) into a dedicated management area, we ensure the core source code repository remains lightweight and reproducible. It aims to make system recovery as simple as running a single script.

## Key Code Features & Implementation Details

### `fix_session.sh`
- **Internal Logic**:
    - Targets the `lock` and `Cookies` files in `~/.config/Antigravity`.
    - Uses `fuser -k` or `pkill` to ensure no browser processes are holding the SQLite database before attempting cleanup.
    - Prevents the "Profile in Use" error that often blocks session restarts on Linux.

### `update_data_js.sh`
- **Implementation**:
    - A Bash wrapper that runs a small Python snippet to convert `reflection_history.jsonl` into a single `var historyData = [...]` assignment in `data.js`.
    - Handles escaping of special characters and newlines within the Lean code blocks to ensure the Javascript dashboard doesn't break during rendering.

### `leanstral_vibe.toml`
- **Configuration Keys**:
    - `model`: Maps to the `labs-leanstral-2603` identifier.
    - `vibe_mode`: Configured for "Reasoning-Heavy" output.
    - `ssh_config`: Defines how the Vibe tool should reach the Ubuntu node for local execution tests.

## Technical Characteristics
- **Idempotency**: Scripts like `fix_session.sh` can be run multiple times without causing side effects.
- **Portability**: Designed to work across Alma, Ubuntu, and Mac with minimal adjustments.

## Current Challenges & Future Outlook

### Challenges
- **Log Fragmentation**: When multiple reflection loops run in parallel, logs can become interleaved or corrupted, making the `update_data_js.sh` parsing fragile.
- **Persistent Lockfiles**: Some Lean/Lake processes leave lockfiles on the Ubuntu node that prevent subsequent runs, requiring manual `rm` despite existing fix scripts.

### Outlook
- **Atomic Log Management**: Moving to a database-backed log system (e.g., SQLite) to ensure data integrity during high-load sessions.
- **Comprehensive Cleanup**: Enhancing `fix_session.sh` to forcefully release file handles on the remote compute node before starting new tasks.
