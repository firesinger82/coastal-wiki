---
file: models/ROMS/raw/source_code/roms/ROMS/Functionals/ana_wtype.h
lines: 184
sha256: 3ba026bef13b5b7bff44cf182d4919bb34ef42bb08b6614d4ed9b3848d97235e
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# ana_wtype.h — 판독 구간 기록

구간은 1행부터 184행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–73 | 시작 시 열린 전처리 조건 없음. `ana_wtype`는 Jerlov 수형(water type) 지수를 설정한다(2·11). 주석은 lmd_swfrac의 단파복사(shortwave radiation) 투과 비율·이중 지수 감쇠(double exponential decay)를 설명한다(12–14). 지원 지수 1..9와 수형 I/IA/IB/II/III/1/3/5/7의 예시를 열거한다(16–36). 모듈·인수·MyFile 선언 뒤 `tile.h`를 포함하고 `ana_wtype_tile`에 h·Jwtype을 전달한다(40–60). DISTRIBUTE별 Lanafile 조건으로 ANANAME(39)을 저장한다(64–70). 반환·루틴 종료를 포함한다(72–73). 원문: `character (len=*), parameter :: MyFile =                          &` (51); `&  __FILE__` (52); `#include "tile.h"` (54); `CALL ana_wtype_tile (ng, tile, model,                             &` (56); `&                     LBi, UBi, LBj, UBj,                          &` (57); `&                     IminS, ImaxS, JminS, JmaxS,                  &` (58); `&                     GRID(ng) % h,                                &` (59); `&                     MIXING(ng) % Jwtype)` (60); `#ifdef DISTRIBUTE` (64); `IF (Lanafile) THEN` (65); `#else` (66); `IF (Lanafile.and.(tile.eq.0)) THEN` (67); `#endif` (68); `ANANAME(39)=MyFile` (69). |
| 74–123 | 시작 시 열린 전처리 조건 없음. `ana_wtype_tile`·모듈·교환 및 통계 루틴 사용·인수 선언을 포함한다(76–98). ASSUMED_SHAPE별 정수 출력 Jwtype와 실수 입력 h의 형상을 선언한다(100–106). first는 save이며 선언 기본값 .TRUE., Stats도 save이다(110·116). i/j/fac 선언·`set_bounds.h` 포함·통계 초기화 주석을 포함한다(112–123). 원문: `#ifdef DISTRIBUTE` (89); `#endif` (91); `#ifdef ASSUMED_SHAPE` (100); `#else` (103); `#endif` (106); `#include "set_bounds.h"` (118). |
| 124–138 | 시작 시 열린 전처리 조건 없음. 시작 시 76행 `ana_wtype_tile` 안. first 조건에서 first=.FALSE.로 바꾸고 Stats의 checksum/count/avg/rms를 0, min을 Large, max를 -Large로 초기화한다(124–132). 빛 흡수(light absorption) 지수 1..9 설정 주석과 빈 줄을 포함한다(133–138). 원문: `IF (first) THEN` (124); `first=.FALSE.` (125); `Stats % checksum=0_i8b` (126); `Stats % count=0` (127); `Stats % min=Large` (128); `Stats % max=-Large` (129); `Stats % avg=0.0_r8` (130); `Stats % rms=0.0_r8` (131). |
| 139–145 | 시작 시 열린 전처리 조건 없음. 시작 시 76행 `ana_wtype_tile` 안. MY_APPLICATION은 역수심 문턱 계수 fac=1.0/1000.0_r8를 사용한다(139–140). j/i 루프에서 수심 h의 tanh 식을 NINT로 반올림하여 Jwtype를 계산한다(141–145). 원문 주석은 결과 범위를 1:5로 적는다(143). 원문: `#ifdef MY_APPLICATION` (139); `fac=1.0/1000.0_r8                   ! Inverse bathymetry threshold` (140); `DO j=JstrT,JendT` (141); `DO i=IstrT,IendT` (142); `Jwtype(i,j)=NINT(5.0_r8-4.5_r8*(TANH(h(i,j)*fac)))       ! 1:5` (143). |
| 146–184 | 시작 시 `#ifdef MY_APPLICATION` (139) 안. 시작 시 76행 `ana_wtype_tile` 안. 나머지 ELSE는 Jwtype 우변에 `???`를 둔다(146–152). `stats_2dfld`를 호출하고 북동 모서리 타일일 때 최소·최대값을 출력한다(156–161). 주기 경계 조건이면 `exchange_r2d_tile`, DISTRIBUTE이면 `mp_exchange2d`를 호출한다(165–177). FORMAT·반환·종료를 포함한다(179–184). 원문: `#else` (146); `DO j=JstrT,JendT` (147); `DO i=IstrT,IendT` (148); `Jwtype(i,j)=???` (149); `#endif` (152); `CALL stats_2dfld (ng, tile, iNLM, r2dvar, Stats, 0,               &` (156); `&                  LBi, UBi, LBj, UBj, Jwtype)` (157); `IF (DOMAIN(ng)%NorthEast_Corner(tile)) THEN` (158); `IF (EWperiodic(ng).or.NSperiodic(ng)) THEN` (165); `CALL exchange_r2d_tile (ng, tile,                               &` (166); `&                          LBi, UBi, LBj, UBj,                     &` (167); `&                          Jwtype)` (168); `#ifdef DISTRIBUTE` (171); `CALL mp_exchange2d (ng, tile, model, 1,                           &` (172); `&                    LBi, UBi, LBj, UBj,                           &` (173); `&                    NghostPoints,                                 &` (174); `&                    EWperiodic(ng), NSperiodic(ng),               &` (175); `&                    Jwtype)` (176); `#endif` (177); `&        '(Grid = ',i2.2,', Min = ',1p,e15.8,0p,                   &` (180); `&                         ' Max = ',1p,e15.8,0p,')')` (181). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 149: MY_APPLICATION이 아닌 분기의 Jwtype 대입 우변은 `???`이다.
- 110·116·124–132: first와 Stats는 save 지역 변수이다. Stats 초기화에는 ng 또는 tile별 별도 조건이 없다.
- 79·101–105·156–157·166–176: Jwtype는 정수 배열이다. 해당 배열을 stats_2dfld·exchange_r2d_tile·mp_exchange2d에 전달한다. 호출 루틴의 정수 인수 지원 여부는 이 파일 판독 범위에 포함하지 않았다.
