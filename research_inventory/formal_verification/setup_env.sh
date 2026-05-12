#!/bin/bash
# Formal Verification Environment Setup Script for Sentinel-Leanstral
# This script recreates the portable Java and TLA+ environment.

set -e
BASE_DIR=$(cd "$(dirname "$0")"; pwd)
RUNTIME_DIR="$BASE_DIR/runtime"

mkdir -p "$RUNTIME_DIR"
cd "$RUNTIME_DIR"

if [ ! -d "java_home" ]; then
    echo "🚀 Downloading OpenJDK 21 (Temurin)..."
    curl -L -o openjdk.tar.gz https://github.com/adoptium/temurin21-binaries/releases/download/jdk-21.0.3%2B9/OpenJDK21U-jdk_x64_linux_hotspot_21.0.3_9.tar.gz
    mkdir -p java_home
    tar -xzf openjdk.tar.gz -C java_home --strip-components=1
    rm openjdk.tar.gz
    echo "✅ Java setup complete."
else
    echo "ℹ️ java_home already exists, skipping download."
fi

if [ ! -f "tools/tla2tools.jar" ]; then
    echo "🚀 Downloading TLA+ tools (tla2tools.jar)..."
    mkdir -p tools
    curl -L -o tools/tla2tools.jar https://github.com/tlaplus/tlaplus/releases/download/v1.8.0/tla2tools.jar
    echo "✅ TLA+ tools setup complete."
else
    echo "ℹ️ tla2tools.jar already exists, skipping download."
fi

echo "---"
echo "Setup finished successfully."
echo "Usage: $RUNTIME_DIR/java_home/bin/java -cp $RUNTIME_DIR/tools/tla2tools.jar tlc2.TLC [Spec.tla]"
