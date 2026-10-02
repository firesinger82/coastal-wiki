"""Deterministic completion, with a side-effect-free verification entry point."""
import os
from pathlib import Path
import subprocess

from .common import (GateError, ZERO, approval, binding, contained, contract, digest,
                     file_hash, hash_obj, inputs, ledger, load, locked, outputs, read,
                     require, validate, write_json)
from .review import paused, purpose_passed, review_summary


def execute(repo, argv, timeout):
    try:
        p = subprocess.run(argv, cwd=repo, stdin=subprocess.DEVNULL,
                           stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=timeout)
        code, stdout, stderr = p.returncode, p.stdout, p.stderr
    except subprocess.TimeoutExpired as e:
        code, stdout, stderr = 124, e.stdout or b'', e.stderr or b''
    except OSError as e:
        code, stdout, stderr = 127, b'', str(e).encode()
    return {'verdict': 'PASS' if code == 0 else 'FAIL', 'exit': code,
            'stdout_sha256': digest(stdout), 'stderr_sha256': digest(stderr)}


def check(repo, spec):
    if spec['type'] == 'command':
        return execute(repo, [str(contained(repo, spec['path'])), *spec['args']],
                       spec['timeout_seconds'])
    path = contained(repo, spec['path'])
    passed = path.is_file()
    if passed and spec['type'] == 'sha256':
        passed = file_hash(path) == spec['sha256']
    return {'verdict': 'PASS' if passed else 'FAIL', 'exit': 0 if passed else 1,
            'stdout_sha256': digest(b''), 'stderr_sha256': digest(b'')}


def record_count(repo, hashes):
    """JSON arrays count elements; JSONL counts objects; other files count nonempty lines."""
    total = 0
    for rel in hashes:
        raw = read(contained(repo, rel))
        if rel.endswith('.json'):
            from .common import strict
            value = strict(raw)
            total += len(value) if isinstance(value, list) else 1
        elif rel.endswith('.jsonl'):
            from .common import strict
            for line in raw.splitlines():
                if line.strip():
                    strict(line)
                    total += 1
        else:
            total += sum(bool(line.strip()) for line in raw.splitlines())
    return total


def calculate(repo, ident):
    c, sha, directory = contract(repo, ident)
    _, approval_sha = approval(c, sha)
    before = binding(repo, c, sha)
    entries = ledger(directory / 'runs.jsonl')
    reservations = [e for e in entries if e['event'] == 'reserved']
    finished = {e['run_id'] for e in entries if e['event'] == 'finished'}
    reasons = []
    if any(e['run_id'] not in finished for e in reservations):
        reasons.append('unfinished/interrupted reservation remains')
    current_runs = [e for e in reservations if e['binding']['revision'] == c['revision']]
    workers = [e for e in current_runs if e['role'] == 'worker']
    if not workers:
        reasons.append('no worker execution')
    if not purpose_passed(repo, c, sha, entries):
        reasons.append('purpose-review missing or not PASS')
    if workers:
        first_index = entries.index(workers[0])
        if not purpose_passed(repo, c, sha, entries[:first_index]):
            reasons.append('purpose-review did not precede first worker')
    checks = {i['id']: check(repo, i['spec']) for i in c['done_when'] if i['kind'] == 'check'}
    reasons.extend(f'check {ident}: FAIL' for ident,result in checks.items()
                   if result['verdict'] != 'PASS')
    validator = execute(repo, ['bash', str(contained(repo, 'tools/validate-all.sh'))], 300)
    if validator['verdict'] != 'PASS':
        reasons.append('validate-all.sh: FAIL')
    hashes = before['output_sha256s']
    reviews, review_reasons = review_summary(repo, c, sha, entries, hashes)
    reasons.extend(review_reasons)
    count = record_count(repo, hashes)
    if 'max_records' in c['budget'] and count > c['budget']['max_records']:
        reasons.append('max_records exceeded')
    if len(current_runs) > c['budget']['codex_runs']:
        reasons.append('codex_runs exceeded')
    if current_runs:
        end_times = [e['ended'] for e in entries if e['event'] == 'finished'
                     and e['run_id'] in {r['run_id'] for r in current_runs}]
        if end_times and max(end_times) - current_runs[0]['started'] > c['budget']['wall_hours'] * 3600:
            reasons.append('wall_hours exceeded')
    stop = paused(repo, c, sha, entries)
    if stop:
        reasons.append(stop)
    # Check programs must not swap the candidate, approval, inputs, policy, or ledger.
    require(binding(repo, c, sha) == before and contract(repo, ident)[1] == sha
            and approval(c, sha)[1] == approval_sha
            and ledger(directory / 'runs.jsonl') == entries, 'snapshot changed during receipt')
    value = {**before, 'approval_sha256': approval_sha,
             'runs_tail_sha256': entries[-1]['entry_sha256'] if entries else ZERO,
             'checks': checks, 'validate_all': validator, 'reviews': reviews,
             'build_plan_levels': c['build_plan_levels'], 'records': count,
             'budget_used': len(current_runs),
             'status': 'paused' if stop else ('incomplete' if reasons else 'complete'),
             'reasons': sorted(set(reasons))}
    return validate(value, 'receipt'), directory


