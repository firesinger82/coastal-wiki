#!/usr/bin/env bash
# install-hooks.sh
#
# coastal-wiki 의 git hooks 를 설치. (재실행 안전)
#
# 사용:
#   bash tools/install-hooks.sh [--writer|--reader]
#
# 역할(R1 I-4, Codex 20회차): --reader 지정 시 이 클론의 커밋을 pre-commit 이 거부
# (절대규칙 #5 단일 writer 의 '커밋·push 사고 2차 방어' — 미커밋 편집은 못 막음, 한계 명시).
# 역할 파일 = `git rev-parse --git-path wiki-role` (worktree 호환). 미지정 = legacy
# (역할 검사 skip, 경고 1줄 — 기존 clone 후방호환).
#
# 동작:
#   - .git/hooks/pre-commit 을 작성/덮어쓰기.
#   - 기존 pre-commit 중 우리 마커가 없는 것은 .bak 으로 백업.
#   - post-merge/post-checkout/post-commit 재색인 훅 설치.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
WIKI_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
HOOK="$WIKI_ROOT/.git/hooks/pre-commit"
MARKER="# coastal-wiki:pre-commit:v7"

if [ ! -d "$WIKI_ROOT/.git" ] && [ ! -f "$WIKI_ROOT/.git" ]; then
    echo "ERROR: $WIKI_ROOT/.git 없음. git repo 루트에서 실행하세요."
    exit 1
fi

# ---------- 역할 지정 (R1 I-4) ----------
ROLE_FILE="$(cd "$WIKI_ROOT" && git rev-parse --git-path wiki-role)"
case "$WIKI_ROOT" in /*) : ;; esac
case "$ROLE_FILE" in
    /*) : ;;
    *) ROLE_FILE="$WIKI_ROOT/$ROLE_FILE" ;;
esac
case "${1:-}" in
    --writer) echo "writer" > "$ROLE_FILE"; echo "역할 기록: writer → $ROLE_FILE" ;;
    --reader) echo "reader" > "$ROLE_FILE"; echo "역할 기록: reader → $ROLE_FILE (이 클론의 커밋은 pre-commit 이 거부)" ;;
    "")
        if [ ! -f "$ROLE_FILE" ]; then
            echo "⚠ 역할 미지정(legacy 설치) — 커밋 역할 검사 없음. 리더 머신이면 'bash tools/install-hooks.sh --reader' 로 재실행하세요."
        fi ;;
    *) echo "ERROR: 알 수 없는 옵션 '$1' (--writer|--reader)"; exit 1 ;;
esac

if [ -f "$HOOK" ] && ! grep -q "coastal-wiki:pre-commit" "$HOOK" 2>/dev/null; then
    cp "$HOOK" "$HOOK.bak"
    echo "기존 pre-commit hook 백업: $HOOK.bak"
fi

cat > "$HOOK" <<EOF
#!/usr/bin/env bash
$MARKER
# 정책 출처: plan.md M10·D3·G8 + 2차 review F1·F3 (2026-05-23) + 정화 G8 (2026-06-18) + R1 I-4 (2026-07-17)
# 검사 순서:
#   0) 역할 가드 (R1 I-4) — wiki-role == reader 면 커밋 거부 (절대규칙 #5 2차 방어)
#   1) staged path guard (F3) — models/*/raw/{source_code,manuals}/ reject
#   2) 대용량 staged blob 경고 (옵션 임계치 COASTAL_WIKI_MAX_BLOB_MB, 기본 50MB)
#   3) tools/validate-all.sh --staged — 무결성 validator 일괄 (목록 SSOT = validate-all.sh, F-8)
set -euo pipefail

WIKI_ROOT="\$(git rev-parse --show-toplevel)"
cd "\$WIKI_ROOT"

