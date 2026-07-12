#!/usr/bin/env python3
"""validate-layer-deps.py — 4-레이어 근거 의존성 방향 검사 (CONVENTIONS §8.1, plan.md 4-레이어 v2).

정책 (Codex 2회차 검토 #6 반영):
  - 검사 대상 = frontmatter 에 `layer:` 필드를 가진 파일만 (신규 레이어 파일 opt-in).
    기존 verified 파일은 소급 적용·검사 대상에서 제외.
  - 근거 의존성(`depends_on:`)은 하위 레이어로만: ④(4)→③(3)→②(2)→①(1).
    depends_on 대상의 레이어가 자신보다 크면 위반. 탐색용 본문 링크는 검사하지 않음.
  - experience/ 를 depends_on 으로 갖는 것은 layer 4 만 허용 (커밋고정 링크 소비).
  - scope guard: layer 파일과 기존 verified 파일(=layer 없음 + citation_status: verified)의
    본문 변경이 한 커밋에 섞이면 실패 (오염 방지 — 커밋 분리).
    escape: COASTAL_WIKI_SKIP_LAYER_GUARD=1

exit: 0 OK / 1 위반 / 2 사용법 오류
"""
import os
import re
import subprocess
import sys

ROOT = subprocess.check_output(
    ["git", "rev-parse", "--show-toplevel"], text=True
).strip()


def staged_files(filters):
    out = subprocess.check_output(
        ["git", "diff", "--cached", "--name-only", f"--diff-filter={filters}"],
        text=True, cwd=ROOT,
    )
    return [p for p in out.splitlines() if p.endswith(".md")]


def read_content(path, staged):
    if staged:
        try:
            return subprocess.check_output(
                ["git", "show", f":{path}"], text=True, cwd=ROOT,
                stderr=subprocess.DEVNULL,
            )
        except subprocess.CalledProcessError:
            return None
    full = os.path.join(ROOT, path)
    if not os.path.isfile(full):
        return None
    with open(full, encoding="utf-8", errors="replace") as f:
        return f.read()


def parse_frontmatter(text):
    """단순 파서: layer(int), depends_on(list[str]), citation_status(str)."""
    fm = {"layer": None, "depends_on": [], "citation_status": None}
    if not text or not text.startswith("---"):
        return fm
    end = text.find("\n---", 3)
    if end < 0:
        return fm
    block = text[:end]
    m = re.search(r"^layer:\s*([1-4])\s*$", block, re.M)
    if m:
        fm["layer"] = int(m.group(1))
    m = re.search(r"^citation_status:\s*([\w-]+)", block, re.M)
    if m:
        fm["citation_status"] = m.group(1)
    dep = re.search(r"^depends_on:\s*\n((?:\s+-\s+.*\n?)*)", block, re.M)
    if dep:
        fm["depends_on"] = re.findall(r"-\s+([^\s#]+)", dep.group(1))
    return fm


def infer_layer(path, staged):
    """대상 파일 레이어: frontmatter 우선, 없으면 경로 휴리스틱. None=판정 불가(스킵)."""
    text = read_content(path, staged) or read_content(path, False)
    if text:
        fm = parse_frontmatter(text)
        if fm["layer"]:
            return fm["layer"]
    if re.match(r"textbook/notes/theory-", path):
        return 1
    if path.startswith("models/"):
        return 2
    if path.startswith("examples/"):
        return 3
    if re.match(r"concepts/[^/]+/\d+-applied-", path):
        return 4
    if path.startswith("experience/"):
        return "experience"
    return None  # concepts 일반·textbook 일반 등 — 비배타적 논리 역할, 자동 판정 안 함


def main():
    staged = "--staged" in sys.argv
    violations = []

    if staged:
        candidates = staged_files("ACMR")
    else:
        try:
            out = subprocess.check_output(
                ["git", "grep", "-l", "^layer:", "--", "*.md"],
                text=True, cwd=ROOT,
            )
        except subprocess.CalledProcessError:
            out = ""  # 매치 없음
        candidates = out.splitlines()

    layered = []
    for path in candidates:
        text = read_content(path, staged)
        if text is None:
            continue
        fm = parse_frontmatter(text)
        if fm["layer"] is None:
            continue
        layered.append(path)
        own = fm["layer"]
        for dep in fm["depends_on"]:
            dep_norm = dep.strip().lstrip("./")
            tgt = infer_layer(dep_norm, staged)
            if tgt == "experience":
                if own != 4:
                    violations.append(
                        f"{path} (layer {own}) → {dep_norm}: experience 근거 의존은 layer 4 만 허용"
                    )
                continue
            if tgt is None:
                continue  # 판정 불가 — 논리 분류라 자동 검사 스킵
            if tgt > own:
                violations.append(
                    f"{path} (layer {own}) → {dep_norm} (layer {tgt}): 근거 의존이 상위 레이어를 향함 (④→③→②→① 위반)"
                )

    # scope guard (staged 모드만): layer 커밋 + 기존 verified 본문 변경 혼합 금지
    if staged and layered and os.environ.get("COASTAL_WIKI_SKIP_LAYER_GUARD") != "1":
        for path in staged_files("M"):
            if path in layered:
                continue
            text = read_content(path, True)
            if text is None:
                continue
            fm = parse_frontmatter(text)
            if fm["layer"] is None and fm["citation_status"] == "verified":
                violations.append(
                    f"scope guard: 레이어 파일 커밋에 기존 verified 파일 변경 혼입 — {path} "
                    f"(커밋 분리 필요; 의도적이면 COASTAL_WIKI_SKIP_LAYER_GUARD=1)"
                )

    mode = "staged" if staged else "full"
    if violations:
        print(f"[layer-deps] 위반 {len(violations)}건 (mode: {mode}):")
        for v in violations:
            print(f"  ✗ {v}")
        return 1
    n = len(layered)
    print(f"[layer-deps] OK: layer 파일 {n}건 검사, 근거 의존 방향 위반 없음 (mode: {mode}).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
