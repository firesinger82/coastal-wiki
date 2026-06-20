#!/usr/bin/env python3
"""validate-link-integrity.py — coastal-wiki 내부 링크 무결성 검사.

정책 근거: 2026-06-18 health 스캔 (깨진 내부 링크 ~20건 발견·정리) 후 회귀 방지.

검사 (authored 레이어 = concepts/·models/·textbook/notes/·experience/·examples/):
  (a) 상대 `.md` 링크 `](path.md)` 가 실제 파일로 resolve 되는지
  (b) `[[wikilink]]` 의 타겟(basename 또는 path 의 basename)이 실존 노트 stem 인지

스킵(의도된 것·비대상):
  - fenced code block + inline code (코드 속 `[[i]]`·`coef[["aux"]]` false positive)
  - glob shorthand (`[[swan-*-implementation]]` 등 `*` 포함)
  - 외부 URL (http/https/mailto/file …)
  - **의도된 forward-ref**: 같은 줄에 `(예정)`·`미생성`·`planned`·`TBD`·`TBA` 마커가 있으면
    아직 안 만든 노트로의 링크라 통과 (wiki 의 '미생성 섹션 추적' 컨벤션, CONVENTIONS §8).
  - textbook/md/**(PDF→md 변환 OCR 미러)·raw/·_archive/·_staging/·_template/

도구 범위: research-isolation·canonical-hygiene 와 동일한 conservative scanner.
Obsidian basename-resolution(전역 basename 매칭) + path-wikilink 둘 다 인정.

사용:
  python3 tools/validate-link-integrity.py            # working tree
  python3 tools/validate-link-integrity.py --staged   # staged snapshot

Exit codes:
  0 = OK
  1 = 깨진 상대 .md 링크
  2 = 깨진 [[wikilink]]
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

AUTHORED_ROOTS = ("concepts", "models", "textbook/notes", "experience", "examples")
EXCLUDE_SEG = ("/raw/", "/_archive/", "/_staging/", "/_template/")
# textbook/md = 변환 OCR 미러 (링크 타겟은 되지만, 그 안의 [[i]] 류는 검사 비대상)
SCAN_EXCLUDE_PREFIX = ("textbook/md/",)

CODE_BLOCK = re.compile(r"```.*?```", re.DOTALL)
INLINE_CODE = re.compile(r"`[^`\n]+`")
WIKI = re.compile(r"\[\[([^\]\|#]+)(?:[#\|][^\]]*)?\]\]")
MDLINK = re.compile(r"\]\(([^)\s]+\.md)(?:#[^)]*)?\)")
URL = re.compile(r"^[a-zA-Z][a-zA-Z0-9+.\-]*:")
INTENT_MARKER = re.compile(r"\(?\s*(?:예정|미생성|planned|TBD|TBA|작성\s*대기)\s*\)?", re.IGNORECASE)


def run(cmd: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(cmd, capture_output=True, text=True, check=False)


def all_note_stems() -> set[str]:
    """repo 전역 .md stem (raw/_archive/_staging/.git 제외). wikilink basename 해석용."""
    stems: set[str] = set()
    for p in WIKI_ROOT.rglob("*.md"):
        s = str(p.relative_to(WIKI_ROOT))
        if any(seg.strip("/") in s.split("/") for seg in (".git",)):
            continue
        if any(x in "/" + s for x in EXCLUDE_SEG):
            continue
        stems.add(p.stem)
    return stems


def tree_files() -> list[str]:
    files: list[str] = []
    for root in AUTHORED_ROOTS:
        rp = Path(root)
        if rp.is_dir():
            files += [str(p) for p in rp.rglob("*.md")]
    return files


def staged_md() -> list[str]:
    out = run(["git", "diff", "--cached", "-z", "--name-only", "--diff-filter=ACMR"])
    if out.returncode != 0:
        print(f"ERROR: git diff 실패: {out.stderr}", file=sys.stderr)
        sys.exit(10)
    return [p for p in out.stdout.split("\0") if p.endswith(".md")]


def under_authored(path: str) -> bool:
    return any(path == r or path.startswith(r + "/") for r in AUTHORED_ROOTS)


def scan_exempt(path: str) -> bool:
    if any(x in "/" + path for x in EXCLUDE_SEG):
        return True
    return any(path.startswith(p) for p in SCAN_EXCLUDE_PREFIX)


def read_staged(path: str) -> str:
    out = run(["git", "show", f":{path}"])
    return out.stdout if out.returncode == 0 else ""


def read_disk(path: str) -> str:
    try:
        return Path(path).read_text(encoding="utf-8", errors="replace")
    except (FileNotFoundError, IsADirectoryError):
        return ""


def check_file(path: str, content: str, stems: set[str]
               ) -> tuple[list[tuple[int, str]], list[tuple[int, str]]]:
    """(broken_mdlinks, broken_wikilinks) — 각 (lineno, target)."""
    broken_md: list[tuple[int, str]] = []
    broken_wiki: list[tuple[int, str]] = []
    file_dir = os.path.dirname(path) or "."
    for i, raw_line in enumerate(content.splitlines(), 1):
        # 줄 단위로 inline code 제거 (코드 false positive 차단)
        line = INLINE_CODE.sub("", raw_line)
        intentional = bool(INTENT_MARKER.search(raw_line))

        for m in MDLINK.finditer(line):
            tgt = m.group(1)
            if URL.match(tgt):
                continue
            resolved = (os.path.normpath(tgt.lstrip("/")) if tgt.startswith("/")
                        else os.path.normpath(os.path.join(file_dir, tgt)))
            if not Path(resolved).exists() and not intentional:
                broken_md.append((i, tgt))

        for m in WIKI.finditer(line):
            name = m.group(1).strip()
            if "*" in name:           # glob shorthand
                continue
            stem = name.split("/")[-1].split(".")[0]  # path·.md 형태 → stem
            if not stem:
                continue
            if stem not in stems and not intentional:
                broken_wiki.append((i, name))
    return broken_md, broken_wiki


def main() -> int:
    staged = "--staged" in sys.argv[1:]
    mode = "staged" if staged else "working-tree"
    reader = read_staged if staged else read_disk
    stems = all_note_stems()

    if staged:
        files = [f for f in staged_md() if under_authored(f) and not scan_exempt(f)]
    else:
        files = [f for f in tree_files() if not scan_exempt(f)]

    print(f"[1/2] 상대 .md 링크 resolve 검사 (mode: {mode})…")
    md_v: list[tuple[str, int, str]] = []
    wiki_v: list[tuple[str, int, str]] = []
    for f in files:
        content = reader(f)
        if not content:
            continue
        bm, bw = check_file(f, CODE_BLOCK.sub("", content), stems)
        md_v += [(f, ln, t) for ln, t in bm]
        wiki_v += [(f, ln, t) for ln, t in bw]

    if md_v:
        print("  FAIL: 깨진 상대 .md 링크:")
        for f, ln, t in md_v:
            print(f"    {f}:{ln} -> {t}")
        print("  → 경로/이름 수정, 또는 미생성이면 같은 줄에 '(예정)' 표기.")
    else:
        print("  OK: 깨진 상대 .md 링크 없음.")

    print("[2/2] [[wikilink]] 타겟 resolve 검사…")
    if wiki_v:
        print("  FAIL: 깨진 [[wikilink]] (실존 노트 stem 아님):")
        for f, ln, t in wiki_v:
            print(f"    {f}:{ln} [[{t}]]")
        print("  → 실존 노트명으로 수정, glob 은 비링크화, 미생성이면 '(예정)' 표기.")
    else:
        print("  OK: 깨진 wikilink 없음.")

    fb, fw = bool(md_v), bool(wiki_v)
    print()
    if fb and fw:
        print("RESULT: FAIL (상대링크 + wikilink)")
        return 3
    if fb:
        print("RESULT: FAIL (상대 .md 링크)")
        return 1
    if fw:
        print("RESULT: FAIL (wikilink)")
        return 2
    print("RESULT: OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
