# Concept: Autonomous Calculation Server (ACS)

This document archives the strategic vision for transforming this PC into a self-governing reasoning and computation node.

## 1. Objective
To establish a server capable of autonomous, 24/7 execution of complex logical and mathematical tasks, reducing human overhead in research and data processing.

## 2. Core Architecture

### Brains (Multi-Model Strategy)
- **Logical Reasoning**: Llama 3 (8B+) for high-fidelity deductive tasks.
- **Mathematical Computation**: Mathstral (7B) for symbolic and numerical conjectures.
- **Efficiency Layer**: Mistral (7B v0.3) for high-speed batch processing and routine categorization.

### Limbs (Model Context Protocol - MCP)
The model should not just "chat" but "operate" through a standardized MCP interface:
- **Python MCP**: For executing code, SymPy simulations, and numerical verification.
- **File System MCP**: For autonomous reading/writing of research ledgers and logs.
- **Sequential Reasoning MCP**: For managing long-chain thoughts and self-correction loops.

## 3. Operational Workflow
1. **Hypothesis Generation**: The LLM proposes a logical step or a calculation method.
2. **Execution**: The model uses an MCP tool to run a Python script or search a database.
3. **Verification**: The system compares the output against known constraints.
4. **Refinement**: If an error is detected, the model re-evaluates its approach autonomously.

## 4. Hardware & Software Foundation (Updated 2026-05-05)
- **OS**: Ubuntu 22.04 LTS
- **GPU**: NVIDIA RTX 3060 (6GB VRAM)
- **Env**: Isolated Miniconda environment (`acs_engine/llm_env/`) within the dedicated library.
- **Library Root**: `acs_engine/` (Contains core, training, and data modules).
- **Serving**: Ollama as the local inference engine.

## 5. Future Roadmap
- Implementation of a high-density MCP toolset specifically for "Lossless AI" research.
- Development of a batch queue system for background theory verification.
- Integration of a "Dynamic Tensor Memory" ledger for long-term reasoning stability.
