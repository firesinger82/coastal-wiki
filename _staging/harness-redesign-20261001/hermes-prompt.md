One-off research task (manual, not a scheduled collection). Search X (x_search) and the web for practitioner discussion and concrete implementations of "harness engineering" for AI coding/research agents, especially:
1. Claude Code harness patterns: PreToolUse / Stop hooks used as gates, task contracts / done_when, state files outside the conversation, managed settings, subagent verifiers, "receipts".
2. Separating builder and verifier models; completion gated by evidence rather than model self-report; preventing scope drift and goal substitution in long-running agent runs.
3. Codex CLI / OpenAI agent harness practices (sandbox, exec wrappers, AGENTS.md), and multi-model (Claude+Codex) orchestration with external gates.
4. Failure reports: agents declaring done without verification, redefining the task, exhaustive busywork unrelated to the goal; what fixed it.
Prefer posts from 2026 with concrete repos, configs or measured results. For each item give: author/handle, date, URL, one-line claim, and whether it includes a concrete artifact (repo/config/data). Return 15–30 items, then a short synthesis of recurring recommendations. Do not write files outside stdout.
