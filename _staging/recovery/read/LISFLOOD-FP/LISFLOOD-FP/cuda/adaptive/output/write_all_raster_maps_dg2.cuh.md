---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/output/write_all_raster_maps_dg2.cuh
lines: 31
sha256: 5fd1d61b1e33696a700549e4867e60e3c884408e5415219bfd46e3dd5f2af4f0
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# write_all_raster_maps_dg2.cuh — 판독 구간 기록

구간은 1행부터 31행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|

| 1–20 | `#pragma once`와 표준 입출력·메모리·CUDA 유틸리티, 흐름 계수(FlowCoeffs)·점·조립 해·모의/해석기 매개변수·저장 간격·최세 격자 헤더를 포함한다(1–14). 래스터 파일(raster file) 출력·Morton 좌표(Morton coordinate) 해독·레벨 시작 인덱스 헤더를 포함한다(16–19). 전처리 조건 분기는 없다. 원문: `#pragma once` (1). |
| 21–31 | `write_all_raster_maps_dg2` 원형이다(21–31). 출력 설정·조립 해·최세 x/y간격·모의/해석기 매개변수·저장 간격·첫 시간 단계 표시를 상수 참조로 받는다(23–30). 기본 인수와 실행 본문은 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
