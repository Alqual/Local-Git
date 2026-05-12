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
