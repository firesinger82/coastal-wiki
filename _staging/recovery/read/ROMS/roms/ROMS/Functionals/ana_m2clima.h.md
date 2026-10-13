---
file: models/ROMS/raw/source_code/roms/ROMS/Functionals/ana_m2clima.h
lines: 111
sha256: d2f04a2d48c80e5849223bdf9fce2a1aeedaff180ea9cb9e3056501abc7c2bce
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# ana_m2clima.h — 판독 구간 기록

구간은 1행부터 111행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–45 | ana_m2clima 시작(2), 저작권·라이선스와 2차원 운동량(momentum) 기후값(climatology) 설정 설명(4–14). mod_param·mod_ncparam·인수·MyFile 선언(15–25). `#include "tile.h"` (27)로 tile.h를 끼워 넣는다. ana_m2clima_tile에 경계 인수 전달(29–31). `#ifdef DISTRIBUTE` (35)의 `IF (Lanafile) THEN` (36), `#else` (37)의 `IF (Lanafile.and.(tile.eq.0)) THEN` (38), `#endif` (39) 뒤 ANANAME(11)=MyFile(40). 조건 종료·RETURN·루틴 종료·주석(41–45). |
| 46–72 | ana_m2clima_tile 시작(47–49), mod_param·mod_clima·mod_scalars·exchange_2d_mod 사용(52–56). `#ifdef DISTRIBUTE` (57)에서 mp_exchange2d 사용(58), `#endif` (59). 인수·i·j 선언(63–69), `#include "set_bounds.h"` (71)로 set_bounds.h를 끼워 넣는다. 주석·빈 줄 포함. |
| 73–88 | 시작 시 47행 ana_m2clima_tile 안. 2차원 운동량 기후값 주석(74). `IF (Lm2CLM(ng)) THEN` (77)의 j=JstrT..JendT·i=IstrP..IendT 루프(78–79)에서 `CLIMA(ng)%ubarclm(i,j)=???` (80). j=JstrP..JendT·i=IstrT..IendT 루프(83–84)에서 `CLIMA(ng)%vbarclm(i,j)=???` (85). 루프 종료·주석(81–82·86–88). 조건은 계속 열린다. |
| 89–111 | 시작 시 47행 ana_m2clima_tile·77행 Lm2CLM 참 분기 안. `IF (EWperiodic(ng).or.NSperiodic(ng)) THEN` (91)이면 exchange_u2d_tile(...,CLIMA(ng)%ubarclm)(92–94)·exchange_v2d_tile(...,CLIMA(ng)%vbarclm)(95–97) 호출. `#ifdef DISTRIBUTE` (100)에서 mp_exchange2d(...,2,...,NghostPoints,EWperiodic(ng),NSperiodic(ng),ubarclm,vbarclm) 호출(101–106). 마지막 인수 행은 `%                      CLIMA(ng) % vbarclm)` (106). `#endif` (107), Lm2CLM 조건 종료(108), 주석·RETURN·루틴 종료(109–111). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 80·85: 두 기후값 대입의 우변은 ???이다.
- 105–106: mp_exchange2d 호출의 105행은 선행 &를 사용한다. 마지막 인수 행 106은 선행 %를 사용한다.
