#!/usr/bin/env bash
# Delft3D 롤백 자산 정리 (2026-09-21) — rollback-cleanup.sh 후속(그 스크립트는 파일럿 5건만 대상이었다)
#
# 삭제 대상
#   models/Delft3D/raw/source_code/Delft3D.old-513eccd…   1.4G
#   /opt/coastal-snapshots/delft3d-*.tar.zst + .sha256     ~589M
#
# 삭제 근거 — 두 복원 경로가 모두 살아 있다
#   소스: 설치 트리가 pinned 커밋 513eccd 객체를 보유 → `git checkout 513eccd -- .` 로 복원
#   노트: 변경이 git 이력에 커밋됨(ca5f39b "migrate wiki notes to upstream 231bbf2 snapshot") + origin/main 동기화
#
# ★검증 방법 주의 (2026-09-21 실측):
#   raw blob(`git show <sha>:<path>`) 과 디스크 파일을 직접 대조하면 **EOL 필터가 적용되지 않아**
#   Delft3D 처럼 .gitattributes 로 CRLF 를 쓰는 저장소에서 가짜 불일치가 난다(표본 200 중 5건).
#   체크아웃이 실제로 재현하는 바이트는 `git cat-file --filters <sha>:<path>` 다 — 이것으로 대조하면 0건.
#   기존 rollback-cleanup.sh 의 대조는 이 필터를 적용하지 않는다(Fortran/JS 저장소라 우연히 통과했다).
#
# 안전장치: 아래 검증이 하나라도 실패하면 아무것도 지우지 않는다.
# 실행: sudo bash ~/coastal-wiki/_staging/delft3d-prescan/rollback-cleanup-delft3d.sh
set -euo pipefail

WIKI="/home/firesinger/coastal-wiki"
SRC="$WIKI/models/Delft3D/raw/source_code/Delft3D"
SHA="513eccdbe249919b3e5e62063dc91eb9fdf2347f"
OLD="$SRC.old-$SHA"
BK="/opt/coastal-snapshots"
OWNER="firesinger"
say(){ printf '\n=== %s ===\n' "$*"; }
die(){ printf '\nABORT: %s — 아무것도 삭제하지 않았다.\n' "$*" >&2; exit 1; }

say "0. 소스 복원 경로 검증 (표본 200, 체크아웃 필터 적용)"
[ -d "$OLD" ] || die "$OLD 없음"
python3 - "$SRC" "$OLD" "$SHA" <<'PY' || die "복원 검증 실패"
import hashlib, random, subprocess, sys
from pathlib import Path
src, old, sha = Path(sys.argv[1]), Path(sys.argv[2]), sys.argv[3]
def git(*a):
    return subprocess.run(["git","-c","safe.directory=*","-C",str(src),*a],capture_output=True)
if git("cat-file","-t",sha).stdout.decode().strip() != "commit":
    print("  FAIL: 설치 트리에 pinned 커밋 객체 없음"); sys.exit(1)
files=[f.decode("utf-8","replace") for f in git("ls-tree","-r","-z","--name-only",sha).stdout.split(b"\0") if f]
missing=[f for f in files if not (old/f).is_file()]
if missing:
    print(f"  FAIL: .old 에 없는 파일 {len(missing)}", missing[:3]); sys.exit(1)
print(f"  pinned tree {len(files)} 파일 — .old 전부 실재")
random.seed(11)
bad=[]
for f in random.sample(files, min(200,len(files))):
    want=hashlib.sha256(git("cat-file","--filters",f"{sha}:{f}").stdout).hexdigest()
    got =hashlib.sha256((old/f).read_bytes()).hexdigest()
    if want!=got: bad.append(f)
print(f"  표본 200 대조 불일치 {len(bad)}")
for b in bad[:5]: print("    MISMATCH", b)
sys.exit(1 if bad else 0)
PY

say "1. 노트 복원 경로 검증 (git 이력)"
[ -z "$(sudo -u "$OWNER" git -C "$WIKI" status --porcelain models/)" ] || die "models/ 에 미커밋 변경 있음"
sudo -u "$OWNER" git -C "$WIKI" rev-parse --verify origin/main >/dev/null || die "origin/main 없음"
sudo -u "$OWNER" git -C "$WIKI" cat-file -t ca5f39b >/dev/null 2>&1 || die "Delft3D 노트 마이그레이션 커밋 없음"
echo "  OK: models/ 깨끗 · origin/main 존재 · ca5f39b 보유"

say "2. 삭제 대상"
du -sh "$OLD" | sed 's/^/  /'
du -sh "$BK" 2>/dev/null | sed 's/^/  /' || true
ls -1 "$BK" 2>/dev/null | sed 's/^/    /' || true

say "3. 삭제"
chmod -R u+w "$OLD"; rm -rf "$OLD"; echo "  removed ${OLD#$WIKI/}"
rm -rf "$BK";        echo "  removed $BK"

say "4. 확인"
[ -d "$OLD" ] && die "$OLD 가 남아 있다"
[ -d "$BK" ]  && die "$BK 가 남아 있다"
rem=$(find "$WIKI"/models -maxdepth 5 -name "*.old-*" | wc -l)
echo "  남은 .old 자산: $rem"
[ "$rem" -eq 0 ] || die "일부 .old 가 남았다"

say "5. 잠금 확인 (일반 사용자 권한)"
W1=$(sudo -u "$OWNER" find "$WIKI/models" -writable 2>/dev/null | wc -l)
echo "  models/ 쓰기 가능: $W1"
[ "$W1" -eq 0 ] || die "잠금 실패 ($W1)"

say "6. 설치 트리 무결성 (삭제 후)"
echo "  HEAD=$(git -c safe.directory='*' -C "$SRC" rev-parse HEAD)"
[ -z "$(git -c safe.directory='*' -C "$SRC" status --porcelain)" ] || die "설치 트리에 변경 발생"
echo "  OK: 설치 트리 clean"

say "완료"
echo "복원 경로(유지): 설치 트리의 pinned 커밋 $SHA · git 이력의 노트(ca5f39b) · upstream 원본"
