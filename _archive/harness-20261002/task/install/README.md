# Human installation and cutover

No scripts in this directory were executed during implementation/tests. All default
to dry-run and change system paths only with `--apply` as root. Review source and the
dry-run inventory first. Stop active agent writers and relevant cron jobs before
cutover; L4 cron work-tree cleanup changes are a separate task.

From the repository:

```sh
tools/task/install/install.sh
sudo tools/task/install/install.sh --apply
```

This one authenticated process preserves a tarball in `/var/backups/coastal-task/`,
copies bin/lib/schemas/hooks/install/README into root-owned
`/usr/local/lib/coastal-task`, creates the root-owned mode-0755 approvals directory,
applies `Defaults timestamp_timeout=0` with `visudo -cf` and `visudo -c`, then backs up
and removes exactly the legacy artifacts listed below. It never modifies global
Claude settings, Git hooks, repository sources, or domain documents. Existing
approvals and legacy installed artifacts are backed up before cutover.

Standalone inventory/apply (normally use the combined installer):

```sh
tools/task/install/harden-sudo.sh
tools/task/install/remove-resume-gate.sh
# Only if needed separately, after inspecting each dry-run:
sudo tools/task/install/harden-sudo.sh --apply
sudo tools/task/install/remove-resume-gate.sh --apply
```

Legacy removal lists these exact paths, including absence, and the specific existing
`resume-*` files; it does not glob other backups or remove the whole agents directory:

- `/etc/claude-code/managed-mcp.json`
- `/etc/claude-code/managed-settings.d/50-coastal-resume.json.bak`
- `/etc/claude-code/.claude/agents/resume-*` files
- `/opt/coastal-resume`

Inspect `sudo -l` yourself for NOPASSWD rules. Timeout hardening cannot revoke
NOPASSWD, and WSL root launch paths remain outside threat model A.

After installation, restart Claude sessions (including subagents) so the NEW project
`.claude/settings.json` hooks load. `.claude/settings.local.json` and
`~/.claude/settings.json` are untouched. Confirm hook matchers/commands appear in
Claude's hook inspection UI. Existing sessions can retain older configuration.

## Required manual smoke tests

Use a fresh bounded task, not the frozen model audit. Pin the intended sources and
checkers. Run approval from the installed copy with absolute `--repo`:

```sh
sudo -k
sudo /usr/local/lib/coastal-task/bin/approve --repo "$PWD" <task_id>
```

Confirm password input, contract/revision/diff/hash display, exact-function-name
input, wrong-name/EOF cancellation, and subsequent reapproval after revision. Repeat
the same command using Claude shell mode:

```text
! sudo /usr/local/lib/coastal-task/bin/approve --repo /absolute/coastal-wiki <task_id>
```

Use separate draft tasks/revisions for each approval. If shell mode cannot handle
either interactive prompt, use the real terminal; do not disable the approval gate.
The automated tests cover typed input and cancellation, but cannot prove cold sudo
authentication or the installed Claude terminal interaction.

Then activate the task, check startup/resume/compaction and SubagentStart reminders
(3–6 lines) and prompt reminders (one line). Check direct `codex exec`, bare `codex`,
`codex-companion`, and editing authority files return JSON denial; an ordinary wiki
note edit, validation, and draft commit must still work. Check malformed hook input
is denied. A missing executable/timeout is a Claude runtime limitation, not a trusted
fail-closed boundary; do not rely solely on hooks.

Execute purpose-review using the configured independent model family, then one small
worker and output review. Inspect actual-model/session identity and verify an
unsupported/fallback slug is rejected. Verify a live `--write` backend cannot write
outside the task outputs or temporary roots. Run receipt and inspect STATUS; verify
an incomplete receipt when criteria are missing. Replace a candidate after PASS and
confirm receipt rejects the stale review. Inspect the exact staged snapshot with
`receipt --staged` before any human-approved model application.

## Rollback

Remove only the four task hook event entries in project `.claude/settings.json`,
remove the protected `/usr/local/lib/coastal-task` installation as the user with sudo,
and restart sessions. Preserve task history and approvals. Use the printed backup
tarball to recover records as needed. Do **not** restore the old global resume locks.
If cutover fails midway, inspect the backup/inventory and finish or roll back before
restarting writers; this script does not claim a transaction across system services.
