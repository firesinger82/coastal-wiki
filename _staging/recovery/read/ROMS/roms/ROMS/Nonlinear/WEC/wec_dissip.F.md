---
file: models/ROMS/raw/source_code/roms/ROMS/Nonlinear/WEC/wec_dissip.F
lines: 188
sha256: 88dedde2d5d018f0641339dd04f12deb8d8cdde051cc6f5b8d28e49a09156964
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# wec_dissip.F — 판독 구간 기록

구간은 1행부터 188행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–30 | `#include "cppdefs.h"` (1)로 cppdefs.h를 포함하고 `wec_dissip_mod` 모듈을 시작한다(2). `#if defined SOLVE3D && (defined WDISS_THORGUZA \|\| \` (4), `                        defined WDISS_CHURTHOR)` (5)가 이하 구현을 감싼다. 저작권·MIT/X 라이선스 주석(7–12), 쇄파(breaking)와 백파(whitecapping) 소산(dissipation) 계산 목적 주석(14–17), Thornton와 Guza(1986) 및 Church와 Thornton(1993) 참고문헌 주석(19–29)을 포함한다. |
| 31–53 | 시작 시 4–5행 `#if defined SOLVE3D && (defined WDISS_THORGUZA \|\| \` / `                        defined WDISS_CHURTHOR)` 안. mod_param·mod_forces·mod_grid·mod_ocean·mod_scalars·exchange_2d_mod를 사용한다(31·35–40). `# if defined DIAGNOSTICS_UV` (32), `# endif` (34)는 mod_diags 사용(33)을 감싼다. bc_r2d_tile을 가져온다(42). `# ifdef DISTRIBUTE` (43), `# endif` (45)는 mp_exchange2d 가져오기(44)를 감싼다. implicit none·PRIVATE·공개 wec_dissip·CONTAINS 선언(47–52)과 주석을 포함한다. |
| 54–84 | 시작 시 4–5행 SOLVE3D 및 두 소산 옵션의 `#if` 안. `wec_dissip(ng, tile)` 진입(55), 입력 정수·MyFile 선언(58–63). `# include "tile.h"` (65)로 tile.h를 포함한다. `# ifdef PROFILE` (67), `# endif` (69)는 `CALL wclock_on (ng, iNLM, 43, __LINE__, MyFile)` (68)을 감싼다. wec_dissip_tile에 타일(tile) 경계·수직 크기 N(ng)·작업 경계·h·zeta·Hwave·Pwave_top·두 소산 배열을 전달한다(70–77). `# ifdef PROFILE` (78), `# endif` (80)는 `CALL wclock_off (ng, iNLM, 43, __LINE__, MyFile)` (79)을 감싼다. RETURN·루틴 종료·주석(81–84). |
| 85–129 | 시작 시 4–5행 SOLVE3D 및 두 소산 옵션의 `#if` 안. `wec_dissip_tile` 진입과 인수 선언(86–97). `# ifdef ASSUMED_SHAPE` (98)의 가정 형상(assumed shape) 선언에는 h·zeta·Hwave·Pwave_top 입력과 두 소산 inout 배열이 있다(99–104). `# else` (105)의 명시 형상 선언에는 h·zeta·Pwave_top과 두 소산 배열이 있다(106–110). `# endif` (111). 지역 i/j·cff1/cff2·fac1/sigmat/Dstp 선언(115–117). `# if defined WDISS_CHURTHOR` (118), `# endif` (120)는 RB1/RB2 선언(119)을 감싼다. 상수는 `real(r8), parameter :: gammaw=0.31_r8` (121), `real(r8), parameter :: eps = 1.0E-14_r8` (122). `# include "set_bounds.h"` (124)로 set_bounds.h를 포함한다. 소산 계산 머리말·빈 줄·주석(123–129). |
| 130–149 | 시작 시 4–5행 SOLVE3D 및 두 소산 옵션의 `#if`·86행 wec_dissip_tile 안. `fac1=3.0_r8*g*SQRT(pi)/16.0_r8` (130). `DO j=Jstr,Jend` (131), `DO i=Istr,Iend` (132)에서 `Dstp=zeta(i,j,1)+h(i,j)` (136), `cff1=0.707_r8*Hwave(i,j)` (137), `sigmat=MIN(1.0_r8/(Pwave_top(i,j)+eps),1.0_r8)` (138). `# ifdef WDISS_THORGUZA` (140)의 Thornton–Guza 경로에서 `cff2=1.0_r8/((gammaw**4.0_r8)*(Dstp**5.0_r8))` (145), `Dissip_break(i,j)=0.2621_r8*fac1*sigmat*                      &` (146), `     &                     (cff1**7.0_r8)*cff2` (147). Dissip_wcap은 0으로 설정한다(148). 계산 설명 주석과 빈 주석도 포함한다. |
| 150–164 | 시작 시 4–5행 SOLVE3D 및 두 소산 옵션의 `#if`·86행 루틴·131행 j 루프·132행 i 루프·140행 `# ifdef WDISS_THORGUZA` 안. `# elif defined WDISS_CHURTHOR` (150)가 Church–Thornton 대체 경로를 연다. `cff2=1.0_r8/(gammaw*Dstp)` (155), `RB1=1.0_r8+TANH(8.0_r8*((cff1*cff2)-1.0_r8))` (156), `RB2=1.0_r8-(1.0_r8+(cff1*cff2)**2.0_r8)**(-2.5_r8)` (157), `Dissip_break(i,j)=(0.2621_r8/Dstp)*fac1*sigmat*               &` (158), `     &                      (cff1**3.0_r8)*RB1*RB2` (159). Dissip_wcap은 0으로 설정한다(160). `# endif` (161)와 두 루프 종료(162–163), 주석·빈 줄을 포함한다. |
| 165–188 | 시작 시 4–5행 SOLVE3D 및 두 소산 옵션의 `#if`·86행 wec_dissip_tile 안이며 두 격자 루프 밖. `# if defined WDISS_THORGUZA \|\| defined WDISS_CHURTHOR` (165), `# endif` (175)는 경계조건(boundary condition) 호출을 감싼다. bc_r2d_tile을 Dissip_break(169–171)와 Dissip_wcap(172–174)에 각각 호출한다. `# ifdef DISTRIBUTE` (176), `# endif` (183)는 `mp_exchange2d` 호출(178–182)을 감싼다. 전달값은 iNLM·필드 수 2·타일 경계·NghostPoints·EWperiodic/NSperiodic·두 소산 배열이다. RETURN·루틴 종료(185–186), 바깥 `#endif` (187), 모듈 종료(188) 및 주석을 포함한다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 89·101·105–111·137: Hwave는 루틴 인수이며 계산에 사용된다. ASSUMED_SHAPE 분기에는 Hwave 선언이 있고, 그 else의 명시 형상 선언에는 Hwave 선언이 없다.
- 136·145·155·158: Dstp는 zeta(i,j,1)+h(i,j)로 계산된다. Dstp를 분모에 쓰기 전에 양수 하한을 적용하는 문장은 이 루틴에 없다.
- 122·138: eps는 파주기 Pwave_top의 분모에 더해진다. sigmat에는 MIN으로 상한 1.0_r8을 적용하고, 하한을 적용하는 문장은 없다.
- 148·160: 두 소산 공식 분기 모두 Dissip_wcap을 0.0_r8로 설정한다.
- 140·150: WDISS_THORGUZA와 WDISS_CHURTHOR 계산 경로는 하나의 ifdef/elif 구조로 배치되어 있다. 두 옵션이 함께 정의되면 앞의 WDISS_THORGUZA 경로가 선택된다.
