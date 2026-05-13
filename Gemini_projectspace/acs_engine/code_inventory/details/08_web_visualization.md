# Section 8: Web & Visualization

## Design Philosophy
Visualization is the **"Cockpit"** of the project. By transforming abstract logs into visual dashboards, we enable human-in-the-loop oversight at a glance. It follows a "Dashboard-as-App" approach, where static HTML/JS files act as full-featured monitoring tools.

## Key UI Components & Frontend Logic

### `math_pipeline_dashboard.html`
- **Dashboard Logic**:
    - Uses **Chart.js** to render bars showing "Attempts per Problem."
    - **Features**: A filterable table that allows sorting by University and "Attempt Count."
    - **Logic**: Reads `historyData` from `data.js` and performs a `reduce` operation to aggregate stats by university.

### `sentinel_monitor_v3_others.html`
- **Internal Logic**:
    - **Telemetry Engine**: Uses a periodic `setInterval` to re-fetch/parse the telemetry data points.
    - **Visuals**: Draws multi-line charts showing the correlation between "Memory Consumption" and "Number of Active Lake Processes."

### `capability_dashboard_deepdive.html`
- **Implementation**:
    - A **Radar Chart** or **Spider Web Chart** visualization showing scores for `Syntax`, `Reasoning`, `Library Knowledge`, and `Connectivity`.

### `launcher.html`
- **Frontend Detail**: A simple, card-based CSS grid that acts as a central hub for all `sentinel_core` HTML tools. It includes tooltips explaining what each dashboard monitors.

## Technical Characteristics
- **Client-Side Heavy**: Uses vanilla JS and libraries (like Chart.js or Mermaid.js) to render data directly from `data.js` without a backend server.
- **Responsive Design**: Optimized for viewing on Alma Linux (GNOME) or Mac (Retina) displays.

## Current Challenges & Future Outlook

### Challenges
- **Error Hallucination Heatmap**: The current dashboards show "Success/Fail" but don't visualize *which* libraries are being hallucinated most frequently.
- **UI Lag**: As the number of reflection attempts grows, the `data.js` file size increases, leading to slow rendering in the browser.

### Outlook
- **Interactive Error Explorer**: Clicking a "Fail" bar in the dashboard should pull up the specific Lean error and the model's failed "library guess."
- **Data Pagination**: Splitting the dashboard data into "Session-specific" files to keep the visualization snappy.
