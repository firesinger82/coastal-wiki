# Fable 5.1 계획 검토

**Verdict: no blockers to adopting BUILD-PLAN as the governing method.** The chain in §1 and the six evidence levels in §4 match the brief, keep the citation_status enum unchanged (CONVENTIONS §2.0 forbids new states), place published validation in models/concepts and personal results in runs/experience (§8.1 ③, absolute rules 2 and 8), and preserve whole-model scope, XBeach R1–R4 and per-claim gates (§2 line 54 non-inheritance is mirrored in §10). All root-relative links resolve except the not-yet-installed `BUILD-PLAN.md`. Four priority findings below need small fixes. Findings 1 and 2 are plan-text fixes. Findings 3 and 4 are for the implementation step, which has not been performed and is not reviewed here.

**Priority findings**

1. **Feature map location escapes the citation gate (plan §2).** The map is to live in each model README, but CONVENTIONS §2.1 exempts directory READMEs from frontmatter, and the hygiene validator only scopes canonical notes. Rows stating "supported / held / out of scope, version X" are capability claims. Minimal fix: one sentence in §2 stating the README holds pointers only, and each row's support claim lives in a frontmattered note (existing manual-notes index or one map note per model) citing source_id, page and version.

2. **Evidence levels are unfindable without a marker (plan §4).** Prose-only description is fine per the no-new-enum rule, but the six level names should be used verbatim in notes so `rg` and L4 can distinguish "코드 구현" from "문서 지원". Minimal fix: add "노트에서는 이 표의 수준명을 그대로 쓴다" to §4. No new field or workflow.

3. **The patch does not perform the Fable substitution.** CLAUDE.md lines 89 and 92 still read "Opus", and the patch's third hunk keeps them as context. AGENTS.md has no model line at all. Plan §9.3 says "작성 모델 지정 갱신" but the artifact lacks the hunks. Minimal fix at apply time: two line edits in the santa-method list to "Fable 5.1 (`claude-fable-5-1`)" and one default line in AGENTS. Optionally name the Codex models in §8, since the routing rule forbids omitting `--model`.

4. **Work rule 1 loses its explicit read-only default.** The replacement keeps scope discipline but drops "읽기·조사·보고가 기본값". The 2026-07-24 incident was precisely modification substituted for reading. Minimal fix: retain one sentence, "조사·질문 요청에서는 수정하지 않는다", inside the new rule 1. This does not reintroduce mid-task confirmation prompts.

**Minor, implementation-level**

- The patched "작업별 문서 안내" list has no entry for BUILD-PLAN itself. Add one bullet: "모델 기능 근거를 보강·비교할 때: BUILD-PLAN.md §2–§7". README routing should point the same way.
- BUILD-PLAN §1 and §11 link into `_staging/build-method-20260914/` and `_staging/instruction-review-20260914/`, both currently untracked. Commit them in the same commit or the links dangle for readers.
- `BUILD-PLAN.md` is not in the CONVENTIONS §2.1 exempt list. The validators do not check root files, so commit will pass, but the list is now incomplete. Either add the name or accept the gap.
- §9.5 adds one line to a plan.md that already has 6 uncommitted lines. Partial staging with `git add -p` is required. Confirm the hook validates the staged snapshot, not the working tree, before relying on it.
- coastal-audit's description lists the bare trigger "audit", which is what caused the instruction-review misfire. The planned description-only rewrite is the right scope.

**Checks against the brief that passed**

- Breadth without exhaustion: §2 maps from the official manual's classification, §5 makes collection purpose-driven and keeps the MPI/Jumpshot exclusion.
- Readiness vs report: §6 states report completion does not equal readiness, forbids completion percentages, and requires justified N/A.
- Comparison ordering: §7 fills rows only after both models' bundles meet §6, and lists the coupling contract separately.
- First bundle (§10) is scoped to two notes plus the needed source spans, with independent review in done_when.

**Limitations of this review**

- I did not read the model-readiness report, the instruction-review README, or the ADCIRC notes, so I cannot confirm the §10 scope items are the right ones.
- I did not test whether the patch applies cleanly. Hunk positions match current CLAUDE.md line numbers.
- My routing memory still says "heavy reasoning → fable, else opus". This session's rule, Fable for all plan authoring and review, was not written to memory because the session is read-only.
