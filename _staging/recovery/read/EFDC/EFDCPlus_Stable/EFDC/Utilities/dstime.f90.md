---
file: models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/Utilities/dstime.f90
lines: 96
sha256: 30939f4fe92887bb00c7f9691ca2a6983f7e062630c29a07c225f6eb237f5d3e
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# dstime.f90 — 판독 구간 기록

구간은 1행부터 96행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–26 | EFDC+ 안내·저작권·GPLv2 머리말(1–8). 초 단위 시간 함수 `REAL*8 FUNCTION DSTIME(IOPTION)` (9), GLOBAL에서 NTHREADS·RKD·IK4 사용(12). 전처리 조건 `#ifndef GNU` (13)에서 IFPORT를 사용한다(14). OMP_LIB·MPI 사용(16–17), 입력 IOPTION과 TARR·TPMC·STATIC LASTTIME·CPUSEC·save allocatable STARTEDD 선언(19–25). |
| 27–41 | 시작 시 9행 DSTIME 함수 안. 반환값을 0으로 초기화한다(27). 원문 조건은 `if( .not. allocated(STARTEDD) )then` (29). 참이면 STARTEDD(0:3)를 할당하고 0으로 초기화한다(30–31). 전처리 `#ifdef GNU` (33)에서는 `call CPU_TIME(TPMC)` (34) 결과를 STARTEDD(1)에 복사한다(35). `#else` (36)에서는 `STARTEDD(1) = RTC()` (38). 이 초기화 조건을 끝낸다(40). |
| 42–59 | 시작 시 9행 DSTIME 함수 안이며 29행 조건 밖. 전처리 `#ifdef GNU` (42)에서는 `call CPU_TIME(TPMC)` (44), `DSTIME = DBLE(TPMC)-STARTEDD(1)` (45). 스레드 수로 나누는 대체식은 주석이다(46). `#else` (47)에서는 `if( IOPTION == 0 )then` (49). 그 분기의 `#ifdef DEBUGGING` (51)은 `DSTIME = MPI_WTIME()` (52), `#else` (53)는 `DSTIME = omp_get_wtime()` (54). 56–58행 CPU 시간 대체 코드는 주석이다. |
| 60–75 | 시작 시 9행 함수·47행 비-GNU 전처리 분기 안이며 49행 if의 다음 분기에서 시작한다. 원문은 `elseif( IOPTION == 1 )then` (60). 이 분기에서 `CPUSEC = RTC()` (62), `DSTIME = CPUSEC - STARTEDD(1)` (63). 병렬 분기 `elseif( IOPTION == 2 )then` (65)는 `TPMC = DTIME(TARR)` (67), `DSTIME = DBLE(TPMC)/DBLE(NTHREADS)` (68). 이 분기 내부 `if( DSTIME < 0.0 )then` (70)은 `DSTIME = ABS(DSTIME)` (71). 별도 단일행 원문은 `if( DSTIME < LASTTIME)DSTIME = LASTTIME` (73). LASTTIME에 반환값을 복사한다(74). |
| 76–96 | 시작 시 9행 함수·47행 비-GNU 전처리 분기 안이며 49행 if의 다음 분기에서 시작한다. `elseif( IOPTION == 3 )then` (76)은 `TPMC = DTIME(TARR)` (78), `DSTIME = DBLE(TARR(1))/DBLE(NTHREADS)` (80), `if( DSTIME < LASTTIME ) DSTIME = LASTTIME` (81), LASTTIME 복사(82). `elseif( IOPTION == 4 )then` (84)은 `#ifdef DEBUGGING` (86)에서 `DSTIME = MPI_WTIME()` (87), `#else` (88)에서 `DSTIME = omp_get_wtime()` (89). 조건과 전처리 종료(91–92), return·빈 줄·함수 종료(93–96). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 22·70–82: STATIC LASTTIME 선언에는 초기값이 없다. IOPTION=2·3 분기는 LASTTIME을 조건식에서 읽은 뒤 현재 DSTIME을 복사한다.
- 25·30–38: STARTEDD는 0:3으로 할당하지만, 0 초기화 이후 개별 값을 설정하고 읽는 인덱스는 1뿐이다.
- 42–45·49–91: GNU 경로에는 IOPTION 분기가 없다. 비-GNU 경로의 IOPTION 조건에는 0·1·2·3·4 이외 값을 처리하는 else가 없다.
