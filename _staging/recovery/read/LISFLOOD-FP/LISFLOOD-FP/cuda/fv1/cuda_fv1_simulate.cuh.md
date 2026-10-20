---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/fv1/cuda_fv1_simulate.cuh
lines: 27
sha256: 428f044dd64df2b2649546eaf6f0b27e795405d26353ae6ed7d86de9c6970ff5
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# cuda_fv1_simulate.cuh — 판독 구간 기록

구간은 1행부터 27행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–11 | `#pragma once` (1), `#include "../../lisflood.h"` (2), `#include "../cuda_simulate.cuh"` (3)와 lis::cuda::fv1 이름공간(namespace)(5–10)이다. 전처리 조건 분기는 없다. |
| 12–27 | `class Simulation : public cuda::Simulation` (12)은 공통 Simulation을 공개 상속(public inheritance)한다. 공개 run은 Fnames·States·Pars·전역 ::Solver 참조와 verbose를 받는다(15–22). 클래스와 이름공간을 닫는다(23–27). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
