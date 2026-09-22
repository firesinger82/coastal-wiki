#!/usr/bin/env bash
# validate-counts.sh — thin entry point (구현: .py).
# 정책: 계수 단언(파일 수·배열 크기)을 glob 실측으로 재현 대조. 하위 집합 계수를
#       총계로 라벨링하는 반복 결함(SWAN 58 / ROMS 54 / LISFLOOD H) 차단.
set -eu
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
exec python3 "$SCRIPT_DIR/validate-counts.py" "$@"
