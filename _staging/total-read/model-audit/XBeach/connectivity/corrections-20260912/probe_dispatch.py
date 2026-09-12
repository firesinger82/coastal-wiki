"""Run the original SELECT block with instrumented callees, not the full model."""
import hashlib
import json
import subprocess
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[5]
SRC = ROOT / 'models/XBeach/raw/source_code/trunk/src/xbeachlibrary'


def excerpt(name, first, last):
    return b'\n'.join((SRC / name).read_bytes().split(b'\n')[first-1:last]).decode()


def main():
    consts = excerpt('paramsconst.F90', 80, 91)
    block = excerpt('morphevolution.F90', 173, 190)
    src = '''module instrumented_dispatch
implicit none
type parameters
 integer :: form, bulk
end type
type state
 integer :: unused=0
end type
integer :: called
logical :: continued
''' + consts + '''
contains
subroutine dispatch(s,par)
type(state) :: s
type(parameters) :: par
''' + block + '''
continued=.true.
end subroutine
'''
    for number, name in [(1, 'sedtransform'), (2, 'Nielsen2006'), (3, 'mccall_vanrijn'), (4, 'intra_sedtr')]:
        src += f'''subroutine {name}(s,par)
type(state) :: s
type(parameters) :: par
called={number}
end subroutine
'''
    src += '''end module
program probe
use instrumented_dispatch
implicit none
type(parameters) :: par
type(state) :: s
integer :: f,b
do f=0,11
 do b=0,1
  par%form=f
  par%bulk=b
  called=0
  continued=.false.
  call dispatch(s,par)
  write(*,'(3(I0,1X),L1)')f,b,called,continued
 enddo
enddo
end program
'''
    (HERE / 'dispatch-probe.f90').write_text(src)
    compiler = subprocess.run(['gfortran', '--version'], capture_output=True, text=True, check=True).stdout.splitlines()[0]
    with tempfile.TemporaryDirectory(prefix='xbeach-form-dispatch-') as td:
        cmd = ['gfortran', '-std=f2008', '-O0', '-fcheck=all', str(HERE / 'dispatch-probe.f90'), '-o', 'probe']
        build = subprocess.run(cmd, cwd=td, capture_output=True, text=True, check=True)
        run = subprocess.run([str(Path(td) / 'probe')], cwd=td, capture_output=True, text=True, check=True)
    rows = []
    expected_calls = {0: 1, 1: 1, 2: 1, 3: 2, 4: 3, 11: 4}
    for line in run.stdout.splitlines():
        f, b, call, cont = line.split()
        f, b, call, cont = int(f), int(b), int(call), cont == 'T'
        assert call == expected_calls.get(f, 0), line
        assert cont == (not (f in (3, 4) and b == 0)), line
        rows.append({'form_value': f, 'bulk': b, 'callee_marker': call, 'reaches_after_select': cont})
    assert len(rows) == 24
    result = {'scope': 'Original paramsconst constants and transus SELECT only. Callees are marker stubs; no input parser, preceding/following physics, full solver or MPI execution.',
              'compiler': compiler, 'compile_command': cmd, 'compile_stderr': build.stderr,
              'source_sha256': hashlib.sha256((HERE / 'dispatch-probe.f90').read_bytes()).hexdigest(),
              'source_excerpts': [{'file': 'paramsconst.F90', 'lines': [80, 91]}, {'file': 'morphevolution.F90', 'lines': [173, 190]}],
              'run_exit_code': run.returncode, 'stdout': run.stdout, 'rows': rows, 'status': 'PASS'}
    (HERE / 'probe-results.json').write_text(json.dumps(result, indent=2) + '\n')
    print('Original SELECT block: 24 form/bulk combinations match the bounded dispatch contracts')


if __name__ == '__main__':
    main()
