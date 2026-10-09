---
file: models/ADCIRC/raw/source_code/adcirc/src/constants.F90
lines: 147
sha256: f8c6c7f4394b3d1a6d251bdf2cd0be82f841cd05c2f26a3f5908f239fbfb633d
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# constants.F90 — 판독 구간 기록

구간은 1행부터 147행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–34 | ADCIRC 저작권 1994–2025, LGPL 3 이상·무보증·라이선스 안내(1–19). ADC_CONSTANTS의 작성자·저작권·용도 주석(20–29). 물리 상수와 변환 계수를 보유하며 입력에서 변경할 수 있는 물리 상수를 제외하고 parameter로 선언해야 한다는 원문 주석(30–32). 구분 주석·빈 줄 포함(33–34). |
| 35–72 | `module ADC_CONSTANTS`·implicit none·public(35–39). 중력 가속도(gravitational acceleration)의 변경 가능한 기본값은 `real(8) :: g = 9.80665d0` (46). 공칭 물 밀도(nominal water density)는 `real(8), parameter :: RhoWat0 = 1000.0d0` (49), 기준 밀도의 sigma-T는 `real(8), parameter :: SigT0 = RHOWAT0 - 1000.0d0` (52). 대기압 기본 상수는 `real(8), parameter :: PRBCKGRND = 1013.0d0` (55)이며 1013.25D0 대안은 주석이다(56). 배경 온도는 `real(8), parameter :: TBCKGRND = 288.15d0` (59), 기체 상수(specific gas constant)는 `real(8), parameter :: RAir = 287.058d0` (62). 실행 중 변경 가능한 공기 밀도 기본값은 `real(8) :: RhoAir = 1.293d0` (67). 이상 기체 법칙(ideal gas law)·kg/m³ 주석과 1.15D0·1.1774D0 대안 주석·빈 줄을 포함한다(64–72). |
| 73–82 | 수학 상수 원문은 `real(8), parameter :: PI = 3.141592653589793d0` (73), `real(8), parameter :: TWOPI = PI*2.d0` (74), `real(8), parameter :: HFPI = PI/2.d0` (75), `real(8), parameter :: e = 2.718281828459045d0` (76). 지구 반지름(earth radius, m)은 `real(8), parameter :: Rearth = 6378206.4d0` (79). `real(8), parameter :: omega = 7.29212d-5` (81). 설명 주석과 빈 줄 포함(77–78·80·82). |
| 83–94 | 시간 변환 계수(time conversion factor) 원문: `real(8), parameter :: hour2sec = 3600.0d0` (84), `real(8), parameter :: sec2hour = 1.0d0/hour2sec` (85), `real(8), parameter :: day2hour = 24.0d0` (86), `real(8), parameter :: hour2day = 1.0d0/day2hour` (87), `real(8), parameter :: day2sec = day2hour*hour2sec` (88), `real(8), parameter :: sec2day = 1.0d0/day2sec` (89), `real(8), parameter :: hour2min = 60.d0` (91), `real(8), parameter :: min2hour = 1.d0/hour2min` (92), `real(8), parameter :: min2day = 1.d0*min2hour*hour2day;` (93). 절 제목 주석·빈 줄 포함(83·90·94). |
| 95–117 | 행성 경계층(planetary boundary layer) 상단 풍속을 지표 풍속으로 줄이는 계수는 `real(8), parameter :: windReduction = 0.9d0` (99). 1.0D0·0.78D0은 주석 처리된 대안이다(100–102). 1분·10분 풍속 변환은 `real(8), parameter :: one2ten = 0.8928d0 !... Powell et al 1996` (105), `real(8), parameter :: ten2one = 1.0d0/one2ten` (108). 1.00D0·0.8787D0은 주석이다(106–107). 30분·1분 변환은 `real(8), parameter :: thirty2one = 1.165d0 !...Luettich` (111), `real(8), parameter :: one2thirty = 1.0d0/thirty2one` (112). 30분·10분 변환은 `real(8), parameter :: thirty2ten = 1.04d0 !...Luettich` (115), `real(8), parameter :: ten2thirty = 1.0d0/thirty2ten` (116). 설명 주석·빈 줄 포함. |
| 118–127 | 파랑 모델로 전달하는 풍속의 배율 기본값은 `real(8) :: waveWindMultiplier = 1.0d0` (119). 파랑 응력 경사(wave stress gradient) 크기의 상한 기본값은 `real(8) :: WaveStressGrad_Cap = 1000.0d0` (122). 각도·거리 변환은 `real(8), parameter :: DEG2RAD = PI/180.0d0` (124), `real(8), parameter :: RAD2DEG = 180.0d0/PI` (125), `real(8), parameter :: MPERDEG = REarth*PI/180.0d0` (126). 설명 주석·빈 줄 포함(118·120–121·123·127). |
| 128–137 | 길이·속력 변환은 `real(8), parameter :: nm2m = 1852.0d0 ! nautical miles to meters` (129), `real(8), parameter :: m2nm = 1.0d0/nm2m ! meters to nautical miles` (130), `real(8), parameter :: kt2ms = nm2m/3600.0d0 ! knots to m/s` (131), `real(8), parameter :: ms2kt = 1.0d0/kt2ms ! m/s to knots` (132). 압력 변환은 `real(8), parameter :: mb2pa = 100.0d0` (135), `real(8), parameter :: pa2mb = 1.0d0/mb2pa` (136). 절 제목 주석·빈 줄 포함(128·133–134·137). |
| 138–147 | 분산(dispersion) 절은 실행 중 변경 가능한 수심 지수·계수·수중 음속을 선언한다(138–143). 원문은 `real(8) :: Bd = 0.23394d0 !...Exponent of Depth` (140), `real(8) :: Ad = 0.0050189d0 !...Coefficient of Depth` (141), `real(8) :: Cs = 1500.0d0 !...Speed of sound in water` (142). Cs2는 음속 제곱이라는 주석이 붙은 초기값 없는 변수다(143). 고정 계수는 `real(8), parameter :: TwoB = 2d0*0.4779d0` (144), `real(8), parameter :: GM2 = 3.486d0**2.0d0` (145). 빈 줄·모듈 종료 포함(146–147). 이 파일에는 실행 루틴·조건 분기·호출문이 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 55–56: 실제 PRBCKGRND 상수는 1013.0d0이다. 1013.25D0 표준 대기압 대안은 주석 처리되어 있다.
- 142–143: Cs는 1500.0d0으로 초기화한다. Cs2 선언에는 초기값이 없으며 이 파일에 Cs2 대입식이 없다.
- 140·144: Bd는 변경 가능한 변수이며 초기값은 0.23394d0이다. TwoB는 Bd를 참조하지 않고 2d0*0.4779d0으로 선언된 parameter다.
