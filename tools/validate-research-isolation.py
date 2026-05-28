#!/usr/bin/env python3
"""validate-research-isolation.py — coastal-wiki D3 enforcer.

정책 출처: plan.md M10, CONVENTIONS.md §6, research/README.md §금지
결정 근거: codex adversarial-review 2026-05-23 (D3·F1·F2·G1·G2·H1·H2·H3·I1·I2)

검사:
  (a) 본문(concepts/, models/, experience/)이 research/ 로 직접 참조 —
      markdown inline link ](target), angle <target>, reference-style
      [label]: target (multi-line 허용), raw HTML href/src (quoted +
      unquoted). 각 target 을 파일 위치 기준 normpath 로 정규화하거나
      `/` prefix 면 repo-root 기준 정규화 후 research/ 안인지 판정.
  (b) research/ 내부 .md(governance 제외)가
      frontmatter `citation_status: draft-unsourced` 인지.

도구 범위(중요):
  이 스크립트는 **conservative policy scanner** 다. 정식 CommonMark/HTML
  파서가 아니다. 목적은 'research/ 본문 직접 참조' 라는 단일 invariant 를
  pre-commit 단계에서 잡아내는 것이고, 일반적인 실수와 흔한 변형 케이스
  (relative/absolute path, indented refdef, multi-line refdef destination,
  HTML href/src quoted/unquoted, data-* 같은 false-positive prone attr 제외)
  를 커버한다.

  spec-pathological 변형 (예: HTML comment 안의 attr, JS-injected DOM,
  base64 inline data URI 안 link, exotic Markdown extension)은 의도적으로
  cover 하지 않는다. 그런 케이스는 사용자 commit-time review + ultrareview
  multi-defense 로 처리한다.

  CommonMark 완전 준수가 필요하면 markdown-it-py / mistune 같은 parser
  도입 검토. 현재는 dependency 0 + ~33 fixture 회귀 보장으로 운영.

사용:
  python3 tools/validate-research-isolation.py            # working tree
  python3 tools/validate-research-isolation.py --staged   # staged snapshot

Exit codes:
  0 = OK
  1 = (a) 위반
  2 = (b) 위반
  3 = 둘 다
"""
from __future__ import annotations

import os
import re
import subprocess
import sys
from pathlib import Path

WIKI_ROOT = Path(__file__).resolve().parent.parent
os.chdir(WIKI_ROOT)

TARGET_ROOTS = ("concepts", "models", "experience")
GOVERNANCE_EXEMPT = {"research/README.md", "research/manifest.md"}
# research/prompts/ 는 Hermes 운영 자산 (cron 등록용 prompt 파일).
# research/seeds/ 는 Hermes literature-monitoring skill 의 검색 seed keyword 정의.
# 둘 다 본문성 아닌 governance 라서 frontmatter 면제. 정책: research/manifest.md §역할 분리.
GOVERNANCE_EXEMPT_PREFIXES = ("research/prompts/", "research/seeds/")


def is_governance_exempt(path: str) -> bool:
    """research/ 안의 governance 성격 파일 여부 (frontmatter 면제 대상)."""
    if path in GOVERNANCE_EXEMPT:
        return True
    return any(path.startswith(p) for p in GOVERNANCE_EXEMPT_PREFIXES)

URL_SCHEME_RE = re.compile(r"^[a-zA-Z][a-zA-Z0-9+.\-]*:")
INLINE_LINK_RE = re.compile(r"\]\(([^)\s]+)")
ANGLE_LINK_RE = re.compile(r"<([^>\s]+)>")
# G1+H1+H2+I1: CommonMark reference definition.
#   - leading indent: 0~3 spaces only (tab → column-expand → code block)
#   - colon 뒤 whitespace: 0+ space/tab 허용 (`[r]:foo` 도 유효)
#   - I1: colon 뒤 최대 1개 line ending 허용 ([r]:\n  ../research/x.md)
REF_DEF_RE = re.compile(
    r"(?m)^[ ]{0,3}\[[^\]]+\]:[ \t]*(?:\n[ \t]*)?(\S+)"
)
# H3+I2: raw HTML href/src — CommonMark 는 raw HTML 허용.
#   - double/single 쿼트 + unquoted 지원
#   - (?<![\w-]) 로 data-href, x-href 등 false positive 차단
HTML_HREF_RE = re.compile(
    r"""(?ix)
    (?<![\w-])                  # word boundary — data-href 등 제외
    (?:href|src)
    \s*=\s*
    (?:
        "([^"]*)"               # double-quoted
        | '([^']*)'             # single-quoted
        | ([^\s>"'`]+)          # unquoted (no whitespace, '>', quotes, backtick)
    )
    """
)
CODE_BLOCK_RE = re.compile(r"```.*?```", re.DOTALL)
INLINE_CODE_RE = re.compile(r"`[^`\n]+`")
FRONTMATTER_RE = re.compile(r"\A---\n(.*?)\n---", re.DOTALL)
CITATION_DRAFT_RE = re.compile(r"(?m)^citation_status:\s*draft-unsourced\s*$")


