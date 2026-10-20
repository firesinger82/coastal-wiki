---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/operators/limit_slopes.cuh
lines: 25
sha256: 7f26ebcb08210783bba5a13c55ec6363cb9501b7c73743e8fb1d1856be31f89c
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# limit_slopes.cuh — 판독 구간 기록

구간은 1행부터 25행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|

| 1–14 | `#pragma once`와 CUDA 런타임·장치 실행·이웃·해석기·모의 매개변수·Legendre 기저(Legendre basis)·흐름 계수(FlowCoeffs) 헤더를 포함한다(1–10). 제한 경사와 기저 계산 헤더를 포함한다(12–13). 전처리 조건 분기는 없다. 원문: `#pragma once` (1). |
| 15–25 | CUDA 커널(kernel) `limit_slopes` 원형이다(15–25). 조립 해·이웃·모의 매개변수·해석기 매개변수·최세 x/y간격·최대 수심을 받는다(18–24). 기본 인수와 실행 본문은 없다. 원문: `__global__` (15). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
