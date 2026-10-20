---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/fv2/cuda_fv2_simulate.cuh
lines: 31
sha256: ec03877ce4fa527cac80e4dd487e549825c77b0b688959e43ec1748e0e32f496
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# cuda_fv2_simulate.cuh — 판독 구간 기록

구간은 1행부터 31행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–14 | `#pragma once` (1)와 `#pragma once` (3)가 있고 LISFLOOD·geometry·공통 Simulation 헤더를 포함한다(4–6). lis::cuda::fv2 이름 공간(namespace)을 연다(8–13). 조건부 전처리 지시는 없다. |
| 15–31 | `class Simulation : public cuda::Simulation` (15)의 public run은 Fnames·States·Pars·전역 ::Solver 참조와 int verbose를 받는다(18–25). 기본 인수와 실행 본문은 없다. 클래스·이름 공간 종료와 마지막 빈 줄을 포함한다(26–31). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 1·3: pragma once가 두 번 적혀 있다.
