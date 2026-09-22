#!/usr/bin/env bash
# ADCIRC manifest 크기 재측정 반영 (모드 A, 2026-09-22)
set -euo pipefail
WIKI="/home/firesinger/coastal-wiki"; OWNER="firesinger"
f="$WIKI/_staging/adcirc-manifest/manifest.md.new"; t="$WIKI/models/ADCIRC/manifest.md"
[ -s "$f" ] || { echo "수정안 없음"; exit 1; }
cmp -s "$f" "$t" && { echo "변경 없음"; exit 1; }
chmod u+w "$t"; cp "$f" "$t"; chown root:root "$t"; chmod a-w "$t"
cmp -s "$t" "$f" || { echo "불일치"; exit 1; }
echo "applied models/ADCIRC/manifest.md"
W1=$(sudo -u "$OWNER" find "$WIKI/models" -writable 2>/dev/null | wc -l)
echo "models/ 쓰기 가능: $W1"; [ "$W1" -eq 0 ] || exit 1
echo "완료"
