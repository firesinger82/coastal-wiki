#!/usr/bin/env python3
"""Fail-closed phase-5 decision engine for resume-gate.

The engine owns all state paths.  Worker input is only a submission JSON
document; paths, judge configuration, verdicts, and completion claims are not
accepted.  External judge execution is available only through an injected
callable, so this module has no subprocess or network execution path.
"""
from __future__ import annotations

import dataclasses
import hashlib
import importlib.util
import json
import os
import pathlib
import re
import sys
import tempfile
import unicodedata
from collections.abc import Callable, Mapping
from typing import Any, Protocol

from jsonschema import Draft202012Validator


ENGINE_DIR = pathlib.Path(__file__).resolve().parent
GATE_ROOT = ENGINE_DIR.parent
DEFAULT_SCHEMA_DIR = GATE_ROOT / "schemas"
DEFAULT_STATE_ROOT = pathlib.Path.home() / ".local" / "state" / "resume-gate"
ENGINE_VERSION = "resume-gate-engine/1"
CONTRACT_VERSION = "resume-gate/1"
ZERO_HASH = "0" * 64
RUN_ID_RE = re.compile(r"^[a-z0-9][a-z0-9_-]{7,63}$")
MAX_SUBMITS = 6


def _load_validator() -> Any:
    path = GATE_ROOT / "validator" / "validate.py"
    spec = importlib.util.spec_from_file_location("resume_gate_stage3_for_engine", path)
    if spec is None or spec.loader is None:
        raise RuntimeError("stage-3 validator cannot be loaded")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


deterministic = _load_validator()


class SecurityError(RuntimeError):
    """A derived state path is unsafe or an immutable file would be replaced."""


class LedgerError(RuntimeError):
    """The append-only ledger or its head checkpoint is invalid."""


class JudgeInvoker(Protocol):
    """Injected stage-4 adapter boundary.

    The callable must return either an AdapterOutcome-like object exposing
    ``as_dict()`` or the equivalent mapping.
    """

    def __call__(
        self,
        *,
        judge_name: str,
        repo_root: pathlib.Path,
        manifest_path: pathlib.Path,
        submission_path: pathlib.Path,
        launcher_run_id: str,
    ) -> Any:
        ...


@dataclasses.dataclass(frozen=True)
class ControlArtifacts:
    canary_submission: pathlib.Path
    parser_negative: pathlib.Path
    execution_artifact: pathlib.Path


@dataclasses.dataclass(frozen=True)
class EngineConfig:
    repo_root: pathlib.Path
    manifest_path: pathlib.Path
    run_id: str
    control_artifacts: ControlArtifacts
    state_root: pathlib.Path = DEFAULT_STATE_ROOT
    schema_dir: pathlib.Path = DEFAULT_SCHEMA_DIR
    auto_start_controls: bool = True


@dataclasses.dataclass(frozen=True)
class JudgeCapture:
    stdout: bytes
    stderr: bytes
    meta: dict[str, Any]


def _sha256_bytes(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def _file_sha256_or_zero(path: pathlib.Path) -> str:
    try:
        return deterministic.file_sha256(path)
    except OSError:
        return ZERO_HASH


def _canonical_hash(value: Any) -> str:
    return deterministic.jcs_sha256(value)


def _json_bytes(value: Any) -> bytes:
    return (
        json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
        + "\n"
    ).encode("utf-8")


def _strict_object(raw: bytes, label: str) -> tuple[dict[str, Any] | None, list[str]]:
    value, issues = deterministic.strict_json_load_bytes(raw, label)
    if issues:
        return None, [issue.code.value for issue in issues]
    if not isinstance(value, dict):
        return None, ["SCHEMA_VALIDATION_FAILED"]
    return value, []


def _ensure_directory(path: pathlib.Path) -> None:
    """Create a directory without accepting symlinks in its existing prefix."""

    missing: list[pathlib.Path] = []
    cursor = path
    while not cursor.exists():
        missing.append(cursor)
        if cursor.parent == cursor:
            break
        cursor = cursor.parent
    if cursor.exists() and (cursor.is_symlink() or not cursor.is_dir()):
        raise SecurityError(f"unsafe directory prefix: {cursor}")
    for directory in reversed(missing):
        try:
            directory.mkdir(mode=0o700)
        except FileExistsError:
            pass
        if directory.is_symlink() or not directory.is_dir():
            raise SecurityError(f"unsafe directory: {directory}")


def _write_new(path: pathlib.Path, raw: bytes) -> None:
    _ensure_directory(path.parent)
    flags = os.O_WRONLY | os.O_CREAT | os.O_EXCL
    if hasattr(os, "O_NOFOLLOW"):
        flags |= os.O_NOFOLLOW
    try:
        descriptor = os.open(path, flags, 0o600)
    except OSError as error:
        raise SecurityError(f"refusing to replace immutable artifact: {path.name}") from error
    try:
        with os.fdopen(descriptor, "wb") as handle:
            handle.write(raw)
            handle.flush()
            os.fsync(handle.fileno())
    except BaseException:
        try:
            path.unlink()
        except OSError:
            pass
        raise


def _replace_regular(path: pathlib.Path, raw: bytes) -> None:
    """Atomically replace an engine-owned current-state file, never a symlink."""

    _ensure_directory(path.parent)
    if path.exists() or path.is_symlink():
        if path.is_symlink() or not path.is_file():
            raise SecurityError(f"unsafe current-state target: {path.name}")
    descriptor, temporary_name = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent)
    temporary = pathlib.Path(temporary_name)
    try:
        os.fchmod(descriptor, 0o600)
        with os.fdopen(descriptor, "wb") as handle:
            handle.write(raw)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, path)
    finally:
        try:
            temporary.unlink()
        except FileNotFoundError:
            pass


def _ledger_entry_hash(entry_without_hash: Mapping[str, Any]) -> str:
    return _canonical_hash(dict(entry_without_hash))


