#!/usr/bin/env bash
# 변종 트리 source_scope 선언 27노트 (모드 A, 2026-09-22)
#   CADMAS-SURF 13 — Simulators/{CADMAS-SURF-3D, CADMAS-SURF-3D2F, AGENT}
#   FUNWAVE     14 — {FUNWAVE-TVD, FUNWAVE-GPU}
# 드라이런: 위키 전체 AMBIGUOUS 460 → 104 (356 해소)
set -euo pipefail
WIKI="/home/firesinger/coastal-wiki"; SRC="$WIKI/_staging/scope-declarations"; OWNER="firesinger"
say(){ printf '\n=== %s ===\n' "$*"; }; die(){ printf '\nABORT: %s\n' "$*" >&2; exit 1; }
say "0. 사전 조건"
n=0
for f in "$SRC"/models__*; do
  rel="$(basename "$f" | sed 's|__|/|g')"; tgt="$WIKI/$rel"
  [ -f "$tgt" ] || die "대상 없음: $rel"
  cmp -s "$f" "$tgt" && die "변경 없음: $rel"
  n=$((n+1))
done
[ "$n" -eq 27 ] || die "개수 불일치: $n (기대 27)"
echo "OK 27쌍"
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
