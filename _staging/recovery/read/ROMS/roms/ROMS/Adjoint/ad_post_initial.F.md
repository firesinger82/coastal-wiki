---
file: models/ROMS/raw/source_code/roms/ROMS/Adjoint/ad_post_initial.F
lines: 92
sha256: 32ae1a3234778385d82b67245567935725f17f047642e9ee88744db05d61a976
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# ad_post_initial.F — 판독 구간 기록

구간은 1행부터 92행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–41 | 시작 시 열린 전처리 조건·루틴·반복·분기 없음. `cppdefs.h`를 포함하고 모듈을 시작한다(1–2). `ADJOINT`에서 마지막 시간 단계(time step)에 초기 자유수면(free surface)의 초기 수심·층 두께(layer thickness) 수반(adjoint) 값을 계산하고 상태 변수(state variable)의 시간 수준(time level) 초기화와 측면 경계(lateral boundary) 처리를 한다는 주석이다(3·13–16). `NESTING`에서 스칼라 모듈을 가져온다(22–24). `set_zeta_timeavg`·수반 초기화 루틴을 가져오고 `SOLVE3D`에서 기본·수반 수심 루틴을 가져온다(26–33). 공개 루틴·기본 접근·`CONTAINS`를 선언한다(35–40).<br>원문 조건·반복·대입·호출·전처리 행:<br>`#include "cppdefs.h"` (1)<br>`#ifdef ADJOINT` (3)<br>`# ifdef NESTING` (22)<br>`# endif` (24)<br>`# ifdef SOLVE3D` (27)<br>`# endif` (29)<br>`# ifdef SOLVE3D` (31)<br>`# endif` (33) |
| 42–65 | 시작 시 전처리 3행 `#ifdef ADJOINT` 안. `ad_post_initial`은 격자와 모델 번호를 받고 지역 타일(tile) 번호를 선언한다(43–52). `NESTING`에서 정련 격자(refined grid)의 접촉점(contact point) 초기 자료를 처리한다는 주석이다(54–60). `RefinedGrid(ng)`가 참이면 `ad_nesting(ng,model,ngetD)`를 호출한다(61–63).<br>원문 조건·반복·대입·호출·전처리 행:<br>`# ifdef NESTING` (54)<br>`IF (RefinedGrid(ng)) THEN` (61)<br>`CALL ad_nesting (ng, model, ngetD)` (62)<br>`# endif` (64) |
| 66–74 | 시작 시 전처리 3행 `#ifdef ADJOINT`; 43행 `ad_post_initial` 루틴 안. 다른 상태 변수 초기화 블록이다(66–68). 마지막 타일부터 첫 타일까지 -1 간격으로 `ad_ini_fields`를 호출한다(70–72). OpenMP 장벽(barrier)을 둔다(73).<br>원문 조건·반복·대입·호출·전처리 행:<br>`DO tile=last_tile(ng),first_tile(ng),-1` (70)<br>`CALL ad_ini_fields (ng, tile, model)` (71) |
| 75–88 | 시작 시 전처리 3행 `#ifdef ADJOINT`; 43행 `ad_post_initial` 루틴 안. 주석은 초기 `ad_ubar`·`ad_vbar` 계산에 비선형(nonlinear) `Zt_avg1`·`Hz`가 필요하다고 적는다(75–79). 첫 타일부터 마지막 타일까지 +1 간격으로 `set_zeta_timeavg`·`set_depth`를 `iNLM`으로 호출한다(81–83). 이어 `ad_set_depth`·`ad_ini_zeta`를 전달된 모델 번호로 호출한다(84–86). OpenMP 장벽을 둔다(87).<br>원문 조건·반복·대입·호출·전처리 행:<br>`DO tile=first_tile(ng),last_tile(ng),+1` (81)<br>`CALL set_zeta_timeavg (ng, tile, iNLM)` (82)<br>`CALL set_depth (ng, tile, iNLM)` (83)<br>`CALL ad_set_depth (ng, tile, model)` (84)<br>`CALL ad_ini_zeta (ng, tile, model)` (85) |
| 89–92 | 시작 시 전처리 3행 `#ifdef ADJOINT`; 43행 `ad_post_initial` 루틴 안. 루틴을 반환·종료하고 `ADJOINT` 조건과 모듈을 닫는다(89–92).<br>원문 조건·반복·대입·호출·전처리 행:<br>`#endif` (91) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 27–33·81–86: `set_depth`·`ad_set_depth`의 `USE` 문장은 `SOLVE3D` 전처리 조건 안에 있다. 두 루틴의 호출(83–84)은 `SOLVE3D` 전처리 조건 없이 타일 반복 안에 있다.
