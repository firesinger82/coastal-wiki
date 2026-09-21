#!/usr/bin/env bash
# ShorelineS 공식 매뉴얼 v1.0 발췌 노트 편입 (모드 A, 2026-09-22)
#
# 신규: models/ShorelineS/manual-notes/shorelines-technical-manual-v1.md
# 갱신: ShorelineS/README.md(MN 2→3) · web-refs(발췌 완료 표시) · AUDIT-LEDGER(문서축 재종결)
set -euo pipefail
WIKI="/home/firesinger/coastal-wiki"; MIG="$WIKI/_staging/shorelines-manual"
NOTE="$WIKI/models/ShorelineS/manual-notes/shorelines-technical-manual-v1.md"
OWNER="firesinger"
say(){ printf '\n=== %s ===\n' "$*"; }; die(){ printf '\nABORT: %s\n' "$*" >&2; exit 1; }

say "0. 사전 조건"
for f in shorelines-technical-manual-v1.md README.md.new web-refs.md.new AUDIT-LEDGER.md.new; do
  [ -s "$MIG/$f" ] || die "산출물 없음: $f"
done
[ ! -e "$NOTE" ] || die "이미 존재: $NOTE"
[ -z "$(sudo -u "$OWNER" git -C "$WIKI" status --porcelain models/)" ] || die "models/ 에 미커밋 변경 있음"
echo OK

say "1. 신규 노트 배치"
D="$(dirname "$NOTE")"; chmod u+w "$D"
cp "$MIG/shorelines-technical-manual-v1.md" "$NOTE"
chown root:root "$NOTE"; chmod a-w "$NOTE"; chmod a-w "$D"
echo "  created ${NOTE#$WIKI/}"

say "2. 색인 갱신"
apply_note(){ local new="$MIG/$1" tgt="$2"
  [ -f "$tgt" ] || die "대상 없음: $tgt"
  chmod u+w "$tgt"; cp "$new" "$tgt"; chown root:root "$tgt"; chmod a-w "$tgt"
  cmp -s "$tgt" "$new" || die "불일치: $tgt"; echo "  applied ${tgt#$WIKI/}"; }
apply_note README.md.new      "$WIKI/models/ShorelineS/README.md"
apply_note web-refs.md.new    "$WIKI/models/ShorelineS/web-refs/shorelines-official-resources.md"
apply_note AUDIT-LEDGER.md.new "$WIKI/models/AUDIT-LEDGER.md"

say "3. 대조"
cmp -s "$NOTE" "$MIG/shorelines-technical-manual-v1.md" || die "신규 노트 불일치"
echo "  OK 4파일"

say "4. 잠금 확인 (일반 사용자 권한)"
W1=$(sudo -u "$OWNER" find "$WIKI/models" -writable 2>/dev/null | wc -l)
echo "  models/ 쓰기 가능: $W1"; [ "$W1" -eq 0 ] || die "잠금 실패 ($W1)"

say "완료"
