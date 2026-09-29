#!/usr/bin/env bash
# validate-experience-numbers.sh — experience 수치 인용 구조 검사.
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
exec python3 "$SCRIPT_DIR/validate-experience-numbers.py" "$@"
