# Backup Policy: Hierarchical State Preservation

This policy governs the frequency, scope, and management of backups for the Lossless AI project. It ensures that the project's intellectual assets (L2/L3 memory, research logic) are preserved with high redundancy, while heavy environment assets are archived strategically.

---

## 1. Backup Tiers (バックアップ階層)

We categorize all project data into two tiers to optimize storage and transfer speed.

| Tier | Name | Target Scope | Exclusions | Trigger |
| :--- | :--- | :--- | :--- | :--- |
| **Tier 1** | **Core Snapshot** | `meta_management/`, `l2_episodic_dock/`, `RESEARCH_STATE.md`, all `.py` and `.md` files in research directories. | `.venv*`, `local_libs/`, ` 기초データ/`, `__pycache__`, large datasets. | Phase Settlement, Monthly, or before major refactoring. |
| **Tier 2** | **Full Archive** | Entire `Gemini_projectspace` directory. | None. | Phase Completion (e.g., closing Phase 18). |

---

## 2. Operational Procedures (運用手順)

### 2.1 Automated Script usage
Backups are managed via the [backup_manager.sh](file:///home/tack-mit/デスクトップ/Gemini_projectspace/meta_management/backup_manager.sh) script.

-   **Command**: `bash meta_management/backup_manager.sh [core|full]`
-   **Output**: Compressed `.tar.gz` file stored in `/home/tack-mit/デスクトップ/backups_lossless_ai/`.

### 2.2 Storage Specification
-   **Location**: `/home/tack-mit/デスクトップ/backups_lossless_ai/`
-   **Naming Convention**: `lossless_ai_backup_[type]_[YYYYMMDD]_[HHMM].tar.gz`

---

## 3. Retention & Rotation (保存とローテーション)

To prevent disk bloat, the following rotation policy is enforced:

*   **Core Snapshots**: Keep the last **10** versions.
*   **Full Archives**: Keep the last **2** versions.
*   **Airlock Sync**: After a Phase Settlement, the most recent Core Snapshot should be moved to the [export_dock/](file:///home/tack-mit/デスクトップ/Gemini_projectspace/meta_management/export_dock/) for potential external storage.

---

## 4. Verification & Recovery (検証と復旧)

*   **Integrity Check**: Every backup generation must be followed by a listing check (`tar -tvf`) to ensure no corruption.
*   **Recovery Test**: Once per Phase, a recovery test must be performed into a temporary folder to verify that the project can be "Re-hydrated" from the backup alone.

---
*Last Updated: 2026-04-22*
*Status: ACTIVE*
