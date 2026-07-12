#!/usr/bin/env bash
# count-notes.sh — thin entry point (구현: .py). 노트 개수 실측·원장 대조 (F-1).
# 사용: bash tools/count-notes.sh [--check|--json]
set -eu
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
exec python3 "$SCRIPT_DIR/count-notes.py" "$@"
