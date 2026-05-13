# Test Category 3: Infrastructure & Maintenance Pulse

## Test Objective
To ensure that the distributed environment is "Always Ready" for computation and that maintenance scripts are effective.

## Detailed Test Procedures

### INFRA-01: SSH/SCP Pulse
- **Method**: Running a script that transfers a 1MB dummy file and executes `uptime` on all nodes.
- **Metric**: "Round-Trip Time" (RTT). Ensures that Tailscale latency isn't degrading the translation loop speed.

### INFRA-02: Session Repair Validation
- **Method**: Manually creating a `.lock` file in the browser directory.
- **Expected Result**: `fix_session.sh` should detect the lock, kill the associated PID, and remove the file cleanly.
- **Pass Criteria**: Successful browser launch after script execution.

### INFRA-03: Dashboard Data Integrity
- **Method**: Injecting a complex JSON object with nested quotes into `reflection_history.jsonl`.
- **Expected Result**: `update_data_js.sh` must escape the quotes correctly such that `data.js` remains a valid Javascript file and the dashboard renders without console errors.

## Challenges & Outlook
- **Zombie Processes**: Some SSH sessions hang, leaving "Ghost" processes on the Ubuntu node.
- **Outlook**: "Distributed Heartbeat". A background service that periodically cleans up stale SSH tunnels and temporary `/tmp/remote_*` files.
