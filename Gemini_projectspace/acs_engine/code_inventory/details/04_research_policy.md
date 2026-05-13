# Section 4: Research, Concept & Policy Documents

## Design Philosophy
This section serves as the **"Institutional Memory"** of the project. In an environment where the AI agent changes frequently, these documents provide the stable "North Star" goals and the reasoning behind historical architectural decisions.

## Key Document Features & Content Details

### `AUTONOMOUS_CALC_SERVER_CONCEPT.md`
- **Core Tiers**:
    - **Tier 1 (Proxy)**: Simple script-based execution.
    - **Tier 2 (Sentinel)**: Basic resource monitoring and safety.
    - **Tier 3 (Self-Evolving)**: The agent can modify its own translation engine based on log analysis (The current goal).
- **Security Tiers**: Defines "Air-gapping" vs "SSH-Control" architectures.

### `RESEARCH_STATE.md`
- **Structure**: Divided into "Experimental Log" (What we tried), "Knowledge Base" (What we learned, e.g., 'Lean 4 autoImplicit trap'), and "Backlog" (Next experiments).
- **Key Discovery Recorded**: The realization that Leanstral performs better on geometry proofs than basic Gemini, but fails more on imports.

### `security_policy.md`
- **Ruleset**:
    - **Restriction 1**: No deletion of files outside `sentinel_core`.
    - **Restriction 2**: No outbound HTTP calls to unknown domains.
    - **Intervention**: Defines the "Stop everything" criteria for the Sentinel agent.

## Strategic Importance
- **Onboarding**: Allows new sessions to immediately understand the project's current maturity and constraints.
- **Auditability**: Provides a trail of the "philosophical" evolution of the project.

## Current Challenges & Future Outlook

### Challenges
- **Failure Taxonomy**: We lack a standardized way to categorize the *types* of failures (e.g., "Library Guessing" vs. "Logical Error") in our research documents.
- **Knowledge Silos**: Critical findings from logs (like the `autoImplicit` issue) are not yet codified into the "Model Instructions" or "Policy."

### Outlook
- **Error Pattern Library**: Creating a dedicated document that lists "Common Hallucinations" and their "Correct Alternatives" for future model fine-tuning.
- **Automated Policy Injection**: Automatically appending recent "Failure Lessons" to the model prompt to prevent repeated mistakes in a single session.
