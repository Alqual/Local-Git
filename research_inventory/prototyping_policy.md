# Prototyping & Experimentation Policy

This document outlines the core methodology and guidelines for developing new features, scripts, and reasoning loops within the Sentinel-Leanstral project. It ensures that innovation remains safe, cost-effective, and reproducible.

---

## 1. The "Sandbox-to-Engine" Workflow
We follow a strict tiered approach for code maturity.

1.  **Tier 1: Sandbox (Exploration)**
    - **Goal**: Test a new idea (e.g., a new geometry prompt).
    - **Policy**: Use standalone scripts in `sandbox/`. Don't worry about clean code; worry about "Proof-of-Concept."
2.  **Tier 2: Refinement (Integration)**
    - **Goal**: Port successful sandbox logic into the `acs_engine`.
    - **Policy**: Add error handling, SSH robustness, and standardized logging.
3.  **Tier 3: Core (Standardization)**
    - **Goal**: Move logic into stable orchestration scripts.
    - **Policy**: Full documentation and registration in the `code_inventory`.

---

## 2. Experimental Principles

### A. Failure-Oriented Development
- **Policy**: A "failed" proof is not a loss; it is a data point. 
- **Action**: Always record the raw compiler error. The "Reflection Loop" is only as good as the failure data it is fed.

### B. Environment Parity
- **Policy**: Never assume code that works on Alma will work on Ubuntu (where Lean lives).
- **Action**: Every experimental script must include a cross-node verification step.

### C. Hierarchical Cost Scaling
- **Policy**: Do not use "Pro" models for debugging syntax errors.
- **Action**: Use "Flash" models for at least the first 5 iterations of any new reasoning logic.

---

## 3. Sentinel-Synchronized Prototyping
- **Policy**: New experiments often have unpredictable resource profiles.
- **Action**: Never disable Sentinel during experiments. Instead, update the `security_policy.md` to accommodate the new script's behavior if it is intentionally heavy.

---

## 4. Documentation of "The Why"
- **Policy**: Record the *reasoning* behind an experiment, not just the result.
- **Action**: Update `RESEARCH_STATE.md` after every major experimental session to capture the "Model Vibes" and "Aha!" moments.

---
*Last Updated: 2026-05-11 - Formalizing the Prototyping Methodology*
