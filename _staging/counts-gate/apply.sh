#!/usr/bin/env bash
# 계수 게이트 도입에 따른 노트 정리 5건 (모드 A, 2026-09-22)
#   AUDIT-LEDGER·SWAN/README : stale "58 source files" → 75 + count 지시자
#   swan-source-coverage-audit : count 지시자 3곳
#   roms_tangent_linear_model  : ".F 54 + .h 18 = 72" 내역 명시 + 지시자
#   swan-source-terms-implementation : 계수 오인 문구 해소
set -euo pipefail
WIKI="/home/firesinger/coastal-wiki"; SRC="$WIKI/_staging/counts-gate"; OWNER="firesinger"
say(){ printf '\n=== %s ===\n' "$*"; }; die(){ printf '\nABORT: %s\n' "$*" >&2; exit 1; }
say "0. 사전 조건"
n=0
for f in "$SRC"/models__*; do
  rel="$(basename "$f" | sed 's|__|/|g')"; tgt="$WIKI/$rel"
  [ -f "$tgt" ] || die "대상 없음: $rel"
  cmp -s "$f" "$tgt" && die "변경 없음: $rel"
  n=$((n+1))
done
[ "$n" -eq 5 ] || die "개수 불일치: $n"
echo "OK 5쌍"
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
