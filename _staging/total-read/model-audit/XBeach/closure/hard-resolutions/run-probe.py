"""Compile the unchanged datastore and check the exact seed statement in isolation."""
from pathlib import Path
import json
import subprocess

ROOT = Path(__file__).resolve().parents[6]
OUT = Path(__file__).resolve().parent
SCRATCH = Path('/tmp/xbeach-closure-hard')
SCRATCH.mkdir(exist_ok=True)
SRC = ROOT / 'models/XBeach/raw/source_code/trunk/src/xbeachlibrary'
line = (SRC / 'wave_boundary_main.f90').read_bytes().decode().split('\n')[222].rstrip('\r')
probe = OUT / 'randomseed-probe.f90'
probe.write_text('program randomseed_probe\n use wave_boundary_datastore\n implicit none\n' + line + '\nend program\n')
commands = [
    ['gfortran', '-c', str(SRC / 'wave_boundary_datastore.f90'), '-J', str(SCRATCH), '-o', str(SCRATCH / 'wave_boundary_datastore.o')],
    ['gfortran', '-fsyntax-only', '-I', str(SCRATCH), str(probe)],
]
logs = []
for command in commands:
    r = subprocess.run(command, cwd=SCRATCH, text=True, capture_output=True)
    portable = lambda s: s.replace(str(ROOT) + '/', '')
    logs.append({'command': [portable(s) for s in command], 'exit_code': r.returncode,
                 'stdout': portable(r.stdout), 'stderr': portable(r.stderr)})
assert logs[0]['exit_code'] == 0 and logs[1]['exit_code'] != 0
assert 'must be ALLOCATABLE' in logs[1]['stderr']
(OUT / 'randomseed-probe-results.json').write_text(json.dumps(logs, indent=2) + '\n')
print('PASS: original datastore compiles; exact ALLOCATED/DEALLOCATE statement fails as predicted')
