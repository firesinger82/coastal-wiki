"""PARSER SELF-TEST / GRAMMAR REGRESSION SUITE (DESIGN v2 acceptance gate 13).

실패 시 PARSER_GATE_FAILED. 실행: python3 test_refparser.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import refparser as rp

FIX = [
    # (설명, 입력 줄, expected: [(kind, path, ranges)])
    ("f",            "see `calexp.f:120`",                    [("file-line", "calexp.f", [(120, 120)])]),
    ("f90",          "`mod_heat.f90:251-1490`",               [("file-line", "mod_heat.f90", [(251, 1490)])]),
    ("ftn",          "`swanpre1.ftn:738`",                    [("file-line", "swanpre1.ftn", [(738, 738)])]),
    ("ftn90-필수1",  "`SwanReadADCGrid.ftn90:44-153`",        [("file-line", "SwanReadADCGrid.ftn90", [(44, 153)])]),
    ("ftn90-필수2",  "`SwanReadADCGrid.ftn90:44-103`",        [("file-line", "SwanReadADCGrid.ftn90", [(44, 103)])]),
    ("F90",          "`weir_boundary.F90:2477-2579`",         [("file-line", "weir_boundary.F90", [(2477, 2579)])]),
    ("for",          "`svdcmp.for:163`",                      [("file-line", "svdcmp.for", [(163, 163)])]),
    ("cpp",          "`lisflood.cpp:88-90`",                  [("file-line", "lisflood.cpp", [(88, 90)])]),
    ("range-interior-필수3", "## 1. 카탈로그 (nodalattr.F:636-686)", [("file-line", "nodalattr.F", [(636, 686)])]),
    ("복수 범위",    "`input.f90:1-3,5-7`",                   [("file-line", "input.f90", [(1, 3), (5, 7)])]),
    ("en dash",      "`vsmy.F:1479–1486`",                    [("file-line", "vsmy.F", [(1479, 1486)])]),
    ("L 접두",       "`gwce.F:L1064`",                        [("file-line", "gwce.F", [(1064, 1064)])]),
    ("상대경로",     "`../thirdparty/swan/SwanReadADCGrid.ftn90:44-158`",
                     [("file-line", "../thirdparty/swan/SwanReadADCGrid.ftn90", [(44, 158)])]),
    ("괄호 안",      "적용(`setbcs.f90:203-490`) 참조",       [("file-line", "setbcs.f90", [(203, 490)])]),
    ("표 셀",        "| `hdmt.f90:88` | dispatch |",          [("file-line", "hdmt.f90", [(88, 88)])]),
    ("파일만",       "`couple2swan.F` 모듈",                  [("file", "couple2swan.F", None)]),
    ("bare",         "적용 지점(`:2271`)",                    [("bare", None, [(2271, 2271)])]),
    ("bare 범위",    "(`:2936-2970`)",                        [("bare", None, [(2936, 2970)])]),
    ("bracket",      "`[file=aaefdc.f90 line=22]`",           [("file-line", "aaefdc.f90", [(22, 22)])]),
    # 스크립트·설정 확장자 (asgs 파일럿 2026-09-21: 미인식으로 교집합 0 오판)
    ("shell",        "`asgs_main.sh:2208`",                   [("file-line", "asgs_main.sh", [(2208, 2208)])]),
    ("perl",         "`storm_track_gen.pl:46`",               [("file-line", "storm_track_gen.pl", [(46, 46)])]),
    ("cuda",         "`cuda_flow.cu:41`",                     [("file-line", "cuda_flow.cu", [(41, 41)])]),
    ("cuda header",  "`cuda/cuda_flow.cuh:9`",                [("file-line", "cuda/cuda_flow.cuh", [(9, 9)])]),
    ("def",          "`params.def:147`",                      [("file-line", "params.def", [(147, 147)])]),
    ("in",           "`s4dvar.in:461`",                       [("file-line", "s4dvar.in", [(461, 461)])]),
    ("txt",          "`doc/util/aswip.1.txt:133`",            [("file-line", "doc/util/aswip.1.txt", [(133, 133)])]),
]

SYMBOL_FIX = [("symbol-only", "`PADCSWAN_RUN` 호출", "PADCSWAN_RUN"),
              ("file+symbol", "`nodalattr.F:657` 의 `readNodalAttrXDMF`", "readNodalAttrXDMF")]

# SWAN 파일럿(2026-09-20) 회귀 fixture — 문맥 오탐 3종
NEGATIVE_FIX = [
    ("수식-복소공액", r"$$W(\vec{x}) = -\mathrm{i}\,\omega + \mathrm{c.c.}$$"),
    ("인라인 수식",   r"Fourier $\hat{\Gamma}(c.c.)$ 경유"),
    ("확장자 언급",   "어떤 `.ftn`/`.ftn90` 이 무슨 역할인지"),
]
ANOMALY_FIX = [("슬래시 축약1", "`swancom1/5.ftn`", "NUMERIC_STEM"),
               ("슬래시 축약2", "`swanpre1/2.ftn`", "NUMERIC_STEM"),
               # 논문 저자 이니셜 (2026-09-22). `^[A-Z]\.[A-Z]$` 형태 실파일은 0건 확인.
               # 짧은 stem 일반 억제는 금지 — io.F·bc.F 등 실참조가 죽는다(failure mode 30).
               ("저자 이니셜1", "Fairall, C.W., E.F. Bradley, D.P. Rogers (1996)", "BIBLIOGRAPHIC_INITIALS"),
               ("저자 이니셜2", "Grachev, A.A., A.F. Edson (2003)", "BIBLIOGRAPHIC_INITIALS"),
               # 글롭 패턴 (2026-09-22) — 선행 `*` 로 판정. `_` 로 시작하는 실파일이
               # 존재하므로(__init__.py·_config.yml) 모양만으로 억제하면 실참조가 죽는다.
               ("글롭1", "CUDA 8 *_gpu.F 파일", "GLOB_PATTERN"),
               ("글롭2", "셰이더 *_simulate.cuh 군", "GLOB_PATTERN")]

def norm(refs):
    return [(r["kind"], r["path"], r["ranges"]) for r in refs if r["kind"] != "symbol"]

def main():
    fails = []
    for name, line, exp in FIX:
        got = norm(rp.parse_line(line))
        if got != exp:
            fails.append(f"{name}: got {got} expected {exp}")
    for name, line, sym in SYMBOL_FIX:
        syms = [r.get("symbol") for r in rp.parse_line(line) if r["kind"] == "symbol"]
        if sym not in syms:
            fails.append(f"{name}: symbol {sym} not detected (got {syms})")
    # 확장자 절단 금지: .ftn90 이 .f/.ftn 으로 잘리지 않는다
    r = rp.parse_line("`SwanReadADCGrid.ftn90:44-153`")[0]
    if not r["path"].endswith(".ftn90"):
        fails.append(f"extension truncation: {r['path']}")
    # bare 를 file-qualified 로 오인하지 않는다
    if any(x["kind"] != "bare" for x in rp.parse_line("(`:2271`)")):
        fails.append("bare misparsed as file-qualified")
    # 한 문장 다중 파일: 둘 다 수집 (nearest-file 금지 근거)
    multi = rp.parse_line("`SwashUBotFrict.ftn90:254` 와 `SwashBotFrict.ftn90:298` 비교")
    if len([x for x in multi if x["kind"] == "file-line"]) != 2:
        fails.append("multi-file sentence not fully collected")
    # 코드블록 제외 표시
    note = "```fortran\n`calexp.f90:10`\n```\n`calexp.f90:20`\n"
    ex = [r for r in rp.parse_note(note) if r["kind"] == "file-line"]
    # 설계: 제외 영역도 탐지하되 excluded=True 로 표시(ledger 보존), 자동 수정 대상 아님
    if not (len(ex) == 2 and ex[0]["excluded"] and not ex[1]["excluded"]):
        fails.append(f"code block exclusion flag failed: {[(r['ranges'], r['excluded']) for r in ex]}")
    # 위키 내부 링크(.md)를 소스 참조로 잡지 않는다 — 넣으면 2,052건 오탐
    if [r for r in rp.parse_line("- [README](../README.md) 참조") if r["kind"] in ("file", "file-line")]:
        fails.append(".md 를 소스 참조로 오인")
    # 부분 파싱 금지: 잘못된 범위는 None
    if rp.parse_ranges("12-") is not None:
        fails.append("malformed range accepted")
    # 범위 교집합 계산
    if rp.intervals_overlap((636, 686), [(645, 650)]) == []:
        fails.append("interval intersection failed")
    # 문맥 오탐 금지 (SWAN 파일럿)
    for name, line in NEGATIVE_FIX:
        got = [r for r in rp.parse_line(line) if r["kind"] in ("file", "file-line")]
        if got:
            fails.append(f"{name}: 오탐 {[r['path'] for r in got]}")
    for name, line, want in ANOMALY_FIX:
        got = [r for r in rp.parse_line(line) if r["kind"] in ("file", "file-line")]
        if not (len(got) == 1 and got[0].get("anomaly") == want):
            fails.append(f"{name}: anomaly {[(r['path'], r.get('anomaly')) for r in got]} != {want}")
    # 짧은 stem 실참조는 살아 있어야 한다 — 이니셜 규칙이 이들을 잡으면 안 된다
    # (파서 인식 확장자만 — .mat/.inp 는 EXTS 에 없어 애초에 참조로 잡지 않는다)
    # 글롭 판정이 **마크다운 강조**를 먹지 않는지. 구분 없이 선행 `*` 만 보면
    # `**swancom1.ftn**` 이 글롭이 되어 실참조 65건이 통째로 죽는다(실측 2026-09-22).
    for probe in ("`__init__.py` 참조", "**swancom1.ftn** 참조", "*swancom1.ftn* 이탤릭",
                  "강조 **calexp.f90:10-20** 인용"):
        g = [r for r in rp.parse_line(probe) if r["kind"] in ("file", "file-line")]
        if g and g[0].get("anomaly") == "GLOB_PATTERN":
            fails.append(f"강조/일반 참조를 글롭으로 오판: {probe}")

    for probe in ("io.F", "bc.F", "gp.c", "df.c", "oc.c"):
        got = [r for r in rp.parse_line(f"`{probe}` 참조") if r["kind"] in ("file", "file-line")]
        if not got or got[0].get("anomaly"):
            fails.append(f"짧은 stem 실참조가 억제됨: {probe} → {got}")

    # 여러 줄 수식 블록 펜스
    mb = [r for r in rp.parse_note("$$\n\\mathrm{c.c.}\n$$\n`calexp.f90:20`\n")
          if r["kind"] == "file-line"]
    if len(mb) != 1 or mb[0]["path"] != "calexp.f90":
        fails.append(f"math fence failed: {[(r['path'], r['ranges']) for r in mb]}")

    n = len(FIX) + len(SYMBOL_FIX) + len(NEGATIVE_FIX) + len(ANOMALY_FIX)
    print(f"fixtures {n} + 규칙검사 11 | 실패 {len(fails)}")
    for f in fails:
        print("  FAIL:", f)
    if fails:
        print("\nPARSER_GATE_FAILED")
        return 1
    print("\nPARSER_GATE_PASSED")
    return 0

if __name__ == "__main__":
    sys.exit(main())
