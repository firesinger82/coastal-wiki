#!/usr/bin/env bash
# ShorelineS snapshot 교체 + 노트 반영 (모드 A, 2026-09-21)
#
# 변경 내용: upstream 커밋 1건 = doc/ShorelineS_manual_v1.0.pdf 신규 추가뿐.
#            .m 소스 484건 전부 바이트 동일 → file:line 인용 좌표 변경 0건.
# 노트 반영: 스냅샷 sha 기록 갱신 + 매뉴얼 존재 반영(본문 발췌는 backlog).
#            DESIGN §GATE — 스냅샷 교체와 노트 반영은 같은 게이트에서 수행한다(asgs 교훈).
set -euo pipefail
WIKI="/home/firesinger/coastal-wiki"; MIG="$WIKI/_staging/shorelines-prescan"
SRC="$WIKI/models/ShorelineS/raw/source_code/shorelines"
STG="/home/firesinger/.cache/coastal-snapshots/shorelines-upstream"
OLD="7bf4481ab84c635033ef475fa648a1b09cf9f36b"
NEW="f3ec8638ddb53eb93fc2a77fa472bcb11b2cf940"
OWNER="firesinger"
say(){ printf '\n=== %s ===\n' "$*"; }; die(){ printf '\nABORT: %s\n' "$*" >&2; exit 1; }

say "0. 사전 조건"
[ "$(git -c safe.directory='*' -C "$STG" rev-parse HEAD)" = "$NEW" ] || die "staging HEAD 불일치"
[ "$(git -c safe.directory='*' -C "$SRC" rev-parse HEAD)" = "$OLD" ] || die "설치 HEAD 불일치"
[ -z "$(git -c safe.directory='*' -C "$SRC" status --porcelain)" ] || die "설치 트리에 로컬 변경 있음"
for f in README.md.new shorelines-official-resources.md.new AUDIT-LEDGER.md.new; do
  [ -s "$MIG/$f" ] || die "노트 수정안 없음: $f"
done
echo OK

say "1. before-hash (설치 소스 484)"
python3 - "$MIG/manifest-B-installed.csv" "$SRC" <<'PY'
import csv,hashlib,sys
from pathlib import Path
man,src=Path(sys.argv[1]),Path(sys.argv[2])
def sha(p):
    h=hashlib.sha256()
    with open(p,"rb") as f:
        for b in iter(lambda:f.read(1<<20),b""): h.update(b)
    return h.hexdigest()
bad=[r["path"] for r in csv.DictReader(open(man))
     if not (src/r["path"]).is_file() or sha(src/r["path"])!=r["sha256"]]
print("MISMATCH",len(bad),bad[:5]) if bad else print("OK 484")
sys.exit(1 if bad else 0)
PY

say "2. 스냅샷 교체"
rm -rf "$SRC.old-$OLD"; mv "$SRC" "$SRC.old-$OLD"; cp -a "$STG" "$SRC"
chown -R root:root "$SRC"; chmod -R a-w "$SRC"
echo "HEAD=$(git -c safe.directory='*' -C "$SRC" rev-parse HEAD)"

say "3. after-hash (신 스냅샷 485)"
python3 - "$MIG/manifest-A-staging.csv" "$SRC" <<'PY'
import csv,hashlib,sys
from pathlib import Path
man,src=Path(sys.argv[1]),Path(sys.argv[2])
def sha(p):
    h=hashlib.sha256()
    with open(p,"rb") as f:
        for b in iter(lambda:f.read(1<<20),b""): h.update(b)
    return h.hexdigest()
bad=[r["path"] for r in csv.DictReader(open(man))
     if not (src/r["path"]).is_file() or sha(src/r["path"])!=r["sha256"]]
print("MISMATCH",len(bad),bad[:5]) if bad else print("OK 485")
sys.exit(1 if bad else 0)
PY

say "4. 노트 반영 (파일별 최소 unlock → 복사 → 즉시 relock)"
apply_note(){  # $1 = 수정안, $2 = 대상 경로
  local new="$MIG/$1" tgt="$2"
  [ -f "$tgt" ] || die "대상 없음: $tgt"
  chmod u+w "$tgt"; cp "$new" "$tgt"
  chown root:root "$tgt"; chmod a-w "$tgt"
  echo "  applied ${tgt#$WIKI/}"
}
apply_note README.md.new                        "$WIKI/models/ShorelineS/README.md"
apply_note shorelines-official-resources.md.new "$WIKI/models/ShorelineS/web-refs/shorelines-official-resources.md"
apply_note AUDIT-LEDGER.md.new                  "$WIKI/models/AUDIT-LEDGER.md"

say "5. 노트 대조"
for p in "models/ShorelineS/README.md:README.md.new" \
         "models/ShorelineS/web-refs/shorelines-official-resources.md:shorelines-official-resources.md.new" \
         "models/AUDIT-LEDGER.md:AUDIT-LEDGER.md.new"; do
  t="${p%%:*}"; n="${p##*:}"
  cmp -s "$WIKI/$t" "$MIG/$n" || die "노트 불일치: $t"
  echo "  OK $t"
done

say "6. 잠금 확인 (일반 사용자 권한 — find -writable 은 root 로 항상 참)"
W1=$(sudo -u "$OWNER" find "$WIKI/models" -writable 2>/dev/null | wc -l)
echo "  models/ 쓰기 가능: $W1"
[ "$W1" -eq 0 ] || die "잠금 실패 ($W1)"

say "7. 구 스냅샷 제거 (복원 경로 = pinned 커밋 객체)"
git -c safe.directory='*' -C "$SRC" cat-file -t "$OLD" >/dev/null 2>&1 \
  || die "신 스냅샷에 pinned 객체 $OLD 없음 — .old 유지"
chmod -R u+w "$SRC.old-$OLD"; rm -rf "$SRC.old-$OLD"; echo "  removed .old-$OLD"

say "완료"
