---
file: models/ROMS/raw/source_code/roms/ROMS/Nonlinear/Vegetation/marsh_dynamics.F
lines: 119
sha256: c3a5c6b91d4df24e3176a84f1c6399493234584b4bfe3a35130d2790d3090ce0
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# marsh_dynamics.F — 판독 구간 기록

구간은 1행부터 119행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|

| 1–55 | 파일 내부에서 열린 전처리 조건 없음. `#include "cppdefs.h"` (1)로 cppdefs.h 포함, MODULE marsh_dynamics_mod(2). `#if defined VEGETATION && defined MARSH_DYNAMICS` (4). 저작권·MIT/X 머리말(6–11). 습지(marsh) 동역학의 주 구동 루틴(main driver)이며 파랑 횡방향 추력(lateral wave thrust)·경계 침식(edge erosion), 자체 생산(autochthonous supply)에 의한 유기물·수직 성장(vertical growth)을 처리한다는 주석(13–20). 네 하위 모듈 목적(22–33), Beudin 등 2017·Kalra 등 2021 문헌과 DOI(35–45). implicit none·PRIVATE·공개 marsh_dynamics·CONTAINS(49–54), 주석·빈 줄 포함. |
| 56–80 | 시작 시 4행 `#if defined VEGETATION && defined MARSH_DYNAMICS` 안. marsh_dynamics(ng,tile) 선언(57). mod_param/stepping/scalars 사용(60–62). `# if defined MARSH_WAVE_THRUST` (64)은 marsh_wave_thrust USE(65), `# endif` (66). `# if defined MARSH_SED_EROSION` (67)은 marsh_sed_erosion USE(68), `# endif` (69). `# if defined MARSH_TIDAL_RANGE` (70)은 marsh_tidal_range USE(71), `# endif` (72). `# if defined MARSH_VERT_GROWTH` (73)은 marsh_vert_growth USE(74), `# endif` (75). ng·tile 정수 intent(in)(79), 주석·빈 줄 포함. |
| 81–97 | 시작 시 4행 `#if defined VEGETATION && defined MARSH_DYNAMICS` 안, 57행 marsh_dynamics 안. 파랑 유도 습지 경계 추력 구분 주석(81–84). `# if defined MARSH_WAVE_THRUST` (85)에서 `CALL marsh_wave_thrust (ng, tile)` (86), `# endif` (87). 빈 줄(88). `# if defined MARSH_SED_EROSION` (89)에서 수심 변화 기반 퇴적물 침식 주석(91–93), `CALL marsh_sed_erosion (ng, tile)` (95), `# endif` (96), 빈 줄(97). 두 옵션이 모두 정의되면 추력 호출이 침식 호출보다 먼저 놓인다. |
| 98–119 | 시작 시 4행 `#if defined VEGETATION && defined MARSH_DYNAMICS` 안, 57행 marsh_dynamics 안. `# if defined MARSH_TIDAL_RANGE` (98) 아래 지정 주기의 조차(tidal range)와 평균 고조위(mean high water)를 계산한다는 주석(100–102), `CALL marsh_tidal_range (ng, tile)` (104), `#  endif` (105). `#  if defined MARSH_VERT_GROWTH` (107) 아래 수직 생체량(biomass) 생산 주석(109–111), `CALL marsh_vert_growth (ng, tile)` (113), `# endif` (114). RETURN·루틴 종료(116–117), `#endif` (118), MODULE 종료(119). 옵션이 함께 정의되면 조차 호출 다음에 수직 성장 호출이 놓인다. 이 파일에는 수치 계산 대입식이나 기본값 설정이 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
