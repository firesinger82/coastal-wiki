#!/usr/bin/env bash
# ADCIRC source snapshot 적용: 6037225 → e8b62a70
# 사용자가 일반 계정으로 실행(내부에서 필요한 명령만 sudo). 삭제·덮어쓰기 명령 없음.
#   bash ~/coastal-wiki/_staging/adcirc-upstream-review/apply-snapshot.sh
# v2: SIGPIPE(tar|head) 로 중단되던 문제 수정 + 이미 만들어진 백업은 검증 후 재사용.
set -euo pipefail

SRCDIR="$HOME/coastal-wiki/models/ADCIRC/raw/source_code"
STG="$HOME/.cache/coastal-snapshots/adcirc-e8b62a70"
OLD="$SRCDIR/adcirc.old-6037225"
INS="$SRCDIR/adcirc"
TAR=/opt/coastal-snapshots/adcirc-6037225.tar.zst
LIST=$(mktemp)
BASE=6037225ce4573efd3c1f8877a5dc908d01c199a8
NEW=e8b62a70db39dbc8875785ee999a2214be75302b
G=(git -c safe.directory='*' --no-optional-locks)

blocked() { echo "BLOCKED: $*" >&2; exit 1; }
step() { printf '\n== %s\n' "$*"; }
trap 'rm -f "$LIST"' EXIT

[ "$(id -u)" -ne 0 ] || blocked "root 로 직접 실행하지 마세요 (경로가 /root 로 잡힙니다). 일반 계정으로 실행하면 필요한 곳에서만 sudo 를 씁니다."

step "0. PRE-APPLY GATE"
[ -d "$INS" ] || blocked "설치본 없음: $INS"
[ -d "$STG" ] || blocked "staging 없음: $STG"
[ "$("${G[@]}" -C "$INS" rev-parse HEAD)" = "$BASE" ] || blocked "설치본 HEAD 가 baseline($BASE) 이 아님"
[ -z "$("${G[@]}" -C "$INS" status --porcelain)" ] || blocked "설치본에 예상 밖 로컬 수정 있음"
[ "$("${G[@]}" -C "$STG" rev-parse HEAD)" = "$NEW" ] || blocked "staging HEAD 가 목표($NEW) 가 아님"
[ -z "$("${G[@]}" -C "$STG" status --porcelain)" ] || blocked "staging 작업트리가 깨끗하지 않음"
[ ! -e "$OLD" ] || blocked "rollback 경로가 이미 존재: $OLD (덮어쓰지 않음)"
echo "PASS — installed=$BASE, staging=$NEW, rollback 경로 비어 있음"

step "1. BACKUP (없으면 생성, 있으면 재사용 — 덮어쓰지 않음)"
if [ -e "$TAR" ]; then
  echo "기존 백업 재사용: $TAR"
else
  sudo mkdir -p /opt/coastal-snapshots
  sudo tar --zstd -cf "$TAR" -C "$SRCDIR" adcirc
  echo "새 백업 생성: $TAR"
fi

step "2. BACKUP 비어있지 않은지"
sudo test -s "$TAR" || blocked "백업이 비어 있음"
ls -lh "$TAR"

step "3. BACKUP 목록 판독 (전체 목록을 임시파일로 — SIGPIPE 회피)"
sudo tar --zstd -tf "$TAR" > "$LIST"
head -3 "$LIST"
echo "  ... 총 $(wc -l < "$LIST") 항목"
grep -qx 'adcirc/src/gwce.F' "$LIST" || blocked "백업 목록에 예상 파일(adcirc/src/gwce.F)이 없음"

step "4. BACKUP sha256 기록"
if [ -e "$TAR.sha256" ]; then
  echo "기존 해시 파일 유지: $(sudo cat "$TAR.sha256")"
else
  sudo sha256sum "$TAR" | sudo tee "$TAR.sha256"
fi

step "5. rollback 경로 재확인"
[ ! -e "$OLD" ] || blocked "rollback 경로가 생성됨: $OLD"

step "6. 기존 설치본 → $OLD (atomic rename, 삭제 아님)"
sudo mv -n "$INS" "$OLD"
sudo test -d "$OLD" || blocked "rename 실패"
[ ! -e "$INS" ] || blocked "rename 후에도 옛 경로가 남아 있음"

step "7. staging → 새 설치본 복사 (staging 원본 보존)"
sudo cp -a "$STG" "$INS"

step "8. 소유 복구 root:root"
sudo chown -R root:root "$INS"

step "9. 재잠금 (쓰기 권한 제거)"
sudo chmod -R a-w "$INS"

step "10. 적용 직후 확인 (.old 와 tar 는 삭제하지 않음)"
stat -c '%A %U %n' "$INS" "$OLD"
echo "HEAD=$("${G[@]}" -C "$INS" rev-parse HEAD)"
echo "tracked=$("${G[@]}" -C "$INS" ls-files | wc -l)"
if [ -f "$INS/CITATION.cff" ]; then echo "CITATION.cff 존재"; else echo "CITATION.cff 없음 (검증 실패 처리)"; fi

printf '\nAPPLY DONE — Claude 에게 알리면 post-apply verification(manifest 전수 대조)을 수행합니다.\n'
