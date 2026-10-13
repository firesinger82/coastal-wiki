---
file: models/ROMS/raw/source_code/roms/ROMS/Functionals/ana_tair.h
lines: 119
sha256: 48a1fd52882da4caf2961e0209f8780e8ac46fe58b63005cdefd2bfb5aab8e4f
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# ana_tair.h — 판독 구간 기록

구간은 1행부터 119행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–48 | ana_tair의 머리말은 표면 기온(surface air temperature)의 단위를 degC로 적는다(2–14). param·forces·ncparam, 입력 인수·MyFile을 선언한다(16–27). 29행은 tile.h를 끼워 넣는다. ana_tair_tile에 FORCES(ng)%Tair를 넘긴다(31–34). DISTRIBUTE 조건에 따라 ANANAME(32)에 MyFile을 저장하고 끝낸다(38–48). 원문 조건·대입·전처리 행: `character (len=*), parameter :: MyFile =                          &` (26), `&  __FILE__` (27), `#include "tile.h"` (29), `#ifdef DISTRIBUTE` (38), `IF (Lanafile) THEN` (39), `#else` (40), `IF (Lanafile.and.(tile.eq.0)) THEN` (41), `#endif` (42), `ANANAME(32)=MyFile` (43), `END IF` (44). |
| 49–85 | ana_tair_tile 입구와 param·scalars 모듈이다(50–57). exchange_r2d_tile을 사용하고 DISTRIBUTE에서 mp_exchange2d를 가져온다(59–62). ASSUMED_SHAPE에 따라 Tair 출력 배열의 경계를 선언한다(70–74). 지역 i·j를 선언하고 80행에서 set_bounds.h를 끼워 넣는다. 기온 설정 주석과 빈 줄을 포함한다(82–85). 원문 조건·대입·전처리 행: `#ifdef DISTRIBUTE` (60), `#endif` (62), `#ifdef ASSUMED_SHAPE` (70), `#else` (72), `#endif` (74), `#include "set_bounds.h"` (80). |
| 86–91 | 시작 시 50행 ana_tair_tile 안. BENCHMARK는 j=JstrT..JendT·i=IstrT..IendT의 모든 타일 지점에 Tair=4.0_r8를 설정한다(86–91). 원문 조건·대입·전처리 행: `#if defined BENCHMARK` (86), `DO j=JstrT,JendT` (87), `DO i=IstrT,IendT` (88), `Tair(i,j)=4.0_r8` (89), `END DO` (90), `END DO` (91). |
| 92–97 | 시작 시 `#if defined BENCHMARK` (86) 안. 시작 시 50행 ana_tair_tile 안. BL_TEST는 같은 타일 범위의 모든 지점에 Tair=23.567_r8를 설정한다(92–97). 원문 조건·대입·전처리 행: `#elif defined BL_TEST` (92), `DO j=JstrT,JendT` (93), `DO i=IstrT,IendT` (94), `Tair(i,j)=23.567_r8` (95), `END DO` (96), `END DO` (97). |
| 98–103 | 시작 시 `#if defined BENCHMARK` (86)의 `#elif defined BL_TEST` (92) 분기 안. 시작 시 50행 ana_tair_tile 안. 기본 전처리 분기는 Tair 값이 제공되지 않았다는 문장을 둔다(98–100). 경계 교환 주석과 빈 줄을 포함한다(101–103). 원문 조건·대입·전처리 행: `#else` (98), `ana_tair.h: no values provided for Tair.` (99), `#endif` (100). |
| 104–119 | 시작 시 50행 ana_tair_tile 안. 동서 또는 남북 주기경계(periodic boundary)가 있으면 exchange_r2d_tile을 Tair에 호출한다(104–108). DISTRIBUTE는 mp_exchange2d에 Tair·NghostPoints·주기 플래그를 넘긴다(110–116). RETURN과 루틴 종료를 포함한다(118–119). 원문 조건·대입·전처리 행: `IF (EWperiodic(ng).or.NSperiodic(ng)) THEN` (104), `END IF` (108), `#ifdef DISTRIBUTE` (110), `#endif` (116). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 86–99: 기온은 BENCHMARK에서 4.0_r8, BL_TEST에서 23.567_r8로 고정된다. 기본 전처리 분기는 “ana_tair.h: no values provided for Tair.” 문장을 둔다.
