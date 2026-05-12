# Code Inventory & Metadata List

This document provides a comprehensive overview of all scripts and code artifacts created within the Sentinel and Leanstral projects.

## 1. Core Reasoning Engine (ACS Engine)
[Detail: 01_core_reasoning.md](file:///home/tack_fr/デスクトップ/Local-Git/code_inventory/details/01_core_reasoning.md)

| File Path | Language | Purpose |
| :--- | :--- | :--- |
| `scripts/lean_translator_v4_smart.py` | Python | **Main Engine**: Orchestrates math problem translation using Gemini with smart retry logic. |
| `scripts/verify_on_ubuntu.py` | Python | **Node Link**: Triggers Lean 4 compilation on the Ubuntu node via SSH. |
| `scripts/success_harvester.sh` | Bash | **Result Collector**: Aggregates successful Lean files from compute nodes. |
| `scripts/debug_translate.py` | Python | Utility for testing translation prompts on single problems. |
| `lean_verify/lakefile.lean` | Lean 4 | Configuration for the Lean 4 verification project on Ubuntu. |
| `lean_verify/VerificationTask.lean` | Lean 4 | The primary file where Leanstral/Gemini attempts proofs for verification. |

## 2. Sentinel Monitoring System
[Detail: 02_sentinel_monitoring.md](file:///home/tack_fr/デスクトップ/Local-Git/code_inventory/details/02_sentinel_monitoring.md)

| File Path | Language | Purpose |
| :--- | :--- | :--- |
| `sentinel.py` | Python | **Sub-Sentinel**: Local monitoring agent running on Ubuntu/Alma. |
| `remote_main_sentinel.py` | Python | **Main-Sentinel**: Distributed judge logic running on Mac. |
| `ubuntu_telemetry.py` | Python | Telemetry collector for Ubuntu node resource monitoring. |
| `sentinel_reliability_test.py` | Python | Stress test suite for Sentinel's intervention capabilities (TC-3.1–3.4). |
| `chaos_stresser.py` | Python | Tool for simulating system failures and resource exhaustion. |
| `sentinel_dashboard.html` | HTML/JS | Real-time visual dashboard for monitoring Sentinel state. |

## 3. Environment & Maintenance
[Detail: 03_env_maintenance.md](file:///home/tack_fr/デスクトップ/Local-Git/code_inventory/details/03_env_maintenance.md)

| File Path | Language | Purpose |
| :--- | :--- | :--- |
| `scripts/fix_session.sh` | Bash | Utility to clear corrupted session cookies and lockfiles. |
| `scripts/update_data_js.sh` | Bash | Synchronizes reflection history with the dashboard UI. |
| `model_settings/leanstral_vibe.toml` | TOML | Configuration for Mistral Vibe and the Leanstral model. |

## 4. Research, Concept & Policy Documents
[Detail: 04_research_policy.md](file:///home/tack_fr/デスクトップ/Local-Git/code_inventory/details/04_research_policy.md)

| File Path | Language | Purpose |
| :--- | :--- | :--- |
| `AUTONOMOUS_CALC_SERVER_CONCEPT.md` | Markdown | **Vision**: High-level conceptual design of the autonomous calculation server. |
| `sentinel_core/security_policy.md` | Markdown | **Policy**: Defines security protocols and intervention triggers for Sentinel. |
| `sentinel_core/environment_roles.md` | Markdown | **Architecture**: Detailed roles and specifications for each compute/control node. |
| `sentinel_core/RESEARCH_STATE.md` | Markdown | **Tracker**: Ongoing log of research questions, hypotheses, and experimental states. |
| `sentinel_core/sentinel_capability_report_final.md` | Markdown | **Report**: Final summary of the Sentinel reliability stress tests. |

## 5. Sandbox & Experimental Scripts
[Detail: 05_sandbox_experimental.md](file:///home/tack_fr/デスクトップ/Local-Git/code_inventory/details/05_sandbox_experimental.md)

| File Path | Language | Purpose |
| :--- | :--- | :--- |
| `sandbox/run_loop.py` | Python | Experimental loop for continuous translation attempts. |
| `sandbox/run_osaka_logic.py` | Python | Specialized logic test for Osaka University entrance exam problems. |
| `sandbox/test_lean_runner.py` | Python | Unit test for the Lean 4 execution and error parsing logic. |
| `scripts/tit_2022_search.py` | Python | Scraper/Search utility specifically for Tokyo Tech 2022 problems. |

## 6. Logs & History Data (JSONL/JS)
[Detail: 06_logs_history.md](file:///home/tack_fr/デスクトップ/Local-Git/code_inventory/details/06_logs_history.md)

| File Path | Language | Purpose |
| :--- | :--- | :--- |
| `sentinel_core/reflection_history.jsonl` | JSONL | **Lean History**: Detailed logs of every translation attempt and self-correction. |
| `sentinel_core/reliability_history_v3_others.jsonl` | JSONL | **Sentinel History**: Logs from the latest multi-node reliability tests. |
| `sentinel_core/data.js` | Javascript | Flattened data exported for the HTML dashboards. |

## 7. Mathematical Artifacts (Lean Proofs)
[Detail: 07_math_artifacts.md](file:///home/tack_fr/デスクトップ/Local-Git/code_inventory/details/07_math_artifacts.md)

| Directory | Content |
| :--- | :--- |
| `sentinel_core/final_successes/` | Successfully translated and verified Lean 4 files. |
| `sentinel_core/verified_gold/` | Manually curated "Golden" proofs for benchmarking. |
| `sentinel_core/lean_translations/` | Raw output from various model attempts. |

## 8. Web & Visualization
[Detail: 08_web_visualization.md](file:///home/tack_fr/デスクトップ/Local-Git/code_inventory/details/08_web_visualization.md)

| File Path | Language | Purpose |
| :--- | :--- | :--- |
| `sentinel_core/math_pipeline_dashboard.html` | HTML/JS | Dashboard for tracking Lean translation progress and success rates. |
| `sentinel_core/sentinel_monitor_v3_others.html` | HTML/JS | Advanced telemetry viewer for the distributed sentinel network. |
| `sentinel_core/sentinel_monitor_v3_others_deepdive.html` | HTML/JS | **New**: Deep-dive telemetry for specific node clusters. |
| `sentinel_core/sentinel_analysis.html` | HTML | **New**: Post-hoc stress test analysis report visualizer. |
| `sentinel_core/launcher.html` | HTML | Entry point for accessing various project dashboards. |

---
*Last Updated: 2026-05-11 22:50 (Integrated detailed metadata and new visualization artifacts)*
