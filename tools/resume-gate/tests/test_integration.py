#!/usr/bin/env python3
"""Non-installing phase-7 integration tests for resume-gate.

All mutable state is created below a TemporaryDirectory.  The suite copies the
installed ``lib/`` and ``bin/`` shape into that tree, injects mock judges, and
never invokes Claude, Codex, Grok, sudo, or a network client.

Run:
  PYTHONDONTWRITEBYTECODE=1 .venv/bin/python \
    tools/resume-gate/tests/test_integration.py
"""
from __future__ import annotations

import copy
import hashlib
import importlib.util
import inspect
import json
import os
import pathlib
import shutil
import stat
import subprocess
import sys
import tempfile
from collections.abc import Iterator, Mapping
from contextlib import contextmanager
from dataclasses import dataclass
from typing import Any, Callable


sys.dont_write_bytecode = True

GATE_ROOT = pathlib.Path(__file__).resolve().parents[1]
REPO_ROOT = GATE_ROOT.parents[1]
SOURCE_BIN = GATE_ROOT / "bin"
SOURCE_SCHEMAS = GATE_ROOT / "schemas"
SOURCE_ENGINE = GATE_ROOT / "engine"
SOURCE_JUDGE = GATE_ROOT / "judge"
SOURCE_VALIDATOR = GATE_ROOT / "validator"
POLICY_PATH = GATE_ROOT / "policy" / "50-coastal-resume.json"
RUN_ID = "integration-run-0001"
CANARY_RUN_ID = "integration-control-canary-001"
ZERO_HASH = "0" * 64

_BASELINE_GIT: bytes | None = None
_BASELINE_MODE: tuple[tuple[str, int, int, int, str | None], ...] | None = None


def criteria(*identifiers: str) -> Callable[[Callable[..., None]], Callable[..., None]]:
    def decorate(function: Callable[..., None]) -> Callable[..., None]:
        setattr(function, "criteria", identifiers)
        return function

    return decorate


