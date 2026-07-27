#!/usr/bin/env python3
"""Fail-closed external judge adapter for resume-gate.

The adapter never trusts a worker-supplied prompt or source slice. It first
re-runs the frozen deterministic validator, builds DATA only from its decoded
objects and verified source snapshots, invokes a pinned subscription CLI
through an injectable runner, and validates every returned binding.
"""
from __future__ import annotations

import argparse
import copy
import dataclasses
import hashlib
import hmac
import importlib.util
import json
import os
import pathlib
import subprocess
import sys
import tempfile
import tomllib
import unicodedata
from collections.abc import Mapping, Sequence
from typing import Any, Protocol

from jsonschema import Draft202012Validator


ADAPTER_DIR = pathlib.Path(__file__).resolve().parent
GATE_ROOT = ADAPTER_DIR.parent
PROMPT_PATH = ADAPTER_DIR / "prompt.fixed.txt"
PROMPT_SHA256 = "7a71c502a919bfb3ca70e18f1aca7dbb392dd5e7808f4962e7237ef9f75fe8b0"
DEFAULT_SCHEMA_DIR = GATE_ROOT / "schemas"
DEFAULT_EMPTY_CWD = pathlib.Path("/opt/coastal-resume/empty")
CODEX_BINARY = pathlib.Path("/home/firesinger/.local/bin/codex")
GROK_BINARY = pathlib.Path("/home/firesinger/.local/bin/grok")
ENV_BINARY = pathlib.Path("/usr/bin/env")
CODEX_ENGINE_VERSION = "codex-cli 0.144.1"
GROK_ENGINE_VERSION = "grok 0.2.112 (9bbd559437)"
API_KEY_ENV_NAMES = (
    "OPENAI_API_KEY",
    "XAI_API_KEY",
    "GROK_CODE_XAI_API_KEY",
)
UNKNOWN_GROK_AUTH_ENV_NAMES = (
    "GROK_AUTH_PROVIDER_COMMAND",
    "GROK_CLI_CHAT_PROXY_BASE_URL",
    "GROK_OIDC_ISSUER",
    "GROK_OIDC_CLIENT_ID",
)
DATA_BEGIN = "<<<RESUME_GATE_DATA_BEGIN>>>"
DATA_END = "<<<RESUME_GATE_DATA_END>>>"
_RESERVED_DATA_MARKERS = ("<<<RESUME_GATE_DATA_", "<<<SLICE_")
CLI_ERROR_MESSAGE_LIMIT = 500


