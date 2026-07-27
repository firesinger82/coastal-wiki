#!/usr/bin/env python3
"""Mock-only phase-5 tests for decision engine, ledger, and MCP surface.

Run:
  .venv/bin/python tools/resume-gate/tests/test_engine.py
"""
from __future__ import annotations

import copy
import hashlib
import importlib.util
import io
import json
import pathlib
import shutil
import sys
import tempfile
from contextlib import contextmanager
from typing import Any, Iterator

from jsonschema import Draft202012Validator


GATE_ROOT = pathlib.Path(__file__).resolve().parents[1]
REPO_ROOT = GATE_ROOT.parents[1]
FIXTURES = pathlib.Path(__file__).resolve().parent / "fixtures"
CORE_PATH = GATE_ROOT / "engine" / "core.py"
MCP_PATH = GATE_ROOT / "engine" / "mcp_server.py"
VALIDATOR_PATH = GATE_ROOT / "validator" / "validate.py"

CORE_SPEC = importlib.util.spec_from_file_location("resume_gate_phase5_core_test", CORE_PATH)
assert CORE_SPEC is not None and CORE_SPEC.loader is not None
core = importlib.util.module_from_spec(CORE_SPEC)
sys.modules[CORE_SPEC.name] = core
CORE_SPEC.loader.exec_module(core)

MCP_SPEC = importlib.util.spec_from_file_location("resume_gate_phase5_mcp_test", MCP_PATH)
assert MCP_SPEC is not None and MCP_SPEC.loader is not None
mcp = importlib.util.module_from_spec(MCP_SPEC)
sys.modules[MCP_SPEC.name] = mcp
MCP_SPEC.loader.exec_module(mcp)


