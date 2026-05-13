# Section 1: Core Reasoning Engine (ACS Engine)

## Design Philosophy
The ACS (Autonomous Calculation Server) Engine is built on the principle of **"Formalization-as-a-Service"**. Its core goal is to eliminate the manual labor involved in formalizing mathematical problems into Lean 4. It treats the LLM (Gemini/Leanstral) as a "stochastic translator" and the Lean compiler as a "deterministic judge."

## Key Code Features & Implementation Details

### `lean_translator_v4_smart.py`
- **Internal Structure**: A functional Python script utilizing `ThreadPoolExecutor` for parallel problem processing.
- **Key Functions**:
    - `process_problem(prob_data)`: The main orchestration loop. Manages the retry counter (up to 15 attempts) and coordinates between the model and the verifier.
    - `get_reflection_prompt(history)`: A specialized prompt builder that iterates through `history[]`, extracting only the first 100 characters of previous errors to keep the prompt concise while providing context on *what* failed before.
    - `run_lean_verify(code, file_name)`: **The Cross-Node Bridge**. 
        1. Writes code to a local `/tmp` file.
        2. Uses `scp` with `-o StrictHostKeyChecking=no` for seamless transfer to the Ubuntu node.
        3. Executes `lake env lean` via `ssh` and captures both `stdout` and `stderr` for reflection.
- **Algorithm**: **Reflection-Loop with Context Compression**. It uses regex (`r"```lean4?\n(.*?)\n```"`) to extract code blocks from model responses, ensuring robustness against conversational "noise."

### `verify_on_ubuntu.py`
- **Purpose**: A standalone CLI version of the verification logic used for debugging individual `.lean` files without running the full pipeline.
- **Structure**: Simplified SSH-executor that mirrors the `run_lean_verify` logic in the main translator.

### `success_harvester.sh`
- **Mechanism**: A Bash script using `rsync` or `scp` to pull verified results. It filters for files that *do not* contain `sorry` (if configured) to ensure only complete proofs are harvested.

## Configuration & Constants
- `MAX_RETRIES = 15`: High retry limit to allow the model to overcome complex library name hallucinations.
- `CONCURRENCY = 2`: Conservative parallelization to avoid overwhelming the Ubuntu node's CPU during Lean compilation.
- `SSH_TARGET`: Tailscale IP or hostname of the compute node.

## Current Challenges & Future Outlook

### Challenges
- **Library Hallucination**: Models frequently "guess" the names of Mathlib functions (e.g., `EuclideanGeometry.area`) that do not exist or have different names in Mathlib4, leading to unfixable errors.
- **Auto-Implicit Trap**: Unknown identifiers are treated as implicit variables rather than missing functions, confusing the model with secondary `Function expected` errors.
- **Reflection Saturation**: After multiple attempts, the model tends to repeat the same library guess rather than exploring alternative library paths.

### Outlook
- **RAG-Enhanced Feedback**: Instead of raw error messages, provide the model with a list of "actually existing" similar functions from the current Mathlib.
- **Library Guardrails**: Hardcoding key library imports and basic definitions to prevent the model from hallucinating foundational math concepts.
