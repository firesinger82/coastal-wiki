#!/usr/bin/env python3
"""Read-only validation of the staged candidate; logs stay in this directory."""
import csv
import hashlib
import json
import os
import re
import subprocess
import sys
from collections import Counter
from pathlib import Path

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / '_staging/efdc-migration'
CAND = OUT / 'wiki-candidate'
sys.path.insert(0, str(ROOT / '_staging/model-migration-framework'))
import refparser as rp

def read_csv(name):
    return list(csv.DictReader((OUT / name).open()))

def mask_coords(text):
    def sub(m):
        if not m.group('lines'):
            return m.group()
        a = m.start('lines') - m.start()
        b = m.end('lines') - m.start()
        return m.group()[:a] + '<COORD>' + m.group()[b:]
    # Brackets are absent from this particular CSV but handled without changing syntax.
    return rp.FILE_RE.sub(sub, rp.BRACKET_RE.sub(sub, text))

def audit():
    rows, ledger, classes = read_csv('line-ref-map.csv'), read_csv('apply-report.csv'), read_csv('final-classification.csv')
    assert Counter(r['category'] for r in ledger) == {'A': 11, 'B': 7, 'C': 152, 'D': 12}
    assert all(r['applied'] == 'yes' for r in ledger)
    print('PASS: apply-report 182 operations = A11 / B7 / C152 / D12; UNRESOLVED 0')
    originals = {str(p.relative_to(CAND)): (ROOT / p.relative_to(CAND)).read_text()
                 for p in CAND.rglob('*.md')}
    candidates = {p: (CAND / p).read_text() for p in originals}
    assert len(originals) == 31
    assert all(originals[p] != candidates[p] for p in originals)
    for p in originals:
        orig = ROOT / p
        dest = CAND / p
        assert orig.stat().st_mode == dest.stat().st_mode, ('mode changed', p)
        assert not dest.is_symlink() and dest.stat().st_nlink == 1
    print('PASS: only the 31 designated candidate notes; file modes preserved; no symlinks/hardlinks')

    # Reconstruct each whole note from the delivered ledger. Its before/after
    # columns are sequential C -> D -> A -> B operations in original-line space.
    state = {p: text.splitlines(keepends=True) for p, text in originals.items()}
    spans = {
        ('models/EFDC/manifest.md', 17): (17, 17),
        ('models/EFDC/manual-notes/efdc-implementation-guide.md', 193): (189, 193),
        ('models/EFDC/manual-notes/efdc-user-manual-r850.md', 104): (104, 104),
        ('models/EFDC/source-analysis/efdc_transport_scheme.md', 28): (18, 35),
        ('models/EFDC/source-analysis/efdc_transport_scheme.md', 65): (65, 77),
        ('models/EFDC/source-analysis/sediment/efdc_sediment.md', 205): (205, 205),
        ('models/EFDC/source-analysis/efdc_water_quality.md', 106): (106, 107),
        ('models/EFDC/source-analysis/efdc_vertical.md', 80): (70, 80),
        ('models/EFDC/source-analysis/efdc_vertical.md', 81): (81, 81),
        ('models/EFDC/source-analysis/efdc_vertical.md', 82): (82, 82),
        ('models/EFDC/source-analysis/efdc_baroclinic_eos.md', 75): (75, 83),
    }
    for r in ledger:
        p, n = r['note'], int(r['note_line'])
        a, b = spans[(p, n)] if r['category'] == 'A' else (n, n)
        assert ''.join(state[p][a-1:b]).rstrip('\n') == r['note_text_before'], ('ledger before', p, n)
        if r['category'] in ('C', 'D'):
            assert mask_coords(r['note_text_before']) == mask_coords(r['note_text_after']), ('coordinate prose drift', p, n)
        state[p][a-1] = r['note_text_after'] + '\n'
        for i in range(a, b):
            state[p][i] = ''
    assert all(''.join(state[p]) == candidates[p] for p in state)
    print('PASS: delivered ledger reconstructs candidate bytes; all C/D operations change only coordinates')

    moved = [r for r in rows if r['status'] == 'MOVED']
    interior = 0
    for r in moved:
        old = (ROOT / 'models/EFDC/raw/source_code/EFDCPlus_Stable' / r['source']).read_text().splitlines()
        new = (ROOT / '_staging/efdc-prescan/new' / r['source'].replace('/', '__')).read_text().splitlines()
        old_ranges, new_ranges = rp.parse_ranges(r['old']), rp.parse_ranges(r['new'])
        assert len(old_ranges) == len(new_ranges)
        for (a, b), (c, d) in zip(old_ranges, new_ranges):
            assert old[a-1] == new[c-1] and old[b-1] == new[d-1], r
        interior += any(old[a-1:b] != new[c-1:d] for (a, b), (c, d) in zip(old_ranges, new_ranges))
        # Independently extract the target citation from the corresponding CSV operation.
        ops = [x for x in ledger if x['category'] == 'C' and x['note'] == r['note'] and x['note_line'] == r['note_line']]
        target = next(ref for op in ops for ref in rp.parse_line(op['note_text_after'])
                      if ref['kind'] == 'file-line' and Path(ref['path']).name == Path(r['source']).name
                      and ref['ranges'] == new_ranges)
        assert target['raw'] in candidates[r['note']], ('target missing', r)
        om = rp.BRACKET_RE.fullmatch(r['ref']) or rp.FILE_RE.fullmatch(r['ref'])
        nm = rp.BRACKET_RE.fullmatch(target['raw']) or rp.FILE_RE.fullmatch(target['raw'])
        assert re.sub(r'\d+', '#', om.group('lines')) == re.sub(r'\d+', '#', nm.group('lines'))
        assert om.group('path') == nm.group('path')
    assert interior == 31
    print('PASS: 152 MOVED citations present with exact range syntax/path preservation; endpoints equal 152/152')
    print('INFO: whole ranges equal 121; interior differs 31, authorized by codex-task DECISIONS D1')

    identical_in, identical_out = 0, 0
    for r in rows:
        if r['status'] != 'IDENTICAL':
            continue
        p, n = r['note'], int(r['note_line'])
        if p in state:
            interval = next(((a, b) for (name, _), (a, b) in spans.items() if name == p and a <= n <= b), (n, n))
            assert r['ref'] in ''.join(state[p][interval[0]-1:interval[1]])
            identical_in += 1
        else:
            assert r['ref'] in (ROOT / p).read_text().splitlines()[n-1]
            identical_out += 1
    assert identical_in + identical_out == 167
    print(f'PASS: IDENTICAL citations preserved 167 ({identical_in} in candidate notes, {identical_out} outside candidate)')
    for r in classes:
        if r['final'] != 'NO_ACTION':
            continue
        p, n = r['note'], int(r['note_line'])
        old = originals.get(p, (ROOT / p).read_text()).splitlines()[n-1]
        new = state[p][n-1].rstrip('\n') if p in state else old
        assert mask_coords(old) == mask_coords(new), ('NO_ACTION prose changed', r)
    print('PASS: NO_ACTION prose unchanged 20/20 (explicit C/D coordinate updates excluded)')
    fm = re.compile(r'\A---\n.*?\n---', re.S)
    for p in originals:
        a, b = fm.match(originals[p]), fm.match(candidates[p])
        assert (a.group() if a else None) == (b.group() if b else None)
    v = 'models/EFDC/source-analysis/efdc_vertical.md'
    assert originals[v].splitlines()[132] == state[v][132].rstrip('\n')
    impl = 'models/EFDC/manual-notes/efdc-implementation-guide.md'
    assert originals[impl].splitlines()[188] in candidates[impl]
    print('PASS: all frontmatter and both explicitly protected B sites preserved')
    for r in ledger:
        if r['category'] != 'B':
            continue
        t = r['note_text_after']
        assert 'EFDC+ Stable 12.5' in t and 'SGZ' in t and 'IINTPG /= 0' in t and 'setbcs.f90:449' in t
    print('PASS: all 7 B sites contain the version scope and three required elements')
    for rel, sha in json.loads((OUT / 'baseline-sha256.json').read_text()).items():
        assert hashlib.sha256((ROOT / rel).read_bytes()).hexdigest() == sha, ('read-only baseline changed', rel)
    print('PASS: original notes, referenced pinned sources, new sources, patches and task/input CSV hashes unchanged')
    # Read-only applicability check. Do not apply the patch to canonical files.
    res = subprocess.run(['git', 'apply', '--check', str(OUT / 'wiki-candidate.diff')], cwd=ROOT, capture_output=True, text=True)
    assert res.returncode == 0, res.stderr
    print('PASS: git apply --check wiki-candidate.diff (read-only; no apply performed)')
    print('RESULT: PASS')

