#!/usr/bin/env python3
"""test_validate_canonical_hygiene.py — G8 validator 회귀 fixture.

순수 함수(find_local_paths·find_placeholders·is_exempt) 단위 테스트.
dependency-0, repo 상태 불필요.

실행: python3 tools/test_validate_canonical_hygiene.py
"""
from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path

_spec = importlib.util.spec_from_file_location(
    "vch", Path(__file__).resolve().parent / "validate-canonical-hygiene.py"
)
vch = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(vch)


class TestG8bPaths(unittest.TestCase):
    def _kinds(self, line: str) -> set[str]:
        return {kind for _, kind, _ in vch.find_local_paths(line)}

    # --- 위반 (작성자 로컬) ---
    def test_win_drive_single_backslash(self):
        self.assertIn("win-drive", self._kinds(r"파일: D:\Numerical_models\x.csv"))

    def test_win_drive_double_backslash(self):
        self.assertIn("win-drive", self._kinds(r'"E:\\KHOA_연간백서\\markdowns\\R.md 인용"'))

    def test_wsl_mount(self):
        self.assertIn("wsl-mount", self._kinds("load /mnt/e/models/swan/src"))

    def test_home(self):
        self.assertIn("home", self._kinds("see ~/.hermes/skills/x"))
        self.assertIn("home", self._kinds("cd ~/coastal-wiki/data"))

    def test_wsl_unc(self):
        self.assertIn("wsl-unc", self._kinds(r"\\wsl$\Ubuntu\home"))

    # --- 비위반 (vendor / generic / repo-상대) ---
    def test_vendor_program_files_ok(self):
        self.assertEqual(self._kinds(r'"C:\Program Files\swan\bin"'), set())

    def test_vendor_windows_ok(self):
        self.assertEqual(self._kinds(r"C:\Windows\system32"), set())

    def test_manual_placeholder_path_to_ok(self):
        self.assertEqual(self._kinds(r'CD "C:\Path\To\WorkingDirectory\"'), set())

    def test_repo_relative_file_line_ok(self):
        self.assertEqual(
            self._kinds("models/ADCIRC/raw/source_code/adcirc/src/gwce.F:2003"), set()
        )

    def test_unix_vendor_install_ok(self):
        # /opt, /usr 는 forbidden 패턴 자체에 없음
        self.assertEqual(self._kinds("install to /opt/swan or /usr/local/bin"), set())

    def test_plain_prose_ok(self):
        self.assertEqual(self._kinds("the storm-surge/·tide/ subdir 분석"), set())


class TestG8dPlaceholders(unittest.TestCase):
    def _hit(self, line: str) -> bool:
        return bool(vch.find_placeholders(line))

    # --- 위반 ---
    def test_user_experience_cases_direct(self):
        self.assertTrue(self._hit("- ▢ User-experience cases — placeholder."))

    def test_user_experience_cases_korean_label(self):
        self.assertTrue(self._hit("**User experience cases (to be filled):**"))

    def test_checkbox_plus_personal_case(self):
        self.assertTrue(self._hit("- ▢ 개인 사례: 어느 항만에서 무엇을 관찰했는가 채워 넣기"))

    def test_lead_modeler_fill(self):
        self.assertTrue(
            self._hit("to be filled by the lead modeler from project memory: run result")
        )

    # --- 비위반 ---
    def test_source_needed_stub_ok(self):
        self.assertFalse(self._hit("- (예정) source-needed: 공식 인용 확보 후 작성"))

    def test_plain_todo_ok(self):
        self.assertFalse(self._hit("## Next expansion candidates"))

    def test_objective_heading_ok(self):
        self.assertFalse(self._hit("- ▢ NWS=8 parametric vortex 보강 (source-code)"))


class TestExemptions(unittest.TestCase):
    def test_textbook_md_exempt(self):
        self.assertTrue(vch.is_exempt("textbook/md/Stewart.md"))

    def test_raw_exempt(self):
        self.assertTrue(vch.is_exempt("models/ADCIRC/raw/source_code/x.md"))

    def test_template_exempt(self):
        self.assertTrue(vch.is_exempt("concepts/_template/01-concept.md"))

    def test_governance_policy_index_exempt(self):
        self.assertTrue(vch.is_exempt("textbook/POLICY.md"))
        self.assertTrue(vch.is_exempt("textbook/INDEX.md"))

    def test_canonical_note_not_exempt(self):
        self.assertFalse(vch.is_exempt("concepts/tides/02-theory.md"))
        self.assertFalse(vch.is_exempt("models/EFDC/manifest.md"))


if __name__ == "__main__":
    unittest.main(verbosity=2)
