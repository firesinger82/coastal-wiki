#!/usr/bin/python3 -I
"""Claude command hook: explicit JSON denial; ordinary wiki tools are unaffected."""
import json
import os
from pathlib import Path
import shlex
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from lib.common import GateError, approvals_dir, load, strict
from lib.cli import repo_root


def direct(command):
    try:
        lexer = shlex.shlex(command, posix=True, punctuation_chars=';&|()\n')
        lexer.whitespace_split = True
        tokens = list(lexer)
    except ValueError:
        # A malformed shell string containing a direct executable must not fail open.
        return 'codex' in command
    segments = [[]]
    for token in tokens:
        if token and all(c in ';&|()\n' for c in token):
            segments.append([])
        else:
            segments[-1].append(token)
    for segment in segments:
        # Codex companion runs as `node .../codex-companion.mjs ...`: match only when a JS runtime
        # executes that script (first non-option argument), not when the name merely appears in text.
        runtimes = ('node', 'nodejs', 'bun', 'deno')
        for k, tok in enumerate(segment):
            if Path(tok).name in runtimes:
                script = next((x for x in segment[k + 1:] if not x.startswith('-')), '')
                if Path(script).name in ('codex-companion.mjs', 'codex-companion.js', 'codex-companion'):
                    return True
                break
            if '=' in tok and not tok.startswith('/'):
                continue
            if Path(tok).name in ('env', 'sudo', 'command', 'exec', 'nohup', 'time', 'timeout', 'nice'):
                continue
            break
        i = 0
        while i < len(segment):
            token = segment[i]
            name = Path(token).name
            if name in ('codex','codex-companion'):
                return True
            if '=' in token and not token.startswith('/'):
                i += 1
                continue
            if name in ('env','sudo','command','exec','nohup','time','timeout','nice'):
                # Wrapper flags have values (-u root, -n 10, timeout 30s).
                # Search the wrapped command conservatively; never let a wrapper hide Codex.
                if any(Path(x).name in ('codex','codex-companion') for x in segment[i+1:]):
                    return True
                i += 1
                while i < len(segment) and (segment[i].startswith('-') or
                                           segment[i].isdigit()):
                    i += 1
                continue
            if name in ('bash','sh','zsh','dash'):
                for index in range(i+1, len(segment)-1):
                    option = segment[index]
                    if (option == '--command' or (option.startswith('-') and
                                                  not option.startswith('--') and 'c' in option[1:])):
                        if direct(segment[index+1]):
                            return True
            # Shell command substitutions execute independently, even in echo arguments.
            for arg in segment[i+1:]:
                if '$(' in arg or '`' in arg:
                    if 'codex ' in arg or 'codex-companion' in arg:
                        return True
            break
    return False


def protected(repo, value):
    path = Path(value)
    if not path.is_absolute():
        path = repo / path
    lexical = Path(os.path.abspath(path))
    candidates = [lexical, lexical.resolve()]
    for path in candidates:
        try:
            parts = path.relative_to(repo).parts
        except ValueError:
            continue
        if len(parts) < 3 or parts[0] != 'tasks':
            continue
        if parts[2] in ('RECEIPT.json','STATUS.json','runs.jsonl','verdicts'):
            return True
        if parts[2] == 'CONTRACT.json':
            root = approvals_dir()
            approvals = list(root.glob(parts[1]+'.*.json'))
            if not approvals:
                return False
            # A legitimate new-task --revise draft remains editable. Hash drift of an
            # already-approved revision does not remove its protection.
            try:
                c = load(path)
                if (isinstance(c,dict) and c.get('task_id')==parts[1]
                        and type(c.get('revision')) is int and c['revision'] > 0):
                    return (root / f'{parts[1]}.{c["revision"]}.json').exists()
            except (GateError, OSError):
                pass
            return True
    return False


def deny(reason):
    print(json.dumps({'hookSpecificOutput':{'hookEventName':'PreToolUse',
                     'permissionDecision':'deny','permissionDecisionReason':reason}}, ensure_ascii=False))


def main():
    try:
        payload = strict(sys.stdin.buffer.read())
        if not isinstance(payload,dict) or not isinstance(payload.get('tool_name'),str):
            raise GateError('malformed hook payload')
        tool = payload['tool_name']
        data = payload.get('tool_input')
        if not isinstance(data,dict):
            raise GateError('malformed tool_input')
        if tool == 'Bash':
            command = data.get('command')
            if not isinstance(command,str):
                raise GateError('missing Bash command')
            if direct(command):
                deny('Direct Codex invocation denied. Use tools/task/bin/codex-run; '
                     'for ordinary work use --task none --purpose <reason> --model <slug> <prompt-file>.')
        elif tool in ('Write','Edit','MultiEdit','NotebookEdit'):
            value = data.get('file_path') or data.get('notebook_path')
            if not isinstance(value,str):
                raise GateError('missing edit path')
            repo = repo_root(os.environ.get('CLAUDE_PROJECT_DIR') or payload.get('cwd'))
            if protected(repo, value):
                deny('Task authority/history files require new-task --revise or receipt/codex-run. '
                     'Direct editing denied.')
    except (GateError, OSError, UnicodeError, TypeError) as e:
        deny(f'Task hook payload/state error: {e}; repair hook/state and retry.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
