"""Original array methods with explicit metadata/ABI markers; two native setters."""
import ast
import ctypes as ct
import hashlib
import json
import subprocess
import sys
import tempfile
from pathlib import Path
from numbers import Number
import numpy as np

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[5]
SOURCE=ROOT/'models/XBeach/raw/source_code/trunk/src/pybeach/xbeach/libxbeach.py'
NATIVE=ROOT/'models/XBeach/raw/source_code/trunk/src/xbeachlibrary/introspection.F90'
PRIOR=HERE.parent/'runtime-20260912'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def dump(name,data):(HERE/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')

tree=ast.parse(SOURCE.read_text())
klass=next(x for x in tree.body if isinstance(x,ast.ClassDef) and x.name=='XBeach')
methods=[x for x in klass.body if isinstance(x,ast.FunctionDef) and x.name in {'get_array','set_array'}]
source_lines=SOURCE.read_text().splitlines(True)
method_source='class OriginalMethods:\n'+''.join(''.join(source_lines[x.lineno-1:x.end_lineno])+'\n' for x in methods)
ns={name:getattr(ct,name) for name in ['c_int','c_double','c_char','POINTER','pointer','byref','create_string_buffer']}
ns.update({'ndpointer':np.ctypeslib.ndpointer,'float64':np.float64,'int32':np.int32,
           'array':np.array,'ndarray':np.ndarray,'Number':Number})
exec(compile(method_source,str(SOURCE),'exec'),ns)
Original=ns['OriginalMethods']
procs=[json.loads(x) for x in (PRIOR/'procedures.jsonl').read_text().splitlines()]
exports={z['name']:p for p in procs if Path(p['path']).name=='introspection.F90' for z in p['bind_c_names']}

class FunctionMarker:
    def __init__(self,lib,symbol):self.lib=lib;self.symbol=symbol;self.argtypes=None
    def __call__(self,name,pointer,length):
        lib=self.lib;lib.called.append(self.symbol)
        if self.symbol.startswith('get'):
            address=ct.addressof(lib.buffer) if lib.rank==0 else lib.buffer.ctypes.data
            ct.cast(pointer,ct.POINTER(ct.c_void_p))[0]=address
        else:
            lib.pointer_type=self.argtypes[1]._type_.__name__
            address=ct.cast(pointer,ct.POINTER(ct.c_void_p))[0]
            element=ct.c_int if lib.typecode=='i' else ct.c_double
            # Probe inputs have sufficient storage; never read a too-small buffer.
            lib.received=np.ctypeslib.as_array(ct.cast(address,ct.POINTER(element)),
                                             shape=(int(np.prod(lib.shape)) if lib.rank else 1,)).copy().tolist()
        return 0

class MarkerLibrary:
    def __init__(self,typecode,rank,shape):
        self.typecode,self.rank,self.shape=typecode,rank,shape
        self.called=[];self.lookups=[];self.received=None;self.pointer_type=None
        dtype=np.int32 if typecode=='i' else np.float64
        self.expected=17 if typecode=='i' else 17.25
        self.buffer=(ct.c_int(self.expected) if typecode=='i' else ct.c_double(self.expected)) if rank==0 else np.array(np.arange(np.prod(shape)).reshape(shape)+1,dtype=dtype,order='F')
    def __getattr__(self,symbol):
        self.lookups.append(symbol)
        if symbol not in exports:raise AttributeError('No source C export '+symbol)
        return FunctionMarker(self,symbol)

def configured(typecode,rank,lib,shape=None):
    o=Original();o._lib=lib
    o.get_arraytype=lambda name:typecode
    o.get_arrayrank=lambda name:rank
    o.get_arrayshape=lambda name:tuple(shape if shape is not None else range(2,rank+2))
    return o

rows=[]
for operation in ['get','set']:
    for typecode in ['i','r','c','unknown',b'i']:
        for rank in range(6):
            shape=tuple(range(2,rank+2));lib=MarkerLibrary('i' if typecode=='i' else 'r',rank,shape)
            o=configured(typecode,rank,lib)
            value=17 if rank==0 else np.array(np.arange(np.prod(shape)).reshape(shape)+1,dtype=np.int32 if typecode=='i' else np.float64,order='F')
            row={'operation':operation,'metadata_type':typecode.decode()+'_bytes' if isinstance(typecode,bytes) else typecode,'rank':rank}
            try:
                result=o.get_array(b'x') if operation=='get' else o.set_array(b'x',value)
                row['outcome']='returned'
                if operation=='get':
                    row['result_shape']=list(np.shape(result))
                    expected=lib.expected if rank==0 else lib.buffer
                    assert np.array_equal(result,expected),(row,result,expected)
                    if rank>0:
                        before=result.copy();lib.buffer[...] = -5
                        assert np.array_equal(before,result)
                        row['python_copy_independent_of_marker_storage']=True
                elif typecode=='i' and rank==0:
                    row['received_integer']=lib.received[0]
                    assert lib.pointer_type=='LP_c_double' and lib.received[0]!=17
                elif typecode in {'i','r'}:
                    expected=np.array(value).ravel(order='F').tolist()
                    assert lib.received==expected,(row,lib.received,expected)
            except (ValueError,AttributeError,UnboundLocalError,ct.ArgumentError) as e:
                row['outcome']=type(e).__name__;row['message']=str(e)
            row['selected_symbols']=lib.lookups;row['called_symbols']=lib.called
            rows.append(row)

# Assert dispatch independently of downstream NumPy conversion. The original
# array(arrayp) conversion fails on the recorded NumPy runtime after the marker.
for row in rows:
    op,code,rank=row['operation'],row['metadata_type'],row['rank']
    if code in {'i','r'}:
        limit=2 if op=='get' and code=='i' else 4
        if rank>limit:
            assert row['outcome']=='ValueError' and not row['selected_symbols'],row
        else:
            symbol=f"{op}{rank}d{'int' if code=='i' else 'double'}array"
            assert row['selected_symbols']==[symbol],row
            if symbol not in exports:
                assert row['outcome']=='AttributeError' and not row['called_symbols'],row
            else:
                assert row['called_symbols']==[symbol],row
                if op=='get' and rank>0:
                    assert row['outcome']=='ValueError' and 'PEP 3118' in row['message'],row
                else:assert row['outcome']=='returned',row
    else:
        assert not row['selected_symbols'] and not row['called_symbols'],row
        assert row['outcome'] in {'ValueError','UnboundLocalError'},row

# Compile two exact original C setters with test-only name/registry/storage adapters.
native_lines=NATIVE.read_bytes().split(b'\n')
native_procs=[exports[n] for n in ['set0dintarray','set0ddoublearray']]
excerpts=[b'\n'.join(native_lines[p['line_start']-1:p['line_end']]) for p in native_procs]
prefix=b"""module marker_state
 use iso_c_binding
 implicit none
 integer(c_int), target, save :: stored_i=-999
 real(c_double), target, save :: stored_r=-999
 integer :: s=0
 type arraytype
   integer(c_int), pointer :: i0
   real(c_double), pointer :: r0
 end type
contains
 function char_array_to_string(name) result(key)
   character(c_char), intent(in) :: name(:)
   character(len=size(name)) :: key
   integer i
   do i=1,size(name)
     key(i:i)=name(i)
   enddo
 end function
 integer function chartoindex(name)
   character(*), intent(in) :: name
   chartoindex=1
 end function
 subroutine indextos(dummy,index,a)
   integer,intent(in) :: dummy,index
   type(arraytype),intent(out) :: a
   a%i0=>stored_i
   a%r0=>stored_r
 end subroutine
 integer(c_int) function inspect_i() bind(C,name='inspect_i')
   inspect_i=stored_i
 end function
 real(c_double) function inspect_r() bind(C,name='inspect_r')
   inspect_r=stored_r
 end function
"""
native_source=prefix+b'\n'.join(excerpts)+b'\nend module\n'
dump('native-excerpts.json',{'source':{'path':str(NATIVE.relative_to(ROOT)),'sha256':sha(NATIVE)},
     'procedures':[{'name':p['name'],'line_start':p['line_start'],'line_end':p['line_end'],
                    'excerpt_sha256':hashlib.sha256(x).hexdigest()} for p,x in zip(native_procs,excerpts)],
     'probe_source_sha256':hashlib.sha256(native_source).hexdigest(),
     'adapters':'Test-only registry/name conversion and persistent scalar storage; two setter bodies and signatures are byte-exact original excerpts'})
with tempfile.TemporaryDirectory(prefix='xbeach-interface-native-') as td:
    tmp=Path(td);f=tmp/'marker.f90';so=tmp/'marker.so';f.write_bytes(native_source)
    args=['gfortran','-shared','-fPIC','-O0','-ffree-line-length-none',str(f),'-o',str(so)]
    compile_result=subprocess.run(args,cwd=tmp,capture_output=True,text=True)
    assert compile_result.returncode==0,compile_result.stderr
    native=ct.CDLL(str(so));native.inspect_i.restype=ct.c_int;native.inspect_r.restype=ct.c_double
    native_results=[]
    for code in ['i','r']:
        configured(code,0,native).set_array(b'x',17)
        got=native.inspect_i() if code=='i' else native.inspect_r()
        native_results.append({'metadata_type':code,'input':17,'observed':got})
    assert native_results[0]['observed']!=17 and native_results[1]['observed']==17

# Wrong shape under normal versus optimized Python; marker does not touch data.
shape_results=[]
for optimization in [0,1]:
    other=dict(ns);exec(compile(method_source,str(SOURCE),'exec',optimize=optimization),other)
    o=other['OriginalMethods']();o.get_arraytype=lambda name:'r';o.get_arrayrank=lambda name:2
    o.get_arrayshape=lambda name:(2,3)
    lib=MarkerLibrary('r',2,(2,3));o._lib=lib
    try:
        o.set_array(b'x',np.ones((3,2),dtype=np.float64,order='F'))
        outcome='returned'
    except AssertionError:outcome='AssertionError'
    shape_results.append({'optimize':optimization,'outcome':outcome,'called_symbols':lib.called})
assert [r['outcome'] for r in shape_results]==['AssertionError','returned']

dump('probe-results.json',{'status':'PASS','status_meaning':'Expected dispatch, rejection and observed incompatibilities reproduced; does not mean the wrapper succeeds',
    'python':sys.version.split()[0],'numpy':np.__version__,'c_int_bytes':ct.sizeof(ct.c_int),'c_double_bytes':ct.sizeof(ct.c_double),
    'compiler':subprocess.check_output(['gfortran','--version'],text=True).splitlines()[0],
    'source':{'path':str(SOURCE.relative_to(ROOT)),'sha256':sha(SOURCE)},
    'original_methods':[{'name':p.name,'line_start':p.lineno,'line_end':p.end_lineno,
       'sha256':hashlib.sha256(''.join(source_lines[p.lineno-1:p.end_lineno]).encode()).hexdigest()} for p in methods],
    'rows':rows,'native_scalar_setters':native_results,'shape_assert':shape_results,
    'limits':['Metadata queries/registry/model storage are adapters; not an unmodified wrapper/model integration test',
      'Dispatch tests include synthetic unsupported ranks, unknown codes and Python3 byte-valued metadata',
      'Array getter markers use stable storage; original scalar getters returning local targets are not dereferenced',
      'Native probe executes only two original scalar setters, not solver/MPI or other numeric functions',
      'Original solver and wrapper files remain unchanged; no human approval issued']})
print('PASS:',len(rows),'conditional dispatch cases; two original native scalar setters; normal/optimized shape guard')
