---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/rain/rain.h
lines: 118
sha256: 21b030d418859f5ac090365b7742c06f0be182e439adf7c299be9c64744844a9
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# rain.h — 판독 구간 기록

구간은 1행부터 118행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–16 | `#pragma once` (1)로 중복 포함을 막고 lisflood.h·geometry.h·DataTypes.h를 포함한다(2–4). `template<class Allocator = std::allocator<NUMERIC_TYPE>>` (6)을 갖는 DynamicRain 공개 클래스 선언이다(7–9). 생성자는 파일명·verbose와 `const Allocator& = Allocator()` (14) 기본 인수를 받는다. 이 헤더에는 _NETCDF에 따른 조건부 선언이 없다. |
| 17–51 | has_same_origin은 강우와 수치표고모델(digital elevation model, DEM)의 원점 일치 검사, is_tile_size_multiple_of_grid는 강우 타일 크기와 DEM 셀 크기의 정수배 검사로 주석에 적혀 있다(17–32). update_time과 update_time_SGC는 시각을 받고 필요한 자료를 갱신하며, 후자는 bool을 반환하도록 선언한다(34–50). |
| 52–77 | rate_at_cell은 Pars 포인터와 i·j를 받으며, 주석은 셀 강우율 단위를 m/s, 강우 영역 밖의 값을 0이라고 적는다(52–61). rate_at_cell_SGC는 i·j와 열 간격 dx_col·dy_col·tly를 받는다(63–70). update_H는 Pars·Solver·Arrays 포인터를 받는다(72–77). |
| 78–92 | update_rain_grid_SGM은 현재 시각, 강우·DEM 배열, 젖음·마름 행 범위(WetDryRowBound), dx_col·dy_col·tyl, 행 수, 패딩 포함 열 수, 행별 셀 면적 배열을 받는 void 선언이다(79–91). 구현이나 조건 분기는 이 구간에 없다. |
| 93–110 | enabled는 enabled_를 반환한다(93–96). geometry는 const Geometry 참조를 반환한다(98–101). data는 현재 시각의 공간 강우율 m/s 지도라는 주석과 함께 netcdf_.data 포인터를 반환한다(103–109). |
| 111–118 | 소멸자를 선언한다(111). 비공개 필드는 enabled_, NetCDFVariable netcdf_, Geometry geometry_, Allocator allocator_이며 이 선언에는 멤버 초기값이 없다(113–118). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 52–55·113–118: 영역 밖 강우율 0은 인터페이스 주석이다. 이 헤더는 범위 검사 구현을 포함하지 않는다.
- 114: enabled_ 선언에는 기본 초기값이 없다.
