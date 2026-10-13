---
file: models/ROMS/raw/source_code/roms/ROMS/Functionals/ana_pair.h
lines: 120
sha256: 735050a56d76755e4ff628d1b9770b8adc51e9ad4a4f624dbcabfad0283979a6
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# ana_pair.h — 판독 구간 기록

구간은 1행부터 120행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–48 | ana_pair는 표면 기압(surface air pressure)을 mb 단위로 설정한다는 머리말이다(2–14). param·forces·ncparam, 입력 ng·tile·model, MyFile을 선언한다(16–27). 29행은 tile.h를 끼워 넣는다. ana_pair_tile에 FORCES(ng)%Pair를 넘긴다(31–34). DISTRIBUTE는 Lanafile, 나머지는 Lanafile과 tile=0을 검사하고 ANANAME(17)을 설정한다(38–44). RETURN과 루틴 종료를 포함한다(46–48). 원문 조건·대입·전처리 행: `character (len=*), parameter :: MyFile =                          &` (26), `&  __FILE__` (27), `#include "tile.h"` (29), `#ifdef DISTRIBUTE` (38), `IF (Lanafile) THEN` (39), `#else` (40), `IF (Lanafile.and.(tile.eq.0)) THEN` (41), `#endif` (42), `ANANAME(17)=MyFile` (43), `END IF` (44). |
| 49–86 | ana_pair_tile 입구이다(50–54). param·scalars·exchange_r2d_tile을 사용하고 DISTRIBUTE에서 mp_exchange2d를 가져온다(56–62). ASSUMED_SHAPE에 따라 Pair 출력 배열의 경계를 선언한다(70–74). 지역 i·j를 선언하고 80행에서 set_bounds.h를 끼워 넣는다. 주석은 기압 단위 환산식을 적는다(83–85). 원문 조건·대입·전처리 행: `#ifdef DISTRIBUTE` (60), `#endif` (62), `#ifdef ASSUMED_SHAPE` (70), `#else` (72), `#endif` (74), `#include "set_bounds.h"` (80), `!  (1 mb = 100 Pa = 1 hPa,  1 bar = 1.0e+5 N/m2 = 1.0e+5 dynes/cm2).` (84). |
| 87–102 | 시작 시 50행 ana_pair_tile 안. BENCHMARK는 모든 타일 지점에 Pair=1025.0_r8를 설정한다(87–92). BL_TEST는 Pair=1013.48_r8를 설정한다(93–98). 기본 분기는 Pair 값이 제공되지 않았다는 문장을 둔다(99–101). 원문 조건·대입·전처리 행: `#if defined BENCHMARK` (87), `DO j=JstrT,JendT` (88), `DO i=IstrT,IendT` (89), `Pair(i,j)=1025.0_r8` (90), `END DO` (91), `END DO` (92), `#elif defined BL_TEST` (93), `DO j=JstrT,JendT` (94), `DO i=IstrT,IendT` (95), `Pair(i,j)=1013.48_r8` (96), `END DO` (97), `END DO` (98), `#else` (99), `ana_pair.h: no values provided for Pair.` (100), `#endif` (101). |
| 103–120 | 시작 시 50행 ana_pair_tile 안. 동서 또는 남북 주기경계(periodic boundary)가 참이면 exchange_r2d_tile을 호출한다(105–109). DISTRIBUTE에서는 mp_exchange2d에 Pair·NghostPoints·두 주기 플래그를 넘긴다(111–117). RETURN과 루틴 종료를 포함한다(119–120). 원문 조건·대입·전처리 행: `IF (EWperiodic(ng).or.NSperiodic(ng)) THEN` (105), `END IF` (109), `#ifdef DISTRIBUTE` (111), `#endif` (117). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 87–100: 기압 상수는 BENCHMARK에서 1025.0_r8, BL_TEST에서 1013.48_r8이다. 기본 분기는 값을 대입하지 않고 “ana_pair.h: no values provided for Pair.” 문장을 둔다.
- 84: 기압 단위 주석은 “1 bar = 1.0e+5 N/m2 = 1.0e+5 dynes/cm2”라고 적는다. 이 기록에서는 해당 단위 등식의 타당성을 검증하지 않았다.
