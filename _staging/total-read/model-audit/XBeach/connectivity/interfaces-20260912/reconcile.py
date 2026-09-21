"""Reconcile the fixed G2/G3 residuals; does not close the general G1 call graph."""
import base64
import collections
import hashlib
import json
import re
import runpy
import shutil
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[5]
PREV = HERE.parent / 'runtime-20260912'
SRC = ROOT / 'models/XBeach/raw/source_code/trunk'
sys.path.insert(0, str(PREV))
from index_calls import statements, strip_comment, mask_strings

def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def read(p): return json.loads(p.read_text())
def dump(name, obj): (HERE / name).write_text(json.dumps(obj, ensure_ascii=False, indent=2) + '\n')
bindings = read(PREV / 'source-bindings.json')
units = {x['path']: x for x in bindings}
procs = [json.loads(s) for s in (PREV / 'procedures.jsonl').read_text().splitlines()]
byid = {x['id']: x for x in procs}
interfaces = read(PREV / 'interfaces.json')
sites = read(PREV / 'include-sites.json')
gaps = read(PREV / 'remaining-gaps.json')
ids = gaps['gaps'][1]['procedure_ids']
evidence = {}

def span(path, start, end):
    path = str(path)
    p = ROOT / path
    key = f'{path}:{start}-{end}'
    if key not in evidence:
        lines = p.read_bytes().split(b'\n')
        assert 1 <= start <= end <= len(lines), key
        raw = b'\n'.join(lines[start - 1:end])
        row = {'path': path, 'line_start': start, 'line_end': end,
               'sha256': sha(p), 'span_sha256': hashlib.sha256(raw).hexdigest()}
        try: row['quote_exact_utf8'] = raw.decode('utf8')
        except UnicodeDecodeError: row['quote_exact_base64'] = base64.b64encode(raw).decode()
        evidence[key] = row
    return key

for u in bindings:
    assert sha(ROOT / u['path']) == u['sha256'], u['path']

# Each entry is a human-readable source disposition, not an inference from zero calls alone.
details = {
 'space_consistency': ('cpp-disabled', 1, 50, 'Entire debugging module is inside literal #if 0.'),
 'printssums': ('cpp-disabled', 1, 50, 'Entire debugging module is inside literal #if 0.'),
 'printssumso': ('cpp-disabled', 1, 50, 'Entire debugging module is inside literal #if 0.'),
 'getnkeys': ('public-helper', 1, 32, 'Public key-count helper expands getkey.inc; no internal call observed.'),
 'gw_calc_local_connected_infil': ('cpp-disabled', 1718, 1799, 'Unused local infiltration implementation is enclosed in #if 0.'),
 'linear_interp_2d': ('public-helper', 1, 7, 'Public interpolation helper; former waveparamsnew calls are commented out.'),
 'make_map': ('public-helper', 1, 7, 'Public mapping helper; no internal call observed.'),
 'mkmap_step': ('public-helper', 1, 7, 'Public mapping-step helper; no internal call observed.'),
 'trapezoidal': ('public-helper', 1, 7, 'Public integration helper; same word in a later comment is not a call.'),
 'getarraydimsize_fortran': ('public-interface-helper', 1, 111, 'Direct public Fortran wrapper forwards to getarraydimsize_c; no matching named generic is declared here. DEC export comment uses another spelling; no linker export success is inferred.'),
 'set2dintarray_fortran': ('public-interface-helper', 1, 111, 'Direct public Fortran setter; no set2dintarray generic is declared in the header. Separate bind(C) setter exists.'),
 'strcmp': ('public-helper', 1, 22, 'Default-public string helper, no internal call or bind(C) entry observed.'),
 'strcpy': ('public-helper', 1, 22, 'Default-public string helper, no internal call or bind(C) entry observed.'),
 'stringlength': ('public-helper', 1, 16, 'Default-public name helper, no internal call observed.'),
 'dimensionnames': ('private-helper', 45, 63, 'Private ncoutput helper under USENETCDF; builds a joined dimension-name string through the NetCDF interface. No internal call observed.'),
 'runup': ('public-helper', 1, 28, 'Default-public prototype helper with incorrect-code comment; s%runup occurrences are data members, not calls to this function. This does not exclude active runup diagnostics.'),
 'solver_free': ('public-helper', 44, 58, 'Public deallocator for two solver work arrays; no internal call observed. Does not establish full cleanup in final().'),
 'index_allocated': ('public-helper-imported', 1, 39, 'Default-public allocation query; BMI imports the name but does not call it. Body expands index_allocated.inc.'),
 'space_shift_borders_matrix_real8': ('public-generic-helper', 1, 39, 'Specific of space_shift_borders under USEMPI; no internal call to the generic observed.'),
 'space_shift_borders_block_real8': ('public-generic-helper', 1, 39, 'Specific of space_shift_borders under USEMPI; no internal call to the generic observed.'),
 'space_collect_vector_real8': ('public-helper', 1, 39, 'Default-public USEMPI helper; absent from the space_collect generic, unlike the matrix/block specifics.'),
 'makecrossvector': ('public-helper', 1, 20, 'Public cross-section helper in otherwise private means_module; no internal call observed.'),
 'indextocrossunit': ('cpp-disabled', 1, 29, 'Private old output helper; entire varoutput module is inside #if 0 and retained for reference.'),
 'makebcf': ('public-legacy-helper', 1, 36, 'Old public waveparams provider; no active use waveparams or call makebcf in the frozen source inventory. Current boundary provider is waveparamsnew (prior R3-C1).'),
 'testje': ('public-test-helper', 1, 18, 'Default-public USEMPI test helper, no internal call observed. Model-owned calls only; no external MPI implementation read.'),
 'xmpi_getrow': ('public-helper', 1, 18, 'Default-public USEMPI row-gather helper, no internal call observed.'),
}