def _load_validator() -> Any:
    candidates = (
        GATE_ROOT / "validator" / "validate.py",
        GATE_ROOT / "share" / "validator" / "validate.py",
    )
    path = next((candidate for candidate in candidates if candidate.is_file()), None)
    if path is None:
        raise RuntimeError("deterministic validator module is unavailable")
    module_name = "resume_gate_stage3_validator_for_judge"
    spec = importlib.util.spec_from_file_location(module_name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError("deterministic validator module cannot be loaded")
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module


deterministic = _load_validator()


@dataclasses.dataclass(frozen=True)
class JudgeConfig:
    name: str
    engine_version: str
    binary: pathlib.Path


JUDGES = {
    "codex": JudgeConfig("codex", CODEX_ENGINE_VERSION, CODEX_BINARY),
    "grok": JudgeConfig("grok", GROK_ENGINE_VERSION, GROK_BINARY),
}


@dataclasses.dataclass(frozen=True)
class ProcessResult:
    returncode: int
    stdout: bytes
    stderr: bytes


class RunnerError(RuntimeError):
    """A runner preflight or invocation failure that contains no credentials."""


class RunnerTimeout(RunnerError):
    pass


class JudgeRunner(Protocol):
    """Injectable boundary around all subscription CLI access."""

    def preflight(
        self,
        config: JudgeConfig,
        environment: Mapping[str, str],
        empty_cwd: pathlib.Path,
    ) -> None:
        """Verify the pinned CLI version and subscription authentication."""

    def invoke(
        self,
        config: JudgeConfig,
        *,
        prompt: bytes,
        schema: dict[str, Any],
        empty_cwd: pathlib.Path,
        environment: Mapping[str, str],
        timeout_seconds: int,
    ) -> ProcessResult:
        """Run exactly one external judge process."""


@dataclasses.dataclass(frozen=True)
class AdapterFailure:
    code: str
    detail: str

    def as_dict(self) -> dict[str, str]:
        return {"code": self.code, "detail": self.detail}


@dataclasses.dataclass(frozen=True)
class AdapterOutcome:
    status: str
    judge_result: dict[str, Any] | None = None
    failure: AdapterFailure | None = None

    @classmethod
    def validated(cls, result: dict[str, Any]) -> "AdapterOutcome":
        return cls(status="VALIDATED", judge_result=result)

    @classmethod
    def failed(cls, code: str, detail: str) -> "AdapterOutcome":
        return cls(status="FAIL", failure=AdapterFailure(code, detail))

    def as_dict(self) -> dict[str, Any]:
        value: dict[str, Any] = {"status": self.status}
        if self.judge_result is not None:
            value["judge_result"] = self.judge_result
        if self.failure is not None:
            value["failure"] = self.failure.as_dict()
        return value


def _strict_json_bytes(raw: bytes, label: str) -> Any:
    value, issues = deterministic.strict_json_load_bytes(raw, label)
    if issues:
        raise ValueError("; ".join(issue.detail for issue in issues))
    return value


def _json_compact(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, separators=(",", ":"))


def derive_cli_schema(schema: dict[str, Any]) -> dict[str, Any]:
    """Derive the generation-only schema without weakening the contract schema."""

    return {
        key: copy.deepcopy(value)
        for key, value in schema.items()
        if key != "allOf"
    }


def _contains_reserved_marker(value: str) -> bool:
    return any(marker in value for marker in _RESERVED_DATA_MARKERS)


def _snapshot_slice(
    snapshot: Any,
    locator: dict[str, Any],
    evidence_index: int,
) -> str:
    if snapshot.artifact_type == "code":
        if snapshot.lines is None or locator["type"] != "line_range":
            raise ValueError(f"evidence[{evidence_index}] has no verified code snapshot")
        raw = "\n".join(snapshot.lines[locator["start"] - 1 : locator["end"]])
    else:
        if snapshot.pages is None or locator["type"] != "page_range":
            raise ValueError(f"evidence[{evidence_index}] has no verified PDF snapshot")
        pages: list[str] = []
        for page in range(locator["start"], locator["end"] + 1):
            if page not in snapshot.pages:
                raise ValueError(
                    f"evidence[{evidence_index}] page {page} is absent from the verified snapshot"
                )
            pages.append(snapshot.pages[page])
        raw = "\n".join(pages)
    return unicodedata.normalize("NFKC", raw)


def build_data_block(
    *,
    config: JudgeConfig,
    manifest: dict[str, Any],
    submission: dict[str, Any],
    submission_sha256: str,
    snapshots: Mapping[str, Any],
) -> bytes:
    """Build the frozen DATA grammar from the strict allowlist only."""

    candidate = submission["candidate"]
    source_id = candidate["source_id"]
    snapshot = snapshots.get(source_id)
    if snapshot is None:
        raise ValueError(f"verified source snapshot is absent for {source_id}")

    allowlisted_candidate = {
        "source_id": candidate["source_id"],
        "claim_type": candidate["claim_type"],
        "claim": candidate["claim"],
    }
    scalar_values = (
        config.name,
        config.engine_version,
        manifest["contract_version"],
        manifest["manifest_id"],
        deterministic.jcs_sha256(manifest),
        submission_sha256,
        candidate["source_id"],
        candidate["claim_type"],
        candidate["claim"],
    )
    if any(_contains_reserved_marker(value) for value in scalar_values):
        raise ValueError("reserved DATA delimiter occurs in an allowlisted scalar field")

    lines = [
        DATA_BEGIN,
        f"JUDGE_NAME={_json_compact(config.name)}",
        f"ENGINE_VERSION={_json_compact(config.engine_version)}",
        f"schema_version={_json_compact(submission['schema_version'])}",
        f"contract_version={_json_compact(manifest['contract_version'])}",
        f"manifest_id={_json_compact(manifest['manifest_id'])}",
        f"manifest_sha256={_json_compact(deterministic.jcs_sha256(manifest))}",
        f"submission_sha256={_json_compact(submission_sha256)}",
        f"candidate={_json_compact(allowlisted_candidate)}",
    ]
    for index, evidence in enumerate(submission["evidence"]):
        locator = evidence["locator"]
        quote = evidence["quote"]
        frozen_slice = _snapshot_slice(snapshot, locator, index)
        if _contains_reserved_marker(quote) or _contains_reserved_marker(frozen_slice):
            raise ValueError(f"reserved DATA delimiter occurs in evidence[{index}]")
        lines.extend(
            (
                f"evidence[{index}].locator={_json_compact(locator)}",
                f"evidence[{index}].quote={_json_compact(quote)}",
                f"evidence[{index}].frozen_slice=",
                f"<<<SLICE_{index}_BEGIN>>>",
                frozen_slice,
                f"<<<SLICE_{index}_END>>>",
            )
        )
    lines.append(DATA_END)
    return ("\n".join(lines) + "\n").encode("utf-8", errors="strict")


def build_codex_argv(
    *,
    schema_path: pathlib.Path,
    empty_cwd: pathlib.Path,
) -> tuple[str, ...]:
    return (
        str(ENV_BINARY),
        "-u",
        "OPENAI_API_KEY",
        "-u",
        "XAI_API_KEY",
        str(CODEX_BINARY),
        "exec",
        "--ephemeral",
        "--sandbox",
        "read-only",
        "--cd",
        str(empty_cwd),
        "--skip-git-repo-check",
        "--ignore-user-config",
        "--ignore-rules",
        "--json",
        "--output-schema",
        str(schema_path),
        "-",
    )


def build_grok_argv(
    *,
    prompt: str,
    schema: dict[str, Any],
    empty_cwd: pathlib.Path,
) -> tuple[str, ...]:
    return (
        str(ENV_BINARY),
        "-u",
        "OPENAI_API_KEY",
        "-u",
        "XAI_API_KEY",
        "GROK_DISABLE_AUTOUPDATER=1",
        str(GROK_BINARY),
        "--cwd",
        str(empty_cwd),
        "--sandbox",
        "read-only",
        "--tools",
        "",
        "--disallowed-tools",
        "Agent",
        "--deny",
        "MCPTool",
        "--permission-mode",
        "dontAsk",
        "--no-plan",
        "--no-subagents",
        "--no-memory",
        "--disable-web-search",
        "--max-turns",
        "1",
        "--output-format",
        "json",
        "--json-schema",
        _json_compact(schema),
        "--verbatim",
        "-p",
        prompt,
    )


def _auth_home(environment: Mapping[str, str], variable: str, fallback: str) -> pathlib.Path:
    configured = environment.get(variable)
    if configured:
        return pathlib.Path(configured)
    user_home = environment.get("HOME")
    if not user_home:
        raise RunnerError("HOME is unavailable for subscription authentication")
    return pathlib.Path(user_home) / fallback


def _read_private_json(path: pathlib.Path, label: str) -> dict[str, Any]:
    try:
        mode = path.stat().st_mode & 0o777
        if mode & 0o077:
            raise RunnerError(f"{label} permissions are not owner-only")
        value = _strict_json_bytes(path.read_bytes(), label)
    except RunnerError:
        raise
    except (OSError, ValueError) as error:
        raise RunnerError(f"{label} cannot be verified: {error}") from error
    if not isinstance(value, dict):
        raise RunnerError(f"{label} is not a JSON object")
    return value


def _verify_codex_auth(environment: Mapping[str, str]) -> None:
    auth_path = _auth_home(environment, "CODEX_HOME", ".codex") / "auth.json"
    auth = _read_private_json(auth_path, "Codex auth")
    if auth.get("auth_mode") != "chatgpt":
        raise RunnerError("Codex auth_mode is not the pinned ChatGPT subscription mode")
    if auth.get("OPENAI_API_KEY"):
        raise RunnerError("Codex auth contains an API key")
    if not isinstance(auth.get("tokens"), dict):
        raise RunnerError("Codex cached ChatGPT tokens are absent")


def _has_nested_credential_config(value: Any) -> bool:
    if isinstance(value, dict):
        for key, nested in value.items():
            if key in {"api_key", "env_key", "extra_headers", "env_http_headers"}:
                return True
            if _has_nested_credential_config(nested):
                return True
    elif isinstance(value, list):
        return any(_has_nested_credential_config(item) for item in value)
    return False


def _verify_grok_auth(environment: Mapping[str, str]) -> None:
    grok_home = _auth_home(environment, "GROK_HOME", ".grok")
    auth = _read_private_json(grok_home / "auth.json", "Grok auth")
    if not auth:
        raise RunnerError("Grok cached subscription auth is absent")
    for issuer_key, entry in auth.items():
        if not isinstance(issuer_key, str) or not issuer_key.startswith("https://auth.x.ai::"):
            raise RunnerError("Grok auth contains an unapproved issuer")
        if not isinstance(entry, dict) or entry.get("auth_mode") != "oidc":
            raise RunnerError("Grok auth_mode is not the pinned xAI OAuth/OIDC mode")
        if not entry.get("refresh_token"):
            raise RunnerError("Grok cached OAuth refresh token is absent")

    config_path = grok_home / "config.toml"
    try:
        config = tomllib.loads(config_path.read_text(encoding="utf-8")) if config_path.is_file() else {}
    except (OSError, UnicodeDecodeError, tomllib.TOMLDecodeError) as error:
        raise RunnerError(f"Grok config cannot be verified: {error}") from error
    unapproved_sections = set(config) - {"cli", "ui"}
    if unapproved_sections:
        raise RunnerError(
            "Grok config contains unapproved sections: "
            + ", ".join(sorted(unapproved_sections))
        )
    if _has_nested_credential_config(config):
        raise RunnerError("Grok config contains credential-bearing fields")


def _verify_grok_inspect(value: Any) -> None:
    if not isinstance(value, dict):
        raise RunnerError("Grok inspect output is not an object")
    for field in ("projectInstructions", "hooks", "plugins", "mcpServers"):
        entries = value.get(field)
        if not isinstance(entries, list):
            raise RunnerError(f"Grok inspect omitted list field {field}")
        if entries:
            raise RunnerError(f"Grok inspect found unapproved {field}")

    allowed_sources = {"skills": "bundled", "agents": "builtin"}
    for field, allowed_source in allowed_sources.items():
        entries = value.get(field)
        if not isinstance(entries, list):
            raise RunnerError(f"Grok inspect omitted list field {field}")
        for entry in entries:
            source = entry.get("source") if isinstance(entry, dict) else None
            if not isinstance(source, dict) or source.get("type") != allowed_source:
                raise RunnerError(f"Grok inspect found an unapproved {field} source")

    external = value.get("externalCompat")
    if not isinstance(external, dict) or not isinstance(external.get("cells"), list):
        raise RunnerError("Grok inspect omitted external compatibility state")
    for cell in external["cells"]:
        if not isinstance(cell, dict) or not isinstance(cell.get("enabled"), bool):
            raise RunnerError("Grok inspect external compatibility state is malformed")
        if cell["enabled"]:
            raise RunnerError("Grok external compatibility customization is enabled")


class SubprocessJudgeRunner:
    """Production runner. Tests inject a mock and never enter this class."""

    def _run_preflight(
        self,
        argv: Sequence[str],
        environment: Mapping[str, str],
    ) -> ProcessResult:
        try:
            completed = subprocess.run(
                list(argv),
                stdin=subprocess.DEVNULL,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                env=dict(environment),
                shell=False,
                check=False,
                timeout=10,
            )
        except subprocess.TimeoutExpired as error:
            raise RunnerError("CLI preflight timed out") from error
        except OSError as error:
            raise RunnerError(f"CLI preflight could not start: {error}") from error
        return ProcessResult(completed.returncode, completed.stdout, completed.stderr)

    def preflight(
        self,
        config: JudgeConfig,
        environment: Mapping[str, str],
        empty_cwd: pathlib.Path,
    ) -> None:
        version = self._run_preflight((str(config.binary), "--version"), environment)
        if version.returncode != 0:
            raise RunnerError(f"{config.name} --version exited {version.returncode}")
        try:
            actual_version = version.stdout.decode("utf-8", errors="strict").strip()
        except UnicodeDecodeError as error:
            raise RunnerError(f"{config.name} --version was not UTF-8") from error
        if actual_version != config.engine_version:
            raise RunnerError(
                f"{config.name} version mismatch: expected {config.engine_version!r}, "
                f"got {actual_version!r}"
            )

        if config.name == "codex":
            _verify_codex_auth(environment)
            login = self._run_preflight(
                (str(config.binary), "login", "status"),
                environment,
            )
            login_confirmation = b"Logged in using ChatGPT"
            if login.returncode != 0 or not (
                login.stdout.strip() == login_confirmation
                or login.stderr.strip() == login_confirmation
            ):
                raise RunnerError("Codex CLI did not confirm ChatGPT subscription login")
        else:
            _verify_grok_auth(environment)
            inspect_result = self._run_preflight(
                (
                    str(config.binary),
                    "--cwd",
                    str(empty_cwd),
                    "inspect",
                    "--json",
                ),
                environment,
            )
            if inspect_result.returncode != 0:
                raise RunnerError(f"Grok inspect exited {inspect_result.returncode}")
            try:
                inspect_value = _strict_json_bytes(
                    inspect_result.stdout,
                    "Grok inspect output",
                )
            except ValueError as error:
                raise RunnerError(str(error)) from error
            _verify_grok_inspect(inspect_value)

    def invoke(
        self,
        config: JudgeConfig,
        *,
        prompt: bytes,
        schema: dict[str, Any],
        empty_cwd: pathlib.Path,
        environment: Mapping[str, str],
        timeout_seconds: int,
    ) -> ProcessResult:
        try:
            if config.name == "codex":
                input_bytes: bytes | None = prompt
                schema_bytes = (
                    _json_compact(schema) + "\n"
                ).encode("utf-8", errors="strict")
                with tempfile.NamedTemporaryFile(
                    mode="w+b",
                    prefix="resume-gate-codex-schema-",
                    suffix=".json",
                ) as schema_file:
                    schema_file.write(schema_bytes)
                    schema_file.flush()
                    argv = build_codex_argv(
                        schema_path=pathlib.Path(schema_file.name),
                        empty_cwd=empty_cwd,
                    )
                    completed = subprocess.run(
                        list(argv),
                        input=input_bytes,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE,
                        cwd=empty_cwd,
                        env=dict(environment),
                        shell=False,
                        check=False,
                        timeout=timeout_seconds,
                    )
            else:
                prompt_text = prompt.decode("utf-8", errors="strict")
                argv = build_grok_argv(
                    prompt=prompt_text,
                    schema=schema,
                    empty_cwd=empty_cwd,
                )
                input_bytes = None
                completed = subprocess.run(
                    list(argv),
                    input=input_bytes,
                    stdin=subprocess.DEVNULL,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    cwd=empty_cwd,
                    env=dict(environment),
                    shell=False,
                    check=False,
                    timeout=timeout_seconds,
                )
        except subprocess.TimeoutExpired as error:
            raise RunnerTimeout(f"{config.name} judge timed out") from error
        except (OSError, UnicodeError) as error:
            raise RunnerError(f"{config.name} judge could not start safely: {error}") from error
        return ProcessResult(completed.returncode, completed.stdout, completed.stderr)


def _error_event_message(event: dict[str, Any]) -> str | None:
    message = event.get("message")
    if isinstance(message, str):
        return message[:CLI_ERROR_MESSAGE_LIMIT]
    error = event.get("error")
    if isinstance(error, str):
        return error[:CLI_ERROR_MESSAGE_LIMIT]
    if isinstance(error, dict) and isinstance(error.get("message"), str):
        return error["message"][:CLI_ERROR_MESSAGE_LIMIT]
    return None


def _last_cli_error_event_message(stdout: bytes) -> str | None:
    last_message: str | None = None
    for line_number, raw_line in enumerate(stdout.splitlines(), start=1):
        if not raw_line.strip():
            continue
        try:
            event = _strict_json_bytes(raw_line, f"CLI JSONL line {line_number}")
        except ValueError:
            continue
        if (
            isinstance(event, dict)
            and event.get("type") in {"turn.failed", "error"}
        ):
            last_message = _error_event_message(event)
    return last_message


def _parse_codex_output(stdout: bytes) -> bytes:
    messages: list[str] = []
    turn_completed = False
    last_terminal_event: tuple[str, str | None] | None = None
    for line_number, raw_line in enumerate(stdout.splitlines(), start=1):
        if not raw_line.strip():
            continue
        event = _strict_json_bytes(raw_line, f"Codex JSONL line {line_number}")
        if not isinstance(event, dict) or not isinstance(event.get("type"), str):
            raise ValueError(f"Codex JSONL line {line_number} is not a typed event")
        event_type = event["type"]
        if event_type in {"turn.failed", "error"}:
            last_terminal_event = (event_type, _error_event_message(event))
        if event_type == "turn.completed":
            turn_completed = True
        if event_type == "item.completed":
            item = event.get("item")
            if isinstance(item, dict) and item.get("type") == "agent_message":
                text = item.get("text")
                if not isinstance(text, str):
                    raise ValueError("Codex agent_message text is absent")
                messages.append(text)
    if last_terminal_event is not None:
        event_type, message = last_terminal_event
        detail = f"Codex emitted terminal event {event_type}"
        if message is not None:
            detail += f": {message}"
        raise ValueError(detail)
    if not turn_completed:
        raise ValueError("Codex JSONL has no turn.completed event")
    if len(messages) != 1:
        raise ValueError(f"Codex JSONL contains {len(messages)} completed agent messages")
    return messages[0].encode("utf-8", errors="strict")


def _parse_grok_output(stdout: bytes) -> bytes:
    wrapper = _strict_json_bytes(stdout, "Grok JSON output")
    if not isinstance(wrapper, dict):
        raise ValueError("Grok JSON output is not an object")
    if wrapper.get("stopReason") != "EndTurn":
        raise ValueError(f"Grok stopReason is not EndTurn: {wrapper.get('stopReason')!r}")
    text = wrapper.get("text")
    if not isinstance(text, str):
        raise ValueError("Grok JSON output has no text string")
    return text.encode("utf-8", errors="strict")


def _load_judge_schema(schema_path: pathlib.Path) -> dict[str, Any]:
    try:
        schema = _strict_json_bytes(schema_path.read_bytes(), "judge schema")
    except (OSError, ValueError) as error:
        raise RuntimeError(f"judge schema cannot be loaded safely: {error}") from error
    if not isinstance(schema, dict):
        raise RuntimeError("judge schema top level is not an object")
    try:
        Draft202012Validator.check_schema(schema)
    except Exception as error:
        raise RuntimeError(f"judge schema itself is invalid: {error}") from error
    return schema


def _validate_judge_result(
    raw_result: bytes,
    *,
    schema: dict[str, Any],
    expected: dict[str, str],
) -> dict[str, Any]:
    result = _strict_json_bytes(raw_result, "judge result")
    if not isinstance(result, dict):
        raise ValueError("judge result is not an object")
    errors = sorted(
        Draft202012Validator(schema).iter_errors(result),
        key=lambda error: (tuple(str(item) for item in error.absolute_path), error.message),
    )
    if errors:
        first = errors[0]
        path = "$" + "".join(
            f"[{item}]" if isinstance(item, int) else f".{item}"
            for item in first.absolute_path
        )
        raise ValueError(f"judge schema rejected {path}: {first.message}")

    actual_echo = {
        "contract_version": result["contract_version"],
        "manifest_id": result["manifest"]["manifest_id"],
        "manifest_sha256": result["manifest"]["sha256"],
        "submission_sha256": result["submission_sha256"],
        "judge": result["judge"],
    }
    for field, expected_value in expected.items():
        actual_value = (
            result["engine_version"] if field == "engine_version" else actual_echo[field]
        )
        actual_bytes = actual_value.encode("utf-8", errors="strict")
        expected_bytes = expected_value.encode("utf-8", errors="strict")
        if not hmac.compare_digest(actual_bytes, expected_bytes):
            raise ValueError(f"judge binding mismatch for {field}")
    return result


def _clean_environment(environment: Mapping[str, str]) -> dict[str, str]:
    clean = dict(environment)
    for name in API_KEY_ENV_NAMES:
        clean.pop(name, None)
    return clean


def run_adapter(
    *,
    judge_name: str,
    repo_root: pathlib.Path,
    manifest_path: pathlib.Path,
    submission_path: pathlib.Path,
    launcher_run_id: str,
    runner: JudgeRunner,
    schema_dir: pathlib.Path = DEFAULT_SCHEMA_DIR,
    prompt_path: pathlib.Path = PROMPT_PATH,
    empty_cwd: pathlib.Path = DEFAULT_EMPTY_CWD,
    environment: Mapping[str, str] | None = None,
    timeout_seconds: int = 180,
) -> AdapterOutcome:
    """Execute the complete adapter pipeline, converting every error to FAIL."""

    try:
        if judge_name not in JUDGES:
            return AdapterOutcome.failed("JUDGE_UNKNOWN", f"unsupported judge: {judge_name!r}")
        config = JUDGES[judge_name]

        try:
            prompt_fixed = prompt_path.read_bytes()
        except OSError as error:
            return AdapterOutcome.failed("PROMPT_READ_ERROR", str(error))
        actual_prompt_hash = hashlib.sha256(prompt_fixed).hexdigest()
        if not hmac.compare_digest(actual_prompt_hash, PROMPT_SHA256):
            return AdapterOutcome.failed(
                "PROMPT_HASH_MISMATCH",
                f"expected {PROMPT_SHA256}, got {actual_prompt_hash}",
            )

        source_environment = dict(os.environ if environment is None else environment)
        visible_api_keys = [
            name for name in API_KEY_ENV_NAMES if name in source_environment
        ]
        if visible_api_keys:
            return AdapterOutcome.failed(
                "API_KEY_ENV_PRESENT",
                "API-key environment variable is present: " + ", ".join(visible_api_keys),
            )
        unknown_auth_env = [
            name for name in UNKNOWN_GROK_AUTH_ENV_NAMES if name in source_environment
        ]
        if judge_name == "grok" and unknown_auth_env:
            return AdapterOutcome.failed(
                "AUTH_TYPE_UNAPPROVED",
                "unapproved Grok authentication override is present: "
                + ", ".join(unknown_auth_env),
            )
        clean_environment = _clean_environment(source_environment)
        if judge_name == "grok":
            clean_environment["GROK_DISABLE_AUTOUPDATER"] = "1"

        deterministic_result = deterministic.validate_submission(
            manifest_path,
            submission_path,
            repo_root,
            launcher_run_id,
            schema_dir=schema_dir,
        )
        if deterministic_result["status"] != "PASS":
            codes = deterministic_result.get("failure_codes", [])
            return AdapterOutcome.failed(
                "DETERMINISTIC_VALIDATION_FAILED",
                "stage-3 rejected input: " + ",".join(codes),
            )

        manifest_result, manifest, snapshots = deterministic.validate_manifest(
            manifest_path,
            repo_root,
            schema_dir=schema_dir,
        )
        if manifest_result["status"] != "PASS" or not isinstance(manifest, dict):
            return AdapterOutcome.failed(
                "DETERMINISTIC_RECHECK_FAILED",
                "manifest/source recheck failed after submission validation",
            )
        submission, submission_issues = deterministic.strict_json_load_path(
            submission_path,
            "submission recheck",
        )
        if submission_issues or not isinstance(submission, dict):
            return AdapterOutcome.failed(
                "INPUT_RECHECK_FAILED",
                "submission could not be strict-decoded after deterministic PASS",
            )
        manifest_sha256 = deterministic.jcs_sha256(manifest)
        submission_sha256 = deterministic.jcs_sha256(submission)
        if (
            manifest_result.get("manifest_sha256") != manifest_sha256
            or deterministic_result.get("manifest_sha256") != manifest_sha256
            or deterministic_result.get("submission_sha256") != submission_sha256
        ):
            return AdapterOutcome.failed(
                "INPUT_RECHECK_FAILED",
                "canonical input hash changed during adapter validation",
            )

        try:
            data_block = build_data_block(
                config=config,
                manifest=manifest,
                submission=submission,
                submission_sha256=submission_sha256,
                snapshots=snapshots,
            )
        except (KeyError, TypeError, ValueError, UnicodeError) as error:
            return AdapterOutcome.failed("DATA_ASSEMBLY_FAILED", str(error))
        if b"attempt_reason" in data_block:
            return AdapterOutcome.failed(
                "JUDGE_INPUT_SMUGGLING",
                "attempt_reason occurred in the generated DATA block",
            )
        full_prompt = prompt_fixed + b"\n" + data_block

        schema_path = schema_dir / "judge.schema.json"
        try:
            schema = _load_judge_schema(schema_path)
        except RuntimeError as error:
            return AdapterOutcome.failed("JUDGE_SCHEMA_UNAVAILABLE", str(error))
        cli_schema = derive_cli_schema(schema)
        try:
            if not empty_cwd.is_dir() or any(empty_cwd.iterdir()):
                return AdapterOutcome.failed(
                    "EMPTY_CWD_INVALID",
                    f"judge cwd is absent or non-empty: {empty_cwd}",
                )
        except OSError as error:
            return AdapterOutcome.failed("EMPTY_CWD_INVALID", str(error))

        try:
            runner.preflight(config, clean_environment, empty_cwd)
        except RunnerError as error:
            return AdapterOutcome.failed("RUNNER_PREFLIGHT_FAILED", str(error))
        except Exception as error:
            return AdapterOutcome.failed(
                "RUNNER_PREFLIGHT_FAILED",
                f"{type(error).__name__}: {error}",
            )

        try:
            completed = runner.invoke(
                config,
                prompt=full_prompt,
                schema=cli_schema,
                empty_cwd=empty_cwd,
                environment=clean_environment,
                timeout_seconds=timeout_seconds,
            )
        except RunnerTimeout as error:
            return AdapterOutcome.failed("CLI_TIMEOUT", str(error))
        except RunnerError as error:
            return AdapterOutcome.failed("CLI_INVOCATION_FAILED", str(error))
        except Exception as error:
            return AdapterOutcome.failed(
                "CLI_INVOCATION_FAILED",
                f"{type(error).__name__}: {error}",
            )
        if completed.returncode != 0:
            detail = f"{judge_name} judge exited {completed.returncode}"
            error_message = _last_cli_error_event_message(completed.stdout)
            if error_message is not None:
                detail += f": {error_message}"
            return AdapterOutcome.failed(
                "CLI_EXIT_NONZERO",
                detail,
            )

        try:
            raw_result = (
                _parse_codex_output(completed.stdout)
                if judge_name == "codex"
                else _parse_grok_output(completed.stdout)
            )
        except (ValueError, UnicodeError) as error:
            return AdapterOutcome.failed("CLI_OUTPUT_INVALID", str(error))

        expected = {
            "contract_version": manifest["contract_version"],
            "manifest_id": manifest["manifest_id"],
            "manifest_sha256": manifest_sha256,
            "submission_sha256": submission_sha256,
            "judge": judge_name,
            "engine_version": config.engine_version,
        }
        try:
            judge_result = _validate_judge_result(
                raw_result,
                schema=schema,
                expected=expected,
            )
        except (KeyError, TypeError, ValueError, UnicodeError) as error:
            return AdapterOutcome.failed("JUDGE_RESULT_REJECTED", str(error))
        return AdapterOutcome.validated(judge_result)
    except BaseException as error:
        return AdapterOutcome.failed(
            "ADAPTER_INTERNAL_ERROR",
            f"{type(error).__name__}: {error}",
        )


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--judge", required=True, choices=sorted(JUDGES))
    parser.add_argument("--repo-root", required=True, type=pathlib.Path)
    parser.add_argument("--manifest", required=True, type=pathlib.Path)
    parser.add_argument("--submission", required=True, type=pathlib.Path)
    parser.add_argument("--launcher-run-id", required=True)
    parser.add_argument("--empty-cwd", type=pathlib.Path, default=DEFAULT_EMPTY_CWD)
    parser.add_argument("--timeout-seconds", type=int, default=180)
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    outcome = run_adapter(
        judge_name=args.judge,
        repo_root=args.repo_root,
        manifest_path=args.manifest,
        submission_path=args.submission,
        launcher_run_id=args.launcher_run_id,
        runner=SubprocessJudgeRunner(),
        empty_cwd=args.empty_cwd,
        timeout_seconds=args.timeout_seconds,
    )
    print(
        json.dumps(
            outcome.as_dict(),
            ensure_ascii=False,
            sort_keys=True,
            separators=(",", ":"),
        )
    )
    return 0 if outcome.status == "VALIDATED" else 1


if __name__ == "__main__":
    sys.exit(main())
