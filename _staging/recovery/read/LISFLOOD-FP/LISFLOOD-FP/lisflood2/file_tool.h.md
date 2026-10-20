---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/lisflood2/file_tool.h
lines: 80
sha256: 78d36027189f0ea885214ecda7d671cf3e9ccd3c6c108aa67e1735f2e29fa928
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# file_tool.h — 판독 구간 기록

구간은 1행부터 80행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–14 | 파일 도구 작성자·날짜·전역 변수에 의존하지 않는 ASCII 격자 입출력이라는 주석(1–7). `#pragma once` (8), write_time 원형(10–11), `#define NETCDF_IGNORE -1` (13). 이 구간은 전처리 조건 밖이다. |
| 15–20 | `#if _NUMERIC_MODE == 1` (15)에서 `#define NC_GET_VARA_NUMERIC_TYPE nc_get_vara_double` (16), `#else` (17)에서 `#define NC_GET_VARA_NUMERIC_TYPE nc_get_vara_float` (18), `#endif` (19). 같은 소스 루트 config.default.cmake:2의 `add_compile_definitions(_NUMERIC_MODE=1)`은 double 판독 함수를 선택한다. 다른 값은 float 판독 함수를 선택한다. |
| 21–34 | 전처리 조건 밖. StartNetCDF 원형은 격자 크기·파일명·NetCDFState·수심/수위/유량/유속/수로 유속/수로 출력 스위치를 받는다(21–29). CloseNetCDF는 NetCDFState 포인터형과 정수 파일 ID형 오버로드(overload)를 선언한다(31·33). |
| 35–65 | 전처리 조건 밖. write_grid는 패딩(padding) 없는 격자형(40–44), 패딩을 tmp_grid로 제거할 수 있는 형(52–56)을 선언한다. write_sum_grid는 dataA/dataB·작업 격자·수심 임계값·격자/좌표·출력 매개변수를 받는다(61–64). 각 주석은 netcdf_varid가 NETCDF_IGNORE일 때 NetCDF로 쓰지 않는다고 적는다(37·50·59). |
| 66–80 | 전처리 조건 밖. write_file_asc(66), read_file_asc(68), read_file_bin(70), 내용을 통해 ASCII/binary를 구분한다는 read_file(72–75), compare_grids(77), 시간별 NetCDF 판독 read_file_netCDF와 최초 열기 read_file_netCDF_start(79–80)를 선언한다. 실행 조건문·수치 계산 본문은 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 1–80: NUMERIC_TYPE·OutputParams·NetCDFState·NetCDFVariable을 사용하지만 이 파일 안에는 해당 정의를 포함하는 include 지시가 없다.