def sha256_bytes(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def sha256_file(path: pathlib.Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def write_json(path: pathlib.Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2) + "\n",
        encoding="utf-8",
    )


def load_json(path: pathlib.Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    assert isinstance(value, dict)
    return value


def write_minimal_pdf(path: pathlib.Path, text: str) -> None:
    """Write a one-page PDF whose text is extractable by pdftotext."""

    stream = f"BT /F1 12 Tf 72 720 Td ({text}) Tj ET".encode("ascii")
    objects = [
        b"<< /Type /Catalog /Pages 2 0 R >>",
        b"<< /Type /Pages /Kids [3 0 R] /Count 1 >>",
        (
            b"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 612 792] "
            b"/Resources << /Font << /F1 5 0 R >> >> /Contents 4 0 R >>"
        ),
        b"<< /Length " + str(len(stream)).encode("ascii") + b" >>\nstream\n"
        + stream
        + b"\nendstream",
        b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>",
    ]
    raw = bytearray(b"%PDF-1.4\n%\xe2\xe3\xcf\xd3\n")
    offsets = [0]
    for index, body in enumerate(objects, start=1):
        offsets.append(len(raw))
        raw.extend(f"{index} 0 obj\n".encode("ascii"))
        raw.extend(body)
        raw.extend(b"\nendobj\n")
    xref = len(raw)
    raw.extend(f"xref\n0 {len(objects) + 1}\n".encode("ascii"))
    raw.extend(b"0000000000 65535 f \n")
    for offset in offsets[1:]:
        raw.extend(f"{offset:010d} 00000 n \n".encode("ascii"))
    raw.extend(
        (
            f"trailer\n<< /Size {len(objects) + 1} /Root 1 0 R >>\n"
            f"startxref\n{xref}\n%%EOF\n"
        ).encode("ascii")
    )
    path.write_bytes(bytes(raw))


def load_module(name: str, path: pathlib.Path) -> Any:
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


@dataclass
class Layout:
    root: pathlib.Path
    repo: pathlib.Path
    lib: pathlib.Path
    bin: pathlib.Path
    state: pathlib.Path
    empty: pathlib.Path
    manifest_path: pathlib.Path
    canary_path: pathlib.Path
    parser_negative_path: pathlib.Path
    core: Any
    validator: Any
    adapter: Any


def _copy_install_payload(root: pathlib.Path) -> tuple[pathlib.Path, pathlib.Path]:
    lib = root / "opt-simulation" / "coastal-resume" / "lib"
    bin_dir = root / "opt-simulation" / "coastal-resume" / "bin"
    for directory in (
        lib / "engine",
        lib / "judge",
        lib / "validator",
        lib / "schemas",
        lib / "fixtures" / "pilot",
        bin_dir,
    ):
        directory.mkdir(parents=True, exist_ok=True)
    for source in SOURCE_ENGINE.glob("*.py"):
        shutil.copyfile(source, lib / "engine" / source.name)
    for source in SOURCE_JUDGE.glob("*"):
        if source.is_file():
            shutil.copyfile(source, lib / "judge" / source.name)
    shutil.copyfile(SOURCE_VALIDATOR / "validate.py", lib / "validator" / "validate.py")
    for source in SOURCE_SCHEMAS.glob("*.json"):
        shutil.copyfile(source, lib / "schemas" / source.name)
    for name in ("resume-pretool-guard", "resume-stop-gate", "resume-run"):
        shutil.copyfile(SOURCE_BIN / name, bin_dir / name)
    return lib, bin_dir


def _base_submission(manifest: dict[str, Any], manifest_hash: str) -> dict[str, Any]:
    return {
        "schema_version": 1,
        "contract_version": "resume-gate/1",
        "manifest": {
            "manifest_id": manifest["manifest_id"],
            "sha256": manifest_hash,
        },
        "run_id": CANARY_RUN_ID,
        "candidate": {
            "source_id": "code_one",
            "claim": "The bounded loop reaches 60.",
            "claim_type": "explicit",
        },
        "evidence": [
            {
                "locator": {"type": "line_range", "start": 2, "end": 2},
                "quote": "DO 48 ITS=1,30",
            }
        ],
        "attempt_reason": "fixed semantic canary",
    }


@contextmanager
def installed_layout() -> Iterator[Layout]:
    with tempfile.TemporaryDirectory(prefix="resume-gate-integration-") as temporary:
        root = pathlib.Path(temporary)
        lib, bin_dir = _copy_install_payload(root)
        repo = root / "repo"
        models = repo / "models"
        models.mkdir(parents=True)
        (models / "code-one.f90").write_text(
            "SUBROUTINE TEST\nDO 48 ITS=1,30\nEND\n",
            encoding="utf-8",
        )
        (models / "code-two.f90").write_text(
            "WRITE(LUQ) IQ_GEOM,IQ_DISP,IQ_GEOM\nEND\n",
            encoding="utf-8",
        )
        write_minimal_pdf(
            models / "manual.pdf",
            "Action density N equals E over sigma.",
        )
        outside = root / "outside.f90"
        outside.write_text("OUTSIDE SOURCE\n", encoding="utf-8")

        canary_path = lib / "fixtures" / "pilot" / "canary.json"
        parser_path = lib / "fixtures" / "pilot" / "parser-negative.json"
        parser_path.write_bytes(b'{"schema_version":1,"schema_version":1}\n')
        placeholder_manifest = {
            "manifest_id": "integration-manifest-001",
        }
        write_json(canary_path, _base_submission(placeholder_manifest, ZERO_HASH))

        locator_one = {"type": "line_range", "start": 2, "end": 2}
        locator_two = {"type": "line_range", "start": 1, "end": 1}
        locator_pdf = {"type": "page_range", "start": 1, "end": 1}
        execution_hash = sha256_file(lib / "validator" / "validate.py")
        manifest = {
            "schema_version": 1,
            "contract_version": "resume-gate/1",
            "manifest_id": "integration-manifest-001",
            "run_scope": "temporary phase-7 installed-layout integration fixture",
            "work_items": ["code_one", "code_two", "manual_pdf"],
            "sources": {
                "code_one": {
                    "path": "models/code-one.f90",
                    "sha256": sha256_file(models / "code-one.f90"),
                    "artifact_type": "code",
                    "locators": [locator_one],
                },
                "code_two": {
                    "path": "models/code-two.f90",
                    "sha256": sha256_file(models / "code-two.f90"),
                    "artifact_type": "code",
                    "locators": [locator_two],
                },
                "manual_pdf": {
                    "path": "models/manual.pdf",
                    "sha256": sha256_file(models / "manual.pdf"),
                    "artifact_type": "pdf",
                    "locators": [locator_pdf],
                },
            },
            "controls": {
                "canary": {
                    "control_id": "integration-canary-001",
                    "kind": "canary",
                    "source_id": "code_one",
                    "locator": locator_one,
                    "expected_status": "CAUGHT",
                    "allowed_failure_codes": ["CANARY_FABRICATED_CLAIM"],
                    "input_artifact_sha256": sha256_file(canary_path),
                    "execution_artifact_sha256": execution_hash,
                },
                "parser_negative": {
                    "control_id": "integration-parser-001",
                    "kind": "parser_negative",
                    "mutation": {
                        "mutation_id": "integration-duplicate-001",
                        "operation": "duplicate_key",
                        "target": "sources.code_one",
                    },
                    "expected_status": "REJECTED",
                    "allowed_failure_codes": ["JSON_DUPLICATE_KEY"],
                    "input_artifact_sha256": sha256_file(parser_path),
                    "execution_artifact_sha256": execution_hash,
                },
            },
        }
        validator = load_module(
            f"resume_gate_integration_validator_{id(root)}",
            lib / "validator" / "validate.py",
        )
        manifest_path = lib / "fixtures" / "pilot" / "manifest.frozen.json"
        write_json(manifest_path, manifest)
        core = load_module(
            f"resume_gate_integration_core_{id(root)}",
            lib / "engine" / "core.py",
        )
        adapter = load_module(
            f"resume_gate_integration_adapter_{id(root)}",
            lib / "judge" / "adapter.py",
        )
        empty = root / "opt-simulation" / "coastal-resume" / "empty"
        empty.mkdir()
        yield Layout(
            root=root,
            repo=repo,
            lib=lib,
            bin=bin_dir,
            state=root / "state",
            empty=empty,
            manifest_path=manifest_path,
            canary_path=canary_path,
            parser_negative_path=parser_path,
            core=core,
            validator=validator,
            adapter=adapter,
        )


class MockJudge:
    """Structured stage-4 boundary; no process, credential, or network access."""

    def __init__(
        self,
        core: Any,
        *,
        positive: Mapping[str, str] | None = None,
        canary: Mapping[str, str] | None = None,
        event_log: list[str] | None = None,
    ) -> None:
        self.core = core
        self.positive = dict(positive or {"codex": "PASS", "grok": "PASS"})
        self.canary = dict(canary or {"codex": "FAIL", "grok": "FAIL"})
        self.calls: list[tuple[str, str]] = []
        self.event_log = event_log

    def __call__(self, **kwargs: Any) -> dict[str, Any]:
        judge = kwargs["judge_name"]
        run_id = kwargs["launcher_run_id"]
        self.calls.append((run_id, judge))
        if self.event_log is not None:
            self.event_log.append(f"judge:{run_id}:{judge}")
        behavior = self.canary[judge] if run_id == CANARY_RUN_ID else self.positive[judge]
        if behavior == "timeout":
            raise TimeoutError("mock judge timeout")
        if behavior == "invalid_json":
            return {
                "status": "FAIL",
                "failure": {"code": "CLI_OUTPUT_INVALID", "detail": "mock invalid JSON"},
            }

        submission, submission_issues = self.core.deterministic.strict_json_load_path(
            kwargs["submission_path"], "mock submission"
        )
        manifest, manifest_issues = self.core.deterministic.strict_json_load_path(
            kwargs["manifest_path"], "mock manifest"
        )
        assert not submission_issues and isinstance(submission, dict)
        assert not manifest_issues and isinstance(manifest, dict)
        result = {
            "schema_version": 1,
            "contract_version": "resume-gate/1",
            "manifest": {
                "manifest_id": manifest["manifest_id"],
                "sha256": self.core.deterministic.jcs_sha256(manifest),
            },
            "submission_sha256": self.core.deterministic.jcs_sha256(submission),
            "judge": judge,
            "engine_version": f"mock-{judge}/integration-1",
            "verdict": behavior,
            "claim_supported_by_evidence": behavior == "PASS",
            "reasoning": f"{judge} independent mock rationale",
            "issues": [] if behavior == "PASS" else [f"mock {behavior.lower()}"],
        }
        return {"status": "VALIDATED", "judge_result": result}


def make_engine(
    layout: Layout,
    *,
    run_id: str = RUN_ID,
    judge: MockJudge | None = None,
    state_root: pathlib.Path | None = None,
    auto_start_controls: bool = True,
) -> tuple[Any, MockJudge]:
    selected = judge or MockJudge(layout.core)
    config = layout.core.EngineConfig(
        repo_root=layout.repo,
        manifest_path=layout.manifest_path,
        run_id=run_id,
        state_root=state_root or layout.state,
        schema_dir=layout.lib / "schemas",
        control_artifacts=layout.core.ControlArtifacts(
            canary_submission=layout.canary_path,
            parser_negative=layout.parser_negative_path,
            execution_artifact=layout.lib / "validator" / "validate.py",
        ),
        auto_start_controls=auto_start_controls,
    )
    return layout.core.ResumeGateEngine(config, selected), selected


def submission(
    layout: Layout,
    *,
    run_id: str = RUN_ID,
    source_id: str = "code_one",
    claim: str = "The loop is bounded at 30.",
    quote: str | None = None,
) -> dict[str, Any]:
    manifest = load_json(layout.manifest_path)
    values = {
        "code_one": (
            {"type": "line_range", "start": 2, "end": 2},
            "DO 48 ITS=1,30",
        ),
        "code_two": (
            {"type": "line_range", "start": 1, "end": 1},
            "WRITE(LUQ) IQ_GEOM,IQ_DISP,IQ_GEOM",
        ),
        "manual_pdf": (
            {"type": "page_range", "start": 1, "end": 1},
            "Action density N equals E over sigma.",
        ),
    }
    locator, default_quote = values[source_id]
    return {
        "schema_version": 1,
        "contract_version": "resume-gate/1",
        "manifest": {
            "manifest_id": manifest["manifest_id"],
            "sha256": layout.core.deterministic.jcs_sha256(manifest),
        },
        "run_id": run_id,
        "candidate": {
            "source_id": source_id,
            "claim": claim,
            "claim_type": "explicit",
        },
        "evidence": [{"locator": locator, "quote": quote or default_quote}],
        "attempt_reason": "phase-7 integration fixture",
    }


def hook_event(
    repo: pathlib.Path,
    tool_name: str,
    tool_input: dict[str, Any],
    *,
    event_name: str = "PreToolUse",
) -> dict[str, Any]:
    return {
        "session_id": "integration-session",
        "cwd": str(repo),
        "hook_event_name": event_name,
        "tool_name": tool_name,
        "tool_input": tool_input,
        "tool_use_id": "integration-tool-use",
    }


def run_script(
    script: pathlib.Path,
    event: dict[str, Any],
    environment: Mapping[str, str],
) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(script)],
        input=json.dumps(event),
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        env=dict(environment),
        timeout=20,
        check=False,
    )


