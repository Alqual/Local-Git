# Export Protocol: Research to PR Interface

This document defines the minimalist protocol for exporting settled research results to the PR/Public domain.

## 1. The Boundary (Airlock)
- **Directory**: `meta_management/export_dock/`
- **Destination**: `/home/tack-mit/デスクトップ/outreach_workspace` (Identified as the Official PR Project)
- **PR Agent Entry Point**: The PR Agent in `outreach_workspace` should be configured to prioritize `linked/Gemini_projectspace/meta_management/export_dock/` as its primary knowledge source.
- **Rule**: Any file in this directory is considered "Public-Ready" and may be indexed by external PR Agents.
- **Security**: Never place raw code with credentials or un-scrutinized theoretical drafts here.

## 2. Export Requirements (Minimum)
- **Status Sync**: Any exported item must have its `publicity_status` set to `public_release` in `registry.json`.
- **Anonymization**: Remove local absolute paths (e.g., `/home/tack-mit/...`) and replace with relative project paths.
- **Abstract**: Each export should include a 1-paragraph "Impact Summary" for non-expert consumption.

---
*Last Updated: 2026-04-19*
