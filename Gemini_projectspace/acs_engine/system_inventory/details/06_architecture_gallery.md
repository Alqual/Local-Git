# Architecture Gallery: Sentinel-Leanstral

This gallery provides detailed visual and technical breakdowns of the system's architecture, separated by functional components and code logic.

---

## 1. ACS Engine (Component Architecture)
The brain of the system, responsible for mathematical reasoning and formal verification.

![ACS Engine Component](../../assets/architecture_images/acs_engine_component.png)

```mermaid
graph LR
    T[Lean Translator] -->|Generate| V[Lean 4 Verifier]
    V -->|Error Feedback| T
    V -->|Success| H[Success Harvester]
```

---

## 2. Sentinel Monitoring (Component Architecture)
The immune system, ensuring safety and resource optimization through proactive intervention.

![Sentinel Monitoring Component](../../assets/architecture_images/sentinel_monitoring_component.png)

```mermaid
graph TD
    S1[Local Sentinel] ---|Telemetry| M[Main Sentinel Judge]
    M -->|Intervention| S1
    S1 -->|Interlock| Process[ACS Engine Process]
```

---

## 3. Knowledge & State (Component Architecture)
The memory of the system, maintaining a synchronized Single Source of Truth (SSoT).

![Knowledge & State Component](../../assets/architecture_images/knowledge_state_component.png)

```mermaid
graph TB
    G[Git / GitHub] <-->|Sync| L[Local Repo]
    L ---|Append| H[Reflection History JSONL]
    L ---|Append| S[Sentinel History JSONL]
```

---

## 4. Core Reasoning (Code Architecture)
Logic flow between scripts responsible for problem ingestion and proof generation.

![Core Reasoning Code Flow](../../assets/architecture_images/core_reasoning_code_flow.png)

```mermaid
flowchart TD
    MT[lean_translator_v4_smart.py] -->|Triggers| VU[verify_on_ubuntu.py]
    VU -->|SSH/SCP| VT[VerificationTask.lean]
    VT -->|Result| VU
    VU -->|Log| RH[reflection_history.jsonl]
```

---

## 5. Sentinel System (Code Architecture)
Interaction between local monitoring agents and the central judge logic.

![Sentinel Code Architecture](../../assets/architecture_images/sentinel_code_architecture.png)

```mermaid
flowchart TD
    LS[sentinel.py] -->|Telemetry| RS[remote_main_sentinel.py]
    RS -->|Judgment| LS
    LS -->|Action| P[Process Control]
    LS -->|Log| RE[reliability_history.jsonl]
```

---

## 6. Internal Code Architectures
Detailed logic breakdowns for each critical script in the framework.

### A. `lean_translator_v4_smart.py` (The Brain)
Orchestrates parallel translation and the reflection loop.

![Lean Translator Internal](../../assets/architecture_images/lean_translator_internal.png)

```mermaid
graph TD
    subgraph "lean_translator_v4_smart.py"
        P[process_problem] -->|Loop up to 15x| R[Reflection Loop]
        R -->|Build| PB[Prompt Builder]
        PB -->|Context| CC[Context Compression]
        R -->|Execute| RV[run_lean_verify]
        RV -->|SSH/SCP| Remote[Ubuntu Node]
    end
```

### B. `sentinel.py` (The Local Immune System)
Real-time log monitoring and autonomous intervention.

![Sentinel Internal](../../assets/architecture_images/sentinel_internal.png)

```mermaid
graph TD
    subgraph "sentinel.py"
        T[Log Tailer] -->|New Action| J[AI Risk Judge]
        J -->|Evaluate| P[Security Policy]
        J -->|Verdict| I[Intervention Logic]
        I -->|DANGER| K[pkill antigravity]
    end
```

### C. `verify_on_ubuntu.py` (The Bridge)
Standalone verification runner for remote Lean 4 compilation.

![Verify on Ubuntu Internal](../../assets/architecture_images/verify_on_ubuntu_internal.png)

```mermaid
graph LR
    subgraph "verify_on_ubuntu.py"
        LC[Local Command] -->|SSH| S[SSH Server]
        S -->|Execute| LB[lake build]
        LB -->|Return| LC
    end
```

### D. `remote_main_sentinel.py` (The Judge)
Distributed resource monitoring and node-level safety.

![Remote Main Sentinel Internal](../../assets/architecture_images/remote_main_sentinel_internal.png)

```mermaid
graph TD
    subgraph "remote_main_sentinel.py"
        RP[Remote Poller] -->|SSH| N1[Node A: ps/free]
        RP -->|SSH| N2[Node B: ps/free]
        RP -->|Data| CA[Central Aggregator]
        CA -->|Alert| D[Monitoring Dashboard]
    end
```

### E. `success_harvester.sh` (The Collector)
Automated aggregation of verified mathematical proofs.

![Success Harvester Internal](../../assets/architecture_images/success_harvester_internal.png)

```mermaid
graph LR
    subgraph "success_harvester.sh"
        RC[Result Collector] -->|RSYNC| Remote[Compute Node]
        Remote -->|Proofs| SF[Sorry-Filter]
        SF -->|Clean| VPR[Valid Proof Repo]
        SF -->|Incomplete| EDR[Discard Repo]
    end
```
