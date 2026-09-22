#!/usr/bin/env bash
# 전칭 단언 교정 — models/ 41노트 58건 (모드 A, 2026-09-22)
# concepts/ 2건·textbook/ 1건은 잠금 대상이 아니라 별도 적용 완료.
set -euo pipefail
WIKI="/home/firesinger/coastal-wiki"; SRC="$WIKI/_staging/overclaim-sweep/applied"; OWNER="firesinger"
say(){ printf '\n=== %s ===\n' "$*"; }; die(){ printf '\nABORT: %s\n' "$*" >&2; exit 1; }

say "0. 사전 조건"
n=0
for f in "$SRC"/models__*; do
  rel="$(basename "$f" | sed 's|__|/|g')"; tgt="$WIKI/$rel"
  [ -f "$tgt" ] || die "대상 없음: $rel"
  cmp -s "$f" "$tgt" && die "변경 없음(이미 적용?): $rel"
  n=$((n+1))
done
[ "$n" -eq 41 ] || die "수정본 개수 불일치: $n (기대 41)"
echo "OK 41쌍"

say "1. 적용"
for f in "$SRC"/models__*; do
  rel="$(basename "$f" | sed 's|__|/|g')"; tgt="$WIKI/$rel"
  chmod u+w "$tgt"; cp "$f" "$tgt"; chown root:root "$tgt"; chmod a-w "$tgt"
  cmp -s "$tgt" "$f" || die "불일치: $rel"
  echo "  applied $rel"
done

say "2. 잠금 확인 (일반 사용자 권한)"
W1=$(sudo -u "$OWNER" find "$WIKI/models" -writable 2>/dev/null | wc -l)
echo "  models/ 쓰기 가능: $W1"; [ "$W1" -eq 0 ] || die "잠금 실패 ($W1)"
say "완료"
