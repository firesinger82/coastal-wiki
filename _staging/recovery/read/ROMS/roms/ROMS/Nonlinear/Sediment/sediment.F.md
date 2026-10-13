---
file: models/ROMS/raw/source_code/roms/ROMS/Nonlinear/Sediment/sediment.F
lines: 197
sha256: 9264bba4523c55a0b3a64bfa6b4626e704b817819e431cb91fd4092c4a5d2ccc
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# sediment.F — 판독 구간 기록

구간은 1행부터 197행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–29 | `#include "cppdefs.h"` (1)는 cppdefs.h를 삽입한다. 빈 줄·sediment_mod 모듈 시작(2–4), `#if defined NONLINEAR && defined SEDIMENT` (5). 저작권·MIT/X 라이선스와 퇴적물 수송(sediment transport) 주 구동 루틴 설명(6–28). 주석은 수직 침강(settling), 침식(erosion)·퇴적(deposition), 다중 입경, 층서(stratigraphy), 지형 변화(morphology), Meyer Peter Mueller 및 Soulsby 소류사(bed load), 경사 항 문헌을 열거한다. |
| 30–76 | 시작 시 5행 `#if defined NONLINEAR && defined SEDIMENT` 안. 해수 RHO 중심/W 경계는 바닥에서 수면으로 1..N/0..N, 퇴적층은 표면 아래 1..Nbed로 나열한 도식 주석(30–59). Warner 등 2008 문헌 주석(60–68), implicit none·기본 PRIVATE·sediment 공개·CONTAINS·구분 주석(69–76). |
| 77–97 | 시작 시 5행 `#if defined NONLINEAR && defined SEDIMENT` 안. sediment(ng,tile) 시작(77–79). `# if defined COHESIVE_BED  \|\| defined MIXED_BED` (80)은 sed_bed_cohesive 사용, `# elif defined NONCOHESIVE_BED2` (82)는 sed_bed2, `# else` (84)는 sed_bed 사용, `# endif` (86). `# if defined BEDLOAD` (87) 안 `#  if defined BEDLOAD_SOULSBY \|\| defined BEDLOAD_MPM` (88)은 sed_bedload 사용, `#  elif defined BEDLOAD_VANDERA` (90)는 mod_vandera_funcs와 sed_bedload_vandera 사용, `#  endif` (93), `# endif` (94). `# if defined SED_BIODIFF` (95)·`# endif` (97)는 sed_biodiff 사용을 감싼다. |
| 98–118 | 시작 시 sediment(77행)·5행 `#if defined NONLINEAR && defined SEDIMENT` 안. `# ifdef SUSPLOAD` (98) 안 sed_fluxes/sed_settling 사용(99–100), `#  if defined SED_FLOCS` (101)·`#  endif` (103) 안 sed_flocmod 사용(102), `# endif` (104). `# if defined SEDTR_REACTIONS` (105) 안 `#  if defined SEDBIO_COUP` (106)은 sedtr_reactions_pom 사용, `#  elif defined SEDTR_DECAY` (108)는 sedtr_decay 사용, `#  endif` (110), `# endif` (111). sed_surface는 이 바깥 조건 안에서 무조건 사용(113). ng/tile 입력 정수 선언·빈 줄·주석(112–118). |
| 119–131 | 시작 시 sediment(77행)·5행 `#if defined NONLINEAR && defined SEDIMENT` 안. `# ifdef BEDLOAD` (119)은 소류사 수송 호출을 감싼다. `#   if defined BEDLOAD_SOULSBY \|\| defined BEDLOAD_MPM` (125)에서는 `CALL sed_bedload (ng, tile)` (126), `#   elif defined BEDLOAD_VANDERA` (127)에서는 `CALL sed_bedload_vandera(ng, tile)` (128). `#   endif` (129), `# endif` (130), 빈 줄(131). |
| 132–155 | 시작 시 sediment(77행)·5행 `#if defined NONLINEAR && defined SEDIMENT` 안. `# ifdef SUSPLOAD` (132) 안 `#  ifdef SED_FLOCS` (133)·`#  endif` (140)에서는 `CALL sed_flocmod (ng, tile)` (139). 같은 SUSPLOAD 경로에서 이어서 `CALL sed_settling (ng, tile)` (146), `CALL sed_fluxes (ng, tile)` (152)를 호출한다. 주석은 순서대로 응집(flocculation)·수직 침강·바닥과 수주(water column)의 교환으로 설명한다. `# endif` (154), 주석(155). |
| 156–175 | 시작 시 sediment(77행)·5행 `#if defined NONLINEAR && defined SEDIMENT` 안. 층서 계산 주석(156–159), `# if defined COHESIVE_BED \|\| defined MIXED_BED` (160)은 `CALL sed_bed_cohesive (ng, tile)` (161), `# elif defined NONCOHESIVE_BED2` (162)는 `CALL sed_bed2 (ng, tile)` (163), `# else` (164)는 `CALL sed_bed (ng, tile)` (165), `# endif` (166). 생물확산계수(biodiffusivity) 계산 주석(167–171), `# if defined SED_BIODIFF` (172)·`# endif` (174) 안 `CALL sed_biodiff (ng, tile)` (173). |
| 176–197 | 시작 시 sediment(77행)·5행 `#if defined NONLINEAR && defined SEDIMENT` 안. 반응성 퇴적물 항 주석(176–179), `# if defined SEDTR_REACTIONS` (180) 안 `#  if defined SEDBIO_COUP` (181)은 `CALL sedtr_reactions_pom (ng, tile)` (182), `#  elif defined SEDTR_DECAY` (183)는 `CALL sedtr_decay (ng, tile)` (184), `#  endif` (185), `# endif` (186). 표면층 속성 주석(187–191), `CALL sed_surface (ng, tile)` (192), RETURN·루틴 종료(194–195), `#endif` (196), 모듈 종료(197). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
