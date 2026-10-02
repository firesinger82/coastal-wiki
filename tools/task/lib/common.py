"""Strict decoding, containment and hashing adapted from resume-gate.

No resume-gate runtime/policy assumptions are imported.
"""
from __future__ import annotations

import contextlib
import fcntl
import fnmatch
from functools import lru_cache
import hashlib
import json
import math
import os
from pathlib import Path
import re
import tempfile
import time

HOME = Path(__file__).resolve().parents[1]
INSTALLED = Path('/usr/local/lib/coastal-task')
PURPOSE_ID = 'purpose'
PURPOSE_QUESTION = ('이 산출물이 function_question 에 답하는가? done_when 이 그 질문에 비해 '
                    '과하거나(전수·소진형) 모자라지 않은가?')
PLAN_QUESTION = '이 계획이 function_question 에 답하는가, 과한가?'
ZERO = '0' * 64


class GateError(ValueError):
    pass


def require(ok, message):
    if not ok:
        raise GateError(message)


def strict(raw):
    def pairs(items):
        result = {}
        for key, value in items:
            require(key not in result, f'duplicate JSON key: {key}')
            result[key] = value
        return result

    def constant(value):
        raise GateError(f'non-finite JSON: {value}')

    try:
        value = json.loads(raw, object_pairs_hook=pairs, parse_constant=constant)
        canonical(value)  # also rejects overflow (1e999) and invalid Unicode scalars
        return value
    except (UnicodeError, json.JSONDecodeError, TypeError, ValueError) as e:
        raise GateError(f'invalid JSON: {e}') from e


def canonical(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True,
                      separators=(',', ':'), allow_nan=False).encode('utf-8')


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def hash_obj(value):
    return digest(canonical(value))


def safe(path):
    """Reject symlinks in every existing path component, including the leaf."""
    path = Path(os.path.abspath(path))
    for part in [*reversed(path.parents), path]:
        require(not part.is_symlink(), f'symlink forbidden: {part}')
    return path


def relative(value, glob=False):
    require(isinstance(value, str) and value and '\\' not in value,
            'path must be a nonempty POSIX relative path')
    parts = value.split('/')
    require(not value.startswith('/') and all(p not in ('', '.', '..') for p in parts),
            f'path escape: {value}')
    if not glob:
        require(not any(c in value for c in '*?[]'), f'glob forbidden: {value}')
    return value


def contained(root, rel):
    relative(rel)
    root = safe(root)
    path = safe(root / rel)
    require(path.is_relative_to(root), f'path escape: {rel}')
    return path


def read(path):
    path = safe(path)
    if path.exists():
        require(path.is_file(), f'non-regular file: {path}')
    return path.read_bytes()


def load(path):
    return strict(read(path))


def file_hash(path):
    return digest(read(path))


