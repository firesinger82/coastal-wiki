#!/usr/bin/env python3
"""test_validate_layer_deps.py — 4-레이어 lint 회귀 fixture (F-2, 2026-07-12).

단위: parse_frontmatter(인라인/리스트 depends_on·malformed)·MANDATORY_RE·infer_layer 휴리스틱.
통합: 임시 git repo 에서 staged 모드 — 정상/상향 의존/대상 부재/'..'/전용 경로 필드 누락/순환/
      scope guard(HEAD 기준 + escape).

실행: python3 tools/test_validate_layer_deps.py
"""
from __future__ import annotations

import importlib.util
import os
import subprocess
import tempfile
import unittest
from pathlib import Path

TOOLS = Path(__file__).resolve().parent
_spec = importlib.util.spec_from_file_location("vld", TOOLS / "validate-layer-deps.py")
vld = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(vld)


class TestParser(unittest.TestCase):
    def test_layer_and_status(self):
        fm = vld.parse_frontmatter("---\nlayer: 3\ncitation_status: verified\n---\nx")
        self.assertEqual(fm["layer"], 3)
        self.assertEqual(fm["citation_status"], "verified")

    def test_depends_inline_empty(self):
        fm = vld.parse_frontmatter("---\nlayer: 1\ndepends_on: []\n---\nx")
        self.assertTrue(fm["has_depends_key"])
        self.assertEqual(fm["depends_on"], [])

    def test_depends_inline_list(self):
        fm = vld.parse_frontmatter("---\nlayer: 4\ndepends_on: [a.md, b.md]\n---\nx")
        self.assertEqual(fm["depends_on"], ["a.md", "b.md"])

    def test_depends_block_list(self):
        fm = vld.parse_frontmatter("---\nlayer: 4\ndepends_on:\n  - a.md\n  - b.md\n---\nx")
        self.assertTrue(fm["has_depends_key"])
        self.assertEqual(fm["depends_on"], ["a.md", "b.md"])

    def test_malformed_no_frontmatter(self):
        fm = vld.parse_frontmatter("plain text")
        self.assertIsNone(fm["layer"])
        self.assertFalse(fm["has_depends_key"])

    def test_malformed_unclosed(self):
        fm = vld.parse_frontmatter("---\nlayer: 2\nno end")
        self.assertIsNone(fm["layer"])

    def test_invalid_layer_value_ignored(self):
        fm = vld.parse_frontmatter("---\nlayer: 7\n---\nx")
        self.assertIsNone(fm["layer"])  # 1-4 외 = 미인식 (opt-in 불성립)


class TestMandatoryAndHeuristics(unittest.TestCase):
    def test_mandatory_paths(self):
        self.assertTrue(vld.MANDATORY_RE.match("textbook/notes/theory-ch08-x.md"))
        self.assertTrue(vld.MANDATORY_RE.match("concepts/waves/09-applied-y.md"))
        self.assertFalse(vld.MANDATORY_RE.match("concepts/waves/01-concept.md"))
        self.assertFalse(vld.MANDATORY_RE.match("models/SWAN/source-analysis/x.md"))

    def test_infer_layer_paths(self):
        self.assertEqual(vld.infer_layer("models/SWAN/source-analysis/nope-x.md", False), 2)
        self.assertEqual(vld.infer_layer("examples/foo/nope.md", False), 3)
        self.assertEqual(vld.infer_layer("experience/nope.md", False), "experience")
        self.assertEqual(vld.infer_layer("concepts/waves/12-applied-nope.md", False), 4)
        self.assertEqual(vld.infer_layer("textbook/notes/theory-ch99-nope.md", False), 1)
        self.assertIsNone(vld.infer_layer("concepts/waves/01-concept.md", False))


def _run(repo, staged=True, env_extra=None):
    env = dict(os.environ)
    if env_extra:
        env.update(env_extra)
    args = ["python3", str(TOOLS / "validate-layer-deps.py")]
    if staged:
        args.append("--staged")
    r = subprocess.run(args, cwd=repo, env=env, capture_output=True, text=True)
    return r.returncode, r.stdout + r.stderr


