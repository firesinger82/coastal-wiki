---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/acc_nugrid/copy_finest_coefficients.cuh
lines: 27
sha256: 366bc87c13ec95549273b21e85683d26049affa5cb3284939393ea0d7c32e4a0
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# copy_finest_coefficients.cuh — 판독 구간 기록

구간은 1행부터 27행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | `#pragma once` (1), CUDA 실행 환경·장치 실행 매개변수와 `AssembledSolution`, `ScaleCoefficients`, `index_1D` 헤더 포함(3–8). 전처리 조건 분기는 없다. |
| 10–27 | `lis::cuda::acc_nugrid` 이름 공간(namespace)(10–15) 안에 `__global__ void copy_finest_coefficients` (17)를 선언한다. 조립 해, 스케일 계수(scale coefficient), 최세밀 수준 시작 인덱스와 `non_uniform_n`을 값으로 받으며 기본값은 없다(18–23). 이름 공간 종료(25–27). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
