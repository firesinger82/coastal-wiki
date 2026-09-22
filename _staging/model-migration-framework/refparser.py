r"""coastal-wiki source reference parser (DESIGN v2 §REFERENCE GRAMMAR).

명시 규칙:
  - 확장자는 longest-match (정규식 대안 순서에 의존하지 않고 길이 내림차순 + 경계 검사)
  - 범위는 hyphen/en dash, L 접두, 복수 범위(`a-b,c-d`) 보존
  - bare `:NN` 은 file-qualified 로 승격하지 않는다
  - 코드블록/frontmatter 는 excluded 로 표시(탐지는 하되 자동 수정 대상 아님)
  - LaTeX 수식 영역($$…$$, $…$)은 마스킹한다 — `\mathrm{c.c.}` 같은 표기가
    파일 참조로 오인되는 것을 막는다 (SWAN 파일럿 2026-09-20)
  - 빈 stem(`.ftn90`)은 참조가 아니다. 숫자 stem(`swancom1/5.ftn`)은
    슬래시 축약 표기이므로 anomaly 로 표시하고 경로로 해석하지 않는다
"""
import re

# 확장자 목록은 **위키가 실제로 인용하는 것**을 기준으로 한다.
# 소스 언어만 넣으면 스크립트·설정 기반 저장소(asgs 의 sh/pl, LISFLOOD 의 cu,
# XBeach 의 def)의 인용이 통째로 누락된다 — asgs 파일럿에서 실측 247건 확인.
EXTS = sorted(
    # 컴파일 언어
    ["ftn90", "ftn", "F90", "f90", "for", "cpp", "cuh", "cu", "inc",
     "F", "f", "c", "h",
     # 스크립트
     "py", "js", "pl", "pm", "sh", "m",
     # 설정·정의·문서
     "wgsl", "rst", "cff", "def", "igs", "CMN", "yaml", "yml", "json",
     "cmake", "in", "am", "vfproj", "txt"],
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


MATH_BLOCK_RE = re.compile(r"\$\$.*?\$\$", re.S)
MATH_INLINE_RE = re.compile(r"(?<!\$)\$(?!\$)[^$\n]+?(?<!\$)\$(?!\$)")


def mask_math(line):
    """수식 영역을 같은 길이의 공백으로 치환한다(열 오프셋 보존)."""
    def blank(m):
        return " " * (m.end() - m.start())
    return MATH_INLINE_RE.sub(blank, MATH_BLOCK_RE.sub(blank, line))


def _anomaly(path):
    """경로 모양만으로 판별되는 비정상 참조."""
    stem = path.rsplit("/", 1)[-1].rsplit(".", 1)[0]
    if stem == "":
        return "EMPTY_STEM"                                # `.ftn/.ftn90` 같은 확장자 언급
    if stem.isdigit():
        return "NUMERIC_STEM"                              # `swancom1/5.ftn` 슬래시 축약
    ext = path.rsplit("/", 1)[-1][len(stem) + 1:]
    if len(stem) == 1 and stem.isupper() and len(ext) == 1 and ext.isupper():
        # 논문 저자 이니셜 — "Fairall, C.W., **E.F.** Bradley, …" 의 `E.F`
        # 안전성 확인(2026-09-22): `^[A-Z]\.[A-Z]$` 형태의 실파일은 models/*/raw 전체에 0건.
        # **모양 기반 억제 금지(failure mode 30)의 예외가 아니다** — 짧은 stem 자체를
        # 억제하면 io.F·bc.F·gp.c 등 실참조 19건이 죽는다(ROMS 실측). 여기서 억제하는 것은
        # `단일 대문자 + 단일 대문자` 조합뿐이고, 그 조합에 해당하는 실파일이 없음을 확인했다.
        # 서지 줄 전체를 억제하는 안은 기각했다 — 그 줄들에 실참조 11건이 함께 있었다.
        return "BIBLIOGRAPHIC_INITIALS"
    return None


def parse_line(line, in_code=False, in_frontmatter=False, in_math=False):
    """한 줄에서 참조 후보를 뽑는다. 반환: list of dict"""
    refs = []
    excluded = in_code or in_frontmatter
    if in_math:
        return refs                                        # 수식 블록 내부는 탐지하지 않는다
    line = mask_math(line)
    for m in BRACKET_RE.finditer(line):
        refs.append(dict(kind="file-line", path=m.group("path"), ranges=parse_ranges(m.group("lines")),
                         raw=m.group(0), excluded=excluded, anomaly=_anomaly(m.group("path")),
                         syntax="bracket"))
    spans = [m.span() for m in BRACKET_RE.finditer(line)]
    for m in FILE_RE.finditer(line):
        if any(s0 <= m.start() < e0 for s0, e0 in spans):
            continue                                       # bracket 문법 내부 중복 방지
        an = _anomaly(m.group("path"))
        if an == "EMPTY_STEM":
            continue                                       # 참조가 아니다
        rngs = parse_ranges(m.group("lines")) if m.group("lines") else None
        refs.append(dict(kind="file-line" if rngs else "file", path=m.group("path"), ranges=rngs,
                         raw=m.group(0), excluded=excluded, anomaly=an,
                         syntax="file-range" if rngs else "file"))
    for m in BARE_RE.finditer(line):
        refs.append(dict(kind="bare", path=None, ranges=parse_ranges(m.group("lines")),
                         raw=m.group(0), excluded=excluded, anomaly=None, syntax="bare"))
    file_tokens = {r["raw"] for r in refs if r["kind"] in ("file", "file-line")}
    for m in SYM_RE.finditer(line):
        if any(m.group("sym") in t for t in file_tokens):
            continue
        refs.append(dict(kind="symbol", path=None, ranges=None, symbol=m.group("sym"),
                         raw=m.group(0), excluded=excluded, anomaly=None, syntax="symbol"))
    return refs


def parse_note(text):
    """노트 전체. 코드블록·frontmatter 를 표시하고 줄 번호를 붙인다."""
    out = []
    in_code = False
    in_math = False
    lines = text.splitlines()
    in_fm = lines[:1] == ["---"]
    for i, line in enumerate(lines, 1):
        if in_fm and i > 1 and line.strip() == "---":
            in_fm = False
            continue
        if line.lstrip().startswith("```"):
            in_code = not in_code
            continue
        if not in_code and line.strip() == "$$":
            in_math = not in_math            # 여러 줄 수식 블록 펜스
            continue
        for r in parse_line(line, in_code=in_code, in_frontmatter=in_fm, in_math=in_math):
            r["line"] = i
            out.append(r)
    return out


def intervals_overlap(cit, hunks):
    """citation interval [a,b] 와 changed hunk interval 들의 실제 교집합 여부"""
    a, b = cit
    return [h for h in hunks if not (b < h[0] or a > h[1])]
