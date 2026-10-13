---
file: models/ROMS/raw/source_code/roms/ROMS/Utility/mp_routines.F
lines: 178
sha256: 61deca32c1c6f16d83fbe4336bbe2c71afce09dc4e97bace4b6a2a027513ae68
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# mp_routines.F — 판독 구간 기록

구간은 1행부터 178행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–23 | 전처리 조건 밖. `#include "cppdefs.h"` (1)로 cppdefs.h를 끼워 넣는다. 저작권·MIT/X 방식 라이선스·License_ROMS.md 참조와 구분 주석(2–9). 병렬 처리(multi-processing) 보조 루틴 my_getarg·my_getpid·my_numthreads·my_threadnum·my_wtime의 반환 목적을 설명하는 주석(10–22), 빈 줄(23). |
| 24–57 | 시작 시 전처리 조건 밖. `#ifdef DISTRIBUTE` (24)에서만 `my_getarg(Iarg,Carg)`를 정의한다(27–55). mod_kinds를 사용하고 `# if defined NAGFOR` (31)일 때 f90_unix_env를 사용한다(32). `# endif` (33). Iarg는 입력 정수, Carg는 입출력 문자열이며 Lstr·ierror는 지역 정수(39–44). `# ifdef CRAY` (48)이면 `CALL pxfgetarg (Iarg, Carg, Lstr, ierror)` (49). `# else` (50)이면 `CALL getarg (Iarg, Carg)` (51). `# endif` (52). 반환과 루틴 종료(54–55), `#endif` (56), 주석(57). |
| 58–86 | 시작 시 전처리 조건 밖. my_getpid 함수와 mod_kinds·implicit none 선언(58–67). `#if defined NAGFOR` (63)에서 f90_unix_env를 사용한다(64). `#endif` (65). `#ifndef NAGFOR` (69)에서 getpid를 정수로 선언한다(70). `#endif` (71). `#if defined CRAYX1` (76)은 `my_getpid=0` (77). `#elif defined CYGWIN` (78)도 `my_getpid=0` (79). `#else` (80)는 `my_getpid=getpid()` (81). `#endif` (82), 반환·함수 종료·주석(84–86). |
| 87–118 | 시작 시 전처리 조건 밖. my_numthreads 함수는 병렬 영역의 지속 실행 스레드(Persistent Execution Thread, PET) 수를 반환한다는 주석과 선언(87–99). `#ifdef DISTRIBUTE` (100)이면 `my_numthreads=1` (101). `#elif defined _OPENMP` (102)이면 omp_get_max_threads를 정수로 선언하고 `my_numthreads=omp_get_max_threads()` (106). omp_get_num_threads 선언·호출은 주석 처리(104·107). `#elif defined SGI` (108)이면 mp_numthreads를 선언하고 `my_numthreads=mp_numthreads()` (111). `#else` (112)는 `my_numthreads=1` (113). `#endif` (114), 반환·함수 종료·주석(116–118). |
| 119–146 | 시작 시 전처리 조건 밖. my_threadnum 함수 선언·병렬 영역에서 실행 중인 PET 번호 설명(119–131). `#if defined _OPENMP` (132)이면 omp_get_thread_num를 정수로 선언하고 `my_threadnum=omp_get_thread_num()` (135). `#elif defined SGI` (136)이면 mp_my_threadnum을 선언하고 `my_threadnum=mp_my_threadnum()` (139). `#else` (140)는 `my_threadnum=0` (141). `#endif` (142), 반환·함수 종료·주석(144–146). |
| 147–178 | 시작 시 전처리 조건 밖. my_wtime(wtime) 함수는 real(r8) 길이 2 인수와 실수 반환값을 선언한다(148–156). `#ifdef _OPENMP` (157)에서 omp_get_wtime을 선언한다(158). `#endif` (159). `#ifdef CRAYX1` (160)에서 count·count_rate·count_max를 선언한다(161). `#endif` (162). 주석은 임의 과거 시점부터의 경과 벽시계 시간(wall time), 단위 초로 설명한다(164–165). `#if defined _OPENMP` (167)은 `my_wtime=omp_get_wtime()` (168). `#elif defined CRAYX1` (169)은 `CALL system_clock (count, count_rate, count_max)` (170)와 `my_wtime=REAL(count,r8)/REAL(count_rate,r8)` (171). `#else` (172)는 `CALL cpu_time (wtime(1))` (173)와 `my_wtime=wtime(1)` (174). `#endif` (175), 반환·함수 종료(177–178). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 44·49–55: CRAY 분기의 pxfgetarg는 Lstr·ierror를 받는다. 이 루틴에는 반환된 ierror를 검사하는 문장이 없다.
- 76–82: CRAYX1·CYGWIN 분기는 프로세스 ID를 조회하지 않고 반환값을 0으로 설정한다.
- 100–114: DISTRIBUTE 분기의 my_numthreads 반환값은 1이다. 이 분기는 _OPENMP·SGI 분기보다 먼저 선택된다.
- 155·173–174: my_wtime 인수 wtime은 길이 2로 선언한다. 이 파일에서 접근하는 원소는 wtime(1)이다.
- 164–175: my_wtime 설명 주석은 wall time이라고 적는다. 기본 분기의 호출은 cpu_time이다.
- 170–171: CRAYX1 분기는 system_clock의 count_rate로 나눈다. 이 분기에는 count_rate 값의 조건 검사가 없다.
