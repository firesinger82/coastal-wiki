#!/usr/bin/env bash
# 인용 좌표·계수 정정 5노트 (모드 A, 2026-09-22)
#   SWAN   계수 정정 4종 (58→75 등)
#   Delft3D jet3d 귀속 오류 · chknum 범위 초과 · 호출부 표기 명시
#   XBeach  vfproj 구성 줄번호 2건 (범위 초과 1 + 범위 내 오류 1)
#   CADMAS  penst.f 범위 초과
set -euo pipefail
WIKI="/home/firesinger/coastal-wiki"; OWNER="firesinger"
say(){ printf '\n=== %s ===\n' "$*"; }; die(){ printf '\nABORT: %s\n' "$*" >&2; exit 1; }

declare -A M=(
 ["$WIKI/_staging/swan-count-fix/note.md.new"]="$WIKI/models/SWAN/source-analysis/swan-source-coverage-audit.md"
 ["$WIKI/_staging/citation-fix/d3d-physics.md.new"]="$WIKI/models/Delft3D/source-analysis/delft3d_flow2d3d_special_physics.md"
 ["$WIKI/_staging/citation-fix/d3d-inichk.md.new"]="$WIKI/models/Delft3D/source-analysis/delft3d_flow2d3d_inichk_general.md"
 ["$WIKI/_staging/citation-fix/xbeach-audit.md.new"]="$WIKI/models/XBeach/source-analysis/xbeach-audit-resolved-claims.md"
 ["$WIKI/_staging/citation-fix/cadmas-contact.md.new"]="$WIKI/models/CADMAS-SURF/source-analysis/str3d-contact-and-fluid-coupling.md"
)

say "0. 사전 조건"
for n in "${!M[@]}"; do
  [ -s "$n" ] || die "수정안 없음: $n"
  [ -f "${M[$n]}" ] || die "대상 없음: ${M[$n]}"
  cmp -s "$n" "${M[$n]}" && die "변경 없음(이미 적용?): ${M[$n]}"
done
[ -z "$(sudo -u "$OWNER" git -C "$WIKI" status --porcelain models/)" ] || die "models/ 에 미커밋 변경 있음"
echo "OK 5쌍"

say "1. 적용"
for n in "${!M[@]}"; do
  t="${M[$n]}"
  chmod u+w "$t"; cp "$n" "$t"; chown root:root "$t"; chmod a-w "$t"
  cmp -s "$t" "$n" || die "불일치: $t"
  echo "  applied ${t#$WIKI/}"
done

say "2. 잠금 확인 (일반 사용자 권한)"
W1=$(sudo -u "$OWNER" find "$WIKI/models" -writable 2>/dev/null | wc -l)
echo "  models/ 쓰기 가능: $W1"; [ "$W1" -eq 0 ] || die "잠금 실패 ($W1)"

say "완료"
