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
| 1–25 | 표준 모듈·숫자형·ctypes·NumPy·subprocess를 가져온다(1–10). 모듈 로거를 DEBUG로 두고 스트림 핸들러와 포맷을 추가한다(12–18). 공유 라이브러리 접미사의 기본은 `.so`, darwin은 `.dylib`, win32/win64는 `.dll`(21–24). |
| 26–48 | `dlclose(handle)`는 플랫폼 접미사의 `libdl`을 `CDLL`로 열고 `dlerror.restype=c_char_p`, `dlclose.argtypes=[c_void_p]`를 설정한다(26–30). `dlclose` 반환값이 0이 아니면 오류를 로그에 남기고 특정 invalid-handle 문자열과 같을 때만 `ValueError`를 낸다(32–40). `isloaded(lib)`는 절대경로와 PID를 `lsof -p %d &#124; grep %s > /dev/null` 셸 명령에 넣어 종료값 0 여부를 반환한다(43–47). |
| 49–72 | `XBeach` 생성자는 현재 디렉터리를 `olddir`에 저장하고, `workingdir=None`이면 현재 경로를 쓰며 `os.chdir` 뒤 `libpath`를 절대경로화해 `CDLL`을 연다(51–60). `shouldinitialize=True`인 경우에만 `init()`을 호출한 뒤 False로 둔다(61–66). `executestep()`과 `output()`은 각각 라이브러리의 `executestep`, `outputext`를 호출한다(67–72). |
| 73–92 | 매개변수 개수는 `getnparameter(byref(c_int))`로 얻는다(73–76). 인덱스별 이름은 1024바이트 버퍼, `index=c_int(i+1)` 및 길이 변수를 `getparametername`에 전달해 `name.value`를 반환한다(77–86). `get_parameternames`는 `range(get_nparameter())`를 순회해 목록을 만든다(87–92). |
| 93–119 | `get_parameter`는 `get_parametertype` 결과에 따라 문자 `c`이면 `c_char`와 `getcharparameter` 및 `string_at(addressof(value), valuelength)`(98–102), 실수 `r`이면 `c_double/getdoubleparameter`(103–106), 정수 `i`이면 `c_int/getintparameter`(107–110)를 사용한다. 다른 형은 `ValueError`(111–113). 형 조회는 이름 버퍼·`c_char`·이름 길이를 `getparametertype`에 참조 전달한다(114–119). |
| 120–144 | `get_parameters`는 `(name, self.get_parameter(name))` 쌍을 중괄호 컴프리헨션으로 모아 반환한다(120–126). `set_parameter`는 실수형만 `setdoubleparameter`에 넘기며 반환 코드가 0이 아니면 `ValueError`(127–136); 정수 설정 코드는 주석이고 그 외 형은 예외다(137–144). 136행 `result`는 반환하지 않는다. |
| 145–165 | 배열 개수는 `getnarray`로 얻는다(145–148). 이름은 1024바이트 버퍼와 1부터 시작하는 `i+1` 인덱스로 `getarrayname`을 호출한다(149–158). `get_arraynames`는 배열 이름 목록을 만든다(159–164). |
| 166–191 | `get_arraytype`, `get_arrayrank`는 이름·길이·출력 참조를 `getarraytype/getarrayrank`에 전달한다(166–177). `get_arraydimsize`는 Python 차원 번호를 `dim+1`로 바꿔 `getarraydimsize`를 호출한다(178–184). `get_arrayshape`는 rank만큼 차원 길이를 조회한 튜플을 반환한다(185–189); 끝에 빈 줄이 있다(190–191). |
| 192–227 | `get_array`는 rank 0의 shape를 `()`로, 양수 rank의 shape를 조회값으로 정한다(192–205). 문자 배열은 거부(206–207); 정수는 rank≤2에서 `get{rank}dintarray`, rank 0이면 `POINTER(c_int)`, 그 외 `int32`·Fortran 연속 `ndpointer`(208–216). 실수는 rank≤4에서 `get{rank}ddoublearray`, rank 0이면 `POINTER(c_double)`, 그 외 `float64`·Fortran 연속 포인터를 쓴다(217–225). 나머지 형은 예외다(226–227). |
| 228–242 | 조회 함수의 인자형을 이름 포인터·배열 포인터의 포인터·`c_int`로 설정하고 `fun(c_name, byref(arrayp), namelength)`를 호출한다(228–230). rank 0은 `arrayp.contents.value`, 그 외는 `array(arrayp)`를 반환한다(231–236). `get_arrays`는 모든 이름에 대해 값을 읽어 사전을 만든다(237–241). |
| 243–269 | `set_array`는 shape가 `array(value).shape`와 같은지 assert한다(243–252). 문자형과 rank>4는 거부(254–257). 실수는 양수 rank에 `float64`, rank 0에 `c_double`; 정수는 양수 rank에 `int32`, rank 0에도 `c_double`을 둔다(258–263). `set{rank}d{typename}array`를 찾고 스칼라/Fortran 연속 배열 포인터 및 함수 인자형을 설정한다(264–269). |
| 270–290 | 설정값이 `Number`이면 `pointer(dtype(value))`, `ndarray`이면 `value.ctypes.data_as(arraytype)`, 그 외는 예외다(270–275); `fun`을 참조 인자로 호출한다(276). `finalize`는 핸들을 보관하고 `_lib`를 삭제한 뒤 `isloaded`가 참인 동안 같은 핸들에 `dlclose`를 호출한다(278–285). 열린 파일 로그 코드는 주석이고 `shouldinitialize=True`로 되돌린다(286–290). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 120–126: `get_parameters`의 중괄호 컴프리헨션에는 콜론이 없으며 `(이름, 값)` 튜플의 집합을 만든다.
- 261–266: 정수 rank 0 설정 경로의 dtype도 `c_double`이다. 정수 rank 0 조회 경로는 `c_int`를 쓴다(213–214).
- 51–59·278–290: 생성자에서 `olddir`를 저장하고 작업 디렉터리를 변경하지만, 이 파일에는 `olddir`로 돌아가는 코드가 없다.
- 278–289: `finalize`는 `_lib`를 삭제하고 초기화 플래그만 True로 되돌린다. 이 메서드에는 라이브러리 `final` 호출이나 `_lib` 재생성이 없다.
- 256–264: 설정은 정수도 rank≤4를 허용하는 검사인데, 정수 조회는 rank>2를 거부한다(208–210).
- 254–264: 설정의 문자·실수·정수 외 typecode에는 명시적 예외 분기가 없고 `typename`은 실수·정수 분기에서만 정해진다.
- 46: `isloaded`는 라이브러리 경로를 따옴표 없이 셸 명령에 삽입하며 `lsof`·`grep`에 의존한다.
- 252: shape 비교에는 `array(value).shape`를 쓰지만 assert 메시지에는 원래 `value.shape`를 사용한다.
- 4–10·136: 가져온 `as_array`, `zeros`, `subprocess`와 설정 후의 지역 `result`는 이후 실행 코드에서 사용하지 않는다.
- 200–205: rank 0 또는 양수를 처리하지만 음수 rank용 예외 문자열에는 허용 rank가 `(0, 2)`로 적혀 있다.
