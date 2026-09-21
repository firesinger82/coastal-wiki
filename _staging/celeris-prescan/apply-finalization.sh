#!/usr/bin/env bash
# Celeris finalization — snapshot 교체 + 위키 노트 반영을 하나의 게이트에서 수행.
#   pinned f6fd78b → ebca435 (upstream main). 신규 343 / 수정 28.
# 실행:  sudo bash ~/coastal-wiki/_staging/celeris-prescan/apply-finalization.sh
set -euo pipefail
WIKI="/home/firesinger/coastal-wiki"; MIG="$WIKI/_staging/celeris-prescan"
SRC="$WIKI/models/Celeris/raw/source_code/Celeris-WebGPU"
STG="/home/firesinger/.cache/coastal-snapshots/celeris-upstream"; BK="/opt/coastal-snapshots"
OLD="f6fd78bd12af3aeeef11774a850b6b3d52be65b3"; NEW="ebca435d02b258768e0352fbaf27404f2f135799"
OWNER="firesinger"
say(){ printf '\n=== %s ===\n' "$*"; }; die(){ printf '\nABORT: %s\n' "$*" >&2; exit 1; }

say "0. 사전 조건"
[ -d "$STG" ] || die "staging 없음"
[ "$(git -c safe.directory='*' -C "$STG" rev-parse HEAD)" = "$NEW" ] || die "staging HEAD 불일치"
[ "$(git -c safe.directory='*' -C "$SRC" rev-parse HEAD)" = "$OLD" ] || die "설치 트리 HEAD 불일치"
[ -z "$(git -c safe.directory='*' -C "$SRC" status --porcelain)" ] || die "설치 트리 로컬 변경 있음"
echo "OK"

say "1. before-hash 검증"
python3 - "$WIKI" "$MIG" "$SRC" <<'PY'
import csv,hashlib,sys; from pathlib import Path
wiki,mig,src=map(Path,sys.argv[1:4])
def sha(p):
    h=hashlib.sha256(); h.update(Path(p).read_bytes()); return h.hexdigest()
bad=[]
for r in csv.DictReader(open(mig/"manifest-notes.csv")):
    t=wiki/r["path"]
    if not t.exists() or sha(t)!=r["before_sha256"]: bad.append(("note",r["path"]))
for r in csv.DictReader(open(mig/"manifest-B-installed.csv")):
    t=src/r["path"]
    if not t.exists() or sha(t)!=r["sha256"]: bad.append(("source",r["path"]))
if bad: print("MISMATCH",len(bad)); [print("  ",*b) for b in bad[:20]]; sys.exit(1)
print("OK: 노트 9 + 소스 652 before-hash 일치")
PY

say "2. 롤백 자산"
mkdir -p "$BK"
SNAP="$BK/celeris-$OLD.tar.zst"; NOTES="$BK/celeris-notes-before-$NEW.tar.zst"
[ -f "$SNAP" ] && echo "기존 백업 재사용" || tar --zstd -cf "$SNAP" -C "$(dirname "$SRC")" "$(basename "$SRC")"
tar --zstd -cf "$NOTES" -C "$WIKI" $(cut -d, -f1 "$MIG/manifest-notes.csv" | tail -n +2)
sha256sum "$SNAP" "$NOTES" | tee "$BK/celeris-finalization-backup.sha256"

say "3. snapshot 교체"
rm -rf "$SRC.old-$OLD"; mv "$SRC" "$SRC.old-$OLD"; cp -a "$STG" "$SRC"
chown -R root:root "$SRC"; chmod -R a-w "$SRC"
echo "HEAD=$(git -c safe.directory='*' -C "$SRC" rev-parse HEAD)"

say "4. 노트 반영"
while IFS=, read -r path before after locked; do
  [ "$path" = "path" ] && continue
  t="$WIKI/$path"; chmod u+w "$t"; cp "$MIG/wiki-candidate/$path" "$t"
  chown root:root "$t"; chmod a-w "$t"
done < "$MIG/manifest-notes.csv"
echo "노트 9개 반영"

say "5. after-hash 검증"
python3 - "$WIKI" "$MIG" "$SRC" <<'PY'
import csv,hashlib,sys; from pathlib import Path
wiki,mig,src=map(Path,sys.argv[1:4])
def sha(p):
    h=hashlib.sha256(); h.update(Path(p).read_bytes()); return h.hexdigest()
bad=[]
for r in csv.DictReader(open(mig/"manifest-notes.csv")):
    t=wiki/r["path"]
    if not t.exists() or sha(t)!=r["after_sha256"]: bad.append(("note",r["path"]))
for r in csv.DictReader(open(mig/"manifest-A-staging.csv")):
    t=src/r["path"]
    if not t.exists() or sha(t)!=r["sha256"]: bad.append(("source",r["path"]))
if bad: print("MISMATCH",len(bad)); [print("  ",*b) for b in bad[:20]]; sys.exit(1)
print("OK: 노트 9 + 소스 995 after-hash 일치")
PY

say "6. 잠금 확인 (일반 사용자 권한 — DESIGN v2.0 failure mode 25)"
W1=$(sudo -u "$OWNER" find "$WIKI/models" -writable 2>/dev/null | wc -l)
echo "models/ 쓰기 가능: $W1 (0 이어야 정상)"
[ "$W1" -eq 0 ] || die "잠금 실패 ($W1)"

say "완료"
echo "snapshot : $OLD -> $NEW"
echo "notes    : 4개"
echo "롤백     : $SNAP / $NOTES / $SRC.old-$OLD"
