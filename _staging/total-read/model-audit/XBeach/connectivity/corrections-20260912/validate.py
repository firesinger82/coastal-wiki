"""Verify source/receipt bindings and exact staged or installed bytes; no approval."""
import argparse
import hashlib
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[5]
SRC = ROOT / 'models/XBeach/raw/source_code/trunk'
TARGETS = {
    'models/XBeach/README.md',
    'models/XBeach/source-analysis/xbeach_intrawave_sediment_transport.md',
    'models/XBeach/source-analysis/xbeach_morphology.md',
    'models/XBeach/source-analysis/xbeach_wave_boundary_generation.md',
    'models/XBeach/source-analysis/wave/xbeach_wave_boundary.md',
    'models/XBeach/source-analysis/xbeach_wave_action_balance.md',
    'models/XBeach/source-analysis/xbeach_wave_stationary.md',
    'models/XBeach/manual-notes/xbeach-manual-equation-code-contracts.md',
}

def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

def read(p):
    return json.loads(p.read_text())

def bind(f):
    assert sha(ROOT / f['path']) == f['sha256'], ('binding drift', f['path'])

def span(e):
    bind(e)
    raw = (ROOT / e['path']).read_bytes()
    lines = raw.split(b'\n')
    count = len(lines) - int(raw.endswith(b'\n'))
    assert 1 <= e['line_start'] <= e['line_end'] <= count, e
    assert b'\n'.join(lines[e['line_start']-1:e['line_end']]).decode() == e['quote_exact_utf8'], e['path']

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--installed', action='store_true')
    args = parser.parse_args()
    evidence = read(HERE / 'evidence.json')
    for e in evidence['evidence']:
        span(e)
    for e in evidence['reused_evidence']:
        bind(e)
    dispatch = evidence['form_dispatch']
    assert len(dispatch) == 12 and {x['value'] for x in dispatch} == set(range(12))
    assert len({x['input_name'] for x in dispatch}) == 12
    expected = {0:'sedtransform', 1:'sedtransform', 2:'sedtransform', 3:'Nielsen2006', 4:'mccall_vanrijn', 11:'intra_sedtr'}
    for x in dispatch:
        assert x['direct_formula_callee'] == expected.get(x['value'])
        assert x['bulk_zero_early_return'] == (x['value'] in (3,4))
    assert next(x for x in dispatch if x['input_name'] == 'intrasedtr')['value'] == 11
    probe = read(HERE / 'probe-results.json')
    assert probe['status'] == 'PASS' and probe['run_exit_code'] == 0
    assert probe['source_sha256'] == sha(HERE / 'dispatch-probe.f90')
    body = (HERE / 'dispatch-probe.f90').read_bytes()
    for e in probe['source_excerpts']:
        a,b = e['lines']
        original = b'\n'.join((SRC/'src/xbeachlibrary'/e['file']).read_bytes().split(b'\n')[a-1:b])
        assert original in body, e
    assert len(probe['rows']) == 24
    assert {(x['form_value'],x['bulk']) for x in probe['rows']} == {(f,b) for f in range(12) for b in range(2)}
    markers = {'sedtransform':1, 'Nielsen2006':2, 'mccall_vanrijn':3, 'intra_sedtr':4, None:0}
    for x in probe['rows']:
        f,b = x['form_value'],x['bulk']
        assert x['callee_marker'] == markers[expected.get(f)]
        assert x['reaches_after_select'] == (not (f in (3,4) and b == 0))
    build = read(HERE.parent / 'build-mode-20260912/build-map.json')
    for e in build['src_files'] + build['projects'] + build['solutions']:
        assert sha(SRC / e['path']) == e['sha256'], e['path']
    for e in build['autotools']['evidence']:
        span(e)
    excluded = {'wave_boundary_main.f90','wave_boundary_init.f90','wave_boundary_update.f90','wave_boundary_datastore.f90','wave_bc_nextgen.f90','wave_stationary.F90','wave_directions.F90'}
    for name in excluded:
        row = next(x for x in build['src_files'] if x['path'] == 'src/xbeachlibrary/' + name)
        assert not row['build_targets'], name
    comparison = read(HERE.parent/'infiltration-document-code-comparison.json')
    bind(comparison['source'])
    bind(comparison['visual_receipt'])
    visual = read(ROOT / comparison['visual_receipt']['path'])
    chosen = [x for x in visual['records'] if x['base'] in {'kingsday-oleObject133','master-oleObject143','master-oleObject81'}]
    assert len(chosen) == 3
    for x in chosen:
        for name in ['source','preview','paragraph','pdf','png']:
            bind(x[name])
    immutable = read(ROOT/'_staging/total-read/model-audit/XBeach/closure/immutable-baseline.json')['files']
    assert len(immutable) == 292
    for p,h in immutable.items():
        assert sha(ROOT/p) == h, ('immutable drift',p)
    manifest = read(HERE/'install-manifest.json')
    assert len(manifest['files']) == 8 and {x['target'] for x in manifest['files']} == TARGETS
    links = 0
    for x in manifest['files']:
        candidate = ROOT / x['candidate']
        target = ROOT / x['target']
        assert candidate.resolve().is_relative_to((HERE/'canonical').resolve()), candidate
        assert sha(candidate) == x['after_sha256'], candidate
        assert sha(target) == x['after_sha256' if args.installed else 'before_sha256'], target
        # Relative Markdown file links are interpreted from their destination.
        for dest in re.findall(r'\]\(([^\s)]+)\)', candidate.read_text()):
            if '://' in dest or dest.startswith('#'):
                continue
            assert (target.parent / dest.split('#')[0]).exists(), (x['target'],dest)
            links += 1
    review_checked = False
    if (HERE/'review-response.json').exists():
        review = read(HERE/'review-response.json')
        for e in review['reviews'] + review['final_artifacts']:
            bind(e)
        assert review['human_approval_issued'] is False
        review_checked = True
    if args.installed:
        assert review_checked, 'No source review receipt'
    result = {'status':'PASS', 'stage':'installed' if args.installed else 'preflight',
              'source_spans':len(evidence['evidence']), 'input_dispatch_contracts':12,
              'bounded_dispatch_probe_combinations':24, 'canonical_targets':8,
              'relative_links_checked':links, 'immutable_files':292,
              'review_binding_checked':review_checked,
              'scope':'Source/hash/citation/dispatch-probe/install checks, not whole-model validation or approval',
              'whole_model_complete':False, 'human_approval_issued':False}
    (HERE/('validation.json' if args.installed else 'preflight.json')).write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(result,ensure_ascii=False))

if __name__ == '__main__':
    main()
