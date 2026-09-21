#!/usr/bin/env bash
# 파일럿 5건의 롤백 자산 정리 (2026-09-21)
#
# 삭제 대상: /opt/coastal-snapshots 의 tar·sha256, models/ 의 <tree>.old-<sha> 디렉터리
# 삭제 근거: 설치 트리가 pinned 커밋 객체를 보유해 `git show <pinned>:<path>` 로 복원된다.
#            노트 이전 상태는 git 이력(origin/main 동기화)에 있다.
#
# 안전장치: 삭제 **전에** 5개 모델 모두에서 pinned 커밋 조회와 표본 파일 대조를 재확인한다.
#           하나라도 실패하면 아무것도 지우지 않는다.
#
# 실행: sudo bash ~/coastal-wiki/_staging/rollback-cleanup.sh
set -euo pipefail

WIKI="/home/firesinger/coastal-wiki"
BK="/opt/coastal-snapshots"
say(){ printf '\n=== %s ===\n' "$*"; }
die(){ printf '\nABORT: %s — 아무것도 삭제하지 않았다.\n' "$*" >&2; exit 1; }

say "0. 복원 경로 재확인 (삭제 전 필수)"
python3 - "$WIKI" <<'PY' || die "복원 검증 실패"
import hashlib, random, subprocess, sys
from pathlib import Path
W = Path(sys.argv[1])
CASES = [("ADCIRC","adcirc","6037225ce4573efd3c1f8877a5dc908d01c199a8","6037225"),
         ("EFDC","EFDCPlus_Stable","3ed76b6eb1263921ba99bf23b66bb85c1a5feac1",None),
         ("SWAN","swan","55441526ec4330338f05d148759fc66f6fc7fb9d",None),
         ("ROMS","roms","32c79b7435ee0a1a2cdd78fee07264e3bd93bb98",None),
         ("Celeris","Celeris-WebGPU","f6fd78bd12af3aeeef11774a850b6b3d52be65b3",None)]
def git(root,*a):
    return subprocess.run(["git","-c","safe.directory=*","-C",str(root),*a],capture_output=True)
random.seed(7); bad=0
for m,r,sha,suf in CASES:
    inst = W/f"models/{m}/raw/source_code/{r}"
    old  = W/f"models/{m}/raw/source_code/{r}.old-{suf or sha}"
    if git(inst,"cat-file","-t",sha).stdout.decode().strip() != "commit":
        print(f"  FAIL {m}: 설치 트리에 pinned 커밋 객체 없음"); bad+=1; continue
    files = git(inst,"ls-tree","-r","--name-only",sha).stdout.decode("utf-8","replace").split()
    files = [f for f in files if (old/f).is_file()]
    if not files:
        print(f"  WARN {m}: .old 디렉터리 비교 대상 없음(이미 정리됨?)"); continue
    smp = random.sample(files, min(12,len(files))); mism=0
    for f in smp:
        blob = git(inst,"show",f"{sha}:{f}").stdout
        if hashlib.sha256(blob).hexdigest() != hashlib.sha256((old/f).read_bytes()).hexdigest():
            mism+=1
    print(f"  {'OK  ' if mism==0 else 'FAIL'} {m:9} 표본 {len(smp)} 대조 불일치 {mism}")
    bad += (mism>0)
sys.exit(1 if bad else 0)
PY

say "1. 노트 이전 상태가 git 이력에 있는지"
cd "$WIKI"
[ -z "$(sudo -u firesinger git -C "$WIKI" status --porcelain models/)" ] || die "models/ 에 미커밋 변경 있음"
sudo -u firesinger git -C "$WIKI" rev-parse --verify origin/main >/dev/null || die "origin/main 없음"
echo "OK: models/ 깨끗하고 origin/main 존재"

say "2. 삭제 대상 목록"
BEFORE_OPT=$(du -sh "$BK" 2>/dev/null | cut -f1)
BEFORE_OLD=$(du -csh "$WIKI"/models/*/raw/source_code/*.old-* 2>/dev/null | tail -1 | cut -f1)
echo "  $BK                 : $BEFORE_OPT"
ls -1 "$BK" | sed 's/^/    /'
echo "  <tree>.old-<sha>    : ${BEFORE_OLD:-0}"
find "$WIKI"/models -maxdepth 4 -name "*.old-*" -type d | sed "s|$WIKI/|    |"

say "3. 삭제"
rm -rf "$BK"
echo "  removed $BK"
find "$WIKI"/models -maxdepth 4 -name "*.old-*" -type d -print0 |
  while IFS= read -r -d '' d; do chmod -R u+w "$d"; rm -rf "$d"; echo "  removed ${d#$WIKI/}"; done

say "4. 확인"
[ -d "$BK" ] && die "$BK 가 남아 있다"
rem=$(find "$WIKI"/models -maxdepth 4 -name "*.old-*" -type d | wc -l)
echo "  남은 .old 디렉터리: $rem"
[ "$rem" -eq 0 ] || die "일부 .old 디렉터리가 남았다"

say "5. 잠금 확인 (일반 사용자 권한)"
W1=$(sudo -u firesinger find "$WIKI/models" -writable 2>/dev/null | wc -l)
echo "  models/ 쓰기 가능: $W1"
[ "$W1" -eq 0 ] || die "잠금 실패 ($W1)"

say "완료"
echo "회수한 용량: /opt $BEFORE_OPT + .old ${BEFORE_OLD:-0}"
echo "복원 경로(유지): 설치 트리의 pinned 커밋 객체, upstream 원본, git 이력의 노트"
