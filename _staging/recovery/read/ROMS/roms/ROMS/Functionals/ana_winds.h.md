---
file: models/ROMS/raw/source_code/roms/ROMS/Functionals/ana_winds.h
lines: 163
sha256: a2284cbfdfdafa93b90c80992b41a1313392f5d93349ba2507c6e75e80fa276e
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# ana_winds.h — 판독 구간 기록

구간은 1행부터 163행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–56 | 시작 시 열린 전처리 조건 없음. `ana_winds`는 해석식으로 지표 바람(surface wind) 성분을 설정한다(2·11–12). 모듈·인수·MyFile 선언과 `tile.h` 포함을 기록한다(16–30). `ana_winds_tile`에 SPHERICAL이면 lonr/latr, 아니면 xr/yr를 전달하고 Uwind/Vwind를 전달한다(32–43). DISTRIBUTE별 Lanafile 조건으로 ANANAME(36)을 저장하고 반환한다(47–56). 원문: `character (len=*), parameter :: MyFile =                          &` (27); `&  __FILE__` (28); `#include "tile.h"` (30); `CALL ana_winds_tile (ng, tile, model,                             &` (32); `&                     LBi, UBi, LBj, UBj,                          &` (33); `&                     IminS, ImaxS, JminS, JmaxS,                  &` (34); `#ifdef SPHERICAL` (35); `&                     GRID(ng) % lonr,                             &` (36); `&                     GRID(ng) % latr,                             &` (37); `#else` (38); `&                     GRID(ng) % xr,                               &` (39); `&                     GRID(ng) % yr,                               &` (40); `#endif` (41); `&                     FORCES(ng) % Uwind,                          &` (42); `&                     FORCES(ng) % Vwind)` (43); `#ifdef DISTRIBUTE` (47); `IF (Lanafile) THEN` (48); `#else` (49); `IF (Lanafile.and.(tile.eq.0)) THEN` (50); `#endif` (51); `ANANAME(36)=MyFile` (52). |
| 57–117 | 시작 시 열린 전처리 조건 없음. `ana_winds_tile` 인수도 SPHERICAL별 좌표를 선택한다(59–67). 모듈·교환 루틴·인수 선언을 포함한다(70–82). ASSUMED_SHAPE와 SPHERICAL 조합별 좌표 및 출력 바람 배열 형상을 선언한다(84–104). 지역 변수 i/j/Wdir/Wmag/cff/u_wind/v_wind와 `set_bounds.h`를 포함한다(108–112). 주석은 RHO점에서 m/s 단위 성분을 설정한다고 적는다(115). 원문: `#ifdef SPHERICAL` (62); `#else` (64); `#endif` (66); `#ifdef DISTRIBUTE` (74); `#endif` (76); `#ifdef ASSUMED_SHAPE` (84); `# ifdef SPHERICAL` (85); `# else` (88); `# endif` (91); `#else` (94); `# ifdef SPHERICAL` (95); `# else` (98); `# endif` (101); `#endif` (104); `#include "set_bounds.h"` (112). |
| 118–126 | 시작 시 열린 전처리 조건 없음. 시작 시 59행 `ana_winds_tile` 안. BENCHMARK는 Wmag=15로 설정하고 j/i 루프에서 latr로 cff를 계산한다(118–122). Uwind는 Wmag*EXP(-cff*cff), Vwind는 0으로 설정한다(123–124). 두 루프 종료를 포함한다(125–126). 원문: `#if defined BENCHMARK` (118); `Wmag=15.0_r8` (119); `DO j=JstrT,JendT` (120); `DO i=IstrT,IendT` (121); `cff=0.2_r8*(60.0_r8+latr(i,j))` (122); `Uwind(i,j)=Wmag*EXP(-cff*cff)` (123); `Vwind(i,j)=0.0_r8` (124). |
| 127–141 | 시작 시 `#if defined BENCHMARK` (118) 안. 시작 시 59행 `ana_winds_tile` 안. BL_TEST로 전환한다(127). tdays−dstart≤6일 때 지역 u_wind=0, v_wind=10을 설정한다(128–132). v_wind=4.7936은 주석 처리되어 있다(130). 시간 IF 밖의 j/i 루프는 두 지역 값을 Uwind/Vwind에 복사한다(133–138). 나머지 ELSE는 값 미제공 비주석 문장이다(139–141). 원문: `#elif defined BL_TEST` (127); `IF ((tdays(ng)-dstart).le.6.0_r8) THEN` (128); `u_wind=0.0_r8` (129); `v_wind=10.0_r8` (131); `DO j=JstrT,JendT` (133); `DO i=IstrT,IendT` (134); `Uwind(i,j)=u_wind` (135); `Vwind(i,j)=v_wind` (136); `#else` (139); `#endif` (141). |
| 142–163 | 시작 시 열린 전처리 조건 없음. 시작 시 59행 `ana_winds_tile` 안. 주기 경계 조건이면 Uwind와 Vwind 각각에 `exchange_r2d_tile`을 호출한다(145–152). DISTRIBUTE이면 두 배열에 `mp_exchange2d`를 호출한다(154–160). 반환·루틴 종료를 포함한다(162–163). 원문: `IF (EWperiodic(ng).or.NSperiodic(ng)) THEN` (145); `CALL exchange_r2d_tile (ng, tile,                               &` (146); `&                          LBi, UBi, LBj, UBj,                     &` (147); `&                          Uwind)` (148); `CALL exchange_r2d_tile (ng, tile,                               &` (149); `&                          LBi, UBi, LBj, UBj,                     &` (150); `&                          Vwind)` (151); `#ifdef DISTRIBUTE` (154); `CALL mp_exchange2d (ng, tile, model, 2,                           &` (155); `&                    LBi, UBi, LBj, UBj,                           &` (156); `&                    NghostPoints,                                 &` (157); `&                    EWperiodic(ng), NSperiodic(ng),               &` (158); `&                    Uwind, Vwind)` (159); `#endif` (160). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 110·128–136: u_wind·v_wind는 초기값 없는 지역 변수이다. 두 변수의 값 대입은 tdays−dstart≤6 조건 안에 있다. 배열 복사는 이 시간 조건 밖에서 실행한다.
- 110: Wdir는 선언 후 이 파일에서 사용하지 않는다.
- 35–41·118–124: 좌표 인수·선언은 SPHERICAL에 따라 달라진다. BENCHMARK 계산식은 latr를 직접 참조한다.
