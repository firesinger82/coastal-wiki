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
| 1–37 | os/sys·copy·collections 가져오기(1–4); unittest2 시도(5–6), ImportError면 unittest(7–8), nose with_setup·libxbeach·NumPy·logging(9–12). DEBUG logger(14–18), matplotlib interactive(True)(22–23), time(24). 접미사 기본 .so·darwin .dylib·win32/win64 .dll(26–29). XBEACHLIB는 ../../../xbeachlibrary/.libs/libxbeach.0+접미사(30–33), WD는 ../../../../../branches/rewind/data/example1(34–37). 접미사 원문: `dllsuffix = collections.defaultdict(lambda:'.so')` (26), `dllsuffix['darwin'] = '.dylib'` (27), `dllsuffix['win32'] = '.dll'` (28), `dllsuffix['win64'] = '.dll'` (29). 경로 계산 원문: `XBEACHLIB = os.path.join(` (30); `os.path.dirname(__file__),` (31); `'../../../xbeachlibrary/.libs/libxbeach.0' + dllsuffix[sys.platform]` (32); `)` (33). `WD = os.path.join(` (34); `os.path.dirname(__file__),` (35); `'../../../../../branches/rewind/data/example1'` (36); `)` (37). |
| 38–76 | TestXBeach setUp은 XBeach(libpath,workingdir)·init(39–47), tearDown은 finalize(48–50). nparameter·이름 수>=224(52·58), 0번 depfile·20번 disch_timeseries_file(54–55), disch_loc_file 포함(59). eps/morfacopt/depfile 타입 r/i/c(60–66); 값 0.005/1/'z.grd'(67–73), get_parameters 크기>=224(74–76). 테스트 기대값이며 모델 전체 기본값으로 일반화하지 않는다. |
| 77–115 | set_parameter 테스트는 g=9.81·nx=707 설정 예외와 값 유지(79–85), t>=0 후 1.0 설정/확인·0.0 재설정, setter 반환 None(87–90). 배열 이름 수>=30(92), zb/wetz 타입 r/i(94–95), 첫 값 -19.96/1 및 dy/dx=0(97–100), zb 차원 708·1/shape(708,1)(102–105), 전체 배열 수>=30(108). 모든 배열을 같은 값으로 set_array(110–112). executestep 후 t>0(114–115). |
| 116–150 | 빈 줄(116–117), IntegrationTest의 setUp XBeach·init(119–127), tearDown finalize(128–130). rewind에서 첫 timestep(135), 전체 배열 deepcopy·told 저장(136–137). `tnext = 10` (141), tnext 설정(142). `while self.xb.get_parameter('t') < tnext:` (143) 안 executestep·output·tnext 재설정(144–146); 루프 뒤 t1a·배열 deepcopy(147–149), 빈 줄(150). |
| 151–175 | t=told 복구(151), t0_arrays의 모든 배열 set_array(152–153). tnext 설정(156), `while self.xb.get_parameter('t') < tnext:` (157) 안 executestep·output·tnext 재설정(158–160); 루프 뒤 t1b·배열 deepcopy(161–165). 배열 키 집합 동일 assert(167). 이름 루프(168)의 `if isinstance(t1a_arrays[name], np.ndarray) and t1a_arrays[name].size > 0:` (169) 참 분기 `maxdiff = np.abs(t1a_arrays[name]- t1b_arrays[name]).max()` (170); `else:` (171)에서 `maxdiff = np.abs(t1a_arrays[name]- t1b_arrays[name])` (172). 앞 if 종료 뒤 같은 루프 안 독립 `if maxdiff > 0.00001:` (173)일 때 print name,maxdiff(174); 마지막 공백 줄(175). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 30–37: 라이브러리와 fixture 경로는 상대 경로의 .libs/libxbeach.0 및 branches/rewind/data/example1로 고정되어 있다.
- 132·136·149·165·libxbeach.py 235: 테스트 주석은 배열이 XBeach 메모리를 직접 가리킨다고 적고, getter의 반환은 array(arrayp)이다.
- 147·161: t1a·t1b를 저장하지만 두 값에 대한 assert는 없다.
- 167–174: 키 집합은 assert하지만 값 차이는 0.00001 초과 시 출력하며 assert하지 않는다.
- 9·24: with_setup·time을 가져오지만 이후 이 파일에서 쓰지 않는다.
