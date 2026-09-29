#!/usr/bin/env python3
"""validate-experience-numbers.py 회귀·단위 테스트 (v2 설계)."""
from __future__ import annotations

import importlib.util
import os
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path
import sys

TOOLS = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("ven", TOOLS / "validate-experience-numbers.py")
ven = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = ven
spec.loader.exec_module(ven)


class TestBlocksAndTokens(unittest.TestCase):
    names = {"note", "other"}

    def warn(self, text):
        return ven.scan("concepts/x/01-concept.md", text, self.names)

    def test_table_row_and_header_unit_inheritance(self):
        out = self.warn("""표:
| 항목 | rate (mm/yr) |
|---|---|
| A | 3.94 |
| B | 2020-2025 |

전체 분석: [experience/note.md](../../experience/note.md)
""")
        self.assertEqual(len(out), 1)
        self.assertIn("3.94", out[0])

    def test_intro_list_and_source_marker(self):
        self.assertTrue(self.warn("""자료:
- 사례 1: 20%
- 출처: experience/note.md
"""))
        self.assertTrue(self.warn("""결과: experience/note.md
요약 결과는 2배이다.
"""))

    def test_sibling_attribution_needs_source_mark(self):
        # 2026-09-29 오탐: 다음 항목이 탐색용 링크거나 검증 표지가 없으면 앞 항목에 귀속하지 않는다.
        self.assertFalse(self.warn("""- 포항 누년 +36 cm (KHOA 표 3-259)
- 설계 사례는 [[note]]를 탐색용으로 참조한다.
"""))
        self.assertFalse(self.warn("""- Rossby radius (~30-40 km)
- 다층 관측 활용 — [[note]] 의 상관도 modeling 가능
"""))
        self.assertTrue(self.warn("""- 정밀도는 ±11.25° 다(약 20% 성분 오차).
- 규약은 데이터로 검증했다: [experience/note.md](../../experience/note.md) @ `20bc544`
"""))

    def test_suppression_requires_reason(self):
        self.assertFalse(self.warn("[experience/note.md](x) 20% <!-- exp-num-ok: 독립 보고서 -->"))
        self.assertTrue(self.warn("[experience/note.md](x) 20% <!-- exp-num-ok: -->"))

    def test_layer4_and_applied_excluded(self):
        text = "---\nlayer: 4\n---\n[experience/note.md](x) 20%"
        self.assertFalse(ven.scan("concepts/x/01-concept.md", text, self.names))
        self.assertFalse(ven.scan("concepts/x/07-applied-case.md", "[experience/note.md](x) 20%", self.names))

    def test_exclusions_and_formula(self):
        out = self.warn("[experience/note.md](x) 2025, §3, line 12, :44, `20%`, R²=0.81, $x=3.94$ mm/yr")
        self.assertEqual(len(out), 1)
        self.assertIn("3.94", out[0])
        self.assertNotIn("2025,", ", ".join(ven.numeric_tokens(ven.blocks("[experience/note.md](x) 2025, §3, line 12, :44, `20%`, R²=0.81, $x=3.94$ mm/yr", self.names)[0])))

    def test_wikilink_local_resolution(self):
        self.assertTrue(self.warn("[[note]] 3중일치"))
        self.assertFalse(ven.scan("concepts/x/a.md", "[[README]] 20%", {"note"}))

    def test_frontmatter_field_only(self):
        text = "---\nverification_method: experience/note.md\nrelated: experience/other.md\n---\n본문"
        out = ven.scan("concepts/x/a.md", text, self.names)
        self.assertEqual(len(out), 1)
        self.assertIn("frontmatter", out[0])


class TestStaged(unittest.TestCase):
    def test_index_content_and_partial_staging(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            subprocess.run(["git", "init", "-q"], cwd=root, check=True)
            subprocess.run(["git", "config", "user.email", "t@t"], cwd=root, check=True)
            subprocess.run(["git", "config", "user.name", "t"], cwd=root, check=True)
            (root / "tools").mkdir()
            shutil.copy(TOOLS / "validate-experience-numbers.py", root / "tools")
            (root / "experience").mkdir()
            (root / "experience/note.md").write_text("# note\n")
            p = root / "concepts/x.md"
            p.parent.mkdir()
            p.write_text("[experience/note.md](x) 20%\n")
            subprocess.run(["git", "add", "experience/note.md", "concepts/x.md"], cwd=root, check=True)
            p.write_text("[experience/note.md](x) 20%\n")
            r = subprocess.run(["python3", "tools/validate-experience-numbers.py", "--staged"], cwd=root, capture_output=True, text=True)
            self.assertEqual(r.returncode, 0)
            self.assertIn("20%", r.stdout)


if __name__ == "__main__":
    unittest.main(verbosity=1)
