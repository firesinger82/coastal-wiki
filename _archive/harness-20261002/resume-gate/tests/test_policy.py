#!/usr/bin/env python3
"""Mock-only phase-6 policy, hook, launcher, and install-manifest tests.

Run:
  .venv/bin/python tools/resume-gate/tests/test_policy.py
"""
from __future__ import annotations

import hashlib
import importlib.util
import json
import os
import pathlib
import subprocess
import sys
import tempfile
from collections.abc import Iterator
from contextlib import contextmanager
from typing import Any


GATE_ROOT = pathlib.Path(__file__).resolve().parents[1]
REPO_ROOT = GATE_ROOT.parents[1]
POLICY = GATE_ROOT / "policy"
BIN = GATE_ROOT / "bin"
MANIFEST = GATE_ROOT / "INSTALL-MANIFEST.sha256"
PYTHON = pathlib.Path(sys.executable)
RUN_ID = "policy-run-0001"

DESTINATION_SOURCES = {
    "/etc/claude-code/managed-settings.d/50-coastal-resume.json": POLICY
    / "50-coastal-resume.json",
    "/etc/claude-code/managed-mcp.json": POLICY / "managed-mcp.json",
    "/etc/claude-code/.claude/agents/resume-coordinator.md": POLICY
    / "agents"
    / "resume-coordinator.md",
    "/etc/claude-code/.claude/agents/resume-code-reader.md": POLICY
    / "agents"
    / "resume-code-reader.md",
    "/etc/claude-code/.claude/agents/resume-pdf-reader.md": POLICY
    / "agents"
    / "resume-pdf-reader.md",
    "/opt/coastal-resume/bin/resume-submit-mcp": BIN / "resume-submit-mcp",
    "/opt/coastal-resume/bin/resume-pretool-guard": BIN / "resume-pretool-guard",
    "/opt/coastal-resume/bin/resume-stop-gate": BIN / "resume-stop-gate",
    "/opt/coastal-resume/bin/resume-run": BIN / "resume-run",
    "/opt/coastal-resume/lib/engine/__init__.py": GATE_ROOT
    / "engine"
    / "__init__.py",
    "/opt/coastal-resume/lib/engine/core.py": GATE_ROOT / "engine" / "core.py",
    "/opt/coastal-resume/lib/engine/mcp_server.py": GATE_ROOT
    / "engine"
    / "mcp_server.py",
    "/opt/coastal-resume/lib/judge/adapter.py": GATE_ROOT
    / "judge"
    / "adapter.py",
    "/opt/coastal-resume/lib/judge/prompt.fixed.txt": GATE_ROOT
    / "judge"
    / "prompt.fixed.txt",
    "/opt/coastal-resume/lib/validator/validate.py": GATE_ROOT
    / "validator"
    / "validate.py",
    "/opt/coastal-resume/lib/schemas/submission.schema.json": GATE_ROOT
    / "schemas"
    / "submission.schema.json",
    "/opt/coastal-resume/lib/schemas/judge.schema.json": GATE_ROOT
    / "schemas"
    / "judge.schema.json",
    "/opt/coastal-resume/lib/schemas/decision.schema.json": GATE_ROOT
    / "schemas"
    / "decision.schema.json",
    "/opt/coastal-resume/lib/schemas/manifest.schema.json": GATE_ROOT
    / "schemas"
    / "manifest.schema.json",
    "/opt/coastal-resume/lib/fixtures/pilot/manifest.frozen.json": GATE_ROOT
    / "fixtures"
    / "pilot"
    / "manifest.frozen.json",
    "/opt/coastal-resume/lib/fixtures/pilot/canary-fabricated-claim.submission.json": GATE_ROOT
    / "fixtures"
    / "pilot"
    / "canary-fabricated-claim.submission.json",
    "/opt/coastal-resume/lib/fixtures/pilot/parser-negative-duplicate-source.manifest.json": GATE_ROOT
    / "fixtures"
    / "pilot"
    / "parser-negative-duplicate-source.manifest.json",
}