class TestIntegration(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.repo = self.tmp.name
        for cmd in (["git", "init", "-q"],
                    ["git", "config", "user.email", "t@t"],
                    ["git", "config", "user.name", "t"]):
            subprocess.run(cmd, cwd=self.repo, check=True)
        self._write("models/M/source-analysis/base.md", "---\ntitle: b\n---\nx")
        self._commit("init")

    def tearDown(self):
        self.tmp.cleanup()

    def _write(self, rel, content):
        p = Path(self.repo) / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(content, encoding="utf-8")

    def _stage(self, rel):
        subprocess.run(["git", "add", rel], cwd=self.repo, check=True)

    def _commit(self, msg):
        subprocess.run(["git", "add", "-A"], cwd=self.repo, check=True)
        subprocess.run(["git", "commit", "-qm", msg], cwd=self.repo, check=True)

    def test_ok_downward_dep(self):
        self._write("concepts/t/09-applied-a.md",
                    "---\nlayer: 4\ndepends_on:\n  - models/M/source-analysis/base.md\n---\nx")
        self._stage("concepts/t/09-applied-a.md")
        rc, out = _run(self.repo)
        self.assertEqual(rc, 0, out)

    def test_upward_dep_fails(self):
        self._write("concepts/t/09-applied-a.md", "---\nlayer: 4\ndepends_on: []\n---\nx")
        self._commit("l4")
        self._write("textbook/notes/theory-ch01-a.md",
                    "---\nlayer: 1\ndepends_on:\n  - concepts/t/09-applied-a.md\n---\nx")
        self._stage("textbook/notes/theory-ch01-a.md")
        rc, out = _run(self.repo)
        self.assertEqual(rc, 1, out)
        self.assertIn("상위 레이어", out)

    def test_missing_target_fails(self):
        self._write("textbook/notes/theory-ch01-a.md",
                    "---\nlayer: 1\ndepends_on:\n  - textbook/notes/ghost.md\n---\nx")
        self._stage("textbook/notes/theory-ch01-a.md")
        rc, out = _run(self.repo)
        self.assertEqual(rc, 1, out)
        self.assertIn("존재하지 않음", out)

    def test_dotdot_rejected(self):
        self._write("textbook/notes/theory-ch01-a.md",
                    "---\nlayer: 1\ndepends_on:\n  - ../outside.md\n---\nx")
        self._stage("textbook/notes/theory-ch01-a.md")
        rc, out = _run(self.repo)
        self.assertEqual(rc, 1, out)
        self.assertIn("'..'", out)

    def test_mandatory_path_missing_layer_fails(self):
        self._write("textbook/notes/theory-ch01-a.md", "---\ntitle: t\n---\nx")
        self._stage("textbook/notes/theory-ch01-a.md")
        rc, out = _run(self.repo)
        self.assertEqual(rc, 1, out)
        self.assertIn("layer", out)

    def test_same_layer_dep_allowed_but_cycle_fails(self):
        self._write("textbook/notes/theory-ch01-a.md",
                    "---\nlayer: 1\ndepends_on:\n  - textbook/notes/theory-ch02-b.md\n---\nx")
        self._write("textbook/notes/theory-ch02-b.md",
                    "---\nlayer: 1\ndepends_on: []\n---\nx")
        self._stage("textbook/notes/theory-ch01-a.md")
        self._stage("textbook/notes/theory-ch02-b.md")
        rc, out = _run(self.repo)
        self.assertEqual(rc, 0, out)  # 동일 layer 유도 의존 허용 (F-3)
        # 순환으로 전환
        self._write("textbook/notes/theory-ch02-b.md",
                    "---\nlayer: 1\ndepends_on:\n  - textbook/notes/theory-ch01-a.md\n---\nx")
        self._stage("textbook/notes/theory-ch02-b.md")
        rc, out = _run(self.repo)
        self.assertEqual(rc, 1, out)
        self.assertIn("순환", out)

    def test_scope_guard_head_based(self):
        self._write("concepts/t/old.md",
                    "---\ncitation_status: verified\n---\noriginal")
        self._commit("verified base")
        # 같은 커밋에서 verified 파일 수정(+layer 추가 우회 시도) + layer 파일 신설
        self._write("concepts/t/old.md",
                    "---\nlayer: 3\ncitation_status: verified\n---\nmodified")
        self._write("textbook/notes/theory-ch01-a.md",
                    "---\nlayer: 1\ndepends_on: []\n---\nx")
        self._stage("concepts/t/old.md")
        self._stage("textbook/notes/theory-ch01-a.md")
        rc, out = _run(self.repo)
        self.assertEqual(rc, 1, out)
        self.assertIn("scope guard", out)
        # escape hatch
        rc, out = _run(self.repo, env_extra={"COASTAL_WIKI_SKIP_LAYER_GUARD": "1"})
        self.assertEqual(rc, 0, out)
        self.assertIn("SKIP", out)


if __name__ == "__main__":
    unittest.main(verbosity=1)
