---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/acc_nugrid/count_neighbours.cuh
lines: 33
sha256: a71762e2785ca98b0ceef4dd1fc53cb6fa1b26c8aa020308bde5cd70c79157ca
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# count_neighbours.cuh — 판독 구간 기록

구간은 1행부터 33행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–14 | `#pragma once` (1), CUDA 실행 환경·장치 실행 매개변수·표준 출력과 조립 해·방향·모턴 코드(Morton code)·수준·경계·고스트 셀(ghost cell)·좌표 복원 헤더 포함(3–13). 전처리 조건 분기는 없다. |
| 15–33 | `lis::cuda::acc_nugrid` 이름 공간(namespace)(15–20) 안에 `__global__ void count_neighbours` (22)를 선언한다. 조립 해 둘, `Pars`, `Solver`, `Boundaries`를 값으로 받으며 기본값은 없다(23–29). 이름 공간 종료(31–33). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
