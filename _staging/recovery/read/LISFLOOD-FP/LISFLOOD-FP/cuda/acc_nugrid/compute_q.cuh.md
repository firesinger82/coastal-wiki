---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/acc_nugrid/compute_q.cuh
lines: 37
sha256: 90112a249206abaafe392a2eff4ce3cd4504eccc3c1a515955b9ea77056cfaa8
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# compute_q.cuh — 판독 구간 기록

구간은 1행부터 37행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–16 | `#pragma once` (1), CUDA 실행 환경·장치 실행 매개변수·표준 출력과 해·방향·모턴 코드(Morton code)·수준·비균일 이웃·접면(interface)·고스트 셀(ghost cell)·경계 관련 헤더 포함(3–15). 전처리 조건 분기는 없다. |
| 17–37 | `lis::cuda::acc_nugrid` 이름 공간(namespace)(17–22) 안에 `__global__ void compute_q` (24)를 선언한다. 인수는 조립 해, 비균일 이웃, 비균일 접면, `Pars`, `Solver`, `Boundaries`, `non_uniform_n`이고 모두 값으로 받는다(25–33). 인수 기본값은 없다. 이름 공간 종료(35–37). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
