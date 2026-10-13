---
file: models/ROMS/raw/source_code/roms/ROMS/Nonlinear/WEC/wec_wave_mix.F
lines: 209
sha256: 9f9dc50bb6dd4a727da94cb467762a20f339ae3a163f506e066dfa2af8244abc
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# wec_wave_mix.F — 판독 구간 기록

구간은 1행부터 209행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–47 | `cppdefs.h`를 포함하고 wec_wave_mix_mod를 연다(1–2). SOLVE3D/WEC/WAVE_MIXING이 모두 정의된 경우 파랑 유도 혼합(wave-induced mixing)의 수직 점성(vertical viscosity) 기여를 계산한다(3·12–13). 주석은 Uchiyama 등(2010)을 제시한다(17–20). 모듈과 exchange_w3d_tile을 가져온다(24–36). DIAGNOSTICS_UV와 DISTRIBUTE가 추가 사용을 제어한다(26–28·37–39). wec_wave_mix를 공개한다(41–46). 원문 조건·루프·계산식·전처리 행: `#include "cppdefs.h"` (1); `#if defined SOLVE3D && defined WEC && defined WAVE_MIXING` (3); `# if defined DIAGNOSTICS_UV` (26); `# endif` (28); `# ifdef DISTRIBUTE` (37); `# endif` (39). |
| 48–84 | 시작 시 `#if defined SOLVE3D && defined WEC && defined WAVE_MIXING` (3) 안. wec_wave_mix가 ng/tile을 입력받는다(49–54). `tile.h`를 포함하며 PROFILE에서 wclock_on/off를 호출한다(61–65·78–80). wec_wave_mix_tile에 쇄파 소산(breaking dissipation)·백파 소산(whitecapping dissipation), 조건부 롤러 소산(roller dissipation), Hwave와 Hz/z_r/z_w 및 Akv를 전달한다(66–77). RETURN과 루틴 종료를 포함한다(82–84). 원문 조건·루프·계산식·전처리 행: `      character (len=*), parameter :: MyFile =                          &` (58); `     &  __FILE__` (59); `# include "tile.h"` (61); `# ifdef PROFILE` (63); `# endif` (65); `# ifdef WEC_ROLLER` (70); `# endif` (72); `# ifdef PROFILE` (78); `# endif` (80). |
| 85–125 | 시작 시 `#if defined SOLVE3D && defined WEC && defined WAVE_MIXING` (3) 안. wec_wave_mix_tile의 인수와 정수 경계를 선언한다(86–102). WEC_ROLLER는 Dissip_roller 인수를 추가한다(90–92). ASSUMED_SHAPE 참·else는 입력 배열과 intent(inout) Akv의 하한형·명시적 배열 형태를 나눈다(103–125). Akv의 수직 하한은 0이다(113·124). 원문 조건·루프·계산식·전처리 행: `# ifdef WEC_ROLLER` (90); `# endif` (92); `# ifdef ASSUMED_SHAPE` (103); `#  ifdef WEC_ROLLER` (106); `#  endif` (108); `# else` (114); `#  ifdef WEC_ROLLER` (117); `#  endif` (119); `# endif` (125). |
| 126–144 | 시작 시 `#if defined SOLVE3D && defined WEC && defined WAVE_MIXING` (3) 안. 시작 시 86행 wec_wave_mix_tile 루틴 안. 정수와 계수를 선언한다(129–130). eps=1.0E-14, sinb=0.1, Cb=0.002를 parameter로 고정한다(131–133). 수심·역수·분포 계수와 정규화 역수 작업 배열을 선언한다(134–137). `set_bounds.h`를 포함한다(139). 혼합 계산 머리말을 포함한다(141–144). 원문 조건·루프·계산식·전처리 행: `      real(r8), parameter :: eps = 1.0E-14_r8` (131); `      real(r8), parameter :: sinb=0.1_r8` (132); `      real(r8), parameter :: Cb=0.002_r8` (133); `# include "set_bounds.h"` (139). |
| 145–165 | 시작 시 `#if defined SOLVE3D && defined WEC && defined WAVE_MIXING` (3) 안. 시작 시 86행 wec_wave_mix_tile 루틴 안. 내부 수평 셀에서 z_w 차로 수심과 역수를 구한다(145–151). gamr는 수심/파고 비의 계수이며 MIN으로 상한 1을 적용한다(155–157). k=1:N(ng)에서 바닥 기준 상대 높이·gamr의 COSH를 Hz로 적분한다(158–162). 적분값에 eps를 더한 역수를 oroller에 대입한다(163). 두 수평 루프를 닫는다(164–165). 원문 조건·루프·계산식·전처리 행: `      DO j=Jstr,Jend` (145); `        DO i=Istr,Iend` (146); `          Dstp(i,j)=z_w(i,j,N(ng))-z_w(i,j,0)` (150); `          oDstp(i,j)=1.0_r8/Dstp(i,j)` (151); `          oroller(i,j)=0.0_r8` (155); `          gamr(i,j)=MIN(0.707_r8*Dstp(i,j)/                             &` (156); `     &              (1.25_r8*Hwave(i,j)+eps),1.0_r8)` (157); `          DO k=1,N(ng)` (158); `            cff2=(z_r(i,j,k)-z_w(i,j,0))*oDstp(i,j)*gamr(i,j)` (159); `            oroller(i,j)=oroller(i,j)+Hz(i,j,k)*                        &` (160); `     &                   COSH(2.0_r8*pi*cff2)` (161); `          oroller(i,j)=1.0_r8/(oroller(i,j)+eps)` (163). |
| 166–188 | 시작 시 `#if defined SOLVE3D && defined WEC && defined WAVE_MIXING` (3) 안. 시작 시 86행 wec_wave_mix_tile 루틴 안. k=1:N(ng)에서 fac1=0.5*sqrt(2)를 계산하고 내부 셀을 순회한다(170–173). 상대 높이와 gamr로 cosh 수직 분포를 구한다(174–176). cff1은 Dissip_break이다(178). wec_alpha 보정 소산의 1/3 제곱을 cff4로 계산한다(179). WEC_ROLLER는 Dissip_roller의 1/3 제곱을 더한다(180–182). Cb·cff4·fac1·Hwave·수심·분포·정규화 역수의 곱을 Akv에 추가한다(183–185). 세 루프를 닫는다(186–188). 원문 조건·루프·계산식·전처리 행: `      DO k=1,N(ng)` (170); `        fac1=0.5_r8*SQRT(2.0_r8)` (171); `        DO j=Jstr,Jend` (172); `          DO i=Istr,Iend` (173); `            fac2=(z_r(i,j,k)-z_w(i,j,0))*oDstp(i,j)` (174); `            cff2=fac2*gamr(i,j)` (175); `            cff3=COSH(2.0_r8*pi*cff2)` (176); `            cff1=Dissip_break(i,j)` (178); `            cff4=((1.0_r8-wec_alpha(ng))*cff1)**(1.0_r8/3.0_r8)` (179); `# ifdef WEC_ROLLER` (180); `            cff4=cff4+(Dissip_roller(i,j))**(1.0_r8/3.0_r8)` (181); `# endif` (182); `            Akv(i,j,k)=Akv(i,j,k)+                                      &` (183); `     &                 Cb*cff4*fac1*Hwave(i,j)*                         &` (184); `     &                 Dstp(i,j)*cff3*oroller(i,j)` (185). |
| 189–209 | 시작 시 `#if defined SOLVE3D && defined WEC && defined WAVE_MIXING` (3) 안. 시작 시 86행 wec_wave_mix_tile 루틴 안. 주기 경계(periodic boundary)가 있으면 exchange_w3d_tile을 Akv의 수직 범위 0:N(ng)에 호출한다(192–196). DISTRIBUTE에서는 mp_exchange3d에 Akv·유령 격자(ghost points)·주기 설정을 전달한다(197–204). RETURN·루틴·최상위 조건·모듈 종료를 포함한다(205–209). 원문 조건·루프·계산식·전처리 행: `      IF (EWperiodic(ng).or.NSperiodic(ng)) THEN` (192); `# ifdef DISTRIBUTE` (197); `# endif` (204); `#endif` (208). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 129·132: numits와 it는 선언 이후 사용되지 않는다. sinb는 parameter 선언 이후 사용되지 않는다.
- 105·116·177–178: Dissip_wcap은 입력 선언에 있다. Dissip_wcap+Dissip_break 식은 주석이다. 실행 대입은 Dissip_break만 사용한다.
- 150–151·156–157: oDstp는 수심의 역수를 직접 구하며 분모에 eps가 없다. gamr는 MIN으로 상한 1만 적용한다.
- 170–185·192–203: Akv 기여 대입은 k=1:N(ng)에서 수행한다. 경계 교환 범위는 0:N(ng)이다.
- 179–181: 소산 기여에 1/3 실수 제곱을 사용한다. 이 블록에는 해당 밑을 MAX로 제한하거나 부호를 검사하는 조건이 없다.
- 26–28: DIAGNOSTICS_UV에서 mod_diags를 가져온다. 이 파일에는 진단 배열 실행 대입이 없다.
