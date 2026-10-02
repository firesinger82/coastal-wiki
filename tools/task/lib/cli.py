"""Command interfaces. Installed approval entry point imports only this protected copy."""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import difflib
import os
from pathlib import Path
import sys
import tempfile

from .common import (GateError, HOME, INSTALLED, PURPOSE_ID, PURPOSE_QUESTION, active,
                     approval, approvals_dir, atomic, binding, canonical, contract,
                     digest, file_hash, hash_obj, ledger, load, locked, outputs, read,
                     require, safe, state, strict, task_id, test_root, validate, write_json)


def repo_root(value=None):
    if value:
        return safe(value)
    for path in (Path.cwd(), *Path.cwd().parents):
        if (path / '.git').exists():
            return safe(path)
    raise GateError('repository not found; pass --repo')


def approve(repo, ident):
    test = test_root()
    if test is None:
        require(os.geteuid() == 0, 'approve requires effective UID 0 (sudo)')
        require(HOME == INSTALLED, 'approve must run from /usr/local/lib/coastal-task installed copy')
        for path in [HOME, *HOME.rglob('*')]:
            safe(path)
            st = path.stat()
            require(st.st_uid == 0 and st.st_mode & 0o022 == 0, 'installed approval code must be protected')
    c, initial_sha, directory = contract(repo, ident)
    destination = approvals_dir()
    destination.mkdir(parents=True, exist_ok=True, mode=0o755)
    with locked_approval(destination, ident):
        previous = sorted(destination.glob(f'{ident}.*.json'))
        previous = [p for p in previous if not p.name.endswith('.snapshot.json')]
        revisions = [validate(load(p), 'approval')['revision'] for p in previous]
        require(not revisions or c['revision'] > max(revisions),
                'revision must exceed every preserved approval')
        # One private byte snapshot is the source of display and both approval hashes.
        with tempfile.TemporaryDirectory(prefix='.snapshot-', dir=destination) as tmp:
            snap = Path(tmp) / 'CONTRACT.json'
            raw = read(directory / 'CONTRACT.json')
            require(digest(raw) == initial_sha, 'contract changed before snapshot; cancelled')
            atomic(snap, raw, 0o400)
            c = validate(strict(read(snap)), 'contract')
            print(f'function: {c["function"]}\nfunction_question: {c["function_question"]}')
            print(f'budget: {canonical(c["budget"]).decode()}\nout_of_scope: {canonical(c["out_of_scope"]).decode()}')
            print(f'task: {ident} revision: {c["revision"]}')
            if revisions:
                last = destination / f'{ident}.{max(revisions)}.snapshot.json'
                print('Changes from previous approved revision:')
                print(''.join(difflib.unified_diff(read(last).decode().splitlines(True),
                                                 raw.decode().splitlines(True),
                                                 fromfile=f'revision {max(revisions)}',
                                                 tofile=f'revision {c["revision"]}')) or '(none)')
            else:
                print('Changes: first approval')
            print('Approval snapshot:')
            print(read(snap).decode())
            sha = file_hash(snap)
            print(f'snapshot_sha256: {sha}', flush=True)
            typed = input('Type the exact function name to approve (EOF cancels): ')
            require(typed == c['function'], 'function name mismatch; cancelled')
            require(file_hash(directory / 'CONTRACT.json') == sha,
                    'contract changed after display; cancelled')
            value = validate({'task_id':ident,'revision':c['revision'],'contract_sha256':sha,
                              'snapshot_sha256':sha,'approved_at':datetime.now(timezone.utc).isoformat(),
                              'approver':os.environ.get('SUDO_USER') or ('test-user' if test else 'root')}, 'approval')
            base = destination / f'{ident}.{c["revision"]}'
            require(not Path(str(base)+'.json').exists(), 'approval already exists')
            atomic(Path(str(base)+'.snapshot.json'), read(snap), 0o644)
            write_json(Path(str(base)+'.json'), value)
            print(f'Approved {ident} revision {c["revision"]}: {sha}')