def load_json(path: pathlib.Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    assert isinstance(value, dict)
    return value


def sha256(path: pathlib.Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def frontmatter(path: pathlib.Path) -> tuple[dict[str, str], str]:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    assert lines and lines[0] == "---", f"{path.name}: missing opening frontmatter"
    try:
        closing = lines.index("---", 1)
    except ValueError as error:
        raise AssertionError(f"{path.name}: missing closing frontmatter") from error
    fields: dict[str, str] = {}
    for line in lines[1:closing]:
        assert ":" in line, f"{path.name}: malformed frontmatter line"
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip()
        assert key and value and key not in fields
        fields[key] = value
    return fields, "\n".join(lines[closing + 1 :]).strip()


def run_hook(
    script: pathlib.Path,
    event: dict[str, Any],
    *,
    environment: dict[str, str],
) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [str(PYTHON), str(script)],
        input=json.dumps(event),
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        env=environment,
        check=False,
        timeout=10,
    )


@contextmanager
def protected_tree() -> Iterator[tuple[pathlib.Path, pathlib.Path, pathlib.Path]]:
    with tempfile.TemporaryDirectory(prefix="resume-policy-") as temp:
        root = pathlib.Path(temp)
        repo = root / "repo"
        models = repo / "models"
        models.mkdir(parents=True)
        allowed = models / "source.f90"
        allowed.write_text("DO 48 ITS=1,30\n", encoding="utf-8")
        outside = root / "outside.txt"
        outside.write_text("outside\n", encoding="utf-8")
        (models / "escape").symlink_to(outside)
        yield repo, allowed, outside


def pretool_event(
    repo: pathlib.Path,
    tool_name: str,
    tool_input: dict[str, Any],
) -> dict[str, Any]:
    return {
        "session_id": "mock-session",
        "cwd": str(repo),
        "hook_event_name": "PreToolUse",
        "tool_name": tool_name,
        "tool_input": tool_input,
        "tool_use_id": "mock-tool-use",
    }


def guard_environment(repo: pathlib.Path) -> dict[str, str]:
    environment = dict(os.environ)
    environment.update(
        {
            "COASTAL_RESUME_REPO_ROOT": str(repo),
            "COASTAL_RESUME_RUN_ID": RUN_ID,
        }
    )
    return environment


def test_managed_policy_has_every_phase6_lock() -> None:
    policy = load_json(POLICY / "50-coastal-resume.json")
    assert policy["allowManagedPermissionRulesOnly"] is True
    assert policy["allowManagedHooksOnly"] is True
    assert policy["allowManagedMcpServersOnly"] is True
    assert policy["disableSideloadFlags"] is True
    assert policy["strictPluginOnlyCustomization"] is True
    assert policy["disableAutoMode"] == "disable"
    assert policy["disableArtifact"] is True
    assert policy["disableClaudeAiConnectors"] is True
    assert policy["allowedMcpServers"] == [{"serverName": "resume-submit"}]

    permissions = policy["permissions"]
    assert permissions["defaultMode"] == "dontAsk"
    assert permissions["disableBypassPermissionsMode"] == "disable"
    required_denies = {
        "Bash",
        "PowerShell",
        "Write",
        "Edit",
        "NotebookEdit",
        "Artifact",
        "EnterWorktree",
        "ExitWorktree",
        "WebFetch",
        "WebSearch",
        "CronCreate",
        "CronDelete",
        "CronList",
        "ScheduleWakeup",
        "RemoteTrigger",
    }
    assert required_denies <= set(permissions["deny"])
    assert {
        "Agent(resume-code-reader)",
        "Agent(resume-pdf-reader)",
        "mcp__resume-submit__submit",
    } <= set(permissions["allow"])

    pretool = policy["hooks"]["PreToolUse"]
    stop = policy["hooks"]["Stop"]
    assert pretool == [
        {
            "matcher": "*",
            "hooks": [
                {
                    "type": "command",
                    "command": "/opt/coastal-resume/bin/resume-pretool-guard",
                    "args": [],
                }
            ],
        }
    ]
    assert stop == [
        {
            "hooks": [
                {
                    "type": "command",
                    "command": "/opt/coastal-resume/bin/resume-stop-gate",
                    "args": [],
                }
            ]
        }
    ]


def test_policy_readme_maps_every_section3_enforcement_point() -> None:
    text = (POLICY / "README.md").read_text(encoding="utf-8")
    required_terms = {
        "`models/` OS lock",
        "`corpus/` protection",
        "root managed settings",
        "managed permission-only",
        "bypass and auto closure",
        "sideload closure",
        "direct writer removal",
        "PreToolUse whitelist",
        "named subagents only",
        "exclusive managed MCP",
        "single submit surface",
        "manifest and realpath restriction",
        "root-owned executable and decision set",
        "subscription auth and judge isolation",
        "decision-engine-owned state",
        "Stop gate",
        "fixed run ID",
        "append-only attempt ID",
        "hash evidence chain",
        "no-progress hard stop",
        "canonical separation",
        "전역 적용과 한시 설치 전제",
        "설치 → 파일럿 → 제거",
        "상시 설치는 권장하지 않는다",
        "계정 또는 컨테이너 분리",
    }
    missing = sorted(term for term in required_terms if term not in text)
    assert not missing, missing


def test_managed_mcp_is_exactly_one_resume_submit_server() -> None:
    managed = load_json(POLICY / "managed-mcp.json")
    assert set(managed) == {"mcpServers"}
    assert set(managed["mcpServers"]) == {"resume-submit"}
    assert managed["mcpServers"]["resume-submit"] == {
        "type": "stdio",
        "command": "/opt/coastal-resume/bin/resume-submit-mcp",
        "args": [],
        "env": {},
    }


def test_agent_frontmatter_is_valid_and_readers_are_fixed() -> None:
    expected_names = {
        "resume-coordinator.md": "resume-coordinator",
        "resume-code-reader.md": "resume-code-reader",
        "resume-pdf-reader.md": "resume-pdf-reader",
    }
    for filename, expected_name in expected_names.items():
        fields, body = frontmatter(POLICY / "agents" / filename)
        assert fields["name"] == expected_name
        assert fields["description"]
        assert fields["permissionMode"] == "dontAsk"
        assert fields["model"] == "inherit"
        assert body

    coordinator, _ = frontmatter(POLICY / "agents" / "resume-coordinator.md")
    assert (
        coordinator["tools"]
        == "Agent(resume-code-reader, resume-pdf-reader), Read, Grep, Glob, "
        "mcp__resume-submit__submit"
    )
    for filename in ("resume-code-reader.md", "resume-pdf-reader.md"):
        fields, _ = frontmatter(POLICY / "agents" / filename)
        assert [tool.strip() for tool in fields["tools"].split(",")] == [
            "Read",
            "Grep",
            "Glob",
        ]


def test_pretool_guard_allows_only_safe_read_tools_and_submit() -> None:
    with protected_tree() as (repo, allowed, _):
        environment = guard_environment(repo)
        events = [
            pretool_event(repo, "Read", {"file_path": str(allowed)}),
            pretool_event(
                repo,
                "Grep",
                {"pattern": "ITS", "path": str(repo / "models")},
            ),
            pretool_event(
                repo,
                "Glob",
                {"pattern": "**/*.f90", "path": str(repo / "models")},
            ),
            pretool_event(
                repo,
                "Agent",
                {
                    "prompt": "Read the assigned source.",
                    "description": "Read source",
                    "subagent_type": "resume-code-reader",
                },
            ),
            pretool_event(repo, "mcp__resume-submit__submit", {"run_id": RUN_ID}),
        ]
        for event in events:
            completed = run_hook(
                BIN / "resume-pretool-guard",
                event,
                environment=environment,
            )
            assert completed.returncode == 0, (event, completed.stderr)


def test_pretool_guard_denies_writer_agent_and_path_bypasses() -> None:
    with protected_tree() as (repo, _, outside):
        environment = guard_environment(repo)
        denied = [
            pretool_event(repo, "Write", {"file_path": str(repo / "x"), "content": "x"}),
            pretool_event(
                repo,
                "Agent",
                {
                    "prompt": "write",
                    "description": "writer",
                    "subagent_type": "general-purpose",
                },
            ),
            pretool_event(
                repo,
                "Read",
                {"file_path": str(repo / "models" / ".." / outside.name)},
            ),
            pretool_event(
                repo,
                "Read",
                {"file_path": str(repo / "models" / "escape")},
            ),
            pretool_event(
                repo,
                "Read",
                {"file_path": str(repo / "models" / "%2e%2e" / "outside.txt")},
            ),
            pretool_event(
                repo,
                "Glob",
                {"pattern": "../**", "path": str(repo / "models")},
            ),
            pretool_event(
                repo,
                "Glob",
                {"pattern": "*", "path": str(repo / "models")},
            ),
        ]
        for event in denied:
            completed = run_hook(
                BIN / "resume-pretool-guard",
                event,
                environment=environment,
            )
            assert completed.returncode == 2, (event, completed.stdout, completed.stderr)


def _load_engine_test_module() -> Any:
    path = GATE_ROOT / "tests" / "test_engine.py"
    spec = importlib.util.spec_from_file_location("resume_gate_policy_engine_fixture", path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def stop_event() -> dict[str, Any]:
    return {
        "session_id": "mock-session",
        "cwd": str(REPO_ROOT),
        "hook_event_name": "Stop",
        "stop_hook_active": False,
        "last_assistant_message": "mock",
        "background_tasks": [],
        "session_crons": [],
    }


def test_stop_gate_binds_valid_pass_to_current_run() -> None:
    engine_test = _load_engine_test_module()
    with engine_test.engine_context(run_id=RUN_ID) as (
        engine,
        manifest,
        _,
        _,
    ):
        environment = dict(os.environ)
        environment.update(
            {
                "COASTAL_RESUME_RUN_ID": RUN_ID,
                "COASTAL_RESUME_STATE_ROOT": str(engine.state_root),
            }
        )
        missing = run_hook(
            BIN / "resume-stop-gate",
            stop_event(),
            environment=environment,
        )
        assert missing.returncode == 0
        assert json.loads(missing.stdout)["decision"] == "block"

        receipt = engine.submit(engine_test.submission(manifest, run_id=RUN_ID))
        assert receipt["status"] == "PASS"

        other_environment = dict(environment)
        other_environment["COASTAL_RESUME_RUN_ID"] = "policy-run-other"
        other = run_hook(
            BIN / "resume-stop-gate",
            stop_event(),
            environment=other_environment,
        )
        assert json.loads(other.stdout)["decision"] == "block"

        current = run_hook(
            BIN / "resume-stop-gate",
            stop_event(),
            environment=environment,
        )
        assert current.returncode == 0
        assert current.stdout == ""
        assert current.stderr == ""


def test_launcher_pins_isolated_subscription_environment_without_credentials() -> None:
    text = (BIN / "resume-run").read_text(encoding="utf-8")
    for required in (
        '"HOME": str(isolated_home)',
        '"GROK_HOME": str(grok_home)',
        '"CODEX_HOME": str(codex_home)',
        '"CLAUDE_CONFIG_DIR": str(claude_config)',
        '"OPENAI_API_KEY"',
        '"XAI_API_KEY"',
        "GROK_CONFIG_SHA256",
        "COMPAT_VENDORS",
        "COMPAT_CELLS",
        "MARKETPLACE_KEYS",
        "os.execve",
    ):
        assert required in text
    assert "refresh_token" not in text


def test_mcp_wrapper_uses_fixed_engine_arguments_and_removes_api_keys() -> None:
    text = (BIN / "resume-submit-mcp").read_text(encoding="utf-8")
    for required in (
        "lib_root=/opt/coastal-resume/lib",
        '"$lib_root/engine/mcp_server.py"',
        '"$lib_root/fixtures/pilot/manifest.frozen.json"',
        '"$lib_root/fixtures/pilot/canary-fabricated-claim.submission.json"',
        '"$lib_root/fixtures/pilot/parser-negative-duplicate-source.manifest.json"',
        '"$lib_root/validator/validate.py"',
        "--repo-root",
        "--manifest",
        "--run-id",
        "--state-root",
        "--canary-submission",
        "--parser-negative",
        "--execution-artifact",
        "--empty-cwd",
        "unset OPENAI_API_KEY XAI_API_KEY GROK_CODE_XAI_API_KEY",
    ):
        assert required in text
    assert "/home/firesinger/coastal-wiki/tools/resume-gate" not in text
    assert "COASTAL_RESUME_LIB" not in text


def test_install_manifest_hashes_all_phase5_install_payloads() -> None:
    parsed: dict[str, str] = {}
    for line in MANIFEST.read_text(encoding="utf-8").splitlines():
        digest, destination = line.split("  ", 1)
        assert HASH_RE.fullmatch(digest)
        assert destination.startswith("/")
        assert destination not in parsed
        parsed[destination] = digest
    assert set(parsed) == set(DESTINATION_SOURCES)
    for destination, source in DESTINATION_SOURCES.items():
        assert source.is_file(), source
        assert parsed[destination] == sha256(source), (destination, source)

    install_text = (GATE_ROOT / "INSTALL.md").read_text(encoding="utf-8")
    for required in (
        "설치 → 파일럿 → 제거",
        "sudo sha256sum -c /opt/coastal-resume/INSTALL-MANIFEST.sha256",
        "sudo rm -f",
        "claude /doctor",
        "claude mcp list",
        "`models/`·`corpus/`",
    ):
        assert required in install_text
    for destination in DESTINATION_SOURCES:
        assert destination in install_text
    for stale_alias in (
        "/opt/coastal-resume/share/prompts/codex-judge.md",
        "/opt/coastal-resume/share/prompts/grok-judge.md",
        "/opt/coastal-resume/share/fixtures/pilot/manifest.json",
    ):
        assert stale_alias not in install_text


HASH_RE = __import__("re").compile(r"^[0-9a-f]{64}$")

TESTS = [
    test_managed_policy_has_every_phase6_lock,
    test_policy_readme_maps_every_section3_enforcement_point,
    test_managed_mcp_is_exactly_one_resume_submit_server,
    test_agent_frontmatter_is_valid_and_readers_are_fixed,
    test_pretool_guard_allows_only_safe_read_tools_and_submit,
    test_pretool_guard_denies_writer_agent_and_path_bypasses,
    test_stop_gate_binds_valid_pass_to_current_run,
    test_launcher_pins_isolated_subscription_environment_without_credentials,
    test_mcp_wrapper_uses_fixed_engine_arguments_and_removes_api_keys,
    test_install_manifest_hashes_all_phase5_install_payloads,
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
    print(f"\n{len(TESTS) - len(failures)}/{len(TESTS)} policy fixtures behaved as required")
    if failures:
        print("FAILURES:")
        for failure in failures:
            print(f"- {failure}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
