#!/usr/bin/env python3
"""experience 참조 블록의 정량값 복제 검사 (CONVENTIONS §8.1).

의미·출처의 진위는 판정하지 않고, experience 링크와 정량 토큰의 구조적
동시 출현만 검사한다. 기본은 warn, --strict 는 경고를 실패로 승격한다.
"""
from __future__ import annotations

import os
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TARGET_DIRS = ("concepts/", "models/", "textbook/")
PATH_REF = re.compile(r"(?:\.\./)*experience/([A-Za-z0-9_.-]+\.md)(?:[#@][^\s)]+)?")
WIKI_REF = re.compile(r"\[\[([^]|#]+)(?:#[^]|]+)?(?:\|[^]]+)?\]\]")
NUMBER = re.compile(
    r"(?<![\w.])(?:[+-]?\d+(?:\.\d+)?(?:\s*[–—-]\s*\d+(?:\.\d+)?)?\s*(?:mm/yr|cm/yr|m/s|cm/s|mm|cm|km|m|°C|℃|%|mb|hPa|σ|/decade|/yr|/dec)|"
    r"\d+(?:\.\d+)?\s*[×x배]|(?:R²|R\^2)\s*[=:]?\s*\d+(?:\.\d+)?|"
    r"\d+\s*중일치|\d+[- ]dataset|\d+(?:\.\d+)?\s*배|\d+(?:\.\d+)?\s*[–—-]\s*\d+(?:\.\d+)?(?:\s*비|\s*ratio)?)",
    re.I,
)
UNIT = r"(?:mm/yr|cm/yr|m/s|cm/s|mm|cm|km|m|°C|℃|%|mb|hPa|σ|/decade|/yr|/dec)(?![A-Za-z])"
YEAR = re.compile(r"^\d{4}(?:-\d{2}(?:-\d{2})?)?(?:-\d{4})?$")
INLINE = re.compile(r"`[^`]*`")


@dataclass
class Block:
    start: int
    lines: list[str]
    kind: str
    refs: set[str]
    units: list[str] | None = None


def git(args: list[str]) -> str:
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True)


def staged_paths() -> list[str]:
    return [p for p in git(["diff", "--cached", "--name-only", "--diff-filter=ACMR"]).splitlines()
            if p.endswith(".md") and p.startswith(TARGET_DIRS)]


def read(path: str, staged: bool) -> str | None:
    if staged:
        try:
            return git(["show", f":{path}"])
        except subprocess.CalledProcessError:
            return None
    p = ROOT / path
    return p.read_text(encoding="utf-8", errors="replace") if p.is_file() else None


def experience_names(staged: bool) -> set[str]:
    if staged:
        names = git(["ls-files", "--cached", "experience/*.md"]).splitlines()
    else:
        names = [str(p.relative_to(ROOT)) for p in (ROOT / "experience").glob("*.md")]
    return {Path(p).stem for p in names}


def frontmatter(text: str) -> tuple[str, int, int | None]:
    if not text.startswith("---"):
        return text, 0, None
    end = text.find("\n---", 3)
    if end < 0:
        return text, 0, None
    stop = end + 4
    fm = text[:stop]
    m = re.search(r"^layer:\s*([1-4])\s*$", fm, re.M)
    return text[stop:], stop, int(m.group(1)) if m else None


def refs_in(text: str, names: set[str]) -> set[str]:
    found = {Path(m.group(1)).stem for m in PATH_REF.finditer(text) if Path(m.group(1)).stem in names}
    for m in WIKI_REF.finditer(text):
        name = Path(m.group(1).strip()).stem
        # [[README]] 는 현재 노트의 로컬 README 우선(경험 README로 추정하지 않음).
        if name in names and name != "README":
            found.add(name)
    return found


SOURCE_MARK = re.compile(r"검증|확인|근거|출처|전체 분석|@\s*`?[0-9a-f]{7,40}`?")


def _is_table(line: str) -> bool:
    return line.lstrip().startswith("|") and line.count("|") >= 2


def _is_list(line: str) -> bool:
    return bool(re.match(r"^\s*(?:[-*+] |\d+[.)] )", line))


