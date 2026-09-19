#!/usr/bin/env bash
# ADCIRC 노트 19개 갱신분 설치 (models/ 는 root 잠금이라 sudo 필요)
# 일반 계정으로 실행:
#   bash ~/coastal-wiki/_staging/adcirc-upstream-review/apply-wiki-updates.sh
# 삭제·덮어쓰기 보호: 설치 전 각 파일의 현재 sha256 이 예상(before)과 같아야 진행.
set -euo pipefail

W="$HOME/coastal-wiki"
C="$W/_staging/adcirc-upstream-review/wiki-candidate"
MAN="$W/_staging/adcirc-upstream-review/wiki-install-manifest.csv"
BAK=/opt/coastal-snapshots/adcirc-notes-before-e8b62a70.tar.zst

blocked() { echo "BLOCKED: $*" >&2; exit 1; }
step() { printf '\n== %s\n' "$*"; }

[ "$(id -u)" -ne 0 ] || blocked "root 로 직접 실행하지 마세요 (경로가 /root 로 잡힙니다)."
[ -d "$C" ] || blocked "후보 디렉터리 없음: $C"
[ -f "$MAN" ] || blocked "manifest 없음: $MAN"
[ ! -e "$BAK" ] || blocked "백업 파일이 이미 존재: $BAK (덮어쓰지 않음)"

step "0. 대상 파일 현재 상태 검증 (before sha256 일치)"
n=0
while IFS=, read -r path before after; do
  [ "$path" = "path" ] && continue
  [ -f "$W/$path" ] || blocked "대상 없음: $path"
  cur=$(sha256sum "$W/$path" | cut -d' ' -f1)
  [ "$cur" = "$before" ] || blocked "$path 가 후보 생성 시점 이후 변경됨 (현재 $cur ≠ 예상 $before)"
  [ -f "$C/$path" ] || blocked "후보 파일 없음: $path"
  n=$((n+1))
done < "$MAN"
echo "PASS — 대상 $n 개 모두 예상 상태"

step "1. 현재 노트 백업 (rollback 용, 삭제하지 않음)"
sudo mkdir -p /opt/coastal-snapshots
( cd "$W" && cut -d, -f1 "$MAN" | tail -n +2 | sudo tar --zstd -cf "$BAK" -T - )
sudo test -s "$BAK"
sudo sha256sum "$BAK" | sudo tee "$BAK.sha256"

step "2. 설치 (내용 교체, 소유·권한 유지)"
while IFS=, read -r path before after; do
  [ "$path" = "path" ] && continue
  sudo cp --no-preserve=mode,ownership "$C/$path" "$W/$path"
  sudo chown root:root "$W/$path"
  sudo chmod 444 "$W/$path"
done < "$MAN"

step "3. 설치 후 해시 검증"
fail=0
while IFS=, read -r path before after; do
  [ "$path" = "path" ] && continue
  cur=$(sha256sum "$W/$path" | cut -d' ' -f1)
  if [ "$cur" != "$after" ]; then echo "MISMATCH $path"; fail=1; fi
done < "$MAN"
[ "$fail" -eq 0 ] || blocked "설치 후 해시 불일치 — rollback 필요"
echo "PASS — 19 파일 after sha256 일치"

step "4. 권한 확인"
while IFS=, read -r path before after; do
  [ "$path" = "path" ] && continue
  stat -c '%A %U %n' "$W/$path"
done < "$MAN" | head -3
echo "  ... (전체는 -r--r--r-- root)"

printf '\nWIKI UPDATE APPLIED — Claude 에게 알리면 validate-all·diff 검증을 수행합니다.\n'
