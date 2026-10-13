---
file: models/ROMS/raw/source_code/roms/ROMS/Nonlinear/SeaIce/ice_enthalpy.F
lines: 132
sha256: d71048be4d5fedcdd9059bd313dfa6ccd228f6240fde9aed2a99adc8d76422a0
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# ice_enthalpy.F — 판독 구간 기록

구간은 1행부터 132행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–32 | 전처리 조건 밖에서 시작한다. cppdefs.h를 포함하고 모듈을 선언한다(1–2). ICE_MODEL 조건이 구현을 감싼다(4). 머리말은 이류(advection) 전에 ti*hi로 얼음 엔탈피(ice enthalpy)를 계산한다고 적는다(13). 모듈과 exchange_r2d_tile을 사용하고 DISTRIBUTE일 때 mp_exchange2d를 사용한다(17–24). 공개 ice_enthalpy와 CONTAINS를 선언한다(26–31). 원문: `#include "cppdefs.h"` (1); `#ifdef ICE_MODEL` (4); `#ifdef DISTRIBUTE` (22); `#endif` (24). |
| 33–64 | 시작 시 4행 `#ifdef ICE_MODEL`·2행 모듈 안. `ice_enthalpy`의 인수·MyFile을 선언하고 tile.h를 포함한다(34–48). PROFILE은 wclock_on/off를 호출한다(50–52·58–60). tile 루틴에 격자 경계·liold/linew·ICE(ng)%Si를 전달한다(53–57). RETURN·루틴 종료를 포함한다(62–63). 원문: `character (len=*), parameter :: MyFile =                          &` (45); `&  __FILE__` (46); `#include "tile.h"` (48); `# ifdef PROFILE` (50); `CALL wclock_on (ng, model, 42, __LINE__, MyFile)` (51); `# endif` (52); `CALL ice_enthalpy_tile (ng, tile, model,                          &` (53); `&                        LBi, UBi, LBj, UBj,                       &` (54); `&                        IminS, ImaxS, JminS, JmaxS,               &` (55); `&                        liold(ng), linew(ng),                     &` (56); `&                        ICE(ng)%Si)` (57); `# ifdef PROFILE` (58); `CALL wclock_off (ng, model, 42, __LINE__, MyFile)` (59); `# endif` (60). |
| 65–95 | 시작 시 4행 `#ifdef ICE_MODEL`·2행 모듈 안. `ice_enthalpy_tile`의 인수·정수 변수를 선언한다(66–78). ASSUMED_SHAPE 여부로 Si 경계·차원을 선택하고 i/j를 선언하며 set_bounds.h를 포함한다(80–90). 원문: `#ifdef ASSUMED_SHAPE` (80); `#else` (82); `#endif` (84); `#include "set_bounds.h"` (90). |
| 96–106 | 시작 시 4행 `#ifdef ICE_MODEL`·66행 tile 루틴 안. j/i 루프에서 liold와 linew 각각의 Hice*Tice를 Enth에 대입한다(96–101). liold 두께가 min_hi 이하이면 liold Enth만 0으로 둔다(102–104). 두 루프를 닫는다(105–106). 원문: `DO j=JstrT,JendT` (96); `DO i=IstrT,IendT` (97); `Si(i,j,liold,isEnth)=Si(i,j,liold,isHice)*                    &` (98); `&                         Si(i,j,liold,isTice)` (99); `Si(i,j,linew,isEnth)=Si(i,j,linew,isHice)*                    &` (100); `&                         Si(i,j,linew,isTice)` (101); `IF(Si(i,j,liold,isHice).le.min_hi(ng)) THEN` (102); `Si(i,j,liold,isEnth)=0.0_r8` (103). |
| 107–132 | 시작 시 4행 `#ifdef ICE_MODEL`·66행 tile 루틴 안. 주기 경계면 두 시간 단계 Enth의 exchange_r2d_tile을 호출한다(110–118). DISTRIBUTE는 두 Enth 배열의 mp_exchange2d를 호출한다(120–127). tile 루틴·ICE_MODEL 조건·모듈을 닫는다(129–132). 원문: `IF (EWperiodic(ng).or.NSperiodic(ng)) THEN` (110); `CALL exchange_r2d_tile (ng, tile,                               &` (111); `&                          LBi, UBi, LBj, UBj,                     &` (112); `&                          Si(:,:,liold,isEnth))` (113); `CALL exchange_r2d_tile (ng, tile,                               &` (115); `&                          LBi, UBi, LBj, UBj,                     &` (116); `&                          Si(:,:,linew,isEnth))` (117); `# ifdef DISTRIBUTE` (120); `CALL mp_exchange2d (ng, tile, model, 2,                           &` (122); `&                    LBi, UBi, LBj, UBj,                           &` (123); `&                    NghostPoints, EWperiodic(ng), NSperiodic(ng), &` (124); `&                    Si(:,:,liold,isEnth),                         &` (125); `&                    Si(:,:,linew,isEnth))` (126); `# endif` (127); `#endif` (131). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 98–104: 두 시간 단계 모두 Hice*Tice를 계산한다. min_hi 이하 두께의 Enth=0 조건은 liold에만 적용되며 linew에는 대응하는 조건이 없다.
