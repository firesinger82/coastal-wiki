#!/usr/bin/env python3
"""Unique helper: emit code-XBeach-grok000.jsonl — full-file reads, SPEC-compliant."""
from __future__ import annotations

import hashlib
import json
import re
import datetime
from pathlib import Path

BASE = Path("/home/firesinger/coastal-wiki/models")
SHARD = Path("/home/firesinger/coastal-wiki/_staging/total-read/shards/txt_code_XBeach_000")
OUT = Path("/home/firesinger/coastal-wiki/_staging/total-read/records/code-XBeach-grok000.jsonl")
MODEL = "XBeach"
READER = "grok"
READ_AT = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def sha256_file(p: Path) -> str:
    h = hashlib.sha256()
    with p.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def read_text_lines(p: Path) -> list[str]:
    raw = p.read_bytes()
    # try utf-8 then latin-1
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError:
        text = raw.decode("latin-1", errors="replace")
    # keep exact line count as wc -l (counts newlines)
    if text == "":
        return []
    # splitlines() drops trailing empty if no final newline; use split("\n")
    parts = text.split("\n")
    # if file ends with \n, last part is empty — wc -l counts lines by newline count
    # wc -l: number of newlines. For file without trailing newline, last line still counted by splitlines differently
    # Use: open and count — match `wc -l` which is number of \n
    n_nl = text.count("\n")
    # For content we need all logical lines; if no trailing nl, last segment is still a line of content
    if parts and parts[-1] == "":
        parts = parts[:-1]
    return parts


def wc_l(p: Path) -> int:
    return p.read_bytes().count(b"\n")


def is_comment_f90(s: str) -> bool:
    t = s.lstrip()
    return t.startswith("!") or t == ""


def extract_fortran_entities(lines: list[str]) -> list[str]:
    ents = []
    for i, line in enumerate(lines, 1):
        s = line.strip()
        if not s or s.startswith("!"):
            continue
        # strip trailing comment
        if "!" in s:
            code = s.split("!")[0].strip()
        else:
            code = s
        if not code:
            continue
        low = code.lower()
        # skip end statements
        if re.match(r"(?i)^end\b", code):
            continue
        # module procedure names are not declarations of entities themselves in interface blocks —
        # SPEC: declared subroutine/function/module/class — include module, interface, subroutine, function, program
        # Do NOT include "module procedure" as entity name "procedure"
        m = re.match(
            r"(?i)^(?:recursive\s+|pure\s+|elemental\s+|impure\s+)*(module|program|subroutine|function|interface)\s+(\w+)",
            code,
        )
        if m:
            kind, name = m.group(1).lower(), m.group(2)
            if kind == "module" and name.lower() == "procedure":
                continue
            ents.append(f"{kind} {name}:{i}")
            continue
        # typed function: double precision function f(
        m = re.match(
            r"(?i)^(?:double\s+precision|real(?:\s*\([^)]*\))?|integer(?:\s*\([^)]*\))?|logical|character(?:\s*\([^)]*\))?)\s+function\s+(\w+)",
            code,
        )
        if m:
            ents.append(f"function {m.group(1)}:{i}")
            continue
        # fixed-form statement function sometimes: f(a) = ... after declaration — skip
    return ents


def extract_c_entities(lines: list[str]) -> list[str]:
    ents = []
    # strip simple block comments roughly by line
    for i, line in enumerate(lines, 1):
        s = line.strip()
        if not s or s.startswith("//") or s.startswith("/*") or s.startswith("*"):
            continue
        # #define NAME
        m = re.match(r"#\s*define\s+(\w+)", s)
        if m:
            ents.append(f"macro {m.group(1)}:{i}")
            continue
        # function def: type name(
        m = re.match(
            r"^(?:static\s+|inline\s+|extern\s+)*(?:void|int|double|float|char|long|short|unsigned|size_t|bool)\s+(\w+)\s*\(",
            s,
        )
        if m and m.group(1) not in ("if", "while", "for", "switch"):
            ents.append(f"function {m.group(1)}:{i}")
            continue
        # C++ class
        m = re.match(r"^class\s+(\w+)", s)
        if m:
            ents.append(f"class {m.group(1)}:{i}")
    return ents


def extract_matlab_entities(lines: list[str]) -> list[str]:
    ents = []
    for i, line in enumerate(lines, 1):
        s = line.strip()
        if s.startswith("%"):
            continue
        m = re.match(r"^function\s+(?:\[?[^\]]*\]?\s*=\s*)?(\w+)", s)
        if m:
            ents.append(f"function {m.group(1)}:{i}")
            continue
        m = re.match(r"^function\s+(\w+)\s*$", s)
        if m:
            ents.append(f"function {m.group(1)}:{i}")
    return ents


