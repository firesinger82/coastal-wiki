#!/usr/bin/env python3
"""Runtime contract fixtures for resume-gate step 1.

The schema cases use the real Draft 2020-12 jsonschema validator and assert not
only rejection but the expected failing keyword/message. Two boundaries that
JSON Schema cannot express are exercised separately: duplicate JSON object keys
at decoding time and numeric start <= end comparison at stage 3.

Run: .venv/bin/python tools/resume-gate/tests/test_schemas.py
"""
from __future__ import annotations

import copy
import json
import pathlib
import sys
from dataclasses import dataclass
from typing import Any

from jsonschema import Draft202012Validator, ValidationError

ROOT = pathlib.Path(__file__).resolve().parents[1]
SCHEMAS = ROOT / "schemas"


def load(name: str) -> dict[str, Any]:
    return json.loads((SCHEMAS / name).read_text(encoding="utf-8"))


SUB = load("submission.schema.json")
JUD = load("judge.schema.json")
DEC = load("decision.schema.json")
MAN = load("manifest.schema.json")
SCHEMA_SET = {"submission": SUB, "judge": JUD, "decision": DEC, "manifest": MAN}


for schema_name, schema in SCHEMA_SET.items():
    Draft202012Validator.check_schema(schema)


VALID_SUB = {
    "schema_version": 1,
    "contract_version": "resume-gate/1",
    "manifest": {"manifest_id": "pilot-0001", "sha256": "1" * 64},
    "run_id": "run-000001ab",
    "candidate": {
        "source_id": "swan_bqf",
        "claim": "write field 3 is iq_geom",
        "claim_type": "explicit",
    },
    "evidence": [
        {
            "locator": {"type": "line_range", "start": 4570, "end": 4570},
            "quote": "write(luq_bqf) iq_geom,iq_disp,iq_geom",
        }
    ],
    "attempt_reason": "first read of BQF record fields",
}

VALID_JUDGE = {
    "schema_version": 1,
    "contract_version": "resume-gate/1",
    "manifest": {"manifest_id": "pilot-0001", "sha256": "1" * 64},
    "submission_sha256": "2" * 64,
    "judge": "codex",
    "engine_version": "codex-2026-07-25",
    "verdict": "FAIL",
    "claim_supported_by_evidence": False,
    "reasoning": "the cited write line does not support the uncited read-field claim",
    "issues": ["no read anchor cited"],
}

VALID_DECISION = {
    "schema_version": 1,
    "contract_version": "resume-gate/1",
    "run_id": "run-000001ab",
    "attempt_id": 1,
    "provenance": {
        "manifest": {"schema_version": 1, "manifest_id": "pilot-0001", "sha256": "1" * 64},
        "submission": {"schema_version": 1, "sha256": "2" * 64},
        "judges": {
            "codex": {"schema_version": 1, "engine_version": "codex-2026-07-25", "result_sha256": "3" * 64},
            "grok": {"schema_version": 1, "engine_version": "grok-2026-07-25", "result_sha256": "4" * 64},
        },
        "decision_engine_version": "resume-gate-engine/1.0.0",
    },
    "inputs": {
        "deterministic": {"status": "PASS", "failure_codes": []},
        "codex": {"verdict": "PASS"},
        "grok": {"verdict": "PASS"},
        "canary": {
            "control_id": "canary-0001",
            "status": "CAUGHT",
            "failure_codes": ["CANARY_DETECTED"],
            "input_artifact_sha256": "5" * 64,
            "execution_artifact_sha256": "6" * 64,
        },
        "parser_negative": {
            "control_id": "parser-0001",
            "status": "REJECTED",
            "failure_codes": ["PARSER_NEGATIVE_REJECTED"],
            "input_artifact_sha256": "7" * 64,
            "execution_artifact_sha256": "8" * 64,
        },
        "evidence_chain": {"status": "VALID", "provenance_sha256": "9" * 64},
    },
    "status": "PASS",
    "chain_root": "a" * 64,
}