def locked_approval(directory, ident):
    import contextlib
    import fcntl
    @contextlib.contextmanager
    def manager():
        fd = os.open(safe(directory / f'.{ident}.lock'), os.O_CREAT|os.O_RDWR|os.O_NOFOLLOW, 0o600)
        try:
            fcntl.flock(fd, fcntl.LOCK_EX)
            yield
        finally:
            os.close(fd)
    return manager()


def template(ident, model, function, question):
    return {'task_id':ident,'revision':1,'model':model,'function':function,
            'function_question':question,
            'build_plan_levels':{'target':['문서 지원'],'not_performed':['코드 구현','실행 확인','수치 검증','물리 검증']},
            'inputs':[],'allowed_outputs':[f'tasks/{ident}/outputs/*'],
            'constraints':['Write only task outputs; models/ stays read-only.'],
            'done_when':[{'id':PURPOSE_ID,'kind':'review','spec':PURPOSE_QUESTION},
                         {'id':'artifact','kind':'check','spec':{'type':'exists','path':f'tasks/{ident}/outputs/result.txt'}}],
            'budget':{'codex_runs':4,'max_records':10,'wall_hours':1},
            'verifier':{'family':'anthropic','second_for_models':True},
            'out_of_scope':['Unrelated dependencies and exhaustive inventory']}


def new_task(repo, args):
    from .common import contained
    ident = task_id(args.task)
    directory = contained(repo, 'tasks/' + ident)
    if args.revise:
        with locked(repo, ident):
            from .runner import recover
            recover(directory / 'runs.jsonl')  # refuses live runs; closes dead reservations
            c, sha, _ = contract(repo, ident)
            # Preserve the exact preceding draft/approved bytes; never rewrite runs/verdict history.
            history = directory / 'history' / f'{c["revision"]}.CONTRACT.json'
            require(not history.exists(), 'revision already archived')
            atomic(history, read(directory / 'CONTRACT.json'))
            c['revision'] += 1
            write_json(directory / 'CONTRACT.json', c)
            pointer = state(repo) / 'ACTIVE'
            if pointer.exists() and load(pointer).get('task_id') == ident:
                pointer.unlink()  # superseded; explicit fresh approval/activation required
    else:
        require(args.model and args.function and args.question, '--model, --function and --question required')
        require(not directory.exists(), 'task already exists')
        directory.mkdir(parents=True)
        c = template(ident, args.model, args.function, args.question)
        write_json(directory / 'CONTRACT.json', c)
        contract(repo, ident)
    print(f'draft: {ident} revision {c["revision"]}; edit CONTRACT.json, then approve')