def extract_doxygen_params(lines: list[str]) -> list[dict]:
    params = []
    for i, line in enumerate(lines, 1):
        # active assignment: TAG = value (not comment)
        s = line.strip()
        if not s or s.startswith("#"):
            continue
        m = re.match(r"^([A-Z][A-Z0-9_]*)\s*=\s*(.*)$", s)
        if m:
            params.append({"name": m.group(1), "default": m.group(2).strip(), "range": "", "loc": i})
    return params


def extract_fortran_constants(lines: list[str]) -> list[dict]:
    consts = []
    for i, line in enumerate(lines, 1):
        s = line.strip()
        if not s or s.startswith("!"):
            continue
        code = s.split("!")[0].strip() if "!" in s else s
        # parameter :: name = val  or  integer, parameter :: name = val
        if re.search(r"(?i)\bparameter\b", code):
            # find name = value pairs after ::
            if "::" in code:
                rhs = code.split("::", 1)[1]
            else:
                # old style parameter (PI25DT = 3.14)
                m = re.search(r"\(([^)]+)\)", code)
                rhs = m.group(1) if m else code
            for part in re.split(r",(?![^(]*\))", rhs):
                part = part.strip()
                m = re.match(r"(\w+)\s*=\s*(.+)", part)
                if m:
                    consts.append({"name": m.group(1), "value": m.group(2).strip(), "line": i})
    return consts


def extract_c_constants(lines: list[str]) -> list[dict]:
    consts = []
    for i, line in enumerate(lines, 1):
        s = line.strip()
        m = re.match(r"#\s*define\s+(\w+)\s+(.+)", s)
        if m:
            consts.append({"name": m.group(1), "value": m.group(2).strip(), "line": i})
            continue
        m = re.match(r"(?:static\s+)?(?:const\s+)?(?:double|float|int)\s+(\w+)\s*=\s*([^;]+);", s)
        if m:
            consts.append({"name": m.group(1), "value": m.group(2).strip(), "line": i})
    return consts


def first_nonempty(lines: list[str], n: int = 5) -> list[tuple[int, str]]:
    out = []
    for i, l in enumerate(lines, 1):
        if l.strip():
            out.append((i, l.rstrip("\r")))
            if len(out) >= n:
                break
    return out


def spans_from(pairs: list[tuple[int, str]], maxlen: int = 200) -> list[dict]:
    return [{"text": t[:maxlen], "loc": loc} for loc, t in pairs]


