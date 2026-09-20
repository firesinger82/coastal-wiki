"""coastal-wiki source reference parser (DESIGN v2 §REFERENCE GRAMMAR).

명시 규칙:
  - 확장자는 longest-match (정규식 대안 순서에 의존하지 않고 길이 내림차순 + 경계 검사)
  - 범위는 hyphen/en dash, L 접두, 복수 범위(`a-b,c-d`) 보존
  - bare `:NN` 은 file-qualified 로 승격하지 않는다
  - 코드블록/frontmatter 는 excluded 로 표시(탐지는 하되 자동 수정 대상 아님)
"""
import re

EXTS = sorted(
    ["ftn90", "ftn", "F90", "f90", "for", "cpp", "inc", "rst", "cff",
     "wgsl", "F", "f", "c", "h", "py", "js", "m"],
    key=lambda e: (-len(e), e),
)
_EXT_ALT = "|".join(re.escape(e) for e in EXTS)          # 길이 내림차순 고정
_PATH = r"(?:\.{1,2}/)*[A-Za-z0-9_][A-Za-z0-9_./+-]*"
_RANGE = r"L?\d+(?:\s*[-–—]\s*L?\d+)?"
_RANGES = rf"{_RANGE}(?:\s*,\s*{_RANGE})*"

FILE_RE = re.compile(rf"(?P<path>{_PATH}\.(?:{_EXT_ALT}))(?![A-Za-z0-9_])(?::(?P<lines>{_RANGES}))?")
BARE_RE = re.compile(rf"`:(?P<lines>{_RANGES})`")
BRACKET_RE = re.compile(rf"\[file=(?P<path>{_PATH})\s+line=(?P<lines>{_RANGES})\]")
SYM_RE = re.compile(r"`(?P<sym>[A-Za-z_][A-Za-z0-9_%]{2,40})(?:\([^`]*\))?`")


def parse_ranges(text):
    """'44-153, 160' → [(44,153),(160,160)]"""
    out = []
    for part in re.split(r"\s*,\s*", text.strip()):
        m = re.fullmatch(r"L?(\d+)(?:\s*[-–—]\s*L?(\d+))?", part.strip())
        if not m:
            return None                                   # 부분 파싱 성공으로 세지 않음
        a = int(m.group(1))
        b = int(m.group(2)) if m.group(2) else a
        out.append((a, b))
    return out


def parse_line(line, in_code=False, in_frontmatter=False):
    """한 줄에서 참조 후보를 뽑는다. 반환: list of dict"""
    refs = []
    excluded = in_code or in_frontmatter
    for m in BRACKET_RE.finditer(line):
        refs.append(dict(kind="file-line", path=m.group("path"), ranges=parse_ranges(m.group("lines")),
                         raw=m.group(0), excluded=excluded, syntax="bracket"))
    spans = [m.span() for m in BRACKET_RE.finditer(line)]
    for m in FILE_RE.finditer(line):
        if any(s0 <= m.start() < e0 for s0, e0 in spans):
            continue                                       # bracket 문법 내부 중복 방지
        rngs = parse_ranges(m.group("lines")) if m.group("lines") else None
        refs.append(dict(kind="file-line" if rngs else "file", path=m.group("path"), ranges=rngs,
                         raw=m.group(0), excluded=excluded,
                         syntax="file-range" if rngs else "file"))
    for m in BARE_RE.finditer(line):
        refs.append(dict(kind="bare", path=None, ranges=parse_ranges(m.group("lines")),
                         raw=m.group(0), excluded=excluded, syntax="bare"))
    file_tokens = {r["raw"] for r in refs if r["kind"] in ("file", "file-line")}
    for m in SYM_RE.finditer(line):
        if any(m.group("sym") in t for t in file_tokens):
            continue
        refs.append(dict(kind="symbol", path=None, ranges=None, symbol=m.group("sym"),
                         raw=m.group(0), excluded=excluded, syntax="symbol"))
    return refs


def parse_note(text):
    """노트 전체. 코드블록·frontmatter 를 표시하고 줄 번호를 붙인다."""
    out = []
    in_code = False
    lines = text.splitlines()
    in_fm = lines[:1] == ["---"]
    for i, line in enumerate(lines, 1):
        if in_fm and i > 1 and line.strip() == "---":
            in_fm = False
            continue
        if line.lstrip().startswith("```"):
            in_code = not in_code
            continue
        for r in parse_line(line, in_code=in_code, in_frontmatter=in_fm):
            r["line"] = i
            out.append(r)
    return out


def intervals_overlap(cit, hunks):
    """citation interval [a,b] 와 changed hunk interval 들의 실제 교집합 여부"""
    a, b = cit
    return [h for h in hunks if not (b < h[0] or a > h[1])]
