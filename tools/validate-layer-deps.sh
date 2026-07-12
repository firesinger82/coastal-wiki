#!/usr/bin/env bash
# validate-layer-deps.sh — thin entry point (구현: .py).
# 정책: 4-레이어 근거 의존성 단방향 검사 (CONVENTIONS §8.1). 신규 layer 파일 opt-in, 기존 verified 제외.
set -eu
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
exec python3 "$SCRIPT_DIR/validate-layer-deps.py" "$@"