def atomic(path, raw, mode=0o644):
    path = safe(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(prefix='.task-', dir=path.parent)
    try:
        with os.fdopen(fd, 'wb') as stream:
            stream.write(raw)
            stream.flush()
            os.fsync(stream.fileno())
            os.fchmod(stream.fileno(), mode)
        os.replace(tmp, path)
        dfd = os.open(path.parent, os.O_RDONLY | os.O_DIRECTORY)
        try:
            os.fsync(dfd)
        finally:
            os.close(dfd)
    finally:
        if os.path.exists(tmp):
            os.unlink(tmp)


def write_json(path, value, mode=0o644):
    atomic(path, canonical(value) + b'\n', mode)


def task_id(value):
    require(isinstance(value, str) and re.fullmatch(r'[a-z0-9_][a-z0-9_-]{0,63}', value)
            and value != 'none', 'invalid task_id')
    return value


def family(model):
    require(isinstance(model, str) and re.fullmatch(r'[a-zA-Z0-9][a-zA-Z0-9._-]*', model),
            'invalid model slug')
    if model.startswith(('gpt-', 'codex-')):
        return 'openai'
    if model.startswith(('claude-', 'opus', 'fable', 'sonnet')):
        return 'anthropic'
    if model.startswith('grok-'):
        return 'xai'
    raise GateError(f'unknown model family: {model}')


def schema(value, definition, label='$'):
    """Small fail-closed evaluator for the checked-in JSON Schema vocabulary."""
    known = {'$schema', 'title', 'description', 'type', 'properties', 'required',
             'additionalProperties', 'items', 'minItems', 'maxItems', 'minLength',
             'maxLength', 'pattern', 'enum', 'const', 'minimum', 'exclusiveMinimum',
             'maximum', 'oneOf', 'prefixItems'}
    require(set(definition) <= known, 'unsupported schema keyword')
    if 'oneOf' in definition:
        successes = 0
        for choice in definition['oneOf']:
            try:
                schema(value, choice, label)
                successes += 1
            except GateError:
                pass
        require(successes == 1, f'{label}: expected exactly one schema alternative')
    kind = definition.get('type')
    matches = {'object': isinstance(value, dict), 'array': isinstance(value, list),
               'string': isinstance(value, str), 'integer': type(value) is int,
               'number': type(value) in (int, float) and math.isfinite(value),
               'boolean': type(value) is bool, 'null': value is None}
    if kind:
        require(matches.get(kind, False), f'{label}: expected {kind}')
    if 'const' in definition:
        const = definition['const']
        require(value == const and (type(value) is bool if type(const) is bool else True),
                f'{label}: wrong constant')
    if 'enum' in definition:
        require(value in definition['enum'], f'{label}: unexpected value')
    for key, compare in [('minimum', lambda a,b: a >= b),
                         ('exclusiveMinimum', lambda a,b: a > b),
                         ('maximum', lambda a,b: a <= b)]:
        if key in definition:
            require(compare(value, definition[key]), f'{label}: {key}')
    if isinstance(value, str):
        require(len(value) >= definition.get('minLength', 0), f'{label}: empty string')
        require(len(value) <= definition.get('maxLength', 1000000), f'{label}: too long')
        if 'pattern' in definition:
            require(re.search(definition['pattern'], value) is not None, f'{label}: pattern')
    if isinstance(value, list):
        require(len(value) >= definition.get('minItems', 0), f'{label}: too few items')
        require(len(value) <= definition.get('maxItems', 1000000), f'{label}: too many items')
        for i, prefix in enumerate(definition.get('prefixItems', [])):
            if i < len(value):
                schema(value[i], prefix, f'{label}[{i}]')
        for i, item in enumerate(value):
            schema(item, definition.get('items', {}), f'{label}[{i}]')
    if isinstance(value, dict):
        require(set(definition.get('required', [])) <= set(value), f'{label}: missing fields')
        props = definition.get('properties', {})
        for key, item in value.items():
            if key in props:
                schema(item, props[key], f'{label}.{key}')
            else:
                extra = definition.get('additionalProperties', True)
                require(extra is not False, f'{label}: unexpected field {key}')
                if isinstance(extra, dict):
                    schema(item, extra, f'{label}.{key}')


def validate(value, name):
    schema(value, load(HOME / 'schemas' / f'{name}.schema.json'))
    return value


def contract(repo, ident):
    directory = contained(repo, 'tasks/' + task_id(ident))
    raw = read(directory / 'CONTRACT.json')
    c = validate(strict(raw), 'contract')
    require(c['task_id'] == ident, 'task directory/id mismatch')
    levels = c['build_plan_levels']
    values = levels['target'] + levels['not_performed']
    require(len(values) == len(set(values)) and set(values) ==
            {'문서 지원','코드 구현','실행 확인','수치 검증','물리 검증'},
            'build_plan_levels must partition all five levels without overlap')
    ids = [item['id'] for item in c['done_when']]
    require(len(ids) == len(set(ids)), 'duplicate done_when id')
    require(c['done_when'][0] == {'id': PURPOSE_ID, 'kind': 'review', 'spec': PURPOSE_QUESTION},
            'mandatory first purpose question missing')
    prefix = f'tasks/{ident}/outputs/'
    for pattern in c['allowed_outputs']:
        relative(pattern, glob=True)
        require(pattern.startswith(prefix), 'allowed_outputs outside task outputs')
    seen = set()
    for item in c['inputs']:
        relative(item['path'])
        require(item['path'] not in seen, 'duplicate input path')
        seen.add(item['path'])
    for item in c['done_when']:
        if item['kind'] == 'check':
            spec = item['spec']
            if spec['type'] in ('exists', 'sha256'):
                relative(spec['path'])
                require(spec['path'].startswith(prefix), 'check artifact outside outputs')
            else:
                relative(spec['path'])
                require(spec['path'] in seen, 'command checker must be a pinned input')
    return c, digest(raw), directory


def inputs(repo, c):
    result = {}
    for item in c['inputs']:
        actual = file_hash(contained(repo, item['path']))
        require(actual == item['sha256'], f'input drift: {item["path"]}')
        result[item['path']] = actual
    return result


def outputs(repo, c):
    directory = contained(repo, f'tasks/{c["task_id"]}/outputs')
    result = {}
    if directory.exists():
        for path in sorted(directory.rglob('*')):
            safe(path)
            if path.is_file():
                rel = path.relative_to(repo).as_posix()
                require(any(output_match(rel, p) for p in c['allowed_outputs']),
                        f'output outside allowed_outputs: {rel}')
                result[rel] = file_hash(path)
            else:
                require(path.is_dir(), 'non-regular output')
    return result


def output_match(path, pattern):
    """Full POSIX glob: '*' stays in a component; '**' spans zero or more components."""
    parts, glob = path.split('/'), pattern.split('/')
    @lru_cache(maxsize=None)
    def match(i, j):
        if j == len(glob):
            return i == len(parts)
        if glob[j] == '**':
            return match(i,j+1) or (i < len(parts) and match(i+1,j))
        return (i < len(parts) and fnmatch.fnmatchcase(parts[i],glob[j])
                and match(i+1,j+1))
    return match(0,0)


def test_root():
    value = os.environ.get('COASTAL_TASK_TEST_ROOT')
    if value is None:
        return None
    path = safe(value)
    require(path.is_relative_to(Path('/tmp')) and path != Path('/tmp'),
            'test root must be a private directory under /tmp')
    require(path.is_dir() and path.stat().st_uid == os.geteuid(), 'unsafe test root owner')
    require(path.stat().st_mode & 0o077 == 0, 'test root must have mode 0700')
    return path


def approvals_dir():
    root = test_root()
    override = os.environ.get('COASTAL_TASK_APPROVALS_DIR')
    if root:
        path = safe(override) if override else root / 'approvals'
        require(path.is_relative_to(root) and path != root, 'forged approvals path')
    else:
        require(override is None, 'approval directory override requires test mode')
        path = safe('/var/lib/coastal-task/approvals')
        for entry in (path.parent, path):
            if entry.exists():
                require(entry.stat().st_uid == 0 and entry.stat().st_mode & 0o022 == 0,
                        'approval directory must be root-owned and not writable by group/other')
    return path


def approval(c, sha):
    root = approvals_dir()
    path = safe(root / f'{c["task_id"]}.{c["revision"]}.json')
    a = validate(load(path), 'approval')
    if test_root() is None:
        require(path.stat().st_uid == 0 and path.stat().st_mode & 0o022 == 0,
                'approval file must be root-owned')
    require(a['task_id'] == c['task_id'] and a['revision'] == c['revision']
            and a['contract_sha256'] == sha and a['snapshot_sha256'] == sha,
            'approval missing or contract changed; increase revision and reapprove')
    snapshot = safe(root / f'{c["task_id"]}.{c["revision"]}.snapshot.json')
    require(file_hash(snapshot) == sha, 'approval snapshot drift')
    return a, file_hash(path)


def state(repo):
    return contained(repo, 'tools/task/state')


@contextlib.contextmanager
def locked(repo, ident):
    if ident != 'none':
        task_id(ident)
    directory = safe(state(repo) / 'locks')
    directory.mkdir(parents=True, exist_ok=True)
    path = safe(directory / f'{ident}.lock')
    fd = os.open(path, os.O_CREAT | os.O_RDWR | os.O_NOFOLLOW, 0o600)
    try:
        fcntl.flock(fd, fcntl.LOCK_EX)
        yield
    finally:
        os.close(fd)


def ledger(path):
    if not path.exists():
        safe(path)
        return []
    raw = read(path)
    require(not raw or raw.endswith(b'\n'), 'truncated ledger')
    entries = []
    previous = ZERO
    starts = {}
    ends = set()
    for line in raw.splitlines():
        entry = validate(strict(line), 'run')
        payload = {k: v for k,v in entry.items() if k != 'entry_sha256'}
        require(entry['prev_sha256'] == previous and hash_obj(payload) == entry['entry_sha256'],
                'runs.jsonl hash chain corruption')
        ident = entry['run_id']
        if entry['event'] == 'reserved':
            require(ident not in starts, 'duplicate run reservation')
            starts[ident] = entry
        else:
            require(ident in starts and ident not in ends, 'invalid run completion')
            require(entry['reservation_sha256'] == starts[ident]['entry_sha256'],
                    'run completion binding mismatch')
            ends.add(ident)
        entries.append(entry)
        previous = entry['entry_sha256']
    return entries


def append(path, item):
    entries = ledger(path)
    item = dict(item, prev_sha256=entries[-1]['entry_sha256'] if entries else ZERO)
    item['entry_sha256'] = hash_obj(item)
    validate(item, 'run')
    path = safe(path)
    fd = os.open(path, os.O_CREAT | os.O_WRONLY | os.O_APPEND | os.O_NOFOLLOW, 0o644)
    raw = canonical(item) + b'\n'
    with os.fdopen(fd, 'wb') as stream:
        stream.write(raw)
        stream.flush()
        os.fsync(stream.fileno())
    return item


def policy_hash(repo, c):
    """Bind validators, harness code and schemas; no timestamp-dependent fields."""
    files = set()
    for folder in ('lib', 'schemas', 'bin'):
        files.update(p for p in (HOME / folder).rglob('*')
                     if p.is_file() and '__pycache__' not in p.parts and p.suffix != '.pyc')
    versions = {str(p.relative_to(HOME)): file_hash(p) for p in sorted(files)}
    # validate-all's seven wrappers load other validate-* Python/shell helpers.
    for p in sorted((repo / 'tools').glob('validate-*')):
        if p.is_file():
            versions['repo/' + p.relative_to(repo).as_posix()] = file_hash(p)
    for item in c['done_when']:
        if item['kind'] == 'check' and item['spec']['type'] == 'command':
            rel = item['spec']['path']
            versions['repo/' + rel] = file_hash(contained(repo, rel))
    require((repo / 'tools/validate-all.sh').is_file(), 'validate-all.sh missing')
    return hash_obj(versions)


def binding(repo, c, sha):
    return {'task_id': c['task_id'], 'revision': c['revision'], 'contract_sha256': sha,
            'input_sha256s': inputs(repo, c), 'checker_sha256': policy_hash(repo, c),
            'output_sha256s': outputs(repo, c)}


def active(repo, c, sha):
    write_json(state(repo) / 'ACTIVE', {'task_id': c['task_id'], 'revision': c['revision'],
                                     'contract_sha256': sha})


def now():
    return time.time()
