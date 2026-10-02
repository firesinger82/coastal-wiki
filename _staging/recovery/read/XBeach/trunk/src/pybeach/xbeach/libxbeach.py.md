---
file: models/XBeach/raw/source_code/trunk/src/pybeach/xbeach/libxbeach.py
lines: 290
sha256: 55640d609c20815d0b3cf24e0cbf42c48e7a52d8aea701f41d6e3e1c20d5027f
reader: codex gpt-6.1-sol
read_date: 2026-10-02
---

# libxbeach.py — 판독 구간 기록

구간은 1행부터 290행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–25 | os/sys·collections·Number·ctypes·NumPy·subprocess·logging 가져오기(1–12). DEBUG logger와 StreamHandler/formatter 구성(14–18); 비활성 basicConfig 주석(13). DLL 접미사 기본 .so, darwin .dylib, win32/win64 .dll(21–24). 접미사 원문: `dllsuffix = collections.defaultdict(lambda:'.so')` (21), `dllsuffix['darwin'] = '.dylib'` (22), `dllsuffix['win32'] = '.dll'` (23), `dllsuffix['win64'] = '.dll'` (24). |
| 26–48 | dlclose에서 `name = 'libdl' + dllsuffix[sys.platform]` (27), CDLL 로드(28), dlerror.restype=c_char_p·dlclose.argtypes=[c_void_p](29–30), dlclose(handle)(32). `if rc!=0:` (33) 안 dlerror 호출(35); 중첩 `if error == 'invalid handle passed to dlclose()':` (37)일 때만 ValueError(38). 33의 else는 성공 로그(39–40). isloaded는 abspath(45), `ret = os.system("lsof -p %d \| grep %s > /dev/null" % (os.getpid(), libp))` (46), `return (ret == 0)` (47). |
| 49–76 | XBeach 클래스·생성자(49–51)는 olddir 저장(52). `if workingdir is None:` (53)이면 현재 폴더, `else:` (55)는 전달값(56). 이 분기 밖 os.chdir(57), abspath·CDLL 로드(58–59), shouldinitialize=True(60). init의 `if self.shouldinitialize:` (64) 안 `_lib.init()`(65); False 재설정(66)은 if 밖. executestep→_lib.executestep(69), output→_lib.outputext(72), get_nparameter→getnparameter(byref(n)) 및 n.value(74–76). 생성자 기본 인수 원문: `def __init__(self, libpath, workingdir=None):` (51). |
| 77–92 | 파라미터 이름 1024바이트 버퍼(80); Python 인덱스를 `index = c_int(i+1)` (81)로 바꿔 getparametername에 index/name/length 전달(83), name.value 반환(85–86). get_parameternames는 range(get_nparameter())를 순회하여 위 메서드 결과를 list에 append(89–92). |
| 93–126 | get_parameter는 get_parametertype(94)·이름 버퍼·`namelength = c_int(len(name))` (96). `if typecode == 'c':` (98) 안 getcharparameter(100) 후 `result = string_at(addressof(value), valuelength)` (102); 앞 조건 거짓인 `elif typecode == 'r':` (103)는 getdoubleparameter(105), 앞 두 조건 거짓인 `elif typecode == 'i':` (107)는 getintparameter(109); `else:` (111)는 ValueError(112). 성공 분기 뒤 result 반환(113). get_parametertype는 `length = c_int(len(name))` (117), getparametertype(118)·typecode.value 반환(119). get_parameters는 `(name, self.get_parameter(name))` (122)를 get_parameternames(124)에서 모은 집합 comprehension(121–125) 반환(126). |
| 127–148 | set_parameter는 type 조회·이름 버퍼·`namelength = c_int(len(name))` (130). `if typecode == 'r':` (131) 안 c_double 변환(132), setdoubleparameter(133); 중첩 `if (code != 0):` (134)일 때 ValueError(135), 그 검사 밖 같은 r 분기에서 result=value.value(136). 주석 처리된 정수 setter: `# if typecode == 'i':` (137), setintparameter 호출 주석(139), `#     if (code != 0):` (140), 예외·result 주석(141–142). 활성 131의 `else:` (143)는 ValueError(144). get_narray는 getnarray(byref(n))·n.value(145–148). |
| 149–191 | get_arraynamebyindex는 이름 버퍼 1024(152), `index = c_int(i+1)` (153), getarrayname(155), name.value 반환(157–158). get_arraynames는 range(get_narray()) 이름 list(161–164). get_arraytype·get_arrayrank 각각 이름 길이 `namelength = c_int(len(name))` (169·175)와 getarraytype/getarrayrank 호출(170·176), scalar value 반환(171·177). get_arraydimsize는 `dim = c_int(dim+1)` (180), `namelength = c_int(len(name))` (182), getarraydimsize(183)·dimsize.value(184). get_arrayshape는 rank 개수의 각 dimsize를 tuple로 반환(185–189); 빈 줄 포함. |
| 192–227 | get_array에서 type·rank 조회(193–194), `namelength = c_int(len(name))` (196), 작업 변수 None(197–199). `if rank == 0:` (200) → shape=(); `elif rank >= 1:` (202) → get_arrayshape(203); `else:` (204) → ValueError(205). 이 rank 분기 밖 `if typecode == 'c':` (206)는 예외(207); `elif typecode == 'i':` (208) 안 `if rank > 2:` (209) 예외, 그 검사 뒤 get{rank}dintarray(212), `if rank == 0:` (213) → POINTER(c_int), `else:` (215) → F_CONTIGUOUS int32 ndpointer(216). 같은 type 선택의 병렬 `elif typecode == 'r':` (217) 안 `if rank > 4:` (218) 예외, get{rank}ddoublearray(221), `if rank == 0:` (222) → POINTER(c_double), `else:` (224) → F_CONTIGUOUS float64 ndpointer(225). 마지막 type `else:` (226)는 예외(227). |
| 228–242 | 앞 type·rank 선택 모두 끝난 뒤 fun.argtypes 설정(228), arraytype 객체·fun 호출(229–230). 별도 `if rank == 0:` (231)이면 contents.value(233), `else:` (234)는 NumPy array 복사(235); 분기 밖 result 반환(236). get_arrays는 모든 이름에 get_array를 호출해 dict로 반환(237–241), 빈 줄(242). |
| 243–277 | set_array는 type·rank·shape 조회(244–251), `namelength = c_int(len(name))` (247); `assert shape == array(value).shape, "Shapes not equal {} versus {} for variable {}".format(shape, value.shape, name)` (252). 독립 `if typecode == 'c':` (254), `if rank > 4:` (256)는 각각 예외. 별도 `if typecode == 'r':` (258)에서 `dtype = float64 if rank > 0 else c_double` (259), typename='double'; 병렬 `elif typecode == 'i':` (261)에서 `dtype = int32 if rank > 0 else c_double` (262), typename='int'. 선택 뒤 set{rank}d{typename}array 조회(264). `if rank == 0:` (265) → POINTER(dtype), `else:` (267) → F_CONTIGUOUS ndpointer(268). 그 분기 뒤 fun.argtypes(269). `if isinstance(value, Number):` (270) → pointer(dtype(value))(271); `elif isinstance(value, ndarray):` (272) → data_as(arraytype)(273); `else:` (274) → ValueError(275). 성공 선택 뒤 fun 호출(276). |
| 278–290 | finalize는 handle 저장(280), self._lib 삭제(281), isloaded 로그(282). `while isloaded(self.libpath):` (283) 안 dlclose(handle)·상태 로그(284–285). 루프 뒤 subprocess 기반 파일조회는 주석(286–287), shouldinitialize=True(289). 마지막 공백 줄(290). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 52·57·278–290: 생성자는 프로세스 작업 디렉터리를 바꾸고 olddir를 저장하지만 이 파일에서 olddir로 복구하는 문장은 없다.
- 121–125: get_parameters의 comprehension은 키:값 구분자가 없는 (name,value) 튜플 집합이다.
- 98–102: 문자열 getter의 value 저장소는 c_char 하나이며 string_at의 길이에 c_int 객체 valuelength를 그대로 전달한다.
- 200–205: rank>=1을 허용하는 분기와 오류 문자열의 'not in (0, 2)' 표기가 다르다.
- 213–214·261–263: 정수 scalar getter는 POINTER(c_int)를 쓰지만 정수 scalar setter의 dtype은 c_double이다.
- 258–264: setter의 타입 선택에는 r/i만 있고 마지막 else는 없다. typename을 이 선택 이전에 초기화하는 문장도 없다.
- 252: assert의 메시지를 만들 때 전달값의 value.shape를 참조한다. Number 입력 처리 분기는 그 뒤 270행에 있다.
- 278–289: finalize는 _lib.final()을 호출하지 않고 라이브러리 객체 삭제·dlclose 반복을 수행한다.
- 283–285: 라이브러리가 로드된 동안 반복하며 반복 횟수 상한은 없다.
- 8·9·10·286: as_array·zeros는 이후 활성 코드에서 쓰이지 않는다. subprocess 사용 예시는 286행 주석뿐이다.
