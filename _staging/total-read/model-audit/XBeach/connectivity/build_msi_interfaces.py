#!/usr/bin/env python3
"""Persist recoverable import/export/resource-directory evidence, not binary semantics."""
import hashlib
import json
from pathlib import Path
import re

HERE = Path(__file__).resolve().parent


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    inventory = HERE / 'msi-recovery.json'
    recovered = json.loads(inventory.read_text())
    output = HERE / 'msi-interfaces'
    output.mkdir(exist_ok=True)
    rows = []
    for archive in recovered['archives']:
        for member in archive['members']:
            extraction = member['interface_extraction']
            if extraction is None:
                continue
            raw = Path(extraction['path'])
            assert sha(raw) == extraction['sha256']
            text = raw.read_text(errors='replace')
            exports = []
            if '[Ordinal/Name Pointer] Table' in text:
                tail = text.split('[Ordinal/Name Pointer] Table', 1)[1]
                exports = re.findall(r'^\s*\[\s*\d+\]\s+(\S+)\s*$', tail, re.M)
            resource = text.split('The .rsrc Resource Directory section:', 1)
            detail = {
                'archive_path': archive['path'], 'archive_sha256': archive['sha256'],
                'member_id': member['id'], 'member_name': member['name'], 'member_sha256': member['sha256'],
                'kind': member['kind'], 'objdump_exit_code': extraction['exit_code'],
                'objdump_output_sha256': extraction['sha256'],
                'dll_imports': extraction['dll_imports'], 'named_exports': exports,
                'resource_directory_dump': resource[1].strip() if len(resource) == 2 else None,
                'scope': 'Mechanical interface index. DLL dependencies inspected by root; export implementation and resource payload semantics not fully read.',
            }
            target = output / (member['sha256'] + '.json')
            if target.is_file():
                # Different member instances may share bytes, but provenance remains per instance below.
                previous = json.loads(target.read_text())
                assert previous['named_exports'] == exports
                assert previous['dll_imports'] == extraction['dll_imports']
            else:
                target.write_text(json.dumps(detail, indent=2) + '\n')
            rows.append({'archive': archive['path'], 'member_id': member['id'], 'name': member['name'],
                         'sha256': member['sha256'], 'evidence_file': str(target.relative_to(HERE)),
                         'evidence_sha256': sha(target), 'export_count': len(exports),
                         'dll_imports': extraction['dll_imports']})
    result = {
        'date': '2026-09-10', 'inventory_sha256': sha(inventory), 'members': rows,
        'root_review': [
            'Both mpich2mpi.dll dispatchers expose 614 named exports and import KERNEL32.dll in their static import tables. This does not enumerate dynamically loaded implementations.',
            'fmpich2 wrappers import mpich2mpi.dll; MPE profiling wrappers import mpe.dll and mpich2mpi.dll. Static dependencies alone do not prove output initialization or error behavior.',
            'Compute DLL variants have networking, security and Windows service imports; there is no basis to treat their missing source as XBeach solver source.',
            'TraceInput.dll differs by architecture: ia32 has 23 named exports including TRACE_* and decorated JNI names; x64 has 10 named exports including eight JNI names and two MPI Fortran status-ignore symbols. No runtime interchangeability conclusion is made.',
            'AR libraries are recorded as archive interfaces. An empty PE export list for AR is not evidence of no symbols or no executable content.',
        ],
        'overall_semantic_read_complete': False,
        'remaining': 'Compiled implementation, resource payload interpretation and per-library symbol semantics remain unreviewed beyond the explicit dependency observations.',
    }
    (HERE / 'msi-interface-review.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    print('Persisted', len(rows), 'PE/AR member interface instances')


if __name__ == '__main__':
    main()
