---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/swe/dg2/fields.h
lines: 113
sha256: 195518d19ced437b7bfe8abcb22a379bd3222d9d353726e908dde8717d19fdc0
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# fields.h — 판독 구간 기록

구간은 1행부터 113행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–25 | `#pragma once` (1)로 중복 포함을 막고 functional·lisflood.h를 포함한다(2–3). dg2 이름공간(namespace)에서 initialise_field의 두 오버로드(overload)를 선언한다(5–24). 두 함수는 `std::function<NUMERIC_TYPE(NUMERIC_TYPE, NUMERIC_TYPE)> func,` (9) 또는 `std::function<NUMERIC_TYPE(NUMERIC_TYPE, NUMERIC_TYPE)> func,` (18) 형식의 좌표 함수와 Pars·F·F1x·F1y를 받는다. 둘째 선언만 no_data를 추가로 받는다(19). 이 헤더에는 추가 전처리 분기가 없다. |
| 26–56 | 시작 시 5행 dg2 이름공간 안. downscale은 wd0·wd1x·wd1y·no_data·Pars·F를 받는다(26–34). initialise_h_from_eta는 eta·Pars·Arrays를 받는다(36–41). read_dem_slopes는 파일명·격자·배열·verbose, zero_dem_perimeter_slopes는 격자·배열을 받는다(43–55). |
| 57–93 | 시작 시 5행 dg2 이름공간 안. read_h_slopes와 read_discharge_slopes는 Fnames·Pars·Arrays·const int verbose를 받는다(57–71). write_dem·write_DScaled·write_startfile은 const char* root·Pars·Arrays를 받는다(73–92). 선언만 있고 계산식은 없다. |
| 94–113 | 시작 시 5행 dg2 이름공간 안. allocate_fields·deallocate_fields는 Pars·Arrays를 받고(94–98·106–110), allocate는 BoundaryValues&·Pars를 받으며(100–104), deallocate는 BoundaryValues&만 받는다(112). 이름공간을 닫는다(113). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
