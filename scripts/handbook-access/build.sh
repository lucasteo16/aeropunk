#!/usr/bin/env bash
set -euo pipefail
cd -- "$(dirname -- "${BASH_SOURCE[0]}")"
export JAVA_HOME="$PWD/toolchain/jdk-21.0.12.1+1"
export PATH="$JAVA_HOME/bin:$PATH"
export GRADLE_USER_HOME="$PWD/.gradle-user-home"
export TMPDIR="$PWD/build-tmp"
mkdir -p "$TMPDIR"
./gradlew clean test build --console=plain
python verify_artifact.py
