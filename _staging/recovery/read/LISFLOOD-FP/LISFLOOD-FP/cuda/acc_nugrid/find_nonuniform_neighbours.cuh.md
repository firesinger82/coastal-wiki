---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/acc_nugrid/find_nonuniform_neighbours.cuh
lines: 35
sha256: d54e75ef9c0edeb3fba52e6ebfda804fe102656287d973b22d742b6871f4b6ba
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# find_nonuniform_neighbours.cuh — 판독 구간 기록

구간은 1행부터 35행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–15 | `#pragma once` (1), CUDA 실행 환경·장치 실행 매개변수·표준 출력 및 조립 해·방향·모턴 코드(Morton code)·수준·비균일 이웃·고스트 셀(ghost cell)·좌표 복원·경계 헤더를 포함한다(3–14). 전처리 조건 분기는 없다. |
| 16–35 | `lis::cuda::acc_nugrid` 이름 공간(namespace)(16–21) 안에 `__global__ void find_nonuniform_neighbours` (23)를 선언한다. 조립 해 둘·Pars·Solver·비균일 이웃·Boundaries를 값으로 받으며 기본값은 없다(24–31). 이름 공간 종료(33–35). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
