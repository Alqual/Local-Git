#!/bin/bash

# Backup Manager: Hierarchical State Preservation
# Usage: bash meta_management/backup_manager.sh [core|full]

TYPE=$1
WORKSPACE_DIR="/home/tack-mit/デスクトップ/Gemini_projectspace"
BACKUP_BASE_DIR="/home/tack-mit/デスクトップ/backups_lossless_ai"
TIMESTAMP=$(date +%Y%m%d_%H%M)
FILENAME="lossless_ai_backup_${TYPE}_${TIMESTAMP}.tar.gz"

mkdir -p "$BACKUP_BASE_DIR"

if [ "$TYPE" == "core" ]; then
    echo "Starting CORE snapshot..."
    tar -czvf "$BACKUP_BASE_DIR/$FILENAME" \
        -C "$WORKSPACE_DIR" \
        --exclude="*.venv*" \
        --exclude="local_libs" \
        --exclude="基礎データ" \
        --exclude="__pycache__" \
        --exclude=".git" \
        --exclude="*.tar.gz" \
        .
elif [ "$TYPE" == "full" ]; then
    echo "Starting FULL archive (this may take time)..."
    tar -czvf "$BACKUP_BASE_DIR/$FILENAME" \
        -C "$WORKSPACE_DIR" \
        .
else
    echo "Error: Unknown backup type '$TYPE'. Use 'core' or 'full'."
    exit 1
fi

echo "Backup completed: $BACKUP_BASE_DIR/$FILENAME"
ls -lh "$BACKUP_BASE_DIR/$FILENAME"
