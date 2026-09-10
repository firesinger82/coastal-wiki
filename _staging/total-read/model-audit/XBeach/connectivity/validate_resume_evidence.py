#!/usr/bin/env python3
"""Check persisted supplemental evidence; this is not a semantic read gate."""
import hashlib
import json
from pathlib import Path
import zipfile
import olefile

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
    reconciliation = json.loads((HERE / 'resume-reconciliation.json').read_text())
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