def guard_environment(layout: Layout, run_id: str = RUN_ID) -> dict[str, str]:
    value = dict(os.environ)
    value.update(
        {
            "COASTAL_RESUME_REPO_ROOT": str(layout.repo),
            "COASTAL_RESUME_RUN_ID": run_id,
        }
    )
    return value


def stop_event() -> dict[str, Any]:
    return {
        "session_id": "integration-session",
        "cwd": str(REPO_ROOT),
        "hook_event_name": "Stop",
        "stop_hook_active": False,
        "last_assistant_message": "완료",
        "background_tasks": [],
        "session_crons": [],
    }


def stop_environment(layout: Layout, run_id: str = RUN_ID) -> dict[str, str]:
    value = dict(os.environ)
    value.update(
        {
            "COASTAL_RESUME_RUN_ID": run_id,
            "COASTAL_RESUME_STATE_ROOT": str(layout.state),
        }
    )
    return value


def validate_manifest_value(
    layout: Layout,
    value: dict[str, Any],
    *,
    pdf_runner: Callable[..., subprocess.CompletedProcess[bytes]] = subprocess.run,
) -> dict[str, Any]:
    path = layout.root / "case-manifest.json"
    write_json(path, value)
    result, _, _ = layout.validator.validate_manifest(
        path,
        layout.repo,
        schema_dir=layout.lib / "schemas",
        pdf_runner=pdf_runner,
    )
    return result