def blocks(body: str, names: set[str]) -> list[Block]:
    lines = body.splitlines()
    out: list[Block] = []
    i = 0
    while i < len(lines):
        if not lines[i].strip() or lines[i].lstrip().startswith("```"):
            i += 1
            continue
        start = i
        if _is_table(lines[i]):
            table_start = i
            while i < len(lines) and _is_table(lines[i]):
                i += 1
            table = lines[table_start:i]
            header = table[0].split("|")[1:-1]
            units = [re.search(UNIT, x, re.I).group(0)
                     if re.search(UNIT, x, re.I) else ""
                     for x in header]
            for row_no, row in enumerate(table):
                if row_no == 1 and re.fullmatch(r"\s*\|?\s*:?-{2,}", row.replace("|", "").strip()):
                    continue
                out.append(Block(start + row_no, [row], "table", refs_in(row, names), units))
            continue
        elif _is_list(lines[i]):
            i += 1
            while i < len(lines) and lines[i].strip() and not _is_list(lines[i]) and not lines[i].startswith("#"):
                i += 1
            kind = "list"
        else:
            i += 1
            while i < len(lines) and lines[i].strip() and not _is_table(lines[i]) and not _is_list(lines[i]) and not lines[i].startswith("#"):
                i += 1
            kind = "paragraph"
        chunk = lines[start:i]
        out.append(Block(start + 1, chunk, kind, set().union(*(refs_in(x, names) for x in chunk))))

    # 도입부·명시 표지·표 직후의 출처 줄은 인접한 형제 블록에 귀속한다.
    for n, b in enumerate(out):
        if n and out[n - 1].kind == "paragraph" and out[n - 1].refs and b.kind in {"table", "list"}:
            # 도입 문단은 바로 이어지는 표/목록 전체에 귀속한다.
            j = n
            while j < len(out) and out[j].kind == b.kind:
                out[j].refs |= out[n - 1].refs
                j += 1
        if b.kind == "table":
            # 표 직후 출처 문단은 표의 모든 행에 귀속한다.
            j = n + 1
            while j < len(out) and out[j].kind == "table":
                j += 1
            if j < len(out):
                nxt = out[j]
                raw = " ".join(nxt.lines)
                if nxt.kind == "paragraph" and nxt.refs and ("전체 분석:" in raw or "experience/" in raw) and len(raw) < 160:
                    b.refs |= nxt.refs
        if b.kind == "list" and n + 1 < len(out) and out[n + 1].kind == "list":
            # 다음 형제 항목이 출처 줄이면 앞 항목을 포함한 목록에 귀속.
            # 출처 줄 = 검증 표지가 있고 "탐색용" 표지가 없는 항목 (DESIGN v2 #3, 오탐 2026-09-29 반영).
            nxt_raw = " ".join(out[n + 1].lines)
            if (out[n + 1].refs and not NUMBER.search(nxt_raw)
                    and SOURCE_MARK.search(nxt_raw) and "탐색용" not in nxt_raw):
                b.refs |= out[n + 1].refs
            if b.refs and NUMBER.search(" ".join(out[n + 1].lines)) and "같은 experience" in " ".join(out[n + 1].lines):
                out[n + 1].refs |= b.refs
        if b.kind == "paragraph" and n and out[n - 1].kind == "paragraph":
            raw = " ".join(out[n - 1].lines)
            if out[n - 1].refs and (raw.rstrip().endswith(":") or "결과:" in raw or "전체 분석" in raw):
                b.refs |= out[n - 1].refs
    return out


def strip_exclusions(text: str) -> str:
    # 참조는 제거 전에 추출하지만 수치 판정에서는 인라인 코드·주석을 제외한다.
    text = INLINE.sub("", text)
    text = re.sub(r"<!--.*?-->", "", text, flags=re.S)
    return text


def numeric_tokens(block: Block) -> list[str]:
    text = " ".join(block.lines)
    if block.kind == "table" and block.units:
        cells = block.lines[0].split("|")[1:-1]
        text += " " + " ".join(
            (cell + " " + block.units[i]) if i < len(block.units) and not re.match(r"\s*\d{4}", cell)
            else cell
            for i, cell in enumerate(cells)
        )
    text = strip_exclusions(text)
    vals = []
    for m in NUMBER.finditer(text):
        token = m.group(0).strip()
        if re.fullmatch(r"\d{4}\s*(?:m|cm|mm)", token, re.I):
            continue  # 표 헤더 단위 상속이 날짜 열에 붙은 경우
        if YEAR.fullmatch(token) or re.fullmatch(r"\d+", token):
            continue
        vals.append(token)
    return vals


def frontmatter_warnings(text: str, names: set[str], path: str) -> list[str]:
    if not text.startswith("---"):
        return []
    end = text.find("\n---", 3)
    if end < 0:
        return []
    result = []
    for i, line in enumerate(text[:end].splitlines(), 1):
        if re.match(r"\s*(verification_method|sources):", line) and refs_in(line, names):
            result.append(f"{path}:{i}: [exp-num] frontmatter experience 근거 참조 | {line.strip()}")
    return result


def scan(path: str, text: str, names: set[str]) -> list[str]:
    rest, offset, layer = frontmatter(text)
    if layer == 4 or re.search(r"/\d+-applied-[^/]+\.md$", path):
        return []
    warnings = frontmatter_warnings(text, names, path)
    line_base = text[:offset].count("\n") + (1 if offset else 0)
    for b in blocks(rest, names):
        vals = numeric_tokens(b)
        if not vals or not b.refs:
            continue
        raw_block = "\n".join(b.lines)
        suppress = re.search(r"<!--\s*exp-num-ok:\s*(.*?)\s*-->", raw_block, re.S)
        if suppress and suppress.group(1).strip():
            continue
        reason = "·".join(sorted(b.refs))
        preview = " ".join(" ".join(b.lines).split())[:80]
        if suppress:
            warnings.append(f"{path}:{b.start + line_base}: [exp-num] 억제 주석 사유 필수 | {preview}")
        else:
            warnings.append(f"{path}:{b.start + line_base}: [exp-num] {reason} | {', '.join(vals)} | {preview}")
    return warnings


def main() -> int:
    staged = "--staged" in sys.argv
    names = experience_names(staged)
    if staged:
        paths = staged_paths()
    else:
        paths = [p for p in git(["ls-files", "--", "concepts/**/*.md", "models/**/*.md", "textbook/**/*.md"]).splitlines()
                 if p.startswith(TARGET_DIRS)]
    warnings: list[str] = []
    for path in sorted(set(paths)):
        text = read(path, staged)
        if text is not None and ("experience/" in text or "[[" in text):
            warnings.extend(scan(path, text, names))
    mode = "staged" if staged else "full"
    for w in warnings:
        print(w)
    print(f"[exp-num] 경고 {len(warnings)}건 (mode: {mode}).")
    return 1 if warnings and "--strict" in sys.argv else 0


if __name__ == "__main__":
    sys.exit(main())