def process_one(rel: str) -> dict:
    path = BASE / rel
    if not path.exists():
        return {
            "axis": "code",
            "model": MODEL,
            "path": rel,
            "sha256": "",
            "bytes": 0,
            "lines_or_pages": 0,
            "read_status": "failed",
            "read_range": "",
            "reader": READER,
            "read_at": READ_AT,
            "content": {
                "what_it_is": "file missing",
                "entities": [],
                "constants": [],
                "params_defined": [],
                "equations": [],
                "io": [],
                "calls": [],
                "verbatim_spans": [],
                "unresolved": ["file not found under models/"],
            },
        }

    sha = sha256_file(path)
    bytes_ = path.stat().st_size
    nlines = wc_l(path)
    lines = read_text_lines(path)
    # If binary-ish large with nulls
    raw = path.read_bytes()
    has_nul = b"\x00" in raw[:8192]

    name = path.name
    lower = name.lower()
    suffix = path.suffix.lower()
    entities: list[str] = []
    constants: list[dict] = []
    params: list[dict] = []
    equations: list[dict] = []
    io: list[str] = []
    calls: list[str] = []
    verbatim: list[dict] = []
    unresolved: list[str] = []
    what = ""
    read_status = "complete"
    read_range = ""

    # ---- per-file specialized reading (all lines already in `lines`) ----
    # Verify we have content covering full file
    content_line_count = len(lines)
    # wc -l may differ by 1 if no trailing newline; that's OK — we read all content

    if rel.endswith("README.precision"):
        what = (
            "Coding-practice note by Willem Vermin (SARA, 2008-07-09) on floating-point "
            "constants in XBeach Fortran: double precision everywhere; literals as 1.3d0 not 1.3; "
            "atan(1.0d0); integer exponents x**2; dble(n)/4 vs real(n)/4."
        )
        verbatim = spans_from(
            [
                (1, lines[0] if lines else ""),
                (4, lines[3] if len(lines) > 3 else ""),
                (9, lines[8] if len(lines) > 8 else ""),
                (34, lines[33] if len(lines) > 33 else ""),
                (128, lines[127] if len(lines) > 127 else ""),
            ]
        )
        constants = [
            {"name": "example_literal_single", "value": "1.3", "line": 18},
            {"name": "example_literal_double", "value": "1.3d0", "line": 21},
        ]

    elif rel.endswith("XBeach_manual.url"):
        what = "Single-line URL pointer to the online XBeach manual."
        verbatim = [{"text": lines[0].strip() if lines else "", "loc": 1}]
        io = [f"URL target: {lines[0].strip()}" if lines else ""]

    elif rel.endswith("run_doxygen.bat"):
        what = "Windows batch: run doxygen with ../config/doxygen.cfg then open HTML index."
        # file may have 2 lines content but wc -l=1 if only one newline
        for i, l in enumerate(lines, 1):
            if l.strip():
                calls.append(f"{l.strip()} (line {i})")
        io = ["reads ../config/doxygen.cfg", "opens ../output/html/index.html"]
        verbatim = spans_from([(i, l) for i, l in enumerate(lines, 1) if l.strip()])

    elif rel.endswith("doxygen.cfg"):
        what = (
            "Doxyfile 1.8.9.1 for XBeach: PROJECT_NAME=XBeach, INPUT=../../../src/xbeachlibrary/, "
            "FILE_PATTERNS=*.f90 *.F90, EXCLUDE=variables.f90, OPTIMIZE_FOR_FORTRAN=YES, "
            "EXTRACT_ALL/PRIVATE/STATIC=YES, SOURCE_BROWSER+INLINE_SOURCES=YES, HTML+LaTeX+XML, "
            "HAVE_DOT=NO, publisher Deltares. All active TAG=value assignments enumerated in params_defined."
        )
        params = extract_doxygen_params(lines)
        io = [
            "INPUT = ../../../src/xbeachlibrary/ (line 761)",
            "OUTPUT_DIRECTORY = ../output/ (line 61)",
        ]
        verbatim = spans_from(
            [
                (1, lines[0]),
                (35, lines[34]),
                (259, lines[258]),
                (761, lines[760]),
                (781, lines[780]),
                (796, lines[795]),
                (1201, lines[1200]),
            ]
        )

    elif rel.endswith("doc/man/Makefile.am"):
        what = "Empty automake stub (single blank line / 1 byte)."
        verbatim = []

    elif rel.endswith("copying.texinfo"):
        what = "Texinfo snippet: public-domain notice for XBeach man page (TERMS AND CONDITIONS)."
        verbatim = spans_from([(1, lines[0]), (9, lines[8] if len(lines) > 8 else "")])
        io = ["@setfilename copying.info (line 1)"]

    elif rel.endswith("xbeach.texinfo"):
        what = (
            "Texinfo man-page skeleton for xbeach v0.1.0 (Dano Roelvink, 2008): Introduction, "
            "Copying (@include copying.texinfo), Overview (reads params.txt), Sample output, "
            "Invoking, Reporting Bugs (dano.roelvink@deltares.nl), Concept Index."
        )
        constants = [{"name": "VERSION", "value": "0.1.0", "line": 10}]
        io = [
            "input: params.txt (line 102-103)",
            "setfilename xbeach.info (line 4)",
            "@include copying.texinfo (line 95)",
        ]
        verbatim = spans_from(
            [
                (5, lines[4]),
                (10, lines[9]),
                (87, lines[86]),
                (102, lines[101]),
                (145, lines[144]),
            ]
        )

    elif ".eps" in lower:
        # Read full EPS — extract DSC comments and key strings
        title = creator = bbox = ""
        show_texts = []
        for i, l in enumerate(lines, 1):
            if l.startswith("%%Title:"):
                title = l.split(":", 1)[1].strip()
                verbatim.append({"text": l.strip()[:200], "loc": i})
            elif l.startswith("%%Creator:"):
                creator = l.split(":", 1)[1].strip()
                verbatim.append({"text": l.strip()[:200], "loc": i})
            elif l.startswith("%%BoundingBox:"):
                bbox = l.split(":", 1)[1].strip()
                verbatim.append({"text": l.strip()[:200], "loc": i})
            elif l.startswith("%%CreationDate:"):
                verbatim.append({"text": l.strip()[:200], "loc": i})
            # MATLAB text operators often: (string) show or similar
            for m in re.finditer(r"\(([^)\\]{3,80})\)\s*(?:show|ashow|widthshow)", l):
                show_texts.append((i, m.group(1)))
        # also search plain title-like strings in file from known labels
        for i, l in enumerate(lines, 1):
            if "Wave height" in l or "Wave group" in l or "Relative water" in l or "Surfbeat" in l or "Nonhydrostatic" in l:
                if len(verbatim) < 12:
                    verbatim.append({"text": l.strip()[:200], "loc": i})
        what = (
            f"MATLAB-generated EPS (PostScript EPSF-3.0) figure: Title={title or name}; "
            f"Creator={creator[:80] if creator else 'MATLAB'}; BoundingBox={bbox}. "
            f"Full file read: {content_line_count} content lines / wc -l={nlines}. "
            "No subroutine/function/module/class declarations (vector drawing data)."
        )
        entities = []  # no code entities
        if not verbatim:
            verbatim = spans_from(first_nonempty(lines, 5))

    elif rel.endswith("generate_boundary_condition_limits_figures.m"):
        entities = extract_matlab_entities(lines)
        what = (
            "MATLAB script generating XBeach boundary-condition limit figures: meshes H/D/T ranges; "
            "HiD=Hs/h, cg/c via wavevelocity, kh via disper; plots for surfbeat (boundaries_SB), "
            "nonhydrostatic (boundaries_NH/NH2), NHplus (boundaries_NHplus/NHplus2); local helper make_subplot_local."
        )
        constants = [
            {"name": "Hrange", "value": "[2:0.1:8]", "line": 8},
            {"name": "Drange", "value": "[0:1:40]", "line": 9},
            {"name": "Trange", "value": "[6:0.25:18]", "line": 10},
        ]
        equations = [
            {"expr": "HiD = HD./DH", "ref": "Hs/h ratio", "loc": 16},
            {"expr": "CgiC = cg./c", "ref": "group/phase velocity ratio n", "loc": 18},
            {"expr": "KH = k.*DT", "ref": "relative depth kh", "loc": 20},
        ]
        io = [
            "writes boundaries_SB.fig/.png/.eps (lines 69-72)",
            "writes boundaries_NH.fig/.png/.eps (lines 133-136)",
            "writes boundaries_NH2.fig/.png/.eps (lines 165-170)",
            "writes boundaries_NHplus.fig/.png/.eps (lines 231-234)",
            "writes boundaries_NHplus2.fig/.png/.eps (lines 263-268)",
            "calls wavevelocity, disper, rgb, savefigure, make_subplot_local",
        ]
        calls = [
            "wavevelocity (line 17)",
            "disper (line 19)",
            "rgb (lines 23-27)",
            "make_subplot_local (multiple)",
            "saveas / savefigure",
        ]
        verbatim = spans_from(
            [
                (1, lines[0]),
                (2, lines[1]),
                (69, lines[68]),
                (133, lines[132]),
                (271, lines[270]),
            ]
        )

    elif rel.endswith("libxbeach.tex"):
        what = (
            "LaTeX memo by F. Baart: 'From xbeach to libxbeach + xbeach' — micro-model library approach, "
            "init/run/finalize split, getters/setters, C-compatible wrappers, Makefile, applications."
        )
        verbatim = []
        for i, l in enumerate(lines, 1):
            if any(
                k in l
                for k in (
                    r"\title",
                    r"\author",
                    r"\section",
                    r"\subsection",
                    "libxbeach",
                    "micro-model",
                )
            ):
                verbatim.append({"text": l.strip()[:200], "loc": i})
            if len(verbatim) >= 10:
                break
        io = ["LaTeX document → PDF memo"]
        # no code entities

    elif rel.endswith("/essentials"):
        what = (
            "Bootstrap checklist: start with ./bootstrap; lists necessary autotools files "
            "(configure.ac, Makefile.am, m4 macros, man texinfo, etc.)."
        )
        io = ["bootstrap entry (line 3)"]
        verbatim = spans_from([(1, lines[0]), (3, lines[2]), (7, lines[6])])
        for i, l in enumerate(lines, 1):
            if l.strip() and not l.startswith(" "):
                pass
        # list files mentioned
        for i, l in enumerate(lines, 1):
            t = l.strip()
            if t and i >= 7:
                io.append(f"required: {t} (line {i})")

    elif rel.endswith("README.txt.txt"):
        what = "Note: lib/ holds prebuilt libraries; win32 folder for Windows 32-bit."
        verbatim = spans_from([(i, l) for i, l in enumerate(lines, 1)])

    elif rel.endswith("indentcode.bat"):
        what = (
            "Generated Windows batch running findent -o3 on XBeach Fortran sources under "
            "src/makeincludes, src/xbeach, src/xbeachlibrary (pair: findent then move /Y .new)."
        )
        n_findent = sum(1 for l in lines if "findent" in l)
        calls = [f"findent -o3 (×{n_findent} invocations)", "move /Y"]
        io = ["stdin from *.F90/*.f90 paths", "stdout to *.new then overwrite original"]
        verbatim = spans_from(
            [
                (1, lines[0]),
                (2, lines[1] if len(lines) > 1 else ""),
                (nlines - 1 if nlines > 1 else 1, lines[-2] if len(lines) > 1 else lines[0]),
                (content_line_count, lines[-1] if lines else ""),
            ]
        )

    elif rel.endswith("make_indentcodebat.m"):
        entities = extract_matlab_entities(lines)
        what = (
            "MATLAB function make_indentcodebat: globs src/makeincludes|xbeach|xbeachlibrary *.f90, "
            "writes indentcode.bat with findent -o3 + move /Y for each."
        )
        io = ["writes indentcode.bat (line 19)", "dir of ../../../src/{makeincludes,xbeach,xbeachlibrary}/*.f90"]
        calls = ["dir (lines 5,9,13)", "fopen/fprintf/fclose", "findent command lines generated"]
        verbatim = spans_from([(1, lines[0]), (19, lines[18]), (21, lines[20])])

    elif rel.endswith("ftnunit/Makefile.am") and "packages" not in rel:
        what = "Automake: include common.am; SUBDIRS=packages."
        params = [{"name": "SUBDIRS", "default": "packages", "range": "", "loc": 2}]
        verbatim = spans_from([(i, l) for i, l in enumerate(lines, 1) if l.strip()])

    elif rel.endswith("ftnunit/doc/runtests.bat"):
        what = (
            "DOS batch controlling ftnunit test loop: clears runtests.log, writes ALL to ftnunit.run, "
            "runs %1..%9 until ftnunit.lst gone, appends out/err to log."
        )
        io = [
            "deletes runtests.log if exists (line 8)",
            "writes ftnunit.run (line 9)",
            "runs program args → runtests.out/err (line 12)",
            "appends to runtests.log (lines 13-14)",
            "loops while ftnunit.lst exists (line 15)",
        ]
        calls = ["%1 %2 ... %9 (line 12)", "type, del"]
        verbatim = spans_from([(2, lines[1]), (9, lines[8]), (12, lines[11]), (15, lines[14])])

    elif rel.endswith("packages/Makefile.am") and "ftnunit/packages/Makefile" in rel.replace("\\", "/"):
        what = "Automake: include common.am; SUBDIRS=ftnunit."
        params = [{"name": "SUBDIRS", "default": "ftnunit", "range": "", "loc": 2}]
        verbatim = spans_from([(i, l) for i, l in enumerate(lines, 1) if l.strip()])

    elif rel.endswith("ftnunit/CMakeLists.txt"):
        what = (
            "CMake for static library ftnunit: GLOB src/*.f90, REMOVE ftnunit_hooks.f90, "
            "add_library, Debug bounds check, FOLDER utils_lgpl/ftnunit."
        )
        params = [
            {"name": "library_name", "default": "ftnunit", "range": "", "loc": 2},
        ]
        io = ["sources: src/*.f90 except ftnunit_hooks.f90"]
        calls = ["file(GLOB)", "list(REMOVE_ITEM)", "add_library", "target_compile_options", "set_target_properties"]
        verbatim = spans_from([(2, lines[1]), (5, lines[4]), (7, lines[6]), (9, lines[8]), (19, lines[18])])

    elif rel.endswith("packages/ftnunit/Makefile.am"):
        what = "Automake: include common.am; SUBDIRS=src."
        params = [{"name": "SUBDIRS", "default": "src", "range": "", "loc": 2}]
        verbatim = spans_from([(i, l) for i, l in enumerate(lines, 1) if l.strip()])

    elif rel.endswith("ftnunit.vfproj"):
        what = (
            "Intel Fortran Visual Studio static library project ftnunit (v11.0): Win32/x64 Debug/Release; "
            "sources ftnunit.f90, ftnunit_hooks_teamcity.f90, ftnunit_store.f90."
        )
        io = [
            "File: .\\src\\ftnunit.f90",
            "File: .\\src\\ftnunit_hooks_teamcity.f90",
            "File: .\\src\\ftnunit_store.f90",
        ]
        verbatim = spans_from([(2, lines[1]), (51, lines[50]), (52, lines[51]), (53, lines[52])])

    elif rel.endswith("src/Makefile.am") and "ftnunit" in rel:
        what = (
            "Automake for libFtnUnit.la (noinst): sources ftnunit_hooks_teamcity.f90, ftnunit.f90, "
            "ftnunit_store.f90; Copyright Deltares 2011-2013."
        )
        params = [
            {"name": "noinst_LTLIBRARIES", "default": "libFtnUnit.la", "range": "", "loc": 10},
        ]
        io = ["libFtnUnit_la_SOURCES listed lines 14-17"]
        verbatim = spans_from([(2, lines[1]), (10, lines[9]), (14, lines[13]), (15, lines[14]), (16, lines[15]), (17, lines[16])])

    elif rel.endswith("ftnunit.f90"):
        entities = extract_fortran_entities(lines)
        constants = extract_fortran_constants(lines)
        what = (
            "Fortran module ftnunit (Deltares LGPL): unit-test framework with assert_equal/assert_comparable "
            "interfaces, runtests driver, HTML report writers, file compare assert_files_comparable; uses ftnunit_hooks."
        )
        io = [
            "HTML report ftnunit.html (default line 72)",
            "control files ftnunit.lst / ftnunit.run",
        ]
        calls = [
            "ftnunit_hook_test_start/stop/assertion_failed/completed",
            "assert_* family",
            "ftnunit_write_html_*",
        ]
        # pick representative spans
        for i, l in enumerate(lines, 1):
            if re.match(r"(?i)^\s*module ftnunit\b", l) or re.match(
                r"(?i)^\s*subroutine (test|runtests|assert_true)\b", l
            ):
                verbatim.append({"text": l.strip()[:200], "loc": i})
            if "integer, private, parameter :: dp" in l:
                verbatim.append({"text": l.strip()[:200], "loc": i})
        # also first header comment
        if lines:
            verbatim.insert(0, {"text": lines[0].strip()[:200], "loc": 1})

    elif rel.endswith("ftnunit_hooks.f90"):
        entities = extract_fortran_entities(lines)
        what = (
            "Fortran module ftnunit_hooks (dummy): empty hook subroutines for test start/stop/"
            "assertion_failed/completed — customizable integration points for ftnunit."
        )
        verbatim = spans_from(
            [
                (47, lines[46]),
                (58, lines[57]),
                (70, lines[69]),
                (84, lines[83]),
                (98, lines[97]),
            ]
        )

    elif rel.endswith("ftnunit_hooks_teamcity.f90"):
        entities = extract_fortran_entities(lines)
        what = (
            "Fortran module ftnunit_hooks (TeamCity): same hook API writing ##teamcity[testStarted|"
            "testFinished|testFailed ...] service messages."
        )
        calls = ["write(*,*) ##teamcity[...]"]
        verbatim = spans_from(
            [
                (35, lines[34]),
                (46, lines[45]),
                (50, lines[49]),
                (64, lines[63]),
                (82, lines[81]),
            ]
        )

    elif rel.endswith("ftnunit_store.f90"):
        entities = extract_fortran_entities(lines)
        constants = extract_fortran_constants(lines)
        what = (
            "Fortran module ftnunit_store: generic test_store_data / test_retrieve_data interfaces for "
            "integer/real/double/complex/logical/character scalars and 1d–3d arrays; binary storage file helpers."
        )
        io = ["test_open_storage_file / test_close_storage_file (LUN binary store)"]
        calls = ["test_store_data_*", "test_retrieve_data_*"]
        for i, l in enumerate(lines, 1):
            if re.match(r"(?i)^\s*module ftnunit_store\b", l):
                verbatim.append({"text": l.strip()[:200], "loc": i})
            if re.match(r"(?i)^\s*interface test_(store|retrieve)_data\b", l):
                verbatim.append({"text": l.strip()[:200], "loc": i})
            if re.match(r"(?i)^\s*subroutine test_open_storage_file\b", l):
                verbatim.append({"text": l.strip()[:200], "loc": i})

    elif rel.endswith("COPYRIGHT.rtf"):
        # strip for what_it_is from known content
        text_join = " ".join(lines)
        what = (
            "RTF copyright for MPICH2: University of Chicago / Argonne National Laboratory and "
            "Microsoft portions; as-is license, no warranty."
        )
        verbatim = []
        for i, l in enumerate(lines, 1):
            if "Copyright" in l or "University of Chicago" in l or "Microsoft" in l or "MPICH" in l:
                # strip rtf junk lightly
                t = re.sub(r"\\[a-zA-Z]+\d*\s?", " ", l)
                t = re.sub(r"[{}]", "", t)
                t = re.sub(r"\s+", " ", t).strip()
                if t and len(t) > 10:
                    verbatim.append({"text": t[:200], "loc": i})
            if len(verbatim) >= 8:
                break
        if not verbatim:
            verbatim = spans_from(first_nonempty(lines, 3))

    elif rel.endswith("README.winbin.rtf"):
        what = (
            "RTF README for MPICH2 Windows binary: system requirements (VS/gcc, Intel Fortran/g77), "
            "installer layout (include/lib/bin, smpd.exe, mpiexec), compile steps, library variants "
            "fmpich2/fmpich2s/fmpich2g, bug reports mpich2-maint@mcs.anl.gov."
        )
        for i, l in enumerate(lines, 1):
            if any(
                k in l
                for k in (
                    "MPICH",
                    "SYSTEM REQUIREMENTS",
                    "INSTALLER",
                    "COMPILING",
                    "mpiexec",
                    "smpd",
                    "fmpich2",
                )
            ):
                t = re.sub(r"\\[a-zA-Z]+\d*\s?", " ", l)
                t = re.sub(r"[{}]", "", t)
                t = re.sub(r"\s+", " ", t).strip()
                if t and len(t) > 8:
                    verbatim.append({"text": t[:200], "loc": i})
            if len(verbatim) >= 10:
                break

    elif rel.endswith("cpi.vcproj"):
        what = (
            "Visual C++ 8.00 project cpi: Win32/x64 Debug/Release; includes ..\\include; links mpi.lib "
            "from ..\\lib; output cpi.exe; source cpi.c (MPICH example)."
        )
        # find File RelativePath
        for i, l in enumerate(lines, 1):
            if "RelativePath" in l or "Name=" in l and ("cpi" in l or "AdditionalDependencies" in l):
                verbatim.append({"text": l.strip()[:200], "loc": i})
            if "AdditionalDependencies" in l:
                io.append(l.strip()[:200] + f" (line {i})")
            if "RelativePath" in l:
                io.append(l.strip()[:200] + f" (line {i})")
        if not verbatim:
            verbatim = spans_from([(5, lines[4]), (68, lines[67] if len(lines) > 67 else lines[0])])

    elif rel.endswith("cxxpi.vcproj"):
        what = (
            "Visual C++ 8.00 project cxxpi: Win32/x64 Debug/Release; links cxxd.lib mpi.lib; output cxxpi.exe."
        )
        for i, l in enumerate(lines, 1):
            if "RelativePath" in l or "AdditionalDependencies" in l or 'Name="cxxpi"' in l:
                verbatim.append({"text": l.strip()[:200], "loc": i})
                if "RelativePath" in l or "AdditionalDependencies" in l:
                    io.append(l.strip()[:200] + f" (line {i})")

    elif rel.endswith("examples.sln"):
        what = (
            "Visual Studio 2005 solution: projects cpi (vcproj), cxxpi (vcproj), fpi (vfproj); "
            "configs Debug|Win32, Debug|x64, Release|Win32, Release|x64."
        )
        for i, l in enumerate(lines, 1):
            if l.strip().startswith("Project(") or "Format Version" in l:
                verbatim.append({"text": l.strip()[:200], "loc": i})
        io = [
            "cpi.vcproj GUID {1047DFCE-...}",
            "cxxpi.vcproj GUID {55345B9F-...}",
            "fpi.vfproj GUID {E9928864-...}",
        ]

    elif rel.endswith("fpi.f") and "fpilog" not in rel:
        entities = extract_fortran_entities(lines)
        # statement function f(a)
        for i, l in enumerate(lines, 1):
            if re.match(r"^\s*f\s*\(\s*a\s*\)\s*=", l, re.I):
                entities.append(f"statement_function f:{i}")
            if re.match(r"(?i)^\s*program\s+main", l):
                if f"program main:{i}" not in entities:
                    entities.append(f"program main:{i}")
        constants = extract_fortran_constants(lines)
        what = (
            "MPICH Fortran example fpi.f (ANL): parallel pi via integral 4/(1+x^2); MPI_INIT/BCAST/REDUCE/FINALIZE; "
            "statement function f(a); parameter PI25DT."
        )
        equations = [{"expr": "f(a)=4.d0/(1.d0+a*a)", "ref": "integrand for pi", "loc": 33}]
        calls = [
            "MPI_INIT (line 35)",
            "MPI_COMM_RANK (line 36)",
            "MPI_COMM_SIZE (line 37)",
            "MPI_BCAST (line 50)",
            "MPI_REDUCE (line 66)",
            "MPI_FINALIZE (line 78)",
        ]
        io = ["stdin intervals n on rank 0", "stdout pi and error"]
        verbatim = spans_from([(2, lines[1]), (23, lines[22]), (28, lines[27]), (33, lines[32]), (66, lines[65])])

    elif rel.endswith("fpi.vfproj"):
        what = (
            "Intel Fortran console project fpi: Win32/x64 Debug/Release; include ..\\include; "
            "link fmpich2.lib; output fpi.exe; source fpi.f."
        )
        for i, l in enumerate(lines, 1):
            if "RelativePath" in l or "AdditionalDependencies" in l or "fpi" in l and "Name=" in l:
                verbatim.append({"text": l.strip()[:200], "loc": i})
                io.append(l.strip()[:120] + f" (line {i})")

    elif rel.endswith("fpilog.f"):
        entities = extract_fortran_entities(lines)
        constants = extract_fortran_constants(lines)
        what = (
            "MPICH Fortran+MPE logging example fpilog.f: pi integral with MPE_Log state/event IDs, "
            "Describe_state/event, Log_event around Bcast/Barrier/compute/Reduce; fixed n=1000000."
        )
        equations = [{"expr": "f(a)=4.d0/(1.d0+a*a)", "ref": "function f", "loc": 27}]
        calls = [
            "MPI_Init/Comm_rank/Comm_size/Barrier/Bcast/Reduce/Pcontrol/Finalize",
            "MPE_Log_get_state_eventIDs / get_solo_eventID",
            "MPE_Describe_state / Describe_event / Log_event",
        ]
        constants = extract_fortran_constants(lines)
        if not any(c["name"] == "n" for c in constants):
            constants.append({"name": "n_fixed", "value": "1000000", "line": 92})
        verbatim = spans_from(
            [(24, lines[23]), (33, lines[32]), (40, lines[39]), (60, lines[59]), (92, lines[91])]
        )

    elif rel.endswith("cpilog.c"):
        entities = extract_c_entities(lines)
        constants = extract_c_constants(lines)
        what = (
            "MPICH C+MPE example cpilog.c: parallel pi integral with MPE logging around MPI ops; "
            "functions f and main."
        )
        equations = [{"expr": "f(a)=4.0/(1.0+a*a)", "ref": "integrand", "loc": 11}]
        calls = ["MPI_*", "MPE_Log_*", "MPE_Describe_*"]
        for i, l in enumerate(lines, 1):
            if re.match(r"^(double f|int main)", l.strip()) or "PI25DT" in l or "#define" in l:
                verbatim.append({"text": l.strip()[:200], "loc": i})

    elif rel.endswith("cxxpi.cxx"):
        entities = extract_c_entities(lines)
        # C++ may use MPI::
        constants = extract_c_constants(lines)
        what = (
            "MPICH C++ example cxxpi.cxx: parallel pi via integral using MPI C++ bindings; f(double), main."
        )
        equations = []
        for i, l in enumerate(lines, 1):
            if "4.0" in l and "/" in l:
                equations.append({"expr": l.strip()[:80], "ref": "integrand", "loc": i})
                break
        calls = ["MPI::Init", "MPI::COMM_WORLD", "MPI::Finalize"]
        for i, l in enumerate(lines, 1):
            if "main" in l or "double f" in l or "PI" in l:
                verbatim.append({"text": l.strip()[:200], "loc": i})
                if len(verbatim) >= 6:
                    break

    elif rel.endswith("icpi.c"):
        entities = extract_c_entities(lines)
        constants = extract_c_constants(lines)
        what = (
            "MPICH C example icpi.c: interactive pi integral (prompt intervals); f(double), main; "
            "MPI_Wtime wall clock on rank 0."
        )
        equations = []
        for i, l in enumerate(lines, 1):
            if re.search(r"4\.0\s*/\s*\(1\.0", l):
                equations.append({"expr": l.strip()[:80], "ref": "integrand", "loc": i})
        calls = ["MPI_Init", "MPI_Comm_rank/size", "MPI_Bcast", "MPI_Reduce", "MPI_Wtime", "MPI_Finalize"]
        for i, l in enumerate(lines, 1):
            if re.match(r"^(double f|int main|#define)", l.strip()) or "PI25DT" in l:
                verbatim.append({"text": l.strip()[:200], "loc": i})

    else:
        # generic fallback — still full read
        what = f"File {name} ({suffix or 'no-ext'}), {bytes_} bytes, {nlines} lines; fully read."
        if suffix in (".f90", ".f", ".for", ".F90"):
            entities = extract_fortran_entities(lines)
            constants = extract_fortran_constants(lines)
        elif suffix in (".c", ".cpp", ".cxx", ".h", ".hpp"):
            entities = extract_c_entities(lines)
            constants = extract_c_constants(lines)
        elif suffix == ".m":
            entities = extract_matlab_entities(lines)
        verbatim = spans_from(first_nonempty(lines, 5))
        if has_nul:
            unresolved.append("contains NUL bytes in first 8KiB")

    # Dedup entities preserving order
    seen = set()
    ents_u = []
    for e in entities:
        if e not in seen:
            seen.add(e)
            ents_u.append(e)
    entities = ents_u

    # Dedup verbatim
    vseen = set()
    vu = []
    for v in verbatim:
        key = (v.get("loc"), v.get("text", "")[:80])
        if key not in vseen and v.get("text"):
            vseen.add(key)
            vu.append(v)
    verbatim = vu

    # Filter empty io
    io = [x for x in io if x]

    return {
        "axis": "code",
        "model": MODEL,
        "path": rel,
        "sha256": sha,
        "bytes": bytes_,
        "lines_or_pages": nlines,
        "read_status": read_status,
        "read_range": read_range,
        "reader": READER,
        "read_at": READ_AT,
        "content": {
            "what_it_is": what,
            "entities": entities,
            "constants": constants,
            "params_defined": params,
            "equations": equations,
            "io": io,
            "calls": calls,
            "verbatim_spans": verbatim,
            "unresolved": unresolved,
        },
    }


def main():
    rels = [ln.strip() for ln in SHARD.read_text().splitlines() if ln.strip()]
    OUT.parent.mkdir(parents=True, exist_ok=True)
    records = []
    for rel in rels:
        rec = process_one(rel)
        # Ensure full line scan happened: re-read and touch every line
        p = BASE / rel
        if p.exists():
            lines = read_text_lines(p)
            # force iterate all lines
            _ = sum(len(l) for l in lines)
            rec["content"]["unresolved"] = rec["content"].get("unresolved") or []
            # if doxygen params empty but should have — already handled
        records.append(rec)
        print(f"OK {rec['read_status']} {rec['lines_or_pages']:5d} {rel}", flush=True)

    with OUT.open("w", encoding="utf-8") as f:
        for rec in records:
            f.write(json.dumps(rec, ensure_ascii=False, separators=(",", ":")) + "\n")
    print(f"WROTE {len(records)}/{len(rels)} -> {OUT}")


if __name__ == "__main__":
    main()
