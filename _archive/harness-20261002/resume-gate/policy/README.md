# resume-gate managed policy mapping

This directory is the source form for the phase-6 managed Claude Code policy.
It has no enforcement effect until the phase-8 root installation and phase-9
smoke test succeed. The threat-model statements below correspond to
`BUILDPLAN-20260724-recovered.md` §3, lines 183–204.

| §3 enforcement claim | Policy key or installed artifact | What is blocked |
|---|---|---|
| `models/` OS lock | Existing OS ownership/mode; not changed here | Writes to the already protected model tree |
| `corpus/` protection | `permissions.deny` writer set plus the PreToolUse whitelist | Creation or unlocking through a session tool |
| root managed settings | Phase-8 destination `/etc/claude-code/managed-settings.d/50-coastal-resume.json` | User/project/CLI settings cannot replace this tier |
| managed permission-only | `allowManagedPermissionRulesOnly: true` | User/project `allow`, `ask`, and `deny` additions |
| bypass and auto closure | `permissions.disableBypassPermissionsMode: "disable"`; `disableAutoMode: "disable"` | Starting or switching to either permissive mode |
| sideload closure | `disableSideloadFlags: true`; `strictPluginOnlyCustomization: true`; `allowManagedHooksOnly: true` | `--agents`, `--mcp-config`, user/project agents, hooks, skills, and MCP customization |
| direct writer removal | `permissions.defaultMode: "dontAsk"`; managed deny rules for `Bash`, `PowerShell`, `Write`, `Edit`, `NotebookEdit`, `Artifact`, worktree, web, cron/routine, workflow, and messaging tools; `disableArtifact: true` | Direct filesystem, worktree, publication, network, and scheduled writer routes |
| PreToolUse whitelist | Managed `hooks.PreToolUse` invokes `/opt/coastal-resume/bin/resume-pretool-guard` for `*` | Any non-whitelisted tool, unsafe path, traversal, symlink escape, or malformed input |
| named subagents only | Coordinator `tools: Agent(resume-code-reader, resume-pdf-reader)` plus guard check; both reader files fix `tools: Read, Grep, Glob` | General, plugin, worktree, writer, or resumed arbitrary agents |
| exclusive managed MCP | `managed-mcp.json`; `allowedMcpServers`; `allowManagedMcpServersOnly: true`; `disableClaudeAiConnectors: true` | Project, user, plugin, claude.ai, and `claude mcp add` servers |
| single submit surface | `managed-mcp.json` exposes only `resume-submit`; coordinator names only `mcp__resume-submit__submit` | Alternate MCP tools and general filesystem RPC |
| manifest and realpath restriction | Phase-3 validator plus PreToolUse path normalization | Unregistered, changed, escaped, or symlinked source evidence |
| root-owned executable and decision set | Phase-8 `/opt/coastal-resume/bin/*` and `/opt/coastal-resume/lib/` destinations | Session replacement of launcher, hooks, MCP wrapper, validator, judge adapter/prompt, engine, schemas, or frozen controls |
| subscription auth and judge isolation | `resume-run` fixes `HOME`, `GROK_HOME`, and `CODEX_HOME` and removes API-key/override variables; adapter performs the auth preflight | API-key routing and unapproved Grok compatibility/customization |
| decision-engine-owned state | Phase-5 engine and schema | Worker-supplied completion fields |
| Stop gate | Managed `hooks.Stop` invokes `/opt/coastal-resume/bin/resume-stop-gate` | Normal completion without a verified current-run PASS |
| fixed run ID | `resume-run` creates and exports one run ID; MCP wrapper and Stop gate require it | Reuse of another run's decision |
| append-only attempt ID | Phase-5 engine | Replacement of an earlier attempt directory |
| hash evidence chain | Phase-5 engine; Stop gate re-verification | Undetected mutation of ledger-bound attempt artifacts |
| no-progress hard stop | Phase-5 engine | Identical or evidence-free retry loops |
| canonical separation | MCP wrapper fixes the external state root; managed writers remain denied | Treating PASS as permission to modify `models/` or `corpus/` |

The managed file deliberately layers three independent restrictions: a narrow
agent tool list, managed permission rules in `dontAsk` mode, and an all-tool
PreToolUse hook. A silent hook success does not grant permission; it only lets
the managed permission engine evaluate the already restricted call.

## 전역 적용과 한시 설치 전제

Claude Code managed settings는 머신 전역에 적용된다. 이 정책이 설치된
동안에는 이 PC의 모든 Claude Code 세션에서 `Read`·`Grep`·`Glob`도
`models/`·`corpus/` 아래로 제한되고, `Bash`·`Write`·`Edit`·`Skill`·MCP
등의 비허용 도구는 차단된다.

파일럿은 반드시 `INSTALL.md`의 **설치 → 파일럿 → 제거** 순서로 운용한다.
상시 설치는 권장하지 않는다. 13단계 상시 운용은 계정 또는 컨테이너 분리를
전제로 별도 설계해야 한다.

설치와 제거 어느 쪽도 `models/`·`corpus/`의 소유권, 모드, 내용 또는 기존
잠금을 건드리지 않는다.