generated_prior = read(PREV / 'generated-links.json')
prior_outputs = {x['name']: x for x in generated_prior['records']}
generated = []
generated_text = {}
registry = []
with tempfile.TemporaryDirectory(prefix='xbeach-interface-includes-') as td:
    tmp = Path(td)
    for x in generated_prior['inputs']:
        p = ROOT / x['path']; assert sha(p) == x['sha256'], p
        target = tmp / p.relative_to(SRC)
        target.parent.mkdir(parents=True, exist_ok=True); shutil.copyfile(p, target)
    generator = tmp / 'scripts/generate.py'
    def capture(frame, event, arg):
        if event == 'return' and frame.f_code.co_filename == str(generator) and frame.f_code.co_name == 'main':
            registry.extend(frame.f_locals['variables'])
    oldargv = sys.argv
    try:
        sys.argv = [str(generator)]; sys.setprofile(capture)
        runpy.run_path(str(generator), run_name='__main__')
    finally: sys.setprofile(None); sys.argv = oldargv
    for p in sorted((tmp / 'src/xbeachlibrary').glob('*.inc')):
        old = prior_outputs[p.name]; assert sha(p) == old['sha256'], p.name
        generated_text[p.name] = p.read_text()
        hosts = []
        for site in sites:
            if site['include'] != p.name: continue
            u = units[site['path']]
            proc = byid.get(site['owner'])
            host = {**site, 'build_targets': u['build_targets'],
                    'source_evidence': span(site['path'], site['line_start'], site['line_end'])}
            if proc:
                host['declaration'] = proc['declaration']
                host['body_evidence'] = span(proc['path'], proc['line_start'], proc['line_end'])
            if p.name == 'xmpi_bcast.inc':
                target = next(x for x in procs if x['path'] == site['path'] and x['name'] == proc['name'] + '_3')
                host['three_argument_specific'] = target['id']
                host['specific_evidence'] = span(target['path'], target['line_start'], target['line_end'])
                host['resolution'] = 'Same x type/rank as enclosing two-argument wrapper; src and comm supply the third-argument family. Overload choice elsewhere remains G1.'
            hosts.append(host)
        functions = []
        for st in statements(p):
            for m in re.finditer(r'\b([a-z]\w*)\s*\(', mask_strings(st['text']), re.I):
                name = m[1].lower()
                targets = [x['id'] for x in procs if x['name'] == name and x['kind'] == 'function']
                generics = [x for x in interfaces if x['name'] == name]
                if targets or generics:
                    functions.append({'symbol': name, 'line_start': st['line_start'], 'line_end': st['line_end'],
                                      'statement': st['text'], 'candidate_definitions': targets,
                                      'generic_specifics': [s for g in generics for s in g['specific_names']]})
        generated.append({**old, 'host_bindings': hosts, 'model_function_reference_candidates': functions,
                          'disposition': 'included-in-model-hosts' if hosts else 'generated-declaration-asset-with-no-frozen-consumer',
                          'reference_limit': 'Function tokens and generic lists are candidates; source signatures/visibility and per-call feasibility remain G1.'})
