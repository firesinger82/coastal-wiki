"""Compile exact source routines with bounded stubs; never run the model or MPI.

The first probe checks that the real serial output_error path does not return.
The second checks the lifetime of the actual getter declarations, with a stub
compute_dt deliberately changing dtref. Its numbers are not model timesteps.
"""
import hashlib
import json
import subprocess
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[6]
SRC = ROOT / "models/XBeach/raw/source_code/trunk/src/xbeachlibrary"
spans = []
def extract(name, first, last):
    path = SRC / name
    raw = path.read_bytes()
    code = b"\n".join(raw.split(b"\n")[first-1:last]).decode().replace("\r\n", "\n").replace("\r", "")
    spans.append({"path": str(path.relative_to(ROOT)), "sha256": hashlib.sha256(raw).hexdigest(), "first": first, "last": last, "extracted_sha256": hashlib.sha256(code.encode()).hexdigest()})
    return code + "\n"

halt = extract("xmpi.F90", 1680, 1705)
output_error = extract("output.F90", 199, 214)
outputext = extract("libxbeach.F90", 228, 239)
getter = extract("xbeach_bmi.f90", 178, 189)
types = """module probe_types
  implicit none
  type spacepars
    integer :: pad=0
  end type
  type parameters
    real(8) :: dt=0d0
  end type
  type timepars
    integer :: pad=0
  end type
end module
"""
error_program = types + """module xmpi_module
  integer :: xmpi_orank=0
contains
""" + halt + """end module
module logging_module
contains
  subroutine writelog(a,b,c)
    character(*) :: a,b,c
    print '(a)', c
  end subroutine
end module
module output_module
  use probe_types
  use xmpi_module
contains
  subroutine output(sglobal,s,par,tpar,update)
    type(spacepars) :: sglobal,s
    type(parameters) :: par
    type(timepars) :: tpar
    logical,optional :: update
    print '(a)', 'stub output reached'
  end subroutine
""" + output_error + """end module
module core_probe
  use iso_c_binding, only: c_int
  use probe_types
  type(spacepars) :: s,sglobal
  type(parameters) :: par
  type(timepars) :: tpar
  integer :: error=0
contains
""" + outputext + """end module
program error_path_probe
  use core_probe
  character(8) :: arg
  integer :: rc
  call get_command_argument(1,arg)
  read(arg,*) error
  rc=outputext()
  print '(a,i0)', 'RETURNED=',rc
end program
"""
getter_program = types + """module getter_probe
  use probe_types
  use iso_c_binding
  type(spacepars) :: s
  type(parameters) :: par
  type(timepars) :: tpar
contains
  subroutine compute_dt(s,par,tpar,it,ilim,jlim,dtref)
    type(spacepars) :: s
    type(parameters) :: par
    type(timepars) :: tpar
    integer :: it,ilim,jlim
    real(8) :: dtref
    dtref=dtref+1d0
    par%dt=dtref
  end subroutine
""" + getter + """end module
program saved_getter_probe
  use getter_probe
  real(8) :: a,b
  call get_time_step(a)
  call get_time_step(b)
  if (a/=1d0.or.b/=2d0) error stop 'getter local state did not persist'
  print '(a,f3.0,a,f3.0)', 'stub dtref first=',a,' second=',b
end program
"""
result={"scope":"Extracted source control flow/language semantics with stubs; not complete XBeach or MPI execution", "source_spans":spans, "compiler":subprocess.check_output(["gfortran","-dumpfullversion"],text=True).strip(), "runs":[]}
with tempfile.TemporaryDirectory(prefix="xbeach-lifecycle-") as tmp:
    work=Path(tmp)
    for name,program in [("error_path_probe",error_program),("saved_getter_probe",getter_program)]:
        path=HERE/(name+".f90")
        path.write_text(program)
        exe=work/name
        subprocess.run(["gfortran","-cpp","-std=gnu","-fcheck=all",str(path),"-o",str(exe)],cwd=work,check=True,capture_output=True,text=True)
        args_list=[["0"],["1"]] if name=="error_path_probe" else [[]]
        for args in args_list:
            run=subprocess.run([str(exe),*args],cwd=work,capture_output=True,text=True)
            expected=1 if args==["1"] else 0
            if run.returncode!=expected:
                raise RuntimeError((name,args,run.returncode,run.stdout,run.stderr))
            if args==["1"]:
                assert "RETURNED=" not in run.stdout and "STOP 1" in run.stderr
            elif name=="error_path_probe":
                assert "RETURNED=0" in run.stdout
            result["runs"].append({"probe":name,"args":args,"exit_code":run.returncode,"stdout":run.stdout,"serial_stop_1_observed":"STOP 1" in run.stderr,"program_sha256":hashlib.sha256(program.encode()).hexdigest()})
(HERE/"probe-results.json").write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n")
print(json.dumps(result["runs"],ensure_ascii=False))
