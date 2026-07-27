#!/usr/bin/env python3
"""Positive/negative fixtures for the deterministic resume-gate validator.

Run:
  .venv/bin/python tools/resume-gate/tests/test_validator.py
"""
from __future__ import annotations

import copy
import hashlib
import importlib.util
import json
import pathlib
import re
import subprocess
import sys
import tempfile
from typing import Any, Callable


GATE_ROOT = pathlib.Path(__file__).resolve().parents[1]
REPO_ROOT = GATE_ROOT.parents[1]
SCHEMA_DIR = GATE_ROOT / "schemas"
PILOT = GATE_ROOT / "fixtures" / "pilot"
VALIDATOR_PATH = GATE_ROOT / "validator" / "validate.py"

SPEC = importlib.util.spec_from_file_location("resume_gate_stage3_validator", VALIDATOR_PATH)
assert SPEC is not None and SPEC.loader is not None
validator = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = validator
SPEC.loader.exec_module(validator)


def sha256_file(path: pathlib.Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_json(path: pathlib.Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: pathlib.Path, value: Any, *, ensure_ascii: bool = False) -> None:
    path.write_text(
        json.dumps(value, ensure_ascii=ensure_ascii, indent=2) + "\n",
        encoding="utf-8",
    )


def frozen_pilot_manifest() -> dict[str, Any]:
    manifest = load_json(PILOT / "manifest.draft.json")
    manifest.pop("_draft_note")
    execution_hash = sha256_file(VALIDATOR_PATH)
    manifest["controls"]["canary"]["input_artifact_sha256"] = sha256_file(
        PILOT / "canary-fabricated-claim.submission.json"
    )
    manifest["controls"]["canary"]["execution_artifact_sha256"] = execution_hash
    manifest["controls"]["parser_negative"]["input_artifact_sha256"] = sha256_file(
        PILOT / "parser-negative-duplicate-source.manifest.json"
    )
    manifest["controls"]["parser_negative"]["execution_artifact_sha256"] = execution_hash
    return manifest


def manifest_hash(manifest: dict[str, Any]) -> str:
    return validator.jcs_sha256(manifest)


def efdc_submission(manifest: dict[str, Any], run_id: str = "run-stage3-positive-001") -> dict[str, Any]:
    return {
        "schema_version": 1,
        "contract_version": "resume-gate/1",
        "manifest": {
            "manifest_id": manifest["manifest_id"],
            "sha256": manifest_hash(manifest),
        },
        "run_id": run_id,
        "candidate": {
            "source_id": "efdc_svdcmp_its",
            "claim": "The SVD iteration loop has an upper bound of 30.",
            "claim_type": "explicit",
        },
        "evidence": [
            {
                "locator": {"type": "line_range", "start": 163, "end": 163},
                "quote": "DO 48 ITS=1,30",
            }
        ],
        "attempt_reason": "positive deterministic code anchor",
    }


def pdf_submission(manifest: dict[str, Any], quote: str) -> dict[str, Any]:
    submission = efdc_submission(manifest, "run-stage3-pdf-0001")
    submission["candidate"] = {
        "source_id": "swan_swantech_action_density",
        "claim": "Action density is N = E/σ.",
        "claim_type": "explicit",
    }
    submission["evidence"] = [
        {
            "locator": {"type": "page_range", "start": 19, "end": 19},
            "quote": quote,
        }
    ]
    return submission


def code_only_manifest(
    path: str,
    digest: str,
    locator: dict[str, Any] | None = None,
    *,
    artifact_type: str = "code",
) -> dict[str, Any]:
    locator = locator or {"type": "line_range", "start": 1, "end": 1}
    source_id = "fixture_source"
    return {
        "schema_version": 1,
        "contract_version": "resume-gate/1",
        "manifest_id": "fixture-manifest-0001",
        "run_scope": "isolated stage-3 filesystem fixture",
        "work_items": [source_id],
        "sources": {
            source_id: {
                "path": path,
                "sha256": digest,
                "artifact_type": artifact_type,
                "locators": [locator],
            }
        },
        "controls": {
            "canary": {
                "control_id": "fixture-canary-0001",
                "kind": "canary",
                "source_id": source_id,
                "locator": locator,
                "expected_status": "CAUGHT",
                "allowed_failure_codes": ["CANARY_FABRICATED_CLAIM"],
                "input_artifact_sha256": "1" * 64,
                "execution_artifact_sha256": "2" * 64,
            },
            "parser_negative": {
                "control_id": "fixture-parser-0001",
                "kind": "parser_negative",
                "mutation": {
                    "mutation_id": "fixture-mutation-0001",
                    "operation": "duplicate_key",
                    "target": f"sources.{source_id}",
                },
                "expected_status": "REJECTED",
                "allowed_failure_codes": ["JSON_DUPLICATE_KEY"],
                "input_artifact_sha256": "3" * 64,
                "execution_artifact_sha256": "2" * 64,
            },
        },
    }


def validate_manifest_file(path: pathlib.Path, repo_root: pathlib.Path = REPO_ROOT, **kwargs) -> dict[str, Any]:
    result, _, _ = validator.validate_manifest(
        path,
        repo_root,
        schema_dir=SCHEMA_DIR,
        **kwargs,
    )
    return result


def validate_pair(
    manifest_path: pathlib.Path,
    submission_path: pathlib.Path,
    run_id: str,
    repo_root: pathlib.Path = REPO_ROOT,
    **kwargs,
) -> dict[str, Any]:
    return validator.validate_submission(
        manifest_path,
        submission_path,
        repo_root,
        run_id,
        schema_dir=SCHEMA_DIR,
        **kwargs,
    )


def assert_code(result: dict[str, Any], code: str) -> None:
    assert result["status"] == "FAIL", result
    assert code in result["failure_codes"], result


def with_pair(
    manifest: dict[str, Any],
    submission: dict[str, Any],
    run_id: str,
    callback: Callable[[pathlib.Path, pathlib.Path, pathlib.Path], None],
) -> None:
    with tempfile.TemporaryDirectory(prefix="resume-gate-test-") as temp:
        temp_path = pathlib.Path(temp)
        manifest_path = temp_path / "manifest.json"
        submission_path = temp_path / "submission.json"
        write_json(manifest_path, manifest)
        write_json(submission_path, submission)
        callback(temp_path, manifest_path, submission_path)


def test_positive_manifest_and_code_submission() -> None:
    manifest = frozen_pilot_manifest()
    submission = efdc_submission(manifest)

    def check(_temp: pathlib.Path, manifest_path: pathlib.Path, submission_path: pathlib.Path) -> None:
        result = validate_pair(manifest_path, submission_path, submission["run_id"])
        assert result["status"] == "PASS", result
        assert result["failure_codes"] == []
        assert result["manifest_sha256"] == manifest_hash(manifest)
        assert result["submission_sha256"] == validator.jcs_sha256(submission)

    with_pair(manifest, submission, submission["run_id"], check)


def test_pdf_ligature_nfkc_and_single_physical_page() -> None:
    manifest = frozen_pilot_manifest()
    # The extracted source contains "deﬁned"; the fixture deliberately uses ASCII "defined".
    submission = pdf_submission(manifest, "The action density is defined as N = E/σ")
    real_run = subprocess.run
    calls: list[tuple[list[str], dict[str, Any]]] = []

    def recording_runner(argv, **kwargs):
        calls.append((list(argv), dict(kwargs)))
        return real_run(argv, **kwargs)

    def check(_temp: pathlib.Path, manifest_path: pathlib.Path, submission_path: pathlib.Path) -> None:
        result = validate_pair(
            manifest_path,
            submission_path,
            submission["run_id"],
            pdf_runner=recording_runner,
        )
        assert result["status"] == "PASS", result
        assert calls, "pdftotext was not invoked"
        for argv, kwargs in calls:
            assert argv[0] == "/usr/bin/pdftotext"
            assert argv[1:5] == ["-f", "19", "-l", "19"], argv
            assert argv[-1] == "-"
            assert kwargs["shell"] is False

    with_pair(manifest, submission, submission["run_id"], check)


def test_parser_negative_control_duplicate_precedes_schema() -> None:
    extraction_calls = 0

    def forbidden_runner(*_args, **_kwargs):
        nonlocal extraction_calls
        extraction_calls += 1
        raise AssertionError("source extraction must not run after duplicate-key rejection")

    result = validate_manifest_file(
        PILOT / "parser-negative-duplicate-source.manifest.json",
        pdf_runner=forbidden_runner,
    )
    assert result["failure_codes"] == ["JSON_DUPLICATE_KEY"], result
    assert extraction_calls == 0
    manifest = frozen_pilot_manifest()
    control = manifest["controls"]["parser_negative"]
    assert control["expected_status"] == "REJECTED"
    assert result["failure_codes"][0] in control["allowed_failure_codes"]
    assert control["input_artifact_sha256"] == sha256_file(
        PILOT / "parser-negative-duplicate-source.manifest.json"
    )


def test_canary_control_is_deterministically_valid_but_semantically_unjudged() -> None:
    manifest = frozen_pilot_manifest()
    canary = load_json(PILOT / "canary-fabricated-claim.submission.json")
    canary["manifest"]["sha256"] = manifest_hash(manifest)

    def check(_temp: pathlib.Path, manifest_path: pathlib.Path, submission_path: pathlib.Path) -> None:
        result = validate_pair(manifest_path, submission_path, canary["run_id"])
        assert result["status"] == "PASS", result

    with_pair(manifest, canary, canary["run_id"], check)
    control = manifest["controls"]["canary"]
    assert control["expected_status"] == "CAUGHT"
    assert control["allowed_failure_codes"] == ["CANARY_FABRICATED_CLAIM"]
    assert control["input_artifact_sha256"] == sha256_file(
        PILOT / "canary-fabricated-claim.submission.json"
    )


def test_draft_is_schema_invalid_for_tbd_controls() -> None:
    result = validate_manifest_file(PILOT / "manifest.draft.json")
    assert_code(result, "SCHEMA_VALIDATION_FAILED")
    details = " ".join(issue["detail"] for issue in result["issues"])
    assert "TBD_stage3_validator_binary" in details
    assert "TBD_canary_input_after_stage3" in details
    assert "TBD_mutated_input_after_stage3" in details


def test_json_syntax_error() -> None:
    with tempfile.TemporaryDirectory(prefix="resume-gate-test-") as temp:
        path = pathlib.Path(temp) / "bad.json"
        path.write_bytes(b'{"schema_version": 1,,}')
        assert_code(validate_manifest_file(path), "JSON_DECODE_ERROR")


def test_contract_version_schema_mapping() -> None:
    manifest = frozen_pilot_manifest()
    manifest["contract_version"] = "resume-gate/2"
    with tempfile.TemporaryDirectory(prefix="resume-gate-test-") as temp:
        path = pathlib.Path(temp) / "manifest.json"
        write_json(path, manifest)
        result = validate_manifest_file(path)
        assert_code(result, "CONTRACT_VERSION_MISMATCH")


def test_work_item_unknown() -> None:
    manifest = frozen_pilot_manifest()
    manifest["work_items"].append("missing_source")
    with tempfile.TemporaryDirectory(prefix="resume-gate-test-") as temp:
        path = pathlib.Path(temp) / "manifest.json"
        write_json(path, manifest)
        assert_code(validate_manifest_file(path), "SOURCE_ID_UNKNOWN")


def test_registered_source_absent_from_work_items() -> None:
    manifest = frozen_pilot_manifest()
    manifest["work_items"].remove("efdc_svdcmp_its")
    with tempfile.TemporaryDirectory(prefix="resume-gate-test-") as temp:
        path = pathlib.Path(temp) / "manifest.json"
        write_json(path, manifest)
        assert_code(validate_manifest_file(path), "SOURCE_ID_UNKNOWN")


def test_locator_reversed() -> None:
    manifest = frozen_pilot_manifest()
    manifest["sources"]["efdc_svdcmp_its"]["locators"][0] = {
        "type": "line_range",
        "start": 164,
        "end": 163,
    }
    with tempfile.TemporaryDirectory(prefix="resume-gate-test-") as temp:
        path = pathlib.Path(temp) / "manifest.json"
        write_json(path, manifest)
        assert_code(validate_manifest_file(path), "LOCATOR_RANGE_REVERSED")


def test_symlink_escape() -> None:
    with tempfile.TemporaryDirectory(prefix="resume-gate-test-") as temp:
        base = pathlib.Path(temp)
        root = base / "root"
        root.mkdir()
        outside = base / "outside.f90"
        outside.write_text("DO I=1,30\n", encoding="utf-8")
        (root / "escape.f90").symlink_to(outside)
        manifest = code_only_manifest("escape.f90", sha256_file(outside))
        path = base / "manifest.json"
        write_json(path, manifest)
        assert_code(validate_manifest_file(path, root), "PATH_OUTSIDE_PROTECTED_ROOT")


def test_source_missing() -> None:
    with tempfile.TemporaryDirectory(prefix="resume-gate-test-") as temp:
        root = pathlib.Path(temp)
        manifest = code_only_manifest("missing.f90", "0" * 64)
        path = root / "manifest.json"
        write_json(path, manifest)
        assert_code(validate_manifest_file(path, root), "SOURCE_READ_ERROR")


def test_source_hash_mismatch() -> None:
    manifest = frozen_pilot_manifest()
    manifest["sources"]["efdc_svdcmp_its"]["sha256"] = "0" * 64
    with tempfile.TemporaryDirectory(prefix="resume-gate-test-") as temp:
        path = pathlib.Path(temp) / "manifest.json"
        write_json(path, manifest)
        assert_code(validate_manifest_file(path), "SOURCE_HASH_MISMATCH")


def test_code_locator_out_of_range() -> None:
    with tempfile.TemporaryDirectory(prefix="resume-gate-test-") as temp:
        root = pathlib.Path(temp)
        source = root / "one.f90"
        source.write_text("ONLY ONE LINE\n", encoding="utf-8")
        locator = {"type": "line_range", "start": 2, "end": 2}
        manifest = code_only_manifest("one.f90", sha256_file(source), locator)
        path = root / "manifest.json"
        write_json(path, manifest)
        assert_code(validate_manifest_file(path, root), "LOCATOR_OUT_OF_RANGE")


def test_pdf_locator_out_of_range() -> None:
    manifest = frozen_pilot_manifest()
    manifest["sources"]["swan_swantech_action_density"]["locators"] = [
        {"type": "page_range", "start": 999, "end": 999}
    ]
    with tempfile.TemporaryDirectory(prefix="resume-gate-test-") as temp:
        path = pathlib.Path(temp) / "manifest.json"
        write_json(path, manifest)
        assert_code(validate_manifest_file(path), "LOCATOR_OUT_OF_RANGE")


def test_invalid_pdf_extraction() -> None:
    with tempfile.TemporaryDirectory(prefix="resume-gate-test-") as temp:
        root = pathlib.Path(temp)
        source = root / "not-a-pdf.pdf"
        source.write_bytes(b"not a PDF\n")
        locator = {"type": "page_range", "start": 1, "end": 1}
        manifest = code_only_manifest(
            "not-a-pdf.pdf",
            sha256_file(source),
            locator,
            artifact_type="pdf",
        )
        path = root / "manifest.json"
        write_json(path, manifest)
        assert_code(validate_manifest_file(path, root), "PDF_EXTRACTION_FAILED")


def test_manifest_binding_mismatch() -> None:
    manifest = frozen_pilot_manifest()
    submission = efdc_submission(manifest)
    submission["manifest"]["sha256"] = "0" * 64

    def check(_temp: pathlib.Path, manifest_path: pathlib.Path, submission_path: pathlib.Path) -> None:
        assert_code(
            validate_pair(manifest_path, submission_path, submission["run_id"]),
            "MANIFEST_BINDING_MISMATCH",
        )

    with_pair(manifest, submission, submission["run_id"], check)


def test_run_id_mismatch() -> None:
    manifest = frozen_pilot_manifest()
    submission = efdc_submission(manifest)

    def check(_temp: pathlib.Path, manifest_path: pathlib.Path, submission_path: pathlib.Path) -> None:
        assert_code(
            validate_pair(manifest_path, submission_path, "run-different-0001"),
            "RUN_ID_MISMATCH",
        )

    with_pair(manifest, submission, submission["run_id"], check)


def test_locator_not_registered() -> None:
    manifest = frozen_pilot_manifest()
    submission = efdc_submission(manifest)
    submission["evidence"][0]["locator"] = {
        "type": "line_range",
        "start": 164,
        "end": 164,
    }

    def check(_temp: pathlib.Path, manifest_path: pathlib.Path, submission_path: pathlib.Path) -> None:
        assert_code(
            validate_pair(manifest_path, submission_path, submission["run_id"]),
            "LOCATOR_NOT_REGISTERED",
        )

    with_pair(manifest, submission, submission["run_id"], check)


def test_candidate_source_unknown() -> None:
    manifest = frozen_pilot_manifest()
    submission = efdc_submission(manifest)
    submission["candidate"]["source_id"] = "unregistered_source"

    def check(_temp: pathlib.Path, manifest_path: pathlib.Path, submission_path: pathlib.Path) -> None:
        assert_code(
            validate_pair(manifest_path, submission_path, submission["run_id"]),
            "SOURCE_ID_UNKNOWN",
        )

    with_pair(manifest, submission, submission["run_id"], check)


def test_code_quote_mismatch() -> None:
    manifest = frozen_pilot_manifest()
    submission = efdc_submission(manifest)
    submission["evidence"][0]["quote"] = "DO 48 ITS=1,60"

    def check(_temp: pathlib.Path, manifest_path: pathlib.Path, submission_path: pathlib.Path) -> None:
        assert_code(
            validate_pair(manifest_path, submission_path, submission["run_id"]),
            "QUOTE_MISMATCH",
        )

    with_pair(manifest, submission, submission["run_id"], check)


def test_pdf_quote_mismatch() -> None:
    manifest = frozen_pilot_manifest()
    submission = pdf_submission(manifest, "The action density is defined as N = E × σ")

    def check(_temp: pathlib.Path, manifest_path: pathlib.Path, submission_path: pathlib.Path) -> None:
        assert_code(
            validate_pair(manifest_path, submission_path, submission["run_id"]),
            "QUOTE_MISMATCH",
        )

    with_pair(manifest, submission, submission["run_id"], check)


def test_canonicalization_rejects_lone_surrogate() -> None:
    manifest = frozen_pilot_manifest()
    manifest["run_scope"] = "\ud800"
    with tempfile.TemporaryDirectory(prefix="resume-gate-test-") as temp:
        path = pathlib.Path(temp) / "manifest.json"
        write_json(path, manifest, ensure_ascii=True)
        assert_code(validate_manifest_file(path), "CANONICALIZATION_ERROR")


def test_failure_code_enum_shape_and_artifact_hashes() -> None:
    values = [code.value for code in validator.FailureCode]
    assert len(values) == len(set(values))
    assert all(re.fullmatch(r"[A-Z][A-Z0-9_]{2,63}", value) for value in values)
    manifest = frozen_pilot_manifest()
    execution_hash = sha256_file(VALIDATOR_PATH)
    assert manifest["controls"]["canary"]["execution_artifact_sha256"] == execution_hash
    assert manifest["controls"]["parser_negative"]["execution_artifact_sha256"] == execution_hash


def test_jcs_uses_utf16_property_order() -> None:
    # U+10000 sorts before U+E000 by UTF-16 code units, unlike code-point order.
    value = {"\ue000": 1, "\U00010000": 2}
    assert validator.jcs_bytes(value).decode("utf-8") == '{"𐀀":2,"":1}'


def test_missing_schema_fails_closed_as_internal_error() -> None:
    with tempfile.TemporaryDirectory(prefix="resume-gate-test-") as temp:
        result, _, _ = validator.validate_manifest(
            PILOT / "manifest.draft.json",
            REPO_ROOT,
            schema_dir=pathlib.Path(temp),
        )
        assert_code(result, "VALIDATOR_INTERNAL_ERROR")


def test_cli_exit_codes_and_json_stdout() -> None:
    manifest = frozen_pilot_manifest()
    submission = efdc_submission(manifest)

    def check(_temp: pathlib.Path, manifest_path: pathlib.Path, submission_path: pathlib.Path) -> None:
        positive = subprocess.run(
            [
                sys.executable,
                str(VALIDATOR_PATH),
                "submission",
                "--repo-root",
                str(REPO_ROOT),
                "--manifest",
                str(manifest_path),
                "--submission",
                str(submission_path),
                "--launcher-run-id",
                submission["run_id"],
            ],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
            text=True,
        )
        assert positive.returncode == 0, positive.stderr + positive.stdout
        assert json.loads(positive.stdout)["status"] == "PASS"

        negative = subprocess.run(
            [
                sys.executable,
                str(VALIDATOR_PATH),
                "manifest",
                "--repo-root",
                str(REPO_ROOT),
                "--manifest",
                str(PILOT / "parser-negative-duplicate-source.manifest.json"),
            ],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
            text=True,
        )
        assert negative.returncode == 1, negative.stderr + negative.stdout
        assert json.loads(negative.stdout)["failure_codes"] == ["JSON_DUPLICATE_KEY"]

    with_pair(manifest, submission, submission["run_id"], check)


TESTS = [
    test_positive_manifest_and_code_submission,
    test_pdf_ligature_nfkc_and_single_physical_page,
    test_parser_negative_control_duplicate_precedes_schema,
    test_canary_control_is_deterministically_valid_but_semantically_unjudged,
    test_draft_is_schema_invalid_for_tbd_controls,
    test_json_syntax_error,
    test_contract_version_schema_mapping,
    test_work_item_unknown,
    test_registered_source_absent_from_work_items,
    test_locator_reversed,
    test_symlink_escape,
    test_source_missing,
    test_source_hash_mismatch,
    test_code_locator_out_of_range,
    test_pdf_locator_out_of_range,
    test_invalid_pdf_extraction,
    test_manifest_binding_mismatch,
    test_run_id_mismatch,
    test_locator_not_registered,
    test_candidate_source_unknown,
    test_code_quote_mismatch,
    test_pdf_quote_mismatch,
    test_canonicalization_rejects_lone_surrogate,
    test_failure_code_enum_shape_and_artifact_hashes,
    test_jcs_uses_utf16_property_order,
    test_missing_schema_fails_closed_as_internal_error,
    test_cli_exit_codes_and_json_stdout,
]


def main() -> int:
    failures: list[str] = []
    for test in TESTS:
        try:
            test()
        except Exception as error:
            failures.append(f"{test.__name__}: {type(error).__name__}: {error}")
            print(f"[WRONG] {failures[-1]}")
        else:
            print(f"[ok] {test.__name__}")
    print(f"\n{len(TESTS) - len(failures)}/{len(TESTS)} validator fixtures behaved as required")
    if failures:
        print("FAILURES:")
        for failure in failures:
            print(f"- {failure}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
