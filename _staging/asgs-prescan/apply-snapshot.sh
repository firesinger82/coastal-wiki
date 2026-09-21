#!/usr/bin/env bash
# asgs snapshot 교체 — 노트 좌표는 이미 upstream 기준으로 갱신됐으므로 정합을 맞춘다
set -euo pipefail
WIKI="/home/firesinger/coastal-wiki"; MIG="$WIKI/_staging/asgs-prescan"
SRC="$WIKI/models/ADCIRC/raw/source_code/asgs"
STG="/home/firesinger/.cache/coastal-snapshots/asgs-upstream"
OLD="aeb383324bb486a5c4d834ce4edd99a7086566c8"; NEW="08d5187966f4e96f3b37f10f29b9cf37dbf9ba6c"; OWNER="firesinger"
say(){ printf '\n=== %s ===\n' "$*"; }; die(){ printf '\nABORT: %s\n' "$*" >&2; exit 1; }
say "0. 사전 조건"
[ "$(git -c safe.directory='*' -C "$STG" rev-parse HEAD)" = "$NEW" ] || die "staging HEAD 불일치"
[ "$(git -c safe.directory='*' -C "$SRC" rev-parse HEAD)" = "$OLD" ] || die "설치 HEAD 불일치"
[ -z "$(git -c safe.directory='*' -C "$SRC" status --porcelain)" ] || die "로컬 변경 있음"
echo OK
say "1. before-hash (소스)"
python3 - "$MIG" "$SRC" <<'PY'
import csv,hashlib,sys; from pathlib import Path
mig,src=map(Path,sys.argv[1:3])
def sha(p):
    h=hashlib.sha256()
    with open(p,"rb") as f:
        for b in iter(lambda:f.read(1<<20),b""): h.update(b)
    return h.hexdigest()
bad=[r["path"] for r in csv.DictReader(open(mig/"manifest-B-installed.csv"))
     if not (src/r["path"]).exists() or sha(src/r["path"])!=r["sha256"]]
if bad: print("MISMATCH",len(bad),bad[:5]); sys.exit(1)
print("OK")
PY
say "2. 교체"
rm -rf "$SRC.old-$OLD"; mv "$SRC" "$SRC.old-$OLD"; cp -a "$STG" "$SRC"
chown -R root:root "$SRC"; chmod -R a-w "$SRC"
echo "HEAD=$(git -c safe.directory='*' -C "$SRC" rev-parse HEAD)"
say "3. after-hash"
python3 - "$MIG" "$SRC" <<'PY'
import csv,hashlib,sys; from pathlib import Path
mig,src=map(Path,sys.argv[1:3])
def sha(p):
    h=hashlib.sha256()
    with open(p,"rb") as f:
        for b in iter(lambda:f.read(1<<20),b""): h.update(b)
    return h.hexdigest()
bad=[r["path"] for r in csv.DictReader(open(mig/"manifest-A-staging.csv"))
     if not (src/r["path"]).exists() or sha(src/r["path"])!=r["sha256"]]
if bad: print("MISMATCH",len(bad),bad[:5]); sys.exit(1)
print("OK")
PY
say "4. 잠금"
W1=$(sudo -u "$OWNER" find "$WIKI/models" -writable 2>/dev/null | wc -l); echo "쓰기 가능: $W1"
[ "$W1" -eq 0 ] || die "잠금 실패"
say "5. 구 스냅샷 제거 (복원은 pinned 커밋 객체로)"
git -c safe.directory='*' -C "$SRC" cat-file -t "$OLD" >/dev/null || die "pinned 객체 없음 — .old 유지"
chmod -R u+w "$SRC.old-$OLD"; rm -rf "$SRC.old-$OLD"; echo "removed .old-$OLD"
say "완료"
