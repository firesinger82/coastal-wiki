#!/usr/bin/env python3
"""Reconcile saved evidence after interruption; never issue a semantic/HG pass."""
import csv
import hashlib
import json
import zipfile
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    inputs = {}

    def read(name):
        path = (HERE / name).resolve()
        inputs[str(path.relative_to(ROOT))] = sha(path)
        return json.loads(path.read_text())

    baseline_path = HERE.parent / 'closure/immutable-baseline.json'
    baseline = json.loads(baseline_path.read_text())
    errors = [p for p, digest in baseline['files'].items()
              if not (ROOT / p).is_file() or sha(ROOT / p) != digest]
    assert not errors, errors
    source = read('source-read-preflight.json')
    csv_path = HERE / 'manuals-preflight/manuals-read-coverage.csv'
    inputs[str(csv_path.relative_to(ROOT))] = sha(csv_path)
    with csv_path.open() as handle:
        manuals = list(csv.DictReader(handle))
    rows = []
    for item in source['files']:
        rows.append({'path': 'models/XBeach/raw/source_code/' + item['path'],
                     'sha256': item['sha256'], 'prior_status': item['status'],
                     'evidence_status': item['status'], 'supplements': []})
    for item in manuals:
        rows.append({'path': item['path'], 'sha256': item['sha256'],
                     'prior_status': item['effective_semantic_status'],
                     'evidence_status': item['effective_semantic_status'],
                     'supplements': []})
    actual = {str(p.relative_to(ROOT)) for folder in ('source_code', 'manuals')
              for p in (ROOT / 'models/XBeach/raw' / folder).rglob('*') if p.is_file()}
    assert len(rows) == len(actual) == 543
    assert {r['path'] for r in rows} == actual
    assert all(sha(ROOT / r['path']) == r['sha256'] for r in rows)
    by_path = {r['path']: r for r in rows}

    def supplement(item, evidence, status, limitation):
        row = by_path[item['path']]
        assert row['sha256'] == item['sha256'], item['path']
        row['supplements'].append({'path': str((HERE / evidence).relative_to(ROOT)),
                                   'sha256': sha(HERE / evidence), 'limitation': limitation})
        row['evidence_status'] = status

    numeric_name = 'manuals-preflight/numeric-read/numeric-read-receipts.jsonl'
    inputs[str((HERE / numeric_name).relative_to(ROOT))] = sha(HERE / numeric_name)
    numeric = [json.loads(line) for line in (HERE / numeric_name).read_text().splitlines()]
    assert len(numeric) == 7 and len({r['path'] for r in numeric}) == 7
    for item in numeric:
        supplement(item, numeric_name, item['read_status'], item['scope'])
    report_name = 'lifecycle/parallel-report-read.json'
    report = read(report_name)
    assert {r['physical_page'] for r in report['page_records']} == set(range(1, 15))
    for item in report['source_copies']:
        supplement(item, report_name, 'saved-full-visual-read-evidence',
                   'Prior reader attribution retained; this run checks source hashes, not visual semantics.')
    font_name = 'manuals-preflight/font-resource-read.json'
    font = read(font_name)
    for item in font['sources']:
        supplement(item, font_name, 'resource-read-with-unreviewed-hinting', font['inspection'])
    workbook_name = 'namespaces-workbook-read.json'
    workbook = read(workbook_name)
    supplement(workbook, workbook_name, 'workbook-values-read-formulas-unresolved', workbook['method'])
    # Exact-byte copies can reuse evidence, with the original qualification intact.
    for row in rows:
        if row['evidence_status'] != 'unreconciled':
            continue
        donors = [r for r in rows if r['sha256'] == row['sha256']
                  and r['path'].startswith('models/XBeach/raw/manuals/')
                  and r['evidence_status'] in ('complete', 'complete-via-sha-bound-conversion')]
        if donors:
            donor = donors[0]
            row['evidence_status'] = 'exact-sha-copy-of-' + donor['evidence_status']
            row['supplements'].append({'path': str(csv_path.relative_to(ROOT)),
                                       'sha256': sha(csv_path), 'donor_path': donor['path'],
                                       'limitation': 'Reuses saved evidence only; no new semantic adjudication.'})
    # Later evidence must supersede optimistic historical conversion statuses.
    source_map_name = '../closure/document-inventory/source-map.json'
    source_map = read(source_map_name)
    x00_name = '../XBeach-X00.jsonl'
    x00_path = HERE / x00_name
    inputs[str(x00_path.resolve().relative_to(ROOT))] = sha(x00_path)
    converted_reads = {r['path']: r for r in
                       (json.loads(line) for line in x00_path.read_text().splitlines())}
    for work in source_map['works']:
        for rep in work['representations']:
            assert sha(ROOT / rep['path']) == rep['sha256']
            extract = ROOT / rep['audit_extract']
            assert sha(extract) == rep['audit_extract_sha256']
            inputs[rep['audit_extract']] = sha(extract)
            receipt = converted_reads[extract.name]
            damage = [r for r in receipt['unresolved'] if r['class'].replace('-', '_') == 'conversion_damage']
            assert damage, extract.name
            for row in rows:
                if row['sha256'] == rep['sha256']:
                    row['evidence_status'] = 'text-read-with-unresolved-equation-or-layout-loss'
                    row['supplements'].append({
                        'path': str(x00_path.resolve().relative_to(ROOT)), 'sha256': sha(x00_path),
                        'record': extract.name, 'source_map': str((HERE / source_map_name).resolve().relative_to(ROOT)),
                        'source_map_sha256': sha(HERE / source_map_name),
                        'audit_extract': rep['audit_extract'], 'audit_extract_sha256': sha(extract),
                        'limitation': damage})
    premise_name = 'physics/document-read-premise.json'
    premise = read(premise_name)
    for work in premise['documents']:
        for item in work['sources']:
            if item.get('new_visual_status') != 'physics-block-visual-read':
                continue
            limitation = ('Saved visual ranges only: ' + item['covered_pdf_physical_pages'] +
                          '. ' + item['coverage_note'])
            for copy in (item, item['exact_duplicate']):
                supplement(copy, premise_name, 'text-read-with-partial-pdf-visual-supplement', limitation)
    nonhydro_name = 'nonhydro-read/read-receipt.json'
    nonhydro = read(nonhydro_name)
    pdf = nonhydro['pdf']
    assert pdf['prior_evidence']['sha256'] == sha(HERE / premise_name)
    assert set(pdf['prior_evidence']['physical_pages']) == set(range(13, 69))
    assert set(pdf['prior_evidence']['physical_pages']) | {p['physical_page'] for p in pdf['new_page_records']} == set(range(1, 70))
    for item in pdf['new_page_records']:
        assert sha(ROOT / item['path']) == item['sha256']
    for item in pdf['sources']:
        assert item['sha256'] == pdf['prior_evidence']['source_sha256']
        supplement(item, nonhydro_name, pdf['read_status'], pdf['limitations'])
    doc = nonhydro['doc']
    assert {p['physical_render_page'] for p in doc['page_records']} == set(range(1, 71))
    for item in doc['page_records'] + [doc['render_pdf'], doc['container_inventory']]:
        assert sha(ROOT / item['path']) == item['sha256']
    supplement(doc, nonhydro_name, doc['read_status'], doc['limitations'])
    recovery_name = 'nonhydro-read/field-recovery/receipt.json'
    recovery = read(recovery_name)
    for item in recovery['artifacts'] + [recovery['field_evidence'], recovery['recovery_script']]:
        assert sha(ROOT / item['path']) == item['sha256']
    supplement(recovery['source'], recovery_name, doc['read_status'], recovery['remaining'])
    body_name = 'nonhydro-read/body-field-recovery/receipt.json'
    body = read(body_name)
    assert body['prior_recovery']['sha256'] == sha(HERE / recovery_name)
    assert {p['physical_render_page'] for p in body['page_records']} == set(range(1, 72))
    for item in body['artifacts'] + [body['recovery_script'], body['footer_contact_sheet']]:
        assert sha(ROOT / item['path']) == item['sha256']
    for page in body['page_records']:
        for key in ('read_intermediate_image', 'final_image'):
            assert sha(ROOT / page[key]['path']) == page[key]['sha256']
    supplement(body['source'], body_name, body['read_status'], body['remaining'])
    manual_name = 'manuals-visual-read/read-receipts.json'
    manual_visual = read(manual_name)
    for item in manual_visual['records']:
        prior = item['prior_evidence']
        assert prior['sha256'] == sha(HERE / premise_name)
        old = set(prior['physical_pages'])
        new = {p['physical_page'] for p in item['new_page_records']}
        assert not old & new
        assert old | new == set(range(1, item['pdf_physical_pages_total'] + 1))
        for page in item['new_page_records'] + item['extra_visuals']:
            assert sha(ROOT / page['path']) == page['sha256']
        for copy in item['sources']:
            assert copy['sha256'] == prior['source_sha256']
            supplement(copy, manual_name, item['read_status'], item['limitations'])
    docx_name = 'manuals-docx-read/receipt.json'
    docx_review = read(docx_name)
    for item in docx_review['records']:
        for artifact in [item['container_inventory'], item['display_fields']]:
            assert sha(ROOT / artifact['path']) == artifact['sha256']
        for variant in item['variants']:
            pages = variant['visually_inspected_pages']
            assert [p['physical_render_page'] for p in variant['page_records']] == pages
            assert set(pages).isdisjoint(variant['uninspected_pages'])
            assert set(pages + variant['uninspected_pages']) == set(range(1, variant['render_pages'] + 1))
            for artifact in list(variant['artifacts'].values()) + variant['page_records']:
                assert sha(ROOT / artifact['path']) == artifact['sha256']
        supplement(item['source'], docx_name, item['read_status'], item['limitations'])
    for artifact in list(docx_review['equation_preview_supplement']['artifacts'].values()) + [
            docx_review['recovery_script'], docx_review['controls_only_script']]:
        assert sha(ROOT / artifact['path']) == artifact['sha256']
    full_docx_name = 'manuals-docx-read/full-visual-read/receipt.json'
    full_docx = read(full_docx_name)
    assert full_docx['prior_receipt']['sha256'] == sha(HERE / docx_name)
    assert full_docx['whole_model_read_gate'] == 'NOT_PASSED'
    assert full_docx['human_approval_issued'] is False
    for item, prior in zip(full_docx['records'], docx_review['records'], strict=True):
        final = prior['variants'][-1]
        assert item['source'] == prior['source']
        assert item['render_pdf'] == final['artifacts']['pdf']
        assert item['render_pages'] == final['render_pages']
        assert item['prior_inspected_pages'] == final['visually_inspected_pages']
        assert item['newly_inspected_pages'] == final['uninspected_pages']
        assert [p['physical_render_page'] for p in item['page_records']] == item['newly_inspected_pages']
        assert sorted(item['prior_inspected_pages'] + item['newly_inspected_pages']) == item['combined_inspected_pages'] == list(range(1, item['render_pages'] + 1))
        assert not item['uninspected_pages']
        assert sorted(p for n in item['observations'] for p in n['physical_render_pages']) == item['newly_inspected_pages']
        for artifact in item['page_records'] + [item['rotated_diagram']]:
            assert sha(ROOT / artifact['path']) == artifact['sha256']
        supplement(item['source'], full_docx_name, item['read_status'], item['limitations'])
    for item in full_docx['equation_supplements']:
        assert sha(ROOT / item['source']['path']) == item['source']['sha256']
        for artifact in item['artifacts'].values():
            assert sha(ROOT / artifact['path']) == artifact['sha256']
    for item in full_docx['source_empty_paragraphs']:
        artifact = item['artifact']
        assert sha(ROOT / artifact['path']) == artifact['sha256']
    native_name = 'manuals-docx-read/native-probe/receipt.json'
    native = read(native_name)
    assert native['whole_model_read_gate'] == 'NOT_PASSED' and native['human_approval_issued'] is False
    for artifact in [native['prior_visual_receipt'], native['decoder'], native['viewed_contact_sheet']]:
        assert sha(ROOT / artifact['path']) == artifact['sha256']
    for item in native['empty_native_records'] + native['preview_records']:
        assert sha(ROOT / item['source']['path']) == item['source']['sha256']
        for artifact in item['artifacts'].values():
            assert sha(ROOT / artifact['path']) == artifact['sha256']
    for item in full_docx['records']:
        supplement(item['source'], native_name, item['read_status'], native['limitations'])
    glyph_name = 'manuals-docx-read/glyph-record-read/receipt.json'
    glyph = read(glyph_name)
    assert glyph['whole_model_read_gate'] == 'NOT_PASSED' and glyph['human_approval_issued'] is False
    for artifact in [glyph['prior_receipt'], glyph['decoder'], glyph['prefix_decoder']]:
        assert sha(ROOT / artifact['path']) == artifact['sha256']
    for item in glyph['records']:
        assert sha(ROOT / item['source']['path']) == item['source']['sha256']
        for artifact in item['artifacts'].values():
            assert sha(ROOT / artifact['path']) == artifact['sha256']
    for item in full_docx['records']:
        supplement(item['source'], glyph_name, item['read_status'], glyph['limitations'])
    survey_name = 'manuals-docx-read/native-survey.json'
    survey = read(survey_name)
    for artifact in [survey['decoder'], survey['prefix_decoder']]:
        assert sha(ROOT / artifact['path']) == artifact['sha256']
    for item in full_docx['records']:
        supplement(item['source'], survey_name, item['read_status'], survey['limitations'])
    prefix_name = 'manuals-docx-read/native-prefix-survey.json'
    prefix_survey = read(prefix_name)
    for key in ('prior_receipt', 'generator', 'prefix_decoder', 'body_decoder'):
        artifact = prefix_survey[key]
        assert sha(ROOT / artifact['path']) == artifact['sha256']
    for item in full_docx['records']:
        supplement(item['source'], prefix_name, item['read_status'], prefix_survey['limitations'])
    embell_name = 'manuals-docx-read/native-embell-survey.json'
    embell = read(embell_name)
    for key in ('prior_receipt', 'generator', 'decoder'):
        artifact = embell[key]
        assert sha(ROOT / artifact['path']) == artifact['sha256']
    for item in full_docx['records']:
        supplement(item['source'], embell_name, item['read_status'], embell['limitations'])
    layout_name = 'manuals-docx-read/native-layout-survey.json'
    layout = read(layout_name)
    for key in ('prior_receipt', 'generator', 'decoder'):
        artifact = layout[key]
        assert sha(ROOT / artifact['path']) == artifact['sha256']
    for item in full_docx['records']:
        supplement(item['source'], layout_name, item['read_status'], layout['limitations'])
    nudge_name = 'manuals-docx-read/native-nudge-survey.json'
    nudge = read(nudge_name)
    for key in ('prior_receipt', 'generator', 'decoder'):
        artifact = nudge[key]
        assert sha(ROOT / artifact['path']) == artifact['sha256']
    for item in full_docx['records']:
        supplement(item['source'], nudge_name, item['read_status'], nudge['limitations'])
    future_name = 'manuals-docx-read/native-future-probe.json'
    future = read(future_name)
    for key in ('prior_receipt', 'generator', 'prefix_decoder', 'body_decoder'):
        artifact = future[key]
        assert sha(ROOT / artifact['path']) == artifact['sha256']
    master = next(item for item in full_docx['records'] if 'master' in item['source']['path'])
    supplement(master['source'], future_name, master['read_status'], ['Three bodies parsed; FUTURE payload semantics unresolved.'])
    report_name = 'nonhydro-read/native-survey.json'
    report = read(report_name)
    supplement(report['source'], report_name, 'all-render-pages-inspected-with-unresolved-rendering-fidelity', [report['scope']])
    font_name = 'nonhydro-read/native-font-survey.json'
    fonts = read(font_name)
    for key in ('prior_receipt', 'generator', 'prefix_decoder', 'body_decoder', 'candidate_finder'):
        artifact = fonts[key]
        assert sha(ROOT / artifact['path']) == artifact['sha256']
    supplement(fonts['source'], font_name, 'all-render-pages-inspected-with-unresolved-rendering-fidelity', [fonts['scope']])
    conditional_name = 'manuals-docx-read/native-conditional-probe.json'
    conditional = read(conditional_name)
    for key in ('prior_receipt', 'decoder', 'generator'):
        artifact = conditional[key]
        assert sha(ROOT / artifact['path']) == artifact['sha256']
    for item in full_docx['records']:
        supplement(item['source'], conditional_name, item['read_status'], ['20 conditional structures retain unresolved source exceptions.'])
    visual_name = 'manuals-docx-read/conditional-visual-read/receipt.json'
    visual = read(visual_name)
    for item in full_docx['records']:
        supplement(item['source'], visual_name, item['read_status'], visual['limitations'])
    comparison = read('infiltration-document-code-comparison.json')
    assert sha(ROOT / comparison['source']['path']) == comparison['source']['sha256']
    assert sha(ROOT / comparison['visual_receipt']['path']) == comparison['visual_receipt']['sha256']
    read('bytecode-read/disassembly-receipt.json')
    read('bytecode-read/launcher-read.json')
    read('bytecode-read/base-io-read.json')
    read('bytecode-read/slog2-header-read.json')
    read('bytecode-read/slog2-node-read.json')
    read('bytecode-read/slog2-iteration-read.json')
    read('bytecode-read/time-coord-read.json')
    read('bytecode-read/drawable-order-read.json')
    read('bytecode-read/infobox-read.json')
    read('bytecode-read/info-value-read.json')
    read('bytecode-read/nesting-drawn-read.json')
    read('bytecode-read/drawable-buffer-read.json')
    read('bytecode-read/lineid-method-read.json')
    read('bytecode-read/ycoord-read.json')
    read('bytecode-read/shadow-buffer-read.json')
    read('bytecode-read/shadow-read.json')
    read('bytecode-read/category-weight-read.json')
    read('bytecode-read/primitive-read.json')
    read('bytecode-read/composite-read.json')
    read('bytecode-read/output-node-read.json')
    read('bytecode-read/output-flow-read.json')
    read('bytecode-read/clog2-converter-read.json')
    read('bytecode-read/clog-converter-read.json')
    read('bytecode-read/input-kind-read.json')
    read('bytecode-read/trace-converter-read.json')
    read('bytecode-read/trace-input-read.json')
    read('bytecode-read/clog2-input-shell-read.json')
    read('bytecode-read/clog2-content-read.json')
    read('bytecode-read/clog2-matching-read.json')
    read('bytecode-read/clog2-idmap-read.json')
    read('bytecode-read/clog2-record-input-read.json')
    read('bytecode-read/clog2-stream-read.json')
    read('bytecode-read/clog2-comm-read.json')
    read('bytecode-read/clog2-skipped-records-read.json')
    read('bytecode-read/clog2-definitions-read.json')
    read('bytecode-read/clog2-event-color-read.json')
    read('bytecode-read/color-alpha-read.json')
    read('bytecode-read/category-read.json')
    read('bytecode-read/clog2-print-read.json')
    read('bytecode-read/clog2-print-onepass-read.json')
    read('bytecode-read/clog2-print-twopass-read.json')
    read('bytecode-read/lowlevel-print-read.json')
    read('bytecode-read/basic-topology-read.json')
    read('bytecode-read/state-border-read.json')
    read('bytecode-read/preview-event-read.json')
    read('bytecode-read/arrow-render-read.json')
    read('bytecode-read/summary-arrow-read.json')
    read('bytecode-read/summary-state-read.json')
    read('bytecode-read/category-timebox-read.json')
    read('bytecode-read/timeave-box-read.json')
    read('bytecode-read/float-statistics-read.json')
    read('bytecode-read/timeave-buffer-read.json')
    read('bytecode-read/preview-state-read.json')
    read('bytecode-read/input-helpers-read.json')
    read('bytecode-read/input-treenode-read.json')
    read('bytecode-read/input-treefloor-read.json')
    read('bytecode-read/coverage.json')
    formula_name = 'workbook-formula-read.json'
    if (HERE / formula_name).is_file():
        formula = read(formula_name)
        supplement(formula, formula_name, 'workbook-values-and-formula-read', formula['interpretation'])
    office_name = 'office-read/read-receipts.json'
    if (HERE / office_name).is_file():
        office = read(office_name)
        for item in office['records']:
            assert {r['physical_render_page'] for r in item['render_evidence']} == set(range(1, item['render_pages'] + 1))
            for artifact in item['render_evidence']:
                assert sha(ROOT / artifact['path']) == artifact['sha256']
            supplement(item, office_name, item['read_status'], item['container_scope'])
    jumpshot_name = 'jumpshot-pdf-read/read-receipt.json'
    if (HERE / jumpshot_name).is_file():
        jumpshot = read(jumpshot_name)
        assert {r['physical_page'] for r in jumpshot['page_records']} == set(range(1, 62))
        for artifact in jumpshot['page_records']:
            assert sha(ROOT / artifact['render_path']) == artifact['render_sha256']
        supplement(jumpshot, jumpshot_name, jumpshot['read_status'], jumpshot['limitations'])
    archives = read('archive-content-inventory.json')
    member_count = 0
    member_statuses = Counter()
    for archive in archives['archives']:
        path = ROOT / 'models/XBeach/raw/source_code' / archive['path']
        assert sha(path) == archive['sha256']
        with zipfile.ZipFile(path) as handle:
            assert Counter(handle.namelist()) == Counter(m['path'] for m in archive['members'])
            for member in archive['members']:
                data = handle.read(member['path'])
                assert len(data) == member['bytes']
                assert hashlib.sha256(data).hexdigest() == member['sha256']
                member_count += 1
                member_statuses[member['semantic_status']] += 1
    result = {
        'date': '2026-09-11',
        'scope': '543 top-level files only; recursive container members remain separate inventories.',
        'validation': {'path_set_exact': True, 'source_hashes_checked': len(rows),
                       'immutable_files_checked': len(baseline['files']), 'immutable_errors': errors,
                       'baseline_sha256': sha(baseline_path)},
        'input_evidence_sha256': inputs,
        'archive_validation': {'archives_checked': len(archives['archives']),
                               'member_instances_hashed': member_count,
                               'saved_semantic_status_counts': dict(member_statuses),
                               'scope': 'Listed ZIP/JAR inventories only; MSI recursion not validated here.'},
        'status_counts': dict(Counter(r['evidence_status'] for r in rows)),
        'supplemented_paths': sum(bool(r['supplements']) for r in rows),
        'whole_model_read_gate': 'NOT_PASSED',
        'human_approval_issued': False,
        'limitations': ['Saved claims are not independently re-read by this reconciliation.',
                       'No artifact-only, bytecode, hinting, or missing-formula evidence is promoted to complete.',
                       'No new equivalence is inferred from filenames or document titles.'],
        'files': rows,
    }
    (HERE / 'resume-reconciliation.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({k: v for k, v in result.items() if k not in ('files', 'input_evidence_sha256')}, ensure_ascii=False))


if __name__ == '__main__':
    main()
