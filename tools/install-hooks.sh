#!/usr/bin/env bash
# install-hooks.sh
#
# coastal-wiki 의 git hooks 를 설치. (재실행 안전)
#
# 사용:
#   bash tools/install-hooks.sh
#
# 동작:
#   - .git/hooks/pre-commit 을 작성/덮어쓰기.
#   - 기존 pre-commit 중 우리 마커가 없는 것은 .bak 으로 백업.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
WIKI_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
HOOK="$WIKI_ROOT/.git/hooks/pre-commit"
MARKER="# coastal-wiki:pre-commit:v4"

if [ ! -d "$WIKI_ROOT/.git" ]; then
    echo "ERROR: $WIKI_ROOT/.git 없음. git repo 루트에서 실행하세요."
    exit 1
fi

if [ -f "$HOOK" ] && ! grep -q "coastal-wiki:pre-commit" "$HOOK" 2>/dev/null; then
    cp "$HOOK" "$HOOK.bak"
    echo "기존 pre-commit hook 백업: $HOOK.bak"
fi

cat > "$HOOK" <<EOF
#!/usr/bin/env bash
$MARKER
# 정책 출처: plan.md M10·D3·G8 + 2차 review F1·F3 (2026-05-23) + 정화 G8 (2026-06-18)
# 검사 순서:
#   1) staged path guard (F3) — models/*/raw/{source_code,manuals}/ reject
#   2) 대용량 staged blob 경고 (옵션 임계치 COASTAL_WIKI_MAX_BLOB_MB, 기본 50MB)
#   3) research isolation 검증 — staged snapshot 기준 (F1)
#   4) canonical hygiene 검증 (G8b 경로·G8d placeholder) — staged snapshot
#   5) 내부 링크 무결성 (깨진 상대 .md 링크·[[wikilink]]) — staged snapshot
set -euo pipefail

WIKI_ROOT="\$(git rev-parse --show-toplevel)"
cd "\$WIKI_ROOT"

# ---------- 1) staged path guard (F3) ----------
forbidden=\$(git diff --cached -z --name-only --diff-filter=ACMR \\
    | tr '\0' '\n' \\
    | grep -E '^models/[^/]+/raw/(source_code|manuals)/' || true)

if [ -n "\$forbidden" ]; then
    echo "pre-commit: 다음 staged 파일이 vendor raw 영역(.gitignore 보호 대상)을 위반합니다:"
    printf '  %s\n' \$forbidden
    echo
    echo "  → 'models/*/raw/{source_code,manuals}/' 는 vendor 원본이라 git 에 들어가면 안 됩니다."
    echo "  → 'git add -f' 등으로 강제 추가된 것 같습니다."
    echo "  → 'git restore --staged <path>' 로 unstage 후 재시도하세요."
    echo "  (정책: plan.md D1·F3)"
    exit 1
fi

# ---------- 2) 대용량 staged blob 체크 ----------
threshold_mb="\${COASTAL_WIKI_MAX_BLOB_MB:-50}"
threshold_bytes=\$((threshold_mb * 1024 * 1024))
big=""
while IFS= read -r -d '' p; do
    [ -z "\$p" ] && continue
    size=\$(git cat-file -s ":\$p" 2>/dev/null || echo 0)
    if [ "\$size" -gt "\$threshold_bytes" ]; then
        mb=\$(awk "BEGIN {printf \"%.1f\", \$size/1024/1024}")
        big="\${big}  \$p (\${mb} MB)
"
    fi
done < <(git diff --cached -z --name-only --diff-filter=ACMR)

if [ -n "\$big" ]; then
    echo "pre-commit: 다음 staged blob 가 \${threshold_mb}MB 초과:"
    printf '%s' "\$big"
    echo "  → push 부담 / 호스트 한도(GitHub 100MB) 위험."
    echo "  → 의도된 commit 이면 COASTAL_WIKI_MAX_BLOB_MB=N bash ... 로 임계치 조정."
    echo "  → 또는 .gitignore / git LFS 검토."
    exit 1
fi

# ---------- 3) research isolation (staged snapshot) ----------
SCRIPT="\$WIKI_ROOT/tools/validate-research-isolation.sh"
if [ ! -x "\$SCRIPT" ]; then
    echo "pre-commit: \$SCRIPT 실행 불가. chmod +x 또는 누락 확인."
    exit 1
fi
bash "\$SCRIPT" --staged

# ---------- 4) canonical hygiene (G8b 경로 · G8d placeholder, staged snapshot) ----------
HYGIENE="\$WIKI_ROOT/tools/validate-canonical-hygiene.sh"
if [ ! -x "\$HYGIENE" ]; then
    echo "pre-commit: \$HYGIENE 실행 불가. chmod +x 또는 누락 확인."
    exit 1
fi
bash "\$HYGIENE" --staged

# ---------- 5) 내부 링크 무결성 (staged snapshot) ----------
LINKS="\$WIKI_ROOT/tools/validate-link-integrity.sh"
if [ ! -x "\$LINKS" ]; then
    echo "pre-commit: \$LINKS 실행 불가. chmod +x 또는 누락 확인."
    exit 1
fi
bash "\$LINKS" --staged
EOF

chmod +x "$HOOK"
echo "OK: pre-commit hook 설치 → $HOOK"
echo "테스트(working tree): bash tools/validate-research-isolation.sh"
echo "테스트(staged):       bash tools/validate-research-isolation.sh --staged"
