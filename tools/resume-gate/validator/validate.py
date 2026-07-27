#!/usr/bin/env python3
"""Deterministic stage-3 validator for resume-gate.

This module deliberately has no judge adapter or network client.  It performs
strict JSON decoding, Draft 2020-12 validation, cross-document binding, source
integrity checks, and exact source-anchor checks.  A deterministic failure is
terminal input to later stages; no result here can be overridden by a judge.

CLI:
  validate.py manifest --repo-root ROOT --manifest MANIFEST
  validate.py submission --repo-root ROOT --manifest MANIFEST \
      --submission SUBMISSION --launcher-run-id RUN_ID
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import pathlib
import subprocess
import sys
import unicodedata
from dataclasses import dataclass
from enum import Enum
from typing import Any, Callable, Iterable, Sequence

from jsonschema import Draft202012Validator


CONTRACT_VERSION = "resume-gate/1"
PDFTOTEXT = "/usr/bin/pdftotext"
MAX_JCS_INTEGER = 9_007_199_254_740_991
_INSTALL_ROOT = pathlib.Path(__file__).resolve().parents[1]
DEFAULT_SCHEMA_DIR = (
    _INSTALL_ROOT / "schemas"
    if (_INSTALL_ROOT / "schemas").is_dir()
    else _INSTALL_ROOT / "share" / "schemas"
)


class FailureCode(str, Enum):
    """Stable stage-3 failure-code vocabulary.

    Values are serialized verbatim and satisfy ^[A-Z][A-Z0-9_]{2,63}$.
    """

    JSON_DECODE_ERROR = "JSON_DECODE_ERROR"
    JSON_DUPLICATE_KEY = "JSON_DUPLICATE_KEY"
    SCHEMA_VALIDATION_FAILED = "SCHEMA_VALIDATION_FAILED"
    CANONICALIZATION_ERROR = "CANONICALIZATION_ERROR"
    CONTRACT_VERSION_MISMATCH = "CONTRACT_VERSION_MISMATCH"
    MANIFEST_BINDING_MISMATCH = "MANIFEST_BINDING_MISMATCH"
    RUN_ID_MISMATCH = "RUN_ID_MISMATCH"
    SOURCE_ID_UNKNOWN = "SOURCE_ID_UNKNOWN"
    LOCATOR_NOT_REGISTERED = "LOCATOR_NOT_REGISTERED"
    LOCATOR_RANGE_REVERSED = "LOCATOR_RANGE_REVERSED"
    PATH_OUTSIDE_PROTECTED_ROOT = "PATH_OUTSIDE_PROTECTED_ROOT"
    SOURCE_READ_ERROR = "SOURCE_READ_ERROR"
    SOURCE_HASH_MISMATCH = "SOURCE_HASH_MISMATCH"
    LOCATOR_OUT_OF_RANGE = "LOCATOR_OUT_OF_RANGE"
    QUOTE_MISMATCH = "QUOTE_MISMATCH"
    PDF_EXTRACTION_FAILED = "PDF_EXTRACTION_FAILED"
    CANARY_FABRICATED_CLAIM = "CANARY_FABRICATED_CLAIM"
    VALIDATOR_INTERNAL_ERROR = "VALIDATOR_INTERNAL_ERROR"


FAILURE_CODE_ORDER = {code: index for index, code in enumerate(FailureCode)}


@dataclass(frozen=True)
class Issue:
    code: FailureCode
    detail: str

    def as_dict(self) -> dict[str, str]:
        return {"code": self.code.value, "detail": self.detail}


class DuplicateKeyError(ValueError):
    pass


class CanonicalizationError(ValueError):
    pass


def _reject_duplicate_keys(pairs: Iterable[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise DuplicateKeyError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def _reject_json_constant(value: str) -> None:
    raise ValueError(f"non-finite JSON number: {value}")


def strict_json_load_bytes(raw: bytes, label: str) -> tuple[Any | None, list[Issue]]:
    """Decode UTF-8 JSON without ever overwriting a duplicate object key."""

    try:
        text = raw.decode("utf-8", errors="strict")
        value = json.loads(
            text,
            object_pairs_hook=_reject_duplicate_keys,
            parse_constant=_reject_json_constant,
        )
        return value, []
    except DuplicateKeyError as error:
        return None, [Issue(FailureCode.JSON_DUPLICATE_KEY, f"{label}: {error}")]
    except (UnicodeDecodeError, json.JSONDecodeError, ValueError) as error:
        return None, [Issue(FailureCode.JSON_DECODE_ERROR, f"{label}: {error}")]


def strict_json_load_path(path: pathlib.Path, label: str) -> tuple[Any | None, list[Issue]]:
    try:
        raw = path.read_bytes()
    except OSError as error:
        return None, [Issue(FailureCode.SOURCE_READ_ERROR, f"{label}: {error}")]
    return strict_json_load_bytes(raw, label)


def _check_jcs_value(value: Any, path: str = "$") -> None:
    if value is None or isinstance(value, bool):
        return
    if isinstance(value, int):
        if not -MAX_JCS_INTEGER <= value <= MAX_JCS_INTEGER:
            raise CanonicalizationError(f"{path}: integer is outside the RFC 8785 interoperable range")
        return
    if isinstance(value, float):
        raise CanonicalizationError(f"{path}: floating-point values are not used by resume-gate schemas")
    if isinstance(value, str):
        try:
            value.encode("utf-8", errors="strict")
        except UnicodeEncodeError as error:
            raise CanonicalizationError(f"{path}: non-Unicode scalar string: {error}") from error
        return
    if isinstance(value, list):
        for index, item in enumerate(value):
            _check_jcs_value(item, f"{path}[{index}]")
        return
    if isinstance(value, dict):
        for key, item in value.items():
            if not isinstance(key, str):
                raise CanonicalizationError(f"{path}: object key is not a string")
            _check_jcs_value(key, f"{path}.<key>")
            _check_jcs_value(item, f"{path}.{key}")
        return
    raise CanonicalizationError(f"{path}: unsupported JSON value type {type(value).__name__}")


def _jcs_text(value: Any) -> str:
    if value is None:
        return "null"
    if value is True:
        return "true"
    if value is False:
        return "false"
    if isinstance(value, int):
        return str(value)
    if isinstance(value, str):
        return json.dumps(value, ensure_ascii=False, separators=(",", ":"))
    if isinstance(value, list):
        return "[" + ",".join(_jcs_text(item) for item in value) + "]"
    if isinstance(value, dict):
        # RFC 8785 follows ECMAScript/UTF-16 code-unit property ordering.
        keys = sorted(value, key=lambda key: key.encode("utf-16-be", errors="strict"))
        return "{" + ",".join(
            f"{_jcs_text(key)}:{_jcs_text(value[key])}" for key in keys
        ) + "}"
    raise CanonicalizationError(f"unsupported JSON value type {type(value).__name__}")


def jcs_bytes(value: Any) -> bytes:
    """Return RFC 8785 bytes for the integer-only resume-gate schemas."""

    _check_jcs_value(value)
    try:
        return _jcs_text(value).encode("utf-8", errors="strict")
    except (TypeError, ValueError, UnicodeEncodeError) as error:
        raise CanonicalizationError(str(error)) from error


def jcs_sha256(value: Any) -> str:
    return hashlib.sha256(jcs_bytes(value)).hexdigest()


def file_sha256(path: pathlib.Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def normalize_quote(text: str) -> str:
    """Normalize ligatures/compatibility forms and all whitespace for matching."""

    return " ".join(unicodedata.normalize("NFKC", text).split())


def _json_path(parts: Sequence[Any]) -> str:
    result = "$"
    for part in parts:
        if isinstance(part, int):
            result += f"[{part}]"
        else:
            result += f".{part}"
    return result


def _schema_issues(
    instance: Any,
    schema: dict[str, Any],
    label: str,
) -> list[Issue]:
    errors = sorted(
        Draft202012Validator(schema).iter_errors(instance),
        key=lambda error: (tuple(str(item) for item in error.absolute_path), error.message),
    )
    issues: list[Issue] = []
    for error in errors:
        code = FailureCode.SCHEMA_VALIDATION_FAILED
        if (
            error.validator == "const"
            and error.absolute_path
            and list(error.absolute_path)[-1] == "contract_version"
        ):
            code = FailureCode.CONTRACT_VERSION_MISMATCH
        issues.append(
            Issue(
                code,
                f"{label}{_json_path(list(error.absolute_path))[1:]}: {error.message}",
            )
        )
    return issues


def _load_schemas(schema_dir: pathlib.Path) -> tuple[dict[str, Any] | None, dict[str, Any] | None, list[Issue]]:
    loaded: dict[str, dict[str, Any]] = {}
    issues: list[Issue] = []
    for kind in ("manifest", "submission"):
        path = schema_dir / f"{kind}.schema.json"
        value, load_issues = strict_json_load_path(path, f"{kind} schema")
        if load_issues:
            for issue in load_issues:
                issues.append(
                    Issue(
                        FailureCode.VALIDATOR_INTERNAL_ERROR,
                        f"{kind} schema could not be loaded safely: {issue.detail}",
                    )
                )
            continue
        if not isinstance(value, dict):
            issues.append(
                Issue(FailureCode.VALIDATOR_INTERNAL_ERROR, f"{kind} schema: top level is not an object")
            )
            continue
        try:
            Draft202012Validator.check_schema(value)
        except Exception as error:
            issues.append(
                Issue(FailureCode.VALIDATOR_INTERNAL_ERROR, f"{kind} schema is invalid: {error}")
            )
            continue
        loaded[kind] = value
    return loaded.get("manifest"), loaded.get("submission"), issues


def _deduplicate_issues(issues: Iterable[Issue]) -> list[Issue]:
    unique = {(issue.code, issue.detail): issue for issue in issues}
    return sorted(
        unique.values(),
        key=lambda issue: (FAILURE_CODE_ORDER[issue.code], issue.detail),
    )


def result_dict(
    issues: Iterable[Issue],
    *,
    manifest_sha256: str | None = None,
    submission_sha256: str | None = None,
) -> dict[str, Any]:
    ordered = _deduplicate_issues(issues)
    codes = sorted(
        {issue.code for issue in ordered},
        key=lambda code: FAILURE_CODE_ORDER[code],
    )
    result: dict[str, Any] = {
        "status": "FAIL" if ordered else "PASS",
        "failure_codes": [code.value for code in codes],
        "issues": [issue.as_dict() for issue in ordered],
    }
    if manifest_sha256 is not None:
        result["manifest_sha256"] = manifest_sha256
    if submission_sha256 is not None:
        result["submission_sha256"] = submission_sha256
    return result


def _range_issues(locator: dict[str, Any], label: str) -> list[Issue]:
    if locator["start"] > locator["end"]:
        return [
            Issue(
                FailureCode.LOCATOR_RANGE_REVERSED,
                f"{label}: start {locator['start']} is greater than end {locator['end']}",
            )
        ]
    return []


def _manifest_membership_issues(manifest: dict[str, Any]) -> list[Issue]:
    issues: list[Issue] = []
    work_items = set(manifest["work_items"])
    source_ids = set(manifest["sources"])
    for source_id in sorted(work_items - source_ids):
        issues.append(
            Issue(FailureCode.SOURCE_ID_UNKNOWN, f"work_items source is not registered: {source_id}")
        )
    for source_id in sorted(source_ids - work_items):
        issues.append(
            Issue(FailureCode.SOURCE_ID_UNKNOWN, f"registered source is absent from work_items: {source_id}")
        )

    for source_id, source in sorted(manifest["sources"].items()):
        for index, locator in enumerate(source["locators"]):
            issues.extend(_range_issues(locator, f"sources.{source_id}.locators[{index}]"))

    canary = manifest["controls"]["canary"]
    canary_source_id = canary["source_id"]
    if canary_source_id not in manifest["sources"]:
        issues.append(
            Issue(FailureCode.SOURCE_ID_UNKNOWN, f"canary source is not registered: {canary_source_id}")
        )
    else:
        issues.extend(_range_issues(canary["locator"], "controls.canary.locator"))
        if canary["locator"] not in manifest["sources"][canary_source_id]["locators"]:
            issues.append(
                Issue(
                    FailureCode.LOCATOR_NOT_REGISTERED,
                    f"controls.canary.locator is not registered for {canary_source_id}",
                )
            )

    mutation = manifest["controls"]["parser_negative"]["mutation"]
    if mutation["operation"] == "duplicate_key" and mutation["target"].startswith("sources."):
        target_source_id = mutation["target"][len("sources.") :]
        if target_source_id not in manifest["sources"]:
            issues.append(
                Issue(
                    FailureCode.SOURCE_ID_UNKNOWN,
                    f"parser-negative target source is not registered: {target_source_id}",
                )
            )
    return issues


def _resolve_source(repo_root: pathlib.Path, relative_path: str, source_id: str) -> tuple[pathlib.Path | None, list[Issue]]:
    try:
        root = repo_root.resolve(strict=True)
    except OSError as error:
        return None, [
            Issue(FailureCode.PATH_OUTSIDE_PROTECTED_ROOT, f"protected root cannot be resolved: {error}")
        ]

    candidate = root / relative_path
    try:
        resolved = candidate.resolve(strict=False)
        contained = os.path.commonpath((str(root), str(resolved))) == str(root)
    except (OSError, ValueError) as error:
        return None, [
            Issue(
                FailureCode.PATH_OUTSIDE_PROTECTED_ROOT,
                f"{source_id}: cannot resolve {relative_path}: {error}",
            )
        ]
    if not contained:
        return None, [
            Issue(
                FailureCode.PATH_OUTSIDE_PROTECTED_ROOT,
                f"{source_id}: realpath escapes protected root: {relative_path} -> {resolved}",
            )
        ]
    if not resolved.is_file():
        return None, [
            Issue(FailureCode.SOURCE_READ_ERROR, f"{source_id}: source is not a regular file: {relative_path}")
        ]
    return resolved, []


PdfRunner = Callable[..., subprocess.CompletedProcess[bytes]]


def _pdftotext_once(path: pathlib.Path, page: int, runner: PdfRunner) -> subprocess.CompletedProcess[bytes]:
    argv = [PDFTOTEXT, "-f", str(page), "-l", str(page), str(path), "-"]
    return runner(
        argv,
        stdin=subprocess.DEVNULL,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        shell=False,
        check=False,
        timeout=30,
    )


def _extract_pdf_page(
    path: pathlib.Path,
    page: int,
    source_id: str,
    runner: PdfRunner,
) -> tuple[str | None, list[Issue]]:
    """Extract exactly one physical, one-based page; never split whole-document output."""

    try:
        completed = _pdftotext_once(path, page, runner)
    except (OSError, subprocess.SubprocessError) as error:
        return None, [
            Issue(FailureCode.PDF_EXTRACTION_FAILED, f"{source_id} page {page}: {error}")
        ]
    if completed.returncode != 0:
        if page > 1:
            try:
                page_one = _pdftotext_once(path, 1, runner)
            except (OSError, subprocess.SubprocessError):
                page_one = None
            if page_one is not None and page_one.returncode == 0:
                return None, [
                    Issue(
                        FailureCode.LOCATOR_OUT_OF_RANGE,
                        f"{source_id}: physical page {page} is outside the PDF",
                    )
                ]
        stderr = completed.stderr.decode("utf-8", errors="replace").strip()
        return None, [
            Issue(
                FailureCode.PDF_EXTRACTION_FAILED,
                f"{source_id} page {page}: pdftotext exit {completed.returncode}: {stderr}",
            )
        ]
    try:
        return completed.stdout.decode("utf-8", errors="strict"), []
    except UnicodeDecodeError as error:
        return None, [
            Issue(
                FailureCode.PDF_EXTRACTION_FAILED,
                f"{source_id} page {page}: stdout is not UTF-8: {error}",
            )
        ]


@dataclass
class SourceSnapshot:
    source_id: str
    artifact_type: str
    path: pathlib.Path
    text: str | None = None
    lines: list[str] | None = None
    pages: dict[int, str] | None = None


def _validate_sources(
    manifest: dict[str, Any],
    repo_root: pathlib.Path,
    pdf_runner: PdfRunner,
) -> tuple[dict[str, SourceSnapshot], list[Issue]]:
    snapshots: dict[str, SourceSnapshot] = {}
    issues: list[Issue] = []
    for source_id, source in sorted(manifest["sources"].items()):
        path, path_issues = _resolve_source(repo_root, source["path"], source_id)
        issues.extend(path_issues)
        if path is None:
            continue
        try:
            actual_sha256 = file_sha256(path)
        except OSError as error:
            issues.append(Issue(FailureCode.SOURCE_READ_ERROR, f"{source_id}: {error}"))
            continue
        if actual_sha256 != source["sha256"]:
            issues.append(
                Issue(
                    FailureCode.SOURCE_HASH_MISMATCH,
                    f"{source_id}: expected {source['sha256']}, got {actual_sha256}",
                )
            )
            continue

        if source["artifact_type"] == "code":
            try:
                text = path.read_bytes().decode("utf-8", errors="strict")
            except (OSError, UnicodeDecodeError) as error:
                issues.append(Issue(FailureCode.SOURCE_READ_ERROR, f"{source_id}: {error}"))
                continue
            lines = text.splitlines()
            snapshot = SourceSnapshot(source_id, "code", path, text=text, lines=lines)
            snapshots[source_id] = snapshot
            for locator in source["locators"]:
                if locator["end"] > len(lines):
                    issues.append(
                        Issue(
                            FailureCode.LOCATOR_OUT_OF_RANGE,
                            f"{source_id}: line {locator['end']} exceeds {len(lines)} lines",
                        )
                    )
        else:
            snapshot = SourceSnapshot(source_id, "pdf", path, pages={})
            snapshots[source_id] = snapshot
            for locator in source["locators"]:
                if locator["start"] > locator["end"]:
                    continue
                for page in range(locator["start"], locator["end"] + 1):
                    if page in snapshot.pages:
                        continue
                    page_text, page_issues = _extract_pdf_page(path, page, source_id, pdf_runner)
                    issues.extend(page_issues)
                    if page_text is not None:
                        snapshot.pages[page] = page_text
    return snapshots, issues


def _validate_evidence(
    manifest: dict[str, Any],
    submission: dict[str, Any],
    snapshots: dict[str, SourceSnapshot],
) -> list[Issue]:
    issues: list[Issue] = []
    source_id = submission["candidate"]["source_id"]
    if source_id not in manifest["sources"] or source_id not in manifest["work_items"]:
        return [Issue(FailureCode.SOURCE_ID_UNKNOWN, f"candidate source is not a work item: {source_id}")]

    registered = manifest["sources"][source_id]["locators"]
    snapshot = snapshots.get(source_id)
    for index, evidence in enumerate(submission["evidence"]):
        locator = evidence["locator"]
        label = f"evidence[{index}]"
        issues.extend(_range_issues(locator, f"{label}.locator"))
        if locator not in registered:
            issues.append(
                Issue(
                    FailureCode.LOCATOR_NOT_REGISTERED,
                    f"{label}.locator is not registered for {source_id}",
                )
            )
            continue
        if snapshot is None:
            continue

        slice_text: str | None = None
        if snapshot.artifact_type == "code":
            assert snapshot.lines is not None
            if locator["end"] > len(snapshot.lines):
                issues.append(
                    Issue(
                        FailureCode.LOCATOR_OUT_OF_RANGE,
                        f"{label}: line {locator['end']} exceeds {len(snapshot.lines)} lines",
                    )
                )
                continue
            slice_text = "\n".join(snapshot.lines[locator["start"] - 1 : locator["end"]])
        else:
            assert snapshot.pages is not None
            page_texts = []
            missing = False
            for page in range(locator["start"], locator["end"] + 1):
                if page not in snapshot.pages:
                    missing = True
                    break
                page_texts.append(snapshot.pages[page])
            if missing:
                continue
            slice_text = "\n".join(page_texts)

        quote = normalize_quote(evidence["quote"])
        source_slice = normalize_quote(slice_text)
        if quote not in source_slice:
            issues.append(
                Issue(
                    FailureCode.QUOTE_MISMATCH,
                    f"{label}: normalized quote is absent from {source_id} locator",
                )
            )
    return issues


def validate_manifest(
    manifest_path: pathlib.Path,
    repo_root: pathlib.Path,
    *,
    schema_dir: pathlib.Path = DEFAULT_SCHEMA_DIR,
    pdf_runner: PdfRunner = subprocess.run,
) -> tuple[dict[str, Any], dict[str, Any] | None, dict[str, SourceSnapshot]]:
    """Validate a manifest and all protected sources.

    The returned tuple is (serialized_result, decoded_manifest, snapshots).
    """

    manifest_schema, _, schema_issues = _load_schemas(schema_dir)
    if schema_issues or manifest_schema is None:
        return result_dict(schema_issues), None, {}

    manifest, decode_issues = strict_json_load_path(manifest_path, "manifest")
    if decode_issues:
        return result_dict(decode_issues), None, {}
    schema_validation_issues = _schema_issues(manifest, manifest_schema, "manifest")
    if schema_validation_issues:
        return result_dict(schema_validation_issues), manifest, {}

    try:
        manifest_hash = jcs_sha256(manifest)
    except CanonicalizationError as error:
        return result_dict(
            [Issue(FailureCode.CANONICALIZATION_ERROR, f"manifest: {error}")]
        ), manifest, {}

    issues = _manifest_membership_issues(manifest)
    if issues:
        return result_dict(issues, manifest_sha256=manifest_hash), manifest, {}
    snapshots, source_issues = _validate_sources(manifest, repo_root, pdf_runner)
    return (
        result_dict(source_issues, manifest_sha256=manifest_hash),
        manifest,
        snapshots,
    )


def validate_submission(
    manifest_path: pathlib.Path,
    submission_path: pathlib.Path,
    repo_root: pathlib.Path,
    launcher_run_id: str,
    *,
    schema_dir: pathlib.Path = DEFAULT_SCHEMA_DIR,
    pdf_runner: PdfRunner = subprocess.run,
) -> dict[str, Any]:
    """Validate exact manifest/submission binding and every submitted quote."""

    manifest_result, manifest, snapshots = validate_manifest(
        manifest_path,
        repo_root,
        schema_dir=schema_dir,
        pdf_runner=pdf_runner,
    )
    if manifest_result["status"] != "PASS" or manifest is None:
        return manifest_result

    _, submission_schema, schema_issues = _load_schemas(schema_dir)
    if schema_issues or submission_schema is None:
        return result_dict(schema_issues, manifest_sha256=manifest_result.get("manifest_sha256"))

    submission, decode_issues = strict_json_load_path(submission_path, "submission")
    if decode_issues:
        return result_dict(decode_issues, manifest_sha256=manifest_result["manifest_sha256"])
    submission_schema_issues = _schema_issues(submission, submission_schema, "submission")
    if submission_schema_issues:
        return result_dict(
            submission_schema_issues,
            manifest_sha256=manifest_result["manifest_sha256"],
        )

    try:
        submission_hash = jcs_sha256(submission)
    except CanonicalizationError as error:
        return result_dict(
            [Issue(FailureCode.CANONICALIZATION_ERROR, f"submission: {error}")],
            manifest_sha256=manifest_result["manifest_sha256"],
        )

    issues: list[Issue] = []
    if submission["contract_version"] != manifest["contract_version"]:
        issues.append(
            Issue(
                FailureCode.CONTRACT_VERSION_MISMATCH,
                "submission contract_version does not equal manifest contract_version",
            )
        )
    expected_binding = {
        "manifest_id": manifest["manifest_id"],
        "sha256": manifest_result["manifest_sha256"],
    }
    if submission["manifest"] != expected_binding:
        issues.append(
            Issue(
                FailureCode.MANIFEST_BINDING_MISMATCH,
                f"submission manifest binding does not equal {expected_binding}",
            )
        )
    if submission["run_id"] != launcher_run_id:
        issues.append(
            Issue(
                FailureCode.RUN_ID_MISMATCH,
                f"submission run_id {submission['run_id']!r} does not equal launcher run_id {launcher_run_id!r}",
            )
        )
    issues.extend(_validate_evidence(manifest, submission, snapshots))
    return result_dict(
        issues,
        manifest_sha256=manifest_result["manifest_sha256"],
        submission_sha256=submission_hash,
    )


def _internal_error(error: BaseException) -> dict[str, Any]:
    return result_dict(
        [
            Issue(
                FailureCode.VALIDATOR_INTERNAL_ERROR,
                f"{type(error).__name__}: {error}",
            )
        ]
    )


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)
    for command in ("manifest", "submission"):
        child = subparsers.add_parser(command)
        child.add_argument("--repo-root", required=True, type=pathlib.Path)
        child.add_argument("--manifest", required=True, type=pathlib.Path)
        if command == "submission":
            child.add_argument("--submission", required=True, type=pathlib.Path)
            child.add_argument("--launcher-run-id", required=True)
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        if args.command == "manifest":
            result, _, _ = validate_manifest(
                args.manifest,
                args.repo_root,
            )
        else:
            result = validate_submission(
                args.manifest,
                args.submission,
                args.repo_root,
                args.launcher_run_id,
            )
    except BaseException as error:
        result = _internal_error(error)
    print(json.dumps(result, ensure_ascii=False, sort_keys=True, separators=(",", ":")))
    return 0 if result["status"] == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())