def run(cmd: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(cmd, capture_output=True, text=True, check=False)


def staged_files() -> list[str]:
    out = run(["git", "diff", "--cached", "-z", "--name-only", "--diff-filter=ACMR"])
    if out.returncode != 0:
        print(f"ERROR: git diff 실패: {out.stderr}", file=sys.stderr)
        sys.exit(10)
    return [p for p in out.stdout.split("\0") if p]


def tree_files(roots: tuple[str, ...]) -> list[str]:
    files: list[str] = []
    for root in roots:
        rp = Path(root)
        if not rp.is_dir():
            continue
        for p in rp.rglob("*.md"):
            files.append(str(p))
    return files


def read_staged(path: str) -> str:
    out = run(["git", "show", f":{path}"])
    return out.stdout if out.returncode == 0 else ""


def read_disk(path: str) -> str:
    try:
        return Path(path).read_text(encoding="utf-8", errors="replace")
    except (FileNotFoundError, IsADirectoryError):
        return ""


def extract_link_targets(content: str) -> list[str]:
    """Markdown + raw HTML 링크 target 추출. 코드/인라인 코드 제거."""
    stripped = CODE_BLOCK_RE.sub("", content)
    stripped = INLINE_CODE_RE.sub("", stripped)
    targets: list[str] = []
    targets.extend(m.group(1) for m in INLINE_LINK_RE.finditer(stripped))
    targets.extend(m.group(1) for m in ANGLE_LINK_RE.finditer(stripped))
    targets.extend(m.group(1) for m in REF_DEF_RE.finditer(stripped))
    # H3+I2: raw HTML href/src (double/single quote + unquoted)
    for m in HTML_HREF_RE.finditer(stripped):
        targets.append(m.group(1) or m.group(2) or m.group(3))
    return targets


def target_resolves_into_research(target: str, file_path: str) -> bool:
    """target 을 정규화해 repo-root research/ 안이면 True.

    경로 모델 (G2):
      - URL/스킴 (http:, mailto:, …) → skip (외부)
      - '/' 로 시작 → repo-root 기준 상대로 해석 (Obsidian vault, static site 흔한 컨벤션)
        예: '/research/inbox/x.md' → 'research/inbox/x.md'
      - 그 외 상대 경로 → file_path 의 디렉토리 기준으로 normpath
    """
    t = target.split("#", 1)[0].split("?", 1)[0].strip()
    if not t:
        return False
    if URL_SCHEME_RE.match(t):
        return False

    if t.startswith("/"):
        # G2: repo-root 기준 상대로 normalize
        resolved = os.path.normpath(t.lstrip("/"))
    else:
        file_dir = os.path.dirname(file_path) or "."
        resolved = os.path.normpath(os.path.join(file_dir, t))

    if resolved == "research":
        return True
    if resolved.startswith("research" + os.sep) or resolved.startswith("research/"):
        return True
    return False


def has_draft_unsourced(content: str) -> bool:
    m = FRONTMATTER_RE.match(content)
    if not m:
        return False
    return bool(CITATION_DRAFT_RE.search(m.group(1)))


def is_under_target_roots(path: str) -> bool:
    return any(path == r or path.startswith(r + "/") for r in TARGET_ROOTS)


def main() -> int:
    staged = "--staged" in sys.argv[1:]
    mode_label = "staged" if staged else "working-tree"

    reader = read_staged if staged else read_disk
    if staged:
        all_files = staged_files()
        body_files = [f for f in all_files if f.endswith(".md") and is_under_target_roots(f)]
        research_files = [f for f in all_files if f.endswith(".md") and f.startswith("research/")]
    else:
        body_files = [f for f in tree_files(TARGET_ROOTS) if f.endswith(".md")]
        research_files = [f for f in tree_files(("research",)) if f.endswith(".md")]

    # 검사 1
    print(f"[1/2] 본문 → research/ 참조 검사 (mode: {mode_label})…")
    ref_violations: list[tuple[str, str]] = []
    for f in body_files:
        content = reader(f)
        if not content:
            continue
        for t in extract_link_targets(content):
            if target_resolves_into_research(t, f):
                ref_violations.append((f, t))

    if ref_violations:
        print("  FAIL: 본문이 research/ 를 직접 참조:")
        for f, t in ref_violations:
            print(f"    {f} → {t}")
        print("  → research/ 자료는 promote 후 본문에 들어가야 합니다 (plan.md M10).")
    else:
        print("  OK: 본문에서 research/ 직접 참조 없음.")

    # 검사 2
    print("[2/2] research/ 내부 .md frontmatter 검사…")
    fm_violations: list[str] = []
    for f in research_files:
        if is_governance_exempt(f):
            continue
        content = reader(f)
        if not content:
            continue
        if not has_draft_unsourced(content):
            fm_violations.append(f)

    if fm_violations:
        print("  FAIL: 다음 파일이 'citation_status: draft-unsourced' frontmatter 결여:")
        for f in fm_violations:
            print(f"    {f}")
        print("  → research/ 내부 (.md, governance 제외) 는 draft-unsourced 로 시작해야 합니다.")
    else:
        print("  OK: research/ 내 모든 .md 가 draft-unsourced 또는 governance 면제.")

    fail_ref = bool(ref_violations)
    fail_fm = bool(fm_violations)
    print()
    if fail_ref and fail_fm:
        print("RESULT: FAIL (본문 참조 + frontmatter 둘 다)")
        return 3
    if fail_ref:
        print("RESULT: FAIL (본문이 research/ 참조)")
        return 1
    if fail_fm:
        print("RESULT: FAIL (research/ frontmatter 위반)")
        return 2
    print("RESULT: OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
