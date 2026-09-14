"""Read-only, bounded readiness inventory. Run from the repository root.

Counts are metadata observations, never semantic-read or approval receipts.
No recursive traversal of raw trees; only named roots/documents are inspected.
"""
from pathlib import Path
from collections import Counter, defaultdict
import hashlib
import json
import posixpath
import re
import subprocess

OUT = Path('_staging/model-readiness-20260913')
BASE = Path('_staging/wiki-navigation-20260913/note-state-before.json')
CORES = {
    'ADCIRC': ['adcirc'],
    'CADMAS-SURF': ['Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami'],
    'Celeris': ['Celeris-WebGPU'], 'Delft3D': ['Delft3D'],
    'EFDC': ['EFDCPlus_Stable'], 'FUNWAVE': ['FUNWAVE-TVD', 'FUNWAVE-GPU'],
    'LISFLOOD-FP': ['LISFLOOD-FP'], 'ROMS': ['roms'], 'SFINCS': ['sfincs'],
    'SWAN': ['swan'], 'SWASH': ['swash'], 'ShorelineS': ['shorelines'], 'XBeach': ['trunk'],
}
DOCS = {
    'ADCIRC': ('17-boundary-and-forcing-inputs.md', 'raw/manuals/pdfs'),
    'CADMAS-SURF': ('cadmas-manuals-catalogue.md', 'raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Manual/CADMAS-SURF3D_Manural_English.pdf'),
    'Celeris': ('celeris-architecture-and-config.md', 'raw/source_code/Celeris-WebGPU/docs/architecture/CONFIGURATION.md'),
    'Delft3D': ('delft3d-manuals-overview.md', 'raw/manuals/pdfs/Delft3D-FLOW_User_Manual.pdf'),
    'EFDC': ('efdc-manuals-overview.md', 'raw/manuals/pdfs/EFDC_Theory_Document_Ver_12.pdf'),
    'FUNWAVE': ('funwave-user-manual-full.md', 'raw/source_code/FUNWAVE-TVD/doc/funwave_tvd_3.0.pdf'),
    'LISFLOOD-FP': ('lisflood-fp-user-manual.md', 'raw/source_code/LISFLOOD-FP/LISFLOOD-FP user manual.pdf'),
    'ROMS': ('roms-wiki-overview.md', 'raw/manuals/wiki'),
    'SFINCS': ('sfincs-numerical-implementation.md', 'raw/source_code/sfincs/docs/overview.rst'),
    'SWAN': ('swan-documentation-stack.md', 'raw/manuals/pdfs/swantech.pdf'),
    'SWASH': ('swash-tech-documentation-overview.md', 'raw/source_code/swash/doc/swashtech.pdf'),
    'ShorelineS': ('shorelines-roelvink2020-frontiers.md', 'raw/source_code/shorelines/doc/FMarS2020_Roelvink_etal.pdf'),
    'XBeach': ('xbeach-document-discrepancies-and-version-drift.md', 'raw/source_code/trunk/doc/manual/XBeach_manual_master.pdf'),
}

def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

snapshot = json.loads(BASE.read_text())
tracked = subprocess.check_output(['git', 'ls-files', '-z'], text=True).split('\0')
notes = [p for p in tracked if p.startswith('models/') and len(Path(p).parts) >= 4
         and Path(p).parts[2] in ('source-analysis', 'manual-notes', 'web-refs')
         and p.endswith('.md') and Path(p).name != 'README.md'
         and Path(p).parts[1] in CORES]
comparisons = sorted(p for p in tracked if p.startswith('concepts/') and p.endswith('-cross-model.md'))
assert len(comparisons) == 5, comparisons
for p in notes + comparisons:
    assert p in snapshot and sha(p) == snapshot[p]['sha256'], f'Baseline changed: {p}'

def state(p):
    m = snapshot[p]['meta']
    return {
        'citation_status': m.get('citation_status', 'unknown').strip('"\''),
        'has_source_needed': m.get('has_source_needed', 'unknown').strip('"\''),
        'source_correction_human_approval': m.get('source_correction_human_approval', 'unknown').strip('"\''),
    }

models = {}
for model, roots in CORES.items():
    prefix = Path('models') / model
    core_info = []
    for name in roots:
        p = prefix / 'raw/source_code' / name
        head = None
        if (p / '.git').exists():
            head = subprocess.check_output(['git', '-c', f'safe.directory={p.resolve()}', '-C', str(p), 'rev-parse', 'HEAD'], text=True).strip()
        core_info.append({'path': str(p), 'exists': p.is_dir(), 'current_local_git_head': head,
                          'head_is_not_note_provenance_verification': True})
    model_notes = [p for p in notes if Path(p).parts[1] == model]
    anchor, doc = DOCS[model]
    anchor = str(prefix / 'manual-notes' / anchor)
    assert Path(anchor).is_file(), anchor
    doc = prefix / doc
    models[model] = {
        'source_roots': core_info,
        'manuals_directory_exists': (prefix / 'raw/manuals').is_dir(),
        'document_anchor': anchor,
        'named_original_path_check': {'path': str(doc), 'exists': doc.exists(),
                                       'kind': 'directory' if doc.is_dir() else 'file'},
        'manifest': str(prefix / 'manifest.md') if (prefix / 'manifest.md').exists() else None,
        'notes_by_folder': dict(sorted(Counter(Path(p).parts[2] for p in model_notes).items())),
        'citation_status': dict(Counter(state(p)['citation_status'] for p in model_notes)),
        'gap_flags_all_notes': dict(Counter(state(p)['has_source_needed'] for p in model_notes)),
        'unapproved_corrections': [p for p in model_notes if state(p)['source_correction_human_approval'] == 'not-issued'],
    }

