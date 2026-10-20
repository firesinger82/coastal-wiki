---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/operators/fv1_update.cuh
lines: 29
sha256: 00cbb27bc33f2d3ecdd3709215d8b978e1174f77bca78991ad9e25100a29744a
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# fv1_update.cuh — 판독 구간 기록

구간은 1행부터 29행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|

| 1–17 | `#pragma once`와 CUDA 런타임·장치 실행·CUB 블록 스캔(block scan)·블록 매크로·이웃·해석기·모의 매개변수·흐름 벡터(FlowVector) 헤더를 포함한다(1–13). HLL(Harten–Lax–van Leer) 플럭스와 하상 생성항(bed source term) 헤더를 포함한다(15–16). 전처리 조건 분기는 없다. 포함된 매크로의 값은 이 파일에서 정의하지 않는다. 원문: `#pragma once` (1). |
| 18–29 | CUDA 커널(kernel) `fv1_update` 원형이다(18–29). 이웃·조립 해·해석기·모의 매개변수·최세 x/y 간격·dt·CFL(Courant–Friedrichs–Lewy) 시간 간격 배열 포인터를 인수로 받는다(21–28). 기본 인수와 실행 본문은 없다. 원문: `__global__` (18). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
