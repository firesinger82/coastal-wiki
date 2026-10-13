---
file: models/ROMS/raw/source_code/roms/ROMS/Functionals/ana_sst.h
lines: 112
sha256: 9638e4462e916842d0aa8e4f7f7646151a92e3eb965e46a84e914498c62cf9fd
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# ana_sst.h — 판독 구간 기록

구간은 1행부터 112행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–51 | ana_sst의 머리말은 해수면 온도(sea surface temperature) SST를 Celsius로 설정하고 표면 열 플럭스(surface heat flux) 보정에 사용한다고 적는다(2–17). 15행은 Q_model 보정 관계식의 주석이다. param·forces·ncparam, 입력 인수·MyFile을 선언한다(19–30). 32행은 tile.h를 끼워 넣는다. ana_sst_tile에 FORCES(ng)%sst를 넘긴다(34–37). DISTRIBUTE 조건에 따라 ANANAME(30)에 MyFile을 저장하고 끝낸다(41–51). 원문 조건·대입·전처리 행: `!       Q_model ~ Q + dQdSST * (T_model - SST)                         !` (15), `character (len=*), parameter :: MyFile =                          &` (29), `&  __FILE__` (30), `#include "tile.h"` (32), `#ifdef DISTRIBUTE` (41), `IF (Lanafile) THEN` (42), `#else` (43), `IF (Lanafile.and.(tile.eq.0)) THEN` (44), `#endif` (45), `ANANAME(30)=MyFile` (46), `END IF` (47). |
| 52–88 | ana_sst_tile 입구와 param·scalars 모듈이다(53–60). exchange_r2d_tile을 사용하고 DISTRIBUTE에서 mp_exchange2d를 가져온다(62–65). ASSUMED_SHAPE에 따라 sst 출력 배열 경계를 선언한다(73–77). i·j를 선언하고 83행에서 set_bounds.h를 끼워 넣는다. SST 단위 주석은 Celsius이다(86). 원문 조건·대입·전처리 행: `#ifdef DISTRIBUTE` (63), `#endif` (65), `#ifdef ASSUMED_SHAPE` (73), `#else` (75), `#endif` (77), `#include "set_bounds.h"` (83). |
| 89–96 | 시작 시 53행 ana_sst_tile 안. j=JstrT..JendT·i=IstrT..IendT에서 sst의 우변에 ??? 자리표시자(placeholder)를 둔다(89–93). 경계 교환 주석과 빈 줄을 포함한다(94–96). 원문 조건·대입·전처리 행: `DO j=JstrT,JendT` (89), `DO i=IstrT,IendT` (90), `sst(i,j)=???` (91), `END DO` (92), `END DO` (93). |
| 97–112 | 시작 시 53행 ana_sst_tile 안. 동서 또는 남북 주기경계(periodic boundary)가 있으면 exchange_r2d_tile을 sst에 호출한다(97–101). DISTRIBUTE는 mp_exchange2d에 sst·NghostPoints·주기 플래그를 넘긴다(103–109). RETURN과 루틴 종료를 포함한다(111–112). 원문 조건·대입·전처리 행: `IF (EWperiodic(ng).or.NSperiodic(ng)) THEN` (97), `END IF` (101), `#ifdef DISTRIBUTE` (103), `#endif` (109). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 91: 해수면 온도 대입문의 우변은 ??? 자리표시자로 남아 있다.
- 46 및 같은 대상 목록의 ana_respiration.h:43: ana_sst와 ana_respiration의 파일 이름 저장 인덱스는 모두 ANANAME(30)이다.
