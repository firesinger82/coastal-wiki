#!/usr/bin/env bash
# validate-canonical-hygiene.sh
#
# Python 구현(validate-canonical-hygiene.py)의 thin entry point.
# 정책: plan.md G8 (G8b 경로·G8d placeholder), CONVENTIONS §4·§6.
#
# 사용:
#   bash tools/validate-canonical-hygiene.sh           # working tree
#   bash tools/validate-canonical-hygiene.sh --staged  # staged snapshot
set -eu
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
exec python3 "$SCRIPT_DIR/validate-canonical-hygiene.py" "$@"
