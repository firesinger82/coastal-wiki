---
file: models/FUNWAVE/raw/source_code/FUNWAVE-TVD/src/mod_param.F
lines: 93
sha256: bded43978218a19bce766578bdf4cdbc329055dcc7b7b921989dc9094fa0f17f
reader: codex gpt-6.1-sol
read_date: 2026-10-17
---

# mod_param.F — 판독 구간 기록

구간은 1행부터 93행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–52 | mod_param.F·FUNWAVE-TVD 소속·2016년 저작권·Simplified BSD 재배포 조건·무보증 머리말(1–44). 고정 매개변수(parameter)를 정의하는 PARAM 모듈의 목적·2010년 이력·루틴 변경에 맞춘 모듈 갱신 설명(45–51). 빈 줄(52). 이 구간은 전처리 조건 밖이다. |
| 53–69 | `MODULE PARAM` (53). `# if defined PARALLEL` (54) 참 구간에서만 USE MPI (55)를 포함하고 `# endif` (56). IMPLICIT NONE (57). `# if defined DOUBLE_PRECISION` (58) 참 구간은 `INTEGER, PARAMETER::SP=8` (59)이며, 그 안의 `# if defined PARALLEL` (60) 참 구간만 `INTEGER, PARAMETER::MPI_SP=MPI_DOUBLE_PRECISION` (61)을 정의하고 `# endif` (62). 58행의 `# else` (63)는 DOUBLE_PRECISION 미정의 분기로 `INTEGER, PARAMETER::SP=SELECTED_REAL_KIND(6,30)` (64)을 선택한다. 그 안의 `# if defined PARALLEL` (65) 참 구간만 `INTEGER, PARAMETER::MPI_SP=MPI_REAL` (66)을 정의하며 `# endif` (67). `# endif` (68)로 정밀도 분기를 닫는다. 따라서 PARALLEL 미정의 시 두 정밀도 분기 모두 MPI_SP를 정의하지 않는다. SELECTED_REAL_KIND 인수는 정밀도 6·지수 범위 30이다. |
| 70–81 | 시작 시 53행 PARAM 모듈 안이며 정밀도 전처리 분기 밖이다. 모든 플래그 조합에서 다음 상수를 선언한다. `REAL(SP), PARAMETER::pi=3.141592653` (71), `REAL(SP), PARAMETER::R_earth = 6371000.0_SP` (72), `REAL(SP), PARAMETER::SMALL=0.000001_SP` (73), `REAL(SP), PARAMETER::LARGE=999999.0_SP` (74), `REAL(SP), PARAMETER:: grav=9.81_SP` (75), `REAL(SP), PARAMETER:: zero = 0.0_SP` (76), `REAL(SP), PARAMETER:: RHO_AW = 0.0012041_SP  ! relative to water` (77), `REAL(SP), PARAMETER:: RHO_AIR = 1.15_SP  ! absolute value` (78), `REAL(SP), PARAMETER:: RHO_WATER = 1000.0_SP` (79), `REAL(SP), PARAMETER:: DEG2RAD = 0.0175_SP` (80). 주석은 RHO_AW를 물에 대한 상대값, RHO_AIR를 절대값으로 설명한다. 매개변수 구분 주석과 빈 줄(70·81). |
| 82–93 | 시작 시 53행 PARAM 모듈 안이다. 전역 작업 변수 I·J·K·RES·itmp1..itmp5·tmp1..tmp5 선언(82–85). `# if defined (ITERATION)` (87) 참 구간에서는 Nwogu 방식처럼 최대 반복 횟수(iteration count)를 2로 둔다는 주석(88), `INTEGER :: ITER_NUM = 2` (89), `REAL(SP) :: ERRORi = 0.0001_SP` (90). 두 값은 PARAMETER가 아닌 초기값이 있는 모듈 변수이다. `# endif` (91). ITERATION 미정의 시 두 변수를 제외하며 `#else`는 없다. 이 선택은 PARALLEL·DOUBLE_PRECISION과 독립이다. 빈 줄과 모듈 종료(86·92–93). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 71–80: pi의 숫자 리터럴에는 _SP 접미사가 없다. 같은 블록의 나머지 실수 상수에는 _SP 접미사가 있다.
- 80: DEG2RAD는 pi를 사용하는 식이 아니라 0.0175_SP 리터럴로 정의되어 있다.
- 83–85·89–90: 전역 작업 변수 선언에는 초기값이 없다. ITERATION 구간의 ITER_NUM·ERRORi에는 초기값이 있다.