@criteria("§2-7", "§4.2-2", "§4.3-1")
def test_direct_writers_and_shell_write_bypasses_are_pretool_blocked() -> None:
    """§2 row 7; §4.2-2; §4.3-1 — every direct writer is pre-tool denied."""

    with installed_layout() as layout:
        sentinel = layout.root / "must-not-exist"
        attempts = [
            ("Write", {"file_path": str(sentinel), "content": "x"}),
            ("Edit", {"file_path": str(sentinel), "old_string": "", "new_string": "x"}),
            ("NotebookEdit", {"notebook_path": str(sentinel), "new_source": "x"}),
            ("Bash", {"command": f"printf x > {sentinel}"}),
            ("Bash", {"command": f"printf x | tee {sentinel}"}),
            (
                "Bash",
                {
                    "command": (
                        f"{sys.executable} -c "
                        f"\"open({str(sentinel)!r},'w').write('x')\""
                    )
                },
            ),
        ]
        for tool_name, tool_input in attempts:
            result = run_script(
                layout.bin / "resume-pretool-guard",
                hook_event(layout.repo, tool_name, tool_input),
                guard_environment(layout),
            )
            assert result.returncode == 2, (tool_name, result.stdout, result.stderr)
            assert not sentinel.exists(), f"{tool_name} reached execution"


@criteria("§4.2-2", "§4.3-3")
def test_alternate_mcp_sideload_plugin_and_agent_inputs_are_rejected() -> None:
    """§4.2-2; §4.3-3 — alternate MCP/sideload/plugin/agent routes are closed."""

    with installed_layout() as layout:
        environment = guard_environment(layout)
        denied = [
            ("Bash", {"command": "claude mcp add attacker -- attacker-server"}),
            ("mcp__attacker__write", {"path": "models/x"}),
            ("Skill", {"skill": "attacker-plugin"}),
            (
                "Agent",
                {
                    "prompt": "write",
                    "description": "arbitrary agent",
                    "subagent_type": "general-purpose",
                },
            ),
            (
                "Agent",
                {
                    "prompt": "plugin",
                    "description": "plugin agent",
                    "subagent_type": "plugin:attacker",
                },
            ),
        ]
        for tool_name, tool_input in denied:
            result = run_script(
                layout.bin / "resume-pretool-guard",
                hook_event(layout.repo, tool_name, tool_input),
                environment,
            )
            assert result.returncode == 2, (tool_name, result.stderr)

        for reader in ("resume-code-reader", "resume-pdf-reader"):
            result = run_script(
                layout.bin / "resume-pretool-guard",
                hook_event(
                    layout.repo,
                    "Agent",
                    {
                        "prompt": "Read only the assigned source.",
                        "description": "fixed reader",
                        "subagent_type": reader,
                    },
                ),
                environment,
            )
            assert result.returncode == 0, (reader, result.stderr)

        policy = load_json(POLICY_PATH)
        assert policy["disableSideloadFlags"] is True
        allowed_agents = {
            item
            for item in policy["permissions"]["allow"]
            if item.startswith("Agent(")
        }
        assert allowed_agents == {
            "Agent(resume-code-reader)",
            "Agent(resume-pdf-reader)",
        }
        for flag in ("--mcp-config", "--agents"):
            parsed = subprocess.run(
                [
                    sys.executable,
                    str(layout.bin / "resume-run"),
                    "--grok-isolated-home",
                    str(layout.root),
                    "--grok-config-sha256",
                    ZERO_HASH,
                    flag,
                    str(layout.root / "attacker.json"),
                ],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                check=False,
                timeout=20,
            )
            assert parsed.returncode == 2
            assert "unrecognized arguments" in parsed.stderr


@criteria("§2-7", "§4.2-3")
def test_installed_layout_positive_denominator_two_code_and_one_pdf() -> None:
    """§2 row 7; §4.2-3 — two code units and one PDF pass the full mock chain."""

    with installed_layout() as layout:
        assert pathlib.Path(layout.core.__file__).is_relative_to(layout.lib)
        for index, source_id in enumerate(("code_one", "code_two", "manual_pdf"), start=1):
            run_id = f"integration-positive-{index:04d}"
            engine, judge = make_engine(
                layout,
                run_id=run_id,
                state_root=layout.root / f"state-positive-{index}",
            )
            receipt = engine.submit(submission(layout, run_id=run_id, source_id=source_id))
            assert receipt["status"] == "PASS", (source_id, receipt)
            assert judge.calls[-2:] == [(run_id, "codex"), (run_id, "grok")]


