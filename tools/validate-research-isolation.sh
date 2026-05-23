#!/usr/bin/env bash
# validate-research-isolation.sh
#
# Python 구현(validate-research-isolation.py)의 thin entry point.
# 정책·검사 로직은 .py 파일 참조.
#
# 사용:
#   bash tools/validate-research-isolation.sh           # working tree
#   bash tools/validate-research-isolation.sh --staged  # staged snapshot
set -eu
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
exec python3 "$SCRIPT_DIR/validate-research-isolation.py" "$@"
