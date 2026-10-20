---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/acc_nugrid/count_interfaces_per_neighbours.cuh
lines: 30
sha256: 3ccb5df8285e6b7a49344477e2eb2727791f7a1aa9fb0905a47bb5bf0e0f7327
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# count_interfaces_per_neighbours.cuh — 판독 구간 기록

구간은 1행부터 30행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–14 | `#pragma once` (1), CUDA 실행 환경·장치 실행 매개변수·표준 출력과 해·방향·모턴 코드(Morton code)·수준·경계·비균일 이웃·고스트 셀(ghost cell) 헤더를 포함한다(3–13). 전처리 조건 분기는 없다. |
| 15–30 | `lis::cuda::acc_nugrid` 이름 공간(namespace)(15–20) 안에 `__global__ void count_interfaces_per_neighbours` (22)를 선언한다. 비균일 이웃과 조립 해를 값으로 받으며 기본값은 없다(23–26). 이름 공간 종료(28–30). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
