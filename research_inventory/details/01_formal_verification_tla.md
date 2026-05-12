# Research Detail: Formal Verification with TLA+/TLC

## 1. Overview
This research focused on applying formal methods to verify the reliability of the core logic in the Sentinel-Leanstral framework. By using **TLA+** (Temporal Logic of Actions) and the **TLC** Model Checker, we mathematically proved the soundness of the system's self-correction loops.

## 2. Target Component
- **File**: `Gemini_projectspace/acs_engine/scripts/lean_translator_v4_smart.py`
- **Logic**: The **Reflection (Self-Correction) Loop**, which manages LLM code generation, Lean 4 verification, and smart retries.

## 3. Methodology
- **Specification**: Formalized the state transitions using TLA+ syntax.
- **Verification**: 
    1. Initial exhaustive state space search using a custom Python script (Mini-TLC).
    2. Rigorous model checking using the official **TLC Model Checker** on a portable Java 21 environment.
- **Properties Verified**:
    - **Safety (Invariants)**: The retry count never exceeds the predefined `MAX_RETRIES` limit.
    - **Liveness (Termination)**: The system is guaranteed to reach a terminal state (`PASS` or `FAIL_FINAL`) and will not stutter or loop indefinitely under weak fairness assumptions.

## 4. Key Findings
- **Fairness Requirement**: TLC identified that without "Weak Fairness" (the guarantee that an enabled action is eventually taken), a theoretical stuttering loop could exist. This insight ensures that our implementation must have robust progress-guaranteed loops.
- **State Space**: The model checked 32 distinct states across a search depth of 17, with zero errors found.

## 5. Artifacts
- [ReflectionLoop.tla](../formal_verification/ReflectionLoop.tla): The formal TLA+ specification.
- [ReflectionLoop.cfg](../formal_verification/ReflectionLoop.cfg): TLC configuration for the model.
- [verify_logic.py](../formal_verification/verify_logic.py): Custom Python-based model checking script.

## 6. Execution Environment
- **Java**: OpenJDK 21 (Portable JRE in `java_home/`)
- **TLC**: `tla2tools.jar` (v1.8.0)
