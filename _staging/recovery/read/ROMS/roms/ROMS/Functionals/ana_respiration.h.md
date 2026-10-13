---
file: models/ROMS/raw/source_code/roms/ROMS/Functionals/ana_respiration.h
lines: 127
sha256: 3f2bcc35079359325650c3dcfa62b934965b6a2fd2c0c938341b7ace32ff76a5
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# ana_respiration.h — 판독 구간 기록

구간은 1행부터 127행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–48 | ana_respiration의 머리말은 저산소(hypoxia) 호흡률(respiration rate)의 해석식 설정을 설명한다(2–14). param·ncparam·ocean, 입력 인수·MyFile을 선언한다(16–27). 29행은 tile.h를 끼워 넣는다. ana_respiration_tile에 OCEAN(ng)%respiration을 넘긴다(31–34). DISTRIBUTE 조건에 따라 Lanafile 또는 Lanafile과 tile=0을 검사하고 ANANAME(30)을 설정한다(38–44). RETURN·루틴 종료와 빈 줄을 포함한다(46–48). 원문 조건·대입·전처리 행: `character (len=*), parameter :: MyFile =                          &` (26), `&  __FILE__` (27), `#include "tile.h"` (29), `#ifdef DISTRIBUTE` (38), `IF (Lanafile) THEN` (39), `#else` (40), `IF (Lanafile.and.(tile.eq.0)) THEN` (41), `#endif` (42), `ANANAME(30)=MyFile` (43), `END IF` (44). |
| 49–86 | ana_respiration_tile 입구와 param·scalars·biology 사용이다(50–58). exchange_r3d_tile과 DISTRIBUTE의 mp_exchange3d를 가져온다(60–63). ASSUMED_SHAPE에 따라 respiration 출력 배열의 경계를 선언하고 기본 분기는 N(ng)층을 명시한다(71–75). i·j·k를 선언하고 81행에서 set_bounds.h를 끼워 넣는다. 호흡률 단위 주석은 1/day이다(84). 원문 조건·대입·전처리 행: `#ifdef DISTRIBUTE` (61), `#endif` (63), `#ifdef ASSUMED_SHAPE` (71), `#else` (73), `#endif` (75), `#include "set_bounds.h"` (81). |
| 87–109 | 시작 시 50행 ana_respiration_tile 안. CHESAPEAKE_1TERM은 모든 층·타일 지점에 ResRate(ng)를 대입한다(87–91). i>=72·j<=35 또는 i=61..71·j=6..26 조건에서는 respiration을 0으로 바꾼다(92–96). 기본 분기는 모든 층·타일 지점에 ResRate(ng)를 그대로 대입한다(100–108). 루프·전처리 종료와 주석 줄을 포함한다(97–109). 원문 조건·대입·전처리 행: `#if defined CHESAPEAKE_1TERM` (87), `DO k=1,N(ng)` (88), `DO j=JstrT,JendT` (89), `DO i=IstrT,IendT` (90), `respiration(i,j,k)=ResRate(ng)` (91), `IF (((i.ge.72).and.(j.le.35)).or.                           &` (92), `&          (((i.ge.61).and.(i.le.71)).and.                         &` (93), `&           ((j.ge. 6).and.(j.le.26)))) THEN` (94), `respiration(i,j,k)=0.0_r8` (95), `END IF` (96), `END DO` (97), `END DO` (98), `END DO` (99), `#else` (100), `DO k=1,N(ng)` (101), `DO j=JstrT,JendT` (102), `DO i=IstrT,IendT` (103), `respiration(i,j,k)=ResRate(ng)` (104), `END DO` (105), `END DO` (106), `END DO` (107), `#endif` (108). |
| 110–127 | 시작 시 50행 ana_respiration_tile 안. 동서 또는 남북 주기경계(periodic boundary)가 참이면 exchange_r3d_tile을 1..N(ng)층에 호출한다(112–116). DISTRIBUTE는 mp_exchange3d에 같은 층 범위·NghostPoints·두 주기 플래그를 넘긴다(118–124). RETURN과 루틴 종료를 포함한다(126–127). 원문 조건·대입·전처리 행: `IF (EWperiodic(ng).or.NSperiodic(ng)) THEN` (112), `END IF` (116), `#ifdef DISTRIBUTE` (118), `#endif` (124). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 92–95: CHESAPEAKE_1TERM의 무호흡 영역은 i·j 인덱스 72·35·61·71·6·26으로 고정된다. 이 조건은 수직층 k를 사용하지 않는다.
