---
file: models/SWAN/raw/source_code/swan/src/m_constants.ftn90
lines: 52
sha256: 19387730e5269a971c592cde3ee1cab2d89beb0445ce003d00d2645fecf1bebc
reader: codex gpt-6.1-sol
read_date: 2026-10-12
---

# m_constants.ftn90 — 판독 구간 기록

구간은 1행부터 52행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–15 | 구분 주석·m_constants 시작(1–3). 물리 상수(physical constants) 주석(5), 중력의 제곱근 sqrtg·제곱 gsq·물의 동점성계수(kinematic viscosity) nu 선언(7–9). 물·공기 밀도(density) d_water/d_air(11–12), SWAN DEPMIN과 같은 임계 수심(threshold depth) trshdep 선언(14). 이 구간의 real 선언에는 초기값이 없다. |
| 16–27 | 시작 시 2행 m_constants 모듈 안. 수학 상수(mathematical constants) 주석(16). pih의 `pi/2` 주석, 도→라디안 변환 dera, 라디안→도 변환 rade, exp 함수 인수의 하한·상한 expmin/expmax, √2 변수 sqrt2의 의미를 선언 주석으로 적는다(18–23). CONTAINS(25), 주석·구분선(24·26–27). expmin 주석은 언더플로 방지를 적는다(21). expmax 주석은 오버플로 방지를 적는다(22). sqrt2 주석은 `square root of 2 ~ 1.41`이다(23). [10-13 전수 검증 정정] [10-13 전수 검증 보완] |
| 28–39 | 시작 시 2행 모듈 안. init_constants 시작(28), SWCOMM3 사용(31). 각도 상수는 `pih  = 0.5*PI` (33); `dera = PI/180.` (34); `rade = 180./PI` (35). 지수 함수(exponential function) 인수의 하한·상한 설정은 `expmin = -20.` (37); `expmax =  20.` (38)이며 -20..20이다. 주석·빈 줄을 포함한다. |
| 40–49 | 시작 시 2행 모듈·28행 init_constants 루틴 안. 물리 상수 계산·설정은 `sqrtg   = sqrt(GRAV)` (42); `gsq     = GRAV*GRAV` (43); `nu      = 1.e-6` (44); `d_air   = PWIND(16)` (45); `d_water = PWIND(17)` (46). nu는 1.e-6로 고정하고 공기·물 밀도는 PWIND(16:17)에서 복사한다. 임계 수심 설정은 `trshdep = DEPMIN` (48). 주석·빈 줄을 포함한다. |
| 50–52 | 시작 시 2행 모듈·28행 init_constants 루틴 안에서 루틴 종료(50). 주석(51), 모듈 종료(52). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 23·28–50: sqrt2는 real 변수로 선언되어 있다. init_constants에는 sqrt2에 값을 대입하는 실행문이 없다.
- 2–52: 이 파일에는 IMPLICIT NONE, PRIVATE, PUBLIC 또는 PARAMETER 선언이 없다. 이름이 constants인 모듈의 값들은 real 변수로 선언되어 있다.
- 37–44: expmin=-20, expmax=20, nu=1.e-6은 init_constants에서 고정값으로 설정한다.
