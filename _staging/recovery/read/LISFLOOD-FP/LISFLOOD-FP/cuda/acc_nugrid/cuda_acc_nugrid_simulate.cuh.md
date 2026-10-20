---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/acc_nugrid/cuda_acc_nugrid_simulate.cuh
lines: 29
sha256: c2da8dd3ad414e1e934cee4b43757a5bbdf7c6d3cc2d42b0b5b3e6b9d6a0a6e2
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# cuda_acc_nugrid_simulate.cuh — 판독 구간 기록

구간은 1행부터 29행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–5 | `#pragma once` (1), 상위 `lisflood.h`, `geometry.h`, CUDA 시뮬레이션 헤더를 포함한다(2–4). 전처리 조건 분기는 없다. |
| 6–29 | `lis::cuda::acc_nugrid` 이름 공간(namespace)을 열고(6–11), `class Simulation : public cuda::Simulation` (13)으로 기반 시뮬레이션을 공개 상속한다. 공개 `void run` 선언은 `Fnames`, `States`, `Pars`, `::Solver` 참조와 verbose를 받으며 기본값은 없다(15–23). 클래스·이름 공간과 마지막 빈 줄을 포함한다(24–29). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