# Body links only. Frontmatter related lists are not supporting claims.
# Wikilinks are resolved against tracked authored notes; ambiguous stems stay unresolved.
authored = [p for p in tracked if p.endswith('.md') and p.split('/')[0] in ('models', 'concepts', 'textbook', 'experience')
            and '/raw/' not in p and '/_archive/' not in p]
by_stem = defaultdict(list)
for p in authored:
    by_stem[Path(p).stem].append(p)

def resolve(target, origin):
    target = target.split('|')[0].split('#')[0].strip()
    if not target or re.match(r'\w+://', target):
        return []
    if '/' not in target:
        return by_stem.get(Path(target).stem, [])
    candidates = [target, posixpath.normpath(str(Path(origin).parent / target))]
    found = set()
    for c in candidates:
        if not c.endswith('.md'):
            c += '.md'
        if c in authored:
            found.add(c)
    return sorted(found)

cross = {}
for p in comparisons:
    lines = Path(p).read_text().splitlines()
    body_start = lines.index('---', 1) + 1 if lines[0] == '---' else 0
    endpoints, unresolved = defaultdict(list), []
    for number, line in enumerate(lines, 1):
        if number <= body_start:
            continue
        targets = re.findall(r'\[\[([^\]]+)\]\]', line)
        targets += re.findall(r'(?<!!)\[[^\[\]]*\]\(([^\s)]+)\)', line)
        for target in targets:
            found = resolve(target, p)
            if len(found) != 1:
                if not re.match(r'\w+://', target) and not target.startswith('#'):
                    unresolved.append({'line': number, 'target': target, 'candidates': found})
            elif found[0] in notes:
                endpoints[found[0]].append(number)
    cross[p] = {
        'own_state': state(p),
        'unique_direct_model_notes': len(endpoints),
        'unique_model_directories': len({Path(q).parts[1] for q in endpoints}),
        'dependency_gap_flags': dict(Counter(state(q)['has_source_needed'] for q in endpoints)),
        'dependency_citation_status': dict(Counter(state(q)['citation_status'] for q in endpoints)),
        'dependencies_with_unapproved_corrections': [q for q in endpoints if state(q)['source_correction_human_approval'] == 'not-issued'],
        'dependencies': {q: {'body_lines': sorted(set(numbers)), **state(q)} for q, numbers in sorted(endpoints.items())},
        'unresolved_body_links': unresolved,
    }

evidence_paths = [str(BASE), '_staging/wiki-navigation-20260913/model-state-summary.json',
    'models/AUDIT-LEDGER.md', '_staging/total-read/codex-defect-reports/PROGRESS.md',
    '_staging/total-read/model-audit/FUNWAVE/connectivity-preflight/coverage-summary.json',
    '_staging/total-read/model-audit/XBeach/connectivity/remaining-20260912/remaining.json',
    '_staging/total-read/model-audit/XBeach/connectivity/remaining-20260912/progress.json',
    'models/ADCIRC/raw/source_code/adcirc/src/timestep.F',
    'models/ADCIRC/raw/source_code/adcirc/src/read_input.F',
    'models/SWASH/raw/source_code/swash/src/SwashCheckPrep.ftn90']
evidence_paths += [f'models/{m}/README.md' for m in CORES]
evidence_paths += [x['manifest'] for x in models.values() if x['manifest']]
evidence_paths += [x['document_anchor'] for x in models.values()]
result = {
    'schema': 'coastal-model-readiness-observation/v1', 'date': '2026-09-13',
    'basis_commit': subprocess.check_output(['git', 'rev-parse', 'HEAD'], text=True).strip(),
    'scope': 'scope.md', 'semantic_read_or_human_approval_issued': False,
    'baseline_reuse': {'path': str(BASE), 'sha256': sha(BASE), 'matched_note_hashes': len(notes) + len(comparisons)},
    'model_note_count': len(notes), 'models': models, 'standalone_comparisons': cross,
    'evidence_sha256': {p: sha(p) for p in sorted(set(evidence_paths))},
}
(OUT / 'readiness.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'model_count': len(models), 'model_notes': len(notes), 'comparison_count': len(cross),
    'missing_named_documents': [m for m, x in models.items() if not x['named_original_path_check']['exists']],
    'comparisons': {p: {k: v for k, v in x.items() if k != 'dependencies'} for p, x in cross.items()}}, ensure_ascii=False, indent=2))
