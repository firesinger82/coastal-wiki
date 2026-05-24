#!/usr/bin/env bash
# validate-phase2a-manifest.sh
#
# Python 본체(validate-phase2a-manifest.py)의 thin entry point.
# 정책·검사 로직은 .py 파일 참조 (plan.md Sub-phase 2a, v8).
#
# 사용 예:
#   bash tools/validate-phase2a-manifest.sh \
#       --manifest _staging/manifests/phase2a-manifest.csv
#   bash tools/validate-phase2a-manifest.sh \
#       --manifest _staging/manifests/phase2a-manifest.csv \
#       --inventory-source _staging/from-modeling-wiki/knowledge
#   bash tools/validate-phase2a-manifest.sh \
#       --manifest _staging/manifests/phase2a-manifest.csv \
#       --mode post-archive
set -eu
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
exec python3 "$SCRIPT_DIR/validate-phase2a-manifest.py" "$@"
