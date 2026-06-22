#!/usr/bin/env bash
# L4 V3 — 야간 자율 citation 감사 cron 러너
# 설계: plan.md "L4 자가 감사 루프 PoC 설계" V3 (야간 자율, 사람은 리포트만).
# coastal-audit (Claude Code skill) 을 headless 로 1 라운드로빈 슬라이스 실행.
#
# 불변식 (CLAUDE.md 절대규칙 #1 + skill report-only):
#   - cron 으로는 _staging/audit/ 외 어떤 파일도 커밋되지 않는다.
#     1차 보장 = 커밋 스코프(`git add _staging/audit/` + 스테이징 assert).
#     2차 보장 = 실행 후 가드: tracked 수정 복원 + *이번 run 이 새로 만든* untracked 만 제거.
#   - 산출물 = _staging/audit/ (리포트·ledger·제안패치). 제안패치는 생성만, 미적용. push 안 함.
#
# ★ 이 repo 는 정상적으로 untracked 작업물이 상존한다(Hermes research/inbox·_archive·
#   _staging/from-modeling-wiki·작성중 모델노트). 따라서:
#   - step0 은 *tracked 수정*만 검사(untracked 무시) — 아니면 매번 abort.
#   - step3 은 blanket `git clean` 금지 — 실행 전 스냅샷과 diff 해 *새로 생긴* untracked 만 제거.
#
# 알려진 잔여 리스크(F2): claude 실행(~2분) *도중* writer 가 tracked 파일을 편집하면 step3 가
#   되돌릴 수 있음. 완화 = flock + 야간(writer idle) 시각 + step0. cron 은 writer 미작업 시간에.
#
# 환경변수: COASTAL_WIKI_DIR(기본 $HOME/coastal-wiki) · L4_AUDIT_N(기본 8) ·
#           L4_DRY_RUN=1(claude stub) · L4_NO_COMMIT=1(커밋 생략)
set -uo pipefail

REPO="${COASTAL_WIKI_DIR:-$HOME/coastal-wiki}"
N="${L4_AUDIT_N:-8}"
TS="$(date +%Y-%m-%d_%H-%M-%S)"
LOG_DIR="$REPO/_staging/audit/cron-logs"   # gitignore 됨
LOG="$LOG_DIR/$TS.log"
LOCK="$LOG_DIR/.lock"

cd "$REPO" || { echo "repo 없음: $REPO" >&2; exit 1; }
mkdir -p "$LOG_DIR" || { echo "로그 디렉토리 생성 실패" >&2; exit 1; }
exec >>"$LOG" 2>&1
echo "=== L4 V3 audit run $TS (N=$N, dry=${L4_DRY_RUN:-0}) ==="

# 동시 실행 방지
exec 9>"$LOCK"
if ! flock -n 9; then echo "다른 audit 실행 중(flock) — skip"; exit 0; fi

# 0. 사전조건: _staging/audit 외 *tracked* 미커밋 변경 있으면 중단 (untracked 워크벤치는 무시)
DIRTY_TRACKED="$(git status --porcelain --untracked-files=no | grep -v '^.. _staging/audit/' || true)"
if [ -n "$DIRTY_TRACKED" ]; then
  echo "ABORT(step0): _staging/audit 외 tracked 미커밋 변경 존재 — 중단:"
  echo "$DIRTY_TRACKED" | head
  exit 2
fi

# 1. 최신화 (single-writer 라 divergence 사실상 없음)
if ! git pull --ff-only 2>&1 | tail -3; then
  echo "WARN: git pull --ff-only 실패(divergence?) — 현 HEAD 진행"
fi
echo "HEAD=$(git rev-parse --short HEAD)"

# 2. 실행 전 untracked 스냅샷 (기존 Hermes/archive 작업물 보존용)
SNAP_UNTRACKED="$(git status --porcelain --untracked-files=all | grep '^??' | cut -c4- | sort || true)"

# 3. coastal-audit headless 실행 (report-only 스킬; canonical write 는 step4 가드가 복원)
if [ "${L4_DRY_RUN:-0}" = "1" ]; then
  echo "[DRY_RUN] claude 호출 생략"
else
  claude -p "/coastal-audit --n $N" \
    --permission-mode acceptEdits \
    --allowedTools "Read,Bash,Write,Skill,Glob,Grep" \
    --add-dir "$REPO" 2>&1 | tail -50
  echo "claude rc=${PIPESTATUS[0]}"
fi

# 4. 하드 가드 — _staging/audit/ 외 변경 제거
echo "--- report-only 가드 ---"
# (a) tracked 수정 복원 (_staging/audit 제외). step0 에서 clean 이었으니 이건 claude 의 수정.
git checkout -- . ':(exclude)_staging/audit' 2>/dev/null || echo "WARN: 일부 tracked 복원 실패"
# (b) *이번 run 이 새로 만든* untracked 만 제거 (스냅샷에 없던 것). 기존 워크벤치 보존.
NOW_UNTRACKED="$(git status --porcelain --untracked-files=all | grep '^??' | cut -c4- | sort || true)"
comm -13 <(printf '%s\n' "$SNAP_UNTRACKED") <(printf '%s\n' "$NOW_UNTRACKED") | while read -r f; do
  [ -z "$f" ] && continue
  case "$f" in _staging/audit/*) continue ;; esac
  echo "WARN: cron 생성 untracked 제거: $f"; rm -rf -- "$f"
done
# (c) 최종 점검(tracked): _staging/audit 외 tracked 변경 잔존이면 커밋 중단(가시화)
LEFTOVER="$(git status --porcelain --untracked-files=no | grep -v '^.. _staging/audit/' || true)"
if [ -n "$LEFTOVER" ]; then
  echo "ALERT(step4c): 가드 후 _staging/audit 외 tracked 변경 잔존 — 커밋 중단:"
  echo "$LEFTOVER" | head; exit 3
fi

# 5. audit 산출물만 커밋 (감사 메타 = canonical 아님). push 안 함.
if [ "${L4_NO_COMMIT:-0}" = "1" ]; then
  echo "L4_NO_COMMIT=1 — 커밋 생략"
elif [ -n "$(git status --porcelain _staging/audit/)" ]; then
  git add _staging/audit/
  if git diff --cached --name-only | grep -qv '^_staging/audit/'; then
    echo "ALERT(step5): _staging/audit 외 스테이징 감지 — 커밋 중단:"
    git diff --cached --name-only | grep -v '^_staging/audit/' | head
    git reset -q; exit 4
  fi
  git commit -q -m "chore(audit): L4 V3 자율 감사 $TS — N=$N (report-only, cron)

Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>" \
    && echo "audit 산출물 커밋 완료" || echo "커밋 실패"
else
  echo "audit 산출물 변경 없음"
fi
echo "=== done $TS ==="
