#!/usr/bin/env python3
"""test_validate_research_isolation.py — regression test suite.

정책 출처: plan.md M10, D3, codex review F2 (2차) + G1·G2 (3차)
범위:
  - inline / angle / reference-style link 추출
  - file-relative path 정규화 (../../research/, ../research/)
  - root-relative path /research/ (G2)
  - indented reference definition (G1)
  - fragment, query, scheme (URL, mailto)
  - code block 안의 링크는 무시
  - frontmatter citation_status 검사

사용:
  python3 tools/test_validate_research_isolation.py
  → exit 0 모두 통과 / exit 1 실패
"""
from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location(
    "vri", HERE / "validate-research-isolation.py"
)
assert SPEC and SPEC.loader
vri = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(vri)  # type: ignore[union-attr]


# (filepath, content, expected_violators[], description)
LINK_CASES: list[tuple[str, str, list[str], str]] = [
    # ===== 기본 inline link =====
    (
        "concepts/tides/01-concept.md",
        "[x](../../research/inbox/foo.md)",
        ["../../research/inbox/foo.md"],
        "nested inline link to ../../research/",
    ),
    (
        "models/ADCIRC/source-analysis/foo.md",
        "[x](../../../research/digests/bar.md)",
        ["../../../research/digests/bar.md"],
        "deep nested inline link",
    ),
    (
        "concepts/foo.md",
        "[x](../research/inbox/x.md)",
        ["../research/inbox/x.md"],
        "one-level up inline link",
    ),
    # ===== Angle link =====
    (
        "concepts/foo.md",
        "<../research/x.md>",
        ["../research/x.md"],
        "angle link to research/",
    ),
    # ===== Reference-style definitions =====
    (
        "concepts/foo.md",
        "[ref]: ../research/inbox/x.md\n",
        ["../research/inbox/x.md"],
        "reference def, no indent",
    ),
    (
        "concepts/tides/notes.md",
        "   [draft]: ../../research/inbox/a.md\n",
        ["../../research/inbox/a.md"],
        "G1: 3-space indented reference def (2-level path)",
    ),
    (
        "concepts/foo.md",
        " [x]: ../research/y.md\n",
        ["../research/y.md"],
        "G1: 1-space indented reference def",
    ),
    (
        "concepts/foo.md",
        "\t[x]: ../research/y.md\n",
        [],
        "H2: tab-indented → CommonMark column expand 시 4+ col = code block, refdef 아님",
    ),
    (
        "concepts/foo.md",
        "    [x]: ../research/y.md\n",
        [],
        "G1: 4-space indent → CommonMark 는 code block 으로 해석, refdef 아님 (false positive 방지)",
    ),
    # ===== H1: no-space after colon =====
    # (filepath depth-1: ../research/ → root research/)
    (
        "concepts/foo.md",
        "[r]:../research/inbox/x.md\n",
        ["../research/inbox/x.md"],
        "H1: refdef with NO whitespace after colon (CommonMark 허용)",
    ),
    (
        "concepts/foo.md",
        "[r]:\t../research/inbox/x.md\n",
        ["../research/inbox/x.md"],
        "H1: refdef with tab after colon",
    ),
    # ===== H3: raw HTML href/src =====
    (
        "concepts/foo.md",
        '<a href="../research/inbox/x.md">draft</a>',
        ["../research/inbox/x.md"],
        "H3: raw HTML <a href> double-quoted",
    ),
    (
        "concepts/foo.md",
        "<a href='../research/inbox/x.md'>draft</a>",
        ["../research/inbox/x.md"],
        "H3: raw HTML <a href> single-quoted",
    ),
    (
        "concepts/tides/notes.md",
        '<img src="/research/foo.png" alt="x">',
        ["/research/foo.png"],
        "H3: raw HTML <img src> root-relative (depth 무관)",
    ),
    (
        "concepts/foo.md",
        '<A HREF="../research/inbox/x.md">draft</A>',
        ["../research/inbox/x.md"],
        "H3: raw HTML uppercase tag/attribute",
    ),
    (
        "concepts/foo.md",
        '<a href="https://research.example.com/x">ext</a>',
        [],
        "H3: raw HTML with external URL — skip",
    ),
    (
        "concepts/foo.md",
        "`<a href=\"../research/inbox/x.md\">x</a>`",
        [],
        "H3: HTML inside inline code — ignored",
    ),
    # ===== Root-relative (G2) =====
    (
        "concepts/foo.md",
        "[x](/research/inbox/a.md)",
        ["/research/inbox/a.md"],
        "G2: root-relative inline link",
    ),
    (
        "models/ADCIRC/source-analysis/deep/note.md",
        "[x](/research/digests/2026-W21.md)",
        ["/research/digests/2026-W21.md"],
        "G2: root-relative from deep nested path",
    ),
    (
        "concepts/foo.md",
        "[r]: /research/x.md\n",
        ["/research/x.md"],
        "G2: root-relative reference def",
    ),
    # ===== Negative cases =====
    (
        "concepts/foo.md",
        "[x](https://research.example.com/x)",
        [],
        "URL with research in domain",
    ),
    (
        "concepts/foo.md",
        "[x](mailto:research@example.com)",
        [],
        "mailto scheme",
    ),
    (
        "concepts/foo.md",
        "[x](research-grade-tool.md)",
        [],
        "filename starts with research- (not research/)",
    ),
    (
        "concepts/foo.md",
        "[x](concepts/research-methods.md)",
        [],
        "research-methods.md inside concepts (not the research/ workbench)",
    ),
    (
        "concepts/foo.md",
        "`[x](../research/x.md)`",
        [],
        "inline code — link inside backticks ignored",
    ),
    (
        "concepts/foo.md",
        "```\n[x](../research/x.md)\n```\n",
        [],
        "fenced code block — links inside ignored",
    ),
    (
        "concepts/foo.md",
        "[x](../research/inbox/x.md#section)",
        ["../research/inbox/x.md#section"],
        "link with fragment — still detected",
    ),
    (
        "concepts/foo.md",
        "[x](../research/inbox/x.md?v=1)",
        ["../research/inbox/x.md?v=1"],
        "link with query — still detected",
    ),
    # ===== I1: multi-line reference definition (CommonMark 0.31.2) =====
    (
        "concepts/foo.md",
        "[r]:\n  ../research/inbox/x.md\n",
        ["../research/inbox/x.md"],
        "I1: refdef destination on next line",
    ),
    (
        "concepts/foo.md",
        "[r]:\n\t../research/inbox/x.md\n",
        ["../research/inbox/x.md"],
        "I1: refdef destination on next line with tab indent",
    ),
    (
        "concepts/foo.md",
        "[r]:\n\n../research/inbox/x.md\n",
        [],
        "I1: refdef with BLANK line → invalid refdef (allow only single line ending)",
    ),
    # ===== I2: unquoted HTML attributes =====
    (
        "concepts/foo.md",
        "<a href=../research/inbox/x.md>draft</a>",
        ["../research/inbox/x.md"],
        "I2: unquoted href",
    ),
    (
        "concepts/foo.md",
        "<img src=/research/foo.png alt=x>",
        ["/research/foo.png"],
        "I2: unquoted src with root-relative path",
    ),
    (
        "concepts/foo.md",
        "<A HREF=../research/inbox/x.md>draft</A>",
        ["../research/inbox/x.md"],
        "I2: uppercase unquoted",
    ),
    # ===== I2: data-href / x-href false positive 차단 =====
    (
        "concepts/foo.md",
        '<div data-href="../research/inbox/x.md">x</div>',
        [],
        "I2: data-href 는 navigation attr 아님 → false positive 차단",
    ),
    (
        "concepts/foo.md",
        '<div data-src="../research/inbox/x.png">x</div>',
        [],
        "I2: data-src 도 차단",
    ),
    (
        "concepts/foo.md",
        '<custom x-href="../research/inbox/x.md">x</custom>',
        [],
        "I2: x-href 같은 prefix 도 차단 (word boundary)",
    ),
    # ===== boundary: filepath that itself sits in research/ doesn't matter for body-check
    # since validator filters by TARGET_ROOTS first =====
]


