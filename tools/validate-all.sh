#!/usr/bin/env bash
# validate-all.sh — 위키 무결성 validator 단일 진입점 (F-8, 2026-07-12).
# pre-commit 훅과 수동 실행이 이 목록 하나만 참조 — 도구 목록 드리프트 방지 SSOT.
# 사용: bash tools/validate-all.sh [--staged]
# ※ L4 자가 감사(의미 검증, cron)는 별개 축 — 여기 결정적(구조) 검증과 통합 금지.
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

VALIDATORS=(
    validate-research-isolation.sh
    validate-canonical-hygiene.sh
    validate-link-integrity.sh
    validate-layer-deps.sh
)

for v in "${VALIDATORS[@]}"; do
    S="$SCRIPT_DIR/$v"
    if [ ! -x "$S" ]; then
        echo "validate-all: $S 실행 불가 (chmod +x 또는 누락 확인)"
        exit 1
    fi
    bash "$S" "$@"
done
