---
file: models/ROMS/raw/source_code/roms/ROMS/Nonlinear/SeaIce/seaice.F
lines: 215
sha256: 8e17d741a3b747b70a6712c7cba2dd74feb9a9286f2d840f305425a455d12c12
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# seaice.F — 판독 구간 기록

구간은 1행부터 215행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–26 | 시작 시 열린 전처리 조건·바깥 실행 블록 없음. cppdefs.h를 포함하고 seaice_mod를 시작한다(1–3). 주석은 단일층 해빙(sea ice)·눈 모형이며 셀마다 하나의 두께 범주(category)를 둔다고 설명한다(12–16). mod_param·mod_parallel·mod_scalars·mod_stepping·mod_ice·mod_forces를 사용한다(20–25). 원문: `#include "cppdefs.h"` (1); `#ifdef ICE_MODEL` (3). |
| 27–52 | 시작 시 전처리 조건 `#ifdef ICE_MODEL` (3) 안. ice_spdiw·ice_vbc를 가져온다(27–28). ICE_THERMO는 ice_thermo, ICE_MOMENTUM과 ICE_EVP는 ice_evp·ice_evp_sig·ice_elastic, ICE_ADVECT는 ice_advect·ice_enthalpy, ICE_ADVECT 또는 ICE_THERMO는 ice_limit을 가져온다(29–43). FoundError·uppercase를 가져오고 seaice를 공개하며 기본 PRIVATE이다(44–49). 원문: `# ifdef ICE_THERMO` (29); `# endif` (31); `# if defined ICE_MOMENTUM && defined ICE_EVP` (32); `# endif` (36); `# ifdef ICE_ADVECT` (37); `# endif` (40); `# if defined ICE_ADVECT \|\| defined ICE_THERMO` (41); `# endif` (43). |
| 53–83 | 시작 시 전처리 조건 `#ifdef ICE_MODEL` (3) 안. seaice(model) 입구와 tile·중첩격자(nested grid)·EVP 반복 인덱스를 선언한다(53–68). dt_large=1.0E+23_r8과 MyFile을 선언한다(70–73). 주석의 단일 격자 경우 NestLayers는 1이다(79–82). 원문: `real(r8), parameter :: dt_large = 1.0E+23_r8` (70); `character (len=*), parameter :: MyFile =                          &` (72); `&  __FILE__` (73). |
| 84–111 | 시작 시 전처리 조건 `#ifdef ICE_MODEL` (3) 안; 바깥 블록 `SUBROUTINE seaice (model)` (53) 안. NEST_LAYER 루프에서 각 레이어의 격자를 순회한다(84–91). liold에 linew를 복사하고 linew=3-liold로 시간 저장 위치를 바꾼다(92–93). 각 tile에서 ice_spdiw를 호출하고 OpenMP 장벽(barrier)을 둔다(94–98). 다음 격자 루프에서 ice_vbc를 호출한 뒤 장벽을 둔다(104–110). 원문: `NEST_LAYER : DO nl=1,NestLayers` (84); `DO ig=1,GridsInLayer(nl)` (90); `ng=GridNumber(ig,nl)` (91); `liold(ng)=linew(ng)` (92); `linew(ng)=3-liold(ng)` (93); `DO tile=first_tile(ng),last_tile(ng),+1` (94); `CALL ice_spdiw (ng, tile, model)` (95); `DO ig=1,GridsInLayer(nl)` (104); `ng=GridNumber(ig,nl)` (105); `DO tile=first_tile(ng),last_tile(ng),+1` (106); `CALL ice_vbc (ng, tile, model)` (107). |
| 112–130 | 시작 시 전처리 조건 `#ifdef ICE_MODEL` (3) 안; 바깥 블록 `SUBROUTINE seaice (model)` (53)·`NEST_LAYER : DO nl=1,NestLayers` (84) 안. ICE_MOMENTUM·ICE_EVP 경로에서 탄성·점성·소성(Elastic-Viscous-Plastic, EVP) 내부 응력을 준비한다(112–122). liuol·liunw를 교체하고 dtevp=dtice/REAL(nEVP,r8)를 설정한다(123–125). 1..nelas 반복마다 lieol·lienw를 교체하고 iEVP를 저장한다(127–130). 원문: `# ifdef ICE_MOMENTUM` (112); `#  ifdef ICE_EVP` (113); `DO ig=1,GridsInLayer(nl)` (120); `ng=GridNumber(ig,nl)` (121); `nelas=nEVP(ng)` (122); `liuol(ng)=liunw(ng)` (123); `liunw(ng)=3-liuol(ng)` (124); `dtevp(ng)=dtice(ng)/REAL(nEVP(ng), r8)` (125); `DO my_iEVP=1,nelas` (127); `lieol(ng)=lienw(ng)` (128); `lienw(ng)=3-lieol(ng)` (129); `iEVP(ng)=my_iEVP` (130). |
| 131–154 | 시작 시 전처리 조건 `#ifdef ICE_MODEL` (3)·`# ifdef ICE_MOMENTUM` (112)·`#  ifdef ICE_EVP` (113) 안; 바깥 블록 `SUBROUTINE seaice (model)` (53)·`NEST_LAYER : DO nl=1,NestLayers` (84)·`DO ig=1,GridsInLayer(nl)` (120)·`DO my_iEVP=1,nelas` (127) 안. EVP 반복 안에서 ice_evp로 유동학(rheology) 계수를 계산한다(132–137). ice_evp_sig는 tile을 역순으로 처리하고 ice_elastic은 정순으로 처리한다(139–150). 세 단계 뒤에 각각 OpenMP 장벽이 있으며 EVP·격자 루프가 끝난다(137·144·151–153). 원문: `DO tile=first_tile(ng),last_tile(ng),+1` (134); `CALL ice_evp (ng, tile, model)` (135); `DO tile=last_tile(ng),first_tile(ng),-1` (141); `CALL ice_evp_sig (ng, tile, model)` (142); `DO tile=first_tile(ng),last_tile(ng),+1` (148); `CALL ice_elastic (ng, tile, model)` (149). |
| 155–163 | 시작 시 전처리 조건 `#ifdef ICE_MODEL` (3)·`# ifdef ICE_MOMENTUM` (112)·`#  ifdef ICE_EVP` (113) 안; 바깥 블록 `SUBROUTINE seaice (model)` (53)·`NEST_LAYER : DO nl=1,NestLayers` (84) 안. ICE_MOMENTUM 안에서 ICE_EVP의 #else는 유동학 옵션 필요 메시지를 출력한다(155–158). exit_flag=5를 설정하고 원문 IF FoundError 문장으로 RETURN을 시도한다(159–160). 두 전처리 조건을 닫는다(161–162). 원문: `#  else` (155); `exit_flag=5` (159); `IF ((FoundError(exit_flag, NoError, __LINE__, MyFile)) RETURN` (160); `#  endif` (161); `# endif` (162). |
| 164–177 | 시작 시 전처리 조건 `#ifdef ICE_MODEL` (3) 안; 바깥 블록 `SUBROUTINE seaice (model)` (53)·`NEST_LAYER : DO nl=1,NestLayers` (84) 안. ICE_ADVECT에서 각 격자·tile에 ice_enthalpy를 호출하여 얼음·염수(brine) 결합 계의 엔탈피(enthalpy)를 계산한다(164–174). tile 처리 뒤 OpenMP 장벽과 격자 루프 종료를 포함한다(175–176). 원문: `# ifdef ICE_ADVECT` (164); `DO ig=1,GridsInLayer(nl)` (170); `ng=GridNumber(ig,nl)` (171); `DO tile=first_tile(ng),last_tile(ng),+1` (172); `CALL ice_enthalpy (ng, tile, model)` (173). |
| 178–192 | 시작 시 전처리 조건 `#ifdef ICE_MODEL` (3)·`# ifdef ICE_ADVECT` (164) 안; 바깥 블록 `SUBROUTINE seaice (model)` (53)·`NEST_LAYER : DO nl=1,NestLayers` (84) 안. ICE_ADVECT 안에서 각 tile에 ice_advect·ice_limit을 연속 호출한다(183–188). 주석은 단조성과 양의 값 유지를 위한 제한기(limiter) 적용이라고 설명한다(179–180). 장벽과 ICE_ADVECT 종료를 포함한다(189–191). 원문: `DO ig=1,GridsInLayer(nl)` (183); `ng=GridNumber(ig,nl)` (184); `DO tile=first_tile(ng),last_tile(ng),+1` (185); `CALL ice_advect (ng, tile, model)` (186); `CALL ice_limit (ng, tile, model)` (187); `# endif` (191). |
| 193–215 | 시작 시 전처리 조건 `#ifdef ICE_MODEL` (3) 안; 바깥 블록 `SUBROUTINE seaice (model)` (53)·`NEST_LAYER : DO nl=1,NestLayers` (84) 안. ICE_THERMO에서는 각 격자·tile에 ice_thermo·ice_limit을 호출하고 장벽을 둔다(193–207). NEST_LAYER 루프 종료 뒤 RETURN·seaice 루틴 종료·ICE_MODEL 종료·모듈 종료를 포함한다(209–215). 원문: `# ifdef ICE_THERMO` (193); `DO ig=1,GridsInLayer(nl)` (199); `ng=GridNumber(ig,nl)` (200); `DO tile=first_tile(ng),last_tile(ng),+1` (201); `CALL ice_thermo (ng, tile, model)` (202); `CALL ice_limit(ng, tile, model)` (203); `# endif` (207); `#endif` (214). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 70: dt_large는 1.0E+23_r8로 선언되며 이 파일의 이후 실행문에는 사용되지 않는다.
- 160: 원문은 `IF ((FoundError(exit_flag, NoError, __LINE__, MyFile)) RETURN`이다. 이 한 행에는 여는 소괄호 3개와 닫는 소괄호 2개가 있다.
- 123–125: dtevp는 dtice/REAL(nEVP,r8)로 계산한다. 이 대입 앞의 해당 블록에는 nEVP가 0인지 검사하는 조건이 없다.
- 134–150: ice_evp·ice_elastic의 tile 순서는 first_tile에서 last_tile로 증가한다. ice_evp_sig의 tile 순서는 last_tile에서 first_tile로 감소한다.