VALID_MANIFEST = {
    "schema_version": 1,
    "contract_version": "resume-gate/1",
    "manifest_id": "pilot-0001",
    "run_scope": "pilot code and PDF work items",
    "work_items": ["swan_bqf", "swan_manual"],
    "sources": {
        "swan_bqf": {
            "path": "protected/swan/src/mod_xnl4v5.ftn90",
            "sha256": "b" * 64,
            "artifact_type": "code",
            "locators": [{"type": "line_range", "start": 4570, "end": 4570}],
        },
        "swan_manual": {
            "path": "protected/swan/manual.pdf",
            "sha256": "c" * 64,
            "artifact_type": "pdf",
            "locators": [{"type": "page_range", "start": 12, "end": 14}],
        },
    },
    "controls": {
        "canary": {
            "control_id": "canary-0001",
            "kind": "canary",
            "source_id": "swan_bqf",
            "locator": {"type": "line_range", "start": 4570, "end": 4570},
            "expected_status": "CAUGHT",
            "allowed_failure_codes": ["CANARY_DETECTED"],
            "input_artifact_sha256": "5" * 64,
            "execution_artifact_sha256": "6" * 64,
        },
        "parser_negative": {
            "control_id": "parser-0001",
            "kind": "parser_negative",
            "mutation": {
                "mutation_id": "mutation-0001",
                "operation": "duplicate_key",
                "target": "submission.candidate.claim",
            },
            "expected_status": "REJECTED",
            "allowed_failure_codes": ["JSON_DUPLICATE_KEY"],
            "input_artifact_sha256": "7" * 64,
            "execution_artifact_sha256": "8" * 64,
        },
    },
}


def changed(instance: dict[str, Any], mutator) -> dict[str, Any]:
    result = copy.deepcopy(instance)
    mutator(result)
    return result


@dataclass(frozen=True)
class SchemaCase:
    name: str
    schema: dict[str, Any]
    instance: dict[str, Any]
    expected_valid: bool
    validator: str | None = None
    message: str | None = None


def leaves(error: ValidationError):
    yield error
    for child in error.context:
        yield from leaves(child)


def errors_for(schema: dict[str, Any], instance: dict[str, Any]) -> list[ValidationError]:
    return list(Draft202012Validator(schema).iter_errors(instance))


def invalid_case(name, schema, instance, validator, message=None):
    return SchemaCase(name, schema, instance, False, validator, message)


POSITIVE_CASES = [
    SchemaCase("submission valid", SUB, VALID_SUB, True),
    SchemaCase("judge valid FAIL", JUD, VALID_JUDGE, True),
    SchemaCase(
        "judge valid PASS",
        JUD,
        changed(VALID_JUDGE, lambda x: x.update(verdict="PASS", claim_supported_by_evidence=True, issues=[])),
        True,
    ),
    SchemaCase("decision valid PASS", DEC, VALID_DECISION, True),
    SchemaCase(
        "decision valid non-PASS",
        DEC,
        changed(VALID_DECISION, lambda x: (x.update(status="FAIL"), x["inputs"]["grok"].update(verdict="FAIL"))),
        True,
    ),
    SchemaCase("manifest valid", MAN, VALID_MANIFEST, True),
]


