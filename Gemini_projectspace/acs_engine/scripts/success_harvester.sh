#!/bin/bash
LOG_FILE="/home/tack_fr/sentinel_core/reflection_history.jsonl"
SRC_DIR="/home/tack_fr/sentinel_core/lean_translations"
DEST_DIR="/home/tack_fr/sentinel_core/final_successes"

# 合格済みファイルを記録する一時ファイル
PROCESSED_FILE="/tmp/processed_passes.txt"
touch $PROCESSED_FILE

echo "🌾 Success Harvester started. Watching for PASS entries..."

while true; do
    if [ -f "$LOG_FILE" ]; then
        # PASSと記録されたファイル名を抽出
        PASS_FILES=$(grep "\"status\": \"PASS\"" "$LOG_FILE" | sed -n 's/.*"file": "\([^"]*\)".*/\1/p')
        
        for file in $PASS_FILES; do
            # まだ処理していないファイルならコピー
            if ! grep -q "^$file$" "$PROCESSED_FILE"; then
                if [ -f "$SRC_DIR/$file" ]; then
                    cp "$SRC_DIR/$file" "$DEST_DIR/"
                    echo "✅ Harvested: $file (Saved to final_successes/)"
                    echo "$file" >> $PROCESSED_FILE
                fi
            fi
        done
    fi
    sleep 5
done
