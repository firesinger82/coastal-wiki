---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/acc_nugrid/load_interface_q_vol.cuh
lines: 31
sha256: eb890ab1fd912ec805e8a6275f0061e192dae73f96f82732bfe61fedd30e99cc
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# load_interface_q_vol.cuh — 판독 구간 기록

구간은 1행부터 31행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–22 | `#pragma once` (1) 뒤 CUDA 실행 환경·커널 실행 인수·stdio·방향·모턴 코드(Morton code)·수준 인덱스·수준 계산·비균일 이웃(nonuniform neighbours)·유령 셀(ghost cell) 유형·압축·경계·비균일 접면(nonuniform interfaces) 헤더를 포함한다(3–14). `lis::cuda::acc_nugrid` 이름 공간을 연다(16–21). 이 파일에는 전처리 조건 분기가 없다. |
| 23–31 | 시작 시 16–21행의 `lis::cuda::acc_nugrid` 이름 공간 안. CUDA 커널 지정은 `__global__ void load_interface_q_vol` (23)이다. 인수는 값으로 전달되는 `NonUniformNeighbours d_non_uniform_nghbrs`와 `NonUniformInterfaces d_non_uniform_itrfaces`이다(25–26). 선언과 이름 공간을 닫는다(27–31). 커널 본문과 기본 인수 값은 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
