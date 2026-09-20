#!/usr/bin/env bash
# EFDC finalization — snapshot 교체 + 위키 노트 반영을 하나의 게이트에서 수행한다.
#   pinned 3ed76b6 (v12.4 release) → 3b382fd (upstream main, v12.5)
#
# 실행:  sudo bash ~/coastal-wiki/_staging/efdc-migration/apply-finalization.sh
#
# 안전장치: before-hash 불일치 시 즉시 중단, 백업 먼저, 단계별 검증.
set -euo pipefail

WIKI="/home/firesinger/coastal-wiki"
MIG="$WIKI/_staging/efdc-migration"
SRC="$WIKI/models/EFDC/raw/source_code/EFDCPlus_Stable"
STG="/home/firesinger/.cache/coastal-snapshots/efdc-3b382fd"
BK="/opt/coastal-snapshots"
OLD_SHA="3ed76b6eb1263921ba99bf23b66bb85c1a5feac1"
NEW_SHA="3b382fd0b5222a8ed0bac6d2cfc9a7877062db27"

say() { printf '\n=== %s ===\n' "$*"; }
die() { printf '\nABORT: %s\n' "$*" >&2; exit 1; }

# ---------- 0. 사전 조건 ----------
say "0. 사전 조건"
[ -d "$STG" ] || die "staging 클론 없음: $STG"
[ "$(git -c safe.directory='*' -C "$STG" rev-parse HEAD)" = "$NEW_SHA" ] || die "staging HEAD 불일치"
[ "$(git -c safe.directory='*' -C "$SRC" rev-parse HEAD)" = "$OLD_SHA" ] || die "설치 트리 HEAD 불일치"
[ -z "$(git -c safe.directory='*' -C "$SRC" status --porcelain)" ] || die "설치 트리에 로컬 변경 있음"
echo "OK: staging=$NEW_SHA, installed=$OLD_SHA, worktree clean"

# ---------- 1. before-hash 검증 ----------
say "1. 대상 파일 before-hash 검증"
python3 - "$WIKI" "$MIG" "$SRC" <<'PY'
import csv, hashlib, sys
from pathlib import Path
wiki, mig, src = map(Path, sys.argv[1:4])
def sha(p):
    h = hashlib.sha256(); h.update(Path(p).read_bytes()); return h.hexdigest()
bad = []
for r in csv.DictReader(open(mig/"manifest-notes.csv")):
    t = wiki/r["path"]
    if not t.exists() or sha(t) != r["before_sha256"]:
        bad.append(("note", r["path"]))
for r in csv.DictReader(open(mig/"manifest-B-installed.csv")):
    t = src/r["path"]
    if not t.exists() or sha(t) != r["sha256"]:
        bad.append(("source", r["path"]))
if bad:
    print("BEFORE-HASH MISMATCH:", len(bad)); [print("  ", *b) for b in bad[:20]]; sys.exit(1)
print(f"OK: 노트 31개 + 소스 381개 before-hash 일치")
PY

# ---------- 2. 백업 ----------
say "2. 롤백 자산 생성"
mkdir -p "$BK"
SNAP_TAR="$BK/efdc-EFDCPlus_Stable-$OLD_SHA.tar.zst"
NOTE_TAR="$BK/efdc-notes-before-$NEW_SHA.tar.zst"
if [ -f "$SNAP_TAR" ]; then
  echo "기존 백업 재사용: $SNAP_TAR"
else
  tar --zstd -cf "$SNAP_TAR" -C "$(dirname "$SRC")" "$(basename "$SRC")"
  echo "snapshot 백업: $SNAP_TAR ($(du -h "$SNAP_TAR" | cut -f1))"
fi
tar --zstd -cf "$NOTE_TAR" -C "$WIKI" $(cut -d, -f1 "$MIG/manifest-notes.csv" | tail -n +2)
echo "notes 백업:    $NOTE_TAR ($(du -h "$NOTE_TAR" | cut -f1))"
sha256sum "$SNAP_TAR" "$NOTE_TAR" | tee "$BK/efdc-finalization-backup.sha256"

# ---------- 3. snapshot 교체 ----------
say "3. snapshot 교체"
rm -rf "$SRC.old-$OLD_SHA"
mv "$SRC" "$SRC.old-$OLD_SHA"
cp -a "$STG" "$SRC"
chown -R root:root "$SRC"
chmod -R a-w "$SRC"
echo "교체 완료. HEAD=$(git -c safe.directory='*' -C "$SRC" rev-parse HEAD)"

# ---------- 4. 위키 노트 반영 ----------
say "4. 위키 노트 반영 (31개)"
while IFS=, read -r path before after locked; do
  [ "$path" = "path" ] && continue
  tgt="$WIKI/$path"
  if [ "$locked" = "yes" ]; then chmod u+w "$tgt"; fi
  cp "$MIG/wiki-candidate/$path" "$tgt"
  if [ "$locked" = "yes" ]; then chown root:root "$tgt"; chmod a-w "$tgt"; fi
done < "$MIG/manifest-notes.csv"
echo "노트 31개 반영 완료"

# ---------- 5. after-hash 검증 ----------
say "5. after-hash 검증"
python3 - "$WIKI" "$MIG" "$SRC" <<'PY'
import csv, hashlib, sys
from pathlib import Path
wiki, mig, src = map(Path, sys.argv[1:4])
def sha(p):
    h = hashlib.sha256(); h.update(Path(p).read_bytes()); return h.hexdigest()
bad = []
for r in csv.DictReader(open(mig/"manifest-notes.csv")):
    t = wiki/r["path"]
    if not t.exists() or sha(t) != r["after_sha256"]: bad.append(("note", r["path"]))
for r in csv.DictReader(open(mig/"manifest-A-staging.csv")):
    t = src/r["path"]
    if not t.exists() or sha(t) != r["sha256"]: bad.append(("source", r["path"]))
if bad:
    print("AFTER-HASH MISMATCH:", len(bad)); [print("  ", *b) for b in bad[:20]]; sys.exit(1)
print("OK: 노트 31개 + 소스 383개 after-hash 일치")
PY

# ---------- 6. 잠금 확인 ----------
say "6. 잠금 확인"
W1=$(find "$WIKI/models" -writable 2>/dev/null | wc -l)
echo "models/ 쓰기 가능 파일: $W1  (0 이어야 정상)"
[ "$W1" -eq 0 ] || die "잠금 실패 — 쓰기 가능 파일 $W1 개"

say "완료"
cat <<EOF
snapshot : $OLD_SHA -> $NEW_SHA
notes    : 31개 반영 (models/ 25, concepts/ 6)
롤백     : $SNAP_TAR
           $NOTE_TAR
           $SRC.old-$OLD_SHA  (검증 후 제거)
EOF
