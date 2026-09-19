#!/usr/bin/env python3
"""validate-canonical-hygiene.py — coastal-wiki G8 enforcer.

정책 출처: plan.md G8 (G8b 경로 문법 · G8d 본문 위생), CONVENTIONS.md §4·§6,
          CLAUDE.md 절대규칙 8.
결정 근거: 2026-06-18 canonical 정화 + Codex adversarial review 2-round (MODIFY).

검사 (canonical 콘텐츠 = concepts/·models/·textbook/ 의 authored .md):
  (G8b) 작성자 로컬 *식별* 절대경로 금지 — `/mnt/[a-z]/`, Windows drive(`D:\\`·
        `E:\\` …), `~/` home, `\\\\wsl$`. 공식 vendor 경로(`C:\\Program Files\\`,
        `/opt/`, `/usr/`)와 repo-상대 `file:line` 은 비위반.
  (G8d) 개인·프로젝트·실행 사례 기입을 유도하는 placeholder 금지 —
        "User-experience cases" 류, 또는 (체크박스/▢ + 개인사례 keyword) 한 줄.
  (G8e) 작성자 작업환경 흔적 금지 — `local path:`, "this workspace",
        "current local interpretation", "locally confirmed", "local note",
        "local machine/scripts/runnable/calibration/experiments", "위키 머신" 류
        (CONVENTIONS §4 중립 provenance·§6, 절대규칙 8). 2026-09-19 Jev 전수 스윕에서
        정화 잔존 흔적으로 확인된 표현만 등록. 기존 잔존분은 tree 모드에서 WARN(비실패),
        --staged 모드는 *이번에 추가된 줄*만 검사해 신규 유입을 차단.

도구 범위(중요):
  research-isolation validator 와 동일한 **conservative policy scanner** 철학.
  CommonMark/HTML 파서가 아니라 G8b/G8d 두 invariant 를 pre-commit 에서
  잡는 dependency-0 스캐너. 의미론적 출처 혼용(G8c)은 sources.yml 스키마
  보강 후 별도 검사 대상이라 여기서 다루지 않는다.

비대상 (G8b 적용 범위 = canonical 콘텐츠):
  - `models/*/raw/**`, `_staging/**`, `_archive/**` (vendor 미러·이력)
  - `*/_template/**` (템플릿)
  - `textbook/sources.yml` (로컬↔source_id 레지스트리 — .yml 이라 자연 제외)
  - 거버넌스/결정기록(repo-root CLAUDE.md·README.md·CONVENTIONS.md·plan.md 등)
    은 concepts/models/textbook 밖이라 자연 제외.

사용:
  python3 tools/validate-canonical-hygiene.py            # working tree
  python3 tools/validate-canonical-hygiene.py --staged   # staged snapshot

Exit codes (bit OR):
  0 = OK
  1 = G8b(경로) 위반
  2 = G8d(placeholder) 위반
  4 = G8e(작업환경 흔적) 신규 유입 (--staged 만; tree 모드 잔존분은 WARN)
"""
from __future__ import annotations

import os
import re
import subprocess
import sys
from pathlib import Path

WIKI_ROOT = Path(__file__).resolve().parent.parent
os.chdir(WIKI_ROOT)

# canonical 콘텐츠 루트 (G8b·G8d 적용). textbook 은 G8b 만 (excerpt 라 G8d 무관).
CANONICAL_ROOTS = ("concepts", "models", "textbook")
PLACEHOLDER_ROOTS = ("concepts", "models")

# 비대상 경로 segment (어느 위치든 이 segment 포함 시 skip).
EXEMPT_SEGMENTS = ("/raw/", "/_template/", "/_staging/", "/_archive/")
# textbook/md/ = PDF→markdown 변환 원본(vendor 텍스트 미러, OCR 포함). raw/ 등가.
EXEMPT_PREFIXES = ("_staging/", "_archive/", "textbook/md/")

# ---- G8b: 작성자 로컬 식별 절대경로 ----
# 공식 vendor / 표준 설치 경로 + 매뉴얼 generic placeholder — 비위반 (CONVENTIONS §4 허용 ②).
#   - Program Files / Windows : 표준 설치 위치
#   - Path\To / Path/To       : 매뉴얼이 사용자에게 치환하라고 적는 generic placeholder
VENDOR_PREFIX_RE = re.compile(r"(?i)^(?:program files(?: \(x86\))?|windows|path[\\/]to)\b")
# /opt, /usr 는 forbidden 패턴에 애초 포함 안 됨 (drive·/mnt·~ 만 검사).
LOCAL_PATH_PATTERNS = [
    ("win-drive", re.compile(r"(?<![A-Za-z0-9])([A-Za-z]):\\\\?")),  # D:\  D:\\  E:\
    ("wsl-mount", re.compile(r"/mnt/[a-z]/")),                       # /mnt/d/ /mnt/e/
    ("home", re.compile(r"(?<![\w.])~/")),                            # ~/rag ~/.venv
    ("wsl-unc", re.compile(r"\\\\wsl")),                             # \\wsl$ \\wsl.localhost
]