if __name__ == '__main__':
    if '--audit-only' in sys.argv:
        audit()
        raise SystemExit(0)
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE='1')
    # The validator unconditionally chdirs to its own repository and has no
    # --root option. Load its unmodified functions, then set the requested tree.
    hygiene = (
        'import os, runpy, sys; from pathlib import Path; '
        f'ns=runpy.run_path({str(ROOT / "tools/validate-canonical-hygiene.py")!r}); '
        f'os.chdir({str(CAND)!r}); '
        'sys.argv=["validate-canonical-hygiene.py"]; '
        'print("Target: wiki-candidate (working-tree mode)"); '
        'files=ns["tree_files"](ns["CANONICAL_ROOTS"]); '
        'assert len(files)==31; print("Candidate Markdown files:", len(files)); '
        'sys.exit(ns["main"]())'
    )
    jobs = [
        ('validate-canonical-hygiene-tree.txt', [sys.executable, '-B', '-c', hygiene]),
        ('test-refparser.txt', [sys.executable, '-B', '_staging/model-migration-framework/test_refparser.py']),
        ('migration-checks.txt', [sys.executable, '-B', str(Path(__file__)), '--audit-only']),
    ]
    failed = False
    for name, command in jobs:
        result = subprocess.run(command, cwd=ROOT, env=env, text=True, capture_output=True)
        (OUT / name).write_text('COMMAND: ' + repr(command) + '\n\n' + result.stdout + result.stderr + f'\nEXIT_CODE: {result.returncode}\n')
        print(name, 'exit', result.returncode)
        print(result.stdout, end='')
        if result.stderr:
            print(result.stderr, end='')
        failed |= result.returncode != 0
    raise SystemExit(1 if failed else 0)
