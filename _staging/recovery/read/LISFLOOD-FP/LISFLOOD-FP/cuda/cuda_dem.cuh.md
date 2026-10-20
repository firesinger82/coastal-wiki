---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/cuda_dem.cuh
lines: 44
sha256: cb895d4421aba01a34283576e8a40c3122ab3985a058cf7181680ff5df1391b4
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# cuda_dem.cuh — 판독 구간 기록

구간은 1행부터 44행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–11 | `#pragma once` (1), lisflood·geometry 헤더(2–3), lis::cuda 이름 공간(namespace)(5–8), Topography 구조체 시작(10–11). 별도 전처리 조건 분기는 없다. |
| 12–22 | static load 원형(12–21). 파일명, Geometry 참조, int pitch·offset 참조, NUMERIC_TYPE nodata_elevation, int acceleration·verbose를 받고 NUMERIC_TYPE 포인터를 반환한다. 인수의 기본값은 이 선언에 없다. |
| 23–44 | 시작 시 10행 Topography 구조체 안. initialise_Zstar_x(23–27)·initialise_Zstar_y(29–33)는 NUMERIC_TYPE* __restrict__ 출력과 const NUMERIC_TYPE* __restrict__ DEM을 받는다. clamp_boundary_values는 DEM·Geometry 참조·pitch를 받는다(35–40). 구조체·이름 공간 종료(41–44). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
