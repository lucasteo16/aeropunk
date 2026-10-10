#!/usr/bin/env bash
set -euo pipefail
cd -- "$(dirname -- "${BASH_SOURCE[0]}")"
export JAVA_HOME="$PWD/toolchain/jdk-21.0.12.1+1"
export PATH="$JAVA_HOME/bin:$PATH"
export GRADLE_USER_HOME="$PWD/.gradle-user-home"
export TMPDIR="$PWD/build-tmp"
mkdir -p "$TMPDIR"
python prepare_query_dependency.py
./gradlew clean test build accessProbeClasspath -I access-probe.gradle --console=plain
python test_query_integration.py
python test_open_endpoint.py
python test_access_wiring.py
python test_access_wiring.py --negative-control
python verify_artifact.py
