# Export Protocol: Research to Public Interface

This document defines the protocol for exporting settled research results to external or public domains.

## 1. The Boundary (Airlock)
- **Directory**: `meta_management/export_dock/`
- **Destination**: {{EXPORT_DESTINATION}}
- **Rule**: Any file in this directory is considered "Public-Ready" and may be indexed by external agents.
- **Security**: Never place raw code with credentials or un-scrutinized theoretical drafts here.

## 2. Export Requirements
- **Status Sync**: Any exported item must have its status set to `public_release` in `registry.json`.
- **Anonymization**: Remove local absolute paths and replace with relative project paths.
- **Abstract**: Each export should include a 1-paragraph summary for external consumption.

---
*Created: {{DATE}}*