def status_value(receipt):
    return validate({k:receipt[k] for k in ('task_id','revision','contract_sha256','status','reasons')}
                    | {'receipt_sha256':hash_obj(receipt)}, 'status')


def generate(repo, ident, verify=False, staged=False):
    with locked(repo, ident):
        value, directory = calculate(repo, ident)
        status = status_value(value)
        if verify or staged:
            require(load(directory / 'RECEIPT.json') == value, 'forged or stale RECEIPT.json')
            require(load(directory / 'STATUS.json') == status, 'forged or stale STATUS.json')
            if staged:
                verify_index(repo, directory, value)
        else:
            write_json(directory / 'RECEIPT.json', value)
            write_json(directory / 'STATUS.json', status)
        return value


def verify_index(repo, directory, value):
    """Require the index to contain the whole exact candidate and provenance snapshot."""
    paths = {directory / x for x in ('CONTRACT.json','RECEIPT.json','STATUS.json','runs.jsonl')}
    paths.update(contained(repo, p) for p in value['output_sha256s'])
    paths.update(contained(repo, p) for p in value['input_sha256s'])
    paths.update(directory / 'verdicts' / (v['run_id'] + '.json') for v in value['reviews'])
    # Include purpose verdicts too, and require no staged/worktree task-tree additions/deletions.
    paths.update((directory / 'verdicts').glob('*.json'))
    prefix = directory.relative_to(repo).as_posix() + '/'
    indexed = subprocess.run(['git','ls-files','-z','--',prefix], cwd=repo,
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
    staged_paths = {os.fsdecode(p) for p in indexed.stdout.split(b'\0') if p}
    working_paths = {p.relative_to(repo).as_posix() for p in directory.rglob('*') if p.is_file()}
    require(staged_paths == working_paths, 'staged/worktree task tree mismatch')
    paths.update(contained(repo, p) for p in working_paths)
    # The index must use the same validator/checker/policy bytes, not just the outputs.
    paths.update(p for p in (repo / 'tools').glob('validate-*') if p.is_file())
    from .common import HOME
    if HOME.is_relative_to(repo):
        for folder in ('lib','schemas','bin'):
            paths.update(p for p in (HOME / folder).rglob('*') if p.is_file()
                         and '__pycache__' not in p.parts and p.suffix != '.pyc')
    for path in paths:
        rel = path.relative_to(repo).as_posix()
        p = subprocess.run(['git','show', ':' + rel], cwd=repo,
                           stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        require(p.returncode == 0 and p.stdout == read(path), f'staged/worktree mismatch: {rel}')
