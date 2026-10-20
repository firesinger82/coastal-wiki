---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/operators/friction_implicit.cuh
lines: 25
sha256: 1c821418e02024062ab03ede1c6aca2d0d8d0927583f0ddad5a200fca19aa9de
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# friction_implicit.cuh — 판독 구간 기록

구간은 1행부터 25행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|

| 1–16 | `#pragma once`와 CUDA 런타임·장치 실행 매개변수·CUB 블록 스캔(block scan)·블록 변수 매크로·이웃·해석기·모의 매개변수 헤더를 포함한다(1–12). `apply_friction.cuh`와 Morton 코드(Morton code) 생성 헤더를 포함한다(14–15). 전처리 조건 분기는 없다. 포함된 매크로의 값은 이 파일에서 정의하지 않는다. 원문: `#pragma once` (1). |
| 17–25 | CUDA 커널(kernel) `friction_implicit` 원형을 선언한다(17–25). 인수는 조립 해(AssembledSolution), 이웃, 해석기 매개변수, 모의 매개변수, 실수 dt이다(20–24). 기본 인수와 실행 본문은 없다. 원문: `__global__` (17). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