# (filepath, content, expected_has_draft_unsourced, description)
FM_CASES: list[tuple[str, str, bool, str]] = [
    (
        "research/inbox/x.md",
        "---\ncitation_status: draft-unsourced\n---\nbody",
        True,
        "frontmatter with draft-unsourced",
    ),
    (
        "research/inbox/x.md",
        "---\ncitation_status: verified\n---\nbody",
        False,
        "frontmatter with verified (violation)",
    ),
    (
        "research/inbox/x.md",
        "body only, no frontmatter",
        False,
        "no frontmatter (violation)",
    ),
    (
        "research/inbox/x.md",
        "---\ntitle: foo\ncitation_status: draft-unsourced\norigin: hermes\n---\nbody",
        True,
        "frontmatter with multiple fields",
    ),
    (
        "research/inbox/x.md",
        "---\ntitle: foo\n---\nbody",
        False,
        "frontmatter without citation_status",
    ),
]


def run_link_tests() -> tuple[int, int]:
    passed = failed = 0
    for filepath, content, expected, desc in LINK_CASES:
        targets = vri.extract_link_targets(content)
        hits = [t for t in targets if vri.target_resolves_into_research(t, filepath)]
        if hits == expected:
            passed += 1
        else:
            failed += 1
            print(f"  FAIL [link] {desc}")
            print(f"    file:     {filepath}")
            print(f"    content:  {content!r}")
            print(f"    expected: {expected}")
            print(f"    got:      {hits}")
            print(f"    targets:  {targets}")
    return passed, failed


def run_fm_tests() -> tuple[int, int]:
    passed = failed = 0
    for filepath, content, expected, desc in FM_CASES:
        got = vri.has_draft_unsourced(content)
        if got == expected:
            passed += 1
        else:
            failed += 1
            print(f"  FAIL [fm] {desc}")
            print(f"    file:     {filepath}")
            print(f"    content:  {content!r}")
            print(f"    expected: {expected}")
            print(f"    got:      {got}")
    return passed, failed


def main() -> int:
    print("[link tests]")
    lp, lf = run_link_tests()
    print(f"  {lp} passed, {lf} failed")

    print("[frontmatter tests]")
    fp, ff = run_fm_tests()
    print(f"  {fp} passed, {ff} failed")

    total_failed = lf + ff
    total_passed = lp + fp
    print()
    if total_failed == 0:
        print(f"ALL {total_passed} TESTS PASS")
        return 0
    print(f"FAIL: {total_failed} of {total_passed + total_failed} tests failed")
    return 1


if __name__ == "__main__":
    sys.exit(main())
