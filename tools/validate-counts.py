#!/usr/bin/env python3
"""validate-counts.py — 계수 단언(파일 수·배열 크기) 실측 대조 lint (2026-09-22).

배경: 같은 결함이 세 번 반복됐다 — **하위 집합 계수를 총계로 라벨링**.
  SWAN  `swan-source-coverage-audit.md`  "58 source files"  → 실제는 `.ftn90` 수, 총 소스는 75
  ROMS  `roms_tangent_linear_model.md`   "54개 `.F`/`.h`"    → `.F` 54 + `.h` 18 = 72
  LISFLOOD `lisflood-fp-io-boundary.md`  "`H`, `Qx/Qy`는 (xsz+1)×(ysz+1)" → `H` 는 xsz×ysz
세 건 모두 **세어 보면 즉시 드러난다**. 그래서 '세었다는 사실' 을 기계가 재현하게 만든다.
또한 계수는 스냅샷 교체로 조용히 낡는다(SWAN 58 은 구 pinned 시점 값이었다).

검사 2종:

  C1. **선언된 계수는 실측과 일치해야 한다** (결정적, 위반 = 실패)
      노트에 아래 지시자를 두면 glob 을 다시 세어 대조한다.

          <!-- count: models/SWAN/raw/source_code/swan/src/*.ftn90 = 57 -->

      glob 은 repo 루트 기준. `**` 재귀 허용. 디렉터리는 세지 않는다(파일만).

  C2. **위험 패턴은 지시자를 동반해야 한다** (위반 = 실패)
      아래 형태의 계수 단언이 있는 노트는 C1 지시자를 **하나 이상** 가져야 한다.
        · 숫자 + 확장자 2개 이상 나열   예) "54개 `.F`/`.h`"
        · 숫자 + source file(s)/소스 파일  예) "58 source files"
      두 형태 모두 '무엇을 셌는지' 가 문장에서 불분명해 총계로 오독되기 쉽다.
      지시자를 달면 무엇을 셌는지가 glob 으로 고정되고 재현된다.

  --staged: staged 버전 기준, staged 된 .md 만 검사 (pre-commit 용)

대상: concepts/ · models/ · textbook/ 의 .md (raw/·_archive/ 제외).
exit: 0 OK / 1 위반 / 2 사용법 오류
"""
import glob as globmod
import os
import re
import subprocess
import sys

ROOT = subprocess.check_output(
    ["git", "rev-parse", "--show-toplevel"], text=True
).strip()

SCOPE = ("concepts", "models", "textbook")
SKIP_PARTS = ("raw", "_archive", "_staging")

DIRECTIVE = re.compile(r"<!--\s*count:\s*(?P<glob>[^=]+?)\s*=\s*(?P<n>\d+)\s*-->")
# 숫자 + 확장자 2개 이상 (`.F`/`.h`, .f90·.F90 …)
RISK_EXT2 = re.compile(
    r"(\d[\d,]*)\s*(?:개|files?|개의)?\s*[`*]?\.(\w+)[`*]?\s*[/·]\s*[`*]?\.(\w+)")
# 숫자 + source file(s) / 소스 파일.
# `§2 source file map` 처럼 절 번호가 앞에 오는 경우는 계수 단언이 아니다.
RISK_SRC = re.compile(r"(?<![§#.\d])(\d[\d,]*)\s*(?:source files?|소스 ?파일)")
# (C2 는 파일 범위로 판정한다 — 아래 check() 주석 참조)


def in_scope(rel):
    parts = rel.split("/")
    return parts[0] in SCOPE and not any(p in SKIP_PARTS for p in parts)


def staged_files():
    out = subprocess.check_output(
        ["git", "diff", "--cached", "--name-only", "--diff-filter=ACM"], text=True)
    return [f for f in out.splitlines() if f.endswith(".md") and in_scope(f)]


def all_files():
    out = []
    for s in SCOPE:
        base = os.path.join(ROOT, s)
        for dirpath, dirnames, filenames in os.walk(base):
            dirnames[:] = [d for d in dirnames if d not in SKIP_PARTS]
            for fn in filenames:
                if fn.endswith(".md"):
                    out.append(os.path.relpath(os.path.join(dirpath, fn), ROOT))
    return sorted(out)


def read(rel, staged):
    if staged:
        try:
            return subprocess.check_output(
                ["git", "show", f":{rel}"], text=True, errors="replace")
        except subprocess.CalledProcessError:
            return ""
    with open(os.path.join(ROOT, rel), errors="replace") as f:
        return f.read()


def count_glob(pattern):
    """repo 루트 기준 glob 의 **파일** 수. 반환 (n, 오류메시지|None)."""
    if pattern.startswith("/") or ".." in pattern.split("/"):
        return None, "glob 은 repo 루트 기준 상대경로여야 한다"
    hits = globmod.glob(os.path.join(ROOT, pattern), recursive=True)
    files = [h for h in hits if os.path.isfile(h)]
    if not files:
        return 0, None
    return len(files), None


def check(rel, text):
    fails = []
    lines = text.splitlines()
    dirs = {}  # lineno -> (glob, n)
    for i, l in enumerate(lines, 1):
        m = DIRECTIVE.search(l)
        if m:
            dirs[i] = (m.group("glob"), int(m.group("n")))

    # C1
    for ln, (pat, want) in dirs.items():
        got, err = count_glob(pat)
        if err:
            fails.append(f"{rel}:{ln} count 지시자 오류 — {err}: {pat}")
        elif got != want:
            fails.append(
                f"{rel}:{ln} 계수 불일치 — `{pat}` 선언 {want} vs 실측 {got}")

    # frontmatter 범위 — 지시자를 둘 수 없으므로 C2 대상에서 뺀다.
    # (frontmatter 의 계수는 본문 단언의 요약이고, 본문 쪽이 지시자로 검사된다)
    fm_end = 0
    if lines[:1] == ["---"]:
        for j, l in enumerate(lines[1:], 2):
            if l.strip() == "---":
                fm_end = j
                break

    # C2
    for i, l in enumerate(lines, 1):
        if i <= fm_end:
            continue
        s = l.strip()
        if s.startswith("<!--") or s.startswith("#"):
            continue
        hit = None
        if RISK_EXT2.search(l):
            hit = "숫자+확장자 2종 나열"
        elif RISK_SRC.search(l):
            hit = "숫자+source files"
        if not hit:
            continue
        # 파일 범위로 판정한다. 지시자는 C1 이 실측 대조하므로, 같은 노트 안에
        # 검사된 지시자가 하나라도 있으면 그 노트의 계수는 기계가 재현한다.
        # (줄 거리로 요구하면 같은 지시자를 한 파일에 여러 번 붙이게 되어 잡음이다)
        if dirs:
            continue
        fails.append(
            f"{rel}:{i} 계수 단언에 count 지시자가 없다 ({hit}) — "
            f"이 노트 어딘가에 `<!-- count: <glob> = <N> -->` 를 두어라\n"
            f"    {s[:110]}")
    return fails


def main(argv):
    staged = "--staged" in argv[1:]
    if [a for a in argv[1:] if a != "--staged"]:
        print(__doc__)
        return 2
    files = staged_files() if staged else all_files()
    fails = []
    for rel in files:
        t = read(rel, staged)
        if t:
            fails += check(rel, t)
    mode = "staged" if staged else "working tree"
    print(f"[counts] 대상 {len(files)}개 검사 (mode: {mode})…")
    if fails:
        print(f"[counts] 위반 {len(fails)}건:")
        for f in fails:
            print("  ✗", f)
        return 1
    print("[counts] OK: 계수 단언 실측 대조 통과.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