def verify_ledger(
    ledger_path: pathlib.Path,
    head_path: pathlib.Path,
    expected_run_id: str,
) -> tuple[str, int, list[dict[str, Any]]]:
    """Verify ordering, every link/hash, and the separately checkpointed tail."""

    if not ledger_path.exists() and not head_path.exists():
        return ZERO_HASH, 0, []
    if ledger_path.is_symlink() or head_path.is_symlink():
        raise LedgerError("ledger paths must not be symlinks")
    if not ledger_path.is_file() or not head_path.is_file():
        raise LedgerError("ledger and head checkpoint must both be regular files")

    entries: list[dict[str, Any]] = []
    previous = ZERO_HASH
    try:
        lines = ledger_path.read_bytes().splitlines()
    except OSError as error:
        raise LedgerError(f"ledger read failed: {error}") from error
    for index, raw in enumerate(lines, start=1):
        entry, codes = _strict_object(raw, f"ledger line {index}")
        if entry is None:
            raise LedgerError(f"ledger line {index} strict decode failed: {','.join(codes)}")
        required = {
            "schema_version",
            "contract_version",
            "run_id",
            "event_index",
            "event_type",
            "prev_hash",
            "payload",
            "entry_hash",
        }
        if set(entry) != required:
            raise LedgerError(f"ledger line {index} has an invalid field set")
        if (
            entry["schema_version"] != 1
            or entry["contract_version"] != CONTRACT_VERSION
            or entry["run_id"] != expected_run_id
            or entry["event_index"] != index
            or entry["prev_hash"] != previous
            or not isinstance(entry["payload"], dict)
        ):
            raise LedgerError(f"ledger line {index} binding/order check failed")
        claimed = entry["entry_hash"]
        material = {key: value for key, value in entry.items() if key != "entry_hash"}
        actual = _ledger_entry_hash(material)
        if claimed != actual:
            raise LedgerError(f"ledger line {index} hash mismatch")
        previous = claimed
        entries.append(entry)

    try:
        head_raw = head_path.read_bytes()
    except OSError as error:
        raise LedgerError(f"ledger head read failed: {error}") from error
    head, codes = _strict_object(head_raw, "ledger head")
    if head is None:
        raise LedgerError(f"ledger head strict decode failed: {','.join(codes)}")
    if set(head) != {"schema_version", "run_id", "entry_count", "head_hash"}:
        raise LedgerError("ledger head has an invalid field set")
    if (
        head["schema_version"] != 1
        or head["run_id"] != expected_run_id
        or head["entry_count"] != len(entries)
        or head["head_hash"] != previous
    ):
        raise LedgerError("ledger tail deletion or head mismatch detected")
    return previous, len(entries), entries


def _passing_inputs(inputs: Mapping[str, Any]) -> bool:
    try:
        return (
            inputs["deterministic"]["status"] == "PASS"
            and inputs["codex"]["verdict"] == "PASS"
            and inputs["grok"]["verdict"] == "PASS"
            and inputs["canary"]["status"] == "CAUGHT"
            and inputs["parser_negative"]["status"] == "REJECTED"
            and inputs["evidence_chain"]["status"] == "VALID"
        )
    except (KeyError, TypeError):
        return False


def compute_decision_status(inputs: Mapping[str, Any]) -> str:
    """The independent implementation-side copy of the six-input truth table."""

    return "PASS" if _passing_inputs(inputs) else "FAIL"


def _hard_fail_reason_codes(inputs: Mapping[str, Any]) -> list[str]:
    """Map engine-observable §4.3 control breaches onto a terminal axis."""

    reasons: list[str] = []
    try:
        if inputs["canary"]["status"] == "MISSED":
            reasons.extend(
                inputs["canary"].get("failure_codes") or ["CANARY_CONTROL_FAILED"]
            )
        if inputs["parser_negative"]["status"] == "ACCEPTED":
            reasons.extend(
                inputs["parser_negative"].get("failure_codes")
                or ["PARSER_NEGATIVE_ACCEPTED"]
            )
    except (KeyError, TypeError):
        return sorted(set(reasons))
    return sorted(set(reasons))


def _redacted_argv_is_safe(argv: Any) -> bool:
    if not isinstance(argv, list) or not all(isinstance(item, str) for item in argv):
        return False
    secret_markers = ("token=", "bearer ", "sk-", "xai-", "eyj")
    return not any(
        "/" in item
        or "\\" in item
        or re.match(r"^[A-Za-z]:", item) is not None
        or any(marker in item.lower() for marker in secret_markers)
        for item in argv
    )


