# Meta System List: Sentinel-Leanstral Framework

## 1. System Overview
The **Sentinel-Leanstral Framework** is a distributed, multi-node autonomous environment designed for high-performance mathematical reasoning, formal verification (Lean 4), and proactive system monitoring.

### System Vision
To create a "Self-Evolving Mathematician" that can ingest natural language problems, translate them into machine-verifiable proofs, and autonomously maintain the stability of its distributed compute cluster.

---

## 2. Infrastructure & Node Architecture (The Skeleton)
[Detail: 00_infrastructure_architecture.md](file:///home/tack_fr/デスクトップ/Local-Git/system_inventory/details/00_infrastructure_architecture.md)

| Node Name | Role | Primary Responsibility | Environment |
| :--- | :--- | :--- | :--- |
| **Alma (Main)** | Control Plane | Orchestration, Git Management, UI Hosting | Alma Linux 10 |
| **Ubuntu (Compute)** | Data Plane | Lean 4 Compilation, LLM Execution (Vibe/Leanstral) | Ubuntu 24.04 |
| **Mac (Judge)** | Watchdog Plane | Remote Monitoring, Intervention Judgment | macOS |

---

## 3. Core Sub-Systems (The Components)

### A. ACS (Autonomous Calculation Server) Engine
[Detail: 01_acs_engine.md](file:///home/tack_fr/デスクトップ/Local-Git/system_inventory/details/01_acs_engine.md)
- **Role**: The "Brain" of the system.
- **Function**: Translates math problems to Lean 4, performs cross-node verification, and executes the "Reflection Loop" for self-correction.

### B. Sentinel Monitoring Framework
[Detail: 02_sentinel_framework.md](file:///home/tack_fr/デスクトップ/Local-Git/system_inventory/details/02_sentinel_framework.md)
- **Role**: The "Immune System" of the system.
- **Function**: Monitors system telemetry, detects security/resource risks, and executes autonomous interlocks.

### C. Knowledge & State Management (SSoT)
[Detail: 03_knowledge_state.md](file:///home/tack_fr/デスクトップ/Local-Git/system_inventory/details/03_knowledge_state.md)
- **Role**: The "Memory" of the system.
- **Function**: Ensures all nodes are synchronized and maintains a detailed history of reasoning.

### D. Visualization & Human-in-the-Loop UI
[Detail: 04_visualization_ui.md](file:///home/tack_fr/デスクトップ/Local-Git/system_inventory/details/04_visualization_ui.md)
- **Role**: The "Cockpit" of the system.
- **Function**: Transforms raw log data into actionable insights for the user.

---

## 4. Operational Flow (The Pulse)
1. **Request**: Problem picked from `jp_exams_raw` on Alma.
2. **Reasoning**: Alma triggers translation on Ubuntu via SSH.
3. **Verification**: Ubuntu runs `lake` to verify the generated Lean code.
4. **Monitoring**: Sentinel monitors CPU/Memory on Ubuntu/Alma during the heavy compilation.
5. **Reflection**: If verification fails, Ubuntu sends errors back to Alma for a new translation attempt.
6. **Commit**: Successes are pulled to Alma and pushed to GitHub.

---

## 5. Security & Safety Boundaries
- **Inter-node Auth**: Ed25519 SSH keys (no passwords).
- **Intervention Protocol**: Sentinel can kill `antigravity` processes if security policy is violated.
- **Network**: Tailscale encrypted overlay network.

---
*Last Updated: 2026-05-11 - Integrated Detailed Component Metadata*
