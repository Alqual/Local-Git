# Component 4: Visualization & Human-in-the-Loop UI

## Component Mission
To provide an interactive "Cockpit" that allows human users to observe, judge, and intervene in the system's autonomous activities.

## UI Architecture
1.  **Data Ingestion**: A Bash script `update_data_js.sh` flattens the latest `reflection_history.jsonl` and `telemetry.jsonl` into a Javascript file `data.js`.
2.  **Frontend Engine**: Static HTML files use vanilla Javascript to load `data.js` and render interactive charts using **Chart.js**.
3.  **Visualization Pillars**:
    - **Performance**: Real-time CPU/Memory usage per node.
    - **Progress**: Translation success rates (University vs. Year).
    - **Reasoning**: Deep-dive view into the specific failed Lean code and the compiler errors.

## Feedback Mechanism
The UI is currently a "Passive Cockpit" (Read-only). Human oversight is achieved by the user reading the dashboard and then giving new instructions to the Antigravity agent in the chat.

## System-Level Challenges & Outlook
- **Data Freshness**: The dashboard only updates when the JS export script is run.
- **Actionability**: No direct "Button" to stop a process or restart a problem from the browser.
- **Outlook**: "Active Control Surface". Adding a lightweight Python backend (FastAPI/Flask) to allow the dashboard to send commands back to the system (e.g., "Redo Kyushu Q5").