assert len(generated) == 27
assert sum(len(x['definitions']) for x in generated) == 41

# Whole-token scans include comments and imports; retained classifications expose false positives.
def occurrences(name):
    rows = []
    pattern = re.compile(r'\b' + re.escape(name) + r'\b', re.I)
    texts = [(u['path'], (ROOT / u['path']).read_text(errors='replace'), False) for u in bindings]
    texts += [('generated:' + name, text, True) for name, text in generated_text.items()]
    for path, text, gen in texts:
        for n, line in enumerate(text.splitlines(), 1):
            if not pattern.search(line): continue
            code = mask_strings(strip_comment(line))
            if not pattern.search(code): kind = 'comment-or-string'
            elif re.match(r'\s*(public|private|module\s+procedure|use)\b', code, re.I): kind = 'visibility-generic-or-import'
            elif re.search(r'\b(?:end\s*)?(?:subroutine|function)\s+' + re.escape(name) + r'\b', code, re.I): kind = 'own-definition'
            elif re.match(r'\s*(integer|real|double\s+precision|logical|character)\b.*::', code, re.I): kind = 'data-or-result-declaration'
            elif re.search(r'\b' + re.escape(name) + r'\s*=(?!=|>)', code, re.I): kind = 'function-result-assignment'
            elif re.search(r'%\s*' + re.escape(name) + r'\b', code, re.I): kind = 'data-component'
            else: kind = 'needs-adjudication'
            row = {'path': path, 'line': n, 'text': line, 'kind': kind}
            if not gen: row['evidence'] = span(path, n, n)
            rows.append(row)
    return rows

resolutions = []
for pid in ids:
    p = byid[pid]; category, a, z, rationale = details[p['name']]
    refs = occurrences(p['name'])
    gs = [g for g in interfaces if g['path'] == p['path'] and p['name'] in g['specific_names']]
    generic_refs = {g['name']: occurrences(g['name']) for g in gs}
    unknown = [r for r in refs if r['kind'] == 'needs-adjudication']
    assert not unknown, (pid, unknown)
    for name, rr in generic_refs.items():
        for r in rr:
            if r['kind'] == 'needs-adjudication' and re.match(r'\s*(?:end\s*)?interface\b', r['text'], re.I):
                r['kind'] = 'generic-definition'
        assert not [r for r in rr if r['kind'] == 'needs-adjudication'], (name, rr)
    resolutions.append({'procedure_id': pid, 'category': category, 'rationale': rationale,
                        'module': p['module'], 'cpp': p['cpp'], 'build_targets': units[p['path']]['build_targets'],
                        'definition_evidence': span(p['path'], p['line_start'], p['line_end']),
                        'visibility_guard_evidence': span(p['path'], a, z),
                        'occurrences': refs, 'generics': gs, 'generic_occurrences': generic_refs,
                        'limit': 'No internal incoming reference in the frozen inventory; externally called public helpers are not ruled out.'})

exports = []
for p in procs:
    if not p['path'].endswith('/introspection.F90'): continue
    for entry in p['bind_c_names']:
        name = entry['name']
        if not re.fullmatch(r'(get|set)[0-4]d(int|double)array', name): continue
        m = re.fullmatch(r'(get|set)([0-4])d(int|double)array', name)
        exports.append({'symbol': name, 'operation': m[1], 'rank': int(m[2]), 'type': m[3], 'procedure_id': p['id'],
                        'evidence': span(p['path'], p['line_start'], p['line_end']),
                        'build_targets': units[p['path']]['build_targets']})
