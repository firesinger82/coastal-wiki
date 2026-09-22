#!/usr/bin/env bash
# ADCIRC bare 참조 명시화 18건 / 8노트 (모드 A, 2026-09-22)
#   `:NNNN` → `file.F:NNNN` — 좌표 유효 또는 유일앵커 재앵커분만.
#   의미 대조가 기계적으로 확인되지 않은 7건은 held-for-review.csv 로 보류.
set -euo pipefail
WIKI="/home/firesinger/coastal-wiki"; SRC="$WIKI/_staging/adcirc-bare/applied"; OWNER="firesinger"
say(){ printf '\n=== %s ===\n' "$*"; }; die(){ printf '\nABORT: %s\n' "$*" >&2; exit 1; }
say "0. 사전 조건"
n=0
for f in "$SRC"/models__*; do
  rel="$(basename "$f" | sed 's|__|/|g')"; tgt="$WIKI/$rel"
  [ -f "$tgt" ] || die "대상 없음: $rel"
  cmp -s "$f" "$tgt" && die "변경 없음: $rel"
  n=$((n+1))
done
[ "$n" -eq 8 ] || die "개수 불일치: $n (기대 8)"
echo "OK 8쌍"
say "1. 적용"
for f in "$SRC"/models__*; do
  rel="$(basename "$f" | sed 's|__|/|g')"; tgt="$WIKI/$rel"
  chmod u+w "$tgt"; cp "$f" "$tgt"; chown root:root "$tgt"; chmod a-w "$tgt"
  cmp -s "$tgt" "$f" || die "불일치: $rel"; echo "  applied $rel"
done
say "2. 잠금 확인"
W1=$(sudo -u "$OWNER" find "$WIKI/models" -writable 2>/dev/null | wc -l)
echo "  models/ 쓰기 가능: $W1"; [ "$W1" -eq 0 ] || die "잠금 실패 ($W1)"
say "완료"
