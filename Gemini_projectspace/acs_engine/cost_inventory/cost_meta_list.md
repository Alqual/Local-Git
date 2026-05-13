# Meta Cost List: Sentinel-Leanstral Budget & Resource Management

This document provides a framework for tracking and optimizing the operational costs of the Sentinel-Leanstral project, including LLM token consumption and infrastructure licensing.

---

## 1. LLM API & Token Costs (Variable)
[Detail: 01_llm_token_optimization.md](file:///home/tack_fr/デスクトップ/Local-Git/cost_inventory/details/01_llm_token_optimization.md)

| Model Tier | Provider | Input Cost ($/1M) | Output Cost ($/1M) | Role in Project |
| :--- | :--- | :--- | :--- | :--- |
| **Gemini 2.5 Flash** | Google Cloud | $0.075 | $0.30 | Primary translator. |
| **Gemini 2.5 Pro** | Google Cloud | $1.25 | $5.00 | Expert reflection loop. |
| **Leanstral (Mistral)** | Mistral AI | (Variable) | (Variable) | Math reasoning expert. |
| **Gemini 3 Flash** | Google Cloud | (Preview) | (Preview) | Sentinel risk monitoring. |

---

## 2. Infrastructure & Tool Licensing (Fixed/Recurring)
[Detail: 02_license_infra_costs.md](file:///home/tack_fr/デスクトップ/Local-Git/cost_inventory/details/02_license_infra_costs.md)

| Item | Type | Cost | Renewal | Role |
| :--- | :--- | :--- | :--- | :--- |
| **Tailscale** | Network | Free Tier | Monthly | Secure inter-node VPN. |
| **GitHub Pro** | Git SSoT | $4 / user | Monthly | High-capacity repository. |
| **Google Cloud** | API Host | (Credit) | - | Centralized API gateway. |

---

## 3. Operational Budget Goals
[Detail: 03_budget_execution_strategy.md](file:///home/tack_fr/デスクトップ/Local-Git/cost_inventory/details/03_budget_execution_strategy.md)

- **Target**: Solve 50 university math problems within a **$50.00 total budget**.
- **Logic**: Hierarchical model usage (Flash -> Pro) and Context Compression to minimize token burn.

---

## 4. Cost Tracking Artifacts
| Artifact Path | Description |
| :--- | :--- |
| `sentinel_core/logs/billing_summary.json` | Weekly automated token usage report. |
| `sentinel_core/cost_analysis.html` | Dashboard showing cost-per-verified-proof. |

---
*Last Updated: 2026-05-11 - Integrated Detailed Cost Metadata*
