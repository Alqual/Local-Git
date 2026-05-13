# Test Category 1: Mathematical Verification (ACS Engine)

## Test Objective
To ensure that generated Lean 4 code is mathematically sound and adheres to the latest Mathlib4 standards without human intervention.

## Detailed Test Procedures

### MATH-01: Lean Compilation Test
- **Method**: The `verify_on_ubuntu.py` script sends the code to the Ubuntu node and runs `~/.elan/bin/lake env lean /tmp/remote_file.lean`.
- **Pass Criteria**: `returncode == 0`. Any non-zero exit code (errors or warnings) is treated as a failure.
- **Internal Logic**: The script captures the `stderr` and maps it to the specific line number in the source code to provide feedback to the model.

### MATH-02: Reflection Loop Stress
- **Method**: Picking problems known to have high complexity (e.g., coordinate geometry with 20+ steps).
- **Metric**: **Success-at-K**. We measure how many attempts ($K$) it takes for the model to reach a zero-error state.
- **Fail Condition**: If the model enters an infinite loop of library name guessing without progressing.

### MATH-03: Gold Standard Benchmark
- **Method**: Running a "Comparison Script" that checks if the machine-generated proof follows a similar logical structure to the `verified_gold/` proofs.
- **Objective**: To prevent "cheat proofs" where the model uses `sorry` or local hacks.

## Challenges & Outlook
- **Tactic Timeout**: Some proofs are so complex that `lake` times out after 60s.
- **Outlook**: Implementing "Tactical Timeout Adjustment," where the system automatically increases the compilation timeout for known hard problems.
