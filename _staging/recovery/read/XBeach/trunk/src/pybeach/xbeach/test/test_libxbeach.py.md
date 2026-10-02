---
file: models/XBeach/raw/source_code/trunk/src/pybeach/xbeach/test/test_libxbeach.py
lines: 175
sha256: 6d94d3af0ab796105b4e5d966419d62f00a141913a3b0b5e7559609c52437ed5
reader: codex gpt-6.1-sol
read_date: 2026-10-02
---

# test_libxbeach.py — 판독 구간 기록

구간은 1행부터 175행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–37 | `unittest2`를 우선 가져오고 실패하면 `unittest`로 대체한다(5–8). nose·래퍼·NumPy와 DEBUG 로거를 준비하고 Matplotlib 대화형 모드를 켠다(9–24). 라이브러리 접미사는 기본 `.so`, darwin `.dylib`, Windows `.dll`(26–29); 라이브러리와 사례 경로는 `__file__` 기준 `../../../xbeachlibrary/.libs/libxbeach.0…`, `../../../../../branches/rewind/data/example1`로 고정한다(30–37). |
| 38–76 | `TestXBeach.setUp`에서 지정 경로로 래퍼를 만들고 `init`, `tearDown`에서 `finalize`를 호출한다(38–50). 매개변수 수≥224, 인덱스 0=`depfile`, 20=`disch_timeseries_file`, 이름 `disch_loc_file` 포함을 검사한다(51–59). 형은 eps=`r`, morfacopt=`i`, depfile=`c`; 값은 0.005·1·`z.grd`를 기대한다(60–73). 전체 매개변수는 길이≥224만 검사한다(74–76). |
| 77–90 | 매개변수 설정 검사: `g=9.81`과 `nx=707`을 읽고 변경 시 `ValueError` 및 원래 값 유지를 기대한다(79–85). `t≥0` 확인 후 `t=1.0` 설정의 반환값 None과 조회값 1.0을 검사하고 `t=0.0`으로 되돌린다(87–90). |
| 91–117 | 배열 이름·전체 배열 수≥30, `zb` 실수형·`wetz` 정수형을 검사한다(91–95·106–108). 초기값 `zb[0,0]=-19.96`, `wetz[0,0]=1`, `dy=dx=0.0`, zb 차원 길이 708·1 및 shape `(708,1)`을 기대한다(96–105). 읽은 모든 배열을 `set_array`로 다시 넣는다(109–112). 한 timestep 뒤 `t>0`을 검사한다(113–115); 끝에 빈 줄이 있다(116–117). |
| 118–139 | `IntegrationTest`도 생성·초기화/정리 루틴을 동일하게 호출한다(118–130). `test_rewind`에서 첫 timestep을 실행한 후 `get_arrays`를 deepcopy하여 `t0_arrays`에 저장하고 시간 `told`를 보관한다(131–138). 배열이 XBeach 메모리를 직접 가리킨다는 주석이 있다(132). |
| 140–175 | `tnext=10`으로 설정하고 `t<tnext` 동안 `executestep`, `output`, `tnext` 재설정을 반복한다(141–146). 첫 결과 `t1a`·배열을 저장한 뒤 `t=told`와 저장 배열을 복구한다(147–154). 같은 루프를 재실행해 `t1b`·배열을 저장한다(156–165). 키 집합 일치를 assert하며(167), 비어 있지 않은 ndarray는 절대차의 max, 그 외는 절대차를 구한다(168–172). 차가 `0.00001`보다 크면 이름과 차를 `print`한다(173–174). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 30–37·51–105: 라이브러리·사례 경로와 개수·인덱스·격자 크기·초기값 기대치가 코드에 고정되어 있다.
- 147·161: `t1a`, `t1b`는 저장되지만 이후 비교나 assert에 사용하지 않는다.
- 167–174: rewind 결과의 키 집합은 assert하지만 수치 차가 `0.00001`을 넘는 경우에는 출력만 하고 수치 일치 assert를 호출하지 않는다.
- 169–172: 크기 0 ndarray는 else에서 배열 절대차를 만들고, 다음 행에서는 `if maxdiff > 0.00001` 조건에 사용한다.
- 9·24: 가져온 `with_setup`, `time`은 이후 코드에서 사용하지 않는다.
- 174: 출력 구문은 `print name, maxdiff` 형식이다.
