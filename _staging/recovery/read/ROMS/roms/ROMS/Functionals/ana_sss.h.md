---
file: models/ROMS/raw/source_code/roms/ROMS/Functionals/ana_sss.h
lines: 109
sha256: d8e0cefb155bcd983b65cc034ecc037c1e28a42d571f52c51cca69f5d0a98cd5
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# ana_sss.h — 판독 구간 기록

구간은 1행부터 109행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–48 | ana_sss의 머리말은 해수면 염분(sea surface salinity)을 PSU로 설정하고 표면 물 플럭스(surface water flux) 보정에 사용한다고 적는다(2–14). 머리말의 변수 약어 표기는 SST이다(11). param·forces·ncparam, 입력 인수·MyFile을 선언한다(16–27). 29행은 tile.h를 끼워 넣는다. ana_sss_tile에 FORCES(ng)%sss를 넘긴다(31–34). DISTRIBUTE 조건에 따라 ANANAME(29)에 MyFile을 저장하고 끝낸다(38–48). 원문 조건·대입·전처리 행: `character (len=*), parameter :: MyFile =                          &` (26), `&  __FILE__` (27), `#include "tile.h"` (29), `#ifdef DISTRIBUTE` (38), `IF (Lanafile) THEN` (39), `#else` (40), `IF (Lanafile.and.(tile.eq.0)) THEN` (41), `#endif` (42), `ANANAME(29)=MyFile` (43), `END IF` (44). |
| 49–85 | ana_sss_tile 입구와 param·scalars 모듈이다(50–57). exchange_r2d_tile을 사용하고 DISTRIBUTE에서 mp_exchange2d를 가져온다(59–62). ASSUMED_SHAPE에 따라 sss 출력 배열 경계를 선언한다(70–74). i·j를 선언하고 80행에서 set_bounds.h를 끼워 넣는다. 염분 설정 주석의 단위는 PSU이다(83). 원문 조건·대입·전처리 행: `#ifdef DISTRIBUTE` (60), `#endif` (62), `#ifdef ASSUMED_SHAPE` (70), `#else` (72), `#endif` (74), `#include "set_bounds.h"` (80). |
| 86–93 | 시작 시 50행 ana_sss_tile 안. j=JstrT..JendT·i=IstrT..IendT에서 sss의 우변에 ??? 자리표시자(placeholder)를 둔다(86–90). 경계 교환 주석과 빈 줄을 포함한다(91–93). 원문 조건·대입·전처리 행: `DO j=JstrT,JendT` (86), `DO i=IstrT,IendT` (87), `sss(i,j)=???` (88), `END DO` (89), `END DO` (90). |
| 94–109 | 시작 시 50행 ana_sss_tile 안. 동서 또는 남북 주기경계(periodic boundary)가 있으면 exchange_r2d_tile을 sss에 호출한다(94–98). DISTRIBUTE는 mp_exchange2d에 sss·NghostPoints·주기 플래그를 넘긴다(100–106). RETURN과 루틴 종료를 포함한다(108–109). 원문 조건·대입·전처리 행: `IF (EWperiodic(ng).or.NSperiodic(ng)) THEN` (94), `END IF` (98), `#ifdef DISTRIBUTE` (100), `#endif` (106). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 11·34·88: 머리말은 해수면 염분을 SST로 표기한다. 호출 인수와 실행 대입은 sss를 사용한다.
- 88: 해수면 염분 대입문의 우변은 ??? 자리표시자로 남아 있다.
