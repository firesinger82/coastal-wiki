---
file: models/ROMS/raw/source_code/roms/ROMS/Functionals/ana_rain.h
lines: 110
sha256: 988ed8c19838b055ad97e6dcd8f0ce353a2460f946e8373c2aefd10432975960
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# ana_rain.h — 판독 구간 기록

구간은 1행부터 110행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–48 | ana_rain의 머리말은 강수율(precipitation rate)의 단위를 kg/m2/s로 적는다(2–14). param·forces·ncparam, 입력 인수·MyFile을 선언한다(16–27). 29행은 tile.h를 끼워 넣는다. ana_rain_tile에 FORCES(ng)%rain을 넘긴다(31–34). DISTRIBUTE 조건에 따라 Lanafile 또는 Lanafile과 tile=0을 검사하고 ANANAME(21)을 설정한다(38–44). RETURN·루틴 종료와 빈 줄을 포함한다(46–48). 원문 조건·대입·전처리 행: `character (len=*), parameter :: MyFile =                          &` (26), `&  __FILE__` (27), `#include "tile.h"` (29), `#ifdef DISTRIBUTE` (38), `IF (Lanafile) THEN` (39), `#else` (40), `IF (Lanafile.and.(tile.eq.0)) THEN` (41), `#endif` (42), `ANANAME(21)=MyFile` (43), `END IF` (44). |
| 49–86 | ana_rain_tile 입구와 모듈 선언이다(50–63). exchange_r2d_tile을 가져오고 DISTRIBUTE에서는 mp_exchange2d를 가져온다(60–63). ASSUMED_SHAPE에 따라 rain 출력 배열의 경계를 선언한다(71–75). 지역 i·j를 선언하고 81행에서 set_bounds.h를 끼워 넣는다. 강수율 설정 주석·빈 줄을 포함한다(83–86). 원문 조건·대입·전처리 행: `#ifdef DISTRIBUTE` (61), `#endif` (63), `#ifdef ASSUMED_SHAPE` (71), `#else` (73), `#endif` (75), `#include "set_bounds.h"` (81). |
| 87–94 | 시작 시 50행 ana_rain_tile 안. j=JstrT..JendT, i=IstrT..IendT의 모든 타일 지점에 rain=0.0_r8를 대입한다(87–91). 경계 교환 주석과 빈 줄을 포함한다(92–94). 원문 조건·대입·전처리 행: `DO j=JstrT,JendT` (87), `DO i=IstrT,IendT` (88), `rain(i,j)=0.0_r8` (89), `END DO` (90), `END DO` (91). |
| 95–110 | 시작 시 50행 ana_rain_tile 안. 동서 또는 남북 주기경계(periodic boundary)가 참이면 exchange_r2d_tile을 호출한다(95–99). DISTRIBUTE에서는 mp_exchange2d에 rain·NghostPoints·두 주기 플래그를 넘긴다(101–107). RETURN과 루틴 종료를 포함한다(109–110). 원문 조건·대입·전처리 행: `IF (EWperiodic(ng).or.NSperiodic(ng)) THEN` (95), `END IF` (99), `#ifdef DISTRIBUTE` (101), `#endif` (107). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 87–91: 이 파일의 강수율 대입은 모든 타일 지점에서 0.0_r8로 고정된다.
