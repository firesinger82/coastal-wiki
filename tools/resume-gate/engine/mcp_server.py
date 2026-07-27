#!/usr/bin/env python3
"""Newline-delimited stdio MCP server exposing exactly one tool: submit."""
from __future__ import annotations

import argparse
import importlib.util
import json
import pathlib
import sys
from collections.abc import Mapping
from typing import Any, TextIO


ENGINE_DIR = pathlib.Path(__file__).resolve().parent
if str(ENGINE_DIR) not in sys.path:
    sys.path.insert(0, str(ENGINE_DIR))

import core  # noqa: E402


PROTOCOL_VERSION = "2024-11-05"
TOOL_NAME = "submit"


def _load_submission_schema(schema_dir: pathlib.Path) -> dict[str, Any]:
    value, issues = core.deterministic.strict_json_load_path(
        schema_dir / "submission.schema.json", "submission schema"
    )
    if issues or not isinstance(value, dict):
        raise RuntimeError("submission schema is unavailable")
    return value


class ResumeGateMCP:
    def __init__(self, engine: core.ResumeGateEngine) -> None:
        self.engine = engine
        self.submission_schema = _load_submission_schema(engine.schema_dir)

    def _tool_list(self) -> dict[str, Any]:
        return {
            "tools": [
                {
                    "name": TOOL_NAME,
                    "description": "Submit one resume-gate submission JSON document.",
                    "inputSchema": self.submission_schema,
                }
            ]
        }

    @staticmethod
    def _content(value: Mapping[str, Any], *, is_error: bool = False) -> dict[str, Any]:
        result: dict[str, Any] = {
            "content": [
                {
                    "type": "text",
                    "text": json.dumps(
                        dict(value),
                        ensure_ascii=False,
                        sort_keys=True,
                        separators=(",", ":"),
                    ),
                }
            ]
        }
        if is_error:
            result["isError"] = True
        return result

    def handle(self, message: Mapping[str, Any]) -> dict[str, Any] | None:
        method = message.get("method")
        params = message.get("params", {})
        if method == "initialize":
            return {
                "protocolVersion": PROTOCOL_VERSION,
                "capabilities": {"tools": {}},
                "serverInfo": {"name": "resume-submit", "version": "1"},
            }
        if method == "tools/list":
            return self._tool_list()
        if method == "resources/list":
            return {"resources": []}
        if method == "prompts/list":
            return {"prompts": []}
        if method == "tools/call":
            if not isinstance(params, Mapping) or params.get("name") != TOOL_NAME:
                return self._content(
                    {
                        "attempt": len(self.engine.attempt_history),
                        "ledger_hash": self.engine.ledger_hash,
                        "status": "FAIL",
                    },
                    is_error=True,
                )
            arguments = params.get("arguments")
            if not isinstance(arguments, Mapping):
                return self._content(
                    {
                        "attempt": len(self.engine.attempt_history),
                        "ledger_hash": self.engine.ledger_hash,
                        "status": "FAIL",
                    },
                    is_error=True,
                )
            try:
                receipt = self.engine.submit(arguments)
            except BaseException:
                return self._content(
                    {
                        "attempt": len(self.engine.attempt_history),
                        "ledger_hash": self.engine.ledger_hash,
                        "status": "FAIL",
                    },
                    is_error=True,
                )
            return self._content(receipt)
        if method == "ping":
            return {}
        return None


def _load_stage4_adapter() -> Any:
    path = core.GATE_ROOT / "judge" / "adapter.py"
    spec = importlib.util.spec_from_file_location("resume_gate_stage4_for_mcp", path)
    if spec is None or spec.loader is None:
        raise RuntimeError("stage-4 adapter cannot be loaded")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


class Stage4AdapterInvoker:
    """Production composition of the injected engine boundary and stage 4."""

    def __init__(self, *, empty_cwd: pathlib.Path, timeout_seconds: int) -> None:
        self.adapter = _load_stage4_adapter()
        self.empty_cwd = empty_cwd
        self.timeout_seconds = timeout_seconds

    def __call__(self, **kwargs: Any) -> Any:
        return self.adapter.run_adapter(
            **kwargs,
            runner=self.adapter.SubprocessJudgeRunner(),
            empty_cwd=self.empty_cwd,
            timeout_seconds=self.timeout_seconds,
        )


def serve(server: ResumeGateMCP, stdin: TextIO = sys.stdin, stdout: TextIO = sys.stdout) -> None:
    for raw_line in stdin:
        raw = raw_line.strip()
        if not raw:
            continue
        value, issues = core.deterministic.strict_json_load_bytes(
            raw.encode("utf-8"), "MCP request"
        )
        if issues or not isinstance(value, dict):
            response = {
                "jsonrpc": "2.0",
                "id": None,
                "error": {"code": -32700, "message": "invalid JSON-RPC request"},
            }
        elif "id" not in value:
            continue
        else:
            result = server.handle(value)
            if result is None:
                response = {
                    "jsonrpc": "2.0",
                    "id": value["id"],
                    "error": {"code": -32601, "message": "method not found"},
                }
            else:
                response = {"jsonrpc": "2.0", "id": value["id"], "result": result}
        stdout.write(json.dumps(response, ensure_ascii=False, separators=(",", ":")) + "\n")
        stdout.flush()


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", required=True, type=pathlib.Path)
    parser.add_argument("--manifest", required=True, type=pathlib.Path)
    parser.add_argument("--run-id", required=True)
    parser.add_argument(
        "--state-root",
        type=pathlib.Path,
        default=core.DEFAULT_STATE_ROOT,
    )
    parser.add_argument("--canary-submission", required=True, type=pathlib.Path)
    parser.add_argument("--parser-negative", required=True, type=pathlib.Path)
    parser.add_argument(
        "--execution-artifact",
        type=pathlib.Path,
        default=core.GATE_ROOT / "validator" / "validate.py",
    )
    parser.add_argument(
        "--empty-cwd",
        type=pathlib.Path,
        default=pathlib.Path("/opt/coastal-resume/empty"),
    )
    parser.add_argument("--timeout-seconds", type=int, default=180)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    config = core.EngineConfig(
        repo_root=args.repo_root,
        manifest_path=args.manifest,
        run_id=args.run_id,
        state_root=args.state_root,
        control_artifacts=core.ControlArtifacts(
            canary_submission=args.canary_submission,
            parser_negative=args.parser_negative,
            execution_artifact=args.execution_artifact,
        ),
    )
    invoker = Stage4AdapterInvoker(
        empty_cwd=args.empty_cwd,
        timeout_seconds=args.timeout_seconds,
    )
    serve(ResumeGateMCP(core.ResumeGateEngine(config, invoker)))
    return 0


if __name__ == "__main__":
    main()
