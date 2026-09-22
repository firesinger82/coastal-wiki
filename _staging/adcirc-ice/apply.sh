#!/usr/bin/env bash
# ADCIRC ICE 커버리지 노트 편입 (모드 A, 2026-09-22)
#   신규: manual-notes/19-ice-coverage.md   (번호 공백 19 를 채운다)
#   갱신: README.md (manual-notes 21→22)
set -euo pipefail
WIKI="/home/firesinger/coastal-wiki"; MIG="$WIKI/_staging/adcirc-ice"; OWNER="firesinger"
NOTE="$WIKI/models/ADCIRC/manual-notes/19-ice-coverage.md"
say(){ printf '\n=== %s ===\n' "$*"; }; die(){ printf '\nABORT: %s\n' "$*" >&2; exit 1; }
say "0. 사전 조건"
[ -s "$MIG/19-ice-coverage.md" ] || die "노트 없음"
[ -s "$MIG/README.md.new" ] || die "README 수정안 없음"
[ ! -e "$NOTE" ] || die "이미 존재: $NOTE"
[ -z "$(sudo -u "$OWNER" git -C "$WIKI" status --porcelain models/)" ] || die "models/ 에 미커밋 변경"
echo OK
say "1. 신규 노트"
D="$(dirname "$NOTE")"; chmod u+w "$D"
cp "$MIG/19-ice-coverage.md" "$NOTE"; chown root:root "$NOTE"; chmod a-w "$NOTE"; chmod a-w "$D"
echo "  created ${NOTE#$WIKI/}"
say "2. README"
t="$WIKI/models/ADCIRC/README.md"
chmod u+w "$t"; cp "$MIG/README.md.new" "$t"; chown root:root "$t"; chmod a-w "$t"
cmp -s "$t" "$MIG/README.md.new" || die "README 불일치"; echo "  applied models/ADCIRC/README.md"
say "3. 잠금 확인"
W1=$(sudo -u "$OWNER" find "$WIKI/models" -writable 2>/dev/null | wc -l)
echo "  models/ 쓰기 가능: $W1"; [ "$W1" -eq 0 ] || die "잠금 실패 ($W1)"
say "완료"
