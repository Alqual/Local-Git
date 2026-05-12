# Sentinel-Leanstral Infrastructure: Comprehensive Requirement Document

**Date:** 2026-05-12  
**Status:** Baseline Specification (Derived from Integrated Review v2)  
**Version:** 1.0.0

---

## 1. Project Mission & Strategic KPIs
The **Sentinel-Leanstral Framework** is a distributed autonomous system designed to achieve high-performance mathematical reasoning through Lean 4 formal verification, supported by a proactive, hierarchical monitoring layer.

### Core Objectives
*   **The Self-Evolving Mathematician**: Ingest natural language mathematical problems and produce machine-verifiable Lean 4 proofs with minimal human intervention.
*   **Hierarchical Stability**: Maintain 99.9% uptime of the compute cluster through an autonomous "Immune System" (Sentinel).

### Key Performance Indicators (KPIs)
*   **Cost Efficiency**: Target an average cost of **$1.00 USD per verified proof**.
*   **Success Rate**: Achieve a >80% verification success rate for "Silver Tier" mathematical problems within 15 reflection attempts.
*   **Safety**: Zero instances of unauthorized API usage or resource exhaustion through hard-kill interlocks.

---

## 2. Infrastructure & Architectural Requirements

### 2.1 Node-Role Specifications
| Node | Name | Environment | Primary Requirement |
| :--- | :--- | :--- | :--- |
| **Control Node** | Alma | Alma Linux 10 | Orchestration, Git Management, Dashboard Hosting. Must be the SSoT for configuration. |
| **Compute Node** | Ubuntu | Ubuntu 24.04 | High-intensity Lean 4 compilation & LLM inference. Requires 100GB+ SSD for Mathlib artifacts. |
| **Judge Node** | Mac | macOS | Independent watchdog. Must operate on a separate power/network cycle if possible. |

### 2.2 Network & Security Requirements
*   **Encryption**: All inter-node communication must traverse a **Tailscale WireGuard** overlay.
*   **Access Control**: SSH access via Ed25519 keys only. **Requirement**: Implement command-level restrictions (rssh) to limit agents to `python3`, `scp`, and `lake` prefixes.
*   **Secret Management**: **CRITICAL**: No plain-text API keys in scripts. All secrets must be loaded via `.env` files or system environment variables.

---

## 3. Functional Requirements

### 3.1 ACS Engine (Autonomous Calculation Server)
*   **Translation**: Multi-stage translation from Natural Language -> Informal Lean -> Formal Lean 4 (Mathlib4 compliant).
*   **Verification**: Integration with `lake exe` to verify proofs.
*   **Reflection Loop**: Autonomous error-correction loop. 
    *   **Requirement**: Implement **Regex-based error extraction** to identify specific Lean 4 tactic failures.
    *   **Requirement**: Implement **Dead-end Detection** to abort attempts early if the model repeats the same error 3+ times.
*   **Checkpointing**: **Requirement**: Save the "Reasoning State" every 5 minutes or per-attempt to prevent data loss during long-running sessions.

### 3.2 Sentinel Monitoring System
*   **Telemetry**: Real-time tracking of CPU, Memory, Disk I/O, and API usage on all nodes.
*   **Active Signaling**: **Requirement**: Implement a "Heartbeat + Task-Context" protocol. The ACS Engine must signal the Sentinel when starting a "High-Intensity" task to prevent false-positive security triggers.
*   **Interlocks**: Sentinel must possess "Kill-Switch" authority to terminate `antigravity` or `python3` processes if resource thresholds (e.g., 90% RAM) are exceeded.
*   **Reliability**: **Requirement**: All Sentinel core scripts must be managed as `systemd` services with `Restart=always` policies.

### 3.3 Visualization & Control (The Cockpit)
*   **Data Latency**: **Requirement**: Transition from "Passive Log Polling" to "Push Telemetry" (WebSocket or similar) to reduce dashboard latency to <5 seconds.
*   **Active Oversight**: **Requirement**: The UI must allow manual "Intervention" (Kill/Restart/Retry) directly from the browser surface.
*   **Financial Tracking**: Weekly billing reconciliation reports must be automatically generated and displayed.

---

## 4. Data & Logic Integrity Requirements

### 4.1 Serialization & Communication
*   **Protocol**: Standardize all cross-node communication on **JSON-Schema**.
*   **Network Partition Resilience**: **Requirement**: Implement a "Local Buffer & Sync" protocol. If Ubuntu loses connection to Alma, it must queue results locally and sync upon reconnection.

### 4.2 Code Standards & Maintenance
*   **Repository Integrity**: **Requirement**: 100% of project logic (including Sentinel core) must reside within the `Local-Git` repository. No "Shadow Code" in `/home/tack_fr/`.
*   **Environment Parity**: **Requirement**: Maintain `requirements.txt` (Python) and `lakefile.lean` (Lean) as locked dependency manifests.
*   **Path Abstraction**: Remove all hardcoded absolute paths (`/home/tack_fr/...`). Use relative paths or a central `config.toml`.

---

## 5. Cost Governance & Optimization

### 5.1 Model Strategy
*   **Standardization**: Consistently utilize **Gemini 3 Flash** as the primary reasoning engine.
*   **Hierarchical Escalation**: Only escalate to "Pro" models after 5 failed attempts with "Flash," and only if "Progress" is detected in the reflection log.

### 5.2 Efficiency Features
*   **Context Caching**: **Requirement**: Implement **Prompt Caching** for Mathlib4 imports and foundational definitions to reduce token overhead by ~80%.
*   **Hard-Kill Credit Limit**: Implement a session-level dollar limit. If a single proof attempt exceeds $5.00, the process must self-terminate regardless of reflection status.

---

## 6. Verification Plan
*   **Automated Tests**: Unit tests for regex-based error extraction and JSON-Schema validation.
*   **Stress Test**: 100-cycle "Reliability Marathon" to verify `systemd` auto-restarts and local buffering.
*   **Security Audit**: Automated scan for hardcoded strings resembling API keys before every Git push.

---
*Created by: Antigravity (AI Architect)*  
*Ref: system_meta_list.md, integrated_system_review_report.md*