# ---- G8d: 개인사례 유도 placeholder ----
G8D_DIRECT_RE = re.compile(r"(?i)user[- ]experience cases")
G8D_MARKER = r"(?:▢|☐|- \[ \]|to be filled|lead modeler|from project memory|채워\s*넣|기입)"
G8D_CASE = r"(?:개인\s*사례|내\s*사례|경험\s*사례|project[- ]specific incident|project memory|run result|런\s*결과|실행\s*사례)"
G8D_INVITE_RE = re.compile(rf"(?i)(?:{G8D_MARKER}).{{0,80}}(?:{G8D_CASE})|(?:{G8D_CASE}).{{0,40}}(?:{G8D_MARKER})")

# ---- G8e: 작성자 작업환경 흔적 ----
# "local" 단독은 물리 용어(local wave height, local depth…)라 금지하지 않는다 — 작업환경을
# 가리키는 결합형만 등록.
G8E_RE = re.compile(
    r"(?i)\blocal path\s*:|\bthis workspace\b|\bcurrent(?:ly)? local\b|\blocally confirmed\b"
    r"|\blocal[- ]note\b|\blocal (?:machine|scripts?|runnable|calibration|experiments?|revalidation)\b"
    r"|(?:위키|writer)\s*머신"
)

FRONTMATTER_RE = re.compile(r"\A---\n.*?\n---", re.DOTALL)


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
        files.extend(str(p) for p in rp.rglob("*.md"))
    return files


def read_staged(path: str) -> str:
    out = run(["git", "show", f":{path}"])
    return out.stdout if out.returncode == 0 else ""


def read_disk(path: str) -> str:
    try:
        return Path(path).read_text(encoding="utf-8", errors="replace")
    except (FileNotFoundError, IsADirectoryError):
        return ""


# 거버넌스/인덱스/정책 문서 (CONVENTIONS §2.1) — canonical 노트 아님. 단일 writer 의
# 운영 경로·레지스트리·변환 커맨드를 담을 수 있어 G8b 비대상.
EXEMPT_BASENAMES = ("POLICY.md", "INDEX.md")


def is_exempt(path: str) -> bool:
    p = "/" + path  # segment match 가 path 시작도 잡도록
    if any(seg in p for seg in EXEMPT_SEGMENTS):
        return True
    if any(path.startswith(pre) for pre in EXEMPT_PREFIXES):
        return True
    return os.path.basename(path) in EXEMPT_BASENAMES


def under(path: str, roots: tuple[str, ...]) -> bool:
    return any(path == r or path.startswith(r + "/") for r in roots)


def find_local_paths(content: str) -> list[tuple[int, str, str]]:
    """(lineno, kind, snippet) 리스트. vendor 경로는 제외."""
    hits: list[tuple[int, str, str]] = []
    for i, line in enumerate(content.splitlines(), 1):
        for kind, pat in LOCAL_PATH_PATTERNS:
            for m in pat.finditer(line):
                if kind == "win-drive":
                    tail = line[m.end():]
                    if VENDOR_PREFIX_RE.match(tail):
                        continue  # C:\Program Files\… 등 vendor — 허용
                snippet = line.strip()
                if len(snippet) > 120:
                    snippet = snippet[:117] + "…"
                hits.append((i, kind, snippet))
                break  # 한 줄에 한 번만 보고
    return hits


def find_placeholders(content: str) -> list[tuple[int, str]]:
    hits: list[tuple[int, str]] = []
    for i, line in enumerate(content.splitlines(), 1):
        if G8D_DIRECT_RE.search(line) or G8D_INVITE_RE.search(line):
            snippet = line.strip()
            if len(snippet) > 120:
                snippet = snippet[:117] + "…"
            hits.append((i, snippet))
    return hits


def find_footprints(content: str) -> list[tuple[int, str]]:
    hits: list[tuple[int, str]] = []
    for i, line in enumerate(content.splitlines(), 1):
        if G8E_RE.search(line):
            snippet = line.strip()
            if len(snippet) > 120:
                snippet = snippet[:117] + "…"
            hits.append((i, snippet))
    return hits


