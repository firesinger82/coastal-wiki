---
file: models/ROMS/raw/source_code/roms/ROMS/Utility/set_grid.F
lines: 207
sha256: bc4dee3d251b515d48eb0062749c4244878017b35f904acadefcca5b8a1347e5
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# set_grid.F — 판독 구간 기록

구간은 1행부터 207행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–57 | 시작 시 열린 전처리 조건 없음. `cppdefs.h`를 끼워 넣고 `set_grid(ng,model)`을 연다(1–2). 초기화 때 한 번 격자(grid)와 관련 변수를 설정한다는 주석과 저작권을 포함한다(4–14). 병렬·중첩 격자(nesting)·분석 함수(analytical function)·평형 조석(equilibrium tide)·격자 추출(grid extraction)·격자/너징 계수(nudging coefficient) 판독 모듈을 조건별로 가져온다(16–43). ng·model·tile·MyFile을 선언한다(45–56). 원문 조건·대입·전처리: `#include "cppdefs.h"` (1); `#ifdef NESTING` (18); `#endif` (20); `#ifdef DISTRIBUTE` (24); `#endif` (26); `#ifdef TIDE_GENERATING_FORCES` (27); `#endif` (29); `#ifdef GRID_EXTRACT` (30); `#endif` (32); `#ifndef ANA_GRID` (33); `#endif` (35); `#ifndef ANA_NUDGCOEF` (36); `#endif` (38); `#ifdef NESTING` (40); `#endif` (42). |
| 58–103 | 시작 시 열린 전처리 조건 없음. 시작 시 2행 `set_grid` 안. ANA_GRID이면 first_tile:last_tile의 각 타일에서 `ana_grid`(65), MASKING의 `ana_mask`(67), 민감도(sensitivity) 관련 전처리 조건의 `ana_scope`(72)를 호출한다. 그 외에는 OpenMP MASTER에서 `get_grid`를 MyRank 또는 -1로 호출한다(77–83). DISTRIBUTE는 exit_flag를 `mp_bcasti`로 방송(broadcast)하고 오류이면 반환한다(84–89). GRID_EXTRACT는 `get_extract`를 MyRank 또는 -1로 호출한다(98–102). 타일 루프 간격은 +1이고 경로별 OpenMP 장벽(barrier)을 포함한다(64·75·87). 원문 조건·대입·전처리: `#ifdef ANA_GRID` (63); `# ifdef MASKING` (66); `# endif` (68); `# if defined AD_SENSITIVITY    \|\| defined I4DVAR_ANA_SENSITIVITY \|\| \` (69) `defined OPT_OBSERVATIONS  \|\| defined SO_SEMI                \|\| \` (70) `defined SENSITIVITY_4DVAR` (71); `# endif` (73); `#else` (76); `# ifdef DISTRIBUTE` (78); `# else` (80); `# endif` (82); `# ifdef DISTRIBUTE` (84); `# endif` (86); `IF (FoundError(exit_flag, NoError, __LINE__, MyFile)) RETURN` (88); `#endif` (89); `#ifdef GRID_EXTRACT` (91); `# ifdef DISTRIBUTE` (98); `# else` (100); `# endif` (102); `#endif` (103). |
| 104–138 | 시작 시 열린 전처리 조건 없음. 시작 시 2행 `set_grid` 안. SOLVE3D에서 OpenMP MASTER로 수직 지형 추종 좌표(terrain-following coordinate) 설정 `set_scoord`(112)를 호출하고 장벽을 둔다(114). 별도 SOLVE3D 블록에서 순압(barotropic) 시간 단계 평균 가중치 `set_weights`(124)를 호출하고 장벽을 둔다(126). 모든 경로에서 first_tile:last_tile,+1 루프가 격자 계량(metric) 조합 `metrics`(135)를 호출하고 장벽을 둔다(137). 원문 조건·대입·전처리: `#ifdef SOLVE3D` (105); `#endif` (115); `#ifdef SOLVE3D` (117); `#endif` (127). |
| 139–162 | 시작 시 열린 전처리 조건 없음. 시작 시 2행 `set_grid` 안. NESTING은 세부 격자 경계 질량 유량(mass flux)에 쓰는 간격을 설정하도록 `nesting(ng,model,ndxdy)`(147)을 호출한다. WTYPE_GRID·ANA_WTYPE과 LMD_SKPP 또는 SOLAR_SOURCE의 결합 조건에서 각 타일에 Jerlov 수형(water type) `ana_wtype(ng,tile,iNLM)`(158)을 호출한다. 타일 루프 뒤 OpenMP 장벽이 있다(160). 원문 조건·대입·전처리: `#ifdef NESTING` (139); `#endif` (148); `#if defined WTYPE_GRID && defined ANA_WTYPE     && \` (150) `(defined LMD_SKPP   \|\| defined SOLAR_SOURCE)` (151); `#endif` (161). |
| 163–193 | 시작 시 열린 전처리 조건 없음. 시작 시 2행 `set_grid` 안. CORRELATION 불성립 경로에서 너징 시간 척도(time scale)를 설정한다. ANA_NUDGCOEF이면 Lnudging 참 조건에서 각 타일의 `ana_nudgcoef`(173)를 호출한다. 그 외에는 같은 Lnudging 조건의 OpenMP MASTER에서 `get_nudgcoef`를 MyRank 또는 -1로 호출한다(178–185). DISTRIBUTE는 `mp_bcasti`(187)로 exit_flag를 전달한다. 장벽 후 `FoundError` 참이면 반환한다(189–190). 원문 조건·대입·전처리: `#ifndef CORRELATION` (163); `# ifdef ANA_NUDGCOEF` (170); `IF (Lnudging(ng)) THEN` (171); `# else` (177); `IF (Lnudging(ng)) THEN` (178); `#  ifdef DISTRIBUTE` (180); `#  else` (182); `#  endif` (184); `#  ifdef DISTRIBUTE` (186); `#  endif` (188); `IF (FoundError(exit_flag, NoError, __LINE__, MyFile)) RETURN` (190); `# endif` (192). |
| 194–207 | 시작 시 전처리 조건 `#ifndef CORRELATION` (163) 안. 시작 시 2행 `set_grid`·163행 CORRELATION 불성립 전처리 분기 안. TIDE_GENERATING_FORCES에서 기준 조석 날짜의 Greenwich 평형 조석 조화 성분(harmonic constituent) 설정 `harmonic_constituents(Lnodal)`(202)을 호출한다. 두 전처리 조건을 닫고 반환·루틴 종료한다(203–207). 원문 조건·대입·전처리: `# ifdef TIDE_GENERATING_FORCES` (194); `# endif` (203); `#endif` (204). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 49·65·135·158: set_grid는 model 인수를 받는다. ana_grid·metrics에는 model을 넘기고 ana_wtype에는 iNLM을 넘긴다.
- 88·98–103·190: get_grid와 get_nudgcoef 경로에는 FoundError 검사와 반환이 있다. get_extract 호출 직후에는 같은 검사가 없다.