assert len(exports) == 16, len(exports)
counts = collections.Counter((v['fortrantype'], v['rank']) for v in registry)
registry_counts = [{'fortran_type': t, 'rank': r, 'count': n} for (t, r), n in sorted(counts.items())]
wrapper = 'models/XBeach/raw/source_code/trunk/src/pybeach/xbeach/libxbeach.py'
native = 'models/XBeach/raw/source_code/trunk/src/xbeachlibrary/introspection.F90'
bmi = 'models/XBeach/raw/source_code/trunk/src/xbeachlibrary/xbeach_bmi.f90'
contracts = [
 ('IF-01', 'Python metadata and dispatch', [span(wrapper, 166, 276)],
  'get: integer ranks 0..2, double ranks 0..4. set: global rank cap 4 but native integer exports end at 2. Synthetic integer ranks 3/4 reach absent setter names; actual registered rank distribution is recorded separately. Python3 c_char.value returns bytes, unlike the string comparisons; marker dispatch uses explicit metadata adapters.'),
 ('IF-02', 'Python scalar integer mismatch', [span(wrapper, 243, 276), span(native, 902, 929), span(native, 1043, 1070)],
  'set_array selects c_double for rank-zero integer values; native set0dintarray uses c_f_pointer to integer(c_int). Original bodies with test registry reproduce input 17 becoming integer 0 on this machine; double scalar remains 17.0. No whole DLL/solver execution is claimed.'),
 ('IF-03', 'Scalar getter target lifetime', [span(native, 529, 552), span(native, 764, 786)],
  'Scalar C getters copy state into local target r0/i0 and return c_loc of that local. No explicit SAVE or persistent target contract is declared there. Actual getters are not dereferenced in the probe; compiler storage flags and all builds are not adjudicated.'),
 ('IF-04', 'Array ABI and shape/layout', [span(wrapper, 178, 276)],
  'Introspection array APIs receive c_ptr without VALUE (pointer-to-pointer) and length by VALUE. Positive-rank getters expose model allocation addresses; Python attempts array(arrayp), which fails after the stable marker on NumPy 2.5.3 with PEP3118 buffer-format ValueError. Setter ndarray pointer casts do not convert dtype/layout; shape is asserted and can be omitted by Python optimization. Native setters copy into model storage.'),
 ('IF-05', 'Separate BMI variable interface', [span(bmi, 1, 34), span(bmi, 138, 140)],
  'Generated get_var returns borrowed model storage through c_ptr without VALUE; set_var receives c_ptr VALUE and copies via c_f_pointer. get_var_shape clears six slots and reverses dimensions to C memory order, unlike Python get_arrayshape. Unknown names return without a valid pointer update or leave zero shape; there is no Python-name aliasing to these entrypoints.'),
]
for template in ['get_var', 'get_var_shape', 'set_var']:
    path = str((SRC / 'src/xbeachlibrary/templates' / (template + '.mako')).relative_to(ROOT))
    contracts[-1][2].append(span(path, 1, len((ROOT / path).read_bytes().split(b'\n'))))
disabled = [p['id'] for p in procs if any(c['current'] == '#if 0' for c in p['cpp'])]
dump('helper-dispositions.json', {'scope': 'Exactly the 26 frozen R1-G2 identifiers', 'status': 'source-dispositions-complete',
     'scanned_inputs': [{'path': u['path'], 'sha256': u['sha256']} for u in bindings],
     'generated_scan_hashes': {x['name']: x['sha256'] for x in generated},
     'records': resolutions, 'literal_if0_definition_ids': disabled,
     'limits': ['Lexical occurrence census plus explicit source classification, not compiler/link/runtime reachability proof',
                'External public callers remain possible; no external dependency internals inspected'], 'human_approval_issued': False})
dump('generated-bindings.json', {'scope': '27 frozen generated outputs and model host/build bindings',
     'inputs': generated_prior['inputs'], 'records': generated,
     'limits': generated_prior['limits'] + ['Windows generate.exe equivalence remains unproved; per-call overload/guard adjudication remains G1'],
     'human_approval_issued': False})
dump('wrapper-contracts.json', {'scope': 'Dynamic Python array choices, introspection C exports and distinct BMI variable API',
     'exports': exports, 'registry_counts': registry_counts,
     'registry_variables': [{'name': v['name'], 'fortran_type': v['fortrantype'], 'rank': v['rank']} for v in registry],
     'contracts': [{'id': i, 'title': t, 'evidence': e, 'disposition': d} for i,t,e,d in contracts],
     'probe': {'path': str((HERE/'probe-results.json').relative_to(ROOT)), 'sha256': sha(HERE/'probe-results.json')},
     'status': 'source-interface-dispositions-complete; known implementation/environment limitations retained',
     'whole_solver_verified': False, 'human_approval_issued': False})
dump('evidence.json', {'base_commit': '760413c', 'scope': 'Fixed R1-G2/G3 only', 'spans': evidence,
                       'human_approval_issued': False})
print(json.dumps({'helpers': len(resolutions), 'generated': len(generated), 'exports': len(exports),
                  'registry_counts': registry_counts, 'source_spans': len(evidence), 'if0_definitions': len(disabled)}))