HUNK_RE = re.compile(r"^@@ -\d+(?:,\d+)? \+(\d+)(?:,(\d+))? @@")


def staged_added_lines(path: str) -> set[int]:
    """staged diff 에서 새로 추가된 줄 번호(새 파일 기준)."""
    out = run(["git", "diff", "--cached", "-U0", "--no-color", "--", path])
    added: set[int] = set()
    for line in out.stdout.splitlines():
        m = HUNK_RE.match(line)
        if m:
            start, count = int(m.group(1)), int(m.group(2) or "1")
            added.update(range(start, start + count))
    return added


def main() -> int:
    staged = "--staged" in sys.argv[1:]
    mode_label = "staged" if staged else "working-tree"
    reader = read_staged if staged else read_disk

    if staged:
        all_files = [f for f in staged_files() if f.endswith(".md")]
        g8b_files = [f for f in all_files if under(f, CANONICAL_ROOTS) and not is_exempt(f)]
        g8d_files = [f for f in all_files if under(f, PLACEHOLDER_ROOTS) and not is_exempt(f)]
    else:
        g8b_files = [f for f in tree_files(CANONICAL_ROOTS) if not is_exempt(f)]
        g8d_files = [f for f in tree_files(PLACEHOLDER_ROOTS) if not is_exempt(f)]

    # 검사 1 — G8b 경로
    print(f"[1/3] G8b 작성자 로컬 절대경로 검사 (mode: {mode_label})…")
    path_violations: list[tuple[str, int, str, str]] = []
    for f in g8b_files:
        content = reader(f)
        if not content:
            continue
        for lineno, kind, snip in find_local_paths(content):
            path_violations.append((f, lineno, kind, snip))

    if path_violations:
        print("  FAIL: canonical 콘텐츠에 작성자 로컬 절대경로:")
        for f, ln, kind, snip in path_violations:
            print(f"    {f}:{ln} [{kind}] {snip}")
        print("  → source_id / repo-상대 file:line / placeholder 로 교체 (CONVENTIONS §4, G8b).")
    else:
        print("  OK: 작성자 로컬 절대경로 없음.")

    # 검사 2 — G8d placeholder
    print("[2/3] G8d 개인사례 유도 placeholder 검사…")
    ph_violations: list[tuple[str, int, str]] = []
    for f in g8d_files:
        content = reader(f)
        if not content:
            continue
        for lineno, snip in find_placeholders(content):
            ph_violations.append((f, lineno, snip))

    if ph_violations:
        print("  FAIL: canonical 노트에 개인사례 유도 placeholder:")
        for f, ln, snip in ph_violations:
            print(f"    {f}:{ln} {snip}")
        print("  → 개인 사례는 experience/. canonical 엔 두지 않음 (CONVENTIONS §6, G8d).")
    else:
        print("  OK: 개인사례 placeholder 없음.")

    # 검사 3 — G8e 작업환경 흔적 (staged: 추가된 줄만 차단 / tree: 잔존분 WARN)
    print("[3/3] G8e 작성자 작업환경 흔적 검사…")
    fp_hits: list[tuple[str, int, str]] = []
    for f in g8d_files:
        content = reader(f)
        if not content:
            continue
        hits = find_footprints(content)
        if staged and hits:
            added = staged_added_lines(f)
            hits = [h for h in hits if h[0] in added]
        fp_hits.extend((f, ln, snip) for ln, snip in hits)

    if fp_hits and staged:
        print("  FAIL: 이번 커밋이 canonical 노트에 작업환경 흔적을 추가:")
    elif fp_hits:
        print(f"  WARN: canonical 노트에 기존 작업환경 흔적 {len(fp_hits)}줄 (비실패 — 정화 대상):")
    for f, ln, snip in fp_hits:
        print(f"    {f}:{ln} {snip}")
    if fp_hits:
        print("  → 공식 출처 표기로 중립화하거나 개인 운영 기록은 experience/·coastal-runs 로 (CONVENTIONS §4·§6, G8e).")
    else:
        print("  OK: 작업환경 흔적 없음.")

    labels = []
    code = 0
    if path_violations:
        code |= 1; labels.append("G8b 경로")
    if ph_violations:
        code |= 2; labels.append("G8d placeholder")
    if staged and fp_hits:
        code |= 4; labels.append("G8e 작업환경 흔적")
    print()
    print(f"RESULT: FAIL ({' + '.join(labels)})" if code else "RESULT: OK")
    return code


if __name__ == "__main__":
    sys.exit(main())
