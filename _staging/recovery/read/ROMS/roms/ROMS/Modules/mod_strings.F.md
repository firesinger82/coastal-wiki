---
file: models/ROMS/raw/source_code/roms/ROMS/Modules/mod_strings.F
lines: 285
sha256: fb485593dc897d336db586faeb0dc752afe5cef30aeb17445f119d8745c29b37
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# mod_strings.F — 판독 구간 기록

구간은 1행부터 285행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–38 | 시작 시 열린 전처리 조건 없음. `#include "cppdefs.h"` (1)로 `cppdefs.h`를 끼워 넣고 `mod_strings` 모듈을 연다(2). 저작권·MIT/X 라이선스 주석(4–9). 컴파일러(compiler)·플래그·실행 제목·C 전처리(preprocessing) 옵션과 코드 실행시간 계측(profiling) 영역 번호의 설명 주석(11–17). StateMsg 설명은 1–18번 상태 판독 메시지를 열거한다(19–37). 초기·이전 상태, 수반 상태(adjoint state), 표면 외력(surface forcing)·개방 경계 조건(open boundary condition, OBC) 증분, 접선 선형(tangent linear) 모델 오차 외력, 충격 외력(impulse forcing), v-space 증분·배경 상태, 상관 표준편차(correlation standard deviation), 정규화 계수(normalization factor), 안장점(saddle-point) Arnoldi 상태 벡터를 설명한다. 마지막 빈 주석행 포함(38). |
| 39–98 | 시작 시 열린 전처리 조건 없음·2행 모듈 안. Pregion 실행시간 계측 영역 1–59번의 설명 주석이다(39–98). 1–11은 메모리 할당·상태 초기화·입출력 처리·경계 조건·전역 적분·2차원 계산·라그랑주 부유체 궤적(Lagrangian float trajectory)·조석 외력(tidal forcing) 영역이다(40–50). 12–20은 2차원/3차원 결합, 수직 격자 계량(vertical metric), 오메가 수직 속도(Omega vertical velocity), 해수 상태 방정식(equation of state), 생물·퇴적물·대기해양 플럭스(flux)·KPP/GLS/My2.5 연직 혼합(vertical mixing) 영역이다(51–59). 21–35는 3차원 우변(right-hand side)·예측 단계(predictor step), 압력 경도(pressure gradient), 추적자(tracer)의 조화·이중 조화 혼합(harmonic/biharmonic mixing), 응력 텐서(stress tensor), 운동량·추적자 보정 단계(corrector step)이다(60–74). 36–44는 중첩(nesting), 저층 경계층(bottom boundary layer), GST 고유문제, 대기·해빙·파랑 양방향 결합(two-way coupling), 해빙·해류에 대한 파랑 효과·침수/노출 식생 계산 영역이다(75–83). 45–59는 Unused 01–15로 적혀 있다(84–98). |
| 99–132 | 시작 시 열린 전처리 조건 없음·2행 모듈 안. Pregion 주석의 60–73은 메시지 전달(message passage) 영역이다(99–112). 2/3/4차원 격자 주변부 교환(halo exchange), 측면 경계 교환, 자료 방송(broadcast)·축약(reduction)·수집(gathering)·분산(scattering), 경계·점·중첩 자료 수집, 동기화 장벽(synchronization barrier), 다중 모델 결합을 열거한다. 74–79는 Unused 01–06이다(113–118). 80–88은 4차원 변분 자료동화(four-dimensional variational data assimilation, 4D-Var)의 상태 벡터 입출력, 사전·사후 오차 공분산 행렬(error covariance matrix), 전조건화(pre-conditioning), 최소화 풀이, 배경·증분·분석 단계이다(119–127). 89–90도 Unused 01–02로 적는다(128–129). 닫는 설명 주석·구분선까지 포함한다(130–132). |
| 133–162 | 시작 시 열린 전처리 조건 없음·2행 모듈 안. `implicit none` (133). title의 길이는 80, Coptions의 길이는 2048이다(135–136). 상수 선언 원문은 `integer, parameter :: Fregion = 80      ! start of 4D-Var region` (138), `integer, parameter :: Mregion = 60      ! start of mpi-region` (139), `integer, parameter :: Nregion = 88` (140)이다. StateMsg는 길이 48의 문자열 19개를 선언과 동시에 채운다(142–161). 1–18은 앞의 상태 설명에 대응하며(143–160), 19번 문자열은 `'cummulative increments for IAU,                 '`이다(161). 각 메시지 문자열은 쉼표와 공백을 포함한다. 끝 주석행 포함(162). |
| 163–200 | 시작 시 열린 전처리 조건 없음·2행 모듈 안. Pregion은 길이 50의 문자열 배열이며 차원은 Nregion이다(163). 배열 생성자(array constructor)의 1–37번 문자열을 채운다(164–200). 1–11은 메모리·상태·입출력·경계·적분·2차원 계산·부유체·조석 영역 이름이다(164–174). 12–20은 결합·수직 속도·상태 방정식·생물·퇴적물·대기해양 플럭스·연직 혼합 영역 이름이다(175–183). 21–35는 3차원 식·압력 경도·추적자 혼합·응력·보정 단계 이름이다(184–198). 36–37은 중첩과 저층 경계층 이름이다(199–200). 문자열 끝은 점으로 채운다. 이 구간은 선언 시 문자열 초기화이며 계산 루틴 호출이 없다. |
| 201–222 | 시작 시 열린 전처리 조건 없음·2행 모듈·163행 Pregion 배열 생성자 안. 38–44번은 GST 고유문제, 대기·해빙·파랑 결합, 해빙, 해류에 대한 파랑 효과, 침수/노출 수생 식생 계산 이름이다(201–207). 45–59번은 Unused 01–15 문자열이다(208–222). 배열 생성자는 다음 구간까지 이어진다. |
| 223–252 | 시작 시 열린 전처리 조건 없음·2행 모듈·163행 Pregion 배열 생성자 안. 60–73번은 격자 주변부·경계 교환, 방송·축약·수집·분산, 경계·점·중첩 자료 수집, 장벽·다중 모델 결합 이름이다(223–236). 74–79번은 Unused 01–06이다(237–242). 80–88번은 4D-Var 상태 벡터 판독·출력, 사전·사후 공분산, 전조건화, 최소화, 배경·증분·분석 단계 문자열이다(243–251). 88번 문자열에서 배열 생성자를 닫는다(251). 마지막 주석행 포함(252). |
| 253–263 | 시작 시 열린 전처리 조건 없음·2행 모듈 안. 운영체제(operating system), CPU, 컴파일 시스템·명령·플래그, 디렉터리·헤더 정보를 C 전처리 중 대입한다는 주석(253–256). 원문 선언은 `character (len=80)  :: my_os = MY_OS` (258), `character (len=80)  :: my_cpu = MY_CPU` (259), `character (len=80)  :: my_fort = MY_FORT` (260), `character (len=80)  :: my_fc = MY_FC` (261), `character (len=512) :: my_fflags = MY_FFLAGS` (262)이다. 끝 주석행 포함(263). |
| 264–273 | 시작 시 열린 전처리 조건 없음·2행 모듈 안. `#ifdef ANALYTICAL_DIR` (264)에서는 `character (len=256) :: Adir = ANALYTICAL_DIR` (265)이다. `#else` (266)에서는 `character (len=256) :: Adir = "NONE"` (267)이며 `#endif` (268)로 닫는다. 별도 `#ifdef HEADER_DIR` (269)에서는 `character (len=256) :: Hdir = HEADER_DIR` (270)이다. `#else` (271)에서는 `character (len=256) :: Hdir = "NONE"` (272)이며 `#endif` (273)로 닫는다. 디렉터리 매크로가 없을 때 기본 문자열은 NONE이다. |
| 274–285 | 시작 시 열린 전처리 조건 없음·2행 모듈 안. `#ifdef ROMS_HEADER` (274)에서는 `character (len=256) :: Hfile = HEADER` (275)이다. `#else` (276)에서는 `character (len=256) :: Hfile = "NONE"` (277)이며 `#endif` (278)로 닫는다. 별도 `#ifdef ROOT_DIR` (279)에서는 `character (len=256) :: Rdir = ROOT_DIR` (280)이다. `#else` (281)에서는 `character (len=256) :: Rdir = "NONE"` (282)이며 `#endif` (283)로 닫는다. 마지막 주석·모듈 종료(284–285). 이 파일에는 실행 루틴이 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 19–37·142–161: StateMsg 머리말은 18개 상태를 설명한다. 실제 선언은 dimension(19)이며 19번에 IAU 증분 문자열을 추가한다.
- 128–129·140·163–251: Pregion 머리말에는 89–90번 Unused 영역이 있다. 실제 Nregion 값과 Pregion 초기 문자열 수는 88이다.
- 274–275: Hfile 선언을 선택하는 조건은 ROMS_HEADER 매크로이다. Hfile에 대입하는 매크로 이름은 HEADER이다. 이 파일에는 두 매크로의 정의가 없다.
