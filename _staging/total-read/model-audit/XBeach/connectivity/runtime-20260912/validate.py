"""Check the bounded source/index/install contract; never grant completion or HG."""
import argparse
import hashlib
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[5]
TARGETS = {'models/XBeach/'+x for x in [
    'README.md', 'source-analysis/xbeach_flow_solver.md', 'source-analysis/xbeach_nonh.md',
    'source-analysis/xbeach_vegetation.md', 'source-analysis/xbeach_tide_forcing.md',
    'source-analysis/xbeach_output.md', 'source-analysis/xbeach-coupled-physics-contracts.md']}

def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def read(p): return json.loads(p.read_text())
def bind(x): assert sha(ROOT/x['path']) == x['sha256'], ('binding drift', x['path'])
def jsonl(name): return [json.loads(x) for x in (HERE/name).read_text().splitlines()]

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--installed', action='store_true')
    args = parser.parse_args()
    scope = read(HERE.parent/'remaining-20260912/source-reuse.json')
    prefix = 'models/XBeach/raw/source_code/trunk/'
    expected = {prefix+x['path']:x for x in scope['files'] if x['role'] in {'compiled_fortran_unit','python_wrapper'}}
    sources = read(HERE/'source-bindings.json')
    assert len(sources)==59 and {x['path'] for x in sources}==set(expected)
    for x in sources:
        bind(x)
        assert x['sha256']==expected[x['path']]['sha256'] and x['role']==expected[x['path']]['role']
        assert x['build_targets']==expected[x['path']]['build_targets']
    procs, calls = jsonl('procedures.jsonl'), jsonl('call-candidates.jsonl')
    byid, callbyid = {x['id']:x for x in procs}, {x['id']:x for x in calls}
    assert len(byid)==len(procs) and len(callbyid)==len(calls), 'duplicate IDs'
    for p in procs:
        bind(p)
        assert p['path'] in expected and expected[p['path']]['role']=='compiled_fortran_unit'
        lines = (ROOT/p['path']).read_bytes().split(b'\n')
        assert 1<=p['line_start']<=p['line_end']<=len(lines)
        assert re.search(r'\b'+re.escape(p['name'])+r'\b', b'\n'.join(lines[p['line_start']-1:p['line_end']]).decode(), re.I)
    incoming = set()
    for c in calls:
        p = byid[c['caller']]
        assert p['line_start']<=c['line_start']<=c['line_end']<=p['line_end']
        targets = c['direct_definition_candidates']+c['generic_specific_candidates']
        assert all(x in byid and not byid[x]['interface_declaration'] for x in targets)
        incoming.update(targets)
        assert c['semantic_status'].startswith('candidate_only')
    orphan_ids = {p['id'] for p in procs if not p['interface_declaration'] and p['id'] not in incoming}
    dispositions = read(HERE/'entry-dispositions.json')
    assert len(dispositions['records'])==len(orphan_ids)
    assert {x['id'] for x in dispositions['records']}==orphan_ids
    for x in dispositions['records']:
        bind(x['source'])
    open_ids = {x['id'] for x in dispositions['records'] if x['classification'].startswith('open_')}
    assert open_ids==set(dispositions['open_ids'])
    gaps = read(HERE/'remaining-gaps.json')
    assert set(next(x for x in gaps['gaps'] if x['id']=='R1-G2')['procedure_ids'])==open_ids
    unknown = {c['id'] for c in calls if not c['direct_definition_candidates'] and not c['generic_specific_candidates']}
    boundaries = read(HERE/'interface-boundaries.json')
    flat = [c for x in boundaries['symbols'] for c in x['call_candidate_ids']]
    assert len(flat)==len(set(flat)) and set(flat)==unknown
    for x in boundaries['symbols']:
        assert all(callbyid[c]['symbol']==x['symbol'] for c in x['call_candidate_ids'])
    assert boundaries['library_internals_inspected'] is False
    generated = read(HERE/'generated-links.json')
    bind(generated['prior_probe'])
    for x in generated['inputs']: bind(x)
    prior = read(ROOT/generated['prior_probe']['path'])
    outputs = {x['name']:x for x in prior['outputs']}
    assert len(generated['records'])==27 and {x['name'] for x in generated['records']}==set(outputs)
    for x in generated['records']:
        assert x['sha256']==outputs[x['name']]['sha256']
        assert sha(ROOT/prefix/x['template'])==x['template_sha256']
    for x in read(HERE/'python-export-links.json')['literal_links']:
        assert x['python_path'] in expected and expected[x['python_path']]['role']=='python_wrapper'
        assert x['C_export_candidates']
        for pid in x['C_export_candidates']:
            assert any(v['name']==x['symbol'] for v in byid[pid]['bind_c_names'])
    evidence = read(HERE/'evidence.json')
    for x in evidence['evidence']:
        bind(x)
        lines = (ROOT/x['path']).read_bytes().split(b'\n')
        assert 1<=x['line_start']<=x['line_end']<=len(lines)
        assert b'\n'.join(lines[x['line_start']-1:x['line_end']]).decode()==x['quote_exact_utf8']
    for x in evidence['reused_evidence']: bind(x)
    evid_ids = {x['id'] for x in evidence['evidence']}
    assert len(evidence['contracts'])==9
    for c in evidence['contracts']:
        assert c['evidence'] and set(c['evidence'])<=evid_ids and c['guard']
    summary = read(HERE/'index-summary.json')
    assert summary['procedure_candidates']==len(procs) and summary['call_candidates']==len(calls)
    assert summary['no_incoming_candidates']==len(orphan_ids)
    assert summary['fortran_units']==57 and summary['python_paths']==2
    for x in [evidence,summary,dispositions,gaps]: assert x['R1_complete'] is False
    immutable_path = ROOT/'_staging/total-read/model-audit/XBeach/closure/immutable-baseline.json'
    immutable = read(immutable_path)['files']
    assert len(immutable)==292
    for p,h in immutable.items(): assert sha(ROOT/p)==h, ('immutable drift',p)
    manifest = read(HERE/'install-manifest.json')
    assert len(manifest['files'])==7 and {x['target'] for x in manifest['files']}==TARGETS
    links = 0
    for x in manifest['files']:
        candidate,target = ROOT/x['candidate'],ROOT/x['target']
        assert candidate.resolve().is_relative_to((HERE/'canonical').resolve())
        assert sha(candidate)==x['after_sha256']
        assert sha(target)==x['after_sha256' if args.installed else 'before_sha256']
        for dest in re.findall(r'\]\(([^\s)]+)\)',candidate.read_text()):
            if '://' in dest or dest.startswith('#'): continue
            assert (target.parent/dest.split('#')[0]).exists(),(x['target'],dest)
            links += 1
    reviewed = False
    if (HERE/'review-response.json').exists():
        review = read(HERE/'review-response.json')
        for x in review['reviews']+review['final_artifacts']: bind(x)
        assert review['human_approval_issued'] is False
        assert review['open_blocking_findings']==0
        reviewed = True
    if args.installed: assert reviewed, 'Final independent review receipt required'
    result = {'status':'PASS','stage':'installed' if args.installed else 'preflight',
              'source_paths':59,'source_spans':len(evidence['evidence']), 'source_contracts':9,
              'procedure_candidates':len(procs),'call_candidates':len(calls),
              'generated_outputs_bound':27,'canonical_targets':7,'relative_links_checked':links,
              'immutable_files':292,'review_binding_checked':reviewed,
              'R1_complete':False,'whole_model_complete':False,'human_approval_issued':False,
              'scope':'Structural/hash/source-quote/install validation; not semantic reachability, solver execution or human acceptance'}
    (HERE/('validation.json' if args.installed else 'preflight.json')).write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(result,ensure_ascii=False))

if __name__=='__main__': main()