def summary(repo, ident=None):
    pointer = state(repo) / 'ACTIVE'
    if ident is None:
        if not pointer.exists():
            safe(pointer)
            return {'status':'none','message':'활성 작업 없음 — 모델 분석 대량 작업 금지'}
        pin = load(pointer)
        require(isinstance(pin,dict) and set(pin)=={'task_id','revision','contract_sha256'}, 'ACTIVE corrupt')
        ident = pin['task_id']
    else:
        pin = None
    c, sha, directory = contract(repo, ident)
    if pin:
        require(pin == {'task_id':ident,'revision':c['revision'],'contract_sha256':sha},
                'ACTIVE revision/hash mismatch (superseded or corrupt)')
    entries = ledger(directory / 'runs.jsonl')
    reservations = [e for e in entries if e['event']=='reserved' and e['binding']['revision']==c['revision']]
    ends = {e['run_id'] for e in entries if e['event']=='finished'}
    lifecycle = 'draft'
    try:
        approval(c, sha)
        lifecycle = 'approved'
    except FileNotFoundError:
        pass
    if reservations:
        lifecycle = 'incomplete'
    if any(e['run_id'] not in ends for e in reservations):
        from .runner import living
        lifecycle = ('running' if any(living(e) for e in reservations if e['run_id'] not in ends)
                     else 'incomplete')
    unmet = [i['id'] for i in c['done_when']]
    status_path = directory / 'STATUS.json'
    if status_path.exists():
        status = validate(load(status_path), 'status')
        receipt = validate(load(directory / 'RECEIPT.json'), 'receipt')
        from .receipt import status_value
        require(status == status_value(receipt), 'STATUS/RECEIPT corrupt')
        current = binding(repo, c, sha)
        fresh = (all(receipt[k]==v for k,v in current.items())
                 and receipt['runs_tail_sha256']==(entries[-1]['entry_sha256'] if entries else '0'*64))
        if fresh and lifecycle != 'running':
            require(status['status']==receipt['status'] and status['reasons']==receipt['reasons'],
                    'STATUS/RECEIPT mismatch')
            lifecycle = status['status']
            if lifecycle=='complete':
                unmet = []
            else:
                passed = {k for k,v in receipt['checks'].items() if v['verdict']=='PASS'}
                from .review import models_outputs
                need = 2 if models_outputs(repo, c, current['output_sha256s']) else 1
                if len(receipt['reviews']) >= need:
                    review_ids = {i['id'] for i in c['done_when'] if i['kind']=='review'}
                    passed.update(ident for ident in review_ids if all(
                        any(q['id']==ident and q['verdict']=='PASS' for q in review['questions'])
                        for review in receipt['reviews']))
                unmet = [i for i in unmet if i not in passed]
    return {'task_id':ident,'revision':c['revision'],'function':c['function'],
            'function_question':c['function_question'],'status':lifecycle,'unmet':unmet,
            'used':len(reservations),'limit':c['budget']['codex_runs']}


def main(command):
    parser = argparse.ArgumentParser(prog=command)
    parser.add_argument('--repo')
    if command == 'codex-run':
        parser.add_argument('--task', required=True)
        parser.add_argument('--role', choices=['worker','verifier'])
        parser.add_argument('--model', required=True)
        parser.add_argument('--write', action='store_true')
        parser.add_argument('--purpose-review', action='store_true')
        parser.add_argument('--purpose')
        parser.add_argument('prompt', nargs='?')
    elif command == 'status':
        parser.add_argument('task', nargs='?')
        parser.add_argument('--activate')
        parser.add_argument('--clear', action='store_true')
        parser.add_argument('--json', action='store_true')
    else:
        parser.add_argument('task')
        if command == 'receipt':
            parser.add_argument('--verify', action='store_true')
            parser.add_argument('--staged', action='store_true')
        if command == 'new-task':
            parser.add_argument('--revise', action='store_true')
            parser.add_argument('--model')
            parser.add_argument('--function')
            parser.add_argument('--question')
    args = parser.parse_args()
    try:
        repo = repo_root(args.repo)
        if command == 'approve':
            approve(repo, task_id(args.task))
        elif command == 'new-task':
            new_task(repo, args)
        elif command == 'codex-run':
            from .runner import run
            return run(repo, args)
        elif command == 'receipt':
            from .receipt import generate
            value = generate(repo, args.task, args.verify, args.staged)
            print(canonical(value).decode())
            return 0 if value['status']=='complete' else 1
        elif command == 'status':
            if args.clear:
                pointer = safe(state(repo) / 'ACTIVE')
                pointer.unlink(missing_ok=True)
            if args.activate:
                c, sha, _ = contract(repo, args.activate)
                approval(c, sha)
                active(repo, c, sha)
            value = summary(repo, args.task)
            print(canonical(value).decode() if args.json else format_summary(value))
        return 0
    except (GateError, OSError, EOFError, UnicodeError) as e:
        print(f'{command}: {e}', file=sys.stderr)
        return 2


def format_summary(value):
    if value['status']=='none':
        return value['message']
    return (f'{value["task_id"]} r{value["revision"]}: {value["status"]}\n'
            f'질문: {value["function_question"]}\n'
            f'미충족: {", ".join(value["unmet"]) or "없음"}\n'
            f'예산: {value["used"]}/{value["limit"]} codex_runs')
