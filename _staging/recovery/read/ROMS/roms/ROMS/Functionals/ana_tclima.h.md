---
file: models/ROMS/raw/source_code/roms/ROMS/Functionals/ana_tclima.h
lines: 133
sha256: 426eeb562f5c030c139e80df8858f60bc803e3ce25bd21dd3afb5e8a1a0ef07e
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# ana_tclima.h — 판독 구간 기록

구간은 1행부터 133행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–44 | 시작 시 열린 전처리 조건 없음. `ana_tclima`는 추적자 기후장(tracer climatology)을 설정하는 진입 루틴이다(2·11). 모듈·인수·파일명 선언을 포함한다(15–25). `tile.h`를 포함하고 `ana_tclima_tile`에 타일 경계(tile bounds)를 전달한다(27–31). DISTRIBUTE일 때 Lanafile만 검사하고, 다른 경우 tile=0도 검사하여 ANANAME(33)에 파일명을 저장한다(35–41). 반환과 루틴 종료를 포함한다(43–44). 원문: `character (len=*), parameter :: MyFile =                          &` (24); `&  __FILE__` (25); `#include "tile.h"` (27); `CALL ana_tclima_tile (ng, tile, model,                            &` (29); `&                      LBi, UBi, LBj, UBj,                         &` (30); `&                      IminS, ImaxS, JminS, JmaxS)` (31); `#ifdef DISTRIBUTE` (35); `IF (Lanafile) THEN` (36); `#else` (37); `IF (Lanafile.and.(tile.eq.0)) THEN` (38); `#endif` (39); `ANANAME(33)=MyFile` (40). |
| 45–79 | 시작 시 열린 전처리 조건 없음. `ana_tclima_tile` 선언과 빈 줄·구분 주석을 포함한다(45–51). 기후장·격자·상수 모듈과 `exchange_r3d_tile`을 사용한다(52–57). DISTRIBUTE일 때 `mp_exchange4d`를 가져온다(58–60). 인수·i/itrc/j/k·val1..val4 선언 뒤 `set_bounds.h`로 계산 경계를 포함한다(64–74). 원문: `#ifdef DISTRIBUTE` (58); `#endif` (60); `#include "set_bounds.h"` (74). |
| 80–99 | 시작 시 열린 전처리 조건 없음. 시작 시 47행 `ana_tclima_tile` 안. 기후장 사용 또는 추적자 너징(tracer nudging) 사용 여부를 검사한다(80). DOUBLE_GYRE 분기는 val1·val2를 계산하고 수직·수평 루프에서 수심과 남북 좌표로 온도를 계산한다(81–91). SALINITY 분기는 같은 셀에 염분을 계산한다(92–96). 세 루프 종료를 포함한다(97–99). 원문: `IF (ANY(LtracerCLM(:,ng)).or.ANY(LnudgeTCLM(:,ng))) THEN` (80); `#if defined DOUBLE_GYRE` (81); `val1=(44.69_r8/39.382_r8)**2` (82); `val2=val1*(rho0*100.0_r8/g)*                                    &` (83); `&       (5.0E-5_r8/((42.689_r8/44.69_r8)**2))` (84); `DO k=1,N(ng)` (85); `DO j=JstrT,JendT` (86); `DO i=IstrT,IendT` (87); `val3=T0(ng)+val2*EXP(GRID(ng)%z_r(i,j,k)/100.0_r8)*       &` (88); `&             (10.0_r8-0.4_r8*TANH(GRID(ng)%z_r(i,j,k)/100.0_r8))` (89); `val4=GRID(ng)%yr(i,j)/el(ng)` (90); `CLIMA(ng)%tclm(i,j,k,itemp)=val3-3.0_r8*val4` (91); `# ifdef SALINITY` (92); `CLIMA(ng)%tclm(i,j,k,isalt)=34.5_r8-                      &` (93); `&                                    0.001_r8*GRID(ng)%z_r(i,j,k)- &` (94); `&                                    val4` (95); `# endif` (96). |
| 100–133 | 시작 시 `#if defined DOUBLE_GYRE` (81) 안. 시작 시 47행 `ana_tclima_tile`·80행 `IF (ANY(LtracerCLM(:,ng)).or.ANY(LnudgeTCLM(:,ng))) THEN` 안. DOUBLE_GYRE가 아닌 분기는 온도·SALINITY 염분에 `???` 자리표시자를 둔다(100–111). 주기 경계(periodic boundary)가 있으면 각 추적자에 `exchange_r3d_tile`을 호출한다(115–121). DISTRIBUTE이면 `mp_exchange4d`로 전체 기후장 경계 데이터를 교환한다(123–129). 외부 IF·루틴 종료를 포함한다(130–133). 원문: `#else` (100); `DO k=1,N(ng)` (101); `DO j=JstrT,JendT` (102); `DO i=IstrT,IendT` (103); `CLIMA(ng)%tclm(i,j,k,itemp)=???` (104); `# ifdef SALINITY` (105); `CLIMA(ng)%tclm(i,j,k,isalt)=???` (106); `# endif` (107); `#endif` (111); `IF (EWperiodic(ng).or.NSperiodic(ng)) THEN` (115); `DO itrc=1,NTCLM(ng)` (116); `CALL exchange_r3d_tile (ng, tile,                           &` (117); `&                              LBi, UBi, LBj, UBj, 1, N(ng),       &` (118); `&                              CLIMA(ng)%tclm(:,:,:,itrc))` (119); `#ifdef DISTRIBUTE` (123); `CALL mp_exchange4d (ng, tile, model, 1,                         &` (124); `&                      LBi, UBi, LBj, UBj, 1, N(ng), 1, NTCLM(ng), &` (125); `&                      NghostPoints,                               &` (126); `&                      EWperiodic(ng), NSperiodic(ng),             &` (127); `&                      CLIMA(ng) % tclm)` (128); `#endif` (129). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 104·106: DOUBLE_GYRE가 아닌 분기의 온도·염분 대입 우변은 `???`이다.
- 82–95: DOUBLE_GYRE 온도·염분 식은 44.69·39.382·42.689·100·5.0E-5·3·34.5·0.001을 코드 상수로 사용한다.
