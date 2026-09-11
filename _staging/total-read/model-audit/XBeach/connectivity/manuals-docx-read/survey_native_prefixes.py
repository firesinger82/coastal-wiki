"""Find unique validated settings prefixes without adding body record support."""
import collections
import io
import json
import zipfile
import olefile
from inspect_empty_native import inspect as inspect_prefix
from inspect_glyph_records import inspect as inspect_body
from survey_native import FOLDER, ROOT, artifact, sha


def candidates(data):
    result = []
    # Explicit bounded search; each candidate must be a complete settings parse
    # ending in FULL. A matching byte alone is never sufficient.
    for offset in range(40, min(len(data), 513)):
        if data[offset-1] != 10:
            continue
        try:
            p = inspect_prefix(data[:offset] + b'\x00', 28)
        except (ValueError, UnicodeError):
            continue
        if p['records'][-2]['tag'] == 10 and any(r['tag'] == 18 for r in p['records']):
            result.append(offset)
    return result


def build():
    prior = json.loads((FOLDER/'native-survey.json').read_text())
    records = []
    for item in prior['records']:
        with zipfile.ZipFile(ROOT/item['source']['path']) as z:
            with olefile.OleFileIO(io.BytesIO(z.read(item['member']))) as ole:
                native = ole.openstream('Equation Native').read()
        assert sha(native) == item['native_sha256']
        offsets = candidates(native)
        r = {'document': item['document'], 'member': item['member'], 'native_sha256': sha(native),
             'prior_status': item['status'], 'candidate_offsets': offsets}
        if len(offsets) == 1:
            r['body_offset'] = offsets[0]
            try:
                d = inspect_body(native, offsets[0])
                r.update(status='mechanically-accepted-not-semantically-reviewed',
                         character_count=len(d['characters']),
                         decoded_sha256=sha(json.dumps(d, sort_keys=True, ensure_ascii=False).encode()))
            except (ValueError, UnicodeError) as exc:
                r.update(status='unsupported-body', reason=str(exc))
        else:
            r.update(status='unresolved-prefix', reason='no unique validated prefix within bounded search')
        records.append(r)
    return {'date': '2026-09-11', 'attribution': 'AI mechanical prefix survey; not formula semantic review',
            'prior_receipt': artifact(FOLDER/'native-survey.json'),
            'generator': artifact(FOLDER/'survey_native_prefixes.py'),
            'prefix_decoder': artifact(FOLDER/'inspect_empty_native.py'),
            'body_decoder': artifact(FOLDER/'inspect_glyph_records.py'),
            'records': records,
            'counts': dict(collections.Counter(r['status'] for r in records)),
            'offset_counts': dict(collections.Counter(str(r.get('body_offset')) for r in records)),
            'newly_accepted': sum(r['prior_status']=='rejected-by-bounded-reader' and r['status'].startswith('mechanically-accepted') for r in records),
            'limitations': ['Only candidate offsets 40..512 ending in a validated FULL/settings sequence.',
                            'Synthetic END validates settings only, not source emptiness.',
                            'Existing body reader unchanged; acceptance is not semantic or visual approval.',
                            'Unsupported prefix or body is not evidence of source corruption.'],
            'whole_model_read_gate':'NOT_PASSED', 'human_approval_issued':False}


if __name__ == '__main__':
    r = build()
    (FOLDER/'native-prefix-survey.json').write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:r[k] for k in ('counts','offset_counts','newly_accepted')}))
