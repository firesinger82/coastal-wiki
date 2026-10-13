---
file: models/ROMS/raw/source_code/roms/ROMS/Utility/ADfromTL.F
lines: 260
sha256: c79d689c346725f63a1d974ae1d793f2b4a8de22a531426955f13c063362a293
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# ADfromTL.F — 판독 구간 기록

구간은 1행부터 260행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–41 | `#include "cppdefs.h"` (1)은 cppdefs.h를 끼워 넣는다. 모듈 시작·빈 줄(2–3), `#if defined SP4DVAR` (4). 저작권·라이선스·빈 주석과 접선선형(tangent linear, TL) 상태로 수반(adjoint, AD) 상태를 초기화한다는 설명(5–16). implicit none·private·공개 ADfromTL·contains(17–22). ADfromTL 입구, mod_param/mod_clima/mod_grid/mod_ocean/mod_stepping 사용, ng/tile 입력 선언(23–39). `# include "tile.h"` (40)은 tile.h를 끼워 넣는다. 빈 주석(41). |
| 42–77 | 시작 시 4행 `#if defined SP4DVAR`·25행 `ADfromTL` 안. `CALL ADfromTL_tile` (42–73)에 공간 경계와 Lold(ng)/knew(ng)(43–45)을 넘긴다. `# ifdef SOLVE3D` (46)은 nstp(ng)(47), `# endif` (48). `# ifdef MASKING` (49)은 GRID의 rmask/umask/vmask(50–52), `# endif` (53). `# ifdef SOLVE3D` (54)은 OCEAN의 tl_u/tl_v/tl_t(55–57), `# endif` (58). `# ifndef SOLVE3D` (59)은 tl_ubar/tl_vbar(60–61), `# endif` (62). tl_zeta(63)는 공통이다. `# ifdef SOLVE3D` (64)은 ad_u/ad_v/ad_t(65–67), `# endif` (68). `# ifndef SOLVE3D` (69)은 ad_ubar/ad_vbar(70–71), `# endif` (72). ad_zeta로 인수 목록 종료(73), 빈 줄·RETURN·래퍼 종료·빈 주석(74–77). |
| 78–118 | 시작 시 4행 `#if defined SP4DVAR` 안. `ADfromTL_tile` 입구와 공간 경계·Linp/kout 인수(78–82). `# ifdef SOLVE3D` (83)은 nout(84), `# endif` (85). `# ifdef MASKING` (86)은 rmask/umask/vmask(87), `# endif` (88). `# ifdef SOLVE3D` (89)은 tl_u/tl_v/tl_t(90), `# endif` (91). `# ifndef SOLVE3D` (92)은 tl_ubar/tl_vbar(93), `# endif` (94). tl_zeta(95)는 공통이다. `# ifdef SOLVE3D` (96)은 ad_u/ad_v/ad_t(97), `# endif` (98). `# ifndef SOLVE3D` (99)은 ad_ubar/ad_vbar(100), `# endif` (101). ad_zeta와 구분 주석(102–104), mod_param/mod_ncparam/mod_scalars 사용·정수 입력 선언(105–114). `# ifdef SOLVE3D` (115)은 nout 선언(116), `# endif` (117), 빈 주석(118). |
| 119–144 | 시작 시 4행 `#if defined SP4DVAR`·79행 `ADfromTL_tile` 안. `# ifdef ASSUMED_SHAPE` (119), `#  ifdef MASKING` (120)은 하한 LBi:/LBj:인 rmask/umask/vmask 입력(121–123), `#  endif` (124). `#  ifdef SOLVE3D` (125)은 tl_u/tl_v 4차원과 tl_t 5차원 intent(inout)(126–128), `#  endif` (129). `#  ifndef SOLVE3D` (130)은 tl_ubar/tl_vbar 3차원(131–132), `#  endif` (133). 공통 tl_zeta 3차원(134). `#  ifdef SOLVE3D` (135)은 ad_u/ad_v/ad_t(136–138), `#  endif` (139). `#  ifndef SOLVE3D` (140)은 ad_ubar/ad_vbar(141–142), `#  endif` (143). 공통 ad_zeta 3차원(144). |
| 145–178 | 시작 시 4행 `#if defined SP4DVAR`·119행 `# ifdef ASSUMED_SHAPE`·79행 루틴 안. `# else` (145)에서 `#  ifdef MASKING` (146)은 LBi:UBi/LBj:UBj 마스크 선언(147–149), `#  endif` (150). `#  ifdef SOLVE3D` (151)은 tl_u/tl_v의 수직 크기 N(ng)·시간 크기 2와 tl_t의 N(ng)·시간 크기 3·NT(ng)(152–154), `#  endif` (155). `#  ifndef SOLVE3D` (156)은 `real(r8), intent(inout) :: tl_ubar(LBi:UBi,LBj:UBj,:)` (157), `real(r8), intent(inout) :: tl_vbar(LBi:UBi,LBj:UBj,:)` (158), `#  endif` (159). `real(r8), intent(inout) :: tl_zeta(LBi:UBi,LBj:UBj,:)` (160). `#  ifdef SOLVE3D` (161)은 같은 크기의 ad_u/ad_v/ad_t(162–164), `#  endif` (165). `#  ifndef SOLVE3D` (166)은 `real(r8), intent(inout) :: ad_ubar(LBi:UBi,LBj:UBj,:)` (167), `real(r8), intent(inout) :: ad_vbar(LBi:UBi,LBj:UBj,:)` (168), `#  endif` (169). `real(r8), intent(inout) :: ad_zeta(LBi:UBi,LBj:UBj,:)` (170), `# endif` (171). i/itrc/j/k 지역 정수·빈 줄과 주석(172–176), `# include "set_bounds.h"` (177)은 set_bounds.h를 끼워 넣는다. 빈 주석(178). |
| 179–192 | 시작 시 4행 `#if defined SP4DVAR`·79행 루틴 안. 주석은 TL 상태의 record 1로 초기화한다고 적는다(179–182). 자유수면(free surface) 주석(183–184), `DO j=JstrR,JendR` (185), `DO i=IstrR,IendR` (186)에서 ad_zeta의 kout에 tl_zeta의 Linp를 복사(187)한다. `#ifdef MASKING` (188): `ad_zeta(i,j,kout)=ad_zeta(i,j,kout)*rmask(i,j)` (189). `#endif` (190), 두 루프 종료(191–192). |
| 193–214 | 시작 시 4행 `#if defined SP4DVAR`·79행 루틴 안. `#ifndef SOLVE3D` (193)은 2차원 운동량(momentum) 경로이다. `DO j=JstrR,JendR` (197), `DO i=Istr,IendR` (198)에서 ad_ubar의 kout에 tl_ubar의 Linp를 복사(199)한다. `#ifdef MASKING` (200): `ad_ubar(i,j,kout)=ad_ubar(i,j,kout)*umask(i,j)` (201). `#endif` (202), 루프 종료·빈 주석(203–205). `DO j=Jstr,JendR` (206), `DO i=IstrR,IendR` (207)에서 ad_vbar의 kout에 tl_vbar의 Linp를 복사(208)한다. `#ifdef MASKING` (209): `ad_vbar(i,j,kout)=ad_vbar(i,j,kout)*vmask(i,j)` (210). `#endif` (211), 루프 종료(212–213), `#endif` (214). |
| 215–240 | 시작 시 4행 `#if defined SP4DVAR`·79행 루틴 안. `# ifdef SOLVE3D` (215)은 3차원 운동량 경로이다. `DO k=1,N(ng)` (219), `DO j=JstrR,JendR` (220), `DO i=Istr,IendR` (221)은 ad_u의 nout에 tl_u의 Linp를 복사(222)한다. `#ifdef MASKING` (223): `ad_u(i,j,k,nout)=ad_u(i,j,k,nout)*umask(i,j)` (224). `#endif` (225), 세 루프 종료·빈 주석(226–229). `DO k=1,N(ng)` (230), `DO j=Jstr,JendR` (231), `DO i=IstrR,IendR` (232)은 ad_v의 nout에 tl_v의 Linp를 복사(233)한다. `#ifdef MASKING` (234): `ad_v(i,j,k,nout)=ad_v(i,j,k,nout)*vmask(i,j)` (235). `#endif` (236), 세 루프 종료·빈 주석(237–240). |
| 241–260 | 시작 시 4행 `#if defined SP4DVAR`·215행 `# ifdef SOLVE3D`·79행 루틴 안. 추적자(tracer) 주석(241–242), `DO itrc=1,NT(ng)` (243), `DO k=1,N(ng)` (244), `DO j=JstrR,JendR` (245), `DO i=IstrR,IendR` (246)은 ad_t의 nout에 tl_t의 Linp를 복사(247)한다. `#ifdef MASKING` (248): `ad_t(i,j,k,nout,itrc)=ad_t(i,j,k,nout,itrc)*rmask(i,j)` (249). `#endif` (250), 네 루프 종료(251–254), `# endif` (255). 빈 줄·RETURN·루틴 종료(256–258), `#endif` (259), 모듈 종료(260). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 45·82·114·180·187·199·208·222·233·247: 초기화 주석은 TL의 record 1이라고 적는다. 실제 원본 인덱스는 인수 Linp이다. 래퍼는 그 인수에 Lold(ng)를 넘긴다.
- 145–170: ASSUMED_SHAPE의 else 분기에서 3차원 u/v/t는 모든 차원의 상한을 지정한다. 같은 분기의 2차원 운동량·자유수면 선언은 앞의 두 차원을 LBi:UBi/LBj:UBj로 쓰고 마지막 차원을 `:`로 쓴다.
- 126–134·152–160·187–249: TL 배열은 intent(inout)으로 선언된다. 이 파일의 실행문은 TL 배열을 읽어 AD 배열에 복사하며 TL 배열에는 대입하지 않는다.
