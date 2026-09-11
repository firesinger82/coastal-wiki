#!/usr/bin/env python3
"""Check persisted supplemental evidence; this is not a semantic read gate."""
import hashlib
import json
from pathlib import Path
import zipfile
import olefile
import importlib.util
import re
import tempfile
import subprocess
from collections import Counter
from PIL import Image, ImageChops
from lxml import etree

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    checks = []

    def check(label, value):
        checks.append({'check': label, 'pass': bool(value)})

    office = json.loads((HERE / 'office-read/read-receipts.json').read_text())
    check('five-office-records', len(office['records']) == 5)
    check('office-page-total-36', sum(r['render_pages'] for r in office['records']) == 36)
    for record in office['records']:
        source = ROOT / record['path']
        check(record['path'] + ':source-sha', digest(source) == record['sha256'])
        actual = {}
        if zipfile.is_zipfile(source):
            with zipfile.ZipFile(source) as handle:
                for member in handle.infolist():
                    data = handle.read(member)
                    actual[member.filename] = (len(data), hashlib.sha256(data).hexdigest())
                check(record['path'] + ':no-duplicate-zip-member-paths', len(actual) == len(handle.infolist()))
        else:
            with olefile.OleFileIO(source) as handle:
                for member in handle.listdir():
                    data = handle.openstream(member).read()
                    actual['/'.join(member)] = (len(data), hashlib.sha256(data).hexdigest())
        expected = {r['path']: (r['bytes'], r['sha256']) for r in record['container_members']}
        check(record['path'] + ':container-set-size-sha', actual == expected)
        pages = record['render_evidence']
        check(record['path'] + ':page-set', len(pages) == record['render_pages'] and
              {r['physical_render_page'] for r in pages} == set(range(1, record['render_pages'] + 1)))
        check(record['path'] + ':page-image-hashes', all(digest(ROOT / r['path']) == r['sha256'] for r in pages))
    for artifact in office['supplementary_evidence']:
        if 'path' in artifact:
            check(artifact['path'], digest(ROOT / artifact['path']) == artifact['sha256'])
    jumpshot = json.loads((HERE / 'jumpshot-pdf-read/read-receipt.json').read_text())
    check('jumpshot-source', digest(ROOT / jumpshot['path']) == jumpshot['sha256'])
    check('jumpshot-page-set-61', len(jumpshot['page_records']) == 61 and
          {r['physical_page'] for r in jumpshot['page_records']} == set(range(1, 62)))
    check('jumpshot-page-hashes', all(digest(ROOT / r['render_path']) == r['render_sha256'] for r in jumpshot['page_records']))
    vba = json.loads((HERE / 'office-read/members/vba-source-read.json').read_text())
    check('vba-source', digest(ROOT / vba['path']) == vba['sha256'])
    check('vba-extract', all(digest(ROOT / r['extraction']) == r['extraction_sha256'] for r in vba['modules']))
    workbook = json.loads((HERE / 'workbook-formula-read.json').read_text())
    check('workbook-source', digest(ROOT / workbook['path']) == workbook['sha256'])
    with olefile.OleFileIO(ROOT / workbook['path']) as handle:
        stream = handle.openstream('Workbook').read()
    f1 = workbook['F1_record']
    body = bytes.fromhex(f1['body_hex'])
    check('F1-literal-record', stream[f1['byte_offset']:f1['byte_offset'] + 4 + len(body)] ==
          b'\x7e\x02' + len(body).to_bytes(2, 'little') + body)
    for formula in workbook['formula_records']:
        pos = formula['byte_offset']
        tokens = bytes.fromhex(formula['tokens_hex'])
        check('E1-formula-tokens', stream[pos:pos + 2] == b'\x06\x00' and stream[pos + 26:pos + 26 + len(tokens)] == tokens)
    recovery = json.loads((HERE / 'msi-recovery.json').read_text())
    check('MSI-inventory-binding', digest(HERE / 'msi-content-inventory.json') == recovery['inventory_sha256'])
    check('MSI-member-count-123', sum(len(r['members']) for r in recovery['archives']) == 123)
    for archive in recovery['archives']:
        check(archive['path'], digest(ROOT / archive['path']) == archive['sha256'])
        for member in archive['members']:
            path = Path(member['scratch_path'])
            check(archive['path'] + ':' + member['name'], path.is_file() and digest(path) == member['sha256'])
    interfaces = json.loads((HERE / 'msi-interface-review.json').read_text())
    check('MSI-interface-recovery-binding', digest(HERE / 'msi-recovery.json') == interfaces['inventory_sha256'])
    check('MSI-interface-set', {(r['archive'], r['member_id']) for r in interfaces['members']} ==
          {(a['path'], r['id']) for a in recovery['archives'] for r in a['members'] if r['interface_extraction'] is not None})
    check('MSI-interface-artifacts', all(digest(HERE / r['evidence_file']) == r['evidence_sha256'] for r in interfaces['members']))
    nonhydro = json.loads((HERE / 'nonhydro-read/read-receipt.json').read_text())
    pdf = nonhydro['pdf']
    prior = pdf['prior_evidence']
    check('nonhydro-prior-binding', digest(ROOT / prior['path']) == prior['sha256'])
    premise = json.loads((ROOT / prior['path']).read_text())
    saved_source = next(s for w in premise['documents'] for s in w['sources']
                        if s.get('covered_pdf_physical_pages') == '13-68 inclusive')
    check('nonhydro-prior-source-and-range', saved_source['sha256'] == prior['source_sha256'] and
          prior['physical_pages'] == list(range(13, 69)))
    check('nonhydro-pdf-sources', all(digest(ROOT / s['path']) == s['sha256'] == prior['source_sha256'] for s in pdf['sources']))
    new = pdf['new_page_records']
    check('nonhydro-new-pages-13', len(new) == 13 and {p['physical_page'] for p in new} == set(range(1, 13)) | {69})
    check('nonhydro-combined-pages-69', set(prior['physical_pages']) | {p['physical_page'] for p in new} ==
          set(pdf['combined_physical_pages']) == set(range(1, 70)))
    check('nonhydro-pdf-images', all(digest(ROOT / p['path']) == p['sha256'] for p in new))
    doc = nonhydro['doc']
    check('nonhydro-doc-source', digest(ROOT / doc['path']) == doc['sha256'])
    check('nonhydro-doc-pages-70', len(doc['page_records']) == 70 and
          {p['physical_render_page'] for p in doc['page_records']} == set(range(1, 71)))
    check('nonhydro-doc-artifacts', all(digest(ROOT / p['path']) == p['sha256']
          for p in doc['page_records'] + [doc['render_pdf'], doc['container_inventory']]))
    inventory = json.loads((ROOT / doc['container_inventory']['path']).read_text())
    with olefile.OleFileIO(ROOT / doc['path']) as handle:
        actual = {}
        for member in handle.listdir():
            data = handle.openstream(member).read()
            actual['/'.join(member)] = (len(data), hashlib.sha256(data).hexdigest())
    check('nonhydro-doc-container', actual == {p['path']: (p['bytes'], p['sha256']) for p in inventory['streams']})
    check('nonhydro-doc-fidelity-remains-open', doc['read_status'] == 'all-render-pages-inspected-with-unresolved-rendering-fidelity' and
          doc['equation_native_streams'] == sum(p.endswith('/Equation Native') for p in actual))
    repair = json.loads((HERE / 'nonhydro-read/field-recovery/receipt.json').read_text())
    check('field-repair-artifacts', all(digest(ROOT / p['path']) == p['sha256']
          for p in repair['artifacts'] + [repair['field_evidence'], repair['recovery_script']]))
    spec = importlib.util.spec_from_file_location('nonhydro_cached_fields', ROOT / repair['recovery_script']['path'])
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    recovered = module.extract()
    check('field-repair-source-reextraction', recovered == json.loads((ROOT / repair['field_evidence']['path']).read_text()))
    folder = HERE / 'nonhydro-read/field-recovery'
    with zipfile.ZipFile(folder / 'converted.docx') as before, zipfile.ZipFile(folder / 'cached-field-restored.docx') as after:
        check('field-repair-other-members-unchanged', before.namelist() == after.namelist() and
              all(before.read(n) == after.read(n) for n in before.namelist() if n != 'word/document.xml'))
    with tempfile.TemporaryDirectory(prefix='nonhydro-field-check-') as scratch:
        rebuilt = Path(scratch) / 'restored.docx'
        module.restore(folder / 'converted.docx', rebuilt, recovered)
        with zipfile.ZipFile(rebuilt) as expected_zip, zipfile.ZipFile(folder / 'cached-field-restored.docx') as saved_zip:
            check('field-repair-reproducible-document-xml', expected_zip.namelist() == saved_zip.namelist() and
                  all(expected_zip.read(n) == saved_zip.read(n) for n in expected_zip.namelist()))
    expected = Counter(r['cached_display'] for r in recovered['records']
                       if not r['nested_in_target'] and r['cached_display'])
    observed = Counter(re.findall(r'\([1-3C]\.\d+\)', (folder / 'cached-field-restored.txt').read_text()))
    check('field-repair-rendered-cache-counts', not expected - observed)
    check('field-repair-no-gate-pass', repair['whole_model_read_gate'] == 'NOT_PASSED' and repair['human_approval_issued'] is False)
    body = json.loads((HERE / 'nonhydro-read/body-field-recovery/receipt.json').read_text())
    check('body-freeze-provenance', all(digest(ROOT / r['path']) == r['sha256'] for r in
          [body['source'], body['prior_recovery'], body['input_docx'], body['recovery_script']]))
    check('body-freeze-artifacts', all(digest(ROOT / r['path']) == r['sha256'] for r in
          body['artifacts'] + [body['footer_contact_sheet']]))
    body_folder = HERE / 'nonhydro-read/body-field-recovery'
    spec = importlib.util.spec_from_file_location('nonhydro_body_fields', ROOT / body['recovery_script']['path'])
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    with tempfile.TemporaryDirectory(prefix='nonhydro-body-check-') as scratch:
        rebuilt = Path(scratch) / 'body.docx'
        removed = module.freeze(ROOT / body['input_docx']['path'], rebuilt)
        with zipfile.ZipFile(rebuilt) as a, zipfile.ZipFile(body_folder / 'body-cached.docx') as b:
            check('body-freeze-member-reproduction', a.namelist() == b.namelist() and
                  all(a.read(n) == b.read(n) for n in a.namelist()))
        check('body-freeze-removes-652-controls', removed == body['transformation']['removed_field_nodes'] == 652)
    with zipfile.ZipFile(ROOT / body['input_docx']['path']) as before, zipfile.ZipFile(body_folder / 'body-cached.docx') as after:
        check('body-freeze-preserves-all-other-members', before.namelist() == after.namelist() and
              all(before.read(n) == after.read(n) for n in before.namelist() if n != 'word/document.xml'))
        a, b = [etree.fromstring(z.read('word/document.xml')) for z in (before, after)]
        ns = {'w': module.W}
        check('body-freeze-preserves-display-runs', a.xpath('//w:t/text()', namespaces=ns) == b.xpath('//w:t/text()', namespaces=ns))
        check('body-freeze-preserves-objects', [etree.tostring(n) for n in a.xpath('//w:object', namespaces=ns)] ==
              [etree.tostring(n) for n in b.xpath('//w:object', namespaces=ns)])
        check('body-freeze-no-body-fields', not b.xpath('//w:instrText | //w:fldChar | //w:fldSimple', namespaces=ns))
        check('body-freeze-instruction-inventory', a.xpath('//w:instrText/text()', namespaces=ns) ==
              body['transformation']['instructions_before'])
    page_records = body['page_records']
    check('body-71-pages-exact', len(page_records) == 71 and {p['physical_render_page'] for p in page_records} == set(range(1, 72)))
    images_ok, bodies_ok, boxes_ok = True, True, True
    for page in page_records:
        images_ok &= all(digest(ROOT / page[k]['path']) == page[k]['sha256'] for k in ('read_intermediate_image', 'final_image'))
        a, b = [Image.open(ROOT / page[k]['path']).convert('RGB') for k in ('read_intermediate_image', 'final_image')]
        box = ImageChops.difference(a, b).getbbox()
        boxes_ok &= (list(box) if box else None) == page['difference_bbox'] and (box is None or box[1] >= 1680)
        crop = (0, 0, 1391, 1680)
        bodies_ok &= a.size == b.size == (1391, 1800) and a.crop(crop).tobytes() == b.crop(crop).tobytes()
        bodies_ok &= hashlib.sha256(b.crop(crop).tobytes()).hexdigest() == page['body_rgb_sha256']
    check('body-page-image-hashes', images_ok)
    check('body-all-71-reviewed-bodies-identical', bodies_ok)
    check('body-differences-limited-to-footer-region', boxes_ok)
    final_text = (body_folder / 'body-cached.txt').read_text()
    check('body-final-equation-caches-retained', not expected - Counter(re.findall(r'\([1-3C]\.\d+\)', final_text)))
    check('body-final-caption-regression-fixed', 'Figure 2-1' in final_text and 'Figure 2-2' in final_text and
          'Figure Theoretical background' not in final_text and 'Equation Chapter (Next)' not in final_text)
    check('body-fidelity-and-gate-remain-open', body['read_status'] == doc['read_status'] and
          body['whole_model_read_gate'] == 'NOT_PASSED' and body['human_approval_issued'] is False)
    manuals = json.loads((HERE / 'manuals-visual-read/read-receipts.json').read_text())
    check('manuals-two-independent-pdf-receipts', len(manuals['records']) == 2 and
          {r['work_id'] for r in manuals['records']} == {'XBeach-manual-kingsday', 'XBeach-manual-master'})
    check('manuals-213-new-pages', sum(len(r['new_page_records']) for r in manuals['records']) == manuals['new_pages'] == 213)
    for record in manuals['records']:
        label = record['work_id']
        prior = record['prior_evidence']
        premise = json.loads((ROOT / prior['path']).read_text())
        saved = next(s for w in premise['documents'] if w['work_id'] == label for s in w['sources'] if s['path'].endswith('.pdf'))
        stop, total = (45, 141) if label.endswith('kingsday') else (46, 145)
        check(label + '-prior-binding', digest(ROOT / prior['path']) == prior['sha256'] and
              prior['source_sha256'] == saved['sha256'] and prior['physical_pages'] == list(range(10, stop + 1)) and
              saved['covered_pdf_physical_pages'] == f'10-{stop} inclusive')
        check(label + '-sources', record['sources'] == [{'path': s['path'], 'sha256': s['sha256']} for s in (saved, saved['exact_duplicate'])] and
              all(digest(ROOT / s['path']) == s['sha256'] for s in record['sources']))
        new = record['new_page_records']
        check(label + '-new-page-range', [p['physical_page'] for p in new] == list(range(1, 10)) + list(range(stop + 1, total + 1)))
        check(label + '-full-combined-coverage', record['combined_physical_pages'] == list(range(1, total + 1)) and
              record['pdf_physical_pages_total'] == total and set(prior['physical_pages']) | {p['physical_page'] for p in new} == set(range(1, total + 1)))
        check(label + '-page-artifacts', all(digest(ROOT / p['path']) == p['sha256'] for p in new + record['extra_visuals']))
    check('manuals-no-gate-pass', manuals['whole_model_read_gate'] == 'NOT_PASSED' and manuals['human_approval_issued'] is False)
    docx_review = json.loads((HERE / 'manuals-docx-read/receipt.json').read_text())
    spec = importlib.util.spec_from_file_location('manual_display', ROOT / docx_review['recovery_script']['path'])
    display_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(display_module)
    check('docx-two-independent-sources', [r['work_id'] for r in docx_review['records']] ==
          ['XBeach-manual-kingsday', 'XBeach-manual-master'])
    check('docx-script-bindings', all(digest(ROOT / docx_review[k]['path']) == docx_review[k]['sha256']
          for k in ('recovery_script', 'controls_only_script')))
    for record in docx_review['records']:
        label = record['work_id'] + '-docx'
        source = ROOT / record['source']['path']
        kingsday = record['work_id'].endswith('kingsday')
        check(label + '-source-sha', digest(source) == record['source']['sha256'])
        inv_art, fields_art = record['container_inventory'], record['display_fields']
        check(label + '-evidence-hashes', all(digest(ROOT / a['path']) == a['sha256'] for a in (inv_art, fields_art)))
        inv = json.loads((ROOT / inv_art['path']).read_text())
        check(label + '-package-and-ole-stream-inventory', display_module.inventory(source) == inv)
        check(label + '-object-denominator', inv['body_object_count'] == len(inv['embeddings']) == (238 if kingsday else 248)
              and len(inv['members']) == (530 if kingsday else 562) and inv['omml_count'] == 0)
        fields = json.loads((ROOT / fields_art['path']).read_text())
        check(label + '-source-bound-display-counts', fields['source_sha256'] == digest(source) and
              fields['target_fields'] == (255 if kingsday else 269) and
              fields['display_arguments_recovered'] == (251 if kingsday else 265) and
              fields['empty_display_arguments'] == sum(not f['display'] for f in fields['fields']) == 4)
        check(label + '-receipt-counts', record['recovery_counts'] ==
              {k: v for k, v in fields.items() if k not in ('fields', 'scope', 'source_sha256')})
        variants = record['variants']
        check(label + '-three-render-stages', [v['stage'] for v in variants] ==
              ['direct', 'controls-only', 'display-recovered'])
        for variant in variants:
            tag = label + '-' + variant['stage']
            artifacts = variant['artifacts']
            check(tag + '-artifacts', all(digest(ROOT / a['path']) == a['sha256']
                  for a in list(artifacts.values()) + variant['page_records']))
            pages = variant['visually_inspected_pages']
            unseen = variant['uninspected_pages']
            check(tag + '-explicit-partial-coverage', bool(unseen) and
                  [p['physical_render_page'] for p in variant['page_records']] == pages and
                  len(pages) == len(set(pages)) and len(unseen) == len(set(unseen)) and
                  not set(pages) & set(unseen) and set(pages + unseen) == set(range(1, variant['render_pages'] + 1)))
            info = subprocess.check_output(['pdfinfo', str(ROOT / artifacts['pdf']['path'])], text=True)
            text_value = subprocess.check_output(['pdftotext', '-layout', str(ROOT / artifacts['pdf']['path']), '-'], text=True)
            check(tag + '-pdf-page-and-text-binding', int(re.search(r'^Pages:\s+(\d+)', info, re.M).group(1)) ==
                  variant['render_pages'] and text_value == (ROOT / artifacts['txt']['path']).read_text())
        final = variants[-1]['artifacts']
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp) / 'reproduced.docx'
            check(label + '-saved-display-tree-reproduces', display_module.recover(source, output) == fields)
            check(label + '-derivative-byte-reproduction', digest(output) == final['docx']['sha256'])
        with zipfile.ZipFile(source) as before, zipfile.ZipFile(ROOT / final['docx']['path']) as after:
            check(label + '-all-other-package-bytes-preserved', before.namelist() == after.namelist() and
                  all(before.read(n) == after.read(n) for n in before.namelist() if n != 'word/document.xml'))
            a, b = [etree.fromstring(z.read('word/document.xml')) for z in (before, after)]
            check(label + '-objects-preserved', [etree.tostring(n) for n in a.xpath('//w:object', namespaces=ns)] ==
                  [etree.tostring(n) for n in b.xpath('//w:object', namespaces=ns)])
            check(label + '-text-preserved-plus-cached-displays', Counter(b.xpath('//w:t/text()', namespaces=ns)) ==
                  Counter(a.xpath('//w:t/text()', namespaces=ns)) + Counter(f['display'] for f in fields['fields'] if f['display']))
            check(label + '-no-body-field-controls', not b.xpath('//w:instrText | //w:fldChar | //w:fldSimple', namespaces=ns))
        final_text = (ROOT / final['txt']['path']).read_text()
        counts = Counter(re.findall(r'\((?:2|B|C)\.\d+\)', final_text))
        expected_displays = Counter(f['display'] for f in fields['fields'] if f['display'])
        check(label + '-pdf-contains-all-saved-displays', not expected_displays - counts)
        check(label + '-no-instruction-debris', all(s not in final_text for s in ('Equation Chapter', 'Equation Section', 'MERGEFORMAT', 'Figure Processes and model formulation')))
        check(label + '-original-errors-retained', final_text.count('Error! Reference source not found.') == (0 if kingsday else 2))
        check(label + '-no-full-visual-claim', record['read_status'] ==
              'text-read-with-partial-docx-visual-supplement-and-unresolved-fidelity')
    eq = docx_review['equation_preview_supplement']
    check('docx-equation-preview-artifacts', all(digest(ROOT / a['path']) == a['sha256'] for a in eq['artifacts'].values()))
    with zipfile.ZipFile(ROOT / eq['source']['path']) as package:
        relationships = {n.get('Id'): n.get('Target') for n in etree.fromstring(package.read('word/_rels/document.xml.rels'))}
        check('docx-equation-preview-source-binding', digest(ROOT / eq['source']['path']) == eq['source']['sha256'] and
              'word/' + relationships[eq['preview_relationship']] == eq['preview_member'] and
              'word/' + relationships[eq['ole_relationship']] == eq['ole_member'] and
              package.read(eq['preview_member']) == (ROOT / eq['artifacts']['emf']['path']).read_bytes() and
              package.read(eq['ole_member']) == (ROOT / eq['artifacts']['bin']['path']).read_bytes())
    check('docx-no-gate-pass', docx_review['whole_model_read_gate'] == 'NOT_PASSED' and docx_review['human_approval_issued'] is False)
    full_docx = json.loads((HERE / 'manuals-docx-read/full-visual-read/receipt.json').read_text())
    check('docx-full-prior-receipt-binding', full_docx['prior_receipt'] == {
        'path': str((HERE / 'manuals-docx-read/receipt.json').relative_to(ROOT)),
        'sha256': digest(HERE / 'manuals-docx-read/receipt.json')})
    check('docx-full-two-independent-sources', [r['source'] for r in full_docx['records']] ==
          [r['source'] for r in docx_review['records']])
    for record, prior in zip(full_docx['records'], docx_review['records'], strict=True):
        label = record['work_id'] + '-docx-full'
        final = prior['variants'][-1]
        check(label + '-render-binding', record['render_pdf'] == final['artifacts']['pdf'] and
              digest(ROOT / record['render_pdf']['path']) == record['render_pdf']['sha256'] and
              record['render_pages'] == final['render_pages'])
        pages = record['newly_inspected_pages']
        check(label + '-prior-and-new-coverage', record['prior_inspected_pages'] == final['visually_inspected_pages'] and
              pages == final['uninspected_pages'] and
              [p['physical_render_page'] for p in record['page_records']] == pages and
              sorted(pages + record['prior_inspected_pages']) == record['combined_inspected_pages'] ==
              list(range(1, record['render_pages'] + 1)) and not record['uninspected_pages'])
        check(label + '-observations-cover-new-pages', sorted(p for n in record['observations']
              for p in n['physical_render_pages']) == pages and all(n['observation'] for n in record['observations']))
        check(label + '-page-image-hashes', all(digest(ROOT / a['path']) == a['sha256'] for a in record['page_records']))
        rotated = record['rotated_diagram']
        original = next(p for p in record['page_records'] if p['physical_render_page'] == rotated['physical_render_page'])
        with Image.open(ROOT / original['path']) as a, Image.open(ROOT / rotated['path']) as b:
            check(label + '-rotated-diagram-pixels', digest(ROOT / rotated['path']) == rotated['sha256'] and
                  a.rotate(-90, expand=True).tobytes() == b.tobytes())
        with tempfile.TemporaryDirectory() as scratch:
            for page in (record['page_records'][0], record['page_records'][-1]):
                n = str(page['physical_render_page'])
                output = Path(scratch) / n
                subprocess.run(['pdftoppm', '-f', n, '-l', n, '-singlefile', '-scale-to', '1800', '-png',
                                str(ROOT / record['render_pdf']['path']), str(output)], check=True)
                check(label + '-rendered-endpoint-' + n, digest(output.with_suffix('.png')) == page['sha256'])
        check(label + '-qualified-coverage', record['read_status'] == 'all-render-pages-inspected-with-unresolved-docx-fidelity' and
              any('undecoded Equation Native' in x for x in record['limitations']))
    source_ns = dict(ns, w14='http://schemas.microsoft.com/office/word/2010/wordml',
                     v='urn:schemas-microsoft-com:vml', o='urn:schemas-microsoft-com:office:office',
                     r='http://schemas.openxmlformats.org/officeDocument/2006/relationships')
    check('docx-full-three-preview-supplements', [(r['equation_label'], r['physical_render_page'])
          for r in full_docx['equation_supplements']] == [('2.40', 27), ('2.43', 28), ('2.38', 27)])
    for item in full_docx['equation_supplements']:
        label = 'docx-preview-' + item['equation_label']
        artifacts = item['artifacts']
        check(label + '-hashes', digest(ROOT / item['source']['path']) == item['source']['sha256'] and
              all(digest(ROOT / a['path']) == a['sha256'] for a in artifacts.values()))
        with zipfile.ZipFile(ROOT / item['source']['path']) as package:
            relationships = {n.get('Id'): n.get('Target') for n in etree.fromstring(package.read('word/_rels/document.xml.rels'))}
            root = etree.fromstring(package.read('word/document.xml'))
            p = root.xpath('//w:p[@w14:paraId="' + item['paragraph_id'] + '"]', namespaces=source_ns)[0]
            check(label + '-paragraph-and-relationships', etree.tostring(p) == (ROOT / artifacts['paragraph']['path']).read_bytes() and
                  p.xpath('.//v:imagedata/@r:id', namespaces=source_ns) == [item['preview_relationship']] and
                  p.xpath('.//o:OLEObject/@r:id', namespaces=source_ns) == [item['ole_relationship']] and
                  p.xpath('.//o:OLEObject/@ProgID', namespaces=source_ns) == [item['prog_id']] and
                  'word/' + relationships[item['preview_relationship']] == item['preview_member'] and
                  'word/' + relationships[item['ole_relationship']] == item['ole_member'])
            check(label + '-exact-source-bytes', package.read(item['preview_member']) == (ROOT / artifacts['preview']['path']).read_bytes() and
                  package.read(item['ole_member']) == (ROOT / artifacts['ole']['path']).read_bytes())
        check(label + '-ole-not-claimed-decoded', item['ole_semantically_decoded'] is False)
    check('docx-full-three-source-empty-paragraphs', [r['equation_label'] for r in full_docx['source_empty_paragraphs']] ==
          ['2.27', '2.41', '2.42'])
    for item in full_docx['source_empty_paragraphs']:
        with zipfile.ZipFile(ROOT / item['source']['path']) as package:
            p = etree.fromstring(package.read('word/document.xml')).xpath(
                '//w:p[@w14:paraId="' + item['paragraph_id'] + '"]', namespaces=source_ns)[0]
            a = item['artifact']
            check('docx-source-empty-' + item['equation_label'], digest(ROOT / item['source']['path']) == item['source']['sha256'] and
                  digest(ROOT / a['path']) == a['sha256'] and etree.tostring(p) == (ROOT / a['path']).read_bytes() and
                  not p.xpath('.//w:object | .//w:drawing | .//w:pict | .//*[local-name()="oMath"]', namespaces=source_ns))
    check('docx-full-not-semantic-or-human-pass', full_docx['whole_model_read_gate'] == 'NOT_PASSED' and
          full_docx['human_approval_issued'] is False)
    reconciliation = json.loads((HERE / 'resume-reconciliation.json').read_text())
    check('reconciliation-input-bindings', all(digest(ROOT / p) == h for p, h in reconciliation['input_evidence_sha256'].items()))
    check('no-overall-or-human-pass', reconciliation['whole_model_read_gate'] == 'NOT_PASSED' and
          reconciliation['human_approval_issued'] is False)
    result = {'scope': 'Structural/source/hash checks only; no independent semantic or human approval.',
              'checks': checks, 'pass': all(r['pass'] for r in checks)}
    (HERE / 'resume-validation.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({'checks': len(checks), 'pass': result['pass'],
                      'failed': [r['check'] for r in checks if not r['pass']]}))
    raise SystemExit(0 if result['pass'] else 1)


if __name__ == '__main__':
    main()
