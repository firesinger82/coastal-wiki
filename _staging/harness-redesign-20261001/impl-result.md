Implemented harness v1.1 within the allowed scope. All 43 offline tests pass.

Files added/changed:

- `tools/task/bin/{new-task,approve,codex-run,receipt,status}`
- `tools/task/hooks/{pretooluse.py,goal-pin.py}`
- `tools/task/lib/{__init__,cli,common,receipt,review,runner}.py`
- `tools/task/schemas/{contract,approval,run,verdict,receipt,status,review-response}.schema.json`
- `tools/task/tests/{test_harness.py,stub_codex.py}`
- `tools/task/install/{install.sh,harden-sudo.sh,remove-resume-gate.sh,README.md}`
- [tools/task/README.md](/home/firesinger/coastal-wiki/tools/task/README.md)
- `tasks/_example/{CONTRACT.json,README.md}`
- `.claude/settings.json`, `.gitignore`

Test command and full summary:

```text
$ python3 -m unittest discover tools/task/tests
...........................................
----------------------------------------------------------------------
Ran 43 tests in 107.552s

OK
```

Conservative interpretations are recorded under README “Decisions.” Git-hook integration remains an opt-in `receipt --staged` check because modifying Git hooks was prohibited. Live Codex, interactive sudo, and Claude lifecycle smoke tests remain manual. No sudo, installer execution, commits, or out-of-scope repository changes were performed.

To install, inspect the dry-run inventory, then run:

```sh
tools/task/install/install.sh
sudo tools/task/install/install.sh --apply
```

Restart Claude sessions and follow [the installation smoke tests](/home/firesinger/coastal-wiki/tools/task/install/README.md). Production approval uses `/usr/local/lib/coastal-task/bin/approve`.

Codex session ID: 01a0fa06-63f7-7d80-ac2e-eecda4bcaa7b
Resume in Codex: codex resume 01a0fa06-63f7-7d80-ac2e-eecda4bcaa7b
