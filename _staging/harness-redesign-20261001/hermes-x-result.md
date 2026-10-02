**X + web search synthesis (harness engineering for AI coding/research agents, 2026 focus)**

**X results (via x_search, 2026 posts):**

1. @jaketselby (mid-Sep 2026) — https://x.com/jaketselby/status/2100578016749355084  
   One source of truth for rules/skills/roles/stances translated to Claude Code/Codex native formats; hooks + measurement against labeled transcripts. Concrete artifact: yes (https://github.com/JakeSelby/model-citizen, MIT, installer, ruleprobe).

2. @jaketselby (v0.13 thread, late Sep 2026) — https://x.com/jaketselby/status/2103518032505225467  
   Trust, measurement, framework isolation, reduced context overhead in harness. Concrete artifact: yes (model-citizen repo updates).

3. @akshay_pachaar (Jul 2026) — https://x.com/akshay_pachaar/status/2072961737008336937  
   Harness (context/memory/tools/verification) often beats model upgrades on same task. Concrete artifact: yes (https://github.com/walkinglabs/learn-harness-engineering, 14 lectures + 8 projects + AGENTS.md starters).

4. @RoundtableSpace (late Sep 2026) — https://x.com/RoundtableSpace/status/2104228317616595247  
   learn-harness-engineering repo reached ~15k stars quickly as practical curriculum. Concrete artifact: yes (repo above).

5. @cj_enlighten (mid-2026) — https://x.com/cj_enlighten/status/2085438188898734410  
   Goal drift is usually a harness failure (context compaction loses pinned objective), not prompt issue. Concrete artifact: yes (links to /goal pattern + Substack).

6. @BAYC2043 (2026) — https://x.com/BAYC2043/status/2071878840385736991  
   /goal pins objective outside context window (GOAL.md/SQLite) for long runs. Concrete artifact: yes (Codex-style persistent goal examples).

7. @skirano (2026) — https://x.com/i/status/2066225908202053818  
   Agents self-author /goal for main task + sub-agents to reduce handoff drift. Concrete artifact: yes (video + Claude Engineer examples).

8. @gilgoldstein (Aug–Sep 2026) — https://x.com/gilgoldstein/status/2103539782139715732  
   harness-kit provides reusable abstractions for deterministic workflows. Concrete artifact: yes (romabeckman harness-kit TS abstractions).

9. @impactology (2026) — https://x.com/impactology/status/2090089629945102414  
   coleam00/archon as harness builder for repeatable AI coding. Concrete artifact: yes (coleam00 GitHub repos).

10. @Jolyne_AI (late Aug 2026) — https://x.com/Jolyne_AI/status/2096237169786732625  
    coleam00/excalidraw-diagram-skill with self-correction loop (Playwright). Concrete artifact: yes (skill config + rendering loop).

**Web results (key 2026 sources with concrete artifacts):**

11. cc.bruniaux.com/guide/agent-harness/ (Oct 1 2026) — https://cc.bruniaux.com/guide/agent-harness/  
    Model-harness pair is the evaluation unit; harness choice changed tokens/solved task by up to 40x on Terminal-Bench Pro (controlled study). Concrete artifact: yes (harness decomposition + tables).

12. arxiv.org/abs/2609.00006 (Jul/Sep 2026) — https://arxiv.org/abs/2609.00006 (and HTML)  
    Source-code anatomy of 11 harnesses (Claude Code, Codex CLI, Hermes, etc.); 13 observations + 29 patterns + 90-line MVP scaffold. Concrete artifact: yes (paper + pinned July 2026 releases).

13. github.com/whieet/harness-kit (Aug 2026) — https://github.com/whieet/harness-kit  
    Claude Code plugin: plan-gating (PreToolUse), verification gate (Stop hook blocks done), loop detection, gen-eval separation via subagent. Concrete artifact: yes (hooks, slash commands, rubric, CLAUDE.md scaffolding).

14. github.com/coleam00/harness-engineering-demo (2026) — https://github.com/coleam00/harness-engineering-demo  
    .claude/hooks examples: post_tool_use_lint.py (PostToolUse), stop_validate.py (Stop blocks until ruff+pytest green), security_guard.py (PreToolUse deny .env/rm -rf). Concrete artifact: yes (full hook scripts + settings.json).

15. github.com/kyu1204/oh-my-harness (2026) — https://github.com/kyu1204/oh-my-harness  
    harness.yaml generates CLAUDE.md + enforceable hooks (block git commit on test fail, TDD guard, path guards) for Claude Code/Codex/Pi. Concrete artifact: yes (harness.yaml + sync check).

16. 13labs.au/guides/ai-coding-agent-harness-hooks-verification (Aug 13 2026) — https://www.13labs.au/guides/ai-coding-agent-harness-hooks-verification  
    Stop hook as deterministic gate (blocks turn end until checks pass; Claude overrides after 8 blocks); PreToolUse/PostToolUse for plan/verification. Concrete artifact: yes (hook event table + examples).

17. arxiv.org/abs/2505.02709 (May 2025, referenced 2026) — https://arxiv.org/abs/2505.02709  
    Goal drift evaluation in agents; best scaffolded Claude 3.5 Sonnet near-perfect adherence >100k tokens in hard setting. Concrete artifact: yes (experimental setup + results).

18. mljar.com/blog/ai-agent-harness/ (Sep 24 2026) — https://mljar.com/blog/ai-agent-harness/  
    Harness engineering discipline; open-source list (Codex CLI sandbox, OpenCode, Aider). Concrete artifact: yes (comparison table + definitions).

19. marktechpost.com/2026/09/14/agent-harness-vs-agent-framework-vs-mcp (Sep 14 2026) — https://www.marktechpost.com/2026/09/14/agent-harness-vs-agent-framework-vs-mcp-which-layer-owns-the-loop-state-tools-permissions-and-recovery/  
    Harness owns loop/permissions/state; Anthropic separates generator/evaluator; OpenAI reports on discipline. Concrete artifact: yes (layer ownership breakdown).

20. addyosmani.com/blog/agent-harness-engineering/ (Apr 19 2026) — https://addyosmani.com/blog/agent-harness-engineering/  
    Hooks for self-improving harness; sprint contract (generator-evaluator negotiate done condition) catches scope drift. Concrete artifact: yes (hook examples + planning patterns).

21. pulumi.com/blog/stop-tuning-prompts-build-a-harness/ (May 26 2026) — https://www.pulumi.com/blog/stop-tuning-prompts-build-a-harness/  
    Stop hook for context survival + rule drift detection; hooks enforce where prose fails (~70% vs 100%). Concrete artifact: yes (settings.json + session_start/stop examples).

22. agentpatterns.ai/tool-engineering/hooks-lifecycle-events/ (Oct 1 2026) — https://agentpatterns.ai/tool-engineering/hooks-lifecycle-events/  
    PreToolUse blocks/rewrites; PostToolUse observes; matcher + exit 2 for deny. Concrete artifact: yes (JSON payload examples + use-case table).

23. padiso.co/blog/subagent-failure-modes-loops-drift-recovery-patterns/ (May 9 2026) — https://www.padiso.co/blog/subagent-failure-modes-loops-drift-recovery-patterns/  
    Loops from ambiguous tool results; prompt drift from gradual deviation; observability + eval required. Concrete artifact: yes (production incident examples + taxonomy).

24. ceaksan.com/en/llm-agentic-failure-modes (Apr 19 2026) — https://ceaksan.com/en/llm-agentic-failure-modes  
    Task drift, reward hacking, alignment faking in loops; defenses: goal anchoring, tool schema validation, eval suite. Concrete artifact: yes (8-mode taxonomy + mitigations).

25. thenewstack.io/aws-strands-harness-agent/ (Sep 21 2026) — https://thenewstack.io/aws-strands-harness-agent/  
    Strands Harness 45% cheaper than Claude Code/Codex on matched runs; Terminal Bench 2.1 numbers. Concrete artifact: yes (benchmark costs/scores vs DeepSeek Harness).

**Short synthesis of recurring recommendations (from 2026 sources)**  
- Treat the harness (loop + hooks + state + verification + permissions) as the primary engineering surface; model is secondary.  
- Use PreToolUse for hard gates (plan required before edit, deny dangerous cmds like rm -rf/.env), PostToolUse for auto-lint/format, Stop/SubagentStop for verification gates that block "done" until evidence (tests/lint/rubric) passes.  
- Separate builder (generator) from verifier/evaluator subagent or hook; gate completion on external evidence, not self-report.  
- Pin goals persistently outside context (/goal file, GOAL.md, SQLite, or state file) and re-inject to fight compaction-induced drift/scope creep.  
- Externalize state (plan files, transcripts, checkpoints, memory dir) and use hooks for self-improvement (e.g., propose CLAUDE.md updates on Stop).  
- Measure everything: precision/recall on labeled transcripts, benchmark harness variants on fixed model, CI eval of rules/hooks.  
- Concrete patterns that recur: plan-gating, loop detection (edit count on one file), gen-eval split, sandbox/allowlists, subagent tool whitelisting via frontmatter or hooks.  
- Failure fixes: add Stop hooks + persistent goal anchoring (reduced drift in long runs); avoid relying on prose instructions alone.  
- Artifacts worth starting from: model-citizen, learn-harness-engineering, whieet/harness-kit, coleam00 demo hooks, oh-my-harness, arXiv 2609.00006 scaffold.  

All items drawn directly from tool outputs (web + X). No files written.

---
Claude 확인 (2026-10-02): 인용된 저장소 5개(whieet/harness-kit, coleam00/harness-engineering-demo, kyu1204/oh-my-harness, JakeSelby/model-citizen, walkinglabs/learn-harness-engineering)와 arXiv 2609.00006 은 HTTP 200 으로 실재 확인. X 게시물 링크·각 항목의 주장 내용은 미확인(Grok 요약).