SCHEMA_NEGATIVES = [
    # Worker authority/smuggling surface.
    invalid_case("submission authority complete", SUB, {**VALID_SUB, "complete": True}, "additionalProperties", "complete"),
    invalid_case("submission authority reader", SUB, {**VALID_SUB, "reader": "claude"}, "additionalProperties", "reader"),
    invalid_case("submission authority status", SUB, {**VALID_SUB, "status": "PASS"}, "additionalProperties", "status"),
    invalid_case(
        "submission authority verified confidence",
        SUB,
        {**VALID_SUB, "verified": True, "confidence": "high"},
        "additionalProperties",
        "verified",
    ),
    invalid_case("submission output path", SUB, {**VALID_SUB, "output_path": "/tmp/x"}, "additionalProperties", "output_path"),
    invalid_case("submission missing evidence", SUB, {k: v for k, v in VALID_SUB.items() if k != "evidence"}, "required", "evidence"),
    invalid_case("submission empty evidence", SUB, {**VALID_SUB, "evidence": []}, "minItems"),
    invalid_case("submission schema version", SUB, {**VALID_SUB, "schema_version": 2}, "const"),
    invalid_case("submission contract version", SUB, {**VALID_SUB, "contract_version": "resume-gate/2"}, "const"),
    invalid_case("submission bad run_id", SUB, {**VALID_SUB, "run_id": "short"}, "pattern"),
    invalid_case(
        "submission bad claim_type",
        SUB,
        changed(VALID_SUB, lambda x: x["candidate"].update(claim_type="guess")),
        "enum",
    ),
    invalid_case(
        "submission unknown locator type",
        SUB,
        changed(VALID_SUB, lambda x: x["evidence"][0].update(locator={"type": "byte_range", "start": 1, "end": 2})),
        "const",
    ),
    invalid_case(
        "submission empty quote",
        SUB,
        changed(VALID_SUB, lambda x: x["evidence"][0].update(quote="")),
        "pattern",
    ),
    invalid_case("submission whitespace claim", SUB, changed(VALID_SUB, lambda x: x["candidate"].update(claim=" \t ")), "pattern"),
    invalid_case("submission whitespace quote", SUB, changed(VALID_SUB, lambda x: x["evidence"][0].update(quote="   ")), "pattern"),
    invalid_case(
        "candidate evidence source mismatch unrepresentable",
        SUB,
        changed(VALID_SUB, lambda x: x["evidence"][0].update(source_id="other_source")),
        "additionalProperties",
        "source_id",
    ),
    invalid_case(
        "submission nested extra property",
        SUB,
        changed(VALID_SUB, lambda x: x["evidence"][0]["locator"].update(unit="line")),
        "additionalProperties",
        "unit",
    ),
    invalid_case("worker submission is not decision", DEC, VALID_SUB, "required", "attempt_id"),
    invalid_case("decision is not submission", SUB, VALID_DECISION, "required", "manifest"),
    # Judge PASS consistency.
    invalid_case(
        "judge PASS support false",
        JUD,
        changed(VALID_JUDGE, lambda x: x.update(verdict="PASS", claim_supported_by_evidence=False, issues=[])),
        "const",
    ),
    invalid_case(
        "judge PASS non-empty issues",
        JUD,
        changed(VALID_JUDGE, lambda x: x.update(verdict="PASS", claim_supported_by_evidence=True, issues=["contradiction"])),
        "maxItems",
    ),
    invalid_case("judge whitespace reasoning", JUD, changed(VALID_JUDGE, lambda x: x.update(reasoning="\n\t")), "pattern"),
    invalid_case("judge unknown verdict", JUD, {**VALID_JUDGE, "verdict": "MAYBE"}, "enum"),
    invalid_case(
        "judge missing verdict",
        JUD,
        {key: value for key, value in VALID_JUDGE.items() if key != "verdict"},
        "required",
        "verdict",
    ),
    invalid_case("judge extra field", JUD, {**VALID_JUDGE, "override": True}, "additionalProperties", "override"),
    # Six PASS truth-table inputs, each independently negative.
    invalid_case(
        "PASS with deterministic FAIL",
        DEC,
        changed(VALID_DECISION, lambda x: x["inputs"]["deterministic"].update(status="FAIL", failure_codes=["SOURCE_HASH_MISMATCH"])),
        "const",
    ),
    invalid_case("PASS with codex FAIL", DEC, changed(VALID_DECISION, lambda x: x["inputs"]["codex"].update(verdict="FAIL")), "const"),
    invalid_case("PASS with grok FAIL", DEC, changed(VALID_DECISION, lambda x: x["inputs"]["grok"].update(verdict="FAIL")), "const"),
    invalid_case("PASS with canary MISSED", DEC, changed(VALID_DECISION, lambda x: x["inputs"]["canary"].update(status="MISSED")), "const"),
    invalid_case(
        "PASS with parser-negative ACCEPTED",
        DEC,
        changed(VALID_DECISION, lambda x: x["inputs"]["parser_negative"].update(status="ACCEPTED")),
        "const",
    ),
    invalid_case(
        "PASS with evidence-chain INVALID",
        DEC,
        changed(VALID_DECISION, lambda x: x["inputs"]["evidence_chain"].update(status="INVALID")),
        "const",
    ),
    invalid_case(
        "all passing inputs cannot claim FAIL",
        DEC,
        changed(VALID_DECISION, lambda x: x.update(status="FAIL")),
        "const",
    ),
    invalid_case(
        "deterministic PASS with failure code",
        DEC,
        changed(VALID_DECISION, lambda x: x["inputs"]["deterministic"].update(failure_codes=["IMPOSSIBLE_PASS_CODE"])),
        "maxItems",
    ),
    invalid_case(
        "deterministic FAIL without failure code",
        DEC,
        changed(
            VALID_DECISION,
            lambda x: (x.update(status="FAIL"), x["inputs"]["deterministic"].update(status="FAIL", failure_codes=[])),
        ),
        "minItems",
    ),
    invalid_case(
        "decision missing provenance binding",
        DEC,
        changed(VALID_DECISION, lambda x: x["provenance"].pop("submission")),
        "required",
        "submission",
    ),
    invalid_case(
        "decision whitespace engine version",
        DEC,
        changed(VALID_DECISION, lambda x: x["provenance"].update(decision_engine_version="   ")),
        "pattern",
    ),
    invalid_case("decision bad status", DEC, {**VALID_DECISION, "status": "DONE"}, "enum"),
    invalid_case(
        "decision missing inputs",
        DEC,
        {key: value for key, value in VALID_DECISION.items() if key != "inputs"},
        "required",
        "inputs",
    ),
    # Fixed denominator and manifest structure.
    invalid_case(
        "legacy denominator mismatch unit1 denominator3",
        MAN,
        changed(
            VALID_MANIFEST,
            lambda x: (x.update(work_items=["swan_bqf"]), x.update(denominator={"code_units": 2, "pdf_claims": 1})),
        ),
        "additionalProperties",
        "denominator",
    ),
    invalid_case(
        "duplicate source_id work item",
        MAN,
        changed(VALID_MANIFEST, lambda x: x.update(work_items=["swan_bqf", "swan_bqf"])),
        "uniqueItems",
    ),
    invalid_case(
        "manifest bad source sha256",
        MAN,
        changed(VALID_MANIFEST, lambda x: x["sources"]["swan_bqf"].update(sha256="xyz")),
        "pattern",
    ),
    invalid_case(
        "manifest missing work_items",
        MAN,
        {key: value for key, value in VALID_MANIFEST.items() if key != "work_items"},
        "required",
        "work_items",
    ),
    invalid_case(
        "manifest unknown artifact_type",
        MAN,
        changed(VALID_MANIFEST, lambda x: x["sources"]["swan_bqf"].update(artifact_type="spreadsheet")),
        "enum",
    ),
    invalid_case(
        "code artifact with page locator",
        MAN,
        changed(VALID_MANIFEST, lambda x: x["sources"]["swan_bqf"].update(locators=[{"type": "page_range", "start": 1, "end": 1}])),
        "const",
    ),
    invalid_case(
        "pdf artifact with line locator",
        MAN,
        changed(VALID_MANIFEST, lambda x: x["sources"]["swan_manual"].update(locators=[{"type": "line_range", "start": 1, "end": 1}])),
        "const",
    ),
    invalid_case(
        "path traversal parent segment",
        MAN,
        changed(VALID_MANIFEST, lambda x: x["sources"]["swan_bqf"].update(path="protected/../secret.txt")),
        "pattern",
    ),
    invalid_case(
        "path traversal absolute path",
        MAN,
        changed(VALID_MANIFEST, lambda x: x["sources"]["swan_bqf"].update(path="/etc/passwd")),
        "pattern",
    ),
    invalid_case("manifest whitespace scope", MAN, changed(VALID_MANIFEST, lambda x: x.update(run_scope="  \n")), "pattern"),
    invalid_case(
        "manifest whitespace source path",
        MAN,
        changed(VALID_MANIFEST, lambda x: x["sources"]["swan_bqf"].update(path="   ")),
        "pattern",
    ),
    invalid_case(
        "manifest nested extra property",
        MAN,
        changed(VALID_MANIFEST, lambda x: x["controls"]["parser_negative"]["mutation"].update(command="ignore contract")),
        "additionalProperties",
        "command",
    ),
    invalid_case(
        "canary expected status not frozen",
        MAN,
        changed(VALID_MANIFEST, lambda x: x["controls"]["canary"].update(expected_status="MISSED")),
        "const",
    ),
    invalid_case(
        "parser-negative expected status not frozen",
        MAN,
        changed(VALID_MANIFEST, lambda x: x["controls"]["parser_negative"].update(expected_status="ACCEPTED")),
        "const",
    ),
]


