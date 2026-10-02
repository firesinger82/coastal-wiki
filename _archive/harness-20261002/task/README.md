# Coastal task harness v1.1

Implements `_staging/harness-redesign-20261001/DESIGN-v1.md`, including the overriding
v1.1 decisions. Threat model A: prevent drift and unsupported self-report, and make
departures visible. Writable hash chains detect corruption; they do not authenticate
executions against a deliberate full-chain replacement, truncation, forged verdicts,
or WSL/root bypass. Hooks are reminders/gates in cooperating Claude sessions.

Python 3.12 standard library only, Linux (`flock`, `/proc`, parent-death signals).
No dependencies or global/Git hooks are installed by running these tools.

## Commands

Run from the repository, or provide `--repo /absolute/repository` to every command.

```sh
tools/task/bin/new-task my-task --model XBeach --function vegetation-drag \
  --question 'Does the vegetation drag implementation support the specified setup?'
# Edit the draft CONTRACT.json and pin input SHA256s before approval.
sudo /usr/local/lib/coastal-task/bin/approve --repo "$PWD" my-task
tools/task/bin/status --activate my-task
tools/task/bin/codex-run --task my-task --role verifier --model claude-fable-5-1 --purpose-review
tools/task/bin/codex-run --task my-task --role worker --model gpt-6-sol --write prompt.txt
tools/task/bin/codex-run --task my-task --role verifier --model claude-fable-5-1
tools/task/bin/receipt my-task
tools/task/bin/receipt my-task --verify
tools/task/bin/receipt my-task --staged
tools/task/bin/status --json
tools/task/bin/new-task my-task --revise
tools/task/bin/status --clear
tools/task/bin/codex-run --task none --purpose 'ordinary wiki investigation' --model gpt-6-sol prompt.txt
```

Model arguments are examples, not availability claims. The backend is `codex exec`.
It must actually execute the requested slug and expose that identity in structured
output or its persisted session `turn_context`. Missing/ambiguous identity and fallback
are failures. A stock Codex provider may not support an Anthropic/xAI slug; that fails
closed and consumes the attempt. This implementation does not invent another provider
or substitute an OpenAI verifier. Confirm the local provider supports the approved
family before using it. No live model calls were used in the test suite.

`approve` must be invoked from the protected installed copy, not with
`sudo tools/task/bin/approve`. It checks effective UID, protected code ownership,
path safety, and revision monotonicity. One private byte snapshot is displayed and
hashed; type the exact function name (EOF/wrong name cancels). A changed contract
requires `new-task --revise` and approval again. Immutable approval/snapshot files
preserve previous revisions; a diff is displayed during the next approval.

`codex-run` logs and fsyncs a reservation before spawning. Failed attempts, timeouts,
SIGTERM, SIGKILL/recovery all count. A Linux parent-death signal terminates the backend
when its wrapper dies. A subsequent launch closes dead reservations as interrupted;
live reservations reject concurrent launches. The last run slot is reserved for
verification. `wall_hours` runs from the first reservation of the current revision
and times out the backend, including the time between runs.

Default execution is read-only with stdin `/dev/null`. Worker `--write` changes the
working root to `tasks/<id>/outputs/`, pins writable roots there, disables implicit
project root discovery and temporary-directory writes, and forbids network access
inside the command sandbox. Output hashes are enumerated against `allowed_outputs`.
Codex's own session/auth/output capture files are executor bookkeeping; model tool
writes are subject to the sandbox. The sandbox behavior was checked through stub
arguments; real-runtime verification is a post-install human smoke test.

Verifier prompts and first purpose questions come exclusively from the contract.
Verdicts cover exactly the requested questions and bind task/revision/contract,
pinned input hashes, checker version, and candidate hashes to a successful run.
Output checks and `tools/validate-all.sh` are run by receipt. Current inputs,
candidate, contract, approvals, policy, and ledger are checked again afterward.
`RECEIPT.json` is deterministic for deterministic check programs and fixed snapshots:
there is no generation timestamp. `STATUS.json` is generated only by receipt and
is the completion authority. Receipt exits 0 for complete, 1 for incomplete/paused,
2 for malformed/drifted provenance. Failed execution exits nonzero; a successfully
executed review returning FAIL is logged normally and makes receipt incomplete.

`receipt --verify` recomputes without writing. `--staged` also compares every task
file and pinned input against the Git index; missing/extra files and differences
are rejected. It is an opt-in feedback command for completion/application review.
Draft/history and ordinary wiki commits remain permitted. Existing Git hooks are
untouched; pre-commit is bypassable and cannot be treated as a security boundary.

## Contract and state

`schemas/` defines strict records. The stdlib evaluator implements only the exact
checked-in JSON Schema vocabulary and fails on unknown keywords. Duplicate JSON
keys, non-finite values, malformed Unicode, unknown fields, symlinks, path traversal,
duplicate input/criterion IDs, and off-task output patterns are rejected.
Output globs match the whole POSIX path: `*`, `?`, and bracket classes stay within
one component; `**` spans zero or more directories.

Check `spec` is one of:

```json
{"type":"exists","path":"tasks/my-task/outputs/result.txt"}
{"type":"sha256","path":"tasks/my-task/outputs/result.txt","sha256":"<64 hex>"}
{"type":"command","path":"tools/check-task.sh","args":[],"timeout_seconds":60}
```

Command checkers must be executable, repository-relative, and listed in `inputs`
with their SHA256; they receive repository cwd and no stdin. Pin all checker data
and dependencies as inputs. The checker version also hashes harness bin/lib/schemas,
all repository `tools/validate-*` entry points/helpers, and command checkers.

