# Meta Component-Code Mapping

This document provides the definitive mapping between the high-level **System Components** and the low-level **Code Files/Artifacts**. It serves as the bridge between the architecture and the implementation.

---

## 1. ACS (Autonomous Calculation Server) Engine
| Component Layer | Primary Code Files | Supporting Files |
| :--- | :--- | :--- |
| **Reasoning Loop** | `lean_translator_v4_smart.py` | `debug_translate.py`, `get_reflection_prompt` (logic) |
| **Cross-Node Bridge** | `verify_on_ubuntu.py` | `success_harvester.sh` |
| **Formal Logic Env** | `lakefile.lean` | `VerificationTask.lean`, `Main.lean` |
| **Knowledge Base** | `jp_exams_raw/*.jsonl` | `special_univ_2005_2015.jsonl` |

---

## 2. Sentinel Monitoring Framework
| Component Layer | Primary Code Files | Supporting Files |
| :--- | :--- | :--- |
| **Local Watchdog** | `sentinel.py` | `security_policy.md` |
| **Remote Judge** | `remote_main_sentinel.py` | `mac_governor.py`, `ubuntu_telemetry.py` |
| **Chaos/Testing** | `sentinel_reliability_test.py` | `chaos_stresser.py`, `cpu_stresser.py` |
| **Analytical Reporting** | `sentinel_analyzer.py` | `sentinel_full_reporter.py` |

---

## 3. Knowledge & State Management (SSoT)
| Component Layer | Primary Code Files | Supporting Files |
| :--- | :--- | :--- |
| **Project Memory** | `reflection_history.jsonl` | `reliability_history_v3_others.jsonl` |
| **Architecture / SSoT** | `project_blueprint.md` | `system_meta_list.md`, `activity_report.md` |
| **Research Logs** | `RESEARCH_STATE.md` | `AUTONOMOUS_CALC_SERVER_CONCEPT.md` |
| **Configuration** | `leanstral_vibe.toml` | `node_configs/*.md` |

---

## 4. Environment Maintenance & Utilities
| Component Layer | Primary Code Files | Supporting Files |
| :--- | :--- | :--- |
| **Session Repair** | `fix_session.sh` | (Antigravity Config) |
| **Data Sync** | `update_data_js.sh` | `force_update_dashboard.py` |
| **Scrapers / Discovery** | `tit_2022_search.py` | `sandbox/run_osaka_logic.py` |

---

## 5. Visualization & UI
| Component Layer | Primary Code Files | Supporting Files |
| :--- | :--- | :--- |
| **Main Cockpit** | `math_pipeline_dashboard.html` | `data.js` |
| **Sentinel HUD** | `sentinel_monitor_v3_others.html` | `sentinel_dashboard.html`, `sentinel_logs.html` |
| **Capability Deepdive** | `capability_dashboard_deepdive.html` | `sentinel_analysis.html` |
| **Navigation Hub** | `launcher.html` | (Various .html links) |

---
*Last Updated: 2026-05-11 - Mapping Components to Code Artifacts*
