#!/usr/bin/env python3
"""test_validate_link_integrity.py — 링크 무결성 validator 회귀 fixture.

check_file 순수 로직 단위 테스트 (wikilink stem 해석·intentional 마커·코드 스킵·상대링크).
mdlink 존재 검사는 repo 실제 파일(CLAUDE.md / 없는 파일)로 확인.

실행: python3 tools/test_validate_link_integrity.py
"""
from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path

_spec = importlib.util.spec_from_file_location(
    "vli", Path(__file__).resolve().parent / "validate-link-integrity.py"
)
vli = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(vli)

STEMS = {"swan-tech-ch6-iterative-solvers", "delft3d_sediment", "01-concept", "CLAUDE"}


class TestWikilinks(unittest.TestCase):
    def _wiki(self, line: str, path="models/X/note.md"):
        _, bw = vli.check_file(path, line, STEMS)
        return [t for _, t in bw]

    def test_resolves_by_basename(self):
        self.assertEqual(self._wiki("see [[swan-tech-ch6-iterative-solvers]]"), [])

    def test_resolves_path_form(self):
        self.assertEqual(self._wiki("see [[../source-analysis/sediment/delft3d_sediment]]"), [])

    def test_broken_wikilink_flagged(self):
        self.assertEqual(self._wiki("see [[no-such-note]]"), ["no-such-note"])

    def test_glob_skipped(self):
        self.assertEqual(self._wiki("모든 [[swan-*-implementation]] 참조"), [])

    def test_intentional_marker_skipped(self):
        self.assertEqual(self._wiki("- [[khoa-tide-surge-coupling]] (예정) — 검증"), [])

    def test_inline_code_skipped(self):
        # `[[i]]` 는 inline code → 스킵
        self.assertEqual(self._wiki("복원용(`[[i]]` 배열 인덱스)"), [])

    def test_alias_pipe_uses_left(self):
        self.assertEqual(self._wiki("[[no-such-note|표시명]]"), ["no-such-note"])


class TestMdLinks(unittest.TestCase):
    def _md(self, line: str, path="CONVENTIONS.md"):
        bm, _ = vli.check_file(path, line, STEMS)
        return [t for _, t in bm]

    def test_existing_relative_ok(self):
        # CONVENTIONS.md 기준 CLAUDE.md 는 실존
        self.assertEqual(self._md("[entry](CLAUDE.md)"), [])

    def test_missing_relative_flagged(self):
        self.assertEqual(self._md("[x](nonexistent-xyz.md)"), ["nonexistent-xyz.md"])

    def test_intentional_marker_skipped(self):
        self.assertEqual(self._md("[x](future-note.md) (예정)"), [])

    def test_url_skipped(self):
        self.assertEqual(self._md("[doc](https://example.com/x.md)"), [])

    def test_anchor_stripped(self):
        self.assertEqual(self._md("[s](CLAUDE.md#section)"), [])


class TestScopeHelpers(unittest.TestCase):
    def test_scan_exempt_textbook_md(self):
        self.assertTrue(vli.scan_exempt("textbook/md/Stewart.md"))

    def test_scan_exempt_raw(self):
        self.assertTrue(vli.scan_exempt("models/X/raw/source_code/y.md"))

    def test_authored_note_not_exempt(self):
        self.assertFalse(vli.scan_exempt("concepts/tides/02-theory.md"))

    def test_under_authored(self):
        self.assertTrue(vli.under_authored("textbook/notes/x.md"))
        self.assertFalse(vli.under_authored("textbook/md/x.md"))


if __name__ == "__main__":
    unittest.main(verbosity=2)
