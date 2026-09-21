#!/usr/bin/env bash
# Delft3D source_scope 선언 — 엔진·패키지 동명 파일 귀속 (소스 교체 없음)
# 실행: sudo bash ~/coastal-wiki/_staging/delft3d-prescan/apply.sh
set -euo pipefail
WIKI="/home/firesinger/coastal-wiki"; MIG="$WIKI/_staging/delft3d-prescan"; OWNER="firesinger"
say(){ printf '\n=== %s ===\n' "$*"; }; die(){ printf '\nABORT: %s\n' "$*" >&2; exit 1; }
say "1. before-hash"
python3 - "$WIKI" "$MIG" <<'PY'
import csv,hashlib,sys; from pathlib import Path
wiki,mig=map(Path,sys.argv[1:3])
def sha(p):
    h=hashlib.sha256(); h.update(Path(p).read_bytes()); return h.hexdigest()
bad=[r["path"] for r in csv.DictReader(open(mig/"manifest-scope-notes.csv"))
     if not (wiki/r["path"]).exists() or sha(wiki/r["path"])!=r["before_sha256"]]
if bad: print("MISMATCH:",bad); sys.exit(1)
print("OK: 노트 48")
PY
say "2. 반영"
while IFS=, read -r path before after locked; do
  [ "$path" = "path" ] && continue
  t="$WIKI/$path"; chmod u+w "$t"; cp "$MIG/scope-candidate/$path" "$t"
  chown root:root "$t"; chmod a-w "$t"
done < "$MIG/manifest-scope-notes.csv"
echo "노트 48개 반영"
say "3. after-hash"
python3 - "$WIKI" "$MIG" <<'PY'
import csv,hashlib,sys; from pathlib import Path
wiki,mig=map(Path,sys.argv[1:3])
def sha(p):
    h=hashlib.sha256(); h.update(Path(p).read_bytes()); return h.hexdigest()
bad=[r["path"] for r in csv.DictReader(open(mig/"manifest-scope-notes.csv")) if sha(wiki/r["path"])!=r["after_sha256"]]
if bad: print("MISMATCH:",bad); sys.exit(1)
print("OK")
PY
say "4. 잠금 확인 (일반 사용자 권한)"
W1=$(sudo -u "$OWNER" find "$WIKI/models" -writable 2>/dev/null | wc -l)
echo "쓰기 가능: $W1"; [ "$W1" -eq 0 ] || die "잠금 실패"
say "완료"
