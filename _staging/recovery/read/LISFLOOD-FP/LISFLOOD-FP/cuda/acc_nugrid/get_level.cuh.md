---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/acc_nugrid/get_level.cuh
lines: 20
sha256: 4c9e31f5f392a0ea251b3a6f0bf07dd117ac86ce5efb574784ef406dab5a0492
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# get_level.cuh — 판독 구간 기록

구간은 1행부터 20행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–15 | `#pragma once` (1) 뒤 CUDA 실행 환경·커널 실행 인수·`math.h`·`index_1D.h`·`../../lisflood.h`를 포함한다(3–7). `lis::cuda::acc_nugrid` 이름 공간을 연다(9–14). 이 파일에는 `#if` 계열의 컴파일 조건 분기가 없다. |
| 16–20 | 시작 시 9–14행의 `lis::cuda::acc_nugrid` 이름 공간 안. `__device__ int get_level(index_1D idx);` (16)로 장치 함수를 선언한다. 빈 줄 뒤 이름 공간을 닫는다(17–20). 함수 본문과 기본 인수 값은 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