class ResumeGateEngine:
    """One run of the phase-5 decision engine."""

    def __init__(self, config: EngineConfig, judge_invoker: JudgeInvoker) -> None:
        self.config = config
        self.judge_invoker = judge_invoker
        if not RUN_ID_RE.fullmatch(config.run_id):
            raise SecurityError("run_id does not satisfy the fixed safe identifier grammar")

        self.repo_root = config.repo_root.resolve(strict=True)
        self.manifest_path = config.manifest_path.resolve(strict=True)
        self.schema_dir = config.schema_dir.resolve(strict=True)
        proposed_state_root = config.state_root.resolve(strict=False)
        try:
            inside_repo = os.path.commonpath(
                (str(self.repo_root), str(proposed_state_root))
            ) == str(self.repo_root)
        except ValueError as error:
            raise SecurityError("state root cannot be compared to repository root") from error
        if inside_repo:
            raise SecurityError("state root must be outside the repository")
        _ensure_directory(config.state_root)
        self.state_root = config.state_root.resolve(strict=True)

        self.run_dir = self.state_root / config.run_id
        _ensure_directory(self.run_dir)
        if self.run_dir.is_symlink():
            raise SecurityError("run state directory must not be a symlink")
        self.ledger_path = self.run_dir / "attempt-ledger.jsonl"
        self.head_path = self.run_dir / "attempt-ledger.head.json"
        self.current_decision_path = self.run_dir / "decision.json"
        self.status_path = self.run_dir / "status.json"

        manifest_result, manifest, source_snapshots = deterministic.validate_manifest(
            self.manifest_path,
            self.repo_root,
            schema_dir=self.schema_dir,
        )
        if manifest_result["status"] != "PASS" or not isinstance(manifest, dict):
            raise ValueError(f"frozen manifest failed stage-3: {manifest_result}")
        self.manifest = manifest
        self.manifest_sha256 = manifest_result["manifest_sha256"]
        self.source_snapshots = source_snapshots
        self.decision_schema = self._load_decision_schema()
        self.judge_schema = self._load_judge_schema()

        self.ledger_hash, _, self.entries = verify_ledger(
            self.ledger_path, self.head_path, config.run_id
        )
        self.controls: dict[str, Any] | None = None
        self.attempt_history: list[dict[str, Any]] = []
        self.current_status = "NOT_COMPLETE"
        self._restore()
        self._verify_control_artifact_continuity()
        self._verify_attempt_artifacts()
        self._verify_status_checkpoint()
        if config.auto_start_controls and self.controls is None:
            self.run_controls()

    def _load_decision_schema(self) -> dict[str, Any]:
        value, issues = deterministic.strict_json_load_path(
            self.schema_dir / "decision.schema.json", "decision schema"
        )
        if issues or not isinstance(value, dict):
            raise RuntimeError("decision schema is unavailable")
        Draft202012Validator.check_schema(value)
        return value

    def _load_judge_schema(self) -> dict[str, Any]:
        value, issues = deterministic.strict_json_load_path(
            self.schema_dir / "judge.schema.json", "judge schema"
        )
        if issues or not isinstance(value, dict):
            raise RuntimeError("judge schema is unavailable")
        Draft202012Validator.check_schema(value)
        return value

    def _restore(self) -> None:
        saw_attempt = False
        for entry in self.entries:
            payload = entry["payload"]
            if entry["event_type"] == "CONTROLS":
                if self.controls is not None or saw_attempt:
                    raise LedgerError("controls must occur exactly once and before attempts")
                self.controls = payload["results"]
            elif entry["event_type"] == "ATTEMPT":
                saw_attempt = True
                self.attempt_history.append(payload)
                self.current_status = payload["current_status"]
            elif entry["event_type"] == "HARD_STOP":
                self.current_status = "FAILED_STOPPED"
            else:
                raise LedgerError(f"unknown ledger event type: {entry['event_type']}")

    def _status_value(self) -> dict[str, Any]:
        return {
            "schema_version": 1,
            "contract_version": CONTRACT_VERSION,
            "run_id": self.config.run_id,
            "accepted_attempts": len(self.attempt_history),
            "ledger_hash": self.ledger_hash,
            "status": self.current_status,
        }

    def _verify_control_artifact_continuity(self) -> None:
        if self.controls is None:
            return
        artifacts = self.config.control_artifacts
        execution_hash = _file_sha256_or_zero(artifacts.execution_artifact)
        current = {
            "canary": _file_sha256_or_zero(artifacts.canary_submission),
            "parser_negative": _file_sha256_or_zero(artifacts.parser_negative),
        }
        for name in ("canary", "parser_negative"):
            result = self.controls.get(name)
            if (
                not isinstance(result, dict)
                or result.get("input_artifact_sha256") != current[name]
                or result.get("execution_artifact_sha256") != execution_hash
            ):
                raise LedgerError(f"{name} control artifact changed after execution")

    @staticmethod
    def _read_artifact(path: pathlib.Path, label: str) -> tuple[bytes, dict[str, Any]]:
        if path.is_symlink() or not path.is_file():
            raise LedgerError(f"{label} must be a regular file")
        try:
            raw = path.read_bytes()
        except OSError as error:
            raise LedgerError(f"{label} read failed: {error}") from error
        value, codes = _strict_object(raw, label)
        if value is None:
            raise LedgerError(f"{label} strict decode failed: {','.join(codes)}")
        return raw, value

    @staticmethod
    def _read_raw_artifact(path: pathlib.Path, label: str) -> bytes:
        if path.is_symlink() or not path.is_file():
            raise LedgerError(f"{label} must be a regular file")
        try:
            return path.read_bytes()
        except OSError as error:
            raise LedgerError(f"{label} read failed: {error}") from error

    @staticmethod
    def _artifact_ref(relative_path: str, raw: bytes) -> dict[str, str]:
        return {"path": relative_path, "sha256": _sha256_bytes(raw)}

    def _verify_artifact_ref(
        self,
        attempt_dir: pathlib.Path,
        reference: Any,
        expected_relative_path: str,
        label: str,
    ) -> bytes:
        if (
            not isinstance(reference, dict)
            or set(reference) != {"path", "sha256"}
            or reference.get("path") != expected_relative_path
        ):
            raise LedgerError(f"{label} has an invalid artifact reference")
        raw = self._read_raw_artifact(attempt_dir / expected_relative_path, label)
        if reference.get("sha256") != _sha256_bytes(raw):
            raise LedgerError(f"{label} hash mismatch")
        return raw

    @staticmethod
    def _normalized_snapshot_slice(
        snapshot: Any,
        locator: Mapping[str, Any],
    ) -> str:
        if snapshot.artifact_type == "code":
            if snapshot.lines is None or locator.get("type") != "line_range":
                raise ValueError("code snapshot/locator mismatch")
            raw = "\n".join(
                snapshot.lines[locator["start"] - 1 : locator["end"]]
            )
        else:
            if snapshot.pages is None or locator.get("type") != "page_range":
                raise ValueError("PDF snapshot/locator mismatch")
            raw = "\n".join(
                snapshot.pages[page]
                for page in range(locator["start"], locator["end"] + 1)
            )
        return unicodedata.normalize("NFKC", raw)

    def _persist_source_artifacts(
        self,
        attempt_dir: pathlib.Path,
        submission: dict[str, Any] | None,
        submission_sha256: str,
        deterministic_result: Mapping[str, Any],
    ) -> dict[str, Any]:
        """Persist the manifest subset and exact NFKC slices supplied to judges."""

        source_entries: list[dict[str, Any]] = []
        slice_refs: list[dict[str, Any]] = []
        if (
            deterministic_result.get("status") == "PASS"
            and isinstance(submission, dict)
        ):
            source_id = submission["candidate"]["source_id"]
            source = self.manifest["sources"][source_id]
            snapshot = self.source_snapshots[source_id]
            locator_entries: list[dict[str, Any]] = []
            for index, evidence in enumerate(submission["evidence"]):
                locator = evidence["locator"]
                slice_text = self._normalized_snapshot_slice(snapshot, locator)
                relative_path = f"source-slices/{source_id}/{index}.txt"
                slice_raw = slice_text.encode("utf-8", errors="strict")
                _write_new(attempt_dir / relative_path, slice_raw)
                reference = {
                    "source_id": source_id,
                    "index": index,
                    "locator": locator,
                    **self._artifact_ref(relative_path, slice_raw),
                }
                slice_refs.append(reference)
                locator_entries.append(
                    {
                        "index": index,
                        "locator": locator,
                        "slice_path": relative_path,
                        "slice_sha256": reference["sha256"],
                    }
                )
            source_entries.append(
                {
                    "source_id": source_id,
                    "path": source["path"],
                    "sha256": source["sha256"],
                    "artifact_type": source["artifact_type"],
                    "locators": locator_entries,
                }
            )

        source_manifest = {
            "schema_version": 1,
            "contract_version": CONTRACT_VERSION,
            "manifest": {
                "manifest_id": self.manifest["manifest_id"],
                "sha256": self.manifest_sha256,
            },
            "submission_sha256": submission_sha256,
            "sources": source_entries,
        }
        source_manifest_raw = _json_bytes(source_manifest)
        source_manifest_path = attempt_dir / "source-manifest.json"
        _write_new(source_manifest_path, source_manifest_raw)
        return {
            "source_manifest": self._artifact_ref(
                "source-manifest.json", source_manifest_raw
            ),
            "source_slices": slice_refs,
        }

    @staticmethod
    def _safe_capture_meta(
        judge_name: str,
        mapped: Mapping[str, Any],
        capture: JudgeCapture,
    ) -> dict[str, Any]:
        meta = dict(capture.meta)
        argv = meta.get("argv")
        argv_is_safe = (
            meta.get("argv_redacted") is True
            and _redacted_argv_is_safe(argv)
        )
        if not argv_is_safe:
            argv = ["<injected-judge-invoker>"]
        exit_code = meta.get("exit_code")
        if not isinstance(exit_code, int) or isinstance(exit_code, bool):
            exit_code = 0 if mapped.get("status") == "VALIDATED" else 1
        duration_ms = meta.get("duration_ms")
        if not isinstance(duration_ms, int) or isinstance(duration_ms, bool):
            duration_ms = 0
        return {
            "schema_version": 1,
            "judge": judge_name,
            "argv": argv,
            "argv_redacted": True,
            "exit_code": exit_code,
            "duration_ms": max(0, duration_ms),
            "stdout_bytes": len(capture.stdout),
            "stderr_bytes": len(capture.stderr),
            "capture": (
                "adapter-process"
                if capture.meta
                else "injected-outcome"
            ),
        }

    def _persist_judge_artifacts(
        self,
        attempt_dir: pathlib.Path,
        judge_name: str,
        mapped: dict[str, Any],
        capture: JudgeCapture,
        source_artifacts: Mapping[str, Any],
    ) -> dict[str, Any]:
        judge_relative_dir = f"judges/{judge_name}"
        stdout_path = f"{judge_relative_dir}/stdout.raw"
        stderr_path = f"{judge_relative_dir}/stderr.raw"
        meta_path = f"{judge_relative_dir}/meta.json"
        verdict_path = f"{judge_relative_dir}/verdict.json"

        meta = self._safe_capture_meta(judge_name, mapped, capture)
        verdict = mapped.get("judge_result")
        if not isinstance(verdict, dict):
            verdict = {
                "schema_version": 1,
                "judge": judge_name,
                "status": "UNAVAILABLE",
                "failure": mapped.get(
                    "failure",
                    {"code": "VERDICT_UNAVAILABLE", "detail": "judge was not called"},
                ),
            }
        meta_raw = _json_bytes(meta)
        verdict_raw = _json_bytes(verdict)
        _write_new(attempt_dir / stdout_path, capture.stdout)
        _write_new(attempt_dir / stderr_path, capture.stderr)
        _write_new(attempt_dir / meta_path, meta_raw)
        _write_new(attempt_dir / verdict_path, verdict_raw)

        artifacts = {
            "source_manifest": source_artifacts["source_manifest"],
            "source_slices": source_artifacts["source_slices"],
            "stdout": self._artifact_ref(stdout_path, capture.stdout),
            "stderr": self._artifact_ref(stderr_path, capture.stderr),
            "meta": self._artifact_ref(meta_path, meta_raw),
            "verdict": self._artifact_ref(verdict_path, verdict_raw),
        }
        return {**mapped, "artifacts": artifacts}

    def _verify_attempt_artifacts(self) -> None:
        """Recompute every persisted attempt's evidence chain from disk."""

        attempt_entries = [
            entry for entry in self.entries if entry["event_type"] == "ATTEMPT"
        ]
        if not attempt_entries:
            if self.current_decision_path.exists() or self.current_decision_path.is_symlink():
                raise LedgerError("decision exists without an attempt ledger entry")
            return

        latest_decision_raw: bytes | None = None
        for entry in attempt_entries:
            payload = entry["payload"]
            attempt = payload.get("attempt")
            if not isinstance(attempt, int) or attempt < 1:
                raise LedgerError("attempt ledger payload has an invalid attempt number")
            attempt_dir = self.run_dir / "attempts" / f"{attempt:06d}"

            request_path = attempt_dir / "request.json"
            if request_path.is_symlink() or not request_path.is_file():
                raise LedgerError(f"attempt {attempt} request is unavailable")
            request_raw = request_path.read_bytes()
            request_value, _ = _strict_object(request_raw, f"attempt {attempt} request")
            request_hash = (
                _canonical_hash(request_value)
                if request_value is not None
                else _sha256_bytes(request_raw)
            )
            if request_hash != payload.get("submission_sha256"):
                raise LedgerError(f"attempt {attempt} submission hash mismatch")

            _, deterministic_result = self._read_artifact(
                attempt_dir / "deterministic.json",
                f"attempt {attempt} deterministic result",
            )
            source_manifest_raw, source_manifest = self._read_artifact(
                attempt_dir / "source-manifest.json",
                f"attempt {attempt} source manifest",
            )
            if (
                source_manifest.get("schema_version") != 1
                or source_manifest.get("contract_version") != CONTRACT_VERSION
                or source_manifest.get("manifest")
                != {
                    "manifest_id": self.manifest["manifest_id"],
                    "sha256": self.manifest_sha256,
                }
                or source_manifest.get("submission_sha256") != request_hash
                or not isinstance(source_manifest.get("sources"), list)
            ):
                raise LedgerError(f"attempt {attempt} source manifest binding mismatch")

            source_slice_refs: list[dict[str, Any]] = []
            expected_sources = 1 if deterministic_result.get("status") == "PASS" else 0
            if len(source_manifest["sources"]) != expected_sources:
                raise LedgerError(f"attempt {attempt} source manifest coverage mismatch")
            for source_entry in source_manifest["sources"]:
                source_id = source_entry.get("source_id")
                registered = self.manifest["sources"].get(source_id)
                if (
                    not isinstance(registered, dict)
                    or source_entry.get("path") != registered.get("path")
                    or source_entry.get("sha256") != registered.get("sha256")
                    or source_entry.get("artifact_type") != registered.get("artifact_type")
                    or not isinstance(source_entry.get("locators"), list)
                    or not isinstance(request_value, dict)
                    or request_value.get("candidate", {}).get("source_id") != source_id
                ):
                    raise LedgerError(f"attempt {attempt} source entry mismatch")
                snapshot = self.source_snapshots.get(source_id)
                if snapshot is None:
                    raise LedgerError(f"attempt {attempt} source snapshot is unavailable")
                evidence_items = request_value.get("evidence")
                if (
                    not isinstance(evidence_items, list)
                    or len(source_entry["locators"]) != len(evidence_items)
                ):
                    raise LedgerError(f"attempt {attempt} source locator coverage mismatch")
                for locator_entry, evidence_item in zip(
                    source_entry["locators"], evidence_items, strict=True
                ):
                    index = locator_entry.get("index")
                    locator = locator_entry.get("locator")
                    if (
                        not isinstance(index, int)
                        or index < 0
                        or index >= len(evidence_items)
                        or evidence_items[index].get("locator") != locator
                    ):
                        raise LedgerError(f"attempt {attempt} source locator mismatch")
                    relative_path = f"source-slices/{source_id}/{index}.txt"
                    reference = {
                        "path": locator_entry.get("slice_path"),
                        "sha256": locator_entry.get("slice_sha256"),
                    }
                    slice_raw = self._verify_artifact_ref(
                        attempt_dir,
                        reference,
                        relative_path,
                        f"attempt {attempt} source slice {source_id}/{index}",
                    )
                    try:
                        expected_slice = self._normalized_snapshot_slice(
                            snapshot, locator
                        ).encode("utf-8", errors="strict")
                    except (KeyError, TypeError, ValueError) as error:
                        raise LedgerError(
                            f"attempt {attempt} source slice cannot be reconstructed"
                        ) from error
                    if slice_raw != expected_slice:
                        raise LedgerError(
                            f"attempt {attempt} source slice content mismatch"
                        )
                    source_slice_refs.append(
                        {
                            "source_id": source_id,
                            "index": index,
                            "locator": locator,
                            "path": relative_path,
                            "sha256": _sha256_bytes(slice_raw),
                        }
                    )
            source_artifacts = {
                "source_manifest": self._artifact_ref(
                    "source-manifest.json", source_manifest_raw
                ),
                "source_slices": source_slice_refs,
            }

            judge_records: dict[str, dict[str, Any]] = {}
            for judge_name in ("codex", "grok"):
                _, judge_records[judge_name] = self._read_artifact(
                    attempt_dir / "judges" / f"{judge_name}.json",
                    f"attempt {attempt} {judge_name} result",
                )
            decision_raw, decision = self._read_artifact(
                attempt_dir / "decision.json",
                f"attempt {attempt} decision",
            )
            errors = list(
                Draft202012Validator(self.decision_schema).iter_errors(decision)
            )
            if errors:
                raise LedgerError(
                    f"attempt {attempt} decision schema mismatch: {errors[0].message}"
                )
            if (
                decision.get("attempt_id") != attempt
                or decision.get("status") != payload.get("decision_status")
                or decision.get("provenance", {}).get("submission", {}).get("sha256")
                != request_hash
                or _canonical_hash(decision) != payload.get("decision_sha256")
            ):
                raise LedgerError(f"attempt {attempt} decision binding mismatch")

            judge_hashes: dict[str, str] = {}
            for judge_name, record in judge_records.items():
                artifacts = record.get("artifacts")
                if (
                    not isinstance(artifacts, dict)
                    or set(artifacts)
                    != {
                        "source_manifest",
                        "source_slices",
                        "stdout",
                        "stderr",
                        "meta",
                        "verdict",
                    }
                    or artifacts["source_manifest"] != source_artifacts["source_manifest"]
                    or artifacts["source_slices"] != source_artifacts["source_slices"]
                ):
                    raise LedgerError(
                        f"attempt {attempt} {judge_name} artifact binding mismatch"
                    )
                judge_relative_dir = f"judges/{judge_name}"
                stdout_raw = self._verify_artifact_ref(
                    attempt_dir,
                    artifacts["stdout"],
                    f"{judge_relative_dir}/stdout.raw",
                    f"attempt {attempt} {judge_name} raw stdout",
                )
                stderr_raw = self._verify_artifact_ref(
                    attempt_dir,
                    artifacts["stderr"],
                    f"{judge_relative_dir}/stderr.raw",
                    f"attempt {attempt} {judge_name} raw stderr",
                )
                meta_raw = self._verify_artifact_ref(
                    attempt_dir,
                    artifacts["meta"],
                    f"{judge_relative_dir}/meta.json",
                    f"attempt {attempt} {judge_name} metadata",
                )
                meta, meta_codes = _strict_object(
                    meta_raw, f"attempt {attempt} {judge_name} metadata"
                )
                if (
                    meta is None
                    or meta_codes
                    or meta.get("judge") != judge_name
                    or meta.get("argv_redacted") is not True
                    or not _redacted_argv_is_safe(meta.get("argv"))
                    or not isinstance(meta.get("exit_code"), int)
                    or isinstance(meta.get("exit_code"), bool)
                    or not isinstance(meta.get("duration_ms"), int)
                    or isinstance(meta.get("duration_ms"), bool)
                    or meta.get("stdout_bytes") != len(stdout_raw)
                    or meta.get("stderr_bytes") != len(stderr_raw)
                ):
                    raise LedgerError(
                        f"attempt {attempt} {judge_name} metadata is unsafe"
                    )
                verdict_raw = self._verify_artifact_ref(
                    attempt_dir,
                    artifacts["verdict"],
                    f"{judge_relative_dir}/verdict.json",
                    f"attempt {attempt} {judge_name} normalized verdict",
                )
                verdict, verdict_codes = _strict_object(
                    verdict_raw, f"attempt {attempt} {judge_name} normalized verdict"
                )
                if verdict is None or verdict_codes:
                    raise LedgerError(
                        f"attempt {attempt} {judge_name} verdict decode mismatch"
                    )
                if isinstance(record.get("judge_result"), dict):
                    if verdict != record["judge_result"]:
                        raise LedgerError(
                            f"attempt {attempt} {judge_name} verdict binding mismatch"
                        )
                    verdict_errors = list(
                        Draft202012Validator(self.judge_schema).iter_errors(verdict)
                    )
                    if verdict_errors:
                        raise LedgerError(
                            f"attempt {attempt} {judge_name} verdict schema mismatch: "
                            f"{verdict_errors[0].message}"
                        )
                elif verdict.get("status") != "UNAVAILABLE":
                    raise LedgerError(
                        f"attempt {attempt} {judge_name} unavailable verdict mismatch"
                    )
                record_hash = _canonical_hash(record)
                judge_hashes[judge_name] = record_hash
                if (
                    decision["provenance"]["judges"][judge_name]["result_sha256"]
                    != record_hash
                ):
                    raise LedgerError(
                        f"attempt {attempt} {judge_name} provenance hash mismatch"
                    )
            chain_material = {
                "manifest_sha256": self.manifest_sha256,
                "submission_sha256": request_hash,
                "deterministic_sha256": _canonical_hash(deterministic_result),
                "judge_sha256": judge_hashes,
                "previous_ledger_hash": entry["prev_hash"],
            }
            provenance_hash = _canonical_hash(chain_material)
            if (
                decision["inputs"]["evidence_chain"]["status"] != "VALID"
                or decision["inputs"]["evidence_chain"]["provenance_sha256"]
                != provenance_hash
                or decision["chain_root"]
                != _canonical_hash(
                    {"provenance_sha256": provenance_hash, "inputs": decision["inputs"]}
                )
            ):
                raise LedgerError(f"attempt {attempt} evidence chain mismatch")
            latest_decision_raw = decision_raw

        current_raw, _ = self._read_artifact(
            self.current_decision_path, "current decision"
        )
        if current_raw != latest_decision_raw:
            raise LedgerError("current decision does not match the latest attempt")

    def _write_status_checkpoint(self) -> None:
        _replace_regular(self.status_path, _json_bytes(self._status_value()))

    def _verify_status_checkpoint(self) -> None:
        if not self.status_path.exists() and not self.status_path.is_symlink():
            if self.entries:
                raise LedgerError("status checkpoint is missing for a non-empty ledger")
            return
        if self.status_path.is_symlink() or not self.status_path.is_file():
            raise LedgerError("status checkpoint must be a regular file")
        value, codes = _strict_object(self.status_path.read_bytes(), "status checkpoint")
        if value is None or value != self._status_value():
            raise LedgerError(
                "status checkpoint does not match the verified ledger"
                + (f": {','.join(codes)}" if codes else "")
            )

    def _append_ledger(self, event_type: str, payload: dict[str, Any]) -> str:
        previous, count, _ = verify_ledger(
            self.ledger_path, self.head_path, self.config.run_id
        )
        if previous != self.ledger_hash:
            raise LedgerError("ledger changed since the engine loaded it")
        material = {
            "schema_version": 1,
            "contract_version": CONTRACT_VERSION,
            "run_id": self.config.run_id,
            "event_index": count + 1,
            "event_type": event_type,
            "prev_hash": previous,
            "payload": payload,
        }
        entry = {**material, "entry_hash": _ledger_entry_hash(material)}
        line = _json_bytes(entry)
        _ensure_directory(self.ledger_path.parent)
        flags = os.O_WRONLY | os.O_APPEND | os.O_CREAT
        if hasattr(os, "O_NOFOLLOW"):
            flags |= os.O_NOFOLLOW
        descriptor = os.open(self.ledger_path, flags, 0o600)
        try:
            with os.fdopen(descriptor, "ab") as handle:
                handle.write(line)
                handle.flush()
                os.fsync(handle.fileno())
        except BaseException:
            raise
        head = {
            "schema_version": 1,
            "run_id": self.config.run_id,
            "entry_count": count + 1,
            "head_hash": entry["entry_hash"],
        }
        _replace_regular(self.head_path, _json_bytes(head))
        self.ledger_hash = entry["entry_hash"]
        self.entries.append(entry)
        return self.ledger_hash

    @staticmethod
    def _outcome_mapping(outcome: Any) -> dict[str, Any]:
        if hasattr(outcome, "as_dict"):
            outcome = outcome.as_dict()
        if not isinstance(outcome, Mapping):
            return {
                "status": "FAIL",
                "failure": {"code": "ADAPTER_RESULT_INVALID", "detail": "not a mapping"},
            }
        return dict(outcome)

    def _invoke_judge(
        self,
        judge_name: str,
        submission_path: pathlib.Path,
        launcher_run_id: str,
        submission_sha256: str,
    ) -> tuple[dict[str, Any], str, str, JudgeCapture]:
        outcome: Any = None
        try:
            outcome = self.judge_invoker(
                judge_name=judge_name,
                repo_root=self.repo_root,
                manifest_path=self.manifest_path,
                submission_path=submission_path,
                launcher_run_id=launcher_run_id,
            )
        except BaseException as error:
            mapped = {
                "status": "FAIL",
                "failure": {
                    "code": "ADAPTER_INVOCATION_FAILED",
                    "detail": type(error).__name__,
                },
            }
        else:
            mapped = self._outcome_mapping(outcome)
        if outcome is not None:
            raw_stdout = getattr(outcome, "raw_stdout", None)
            raw_stderr = getattr(outcome, "raw_stderr", None)
            audit_meta = getattr(outcome, "audit_meta", None)
        else:
            raw_stdout = raw_stderr = audit_meta = None
        if not isinstance(raw_stdout, bytes):
            raw_stdout = _json_bytes(mapped)
        if not isinstance(raw_stderr, bytes):
            raw_stderr = b""
        if not isinstance(audit_meta, Mapping):
            audit_meta = {}
        capture = JudgeCapture(raw_stdout, raw_stderr, dict(audit_meta))
        result = mapped.get("judge_result")
        valid = (
            mapped.get("status") == "VALIDATED"
            and isinstance(result, dict)
            and result.get("judge") == judge_name
            and result.get("verdict") in {"PASS", "FAIL", "INCONCLUSIVE"}
            and result.get("submission_sha256") == submission_sha256
            and result.get("manifest")
            == {
                "manifest_id": self.manifest["manifest_id"],
                "sha256": self.manifest_sha256,
            }
            and isinstance(result.get("engine_version"), str)
            and bool(result["engine_version"].strip())
        )
        if valid:
            return (
                mapped,
                result["verdict"],
                result["engine_version"],
                capture,
            )
        return (
            mapped,
            "INCONCLUSIVE",
            f"{judge_name}-adapter-failure",
            capture,
        )

    def _control_result(
        self,
        control: dict[str, Any],
        *,
        status: str,
        failure_codes: list[str],
        input_hash: str,
        execution_hash: str,
    ) -> dict[str, Any]:
        return {
            "control_id": control["control_id"],
            "status": status,
            "failure_codes": failure_codes,
            "input_artifact_sha256": input_hash,
            "execution_artifact_sha256": execution_hash,
        }

    def run_controls(self) -> dict[str, Any]:
        """Run and persist both frozen negative controls exactly once."""

        if self.controls is not None:
            return self.controls
        if self.attempt_history:
            raise RuntimeError("controls cannot run after a positive submission attempt")
        controls = self.manifest["controls"]
        artifacts = self.config.control_artifacts
        execution_hash = _file_sha256_or_zero(artifacts.execution_artifact)

        parser = controls["parser_negative"]
        parser_input_hash = _file_sha256_or_zero(artifacts.parser_negative)
        parser_result, _, _ = deterministic.validate_manifest(
            artifacts.parser_negative,
            self.repo_root,
            schema_dir=self.schema_dir,
        )
        parser_codes = sorted(set(parser_result.get("failure_codes", [])))
        parser_ok = (
            parser_input_hash == parser["input_artifact_sha256"]
            and execution_hash == parser["execution_artifact_sha256"]
            and parser_result.get("status") == "FAIL"
            and parser_codes == ["JSON_DUPLICATE_KEY"]
            and set(parser_codes).issubset(set(parser["allowed_failure_codes"]))
        )
        parser_control_result = self._control_result(
            parser,
            status="REJECTED" if parser_ok else "ACCEPTED",
            failure_codes=parser_codes or ["PARSER_NEGATIVE_ACCEPTED"],
            input_hash=parser_input_hash,
            execution_hash=execution_hash,
        )

        canary = controls["canary"]
        canary_input_hash = _file_sha256_or_zero(artifacts.canary_submission)
        canary_raw = artifacts.canary_submission.read_bytes()
        canary_value, canary_decode_codes = _strict_object(canary_raw, "canary input")
        canary_artifacts_ok = (
            canary_input_hash == canary["input_artifact_sha256"]
            and execution_hash == canary["execution_artifact_sha256"]
            and canary_value is not None
        )
        canary_caught = False
        canary_judges: dict[str, Any] = {}
        if canary_artifacts_ok and canary_value is not None:
            canary_value["manifest"] = {
                "manifest_id": self.manifest["manifest_id"],
                "sha256": self.manifest_sha256,
            }
            control_dir = self.run_dir / "controls" / "canary"
            request_path = control_dir / "request.json"
            _write_new(request_path, _json_bytes(canary_value))
            stage3 = deterministic.validate_submission(
                self.manifest_path,
                request_path,
                self.repo_root,
                canary_value["run_id"],
                schema_dir=self.schema_dir,
            )
            if stage3.get("status") == "PASS":
                submission_hash = stage3["submission_sha256"]
                verdicts: dict[str, str] = {}
                for judge_name in ("codex", "grok"):
                    mapped, verdict, _, _ = self._invoke_judge(
                        judge_name,
                        request_path,
                        canary_value["run_id"],
                        submission_hash,
                    )
                    canary_judges[judge_name] = mapped
                    verdicts[judge_name] = verdict
                canary_caught = verdicts == {"codex": "FAIL", "grok": "FAIL"}
            else:
                canary_judges["deterministic"] = stage3
        else:
            canary_judges["input"] = {"failure_codes": canary_decode_codes}
        canary_codes = list(canary["allowed_failure_codes"])
        if not canary_caught:
            canary_codes = (
                ["CANARY_JUDGE_PASS"]
                if any(
                    isinstance(record.get("judge_result"), dict)
                    and record["judge_result"].get("verdict") == "PASS"
                    for record in canary_judges.values()
                    if isinstance(record, dict)
                )
                else ["CANARY_CONTROL_FAILED"]
            )
        canary_control_result = self._control_result(
            canary,
            status="CAUGHT" if canary_caught else "MISSED",
            failure_codes=canary_codes,
            input_hash=canary_input_hash,
            execution_hash=execution_hash,
        )

        results = {
            "canary": canary_control_result,
            "parser_negative": parser_control_result,
        }
        payload = {
            "results": results,
            "hard_fail_reasons": _hard_fail_reason_codes(
                {
                    "canary": canary_control_result,
                    "parser_negative": parser_control_result,
                }
            ),
            "artifacts_sha256": {
                "canary_judges": _canonical_hash(canary_judges),
                "parser_result": _canonical_hash(parser_result),
            },
        }
        self._append_ledger("CONTROLS", payload)
        self.controls = results
        self._write_status_checkpoint()
        return results

    def _controls_for_decision(self) -> tuple[dict[str, Any], dict[str, Any]]:
        if self.controls is not None:
            artifacts = self.config.control_artifacts
            execution_hash = _file_sha256_or_zero(artifacts.execution_artifact)
            canary_hash = _file_sha256_or_zero(artifacts.canary_submission)
            parser_hash = _file_sha256_or_zero(artifacts.parser_negative)
            canary_expected = self.manifest["controls"]["canary"]
            parser_expected = self.manifest["controls"]["parser_negative"]
            if (
                canary_hash != canary_expected["input_artifact_sha256"]
                or execution_hash != canary_expected["execution_artifact_sha256"]
            ):
                canary = {
                    **self.controls["canary"],
                    "status": "MISSED",
                    "failure_codes": ["CONTROL_ARTIFACT_CHANGED"],
                    "input_artifact_sha256": canary_hash,
                    "execution_artifact_sha256": execution_hash,
                }
            else:
                canary = self.controls["canary"]
            if (
                parser_hash != parser_expected["input_artifact_sha256"]
                or execution_hash != parser_expected["execution_artifact_sha256"]
            ):
                parser = {
                    **self.controls["parser_negative"],
                    "status": "ACCEPTED",
                    "failure_codes": ["CONTROL_ARTIFACT_CHANGED"],
                    "input_artifact_sha256": parser_hash,
                    "execution_artifact_sha256": execution_hash,
                }
            else:
                parser = self.controls["parser_negative"]
            return canary, parser
        execution_hash = _file_sha256_or_zero(self.config.control_artifacts.execution_artifact)
        canary = self.manifest["controls"]["canary"]
        parser = self.manifest["controls"]["parser_negative"]
        return (
            self._control_result(
                canary,
                status="NA",
                failure_codes=["CONTROLS_NOT_EXECUTED"],
                input_hash=_file_sha256_or_zero(
                    self.config.control_artifacts.canary_submission
                ),
                execution_hash=execution_hash,
            ),
            self._control_result(
                parser,
                status="NA",
                failure_codes=["CONTROLS_NOT_EXECUTED"],
                input_hash=_file_sha256_or_zero(
                    self.config.control_artifacts.parser_negative
                ),
                execution_hash=execution_hash,
            ),
        )

    def _no_progress_reason(
        self,
        *,
        candidate_evidence_hash: str,
        evidence_hash: str,
        deterministic_result: dict[str, Any],
        decision_status: str,
    ) -> str | None:
        if decision_status == "PASS":
            return None
        failed_history = [
            item
            for item in self.attempt_history
            if item.get("decision_status") != "PASS"
        ]
        if any(
            item.get("candidate_evidence_hash") == candidate_evidence_hash
            for item in failed_history
        ):
            return "IDENTICAL_FAILED_CANDIDATE_EVIDENCE"

        if deterministic_result.get("status") == "FAIL" and len(self.attempt_history) >= 2:
            window = self.attempt_history[-2:] + [
                {
                    "deterministic_status": deterministic_result.get("status"),
                    "deterministic_failure_codes": sorted(
                        set(deterministic_result.get("failure_codes", []))
                    ),
                    "evidence_hash": evidence_hash,
                }
            ]
            code_sets = {
                tuple(item.get("deterministic_failure_codes", [])) for item in window
            }
            evidence_hashes = {item.get("evidence_hash") for item in window}
            if (
                all(item.get("deterministic_status") == "FAIL" for item in window)
                and len(code_sets) == 1
                and len(evidence_hashes) == 1
            ):
                return "REPEATED_DETERMINISTIC_FAILURE_WITHOUT_NEW_EVIDENCE"
        return None

    def _receipt(self, attempt: int) -> dict[str, Any]:
        return {
            "attempt": attempt,
            "ledger_hash": self.ledger_hash,
            "status": self.current_status,
        }

    def submit(self, submission: bytes | Mapping[str, Any]) -> dict[str, Any]:
        """Process one worker submission and return only a machine receipt."""

        self._verify_control_artifact_continuity()
        self._verify_attempt_artifacts()
        if self.current_status in {"PASS", "HARD_FAIL", "FAILED_STOPPED"}:
            return self._receipt(len(self.attempt_history))
        attempt = len(self.attempt_history) + 1
        if attempt > MAX_SUBMITS:
            self.current_status = "FAILED_STOPPED"
            self._append_ledger(
                "HARD_STOP",
                {
                    "attempted_submit": attempt,
                    "accepted_attempts": len(self.attempt_history),
                    "reason": "MAX_SUBMITS_EXCEEDED",
                    "current_status": "FAILED_STOPPED",
                },
            )
            self._write_status_checkpoint()
            return self._receipt(attempt)

        raw = _json_bytes(dict(submission)) if isinstance(submission, Mapping) else bytes(submission)
        attempt_dir = self.run_dir / "attempts" / f"{attempt:06d}"
        request_path = attempt_dir / "request.json"
        _write_new(request_path, raw)

        decoded, _ = _strict_object(raw, "submission")
        submission_hash = (
            _canonical_hash(decoded) if decoded is not None else _sha256_bytes(raw)
        )
        candidate_evidence = (
            {
                "candidate": decoded.get("candidate"),
                "evidence": decoded.get("evidence"),
            }
            if decoded is not None
            else {"raw_sha256": submission_hash}
        )
        evidence = (
            decoded.get("evidence")
            if decoded is not None and "evidence" in decoded
            else {"raw_sha256": submission_hash}
        )
        candidate_evidence_hash = _canonical_hash(candidate_evidence)
        evidence_hash = _canonical_hash(evidence)

        deterministic_result = deterministic.validate_submission(
            self.manifest_path,
            request_path,
            self.repo_root,
            self.config.run_id,
            schema_dir=self.schema_dir,
        )
        _write_new(attempt_dir / "deterministic.json", _json_bytes(deterministic_result))
        source_artifacts = self._persist_source_artifacts(
            attempt_dir,
            decoded,
            submission_hash,
            deterministic_result,
        )

        judge_records: dict[str, dict[str, Any]] = {}
        judge_captures: dict[str, JudgeCapture] = {}
        judge_inputs: dict[str, dict[str, str]] = {}
        judge_provenance: dict[str, dict[str, Any]] = {}
        if deterministic_result.get("status") == "PASS":
            validated_submission_hash = deterministic_result["submission_sha256"]
            for judge_name in ("codex", "grok"):
                mapped, verdict, engine_version, capture = self._invoke_judge(
                    judge_name,
                    request_path,
                    self.config.run_id,
                    validated_submission_hash,
                )
                judge_records[judge_name] = mapped
                judge_captures[judge_name] = capture
                judge_inputs[judge_name] = {"verdict": verdict}
                judge_provenance[judge_name] = {
                    "schema_version": 1,
                    "engine_version": engine_version,
                }
        else:
            for judge_name in ("codex", "grok"):
                mapped = {
                    "status": "NOT_CALLED",
                    "failure": {"code": "DETERMINISTIC_REJECT", "detail": judge_name},
                }
                judge_records[judge_name] = mapped
                judge_captures[judge_name] = JudgeCapture(
                    stdout=_json_bytes(mapped),
                    stderr=b"",
                    meta={},
                )
                judge_inputs[judge_name] = {"verdict": "INCONCLUSIVE"}
                judge_provenance[judge_name] = {
                    "schema_version": 1,
                    "engine_version": f"{judge_name}-not-called",
                }
        judges_dir = attempt_dir / "judges"
        for judge_name, record in tuple(judge_records.items()):
            bound_record = self._persist_judge_artifacts(
                attempt_dir,
                judge_name,
                record,
                judge_captures[judge_name],
                source_artifacts,
            )
            judge_records[judge_name] = bound_record
            judge_provenance[judge_name]["result_sha256"] = _canonical_hash(
                bound_record
            )
            _write_new(
                judges_dir / f"{judge_name}.json",
                _json_bytes(bound_record),
            )

        existing_head, _, _ = verify_ledger(
            self.ledger_path, self.head_path, self.config.run_id
        )
        chain_material = {
            "manifest_sha256": self.manifest_sha256,
            "submission_sha256": submission_hash,
            "deterministic_sha256": _canonical_hash(deterministic_result),
            "judge_sha256": {
                name: provenance["result_sha256"]
                for name, provenance in judge_provenance.items()
            },
            "previous_ledger_hash": existing_head,
        }
        provenance_hash = _canonical_hash(chain_material)
        canary, parser_negative = self._controls_for_decision()
        inputs = {
            "deterministic": {
                "status": deterministic_result.get("status", "FAIL"),
                "failure_codes": sorted(
                    set(deterministic_result.get("failure_codes", ["VALIDATOR_INTERNAL_ERROR"]))
                ),
            },
            "codex": judge_inputs["codex"],
            "grok": judge_inputs["grok"],
            "canary": canary,
            "parser_negative": parser_negative,
            "evidence_chain": {
                "status": "VALID",
                "provenance_sha256": provenance_hash,
            },
        }
        decision_status = compute_decision_status(inputs)
        hard_fail_reasons = _hard_fail_reason_codes(inputs)
        stop_reason: str | None = None
        if hard_fail_reasons:
            decision_status = "HARD_FAIL"
        else:
            stop_reason = self._no_progress_reason(
                candidate_evidence_hash=candidate_evidence_hash,
                evidence_hash=evidence_hash,
                deterministic_result=deterministic_result,
                decision_status=decision_status,
            )
            if stop_reason is not None:
                decision_status = "FAILED_STOPPED"

        decision = {
            "schema_version": 1,
            "contract_version": CONTRACT_VERSION,
            "run_id": self.config.run_id,
            "attempt_id": attempt,
            "provenance": {
                "manifest": {
                    "schema_version": 1,
                    "manifest_id": self.manifest["manifest_id"],
                    "sha256": self.manifest_sha256,
                },
                "submission": {
                    "schema_version": 1,
                    "sha256": submission_hash,
                },
                "judges": judge_provenance,
                "decision_engine_version": ENGINE_VERSION,
            },
            "inputs": inputs,
            "status": decision_status,
            "chain_root": _canonical_hash(
                {"provenance_sha256": provenance_hash, "inputs": inputs}
            ),
        }
        errors = list(Draft202012Validator(self.decision_schema).iter_errors(decision))
        if errors:
            raise RuntimeError(f"decision schema rejected engine output: {errors[0].message}")
        _write_new(attempt_dir / "decision.json", _json_bytes(decision))
        _replace_regular(self.current_decision_path, _json_bytes(decision))

        payload = {
            "attempt": attempt,
            "submission_sha256": submission_hash,
            "candidate_evidence_hash": candidate_evidence_hash,
            "evidence_hash": evidence_hash,
            "deterministic_status": deterministic_result.get("status", "FAIL"),
            "deterministic_failure_codes": sorted(
                set(deterministic_result.get("failure_codes", []))
            ),
            "decision_status": decision_status,
            "decision_sha256": _canonical_hash(decision),
            "hard_fail_reasons": hard_fail_reasons,
            "hard_stop_reason": stop_reason,
            "current_status": decision_status,
        }
        self._append_ledger("ATTEMPT", payload)
        self.attempt_history.append(payload)
        self.current_status = decision_status
        self._write_status_checkpoint()
        return self._receipt(attempt)
