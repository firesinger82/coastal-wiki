"""Validate the fixed residual inventory, never mark the XBeach goal complete."""
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[5]
CON = HERE.parent

# Required evidence is specified independently of the generator's output.
# A regenerated manifest cannot weaken its own completeness requirement.
REQUIRED_EVIDENCE = [
    'build-mode-20260912/build-map.json', 'source-read-preflight.json',
    'lifecycle/edges.json', 'lifecycle/resolution-20260912/adjudication.json',
    'physics/connectivity.json', 'physics/resolution-20260912/adjudication.json',
    'build-mode-20260912/contracts.json', 'manuals-docx-read/receipt.json',
    'manuals-docx-read/kingsday/display-fields.json', 'manuals-docx-read/master/display-fields.json',
    'nonhydro-read/cached-fields.json', 'manuals-docx-read/native-nudge-survey.json',
    'nonhydro-read/native-font-survey.json',
    'manuals-docx-read/full-visual-read/receipt.json', 'manuals-visual-read/read-receipts.json',
    'nonhydro-read/read-receipt.json', 'nonhydro-read/body-field-recovery/receipt.json',
    'manuals-preflight/summary.json', 'manuals-preflight/numeric-read/validation.json',
    'lifecycle/parallel-report-read.json', 'resume-reconciliation.json',
    'infiltration-document-code-comparison.json', 'physics/resolution-20260912/review-response.json',
    'lifecycle/resolution-20260912/review-response.json', 'build-mode-20260912/review-response.json',
    'nonhydro-read/stress-tensor-symbol/receipt.json', 'nonhydro-read/solitary-wave-symbols/receipt.json',
]


def read(p):
    return json.loads(p.read_text())


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def bind(row):
    assert sha(ROOT / row['path']) == row['sha256'], row['path']


def main():
    manifest = read(HERE / 'input-bindings.json')
    source = read(HERE / 'source-reuse.json')
    required = {str((CON / rel).relative_to(ROOT)) for rel in REQUIRED_EVIDENCE}
    required.add('_staging/total-read/model-audit/XBeach/closure/immutable-baseline.json')
    required.update(row['path'] for row in source['canonical_notes'])
    actual = [row['path'] for row in manifest['inputs']]
    assert len(actual) == len(set(actual)), 'duplicate input bindings'
    assert set(actual) == required, ('required evidence binding set differs',
                                     sorted(required - set(actual)), sorted(set(actual) - required))
    for row in manifest['inputs']:
        bind(row)
    build = read(CON / 'build-mode-20260912/build-map.json')
    old = {r['path']: r for r in read(CON / 'source-read-preflight.json')['files']}
    assert {r['path']: r['sha256'] for r in source['files']} == {r['path']: r['sha256'] for r in build['src_files']}
    receipts = set()
    for row in source['files']:
        path = ROOT / build['source_root'] / row['path']
        assert sha(path) == row['sha256'], path
        prior = old['trunk/' + row['path']]
        assert row['prior_read_status'] == prior['status']
        assert row['prior_read_receipts'] == prior['evidence']
        for receipt in row['prior_read_receipts']:
            bind(receipt)
            receipts.add(receipt['path'])
        for ref in row['canonical_filename_mentions']:
            assert path.name.lower() in (ROOT / ref).read_text().lower(), ref
    for row in source['canonical_notes']:
        bind(row)
    expected_notes = {str(p.relative_to(ROOT)) for folder in ['source-analysis', 'manual-notes', 'web-refs']
                      for p in (ROOT / 'models/XBeach' / folder).rglob('*.md')}
    assert expected_notes == {r['path'] for r in source['canonical_notes']}

    equations = read(HERE / 'equation-scope.json')
    for row in equations['document_sources']:
        bind(row)
    expected = {}
    for version in ['kingsday', 'master']:
        for field in read(CON / f'manuals-docx-read/{version}/display-fields.json')['fields']:
            if 'MTEqn' in str(field['code']):
                expected[f"{version}:xml:{field['start_xml_ordinal']}"] = field['display']
    for row in read(CON / 'nonhydro-read/cached-fields.json')['records']:
        if not row['nested_in_target'] and row['command'].strip().startswith('MACROBUTTON'):
            expected[f"nonhydro:word:{row['word_stream_start']}"] = row['cached_display']
    captions = equations['captions']
    assert len(captions) == len(expected) == len({c['id'] for c in captions})
    assert {c['id']: c['label_as_saved'] for c in captions} == expected
    expected_objects = {(r['document'], r['member'], r['native_sha256']) for r in read(CON / 'manuals-docx-read/native-nudge-survey.json')['records']}
    expected_objects.update(('nonhydro', '/'.join(r['stream']), r['native_sha256']) for r in read(CON / 'nonhydro-read/native-font-survey.json')['records'])
    actual_objects = {(r['document'], '/'.join(r['locator']) if isinstance(r['locator'], list) else r['locator'], r['native_sha256']) for r in equations['objects_including_inline_symbols']}
    assert actual_objects == expected_objects
    corrections = read(HERE / 'correction-evidence.json')['candidates']
    for candidate in corrections:
        for ev in candidate['evidence']:
            bind(ev)
            raw = (ROOT / ev['path']).read_bytes()
            lines = raw.split(b'\n')
            assert 1 <= ev['line_start'] <= ev['line_end'] <= len(lines) - int(raw.endswith(b'\n'))
            assert b'\n'.join(lines[ev['line_start']-1:ev['line_end']]).decode() == ev['quote_exact_utf8']
    tasks = read(HERE / 'remaining.json')
    assert [t['id'] for t in tasks['tasks']] == ['R1', 'R2', 'R3', 'R4']
    assert set(tasks['tasks'][2]['initial_correction_ids']) == {r['id'] for r in corrections}
    assert not tasks['whole_model_complete'] and not tasks['human_approval_issued']
    immutable = read(ROOT / '_staging/total-read/model-audit/XBeach/closure/immutable-baseline.json')['files']
    for name, h in immutable.items():
        assert sha(ROOT / name) == h, name
    if (HERE / 'review-response.json').exists():
        review = read(HERE / 'review-response.json')
        for row in review['reviews'] + review['reviewed_artifacts']:
            bind(row)
    result = {'status': 'PASS', 'scope': 'Fixed input sets, source/evidence bytes, exact correction citations and preserved history only',
              'fixed_tasks': 4, 'correction_candidates': len(corrections),
              'source_files': len(source['files']), 'prior_read_receipt_files': len(receipts),
              'caption_occurrences': len(captions), 'native_object_locators': len(actual_objects),
              'immutable_files_unchanged': len(immutable), 'whole_model_complete': False,
              'human_approval_issued': False}
    (HERE / 'validation.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps(result, ensure_ascii=False))


if __name__ == '__main__':
    main()