def file_hash(path: pathlib.Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_json(path: pathlib.Path, value: Any) -> None:
    path.write_text(
        json.dumps(value, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def fixture_manifest() -> dict[str, Any]:
    locator = {"type": "line_range", "start": 1, "end": 1}
    execution_hash = file_hash(VALIDATOR_PATH)
    return {
        "schema_version": 1,
        "contract_version": "resume-gate/1",
        "manifest_id": "engine-fixture-manifest-001",
        "run_scope": "isolated phase-5 mock-only fixture",
        "work_items": ["engine_source"],
        "sources": {
            "engine_source": {
                "path": "tools/resume-gate/tests/fixtures/engine-source.txt",
                "sha256": file_hash(FIXTURES / "engine-source.txt"),
                "artifact_type": "code",
                "locators": [locator],
            }
        },
        "controls": {
            "canary": {
                "control_id": "engine-canary-control-001",
                "kind": "canary",
                "source_id": "engine_source",
                "locator": locator,
                "expected_status": "CAUGHT",
                "allowed_failure_codes": ["CANARY_FABRICATED_CLAIM"],
                "input_artifact_sha256": file_hash(
                    FIXTURES / "engine-canary.submission.json"
                ),
                "execution_artifact_sha256": execution_hash,
            },
            "parser_negative": {
                "control_id": "engine-parser-control-001",
                "kind": "parser_negative",
                "mutation": {
                    "mutation_id": "engine-duplicate-key-001",
                    "operation": "duplicate_key",
                    "target": "sources.engine_source",
                },
                "expected_status": "REJECTED",
                "allowed_failure_codes": ["JSON_DUPLICATE_KEY"],
                "input_artifact_sha256": file_hash(
                    FIXTURES / "engine-parser-negative.json"
                ),
                "execution_artifact_sha256": execution_hash,
            },
        },
    }


def submission(
    manifest: dict[str, Any],
    *,
    run_id: str = "engine-run-0001",
    claim: str = "The bounded loop ends at 30.",
    quote: str = "The bounded loop ends at 30.",
) -> dict[str, Any]:
    return {
        "schema_version": 1,
        "contract_version": "resume-gate/1",
        "manifest": {
            "manifest_id": manifest["manifest_id"],
            "sha256": core.deterministic.jcs_sha256(manifest),
        },
        "run_id": run_id,
        "candidate": {
            "source_id": "engine_source",
            "claim": claim,
            "claim_type": "explicit",
        },
        "evidence": [
            {
                "locator": {"type": "line_range", "start": 1, "end": 1},
                "quote": quote,
            }
        ],
        "attempt_reason": "phase-5 mock fixture",
    }


class MockJudgeInvoker:
    def __init__(
        self,
        *,
        positive: dict[str, str] | None = None,
        canary: dict[str, str] | None = None,
    ) -> None:
        self.positive = positive or {"codex": "PASS", "grok": "PASS"}
        self.canary = canary or {"codex": "FAIL", "grok": "FAIL"}
        self.calls: list[tuple[str, str]] = []

    def __call__(self, **kwargs: Any) -> dict[str, Any]:
        judge_name = kwargs["judge_name"]
        run_id = kwargs["launcher_run_id"]
        self.calls.append((run_id, judge_name))
        value, issues = core.deterministic.strict_json_load_path(
            kwargs["submission_path"], "mock judge submission"
        )
        assert not issues and isinstance(value, dict)
        manifest_value, manifest_issues = core.deterministic.strict_json_load_path(
            kwargs["manifest_path"], "mock judge manifest"
        )
        assert not manifest_issues and isinstance(manifest_value, dict)
        verdicts = self.canary if "control-canary" in run_id else self.positive
        verdict = verdicts[judge_name]
        result = {
            "schema_version": 1,
            "contract_version": "resume-gate/1",
            "manifest": {
                "manifest_id": manifest_value["manifest_id"],
                "sha256": core.deterministic.jcs_sha256(manifest_value),
            },
            "submission_sha256": core.deterministic.jcs_sha256(value),
            "judge": judge_name,
            "engine_version": f"mock-{judge_name}/1",
            "verdict": verdict,
            "claim_supported_by_evidence": verdict == "PASS",
            "reasoning": "mock-only result",
            "issues": [] if verdict == "PASS" else ["mock rejection"],
        }
        return {"status": "VALIDATED", "judge_result": result}


@contextmanager
def engine_context(
    *,
    run_id: str = "engine-run-0001",
    invoker: MockJudgeInvoker | None = None,
    auto_start_controls: bool = True,
) -> Iterator[tuple[core.ResumeGateEngine, dict[str, Any], MockJudgeInvoker, pathlib.Path]]:
    with tempfile.TemporaryDirectory(prefix="resume-gate-engine-") as temp:
        temp_root = pathlib.Path(temp)
        manifest = fixture_manifest()
        manifest_path = temp_root / "manifest.json"
        write_json(manifest_path, manifest)
        selected_invoker = invoker or MockJudgeInvoker()
        config = core.EngineConfig(
            repo_root=REPO_ROOT,
            manifest_path=manifest_path,
            run_id=run_id,
            state_root=temp_root / "state",
            schema_dir=GATE_ROOT / "schemas",
            control_artifacts=core.ControlArtifacts(
                canary_submission=FIXTURES / "engine-canary.submission.json",
                parser_negative=FIXTURES / "engine-parser-negative.json",
                execution_artifact=VALIDATOR_PATH,
            ),
            auto_start_controls=auto_start_controls,
        )
        engine = core.ResumeGateEngine(config, selected_invoker)
        yield engine, manifest, selected_invoker, temp_root


def decision_inputs() -> dict[str, Any]:
    return {
        "deterministic": {"status": "PASS", "failure_codes": []},
        "codex": {"verdict": "PASS"},
        "grok": {"verdict": "PASS"},
        "canary": {
            "control_id": "engine-canary-control-001",
            "status": "CAUGHT",
            "failure_codes": ["CANARY_FABRICATED_CLAIM"],
            "input_artifact_sha256": "1" * 64,
            "execution_artifact_sha256": "2" * 64,
        },
        "parser_negative": {
            "control_id": "engine-parser-control-001",
            "status": "REJECTED",
            "failure_codes": ["JSON_DUPLICATE_KEY"],
            "input_artifact_sha256": "3" * 64,
            "execution_artifact_sha256": "2" * 64,
        },
        "evidence_chain": {
            "status": "VALID",
            "provenance_sha256": "4" * 64,
        },
    }


def decision_record(inputs: dict[str, Any], status: str) -> dict[str, Any]:
    return {
        "schema_version": 1,
        "contract_version": "resume-gate/1",
        "run_id": "engine-run-0001",
        "attempt_id": 1,
        "provenance": {
            "manifest": {
                "schema_version": 1,
                "manifest_id": "engine-fixture-manifest-001",
                "sha256": "5" * 64,
            },
            "submission": {"schema_version": 1, "sha256": "6" * 64},
            "judges": {
                "codex": {
                    "schema_version": 1,
                    "engine_version": "mock-codex/1",
                    "result_sha256": "7" * 64,
                },
                "grok": {
                    "schema_version": 1,
                    "engine_version": "mock-grok/1",
                    "result_sha256": "8" * 64,
                },
            },
            "decision_engine_version": "resume-gate-engine/1",
        },
        "inputs": inputs,
        "status": status,
        "chain_root": "9" * 64,
    }


def test_decision_table_all_single_losses_are_double_rejected() -> None:
    schema = json.loads(
        (GATE_ROOT / "schemas" / "decision.schema.json").read_text(encoding="utf-8")
    )
    validator = Draft202012Validator(schema)
    passing = decision_inputs()
    assert core.compute_decision_status(passing) == "PASS"
    assert not list(validator.iter_errors(decision_record(passing, "PASS")))

    losses: dict[str, Any] = {
        "deterministic": {"status": "FAIL", "failure_codes": ["TEST_FAILURE"]},
        "codex": {"verdict": "FAIL"},
        "grok": {"verdict": "INCONCLUSIVE"},
        "canary": {**passing["canary"], "status": "MISSED"},
        "parser_negative": {**passing["parser_negative"], "status": "ACCEPTED"},
        "evidence_chain": {
            **passing["evidence_chain"],
            "status": "INVALID",
        },
    }
    for field, missing_value in losses.items():
        inputs = copy.deepcopy(passing)
        inputs[field] = missing_value
        assert core.compute_decision_status(inputs) == "FAIL", field
        assert not list(validator.iter_errors(decision_record(inputs, "FAIL"))), field
        assert list(validator.iter_errors(decision_record(inputs, "PASS"))), field


def test_controls_run_before_positive_and_full_pass_decision() -> None:
    with engine_context() as (engine, manifest, invoker, _temp):
        assert invoker.calls == [
            ("engine-control-canary-001", "codex"),
            ("engine-control-canary-001", "grok"),
        ]
        assert engine.entries[0]["event_type"] == "CONTROLS"
        receipt = engine.submit(submission(manifest))
        assert receipt["status"] == "PASS", receipt
        assert invoker.calls[-2:] == [
            ("engine-run-0001", "codex"),
            ("engine-run-0001", "grok"),
        ]
        decision = json.loads(engine.current_decision_path.read_text(encoding="utf-8"))
        assert decision["status"] == "PASS"
        assert decision["inputs"]["canary"]["status"] == "CAUGHT"
        assert decision["inputs"]["parser_negative"]["status"] == "REJECTED"


def test_controls_unexecuted_or_missed_prevent_pass() -> None:
    with engine_context(auto_start_controls=False) as (engine, manifest, invoker, _temp):
        receipt = engine.submit(submission(manifest))
        assert receipt["status"] == "FAIL"
        decision = json.loads(engine.current_decision_path.read_text(encoding="utf-8"))
        assert decision["inputs"]["canary"]["status"] == "NA"
        assert decision["inputs"]["parser_negative"]["status"] == "NA"
        assert decision["status"] == "FAIL"
        assert len(invoker.calls) == 2

    missed = MockJudgeInvoker(canary={"codex": "PASS", "grok": "FAIL"})
    with engine_context(invoker=missed) as (engine, manifest, _invoker, _temp):
        assert engine.controls is not None
        assert engine.controls["canary"]["status"] == "MISSED"
        receipt = engine.submit(submission(manifest))
        assert receipt["status"] == "FAIL"


def test_control_artifact_hash_mismatch_is_recorded_and_blocks_pass() -> None:
    with tempfile.TemporaryDirectory(prefix="resume-gate-control-hash-") as temp:
        temp_root = pathlib.Path(temp)
        manifest = fixture_manifest()
        manifest["controls"]["canary"]["input_artifact_sha256"] = "f" * 64
        manifest_path = temp_root / "manifest.json"
        write_json(manifest_path, manifest)
        invoker = MockJudgeInvoker()
        config = core.EngineConfig(
            repo_root=REPO_ROOT,
            manifest_path=manifest_path,
            run_id="engine-run-hash-001",
            state_root=temp_root / "state",
            schema_dir=GATE_ROOT / "schemas",
            control_artifacts=core.ControlArtifacts(
                FIXTURES / "engine-canary.submission.json",
                FIXTURES / "engine-parser-negative.json",
                VALIDATOR_PATH,
            ),
        )
        engine = core.ResumeGateEngine(config, invoker)
        assert engine.controls is not None
        assert engine.controls["canary"]["status"] == "MISSED"
        assert (
            engine.controls["canary"]["input_artifact_sha256"]
            == file_hash(FIXTURES / "engine-canary.submission.json")
        )
        receipt = engine.submit(
            submission(manifest, run_id="engine-run-hash-001")
        )
        assert receipt["status"] == "FAIL"
        assert invoker.calls == [
            ("engine-run-hash-001", "codex"),
            ("engine-run-hash-001", "grok"),
        ]


def test_judge_disagreement_and_inconclusive_are_fail_closed() -> None:
    disagreement = MockJudgeInvoker(positive={"codex": "PASS", "grok": "FAIL"})
    with engine_context(invoker=disagreement) as (engine, manifest, _invoker, _temp):
        receipt = engine.submit(submission(manifest))
        assert receipt["status"] == "FAIL"
        decision = json.loads(engine.current_decision_path.read_text(encoding="utf-8"))
        assert decision["inputs"]["codex"]["verdict"] == "PASS"
        assert decision["inputs"]["grok"]["verdict"] == "FAIL"

    inconclusive = MockJudgeInvoker(
        positive={"codex": "PASS", "grok": "INCONCLUSIVE"}
    )
    with engine_context(invoker=inconclusive) as (engine, manifest, _invoker, _temp):
        receipt = engine.submit(submission(manifest))
        assert receipt["status"] == "FAIL"


def test_no_progress_identical_second_submission_boundary() -> None:
    with engine_context() as (engine, manifest, _invoker, _temp):
        failed = submission(manifest, quote="not in source")
        first = engine.submit(failed)
        second = engine.submit(failed)
        third = engine.submit(failed)
        assert first["status"] == "FAIL"
        assert second["status"] == "FAILED_STOPPED"
        assert third == second
        assert len(engine.attempt_history) == 2
        assert (
            engine.attempt_history[-1]["hard_stop_reason"]
            == "IDENTICAL_FAILED_CANDIDATE_EVIDENCE"
        )


def test_no_progress_three_same_codes_without_new_evidence_boundary() -> None:
    with engine_context() as (engine, manifest, _invoker, _temp):
        receipts = []
        for index in range(3):
            receipts.append(
                engine.submit(
                    submission(
                        manifest,
                        claim=f"Distinct unsupported claim {index}",
                        quote="same absent evidence",
                    )
                )
            )
        assert [item["status"] for item in receipts] == [
            "FAIL",
            "FAIL",
            "FAILED_STOPPED",
        ]
        assert (
            engine.attempt_history[-1]["hard_stop_reason"]
            == "REPEATED_DETERMINISTIC_FAILURE_WITHOUT_NEW_EVIDENCE"
        )


def test_max_six_processed_and_seventh_hard_stops_boundary() -> None:
    with engine_context() as (engine, manifest, invoker, _temp):
        receipts = [
            engine.submit(
                submission(
                    manifest,
                    claim=f"Distinct cap claim {index}",
                    quote=f"absent evidence {index}",
                )
            )
            for index in range(6)
        ]
        assert all(item["status"] == "FAIL" for item in receipts)
        seventh = engine.submit(
            submission(manifest, claim="seventh", quote="seventh absent evidence")
        )
        assert seventh["attempt"] == 7
        assert seventh["status"] == "FAILED_STOPPED"
        assert len(engine.attempt_history) == 6
        assert engine.entries[-1]["event_type"] == "HARD_STOP"
        assert len(invoker.calls) == 2  # canary only; deterministic failures skip judges
        status = json.loads(engine.status_path.read_text(encoding="utf-8"))
        assert status["status"] == "FAILED_STOPPED"
        assert status["accepted_attempts"] == 6
        assert status["ledger_hash"] == seventh["ledger_hash"]


def test_restart_restores_controls_attempts_and_status_without_rerun() -> None:
    with engine_context() as (engine, manifest, _invoker, _temp):
        first = engine.submit(submission(manifest, quote="restart absent evidence"))
        assert first["status"] == "FAIL"
        resumed_invoker = MockJudgeInvoker()
        resumed = core.ResumeGateEngine(engine.config, resumed_invoker)
        assert resumed.controls == engine.controls
        assert resumed.attempt_history == engine.attempt_history
        assert resumed.current_status == "FAIL"
        assert resumed.ledger_hash == engine.ledger_hash
        assert resumed_invoker.calls == []
        second = resumed.submit(
            submission(
                manifest,
                claim="restart second claim",
                quote="restart second absent evidence",
            )
        )
        assert second["attempt"] == 2
        assert second["status"] == "FAIL"


def _copy_ledger(engine: core.ResumeGateEngine, destination: pathlib.Path) -> tuple[pathlib.Path, pathlib.Path]:
    ledger = destination / "ledger.jsonl"
    head = destination / "head.json"
    shutil.copyfile(engine.ledger_path, ledger)
    shutil.copyfile(engine.head_path, head)
    return ledger, head


def _assert_ledger_error(ledger: pathlib.Path, head: pathlib.Path) -> None:
    try:
        core.verify_ledger(ledger, head, "engine-run-0001")
    except core.LedgerError:
        return
    raise AssertionError("corrupt ledger was accepted")


def test_ledger_detects_tamper_tail_deletion_and_reordering() -> None:
    with engine_context() as (engine, manifest, _invoker, temp_root):
        engine.submit(submission(manifest, claim="first", quote="absent first"))
        engine.submit(submission(manifest, claim="second", quote="absent second"))
        verified_hash, count, _ = core.verify_ledger(
            engine.ledger_path, engine.head_path, "engine-run-0001"
        )
        assert verified_hash == engine.ledger_hash
        assert count == 3

        tamper_dir = temp_root / "tamper"
        tamper_dir.mkdir()
        ledger, head = _copy_ledger(engine, tamper_dir)
        lines = ledger.read_text(encoding="utf-8").splitlines()
        entry = json.loads(lines[1])
        entry["payload"]["decision_status"] = "PASS"
        lines[1] = json.dumps(entry, separators=(",", ":"))
        ledger.write_text("\n".join(lines) + "\n", encoding="utf-8")
        _assert_ledger_error(ledger, head)

        delete_dir = temp_root / "delete"
        delete_dir.mkdir()
        ledger, head = _copy_ledger(engine, delete_dir)
        lines = ledger.read_text(encoding="utf-8").splitlines()
        ledger.write_text("\n".join(lines[:-1]) + "\n", encoding="utf-8")
        _assert_ledger_error(ledger, head)

        reorder_dir = temp_root / "reorder"
        reorder_dir.mkdir()
        ledger, head = _copy_ledger(engine, reorder_dir)
        lines = ledger.read_text(encoding="utf-8").splitlines()
        lines[0], lines[1] = lines[1], lines[0]
        ledger.write_text("\n".join(lines) + "\n", encoding="utf-8")
        _assert_ledger_error(ledger, head)


def test_evidence_chain_rejects_attempt_artifact_tamper_on_restart() -> None:
    with engine_context() as (engine, manifest, _invoker, _temp):
        engine.submit(submission(manifest, quote="artifact tamper absent evidence"))
        deterministic_path = (
            engine.run_dir / "attempts" / "000001" / "deterministic.json"
        )
        value = json.loads(deterministic_path.read_text(encoding="utf-8"))
        value["issues"][0]["detail"] = "tampered detail"
        write_json(deterministic_path, value)
        try:
            core.ResumeGateEngine(engine.config, MockJudgeInvoker())
        except core.LedgerError:
            pass
        else:
            raise AssertionError("tampered attempt artifact retained a VALID chain")


def test_mcp_surface_exactly_submit_and_bad_input_fails_closed() -> None:
    with engine_context() as (engine, manifest, _invoker, _temp):
        server = mcp.ResumeGateMCP(engine)
        initialized = server.handle({"method": "initialize"})
        assert initialized is not None
        assert initialized["capabilities"] == {"tools": {}}
        listed = server.handle({"method": "tools/list"})
        assert listed is not None
        assert [tool["name"] for tool in listed["tools"]] == ["submit"]
        assert server.handle({"method": "resources/list"}) == {"resources": []}
        assert server.handle({"method": "prompts/list"}) == {"prompts": []}

        injected = submission(manifest)
        injected["ledger_path"] = "/tmp/attacker-ledger"
        result = server.handle(
            {
                "method": "tools/call",
                "params": {"name": "submit", "arguments": injected},
            }
        )
        assert result is not None and result.get("isError") is not True
        receipt = json.loads(result["content"][0]["text"])
        assert set(receipt) == {"attempt", "ledger_hash", "status"}
        assert receipt["status"] == "FAIL"
        decision = json.loads(engine.current_decision_path.read_text(encoding="utf-8"))
        assert "SCHEMA_VALIDATION_FAILED" in decision["inputs"]["deterministic"][
            "failure_codes"
        ]

        unknown = server.handle(
            {"method": "tools/call", "params": {"name": "not-submit", "arguments": {}}}
        )
        assert unknown is not None and unknown["isError"] is True


def test_mcp_strict_outer_decode_rejects_duplicate_key() -> None:
    with engine_context() as (engine, _manifest, _invoker, _temp):
        server = mcp.ResumeGateMCP(engine)
        request = (
            '{"jsonrpc":"2.0","id":1,"method":"tools/call",'
            '"params":{"name":"submit","arguments":{"run_id":"one","run_id":"two"}}}\n'
        )
        output = io.StringIO()
        mcp.serve(server, io.StringIO(request), output)
        response = json.loads(output.getvalue())
        assert response["error"]["code"] == -32700
        assert len(engine.attempt_history) == 0


def test_path_injection_and_overwrite_targets_are_rejected() -> None:
    try:
        core.EngineConfig(
            repo_root=REPO_ROOT,
            manifest_path=FIXTURES / "engine-source.txt",
            run_id="../escape",
            state_root=pathlib.Path("/tmp/resume-gate-unused"),
            schema_dir=GATE_ROOT / "schemas",
            control_artifacts=core.ControlArtifacts(
                FIXTURES / "engine-canary.submission.json",
                FIXTURES / "engine-parser-negative.json",
                VALIDATOR_PATH,
            ),
        )
    except Exception:
        # EngineConfig is intentionally a data object; validation occurs below.
        pass

    with tempfile.TemporaryDirectory(prefix="resume-gate-path-") as temp:
        manifest = fixture_manifest()
        manifest_path = pathlib.Path(temp) / "manifest.json"
        write_json(manifest_path, manifest)
        bad_config = core.EngineConfig(
            repo_root=REPO_ROOT,
            manifest_path=manifest_path,
            run_id="../escape",
            state_root=pathlib.Path(temp) / "state",
            schema_dir=GATE_ROOT / "schemas",
            control_artifacts=core.ControlArtifacts(
                FIXTURES / "engine-canary.submission.json",
                FIXTURES / "engine-parser-negative.json",
                VALIDATOR_PATH,
            ),
        )
        try:
            core.ResumeGateEngine(bad_config, MockJudgeInvoker())
        except core.SecurityError:
            pass
        else:
            raise AssertionError("path-like run_id was accepted")

    with engine_context() as (engine, manifest, _invoker, temp_root):
        victim = temp_root / "victim.json"
        victim.write_text("do-not-overwrite", encoding="utf-8")
        engine.current_decision_path.symlink_to(victim)
        try:
            engine.submit(submission(manifest))
        except (core.SecurityError, core.LedgerError):
            pass
        else:
            raise AssertionError("decision symlink overwrite was accepted")
        assert victim.read_text(encoding="utf-8") == "do-not-overwrite"

    with tempfile.TemporaryDirectory(
        prefix="resume-gate-repo-state-", dir=GATE_ROOT
    ) as inside:
        manifest = fixture_manifest()
        manifest_path = pathlib.Path(inside) / "manifest.json"
        write_json(manifest_path, manifest)
        config = core.EngineConfig(
            repo_root=REPO_ROOT,
            manifest_path=manifest_path,
            run_id="engine-run-path-001",
            state_root=pathlib.Path(inside),
            schema_dir=GATE_ROOT / "schemas",
            control_artifacts=core.ControlArtifacts(
                FIXTURES / "engine-canary.submission.json",
                FIXTURES / "engine-parser-negative.json",
                VALIDATOR_PATH,
            ),
        )
        try:
            core.ResumeGateEngine(config, MockJudgeInvoker())
        except core.SecurityError:
            pass
        else:
            raise AssertionError("repository-internal state root was accepted")


TESTS = [
    test_decision_table_all_single_losses_are_double_rejected,
    test_controls_run_before_positive_and_full_pass_decision,
    test_controls_unexecuted_or_missed_prevent_pass,
    test_control_artifact_hash_mismatch_is_recorded_and_blocks_pass,
    test_judge_disagreement_and_inconclusive_are_fail_closed,
    test_no_progress_identical_second_submission_boundary,
    test_no_progress_three_same_codes_without_new_evidence_boundary,
    test_max_six_processed_and_seventh_hard_stops_boundary,
    test_restart_restores_controls_attempts_and_status_without_rerun,
    test_ledger_detects_tamper_tail_deletion_and_reordering,
    test_evidence_chain_rejects_attempt_artifact_tamper_on_restart,
    test_mcp_surface_exactly_submit_and_bad_input_fails_closed,
    test_mcp_strict_outer_decode_rejects_duplicate_key,
    test_path_injection_and_overwrite_targets_are_rejected,
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
    print(f"\n{len(TESTS) - len(failures)}/{len(TESTS)} engine fixtures behaved as required")
    if failures:
        print("FAILURES:")
        for failure in failures:
            print(f"- {failure}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
