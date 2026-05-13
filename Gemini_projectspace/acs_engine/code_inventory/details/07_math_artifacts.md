# Section 7: Mathematical Artifacts (Lean Proofs)

## Design Philosophy
This is the **"Vault of Verified Truth"**. Unlike the code, which is transient, these artifacts represent the tangible intellectual output of the project. They follow a hierarchy of verification: from raw machine output to "Gold Standard" human-verified benchmarks.

## Artifact Taxonomy & Quality Standards

### `final_successes/`
- **Validation Criteria**: Must compile with `lake env lean` with a return code of 0.
- **Internal Structure**: 
    - Header: `import Mathlib`, `open Real`, `open BigOperators`.
    - Body: A single `theorem` or `lemma` statement matching a university exam problem.
    - Status: Often contains "Proof-by-Tactic" (e.g., `aesop`, `linarith`).

### `verified_gold/`
- **Source**: Curated from expert Lean contributors or manually corrected by the user.
- **Purpose**: Used as the reference "few-shot" examples in the `lean_translator_v4_smart.py` system prompt.

### `lean_translations/`
- **Management**: This is a volatile directory where the output of the reflection loop is stored before final verification. It serves as the "drafting board."

## Technical Characteristics
- **Self-Contained**: Ideally, each Lean file should be standalone or depend only on `Mathlib`, ensuring long-term portability.
- **Semantic Structure**: Files are named according to University and Year (e.g., `Kyushu_2015_1.lean`) for easy indexing.

## Current Challenges & Future Outlook

### Challenges
- **"Hallucination-Inside" Proofs**: Some proofs compile but use `sorry` or "fake" lemmas that the model defined locally to bypass errors, making them "invalid gold."
- **Import Dependency Chaos**: Proofs often lack the correct `open` or `import` statements because the model doesn't know the exact file hierarchy of Mathlib.

### Outlook
- **Recursive Verification**: A script that re-verifies "successful" proofs by stripping all local definitions and forcing reliance on Mathlib only.
- **Proof-Style Linter**: Implementing a style checker to ensure machine-generated proofs meet the readability standards of the "Gold" set.
