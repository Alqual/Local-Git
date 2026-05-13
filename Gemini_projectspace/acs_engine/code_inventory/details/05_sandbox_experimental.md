# Section 5: Sandbox & Experimental Scripts

## Design Philosophy
The Sandbox is a **"Protected Playground"**. It acknowledges that innovation requires breaking things. By isolating experimental loops and university-specific logic here, we prevent "experimentation noise" from degrading the stability of the core ACS Engine.

## Key Code Features & Implementation Details

### `sandbox/run_loop.py`
- **Internal Loop**:
    - Uses a `while True` or `for _ in range(N)` wrapper around the `process_problem` logic.
    - **Logic**: Implements a "Batch Mode" where it picks 5 random unsolved problems and tries to solve them simultaneously.
    - **Characteristic**: More aggressive error logging than the main engine, printing full stack traces for every failure.

### `sandbox/run_osaka_logic.py`
- **Specialization**:
    - Pre-loads the prompt with Osaka University's specific mathematical style (often involving complex coordinate geometry).
    - Includes a local "Lemma Library" that isn't yet in the main Mathlib, acting as a prototype for the "RAG-Enhanced Feedback" concept.

### `scripts/tit_2022_search.py`
- **Mechanism**:
    - A Python script using `requests` and `BeautifulSoup`.
    - **Algorithm**: Specifically searches for "Tokyo Tech 2022 Math Problems" on educational portal sites, extracts the raw Japanese text, and converts it into the `jp_exams_raw` JSONL format.

## Technical Characteristics
- **Isolated Execution**: Scripts here are often self-contained and don't rely on the full project infrastructure, allowing for rapid debugging.
- **Disposable**: Code here is intended to be refactored into the core or discarded once the experiment concludes.

## Current Challenges & Future Outlook

### Challenges
- **Specialized Library Testing**: Experiments like `run_osaka_logic.py` suffer from lack of access to specific geometry/linear algebra lemmas that the model *expects* but are missing.
- **Manual Heuristic Tuning**: The sandbox requires human intuition to "guess" why a specific university problem fails, which is slow.

### Outlook
- **Automated Lemma Discovery**: A sandbox utility that searches Mathlib for keywords found in the model's failed code to suggest "correct" library paths.
- **Heuristic Benchmarking**: Automatically running sandbox scripts against "Gold Standard" proofs to measure improvement quantitatively.
