---
file: models/ROMS/raw/source_code/roms/ROMS/Nonlinear/post_initial.F
lines: 89
sha256: e4d257f153a608da12929d98768a3f7a1f5d6f2489b7156ceea506059f489790
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# post_initial.F — 판독 구간 기록

구간은 1행부터 89행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–41 | 시작 시 열린 바깥 블록 없음. `cppdefs.h`를 포함하고 post_initial_mod를 연다(1–2). NONLINEAR에서 구현한다(3). 머리말은 첫 시간 단계(timestep)에 초기 자유수면으로 깊이·층 두께를 계산하고 모든 시간 단계의 상태 변수(state variable)를 초기화하며 측면 경계 조건을 적용한다고 설명한다(13–16). ini_fields·ini_zeta를 가져온다(26). NESTING이면 mod_scalars·ngetD·nesting을 가져오고 SOLVE3D이면 set_depth를 가져온다(22–33). post_initial을 공개한다(37–40). 원문: `#include "cppdefs.h"` (1); `#ifdef NONLINEAR` (3); `# ifdef NESTING` (22); `# endif` (24); `# ifdef NESTING` (27); `# endif` (30); `# ifdef SOLVE3D` (31); `# endif` (33). |
| 42–64 | 시작 시 3행 `#ifdef NONLINEAR` 안. post_initial은 ng·model을 받는다(43–48). first_tile부터 last_tile까지 +1 순서로 ini_zeta 다음 set_depth를 호출한다(59–62). 뒤의 OpenMP 장벽(barrier)이 타일 초기화 완료를 동기화한다(63). 원문: `DO tile=first_tile(ng),last_tile(ng),+1` (59); `CALL ini_zeta (ng, tile, model)` (60); `CALL set_depth (ng, tile, model)` (61). |
| 65–89 | 시작 시 3행 `#ifdef NONLINEAR`; 43행 `SUBROUTINE post_initial (ng, model)` 안. last_tile부터 first_tile까지 −1 순서로 ini_fields를 호출한다(69–71). 뒤에 OpenMP 장벽이 있다(72). NESTING이면 RefinedGrid 조건에서 nesting(ng,model,ngetD)을 호출한다(74–84). 주석은 접촉점(contact point)의 제공 격자(donor grid) 초기값을 REFINED에 저장하여 시공간 보간에 사용한다고 적는다(77–78). 반환하고 NONLINEAR와 모듈을 닫는다(86–89). 원문: `DO tile=last_tile(ng),first_tile(ng),-1` (69); `CALL ini_fields (ng, tile, model)` (70); `# ifdef NESTING` (74); `IF (RefinedGrid(ng)) THEN` (81); `CALL nesting (ng, model, ngetD)` (82); `# endif` (84); `#endif` (88). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 31–33·59–62: set_depth의 USE 문장은 SOLVE3D 조건 안에 있다. set_depth 호출은 NONLINEAR의 타일 루프 안에 있고 별도 SOLVE3D 전처리 조건으로 감싸지 않는다.
