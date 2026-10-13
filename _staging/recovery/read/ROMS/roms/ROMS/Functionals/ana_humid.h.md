---
file: models/ROMS/raw/source_code/roms/ROMS/Functionals/ana_humid.h
lines: 126
sha256: 52ad829ce1aa882d8084c45578de6d38e955f5b90767230613f908037637e386
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# ana_humid.h — 판독 구간 기록

구간은 1행부터 126행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–55 | ana_humid 시작(2), 저작권·라이선스(4–9), 표면 대기 습도(surface air humidity) 분석식 설명(11–19). 절대습도(absolute humidity)는 수증기 밀도, 비습(specific humidity)은 습윤 공기 질량 대비 수증기 질량비(g/kg), 상대습도(relative humidity)는 실제·포화 혼합비(mixing ratio)의 비율(percentage)이라는 주석(14–19). 모듈·인수·MyFile 선언(23–34), `#include "tile.h"` (36)로 tile.h를 끼워 넣는다. ana_humid_tile에 FORCES(ng)%Hair 전달(38–41). `#ifdef DISTRIBUTE` (45)의 `IF (Lanafile) THEN` (46), `#else` (47)의 `IF (Lanafile.and.(tile.eq.0)) THEN` (48), `#endif` (49) 뒤 ANANAME(9)=MyFile(50). 조건 종료·RETURN·루틴 종료·주석(51–55). |
| 56–88 | ana_humid_tile 시작(57–60), 공통 모듈과 exchange_r2d_tile 사용(63–66). `#ifdef DISTRIBUTE` (67)에서 mp_exchange2d 사용(68), `#endif` (69). 인수 선언(73–75). `#ifdef ASSUMED_SHAPE` (77)는 Hair assumed-shape 출력 배열(78), `#else` (79)는 명시 크기 출력 배열(80), `#endif` (81). i·j 선언(85), `#include "set_bounds.h"` (87)로 set_bounds.h를 끼워 넣는다. 주석·빈 줄 포함. |
| 89–107 | 시작 시 57행 ana_humid_tile 안. 대기 습도 설정 주석(90). `#if defined BENCHMARK` (93)의 j·i 루프(94–95)에서 `Hair(i,j)=0.8_r8` (96). `#elif defined BL_TEST` (99)의 j·i 루프(100–101)에서 `Hair(i,j)=0.776_r8` (102). `#else` (105)의 비주석 원문은 `ana_humidity.h: no values provided for Hair.` (106). 루프 종료(97–98·103–104), `#endif` (107). |
| 108–126 | 시작 시 57행 ana_humid_tile 안. `IF (EWperiodic(ng).or.NSperiodic(ng)) THEN` (111)이면 exchange_r2d_tile(...,Hair) 호출(112–114). `#ifdef DISTRIBUTE` (117)에서 mp_exchange2d(...,1,...,NghostPoints,EWperiodic(ng),NSperiodic(ng),Hair) 호출(118–122), `#endif` (123). 조건 종료·주석·빈 줄·RETURN·루틴 종료(108–110·115–116·124–126). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 105–107: 기본 else 분기에는 'ana_humidity.h: no values provided for Hair.'라는 비주석 행이 있다. 이 행에 적힌 파일명은 실제 파일명 ana_humid.h와 다르다.
- 14–19·93–104: 설명은 습도 세 종류의 단위를 구분한다. BENCHMARK·BL_TEST 대입 블록에는 선택한 습도 종류나 단위를 명시하는 추가 주석이 없다.
