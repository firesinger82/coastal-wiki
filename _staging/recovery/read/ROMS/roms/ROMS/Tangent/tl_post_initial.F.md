---
file: models/ROMS/raw/source_code/roms/ROMS/Tangent/tl_post_initial.F
lines: 92
sha256: c59c5434eff8e68b4d19fbc763da79b2a5b2e0621fa4d251b4254ddf60dad0da
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# tl_post_initial.F — 판독 구간 기록

구간은 1행부터 92행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–41 | `cppdefs.h` 포함(1), 모듈 입구와 TANGENT 조건(2–3). 첫 시간 단계(time step)에 초기 자유 수면(free surface)으로 층 깊이·두께를 계산하고 모든 시간 레벨(time level)의 접선형(tangent linear) 상태와 측면 경계 조건(lateral boundary condition)을 초기화한다는 주석(13–16). 라이선스(5–11). NESTING일 때 mod_scalars, SOLVE3D일 때 set_depth/tl_set_depth를 가져온다(20–33). set_zeta_timeavg, tl_ini_fields, tl_ini_zeta 가져오기(26·30). tl_post_initial 공개와 기본 private·contains(35–40). 원문 조건·계산식·호출·전처리: `#include "cppdefs.h"` (1); `#ifdef TANGENT` (3); `# ifdef NESTING` (22); `# endif` (24); `# ifdef SOLVE3D` (27); `# endif` (29); `# ifdef SOLVE3D` (31); `# endif` (33). |
| 42–67 | 시작 시 3행 `#ifdef TANGENT` 안. `tl_post_initial(ng,model)` 입구와 정수 인수·tile 선언(43–52). 초기 깊이 평균 속도에 비선형 Zt_avg1/Hz가 필요하다는 주석(55–57). tile=first_tile..last_tile의 증가 루프(60)에서 `set_zeta_timeavg`·`set_depth`를 iNLM으로 호출하고(61–62), `tl_ini_zeta`·`tl_set_depth`를 model로 호출한다(63–64). 루프 종료(65)와 OpenMP BARRIER(66). 원문 조건·계산식·호출·전처리: `DO tile=first_tile(ng),last_tile(ng),+1` (60); `CALL set_zeta_timeavg (ng, tile, iNLM)` (61); `CALL set_depth (ng, tile, iNLM)` (62); `CALL tl_ini_zeta (ng, tile, model)` (63); `CALL tl_set_depth (ng, tile, model)` (64). |
| 68–92 | 시작 시 3행 `#ifdef TANGENT` 안. 43행 `tl_post_initial` 안이며 60행 tile 루프 밖. tile=last_tile..first_tile의 감소 루프(72)에서 다른 상태 초기화 `tl_ini_fields`를 호출한다(73), 루프 종료와 OpenMP BARRIER(74–75). NESTING 조건(77)에서는 세분 격자(refined grid)의 접촉점(contact point) 초기 자료를 REFINED에 저장한다는 주석(80–81). RefinedGrid 조건(84)에서 `tl_nesting(ng,model,ngetD)` 호출(85). 조건 종료(86–87). RETURN·루틴·TANGENT·모듈 종료(89–92). 원문 조건·계산식·호출·전처리: `DO tile=last_tile(ng),first_tile(ng),-1` (72); `CALL tl_ini_fields (ng, tile, model)` (73); `# ifdef NESTING` (77); `IF (RefinedGrid(ng)) THEN` (84); `CALL tl_nesting (ng, model, ngetD)` (85); `# endif` (87); `#endif` (91). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 27–33·60–65: set_depth와 tl_set_depth의 USE ONLY 선언은 SOLVE3D 조건 안에 있다. 두 호출은 TANGENT 안의 tile 루프에서 SOLVE3D 전처리 조건 없이 적혀 있다.
