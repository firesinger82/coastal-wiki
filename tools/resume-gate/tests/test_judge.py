#!/usr/bin/env python3
"""Mock-only fixtures for the resume-gate external judge adapter.

Run:
  .venv/bin/python tools/resume-gate/tests/test_judge.py
"""
from __future__ import annotations

import copy
import importlib.util
import json
import pathlib
import sys
import tempfile
from collections.abc import Callable
from contextlib import contextmanager
from typing import Any, Iterator


GATE_ROOT = pathlib.Path(__file__).resolve().parents[1]
REPO_ROOT = GATE_ROOT.parents[1]
PILOT = GATE_ROOT / "fixtures" / "pilot"
ADAPTER_PATH = GATE_ROOT / "judge" / "adapter.py"
GOLDEN = pathlib.Path(__file__).resolve().parent / "fixtures" / "canary-codex-data.golden.txt"

SPEC = importlib.util.spec_from_file_location("resume_gate_judge_adapter", ADAPTER_PATH)
assert SPEC is not None and SPEC.loader is not None
adapter = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = adapter
SPEC.loader.exec_module(adapter)


def load_json(path: pathlib.Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: pathlib.Path, value: Any) -> None:
    path.write_text(
        json.dumps(value, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def prepared_inputs() -> tuple[dict[str, Any], dict[str, Any]]:
    manifest, issues = adapter.deterministic.strict_json_load_path(
        PILOT / "manifest.frozen.json",
        "frozen manifest",
    )
    assert not issues
    submission, issues = adapter.deterministic.strict_json_load_path(
        PILOT / "canary-fabricated-claim.submission.json",
        "canary submission",
    )
    assert not issues
    submission["manifest"]["sha256"] = adapter.deterministic.jcs_sha256(manifest)
    return manifest, submission


@contextmanager
def input_files() -> Iterator[tuple[pathlib.Path, pathlib.Path, pathlib.Path, dict[str, Any], dict[str, Any]]]:
    manifest, submission = prepared_inputs()
    with tempfile.TemporaryDirectory(prefix="resume-gate-judge-test-") as temp:
        root = pathlib.Path(temp)
        manifest_path = root / "manifest.json"
        submission_path = root / "submission.json"
        empty_cwd = root / "empty"
        empty_cwd.mkdir()
        write_json(manifest_path, manifest)
        write_json(submission_path, submission)
        yield manifest_path, submission_path, empty_cwd, manifest, submission


def judge_result(
    judge_name: str,
    manifest: dict[str, Any],
    submission: dict[str, Any],
    *,
    verdict: str = "FAIL",
) -> dict[str, Any]:
    if verdict == "PASS":
        supported = True
        issues: list[str] = []
        reasoning = "The frozen slice establishes the submitted claim."
    elif verdict == "INCONCLUSIVE":
        supported = False
        issues = ["The frozen slice is insufficient to establish the claim."]
        reasoning = "Only the supplied frozen slice was considered."
    else:
        supported = False
        issues = ["The claim reverses the loop bound shown by the slice."]
        reasoning = "The loop ends at 30 rather than reaching 60."
    return {
        "schema_version": 1,
        "contract_version": manifest["contract_version"],
        "manifest": {
            "manifest_id": manifest["manifest_id"],
            "sha256": adapter.deterministic.jcs_sha256(manifest),
        },
        "submission_sha256": adapter.deterministic.jcs_sha256(submission),
        "judge": judge_name,
        "engine_version": adapter.JUDGES[judge_name].engine_version,
        "verdict": verdict,
        "claim_supported_by_evidence": supported,
        "reasoning": reasoning,
        "issues": issues,
    }


def wrap_output(judge_name: str, result: dict[str, Any]) -> bytes:
    result_text = json.dumps(result, ensure_ascii=False, separators=(",", ":"))
    if judge_name == "codex":
        events = [
            {"type": "thread.started", "thread_id": "mock-thread"},
            {
                "type": "item.completed",
                "item": {"id": "item-0", "type": "agent_message", "text": result_text},
            },
            {"type": "turn.completed", "usage": {}},
        ]
        return (
            "\n".join(
                json.dumps(event, ensure_ascii=False, separators=(",", ":"))
                for event in events
            )
            + "\n"
        ).encode("utf-8")
    wrapper = {
        "text": result_text,
        "stopReason": "EndTurn",
        "sessionId": "mock-session",
        "requestId": "mock-request",
    }
    return json.dumps(wrapper, ensure_ascii=False, separators=(",", ":")).encode("utf-8")


class MockRunner:
    def __init__(
        self,
        process_result: adapter.ProcessResult | None = None,
        *,
        invoke_error: Exception | None = None,
        preflight_error: Exception | None = None,
    ) -> None:
        self.process_result = process_result
        self.invoke_error = invoke_error
        self.preflight_error = preflight_error
        self.preflight_calls = 0
        self.invoke_calls = 0
        self.prompt: bytes | None = None
        self.environment: dict[str, str] | None = None

    def preflight(
        self,
        config: adapter.JudgeConfig,
        environment: dict[str, str],
        empty_cwd: pathlib.Path,
    ) -> None:
        self.preflight_calls += 1
        assert config.engine_version in {
            adapter.CODEX_ENGINE_VERSION,
            adapter.GROK_ENGINE_VERSION,
        }
        assert empty_cwd.is_dir()
        assert not any(empty_cwd.iterdir())
        self.environment = dict(environment)
        if self.preflight_error is not None:
            raise self.preflight_error

    def invoke(self, config: adapter.JudgeConfig, **kwargs: Any) -> adapter.ProcessResult:
        self.invoke_calls += 1
        self.prompt = kwargs["prompt"]
        assert kwargs["empty_cwd"].is_dir()
        assert not any(kwargs["empty_cwd"].iterdir())
        if self.invoke_error is not None:
            raise self.invoke_error
        assert self.process_result is not None
        return self.process_result


def run_with_mock(
    judge_name: str,
    result_factory: Callable[[dict[str, Any], dict[str, Any]], dict[str, Any]],
    *,
    environment: dict[str, str] | None = None,
) -> tuple[adapter.AdapterOutcome, MockRunner]:
    with input_files() as (manifest_path, submission_path, empty_cwd, manifest, submission):
        result = result_factory(manifest, submission)
        runner = MockRunner(adapter.ProcessResult(0, wrap_output(judge_name, result), b""))
        outcome = adapter.run_adapter(
            judge_name=judge_name,
            repo_root=REPO_ROOT,
            manifest_path=manifest_path,
            submission_path=submission_path,
            launcher_run_id=submission["run_id"],
            runner=runner,
            empty_cwd=empty_cwd,
            environment=environment or {"HOME": "/mock/home", "PATH": "/usr/bin"},
        )
        return outcome, runner


def assert_failed(outcome: adapter.AdapterOutcome, code: str) -> None:
    assert outcome.status == "FAIL", outcome.as_dict()
    assert outcome.failure is not None
    assert outcome.failure.code == code, outcome.as_dict()
    assert outcome.judge_result is None


def test_canary_data_golden_and_attempt_reason_omitted() -> None:
    manifest, submission = prepared_inputs()
    result, decoded_manifest, snapshots = adapter.deterministic.validate_manifest(
        PILOT / "manifest.frozen.json",
        REPO_ROOT,
        schema_dir=GATE_ROOT / "schemas",
    )
    assert result["status"] == "PASS", result
    assert decoded_manifest == manifest
    data = adapter.build_data_block(
        config=adapter.JUDGES["codex"],
        manifest=manifest,
        submission=submission,
        submission_sha256=adapter.deterministic.jcs_sha256(submission),
        snapshots=snapshots,
    )
    assert data == GOLDEN.read_bytes()
    assert data.splitlines()[3] == b"schema_version=1"
    assert b"attempt_reason" not in data
    assert submission["attempt_reason"].encode("utf-8") not in data


def test_valid_codex_fail_is_returned_and_prompt_is_exact() -> None:
    outcome, runner = run_with_mock(
        "codex",
        lambda manifest, submission: judge_result("codex", manifest, submission),
    )
    assert outcome.status == "VALIDATED", outcome.as_dict()
    assert outcome.judge_result is not None
    assert outcome.judge_result["verdict"] == "FAIL"
    assert runner.preflight_calls == 1
    assert runner.invoke_calls == 1
    assert runner.prompt is not None
    fixed = (GATE_ROOT / "judge" / "prompt.fixed.txt").read_bytes()
    assert runner.prompt.startswith(fixed + b"\n" + adapter.DATA_BEGIN.encode("ascii"))
    assert b"attempt_reason" not in runner.prompt


def test_echo_fields_and_engine_version_mutations_are_rejected() -> None:
    mutations = (
        ("contract_version", lambda result: result.update(contract_version="resume-gate/2")),
        (
            "manifest_id",
            lambda result: result["manifest"].update(manifest_id="rg-pilot-mutated-001"),
        ),
        ("manifest_sha256", lambda result: result["manifest"].update(sha256="a" * 64)),
        ("submission_sha256", lambda result: result.update(submission_sha256="b" * 64)),
        ("judge", lambda result: result.update(judge="grok")),
        ("engine_version", lambda result: result.update(engine_version="codex-cli 0.144.2")),
    )
    for label, mutate in mutations:
        def factory(
            manifest: dict[str, Any],
            submission: dict[str, Any],
            mutation: Callable[[dict[str, Any]], None] = mutate,
        ) -> dict[str, Any]:
            result = judge_result("codex", manifest, submission)
            mutation(result)
            return result

        outcome, _runner = run_with_mock("codex", factory)
        assert_failed(outcome, "JUDGE_RESULT_REJECTED")
        assert label in outcome.failure.detail or label == "contract_version", outcome.as_dict()


def test_schema_invalid_output_is_rejected() -> None:
    def factory(manifest: dict[str, Any], submission: dict[str, Any]) -> dict[str, Any]:
        result = judge_result("codex", manifest, submission)
        result.pop("reasoning")
        return result

    outcome, _runner = run_with_mock("codex", factory)
    assert_failed(outcome, "JUDGE_RESULT_REJECTED")


def test_pass_with_nonempty_issues_is_schema_rejected() -> None:
    def factory(manifest: dict[str, Any], submission: dict[str, Any]) -> dict[str, Any]:
        result = judge_result("codex", manifest, submission, verdict="PASS")
        result["issues"] = ["PASS must not carry an issue."]
        return result

    outcome, _runner = run_with_mock("codex", factory)
    assert_failed(outcome, "JUDGE_RESULT_REJECTED")


def test_inconclusive_is_a_validated_nonpass_verdict() -> None:
    outcome, _runner = run_with_mock(
        "grok",
        lambda manifest, submission: judge_result(
            "grok",
            manifest,
            submission,
            verdict="INCONCLUSIVE",
        ),
    )
    assert outcome.status == "VALIDATED", outcome.as_dict()
    assert outcome.judge_result is not None
    assert outcome.judge_result["verdict"] == "INCONCLUSIVE"
    assert outcome.judge_result["claim_supported_by_evidence"] is False
    assert _runner.environment is not None
    assert _runner.environment["GROK_DISABLE_AUTOUPDATER"] == "1"


def test_timeout_is_rejected() -> None:
    with input_files() as (manifest_path, submission_path, empty_cwd, _manifest, submission):
        runner = MockRunner(invoke_error=adapter.RunnerTimeout("mock timeout"))
        outcome = adapter.run_adapter(
            judge_name="codex",
            repo_root=REPO_ROOT,
            manifest_path=manifest_path,
            submission_path=submission_path,
            launcher_run_id=submission["run_id"],
            runner=runner,
            empty_cwd=empty_cwd,
            environment={"HOME": "/mock/home"},
        )
        assert_failed(outcome, "CLI_TIMEOUT")


def test_nonzero_exit_is_rejected() -> None:
    with input_files() as (manifest_path, submission_path, empty_cwd, _manifest, submission):
        runner = MockRunner(adapter.ProcessResult(23, b"", b"mock failure"))
        outcome = adapter.run_adapter(
            judge_name="grok",
            repo_root=REPO_ROOT,
            manifest_path=manifest_path,
            submission_path=submission_path,
            launcher_run_id=submission["run_id"],
            runner=runner,
            empty_cwd=empty_cwd,
            environment={"HOME": "/mock/home"},
        )
        assert_failed(outcome, "CLI_EXIT_NONZERO")


def test_api_key_environment_is_rejected_before_runner() -> None:
    for variable, value in (("OPENAI_API_KEY", "must-not-be-used"), ("XAI_API_KEY", "")):
        with input_files() as (
            manifest_path,
            submission_path,
            empty_cwd,
            _manifest,
            submission,
        ):
            runner = MockRunner()
            outcome = adapter.run_adapter(
                judge_name="codex",
                repo_root=REPO_ROOT,
                manifest_path=manifest_path,
                submission_path=submission_path,
                launcher_run_id=submission["run_id"],
                runner=runner,
                empty_cwd=empty_cwd,
                environment={"HOME": "/mock/home", variable: value},
            )
            assert_failed(outcome, "API_KEY_ENV_PRESENT")
            assert runner.preflight_calls == 0
            assert runner.invoke_calls == 0


def test_prompt_hash_mismatch_is_rejected_before_runner() -> None:
    with input_files() as (manifest_path, submission_path, empty_cwd, _manifest, submission):
        changed_prompt = empty_cwd.parent / "prompt.changed.txt"
        changed_prompt.write_bytes((GATE_ROOT / "judge" / "prompt.fixed.txt").read_bytes() + b"x")
        runner = MockRunner()
        outcome = adapter.run_adapter(
            judge_name="grok",
            repo_root=REPO_ROOT,
            manifest_path=manifest_path,
            submission_path=submission_path,
            launcher_run_id=submission["run_id"],
            runner=runner,
            prompt_path=changed_prompt,
            empty_cwd=empty_cwd,
            environment={"HOME": "/mock/home"},
        )
        assert_failed(outcome, "PROMPT_HASH_MISMATCH")
        assert runner.preflight_calls == 0
        assert runner.invoke_calls == 0


def test_pinned_cli_command_lines_block_mutation_surfaces() -> None:
    schema = pathlib.Path("/opt/coastal-resume/share/schemas/judge.schema.json")
    empty = pathlib.Path("/opt/coastal-resume/empty")
    codex = adapter.build_codex_argv(schema_path=schema, empty_cwd=empty)
    assert codex[-1] == "-"
    assert ("--sandbox", "read-only") == (codex[codex.index("--sandbox")], codex[codex.index("--sandbox") + 1])
    assert "--json" in codex
    assert "--output-schema" in codex
    assert "--ignore-user-config" in codex
    assert "--ignore-rules" in codex

    schema_value = load_json(GATE_ROOT / "schemas" / "judge.schema.json")
    grok = adapter.build_grok_argv(
        prompt="mock prompt",
        schema=schema_value,
        empty_cwd=empty,
    )
    assert "GROK_DISABLE_AUTOUPDATER=1" in grok
    assert ("--sandbox", "read-only") == (grok[grok.index("--sandbox")], grok[grok.index("--sandbox") + 1])
    assert grok[grok.index("--tools") + 1] == ""
    assert grok[grok.index("--max-turns") + 1] == "1"
    assert grok[grok.index("--output-format") + 1] == "json"
    assert json.loads(grok[grok.index("--json-schema") + 1]) == schema_value
    for flag in (
        "--no-plan",
        "--no-subagents",
        "--no-memory",
        "--disable-web-search",
        "--verbatim",
    ):
        assert flag in grok


def test_grok_inspect_rejects_external_customization() -> None:
    clean = {
        "projectInstructions": [],
        "hooks": [],
        "plugins": [],
        "mcpServers": [],
        "skills": [{"source": {"type": "bundled"}}],
        "agents": [{"source": {"type": "builtin"}}],
        "externalCompat": {"cells": [{"enabled": False}]},
    }
    adapter._verify_grok_inspect(clean)
    for field in ("projectInstructions", "hooks", "plugins", "mcpServers"):
        changed = copy.deepcopy(clean)
        changed[field] = [{"source": {"type": "user"}}]
        try:
            adapter._verify_grok_inspect(changed)
        except adapter.RunnerError:
            pass
        else:
            raise AssertionError(f"Grok inspect accepted external {field}")
    changed = copy.deepcopy(clean)
    changed["externalCompat"]["cells"][0]["enabled"] = True
    try:
        adapter._verify_grok_inspect(changed)
    except adapter.RunnerError:
        pass
    else:
        raise AssertionError("Grok inspect accepted enabled external compatibility")


TESTS = [
    test_canary_data_golden_and_attempt_reason_omitted,
    test_valid_codex_fail_is_returned_and_prompt_is_exact,
    test_echo_fields_and_engine_version_mutations_are_rejected,
    test_schema_invalid_output_is_rejected,
    test_pass_with_nonempty_issues_is_schema_rejected,
    test_inconclusive_is_a_validated_nonpass_verdict,
    test_timeout_is_rejected,
    test_nonzero_exit_is_rejected,
    test_api_key_environment_is_rejected_before_runner,
    test_prompt_hash_mismatch_is_rejected_before_runner,
    test_pinned_cli_command_lines_block_mutation_surfaces,
    test_grok_inspect_rejects_external_customization,
]


def main() -> int:
    failures: list[str] = []
    for test in TESTS:
        try:
            test()
        except Exception as error:
            failure = f"{test.__name__}: {type(error).__name__}: {error}"
            failures.append(failure)
            print(f"[WRONG] {failure}")
        else:
            print(f"[ok] {test.__name__}")
    print(f"\n{len(TESTS) - len(failures)}/{len(TESTS)} judge fixtures behaved as required")
    if failures:
        print("FAILURES:")
        for failure in failures:
            print(f"- {failure}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