@criteria("§4.3-5")
def test_manifest_path_symlink_hash_and_line_page_ranges_fail_closed() -> None:
    """§4.3-5 — outside/symlink/hash/line/page manifest faults never pass."""

    with installed_layout() as layout:
        original = load_json(layout.manifest_path)
        cases: list[tuple[str, dict[str, Any], str]] = []

        outside = copy.deepcopy(original)
        outside["sources"]["code_one"]["path"] = "../outside.f90"
        cases.append(("manifest outside path", outside, "SCHEMA_VALIDATION_FAILED"))

        escape_target = layout.root / "escape-target.f90"
        escape_target.write_text("DO 48 ITS=1,30\n", encoding="utf-8")
        (layout.repo / "models" / "escape.f90").symlink_to(escape_target)
        symlink = copy.deepcopy(original)
        symlink["sources"]["code_one"]["path"] = "models/escape.f90"
        symlink["sources"]["code_one"]["sha256"] = sha256_file(escape_target)
        cases.append(("symlink escape", symlink, "PATH_OUTSIDE_PROTECTED_ROOT"))

        mismatch = copy.deepcopy(original)
        mismatch["sources"]["code_one"]["sha256"] = ZERO_HASH
        cases.append(("source SHA mismatch", mismatch, "SOURCE_HASH_MISMATCH"))

        line_range = copy.deepcopy(original)
        line_locator = {"type": "line_range", "start": 999, "end": 999}
        line_range["sources"]["code_one"]["locators"] = [line_locator]
        line_range["controls"]["canary"]["locator"] = line_locator
        cases.append(("line range", line_range, "LOCATOR_OUT_OF_RANGE"))

        for label, manifest, expected_code in cases:
            result = validate_manifest_value(layout, manifest)
            assert result["status"] == "FAIL", (label, result)
            assert expected_code in result["failure_codes"], (label, result)

        page_range = copy.deepcopy(original)
        page_range["sources"]["manual_pdf"]["locators"] = [
            {"type": "page_range", "start": 999, "end": 999}
        ]

        def page_runner(
            argv: list[str], **_kwargs: Any
        ) -> subprocess.CompletedProcess[bytes]:
            page = int(argv[2])
            if page == 1:
                return subprocess.CompletedProcess(argv, 0, b"page one", b"")
            return subprocess.CompletedProcess(argv, 1, b"", b"page out of range")

        page_result = validate_manifest_value(
            layout,
            page_range,
            pdf_runner=page_runner,
        )
        assert page_result["status"] == "FAIL", page_result
        assert "LOCATOR_OUT_OF_RANGE" in page_result["failure_codes"], page_result


@criteria("§4.3-5")
def test_fabricated_and_cross_file_evidence_are_deterministically_rejected() -> None:
    """§4.3-5 — nonexistent and other-file quotes cannot produce PASS."""

    with installed_layout() as layout:
        for index, bad_quote in enumerate(
            ("THIS QUOTE DOES NOT EXIST", "WRITE(LUQ) IQ_GEOM,IQ_DISP,IQ_GEOM"),
            start=1,
        ):
            run_id = f"integration-fake-evidence-{index:04d}"
            engine, judge = make_engine(
                layout,
                run_id=run_id,
                state_root=layout.root / f"state-fake-{index}",
            )
            control_calls = len(judge.calls)
            receipt = engine.submit(
                submission(layout, run_id=run_id, source_id="code_one", quote=bad_quote)
            )
            assert receipt["status"] != "PASS", receipt
            decision = load_json(engine.current_decision_path)
            assert decision["inputs"]["deterministic"]["status"] == "FAIL"
            assert "QUOTE_MISMATCH" in decision["inputs"]["deterministic"]["failure_codes"]
            assert len(judge.calls) == control_calls, "judge ran after parser rejection"


@criteria("§4.3-7")
def test_every_mock_judge_failure_mode_prevents_pass() -> None:
    """§4.3-7 — FAIL/INCONCLUSIVE/timeout/invalid JSON all suppress PASS."""

    scenarios = {
        "codex-fail": {"codex": "FAIL", "grok": "PASS"},
        "grok-fail": {"codex": "PASS", "grok": "FAIL"},
        "inconclusive": {"codex": "PASS", "grok": "INCONCLUSIVE"},
        "timeout": {"codex": "timeout", "grok": "PASS"},
        "invalid-json": {"codex": "PASS", "grok": "invalid_json"},
    }
    with installed_layout() as layout:
        for index, (label, verdicts) in enumerate(scenarios.items(), start=1):
            run_id = f"integration-judge-{index:04d}"
            mock = MockJudge(layout.core, positive=verdicts)
            engine, _ = make_engine(
                layout,
                run_id=run_id,
                judge=mock,
                state_root=layout.root / f"state-judge-{index}",
            )
            receipt = engine.submit(submission(layout, run_id=run_id))
            assert receipt["status"] != "PASS", (label, receipt)
            assert load_json(engine.current_decision_path)["status"] != "PASS"


