---
file: models/ROMS/raw/source_code/roms/ROMS/Functionals/ana_dqdsst.h
lines: 130
sha256: ec7ad1093b5b1c8eb0b62c4438285e4a2ff71ce6b99807e16cca9dd6af67b259
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# ana_dqdsst.h — 판독 구간 기록

구간은 1행부터 130행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–55 | ana_dqdsst 시작(2), 저작권·라이선스(4–9). 해수면 온도(sea surface temperature, SST)에 대한 순 열 플럭스(net heat flux) 민감도(sensitivity)를 W/m²/degC에서 rho0*Cp로 나눠 m/s/degC로 바꾼다는 주석(11–15). 보정 주석 식 `!       Q_model ~ Q + dQdSST * (T_model - SST)                         !` (17). 모듈·인수·MyFile 선언(21–33), `#include "tile.h"` (35)로 tile.h를 끼워 넣는다. ana_dqdsst_tile에 GRID(ng)%Hz와 FORCES(ng)%dqdt 전달(37–41). `#ifdef DISTRIBUTE` (45)의 `IF (Lanafile) THEN` (46), `#else` (47)의 `IF (Lanafile.and.(tile.eq.0)) THEN` (48), `#endif` (49) 뒤 ANANAME(38)=MyFile(50). 조건 종료·RETURN·루틴 종료·주석(51–55). |
| 56–93 | ana_dqdsst_tile 시작(57–60), 모듈과 exchange_r2d_tile 사용(63–67). `#ifdef DISTRIBUTE` (68)에서 mp_exchange2d 사용(69), `#endif` (70). 인수 선언(74–76), `#ifdef ASSUMED_SHAPE` (78)는 Hz·dqdt assumed-shape 배열(79–80), `#else` (81)는 Hz의 수직 범위 1:N(ng)와 명시 크기 dqdt(82–83), `#endif` (84). i·j·fac 선언(88–90), `#include "set_bounds.h"` (92)로 set_bounds.h를 끼워 넣는다. 주석·빈 줄 포함. |
| 94–111 | 시작 시 57행 ana_dqdsst_tile 안. 민감도 단위 주석(95), `#ifdef MY_APPLICATION` (98). `fac=day2sec/30.0_r8            ! 30 day relaxation scale 1/s/decC` (99)는 원문 주석에 30일 이완 시간 척도(relaxation time scale)라고 적는다. j·i 루프(100–101)에서 `dqdt(i,j)=fac*Hz(i,j,N(ng))` (102). `#else` (105)의 j·i 루프(106–107)에서 `dqdt(i,j)=???` (108). 루프 종료(103–104·109–110), `#endif` (111). |
| 112–130 | 시작 시 57행 ana_dqdsst_tile 안. 경계 교환(boundary exchange) 주석(113–114). `IF (EWperiodic(ng).or.NSperiodic(ng)) THEN` (115)이면 exchange_r2d_tile(...,dqdt) 호출(116–118). `#ifdef DISTRIBUTE` (121)에서 mp_exchange2d(...,1,...,NghostPoints,EWperiodic(ng),NSperiodic(ng),dqdt) 호출(122–126), `#endif` (127). RETURN·루틴 종료(129–130). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 99: 실행식은 fac=day2sec/30.0_r8이다. 같은 행 주석은 30 day relaxation scale 1/s/decC라고 적는다. day2sec 정의는 이 판독에 포함하지 않았다.
- 98–111: MY_APPLICATION이 아닌 분기의 dqdt 대입 우변은 ???이다.
- 11–12·17: 설명 주석은 민감도를 dQdSTT로 적는다. 보정식 주석은 dQdSST로 적는다.
