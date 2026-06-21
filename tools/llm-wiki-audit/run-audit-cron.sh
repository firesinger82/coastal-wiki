#!/usr/bin/env bash
# L4 V3 — 야간 자율 citation 감사 cron 러너
# 설계: plan.md "L4 자가 감사 루프 PoC 설계" V3 (Hermes cron 급 야간 자율, 사람은 리포트만).
# coastal-audit (Claude Code skill) 을 headless 로 1 라운드로빈 슬라이스 실행.
#
# 불변식 (CLAUDE.md 절대규칙 #1 + skill report-only):
#   - canonical(concepts/models/textbook/experience + 거버넌스 .md) 절대 미수정.
#     스킬이 보장하나, 자율 런타임이라 런너가 사후 *강제 복원*으로 이중 차단.
#   - 산출물 = _staging/audit/ (리포트·ledger·제안패치) 뿐. 제안패치는 생성만, 미적용.
#   - 커밋은 _staging/audit/ 만. push 는 안 함 (사람이 검토 후).
#
# 환경변수:
#   COASTAL_WIKI_DIR  repo 경로 (기본 $HOME/coastal-wiki)
#   L4_AUDIT_N        슬라이스 크기 (기본 8)
#   L4_DRY_RUN=1      claude 호출을 stub 으로 대체 (plumbing 테스트용)
#   L4_NO_COMMIT=1    _staging/audit 자동 커밋 생략 (리포트만 남김)
set -uo pipefail

REPO="${COASTAL_WIKI_DIR:-$HOME/coastal-wiki}"
N="${L4_AUDIT_N:-8}"
TS="$(date +%Y-%m-%d_%H-%M-%S)"
LOG_DIR="$REPO/_staging/audit/cron-logs"
LOG="$LOG_DIR/$TS.log"
CANONICAL_PATHS=(concepts models textbook experience CONVENTIONS.md CLAUDE.md README.md INDEX.md plan.md BOUNDARY.md)

cd "$REPO" || { echo "repo 없음: $REPO" >&2; exit 1; }
mkdir -p "$LOG_DIR"
exec >>"$LOG" 2>&1
echo "=== L4 V3 audit run $TS (N=$N, dry=${L4_DRY_RUN:-0}) ==="

# 0. 사전조건: audit 출력 외 미커밋 변경 있으면 중단 (writer 작업과 충돌 방지)
DIRTY_NONAUDIT="$(git status --porcelain | grep -v '^.. _staging/audit/' || true)"
if [ -n "$DIRTY_NONAUDIT" ]; then
  echo "ABORT: audit 외 미커밋 변경 존재 — 안전상 중단:"
  echo "$DIRTY_NONAUDIT" | head
  exit 2
fi

# 1. 최신화 (writer PC 기준; ff-only 실패해도 진행은 안 함 — divergence 시 사람 개입)
if ! git pull --ff-only 2>&1 | tail -3; then
  echo "WARN: git pull --ff-only 실패 (divergence?) — 현 HEAD 로 진행"
fi
echo "HEAD=$(git rev-parse --short HEAD)"

# 2. coastal-audit headless 실행
if [ "${L4_DRY_RUN:-0}" = "1" ]; then
  echo "[DRY_RUN] claude 호출 생략 — plumbing 만 검증"
else
  # report-only 스킬을 headless 로. canonical write 는 step 3 가 강제 복원.
  claude -p "/coastal-audit --n $N" \
    --permission-mode acceptEdits \
    --allowedTools "Read,Bash,Write,Skill,Glob,Grep" \
    --add-dir "$REPO" 2>&1 | tail -50
  echo "claude rc=${PIPESTATUS[0]}"
fi

# 3. 하드 report-only 가드 — _staging/audit/ 외 변경은 무조건 되돌림
echo "--- report-only 가드 (canonical 변경 복원) ---"
for p in "${CANONICAL_PATHS[@]}"; do
  [ -e "$p" ] || continue
  if ! git diff --quiet -- "$p" 2>/dev/null; then
    echo "WARN: canonical 수정 감지 → 복원: $p"; git checkout -- "$p" 2>/dev/null
  fi
done
# 새로 생성된(untracked) canonical 파일 제거
git ls-files --others --exclude-standard -- "${CANONICAL_PATHS[@]}" 2>/dev/null | while read -r f; do
  echo "WARN: cron 생성 canonical 파일 제거: $f"; rm -f "$f"
done

# 4. audit 산출물만 커밋 (감사 메타 = canonical 아님). push 안 함.
if [ "${L4_NO_COMMIT:-0}" = "1" ]; then
  echo "L4_NO_COMMIT=1 — 커밋 생략 (리포트만)"
elif [ -n "$(git status --porcelain _staging/audit/)" ]; then
  git add _staging/audit/
  git commit -q -m "chore(audit): L4 V3 자율 감사 $TS — N=$N (report-only, cron)

Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>" \
    && echo "audit 산출물 커밋 완료" || echo "커밋 실패"
else
  echo "audit 산출물 변경 없음"
fi
echo "=== done $TS ==="
