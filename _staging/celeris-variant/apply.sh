#!/usr/bin/env bash
# Celeris 변종 선언 — 노트 frontmatter 에 source_scope 추가 (소스 교체 없음)
# 실행: sudo bash ~/coastal-wiki/_staging/celeris-variant/apply.sh
set -euo pipefail
WIKI="/home/firesinger/coastal-wiki"; MIG="$WIKI/_staging/celeris-variant"; OWNER="firesinger"
say(){ printf '\n=== %s ===\n' "$*"; }; die(){ printf '\nABORT: %s\n' "$*" >&2; exit 1; }

say "1. before-hash"
python3 - "$WIKI" "$MIG" <<'PY'
import csv,hashlib,sys; from pathlib import Path
wiki,mig=map(Path,sys.argv[1:3])
def sha(p):
    h=hashlib.sha256(); h.update(Path(p).read_bytes()); return h.hexdigest()
bad=[r["path"] for r in csv.DictReader(open(mig/"manifest-notes.csv"))
     if not (wiki/r["path"]).exists() or sha(wiki/r["path"])!=r["before_sha256"]]
if bad: print("MISMATCH:",bad); sys.exit(1)
print("OK")
PY

say "2. 백업"
mkdir -p /opt/coastal-snapshots
tar --zstd -cf /opt/coastal-snapshots/celeris-notes-before-variant.tar.zst -C "$WIKI" \
    $(cut -d, -f1 "$MIG/manifest-notes.csv" | tail -n +2)
sha256sum /opt/coastal-snapshots/celeris-notes-before-variant.tar.zst

say "3. 반영"
while IFS=, read -r path before after locked; do
  [ "$path" = "path" ] && continue
  t="$WIKI/$path"; chmod u+w "$t"; cp "$MIG/wiki-candidate/$path" "$t"
  chown root:root "$t"; chmod a-w "$t"
done < "$MIG/manifest-notes.csv"
echo "노트 반영 완료"

say "4. after-hash"
python3 - "$WIKI" "$MIG" <<'PY'
import csv,hashlib,sys; from pathlib import Path
wiki,mig=map(Path,sys.argv[1:3])
def sha(p):
    h=hashlib.sha256(); h.update(Path(p).read_bytes()); return h.hexdigest()
bad=[r["path"] for r in csv.DictReader(open(mig/"manifest-notes.csv"))
     if sha(wiki/r["path"])!=r["after_sha256"]]
if bad: print("MISMATCH:",bad); sys.exit(1)
print("OK")
PY

say "5. 잠금 확인 (일반 사용자 권한)"
W1=$(sudo -u "$OWNER" find "$WIKI/models" -writable 2>/dev/null | wc -l)
echo "쓰기 가능: $W1"; [ "$W1" -eq 0 ] || die "잠금 실패"
say "완료"
