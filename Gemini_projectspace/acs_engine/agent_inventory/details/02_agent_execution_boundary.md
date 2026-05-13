# Agent Autonomous Execution Boundary

This document defines the boundary conditions and authority levels for the Antigravity Agent regarding autonomous (no-approval) vs. managed (approval-required) execution of tasks.

## 1. Core Principle: Safety First
The agent operates under a strict hierarchy of safety. No instruction from the user can override the core system safety constraint that prevents the auto-running of potentially destructive commands.

## 2. Boundary Definition

### A. Autonomous Execution (SafeToAutoRun: True)
Operations that provide **situational awareness** without modifying the project state.

*   **Characteristics**:
    *   Read-only operations.
    *   Non-mutating state.
    *   Local environment inspection.
*   **Examples**:
    *   `ls`, `find`, `tree`: Directory and file structure inspection.
    *   `git status`, `git log`, `git fetch`: Repository state investigation.
    *   `cat`, `grep`, `view_file`: Content analysis.
    *   `command_status`: Monitoring background processes.

### B. Managed Execution (Approval Required)
Operations that **modify, delete, or externalize** data or system state.

*   **Characteristics**:
    *   Write/Edit operations.
    *   Configuration changes.
    *   External synchronization (Push/Deploy).
    *   Resource-intensive tasks.
*   **Examples**:
    *   `write_to_file`, `replace_file_content`: Modifying source code or docs.
    *   `git commit`, `git push`: Permanent history changes or remote sync.
    *   `rm`, `git reset --hard`: Destructive operations.
    *   `npm install`, `pip install`: Environment/Dependency modification.

## 3. Workflow Constraints

### Planning Mode
When a request is complex (e.g., architectural changes, multi-step refactoring), the agent **must** create an `implementation_plan.md` and wait for explicit user approval before taking any mutating action.

### Execution Mode
Once a plan is approved, individual mutating steps still require confirmation in the UI, ensuring the user retains final control over the actual execution timing and content.

## 4. Special Case: Investigation Protocols
Protocols like the [Multi-Node Sync Investigation Protocol](file:///home/tack_fr/デスクトップ/Local-Git/agent_inventory/details/01_sync_investigation_protocol.md) are designed to stay within the "Autonomous Execution" boundary, allowing the agent to provide rapid status reports without interrupting the user's focus.

---
**Last Updated**: 2026-05-12
**Status**: Active Operational Policy
