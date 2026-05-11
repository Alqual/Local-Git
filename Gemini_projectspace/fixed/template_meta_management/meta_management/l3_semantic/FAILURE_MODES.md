# Boundary Analysis: Failure Modes & Limits

This document tracks the "Breaking Points" of the {{PROJECT_NAME}} system. Knowledge of these limits allows the Agent to avoid system degradation.

---

## 🛑 Failure Mode Template

### [Failure Mode Name]
*   **Mechanism**: [How does it break?]
*   **Consequence**: [What happens?]
*   **Detection Metric**: [How to measure it?]
*   **Defensive Action**: [What should the agent do?]
*   **Status**: [Current observation]

---

## 🛑 Failure Mode 1: [Example: Data Saturation]
*   **Mechanism**: Too much data for the current model capacity.
*   **Consequence**: Accuracy drops; processing time exceeds limit.
*   **Detection Metric**: Latency > {{LATENCY_LIMIT}}ms or EER > {{EER_LIMIT}}.
*   **Defensive Action**: [HALT INJECTION]
*   **Status**: [Baseline Stable]

---
*Created: {{DATE}}*
