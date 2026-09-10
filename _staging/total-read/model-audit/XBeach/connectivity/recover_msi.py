#!/usr/bin/env python3
"""Recover and hash-check saved MSI members without installing their contents."""
import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
HELPER = HERE.parent / 'closure/local-refutations/mpich-identity/extract_mpich_identity.py'


def sha(data):
    return hashlib.sha256(data).hexdigest()


def main():
    spec = importlib.util.spec_from_file_location('msi_identity', HELPER)
    helper = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(helper)
    saved_path = HERE / 'msi-content-inventory.json'
    saved = json.loads(saved_path.read_text())
    raw = {}
    for path in (ROOT / 'models/XBeach/raw/source_code').rglob('*'):
        if path.is_file():
            raw.setdefault(sha(path.read_bytes()), []).append(str(path.relative_to(ROOT)))
    results = []
    scratch = Path('/tmp/xbeach-msi-recovered')
    for archive in saved['archives']:
        path = ROOT / archive['path']
        assert sha(path.read_bytes()) == archive['sha256']
        helper.MSI = path
        streams = helper.read_streams()
        assert set(streams) == {r['name'] for r in archive['streams']}
        for row in archive['streams']:
            assert len(streams[row['name']]) == row['bytes']
            assert sha(streams[row['name']]) == row['sha256']
        strings = helper.read_string_table(streams)
        columns = helper.read_columns(streams['!_Columns'], strings)
        files = helper.read_file_table(streams['!File'], strings, columns)
        expected = {r['id']: r for r in archive['members']}
        assert len(files) == len(expected)
        dest = scratch / path.stem
        dest.mkdir(parents=True, exist_ok=True)
        cabs = [(name, data) for name, data in streams.items() if data.startswith(b'MSCF')]
        assert len(cabs) == 1
        cabinet = dest / 'payload.cab'
        cabinet.write_bytes(cabs[0][1])
        subprocess.run(['cabextract', '-q', '-d', str(dest), str(cabinet)], check=True)
        members = []
        for row in files:
            ident = row['File']
            old = expected[ident]
            name = row['FileName'].split('|')[-1]
            data = (dest / ident).read_bytes()
            assert name == old['name']
            assert len(data) == row['FileSize'] == old['bytes']
            assert sha(data) == old['sha256']
            kind = ('pe-executable' if data.startswith(b'MZ') else
                    'ar-library' if data.startswith(b'!<arch>\n') else
                    'zip-container' if data.startswith(b'PK\x03\x04') else
                    'pdf' if data.startswith(b'%PDF') else 'other')
            interface = None
            if kind in ('pe-executable', 'ar-library'):
                output = subprocess.run(['objdump', '-p', str(dest / ident)], capture_output=True)
                artifact = dest / (ident + '.objdump-p.txt')
                artifact.write_bytes(output.stdout + output.stderr)
                interface = {'path': str(artifact), 'sha256': sha(artifact.read_bytes()),
                             'exit_code': output.returncode,
                             'dll_imports': sorted({line.split('DLL Name:', 1)[1].strip()
                                                   for line in output.stdout.decode(errors='replace').splitlines()
                                                   if 'DLL Name:' in line})}
            members.append({'id': ident, 'name': name, 'sha256': sha(data), 'bytes': len(data),
                            'kind': kind, 'scratch_path': str(dest / ident),
                            'identical_raw_paths': raw.get(sha(data), []), 'interface_extraction': interface,
                            'status': 'recovered-and-hash-checked; semantic-status-not-promoted'})
        results.append({'path': archive['path'], 'sha256': archive['sha256'],
                        'stream_count_checked': len(streams), 'members': members})
    result = {'date': '2026-09-10', 'inventory_sha256': sha(saved_path.read_bytes()),
              'method': 'MSI stream/table/cabinet/member identity and all hashes rechecked; cabextract 1.11; no installation.',
              'semantic_read_complete': False, 'archives': results}
    (HERE / 'msi-recovery.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    for archive in results:
        print(archive['path'], 'streams', archive['stream_count_checked'], 'members', len(archive['members']),
              'exact-raw-copies', sum(bool(r['identical_raw_paths']) for r in archive['members']))


if __name__ == '__main__':
    main()
