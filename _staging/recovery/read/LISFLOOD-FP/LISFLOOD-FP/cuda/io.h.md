---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/io.h
lines: 149
sha256: ee31b2e6d6cfbacacd20ec9db89c7d7db161a9943f51a99db1d602cafeb5673d
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# io.h — 판독 구간 기록

구간은 1행부터 149행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–36 | `#pragma once` (1)과 future·geometry·LISFLOOD 헤더 포함(2–4). lis 이름 공간(namespace)(6–7). AsciiRaster는 static read_header·read·replace_no_data를 선언한다(9–35). 인수로 파일·격자·nodata 참조, 배열·pitch·offset, 원래 nodata와 대체값을 받는다. 조건부 전처리 지시는 없다. |
| 37–58 | 시작 시 6행 이름 공간·9행 AsciiRaster 구조체 안. `template<typename F>` (37)의 static write는 파일·배열 접근자 F·Geometry·pitch·offset·nodata·outflag를 받는다(38–46). 기본값은 `int precision = DEFAULT_PRECISION` (47). static match_cell_dimensions_or_die는 expected·candidate 격자 참조와 message를 받는다(51–56). 구조체 종료(57). |
| 59–90 | StartFile은 static load와 subtract_dem을 공개하고(59–78), zero_no_data_values는 private static으로 둔다(80–88). load는 파일명·배열·격자·pitch·offset·verbose를 받는다. subtract_dem은 H·DEM·격자·pitch·offset을 받는다. |
| 91–111 | Snapshot은 static initialise_async를 선언한다(91–93). `template<typename F>` (95)의 write_async는 `std::future<void>`를 반환하며 배열·격자·pitch·offset·prefix·counter·suffix·verbose·outflag·call_gzip 참조를 받는다(96–107). 기본값은 `int precision = DEFAULT_PRECISION,` (108), `NUMERIC_TYPE no_data_value = NULLVAL` (109). 두 매크로의 수치 정의는 이 파일에 없다. |
| 112–129 | 시작 시 6행 이름 공간·91행 Snapshot 안. `template<typename F>` (112)의 동기 write는 배열·격자·pitch·offset·prefix·counter·suffix·verbose·outflag·call_gzip 참조를 받는다(113–124). 기본값은 `int precision = DEFAULT_PRECISION,` (125), `NUMERIC_TYPE no_data_value = NULLVAL` (126). |
| 130–149 | 시작 시 6행 이름 공간·91행 Snapshot 안. `template<typename F>` (130)의 write_max는 counter·gzip 인수 없이 배열·격자·pitch·offset·prefix·suffix·verbose·outflag를 받는다(131–140). 기본값은 `int precision = DEFAULT_PRECISION,` (141), `NUMERIC_TYPE no_data_value = NULLVAL` (142). 구조체·이름 공간 종료(145–147). `#include "io.templates.cpp"` (149)로 템플릿(template) 구현을 포함한다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