`build_plan_levels` has `target` and `not_performed` lists; receipt preserves them
without converting unperformed levels into verified claims. They partition all five
levels without overlap or duplicate entries. `model` names the
coastal/domain model; the execution slug comes from required `--model` and actual
metadata. Families are fixed: `gpt-*`/`codex-*` → openai;
`claude-*`/`opus*`/`fable*`/`sonnet*` → anthropic; `grok-*` → xai.

`state/ACTIVE` holds `{task_id, revision, contract_sha256}`. `status --activate`
validates approval; the first task launch also activates a matching task. A different,
corrupt, or superseded pointer prevents launch until explicitly repaired/activated.
`status --clear` clears the pointer. Revision archives the prior contract and clears
that task's pointer; approvals, runs, verdicts, receipts, and outputs remain preserved.
Draft → approved → running → incomplete/paused/complete is derived by status from
contract/approval/reservations and the current receipt. Archived contract revisions
are superseded. No status writer other than receipt is introduced.

Goal-pin distinguishes missing ACTIVE from corrupt/stale state. SessionStart
(startup/resume/compaction) and SubagentStart emit four bounded lines for active tasks;
UserPromptSubmit emits one. Maximum six lines, 240 characters per line. Ordinary wiki
Write/Edit/validation is allowed; authority/history edits and direct Codex commands
are denied by PreToolUse JSON, including subagent payloads. Malformed hook payloads
produce an explicit denial (goal-pin produces a warning). Missing hook executables
and timeouts cannot be made fail-closed by a command hook itself: execution/receipt
gates remain necessary, and hook loading needs the manual smoke test.

## Decisions

- User scope overrides v1 live-pilot, global hook, archive, policy-document, and commit
  steps: no live calls, sudo execution, install-script execution, Git hook changes,
  legacy-source moves, `models/` changes, or commits are performed here. Installation
  is a human-run combined dry-run/apply script; its backup preserves installed legacy
  artifacts. Old source `tools/resume-gate/` remains intact.
- `model` means the domain/coastal model (e.g. XBeach). Worker/verifier independence
  uses backend slugs and actual run metadata, not this domain name. A worker's family
  must differ from the contract verifier family; two model-application reviewers must
  have different actual model slugs and separate successful runs. The latest review
  for each model counts; FAIL/UNCERTAIN or a failed/stale latest run cannot be hidden
  by an older PASS. Purpose review is a separate `--purpose-review` phase, covering
  the mandatory relevance question before the first worker. It survives output changes
  but never contract/input/checker drift.
- Purpose + worker + final review require at least three slots. One slot is always
  withheld from workers. Reservations are serialized with flock and one task cannot
  run two backends concurrently; distinct tasks can run only after explicit ACTIVE
  selection. Budgets are per revision; interrupted/failed attempts are never refunded.
  Non-task runs are read-only, have no task role/approval/budget, and only log.
- Two FAILs for an item within an unchanged output segment permanently pause that
  revision, even if an intervening reviewer says PASS. A changed output between FAILs
  resets that segment. Recovery requires a new revision and human approval; there
  is no unapproved auto-unpause.
- Every `.patch`/`.diff` artifact conservatively needs two independent models, even
  if its destination is not recognizable. Scripts containing `models/` also require
  two. Other model-application artifacts must declare a constraint beginning
  `models-application:`; opaque intent cannot be proven from hashes. These artifacts
  can be drafted/reviewed but receive application authority only with a complete
  staged receipt. Actual application to `models/` remains the existing human gate.
- `max_records` counts JSON array elements (other JSON values: one), nonempty JSONL
  records (strictly decoded), and nonempty lines for other files. No unspecified
  filesystem-wide record scan is added. Receipt enforces this optional bound.
- Receipt time fields come from recorded runs; completion is based on recorded
  execution duration, not the time receipt is regenerated. A new launch is blocked
  once wall time expires. Check commands must themselves be deterministic; stdout
  and stderr hashes make nondeterminism visible to `--verify`.
- Test mode is explicit: `COASTAL_TASK_TEST_ROOT` must name an owned mode-0700 `/tmp`
  directory. It permits unprivileged source-copy approval and stub execution, with
  approvals confined under that directory. This is the deliberate exception needed
  for sudo-free tests. Production rejects overrides; `COASTAL_TASK_APPROVALS_DIR` is
  accepted only inside the test root. `COASTAL_TASK_BACKEND` is one executable path,
  receives Codex exec arguments, and is rejected without test mode. Never set these
  variables for human production approval.
- The suite tests hook protocol/loading configuration and sandbox arguments, not
  actual Claude lifecycle, sudo authentication, or live-provider sandbox/identity.
  Both `! sudo ...` and real-terminal paths, cold credentials, cancellation, and
  startup/subagent reminders must be checked by the user after installation.

## Tests

```sh
python3 -m unittest discover tools/task/tests
```

Fixtures use isolated `/tmp` repositories, a stub Codex backend, and a deterministic
fixture `tools/validate-all.sh`. They stage an isolated Git index to test drift but
never commit, install hooks, use sudo, or invoke installation scripts. They cover
the v1 §7/v1.1 #13 negatives, approval races, actual-model failures, checker/input
drift, purpose coverage, reviewer identity, concurrency, kill/restart, loop stop,
wall timeout, record budgets, authority forgery, and ordinary wiki workflow.

Installation, manual smoke tests, and rollback: [install/README.md](install/README.md).
Codex command/config behavior was checked against the local CLI help and official
[configuration reference](https://learn.chatgpt.com/docs/config-file/config-reference)
and [non-interactive mode](https://learn.chatgpt.com/docs/non-interactive-mode).
