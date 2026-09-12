"""Source-bound evidence for fixed residual corrections R3-C1..C4."""
import hashlib
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[5]
SRC = ROOT / 'models/XBeach/raw/source_code/trunk'


def bind(p):
    return {'path': str(p.relative_to(ROOT)), 'sha256': hashlib.sha256(p.read_bytes()).hexdigest()}


def span(rel, first, last):
    p = SRC / rel
    raw = p.read_bytes()
    lines = raw.split(b'\n')
    assert 1 <= first <= last <= len(lines) - int(raw.endswith(b'\n')), (rel, first, last)
    return {**bind(p), 'line_start': first, 'line_end': last,
            'quote_exact_utf8': b'\n'.join(lines[first-1:last]).decode()}


def main():
    selected = {
        'src/xbeachlibrary/params.F90': [(321, 334), (928, 949)],
        'src/xbeachlibrary/paramsconst.F90': [(80, 91)],
        'src/xbeachlibrary/readkey.F90': [(762, 804), (806, 824), (866, 875)],
        'src/xbeachlibrary/morphevolution.F90': [(173, 204), (1333, 1333), (1858, 1858),
                                               (2116, 2116), (2502, 2502), (2565, 2576)],
        'src/xbeachlibrary/libxbeach.F90': [(293, 310)],
        'src/xbeachlibrary/boundaryconditions.F90': [(39, 44), (205, 250), (655, 671)],
        'src/xbeachlibrary/waveparamsnew.F90': [(1, 11), (98, 106), (128, 151), (167, 205),
                                              (211, 241), (244, 290), (340, 349), (408, 426),
                                              (936, 941), (2695, 2704), (2783, 2861), (2872, 2935),
                                              (2964, 2982), (3032, 3037)],
        'src/xbeachlibrary/wave_timestep.F90': [(75, 114)],
        'src/xbeachlibrary/wave_stationary_directions.F90': [(33, 49), (71, 76)],
        'src/xbeachlibrary/groundwater.F90': [(283, 285), (610, 638), (1554, 1643)],
    }
    evidence = [span(rel, a, b) for rel, intervals in selected.items() for a, b in intervals]
    params = (SRC / 'src/xbeachlibrary/params.F90').read_text().splitlines()
    pairs = re.findall(r"'([^']+)'\s*,\s*(FORM_\w+)", '\n'.join(params[931:943]))
    consts = dict((k, int(v)) for k, v in re.findall(r'\b(FORM_\w+)\s*=\s*(\d+)',
                   (SRC / 'src/xbeachlibrary/paramsconst.F90').read_text()))
    names = {0: 'sedtransform', 1: 'sedtransform', 2: 'sedtransform', 3: 'Nielsen2006',
             4: 'mccall_vanrijn', 11: 'intra_sedtr'}
    assert len(pairs) == 12 and len(set(v for _, v in pairs)) == 12
    contracts = [{'input_name': n, 'constant': c, 'value': consts[c],
                  'direct_formula_callee': names.get(consts[c]),
                  'bulk_zero_early_return': consts[c] in (3, 4),
                  'otherwise': 'common transport section after SELECT',
                  'limit': 'Source SELECT dispatch only; not a full numerical-run result'} for n, c in pairs]
    reuse = ['build-mode-20260912/build-map.json', 'build-mode-20260912/contracts.json',
             'infiltration-document-code-comparison.json',
             'manuals-docx-read/conditional-visual-read/receipt.json',
             'remaining-20260912/remaining.json']
    result = {'scope': 'R3-C1..C4 source corrections, not full model coverage or solver patches',
              'human_approval_issued': False, 'evidence': evidence,
              'form_dispatch': contracts, 'reused_evidence': [bind(HERE.parent / n) for n in reuse]}
    (HERE / 'evidence.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    print(f'Recorded {len(contracts)} input-to-dispatch contracts and {len(evidence)} source spans')


if __name__ == '__main__':
    main()
