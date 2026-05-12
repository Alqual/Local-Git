# Meta Test List: Sentinel-Leanstral Verification Suites

This document provides a comprehensive overview of the testing protocols, stress tests, and verification suites used to ensure the reliability and accuracy of the Sentinel-Leanstral Framework.

---

## 1. Mathematical Verification (ACS Engine Tests)
[Detail: 01_math_verification_tests.md](file:///home/tack_fr/デスクトップ/Local-Git/test_inventory/details/01_math_verification_tests.md)

| Test ID | Name | Target | Method |
| :--- | :--- | :--- | :--- |
| **MATH-01** | Lean Compilation Test | Generated `.lean` files | `lake env lean <file>` on Ubuntu node. |
| **MATH-02** | Reflection Loop Stress | `lean_translator_v4_smart.py` | Attempting complex problems over 15+ retries. |
| **MATH-03** | Gold Standard Benchmark | `verified_gold/` set | Comparing against human-verified "Ground Truth." |
| **MATH-04** | Sandbox Logic Test | `sandbox/run_osaka_logic.py` | Testing university-specific heuristics. |

---

## 2. Sentinel Reliability & Security Tests
[Detail: 02_sentinel_reliability_tests.md](file:///home/tack_fr/デスクトップ/Local-Git/test_inventory/details/02_sentinel_reliability_tests.md)

| Test ID | Name | Target | Method |
| :--- | :--- | :--- | :--- |
| **SENT-01** | TC-3.1: CPU Stress | `cpu_stresser.py` | Spawning high-CPU loads for throttling test. |
| **SENT-02** | TC-3.2: Memory Leak | `chaos_stresser.py` | Simulating OOM conditions for interlock test. |
| **SENT-03** | TC-3.3: Risk Evaluation | `sentinel.py` | Executing suspicious commands for AI risk test. |
| **SENT-04** | TC-3.4: Multi-Node Sync | `remote_main_sentinel.py` | Testing remote judge response. |

---

## 3. Infrastructure & Maintenance Tests
[Detail: 03_infrastructure_maintenance_tests.md](file:///home/tack_fr/デスクトップ/Local-Git/test_inventory/details/03_infrastructure_maintenance_tests.md)

| Test ID | Name | Target | Method |
| :--- | :--- | :--- | :--- |
| **INFRA-01** | SSH Connectivity Pulse | `verify_on_ubuntu.py` | Verifying auth and SCP speed. |
| **INFRA-02** | Session Recovery Test | `fix_session.sh` | Verifying script-based browser repair. |
| **INFRA-03** | Dashboard Data Sync | `update_data_js.sh` | Verifying JSONL-to-JS conversion integrity. |

---

## 4. Test Reporting & Artifacts
| Artifact Path | Description |
| :--- | :--- |
| `sentinel_core/sentinel_capability_report_final.md` | Summary of the latest 100-cycle stress test results. |
| `sentinel_core/reliability_history.jsonl` | Raw time-series data of test events and interventions. |
| `sentinel_core/sentinel_analysis.html` | Visual representation of failure rates and response latencies. |

---
*Last Updated: 2026-05-11 - Integrated Detailed Test Metadata*
