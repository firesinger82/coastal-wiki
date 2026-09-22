#!/usr/bin/env bash
# concepts/rip-currents 모델 표현 노트 신설 (2026-09-22) — concepts/ 는 잠금 대상 아님
set -euo pipefail
WIKI="/home/firesinger/coastal-wiki"; MIG="$WIKI/_staging/rip-model"
N="$WIKI/concepts/rip-currents/06-model-application.md"
[ ! -e "$N" ] || { echo "이미 존재"; exit 1; }
cp "$MIG/06-model-application.md" "$N"; echo "created concepts/rip-currents/06-model-application.md"
cp "$MIG/README.md.new" "$WIKI/concepts/rip-currents/README.md"; echo "applied README"
