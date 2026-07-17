#!/usr/bin/env python3
"""validate-claims.py — theory 노트 단언 집계 산술·manifest 대조 lint (plan.md R1 I-1, 2026-07-17).

배경: 게이트 18·19회차 연속 지표 산술 불일치 → Codex 20회차 설계 반영.
  Tier-0(산술)만 여기서 검사 — 단언 분류의 *의미* 타당성은 L4 감사 축(F-8 분리).

검사 (대상 = textbook/notes/theory-*.md):
  1. 집계 4필드 실존 + 비음수 정수: claims_total/claims_attached/claims_dropped/claims_source_needed
  2. 산술: total == attached + dropped + source_needed
  3. 정합: (claims_source_needed > 0) == (has_source_needed == true)
  4. claims_basis ∈ {legacy-ledger, claim-manifest}. claim-manifest 인 노트는
     textbook/notes/claims/<stem>-claims.yml 실존 + disposition 별 카운트가 frontmatter 와 일치.
     (불일치 = 실패 — 'frontmatter 우선' 규칙 없음, 드리프트는 발견 즉시 실패)
  5. --staged: staged 버전 기준, staged 된 theory-* 파일만 검사 (pre-commit 용)

exit: 0 OK / 1 위반 / 2 사용법 오류
"""
import os
import re
import subprocess
import sys

ROOT = subprocess.check_output(
    ["git", "rev-parse", "--show-toplevel"], text=True
).strip()

FIELDS = ("claims_total", "claims_attached", "claims_dropped", "claims_source_needed")
BASES = ("legacy-ledger", "claim-manifest")


def frontmatter(text):
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    return m.group(1) if m else ""


def parse_fields(fm):
    """frontmatter 문자열 → dict (집계 4필드 int, basis, has_source_needed bool|None)."""
    out = {}
    for f in FIELDS:
        m = re.search(rf"(?m)^{f}:\s*(-?\d+)\s*$", fm)
        out[f] = int(m.group(1)) if m else None
    m = re.search(r"(?m)^claims_basis:\s*(\S+)\s*$", fm)
    out["claims_basis"] = m.group(1) if m else None
    m = re.search(r"(?m)^has_source_needed:\s*(true|false)\s*$", fm)
    out["has_source_needed"] = (m.group(1) == "true") if m else None
    return out


def manifest_counts(path):
    """claim manifest(yml) 의 disposition 별 카운트. 순수 stdlib — 라인 스캔."""
    counts = {"attached": 0, "dropped": 0, "source-needed": 0}
    ids = []
    for line in open(path, encoding="utf-8"):
        if line.lstrip().startswith("#"):
            continue
        m = re.search(r"disposition:\s*([a-z-]+)", line)
        if m:
            d = m.group(1)
            if d not in counts:
                return None, f"알 수 없는 disposition '{d}'"
            counts[d] += 1
        mi = re.search(r"\{id:\s*([A-Za-z0-9_-]+)", line)
        if mi:
            ids.append(mi.group(1))
    if len(ids) != len(set(ids)):
        dup = sorted({i for i in ids if ids.count(i) > 1})
        return None, f"중복 claim id: {', '.join(dup)}"
    return counts, None


def check_note(relpath, text, errors):
    fm = frontmatter(text)
    if not fm:
        errors.append(f"{relpath}: frontmatter 미발견")
        return
    f = parse_fields(fm)
    missing = [k for k in FIELDS if f[k] is None]
    if missing:
        errors.append(f"{relpath}: 집계 필드 누락 — {', '.join(missing)}")
        return
    neg = [k for k in FIELDS if f[k] < 0]
    if neg:
        errors.append(f"{relpath}: 음수 집계 — {', '.join(neg)}")
        return
    t, a, d, s = (f[k] for k in FIELDS)
    if t != a + d + s:
        errors.append(f"{relpath}: 산술 불일치 — total {t} != {a}+{d}+{s} = {a+d+s}")
    hsn = f["has_source_needed"] or False
    if (s > 0) != hsn:
        errors.append(
            f"{relpath}: 정합 위반 — claims_source_needed={s} 인데 has_source_needed={hsn}"
        )
    basis = f["claims_basis"]
    if basis not in BASES:
        errors.append(f"{relpath}: claims_basis 누락/무효 ('{basis}') — {BASES} 중 하나")
        return
    if basis == "claim-manifest":
        stem = os.path.splitext(os.path.basename(relpath))[0]
        mpath = os.path.join(ROOT, "textbook/notes/claims", f"{stem}-claims.yml")
        if not os.path.isfile(mpath):
            errors.append(f"{relpath}: claim manifest 미실존 — {os.path.relpath(mpath, ROOT)}")
            return
        counts, err = manifest_counts(mpath)
        if err:
            errors.append(f"{relpath}: manifest 파싱 실패 — {err}")
            return
        expect = {"attached": a, "dropped": d, "source-needed": s}
        for k, v in expect.items():
            if counts[k] != v:
                errors.append(
                    f"{relpath}: manifest 불일치 — {k}: manifest {counts[k]} vs frontmatter {v}"
                )


def main(argv):
    staged = "--staged" in argv
    errors = []
    if staged:
        out = subprocess.check_output(
            ["git", "diff", "--cached", "--name-only", "--diff-filter=ACM"],
            text=True, cwd=ROOT,
        )
        targets = [p for p in out.splitlines()
                   if re.fullmatch(r"textbook/notes/theory-[^/]+\.md", p)]
        for rel in targets:
            try:
                text = subprocess.check_output(
                    ["git", "show", f":{rel}"], text=True, cwd=ROOT)
            except subprocess.CalledProcessError:
                continue
            check_note(rel, text, errors)
    else:
        base = os.path.join(ROOT, "textbook/notes")
        targets = sorted(
            f for f in os.listdir(base)
            if f.startswith("theory-") and f.endswith(".md"))
        for fn in targets:
            rel = f"textbook/notes/{fn}"
            check_note(rel, open(os.path.join(base, fn), encoding="utf-8").read(), errors)
    mode = "staged" if staged else "full"
    if errors:
        print(f"[claims] 위반 {len(errors)}건 (mode: {mode}):")
        for e in errors:
            print(f"  ✗ {e}")
        return 1
    print(f"[claims] OK: theory 노트 {len(targets)}건 집계 산술·manifest 대조 통과 (mode: {mode}).")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
