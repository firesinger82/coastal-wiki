"""Review provenance, freshness, independence, and repeated-failure detection."""
from .common import (GateError, PURPOSE_ID, approval, binding, contained, file_hash,
                     load, require, validate)


def verified_reviews(repo, c, sha, entries, phase):
    starts = {e['run_id']: e for e in entries if e['event'] == 'reserved'}
    current = binding(repo, c, sha)
    latest = {}
    reasons = []
    for end in entries:
        if end['event'] != 'finished':
            continue
        start = starts[end['run_id']]
        if start['role'] != 'verifier' or start['phase'] != phase:
            continue
        if start['binding']['revision'] != c['revision']:
            continue
        latest[start['model']] = (start, end)
    result = []
    for model, (start, end) in sorted(latest.items()):
        if end['exit'] != 0 or end['error'] or not end['verdict_path']:
            reasons.append(f'{phase} verifier failed: {model}')
            continue
        try:
            path = contained(repo, end['verdict_path'])
            require(file_hash(path) == end['verdict_sha256'], 'verdict file hash mismatch')
            verdict = validate(load(path), 'verdict')
            require(verdict['run_id'] == end['run_id'] and verdict['actual_model'] == model
                    == end['actual_model'] and verdict['phase'] == phase,
                    'verdict run/model mismatch')
            expected = dict(current)
            if phase == 'purpose':
                # A plan review survives later worker outputs, but never plan/input/policy drift.
                expected['output_sha256s'] = start['binding']['output_sha256s']
            require(start['binding'] == expected, 'stale verifier binding')
            require(all(verdict[key] == value for key,value in expected.items()),
                    'stale verdict after output/input/checker swap')
            require(end['output_sha256s'] == expected['output_sha256s'],
                    'candidate changed during verification')
            ids = [q['id'] for q in verdict['questions']]
            expected_ids = ([PURPOSE_ID] if phase == 'purpose' else
                            [i['id'] for i in c['done_when'] if i['kind'] == 'review'])
            require(len(ids) == len(set(ids)) and set(ids) == set(expected_ids),
                    'review does not cover exactly all questions')
            result.append((start, end, verdict))
        except (GateError, OSError) as e:
            reasons.append(str(e))
    return result, reasons


def purpose_passed(repo, c, sha, entries):
    reviews, reasons = verified_reviews(repo, c, sha, entries, 'purpose')
    return bool(reviews) and not reasons and all(
        q['verdict'] == 'PASS' for _,_,v in reviews for q in v['questions'])


def paused(repo, c, sha, entries):
    """Any two FAILs on an unchanged candidate pause this revision, persistently."""
    starts = {e['run_id']: e for e in entries if e['event'] == 'reserved'}
    counts = {}
    for end in entries:
        if end['event'] != 'finished' or end['exit'] != 0 or end['error']:
            continue
        start = starts[end['run_id']]
        if start['role'] != 'verifier' or start['binding']['contract_sha256'] != sha:
            continue
        path = contained(repo, end['verdict_path'])
        require(file_hash(path) == end['verdict_sha256'], 'verdict file hash mismatch')
        verdict = validate(load(path), 'verdict')
        require(all(verdict[k] == v for k,v in start['binding'].items()), 'verdict binding mismatch')
        # Reset upon *any* output transition, even A -> B -> A.
        candidate = start['binding']['output_sha256s']
        segment = 0
        previous = None
        for event in entries:
            if event is end:
                break
            hashes = (event.get('output_sha256s') if event['event'] == 'finished' else
                      (event['binding'] or {}).get('output_sha256s'))
            if hashes is not None and hashes != previous:
                segment += 1
                previous = hashes
        for q in verdict['questions']:
            if q['verdict'] == 'FAIL':
                key = (start['phase'], segment, tuple(sorted(candidate.items())), q['id'])
                counts[key] = counts.get(key, 0) + 1
                if counts[key] >= 2:
                    return f'two FAILs without output change: {q["id"]}; revise and reapprove'
    return None


def models_outputs(repo, c, hashes):
    """Detect patches for models/, and conservatively treat all patch artifacts as model work."""
    for rel in hashes:
        if rel.endswith(('.patch', '.diff')):
            return True
        if rel.endswith(('.sh', '.py')):
            if b'models/' in contained(repo, rel).read_bytes():
                return True
    return any(x.startswith('models-application:') for x in c['constraints'])


def review_summary(repo, c, sha, entries, hashes):
    reviews, reasons = verified_reviews(repo, c, sha, entries, 'output')
    need = 2 if models_outputs(repo, c, hashes) else 1
    models = {v['actual_model'] for _,_,v in reviews}
    if len(models) < need:
        reasons.append(f'need {need} distinct output reviewers; have {len(models)}')
    for _,_,v in reviews:
        for q in v['questions']:
            if q['verdict'] != 'PASS':
                reasons.append(f'review {q["id"]}: {q["verdict"]}')
    return [{'run_id':end['run_id'], 'model':v['actual_model'],
             'verdict_sha256':end['verdict_sha256'], 'questions':v['questions']}
            for _,end,v in reviews], reasons
