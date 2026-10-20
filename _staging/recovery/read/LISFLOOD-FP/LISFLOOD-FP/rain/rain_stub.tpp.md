---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/rain/rain_stub.tpp
lines: 98
sha256: d56d8daaa412a2e3c2cf7e78d19c7bc5a96afb525aea41563b8d3ab3f96659f9
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# rain_stub.tpp — 판독 구간 기록

구간은 1행부터 98행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–12 | rain.h·utility.h를 포함한다(1–2). 템플릿 생성자는 filename·verbose·allocator를 받지만 본문은 비어 있다(4–11). 이 파일 자체에는 전처리 조건이 없다. rain.cpp의 #if _NETCDF == 1이 불성립하는 #else 쪽에서 포함되는 대체 구현(stub)이다. |
| 13–30 | has_same_origin과 is_tile_size_multiple_of_grid는 인수를 사용하지 않고 각각 false를 반환한다(13–20·22–29). |
| 31–46 | update_time의 본문은 비어 있다(31–36). update_time_SGC는 전달 시각을 사용하지 않고 false를 반환한다(38–45). |
| 47–70 | rate_at_cell과 rate_at_cell_SGC는 각각 `throw std::logic_error("Not implemented");` (55), `throw std::logic_error("Not implemented");` (68)로 std::logic_error를 던진다. 첫 함수는 Pars·i·j, 둘째 함수는 i·j·dx_col·dy_col·tly를 받는다(48–53·59–66). |
| 71–98 | update_H는 Pars·Solver·Arrays 인수를 받고 본문이 비어 있다(71–78). update_rain_grid_SGM은 강우·DEM·행 범위·간격·면적 등의 인수를 받고 본문이 비어 있다(80–94). 소멸자도 빈 본문이다(96–98). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 4–11: 생성자는 전달된 allocator를 allocator_ 초기화 목록에 넣지 않는다. 본문에도 enabled_·netcdf_·geometry_를 설정하는 문장이 없다.
- 55·68: 셀 강우율 함수의 대체 구현은 0 반환 대신 std::logic_error 예외를 발생시킨다.
