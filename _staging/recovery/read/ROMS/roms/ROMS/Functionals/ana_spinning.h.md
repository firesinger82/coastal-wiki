---
file: models/ROMS/raw/source_code/roms/ROMS/Functionals/ana_spinning.h
lines: 146
sha256: 982fadfcd826183795457424ef1017f1e095785b1cca7d09ee5ddfc91b1c1b3f
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# ana_spinning.h — 판독 구간 기록

구간은 1행부터 146행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–58 | ana_spinning의 머리말은 극좌표(polar coordinate) 환형 격자(annulus grid)의 시간 가변 코리올리(Coriolis)·구심(centripetal) 가속도 합을 설명한다(2–15). param·grid·ncparam, 입력 인수·MyFile을 선언한다(17–28). 30행은 tile.h를 끼워 넣는다. ana_spinning_tile에 SPHERICAL의 lonr·latr 또는 xr·yr 및 f·omn·fomn을 넘긴다(32–44). DISTRIBUTE 조건에 따라 ANANAME(26)에 MyFile을 저장하고 끝낸다(48–58). 원문 조건·대입·전처리 행: `character (len=*), parameter :: MyFile =                          &` (27), `&  __FILE__` (28), `#include "tile.h"` (30), `#ifdef SPHERICAL` (35), `#else` (38), `#endif` (41), `#ifdef DISTRIBUTE` (48), `IF (Lanafile) THEN` (49), `#else` (50), `IF (Lanafile.and.(tile.eq.0)) THEN` (51), `#endif` (52), `ANANAME(26)=MyFile` (53), `END IF` (54). |
| 59–103 | ana_spinning_tile의 인수 목록은 SPHERICAL에 따라 좌표를 바꾼다(60–68). param·scalars와 입력 인수를 선언한다(71–78). ASSUMED_SHAPE·SPHERICAL에 따라 입력 f·omn·좌표와 출력 fomn의 경계를 선언한다(80–102). SPHERICAL 인수 연속행의 실제 표기도 인용한다(64). 원문 조건·대입·전처리 행: `#ifdef SPHERICAL` (63), `&                              lonr, latr                          &` (64), `#else` (65), `#endif` (67), `#ifdef ASSUMED_SHAPE` (80), `# ifdef SPHERICAL` (83), `# else` (86), `# endif` (89), `#else` (91), `# ifdef SPHERICAL` (94), `# else` (97), `# endif` (100), `#endif` (102). |
| 104–125 | 시작 시 60행 ana_spinning_tile 안. LAB_CANYON에서 Omega0=2*pi/25·Width=0.20·Ro=0.10·Rs=0.55·little_omega=2*pi/24·Bu=10·hd=0.125를 parameter로 선언한다(106–113). 시간 가변 회전과 밀도경사 지역변수를 선언한다(115–117). 119행은 set_bounds.h를 끼워 넣는다. 회전력 계산 주석과 빈 줄을 포함한다(121–125). 원문 조건·대입·전처리 행: `#ifdef LAB_CANYON` (106), `real(r8), parameter :: Omega0 = 2.0_r8*pi/25.0_r8` (107), `real(r8), parameter :: Width = 0.20_r8` (108), `real(r8), parameter :: Ro = 0.10_r8` (109), `real(r8), parameter :: Rs = 0.55_r8` (110), `real(r8), parameter :: little_omega = 2.0_r8*pi/24.0_r8` (111), `real(r8), parameter :: Bu = 10.0_r8` (112), `real(r8), parameter :: hd = 0.125_r8` (113), `#endif` (117), `#include "set_bounds.h"` (119). |
| 126–146 | 시작 시 60행 ana_spinning_tile 안. LAB_CANYON에서 fcor·Omega1·Ro_t·d_rho_dz를 계산한다(126–130). 사인식 time_fac·Omega1_of_t와 코사인식 d_Omega1_dt를 계산한다(131–133). 모든 타일 지점의 fomn은 f*time_fac와 반경에 회전 항을 곱한 값을 더하고 omn을 곱한다(135–142). LAB_CANYON을 닫고 RETURN·루틴 종료를 포함한다(143–146). 원문 조건·대입·전처리 행: `#ifdef LAB_CANYON` (126), `fcor=2.0_r8*Omega0` (127), `Omega1=fcor*Width*Ro/Rs` (128), `Ro_t=little_omega/fcor` (129), `d_rho_dz=(1000.0_r8*Bu/g)*(fcor*Width/hd)**2` (130), `time_fac=1.0_r8+(Omega1/Omega0)*SIN(little_omega*time(ng))` (131), `Omega1_of_t=Omega1*SIN(little_omega*time(ng))` (132), `d_Omega1_dt=Omega1*little_omega*COS(little_omega*time(ng))` (133), `DO j=JstrT,JendT` (135), `DO i=IstrT,IendT` (136), `fomn(i,j)=(f(i,j)*time_fac+                                   &` (137), `&               SQRT(xr(i,j)*xr(i,j)+yr(i,j)*yr(i,j))*             &` (138), `&               ((2.0_r8*Omega0+Omega1_of_t)*Omega1_of_t))*        &` (139), `&              omn(i,j)` (140), `END DO` (141), `END DO` (142), `#endif` (143). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 63–68: SPHERICAL 인수 목록의 “lonr, latr” 연속행은 latr 뒤에 쉼표가 없다. 다음 인수 행은 f·omn·fomn이다.
- 63–101·137–139: SPHERICAL에서는 lonr·latr를 인수로 선언한다. LAB_CANYON 계산식은 xr·yr를 참조한다. 이 파일에는 두 옵션을 배타적으로 검사하는 전처리 행이 없다.
- 129–133: Ro_t·d_rho_dz·d_Omega1_dt는 계산되지만 이후 fomn 식에서 참조되지 않는다.
- 126–143: fomn 대입은 LAB_CANYON 조건 안에만 있다. 이 파일에는 LAB_CANYON 이외의 대입 분기가 없다.
