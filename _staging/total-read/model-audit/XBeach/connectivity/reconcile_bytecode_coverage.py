"""Aggregate explicit reading receipts; does not issue semantic approval."""
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]


def build():
    directory = HERE / 'bytecode-read'
    inputs = {}
    def read(path):
        inputs[str(path.relative_to(ROOT))] = hashlib.sha256(path.read_bytes()).hexdigest()
        return json.loads(path.read_text())
    inventory = read(directory / 'disassembly-receipt.json')
    originals = {x['sha256']: x for x in inventory['records']}
    readings = {}
    for path in sorted(directory.glob('*-read.json')):
        receipt = read(path)
        assert receipt['whole_model_read_gate'] == 'NOT_PASSED'
        assert receipt['human_approval_issued'] is False
        assert receipt['unique_classes_read'] == len(receipt['records'])
        assert receipt['instances_covered'] == sum(len(x['instances']) for x in receipt['records'])
        for record in receipt['records']:
            sha = record['sha256']
            assert sha not in readings, ('duplicate reading', sha)
            original = originals[sha]
            assert original['kind'] == 'java-bytecode'
            assert all(record[k] == original[k] for k in ('instances', 'class_file', 'disassembly'))
            assert record['read_lines'] == [1, original['disassembly_lines']]
            assert record['observation']
            readings[sha] = str(path.relative_to(ROOT))
    rows = []
    for sha, original in originals.items():
        rows.append({'sha256': sha, 'kind': original['kind'],
                     'instance_count': len(original['instances']),
                     'reading_receipt': readings.get(sha),
                     'status': 'direct-reading-evidence' if sha in readings else 'unread'})
    return {'scope': 'Receipt coverage only; no independent semantic or whole-model approval.',
            'input_evidence_sha256': inputs,
            'generator_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'java_unique_read': len(readings),
            'java_unique_unread': sum(x['kind'] == 'java-bytecode' and x['status'] == 'unread' for x in rows),
            'python_unique_unread': sum(x['kind'] == 'python-bytecode' and x['status'] == 'unread' for x in rows),
            'instances_with_reading_evidence': sum(x['instance_count'] for x in rows if x['reading_receipt']),
            'records': rows, 'whole_model_read_gate': 'NOT_PASSED', 'human_approval_issued': False}


if __name__ == '__main__':
    result = build()
    (HERE / 'bytecode-read/coverage.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    print({k: result[k] for k in ('java_unique_read', 'java_unique_unread', 'python_unique_unread', 'instances_with_reading_evidence')})
