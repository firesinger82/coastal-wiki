#!/usr/bin/env bash
# validate-link-integrity.sh — thin entry point (구현: .py).
# 정책: 내부 링크 무결성 (상대 .md 링크 + [[wikilink]] resolve). '(예정)' forward-ref 통과.
set -eu
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
exec python3 "$SCRIPT_DIR/validate-link-integrity.py" "$@"