@criteria("§4.2-4", "§4.3-9")
def test_semantic_canary_single_judge_pass_is_pilot_hard_fail() -> None:
    """§4.2-4; §4.3-9 — one canary PASS must mark the pilot HARD_FAIL."""

    with installed_layout() as layout:
        mock = MockJudge(
            layout.core,
            canary={"codex": "PASS", "grok": "FAIL"},
        )
        engine, _ = make_engine(layout, judge=mock)
        assert engine.controls["canary"]["status"] == "MISSED"
        receipt = engine.submit(submission(layout))
        assert receipt["status"] == "HARD_FAIL", (
            "semantic canary was missed but pilot status was not HARD_FAIL",
            receipt,
        )


@criteria("§4.2-5", "§4.3-10")
def test_parser_negative_is_rejected_before_any_judge_call() -> None:
    """§4.2-5; §4.3-10 — parser control rejection precedes judge invocation."""

    with installed_layout() as layout:
        events: list[str] = []
        original = layout.core.deterministic.validate_manifest

        def counted(path: pathlib.Path, *args: Any, **kwargs: Any) -> Any:
            if pathlib.Path(path) == layout.parser_negative_path:
                events.append("parser-negative-rejected")
            return original(path, *args, **kwargs)

        layout.core.deterministic.validate_manifest = counted
        try:
            mock = MockJudge(layout.core, event_log=events)
            engine, _ = make_engine(layout, judge=mock)
        finally:
            layout.core.deterministic.validate_manifest = original
        assert engine.controls["parser_negative"]["status"] == "REJECTED"
        assert events[0] == "parser-negative-rejected", events
        assert all(CANARY_RUN_ID in event for event in events[1:]), events
        assert len(mock.calls) == 2, mock.calls


@criteria("§4.2-1")
def test_completion_words_without_submit_remain_not_complete_and_stop_blocks() -> None:
    """§4.2-1 — natural-language completion is NOT_COMPLETE and Stop-blocked."""

    with installed_layout() as layout:
        engine, _ = make_engine(layout)
        status = load_json(engine.status_path)
        assert engine.current_status == "NOT_COMPLETE"
        assert status["status"] == "NOT_COMPLETE"
        result = run_script(
            layout.bin / "resume-stop-gate",
            stop_event(),
            stop_environment(layout),
        )
        assert result.returncode == 0
        assert load_json_from_text(result.stdout)["decision"] == "block"


def load_json_from_text(text: str) -> dict[str, Any]:
    value = json.loads(text)
    assert isinstance(value, dict)
    return value


@criteria("§4.3-12")
def test_stop_gate_never_allows_completion_without_pass_decision() -> None:
    """§4.3-12 — absent/non-PASS decision always yields an explicit Stop block."""

    with installed_layout() as layout:
        engine, _ = make_engine(layout)
        receipt = engine.submit(submission(layout, quote="fabricated"))
        assert receipt["status"] == "FAIL"
        result = run_script(
            layout.bin / "resume-stop-gate",
            stop_event(),
            stop_environment(layout),
        )
        output = load_json_from_text(result.stdout)
        assert output["decision"] == "block", output


@criteria("§4.3-13")
def test_no_progress_hard_stop_rejects_creation_of_another_attempt() -> None:
    """§4.3-13 — after no-progress hard stop, another attempt is not created."""

    with installed_layout() as layout:
        engine, _ = make_engine(layout)
        failed = submission(layout, quote="same fabricated quote")
        first = engine.submit(failed)
        second = engine.submit(failed)
        attempts_before = sorted((engine.run_dir / "attempts").iterdir())
        ledger_before = engine.ledger_path.read_bytes()
        third = engine.submit(failed)
        attempts_after = sorted((engine.run_dir / "attempts").iterdir())
        assert first["status"] == "FAIL"
        assert second["status"] == "FAILED_STOPPED"
        assert third == second
        assert attempts_after == attempts_before
        assert engine.ledger_path.read_bytes() == ledger_before


@criteria("§4.2-6")
def test_decision_links_request_source_slices_parser_and_raw_normalized_judges() -> None:
    """§4.2-6 — decision must bind request, slices, parser, raw and normalized judges."""

    with installed_layout() as layout:
        engine, _ = make_engine(layout)
        receipt = engine.submit(submission(layout))
        assert receipt["status"] == "PASS"
        attempt = engine.run_dir / "attempts" / "000001"
        decision = load_json(attempt / "decision.json")
        request = load_json(attempt / "request.json")
        deterministic = load_json(attempt / "deterministic.json")

        assert decision["provenance"]["submission"]["sha256"] == independent_hash(request)
        assert deterministic["status"] == "PASS"
        for judge_name in ("codex", "grok"):
            record = load_json(attempt / "judges" / f"{judge_name}.json")
            assert (
                decision["provenance"]["judges"][judge_name]["result_sha256"]
                == independent_hash(record)
            )
            assert record["judge_result"]["verdict"] == decision["inputs"][judge_name][
                "verdict"
            ]

        missing: list[str] = []
        if not (attempt / "source-manifest.json").is_file():
            missing.append("source-manifest.json")
        slice_dir = attempt / "source-slices"
        if not slice_dir.is_dir() or not any(slice_dir.iterdir()):
            missing.append("source-slices/*")
        for judge_name in ("codex", "grok"):
            judge_dir = attempt / "judges" / judge_name
            if not judge_dir.is_dir() or not any(
                candidate.name.startswith("stdout") for candidate in judge_dir.iterdir()
            ):
                missing.append(f"judges/{judge_name}/stdout(raw)")
            if not (judge_dir / "verdict.json").is_file():
                missing.append(f"judges/{judge_name}/verdict.json(normalized)")
        assert not missing, "unlinked/missing evidence artifacts: " + ", ".join(missing)