# ---------- 0) 역할 가드 (R1 I-4) ----------
ROLE_FILE="\$(git rev-parse --git-path wiki-role)"
if [ -f "\$ROLE_FILE" ] && [ "\$(cat "\$ROLE_FILE")" = "reader" ]; then
    if [ "\${COASTAL_WIKI_ALLOW_READER_COMMIT:-0}" = "1" ]; then
        echo "⚠⚠ [감사 흔적] reader 클론에서 커밋 강행 (COASTAL_WIKI_ALLOW_READER_COMMIT=1)" >&2
        echo "⚠⚠ 단일 writer 규칙(절대규칙 #5) 예외 — 사유를 커밋 메시지에 남기세요." >&2
    else
        echo "pre-commit: 이 클론은 read-only 리더(wiki-role=reader) — 커밋 거부." >&2
        echo "  → coastal-wiki 의 유일 writer 머신에서 커밋하거나, 이 변경을 폐기하세요:" >&2
        echo "     git restore --staged . && git checkout -- ." >&2
        echo "  → 정말 필요하면 COASTAL_WIKI_ALLOW_READER_COMMIT=1 (감사 흔적 출력됨)." >&2
        exit 1
    fi
fi

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

# ---------- 3~6) 무결성 validator 일괄 (단일 진입점, F-8) ----------
ALLV="\$WIKI_ROOT/tools/validate-all.sh"
if [ ! -x "\$ALLV" ]; then
    echo "pre-commit: \$ALLV 실행 불가. chmod +x 또는 누락 확인."
    exit 1
fi
bash "\$ALLV" --staged
EOF

chmod +x "$HOOK"
echo "OK: pre-commit hook 설치 → $HOOK"

# ---------- post-merge / post-checkout: LLM-Wiki 검색 인덱스 자동 재빌드 ----------
# (방식1 멀티머신: git pull/clone 후 FTS5 인덱스를 ~0.5s 재빌드 → reader 즉시 최신)
REINDEX_MARKER="# coastal-wiki:reindex:v1"

install_reindex_hook() {
    local hook_path="$1" guard="$2"
    if [ -f "$hook_path" ] && ! grep -q "coastal-wiki:reindex" "$hook_path" 2>/dev/null; then
        cp "$hook_path" "$hook_path.bak"
        echo "기존 $(basename "$hook_path") hook 백업: $hook_path.bak"
    fi
    cat > "$hook_path" <<EOF
#!/usr/bin/env bash
$REINDEX_MARKER
# git pull/merge/checkout 후 coastal-wiki FTS5 검색 인덱스 자동 재빌드.
# 실패해도 git 동작을 막지 않음(검색 편의 기능). 인덱스는 gitignore 파생물.
$guard
ROOT="\$(git rev-parse --show-toplevel 2>/dev/null)" || exit 0
SCRIPT="\$ROOT/tools/llm-wiki-poc/fts5_index.py"
[ -f "\$SCRIPT" ] || exit 0
command -v python3 >/dev/null 2>&1 || exit 0
if python3 "\$SCRIPT" build >/dev/null 2>&1; then
    echo "coastal-wiki: 검색 인덱스 재빌드 완료"
else
    echo "coastal-wiki: 검색 인덱스 재빌드 실패(무시) — 수동: python3 tools/llm-wiki-poc/fts5_index.py build"
fi
EOF
    chmod +x "$hook_path"
    echo "OK: $(basename "$hook_path") hook 설치 → $hook_path"
}

# post-merge: git pull/merge 후
install_reindex_hook "$WIKI_ROOT/.git/hooks/post-merge" ""
# post-checkout: 브랜치 전환($3=1)일 때만 (파일 checkout 은 skip)
install_reindex_hook "$WIKI_ROOT/.git/hooks/post-checkout" '[ "${3:-0}" = "1" ] || exit 0'
# post-commit: writer 의 일반 커밋 후에도 인덱스 최신 유지 (R1, Codex 20회차 — stale 인덱스 방지)
install_reindex_hook "$WIKI_ROOT/.git/hooks/post-commit" ""

echo
echo "테스트(working tree): bash tools/validate-research-isolation.sh"
echo "테스트(staged):       bash tools/validate-research-isolation.sh --staged"
echo "테스트(인덱스):       python3 tools/llm-wiki-poc/fts5_index.py build"