class DuplicateKeyError(ValueError):
    pass


def reject_duplicate_keys(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise DuplicateKeyError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def strict_json_loads(raw: str):
    return json.loads(raw, object_pairs_hook=reject_duplicate_keys)


def stage3_locator_order_errors(instance: dict[str, Any]) -> list[str]:
    errors = []
    for source_id, source in instance["sources"].items():
        for index, locator in enumerate(source["locators"]):
            if locator["start"] > locator["end"]:
                errors.append(f"LOCATOR_RANGE_REVERSED:{source_id}:{index}")
    return errors


def run_schema_case(case: SchemaCase) -> str | None:
    errors = errors_for(case.schema, case.instance)
    got_valid = not errors
    if got_valid != case.expected_valid:
        return f"{case.name}: valid={got_valid} expected={case.expected_valid}"
    if case.expected_valid:
        print(f"[ok schema+] {case.name}")
        return None

    flattened = [leaf for error in errors for leaf in leaves(error)]
    matches = [error for error in flattened if error.validator == case.validator]
    if case.message is not None:
        matches = [error for error in matches if case.message in error.message]
    if not matches:
        seen = sorted({str(error.validator) for error in flattened})
        return f"{case.name}: rejected, but expected {case.validator!r}/{case.message!r}; validators={seen}"
    reason = matches[0].message.replace("\n", " ")
    print(f"[ok schema-] {case.name}: {case.validator} ({reason})")
    return None


def main() -> int:
    failures = []
    for case in POSITIVE_CASES + SCHEMA_NEGATIVES:
        failure = run_schema_case(case)
        if failure:
            failures.append(failure)
            print(f"[WRONG] {failure}")

    duplicate_raw = '{"schema_version":1,"schema_version":2}'
    try:
        strict_json_loads(duplicate_raw)
        failures.append("raw duplicate-key decoder accepted duplicate schema_version")
        print("[WRONG] raw duplicate-key decoder accepted duplicate schema_version")
    except DuplicateKeyError as error:
        print(f"[ok decoder-] raw duplicate key: {error}")

    reversed_range = changed(
        VALID_MANIFEST,
        lambda x: x["sources"]["swan_bqf"].update(locators=[{"type": "line_range", "start": 10, "end": 9}]),
    )
    if errors_for(MAN, reversed_range):
        failures.append("reversed-range boundary unexpectedly claimed as JSON-Schema-enforced")
        print("[WRONG] reversed range should reach the documented stage-3 comparison")
    else:
        stage3_errors = stage3_locator_order_errors(reversed_range)
        if stage3_errors != ["LOCATOR_RANGE_REVERSED:swan_bqf:0"]:
            failures.append(f"reversed range stage-3 result wrong: {stage3_errors}")
            print(f"[WRONG] reversed range stage-3 result: {stage3_errors}")
        else:
            print(f"[ok stage3-] reversed range: {stage3_errors[0]}")

    canonical_a = json.dumps(VALID_SUB, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    reordered = {key: VALID_SUB[key] for key in reversed(VALID_SUB)}
    canonical_b = json.dumps(reordered, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    if canonical_a != canonical_b:
        failures.append("canonical JSON differs under object-key reordering")
        print("[WRONG] canonical JSON ordering is unstable")
    else:
        print("[ok canonical] object-key ordering is stable")

    total = len(POSITIVE_CASES) + len(SCHEMA_NEGATIVES) + 3
    passed = total - len(failures)
    print(
        f"\n{passed}/{total} fixtures behaved as required "
        f"({len(POSITIVE_CASES)} schema-positive, {len(SCHEMA_NEGATIVES)} schema-negative, "
        "1 decoder-negative, 1 stage3-negative, 1 canonicalization)"
    )
    if failures:
        print("FAILURES:")
        for failure in failures:
            print(f"- {failure}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