def _independent_jcs_text(value: Any) -> str:
    if value is None:
        return "null"
    if value is True:
        return "true"
    if value is False:
        return "false"
    if isinstance(value, int) and not isinstance(value, bool):
        return str(value)
    if isinstance(value, str):
        return json.dumps(value, ensure_ascii=False, separators=(",", ":"))
    if isinstance(value, list):
        return "[" + ",".join(_independent_jcs_text(item) for item in value) + "]"
    if isinstance(value, dict):
        keys = sorted(value, key=lambda item: item.encode("utf-16-be", errors="strict"))
        return "{" + ",".join(
            f"{_independent_jcs_text(key)}:{_independent_jcs_text(value[key])}"
            for key in keys
        ) + "}"
    raise TypeError(f"unsupported JSON value: {type(value).__name__}")


def independent_hash(value: Any) -> str:
    return sha256_bytes(_independent_jcs_text(value).encode("utf-8"))


@criteria("§4.2-7", "§4.3-11")
def test_chain_root_matches_test_owned_independent_recalculation() -> None:
    """§4.2-7; §4.3-11 — a test-owned JCS implementation reproduces chain_root."""

    with installed_layout() as layout:
        engine, _ = make_engine(layout)
        assert engine.submit(submission(layout))["status"] == "PASS"
        attempt = engine.run_dir / "attempts" / "000001"
        decision = load_json(attempt / "decision.json")
        request = load_json(attempt / "request.json")
        deterministic = load_json(attempt / "deterministic.json")
        judge_records = {
            name: load_json(attempt / "judges" / f"{name}.json")
            for name in ("codex", "grok")
        }
        ledger = [
            json.loads(line)
            for line in engine.ledger_path.read_text(encoding="utf-8").splitlines()
        ]
        attempt_entry = next(entry for entry in ledger if entry["event_type"] == "ATTEMPT")
        material = {
            "manifest_sha256": independent_hash(load_json(layout.manifest_path)),
            "submission_sha256": independent_hash(request),
            "deterministic_sha256": independent_hash(deterministic),
            "judge_sha256": {
                name: independent_hash(record) for name, record in judge_records.items()
            },
            "previous_ledger_hash": attempt_entry["prev_hash"],
        }
        provenance_hash = independent_hash(material)
        assert (
            decision["inputs"]["evidence_chain"]["provenance_sha256"]
            == provenance_hash
        )
        expected_root = independent_hash(
            {"provenance_sha256": provenance_hash, "inputs": decision["inputs"]}
        )
        assert decision["chain_root"] == expected_root

        deterministic["status"] = "FAIL"
        deterministic["failure_codes"] = ["TAMPERED_INTEGRATION_FIXTURE"]
        write_json(attempt / "deterministic.json", deterministic)
        blocked = run_script(
            layout.bin / "resume-stop-gate",
            stop_event(),
            stop_environment(layout),
        )
        assert load_json_from_text(blocked.stdout)["decision"] == "block"


@criteria("§4.2-8")
def test_same_run_resume_preserves_attempts_and_cross_run_pass_is_rejected() -> None:
    """§4.2-8 — resume preserves run/attempts; copied cross-run PASS is unusable."""

    with installed_layout() as layout:
        engine, _ = make_engine(layout)
        assert engine.submit(submission(layout))["status"] == "PASS"
        resumed_judge = MockJudge(layout.core)
        resumed = layout.core.ResumeGateEngine(engine.config, resumed_judge)
        assert resumed.config.run_id == RUN_ID
        assert len(resumed.attempt_history) == 1
        assert resumed.attempt_history == engine.attempt_history
        assert resumed_judge.calls == []

        other_run = "integration-run-other"
        shutil.copytree(engine.run_dir, layout.state / other_run)
        result = run_script(
            layout.bin / "resume-stop-gate",
            stop_event(),
            stop_environment(layout, other_run),
        )
        assert load_json_from_text(result.stdout)["decision"] == "block"


class NeverRunner:
    def __init__(self) -> None:
        self.preflight_calls = 0
        self.invoke_calls = 0

    def preflight(self, *_args: Any, **_kwargs: Any) -> None:
        self.preflight_calls += 1
        raise AssertionError("preflight must not run with an API key")

    def invoke(self, *_args: Any, **_kwargs: Any) -> Any:
        self.invoke_calls += 1
        raise AssertionError("judge must not run with an API key")


@criteria("§4.2-10", "§4.3-8")
def test_api_key_environment_is_rejected_before_judge_execution() -> None:
    """§4.2-10; §4.3-8 — OPENAI/XAI API-key presence fails before judge calls."""

    with installed_layout() as layout:
        for variable in ("OPENAI_API_KEY", "XAI_API_KEY"):
            runner = NeverRunner()
            outcome = layout.adapter.run_adapter(
                judge_name="codex",
                repo_root=layout.repo,
                manifest_path=layout.manifest_path,
                submission_path=layout.root / "not-read.json",
                launcher_run_id=RUN_ID,
                runner=runner,
                schema_dir=layout.lib / "schemas",
                prompt_path=layout.lib / "judge" / "prompt.fixed.txt",
                empty_cwd=layout.empty,
                environment={"HOME": str(layout.root), variable: ""},
            )
            value = outcome.as_dict()
            assert value["status"] == "FAIL"
            assert value["failure"]["code"] == "API_KEY_ENV_PRESENT"
            assert runner.preflight_calls == 0
            assert runner.invoke_calls == 0


