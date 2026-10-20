---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/acc_nugrid/init_interfaces.cuh
lines: 33
sha256: 176a2d79f176b28a004bdfff826d739ccf01cd69d290a946cf8c902e80c00a74
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# init_interfaces.cuh — 판독 구간 기록

구간은 1행부터 33행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–25 | `#pragma once` (1) 뒤 CUDA 실행 환경·stdio·stdlib·string·블록 매크로·오류 검사·CUDA 유틸리티·조립 해·수준 시작 인덱스·블록 수·래스터(raster) 읽기·지도 쓰기·모턴 코드(Morton code)·비균일 이웃(nonuniform neighbours)·비균일 접면(nonuniform interfaces) 헤더를 포함한다(3–17). `lis::cuda::acc_nugrid` 이름 공간을 연다(19–24). 이 파일에는 전처리 조건 분기가 없다. |
| 26–33 | 시작 시 19–24행의 `lis::cuda::acc_nugrid` 이름 공간 안. `__host__ NonUniformInterfaces init_interfaces` (26)를 값 인수 `NonUniformNeighbours d_non_uniform_nghbrs` 하나로 선언한다(27–29). 선언과 이름 공간을 닫는다(30–33). 함수 본문과 기본 인수 값은 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
