"""Inventory existing XBeach evidence for a fixed residual plan, never award completion.

No source/Office decoding, compilation, numerical validation or semantic re-read.
Input hashes bind this reconciliation to the already reviewed snapshot.
"""
import collections
import hashlib
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[5]
CON = HERE.parent
SRC = ROOT / 'models/XBeach/raw/source_code/trunk'


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def binding(p):
    return {'path': str(p.relative_to(ROOT)), 'sha256': sha(p)}


def read(p):
    return json.loads(p.read_text())


def save(name, data):
    (HERE / name).write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')


def paths_in(obj):
    """Discover explicit source locators, not infer call-graph coverage."""
    if isinstance(obj, dict):
        for k, v in obj.items():
            if k == 'path' and isinstance(v, str):
                yield v
            yield from paths_in(v)
    elif isinstance(obj, list):
        for value in obj:
            yield from paths_in(value)


def main():
    inputs = []

    def ledger(rel):
        p = CON / rel
        inputs.append(binding(p))
        return read(p)

    build = ledger('build-mode-20260912/build-map.json')
    preflight = ledger('source-read-preflight.json')
    old_reads = {r['path']: r for r in preflight['files']}
    # Avoid treating a source filename mentioned in an existing note as a review.
    notes = sorted(p for folder in ['source-analysis', 'manual-notes', 'web-refs']
                   for p in (ROOT / 'models/XBeach' / folder).rglob('*.md'))
    note_text = {str(p.relative_to(ROOT)): p.read_text() for p in notes}
    canonical = []
    for p in notes:
        s = p.read_text()
        status = re.search(r'^citation_status:\s*(.+)$', s, re.M)
        canonical.append({**binding(p), 'citation_status': status[1] if status else None})
    sources_in_ledgers = {}
    reused = {}
    for rel in ['lifecycle/edges.json', 'lifecycle/resolution-20260912/adjudication.json',
                'physics/connectivity.json', 'physics/resolution-20260912/adjudication.json',
                'build-mode-20260912/contracts.json']:
        obj = ledger(rel)
        reused[rel] = obj
        sources_in_ledgers[rel] = set(paths_in(obj))

    src_records = []
    for f in build['src_files']:
        raw = SRC / f['path']
        assert sha(raw) == f['sha256'], f['path']
        prior = old_reads['trunk/' + f['path']]
        assert prior['sha256'] == f['sha256'], f['path']
        references = [rel for rel, paths in sources_in_ledgers.items()
                      if f['path'] in paths or str(raw.relative_to(ROOT)) in paths]
        mentions = [rel for rel, s in note_text.items()
                    if raw.name.lower() in s.lower()]
        src_records.append({**f, 'prior_read_status': prior['status'],
                            'prior_read_receipts': prior['evidence'],
                            'existing_ledger_mentions': references,
                            'canonical_filename_mentions': mentions,
                            'coverage_interpretation': 'Reusable locators only; no automatic all-routine/guard coverage judgment'})

    # Retain version, physical XML/Word location and occurrence. Labels are not IDs:
    # Master repeats 2.110; the report repeats labels 2.1..2.11 in another section.
    captions = []
    document_sources = []
    manual_receipt = ledger('manuals-docx-read/receipt.json')
    source_by_version = {r['work_id'].removeprefix('XBeach-manual-'): r['source']
                         for r in manual_receipt['records']}
    for version in ['kingsday', 'master']:
        source = source_by_version[version]
        assert sha(ROOT / source['path']) == source['sha256']
        document_sources.append(source)
        rel = f'manuals-docx-read/{version}/display-fields.json'
        fields = ledger(rel)
        assert fields['source_sha256'] == source['sha256']
        for field in fields['fields']:
            if 'MTEqn' not in str(field['code']):
                continue
            label = field['display']
            loc = field['start_xml_ordinal']
            selected = label in [f'(2.{i})' for i in range(5, 11)] + ['(B.37)', '(C.37)']
            captions.append({'id': f'{version}:xml:{loc}', 'document': version,
                             'label_as_saved': label, 'locator_kind': 'start_xml_ordinal',
                             'locator': loc, 'field_evidence': str((CON / rel).relative_to(ROOT)),
                             'existing_bounded_contract': 'build-mode-20260912/contracts.json' if selected else None,
                             'residual_action': 'reuse_bounded_equation_contract' if selected else 'reconcile_existing_evidence_before_any_reread'})
    cached = ledger('nonhydro-read/cached-fields.json')
    nonh_source = {'path': cached['source_path'], 'sha256': cached['source_sha256']}
    assert sha(ROOT / nonh_source['path']) == nonh_source['sha256']
    document_sources.append(nonh_source)
    for row in cached['records']:
        if row['nested_in_target'] or not row['command'].strip().startswith('MACROBUTTON'):
            continue
        captions.append({'id': f"nonhydro:word:{row['word_stream_start']}", 'document': 'nonhydro',
                         'label_as_saved': row['cached_display'], 'locator_kind': 'word_stream_byte_offset',
                         'locator': row['word_stream_start'], 'raw_field_sha256': row['raw_field_sha256'],
                         'field_evidence': str((CON / 'nonhydro-read/cached-fields.json').relative_to(ROOT)),
                         'existing_bounded_contract': None,
                         'residual_action': 'reconcile_existing_evidence_before_any_reread'})
    assert len({c['id'] for c in captions}) == len(captions)
    # Existing object inventories include inline symbols. They are NOT 874 new tasks.
    manual_native = ledger('manuals-docx-read/native-nudge-survey.json')
    nonh_native = ledger('nonhydro-read/native-font-survey.json')
    objects = [{'document': r['document'], 'locator': r['member'],
                'native_sha256': r['native_sha256']} for r in manual_native['records']]
    objects += [{'document': 'nonhydro', 'locator': r['stream'],
                 'native_sha256': r['native_sha256']} for r in nonh_native['records']]
    save('source-reuse.json', {'scope': 'Fixed model src file set and reusable evidence locators',
                             'files': src_records, 'canonical_notes': canonical})
    save('equation-scope.json', {'scope': 'Existing numbered-caption occurrences and Native inventory locators; neither unique mathematical equations nor unread/defect counts',
                                'document_sources': document_sources, 'captions': captions,
                                'objects_including_inline_symbols': objects,
                                'policy': 'Reuse full visual reads, XH001..207 dispositions, prior contracts and original images. Relate inline symbols to their surrounding contract. Same number/hash alone does not establish semantic equivalence across versions. Missing author intent or formatting is a documented limit, not a mandate to repair fonts or investigate tools.'})
    # Governance evidence is historical. Check only its immutable hashes, not old
    # installed snapshots that intentionally predate today's canonical corrections.
    baseline_path = ROOT / '_staging/total-read/model-audit/XBeach/closure/immutable-baseline.json'
    baseline = read(baseline_path)
    for name, h in baseline['files'].items():
        assert sha(ROOT / name) == h, name
    inputs.append(binding(baseline_path))
    for f in canonical:
        inputs.append(f)
    for rel in ['manuals-docx-read/full-visual-read/receipt.json',
                'manuals-visual-read/read-receipts.json', 'nonhydro-read/read-receipt.json',
                'nonhydro-read/body-field-recovery/receipt.json', 'manuals-preflight/summary.json',
                'manuals-preflight/numeric-read/validation.json', 'lifecycle/parallel-report-read.json',
                'resume-reconciliation.json', 'infiltration-document-code-comparison.json',
                'physics/resolution-20260912/review-response.json',
                'lifecycle/resolution-20260912/review-response.json',
                'build-mode-20260912/review-response.json',
                'nonhydro-read/stress-tensor-symbol/receipt.json',
                'nonhydro-read/solitary-wave-symbols/receipt.json']:
        p = CON / rel
        if str(p.relative_to(ROOT)) not in {r['path'] for r in inputs}:
            inputs.append(binding(p))
    save('input-bindings.json', {'basis_commit': 'cd8c769', 'inputs': inputs})
    compiled = [f for f in src_records if f['role'] == 'compiled_fortran_unit']
    summary = {
        'source_files': len(src_records), 'compiled_fortran_units': len(compiled),
        'compiled_unit_prior_read_states': dict(collections.Counter(f['prior_read_status'] for f in compiled)),
        'wrapper_files': [f['path'] for f in src_records if f['role'] == 'python_wrapper'],
        'canonical_notes': len(canonical),
        'new_draft_notes': [x['path'] for x in canonical if x['citation_status'] == 'draft-unsourced'],
        'lifecycle_contracts_with_adjudications': len(reused['lifecycle/resolution-20260912/adjudication.json']['findings']),
        'physics_candidates_with_adjudications': len(reused['physics/resolution-20260912/adjudication.json']['findings']),
        'caption_occurrences_by_document': dict(collections.Counter(x['document'] for x in captions)),
        'caption_label_duplicates_by_document': {v: {label: n for label, n in collections.Counter(x['label_as_saved'] for x in captions if x['document'] == v).items() if n > 1} for v in ['kingsday', 'master', 'nonhydro']},
        'caption_occurrences_with_selected_equation_contract': sum(x['existing_bounded_contract'] is not None for x in captions),
        'object_locator_counts_by_document': dict(collections.Counter(x['document'] for x in objects)),
        'immutable_history_files_unchanged': len(baseline['files']),
        'meaning': 'Evidence reconciliation input sizes. No remaining-error count, completion percentage, all-routine coverage, or human approval inferred.'}
    save('inventory-summary.json', summary)
    print(json.dumps(summary, ensure_ascii=False))


if __name__ == '__main__':
    main()