@criteria("§4.4")
def test_soft_rationale_differences_do_not_change_unanimous_pass() -> None:
    """§4.4 — noncritical rationale differences neither relax nor block PASS."""

    with installed_layout() as layout:
        engine, _ = make_engine(layout)
        receipt = engine.submit(submission(layout))
        assert receipt["status"] == "PASS"
        decision = load_json(engine.current_decision_path)
        codex = load_json(engine.run_dir / "attempts" / "000001" / "judges" / "codex.json")
        grok = load_json(engine.run_dir / "attempts" / "000001" / "judges" / "grok.json")
        assert codex["judge_result"]["reasoning"] != grok["judge_result"]["reasoning"]
        assert decision["inputs"]["codex"]["verdict"] == "PASS"
        assert decision["inputs"]["grok"]["verdict"] == "PASS"


def git_snapshot() -> bytes:
    completed = subprocess.run(
        ["git", "status", "--porcelain=v1", "-z", "--untracked-files=all"],
        cwd=REPO_ROOT,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=True,
    )
    return completed.stdout


def models_mode_snapshot() -> tuple[tuple[str, int, int, int, str | None], ...]:
    models = REPO_ROOT / "models"
    records: list[tuple[str, int, int, int, str | None]] = []
    paths = [models, *models.rglob("*")]
    for path in paths:
        metadata = path.lstat()
        target = os.readlink(path) if stat.S_ISLNK(metadata.st_mode) else None
        records.append(
            (
                str(path.relative_to(REPO_ROOT)),
                stat.S_IMODE(metadata.st_mode),
                metadata.st_uid,
                metadata.st_gid,
                target,
            )
        )
    return tuple(sorted(records))


@criteria("§4.2-9", "§4.3-4")
def test_repository_models_permissions_and_git_status_are_unchanged() -> None:
    """§4.2-9; §4.3-4 — models permissions and exact git status stay unchanged."""

    assert _BASELINE_MODE is not None and _BASELINE_GIT is not None
    assert models_mode_snapshot() == _BASELINE_MODE
    assert git_snapshot() == _BASELINE_GIT


TESTS = [
    test_direct_writers_and_shell_write_bypasses_are_pretool_blocked,
    test_alternate_mcp_sideload_plugin_and_agent_inputs_are_rejected,
    test_installed_layout_positive_denominator_two_code_and_one_pdf,
    test_manifest_path_symlink_hash_and_line_page_ranges_fail_closed,
    test_fabricated_and_cross_file_evidence_are_deterministically_rejected,
    test_every_mock_judge_failure_mode_prevents_pass,
    test_semantic_canary_single_judge_pass_is_pilot_hard_fail,
    test_parser_negative_is_rejected_before_any_judge_call,
    test_completion_words_without_submit_remain_not_complete_and_stop_blocks,
    test_stop_gate_never_allows_completion_without_pass_decision,
    test_no_progress_hard_stop_rejects_creation_of_another_attempt,
    test_decision_links_request_source_slices_parser_and_raw_normalized_judges,
    test_chain_root_matches_test_owned_independent_recalculation,
    test_same_run_resume_preserves_attempts_and_cross_run_pass_is_rejected,
    test_api_key_environment_is_rejected_before_judge_execution,
    test_soft_rationale_differences_do_not_change_unanimous_pass,
    test_repository_models_permissions_and_git_status_are_unchanged,
]


def main() -> int:
    global _BASELINE_GIT, _BASELINE_MODE
    _BASELINE_GIT = git_snapshot()
    _BASELINE_MODE = models_mode_snapshot()
    results: list[tuple[Callable[..., None], bool, str]] = []
    for test in TESTS:
        identifiers = ", ".join(getattr(test, "criteria"))
        try:
            test()
        except BaseException as error:
            detail = f"{type(error).__name__}: {error}"
            results.append((test, False, detail))
            print(f"[FAIL] {test.__name__} [{identifiers}]")
            print(f"       {detail}")
        else:
            results.append((test, True, ""))
            print(f"[PASS] {test.__name__} [{identifiers}]")

    criterion_results: dict[str, list[bool]] = {}
    for test, passed, _detail in results:
        for identifier in getattr(test, "criteria"):
            criterion_results.setdefault(identifier, []).append(passed)
    print("\n§ criterion mapping")
    for identifier in sorted(criterion_results):
        values = criterion_results[identifier]
        state = "PASS" if all(values) else "FAIL"
        print(f"- {identifier}: {state} ({sum(values)}/{len(values)} tests)")

    failures = [(test, detail) for test, passed, detail in results if not passed]
    print(f"\nSummary: {len(results) - len(failures)}/{len(results)} passed")
    if failures:
        print("Failures:")
        for test, detail in failures:
            doc = inspect.getdoc(test) or ""
            print(f"- {test.__name__}: {detail}")
            print(f"  mapping: {doc.splitlines()[0] if doc else 'missing'}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
