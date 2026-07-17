#!/usr/bin/env bash
# validate-claims.sh — thin entry point (구현: .py).
# 정책: theory 노트 단언 집계 산술·claim manifest 대조 (plan.md R1 I-1, Codex 20회차 반영).
set -eu
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
exec python3 "$SCRIPT_DIR/validate-claims.py" "$@"
