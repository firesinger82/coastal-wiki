#!/usr/bin/env bash
# LISFLOOD-FP source_scope 선언 6노트 (모드 A, 2026-09-22)
# 새 문법 `dir/*`(직속만) 사용 — 루트와 하위가 같은 파일명을 쓰는 저장소용.
# 드라이런: LISFLOOD-FP AMBIGUOUS 43→8, 위키 전체 104→69
set -euo pipefail
WIKI="/home/firesinger/coastal-wiki"; SRC="$WIKI/_staging/lisflood-scope"; OWNER="firesinger"
say(){ printf '\n=== %s ===\n' "$*"; }; die(){ printf '\nABORT: %s\n' "$*" >&2; exit 1; }
say "0. 사전 조건"
n=0
for f in "$SRC"/models__*; do
  rel="$(basename "$f" | sed 's|__|/|g')"; tgt="$WIKI/$rel"
  [ -f "$tgt" ] || die "대상 없음: $rel"
  cmp -s "$f" "$tgt" && die "변경 없음: $rel"
  n=$((n+1))
done
[ "$n" -eq 6 ] || die "개수 불일치: $n (기대 6)"
echo "OK 6쌍"
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
