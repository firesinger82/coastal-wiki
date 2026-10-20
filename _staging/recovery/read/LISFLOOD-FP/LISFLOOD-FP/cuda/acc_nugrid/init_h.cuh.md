---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/acc_nugrid/init_h.cuh
lines: 32
sha256: 520df6ef61274af90b94632ac38d10ad87e0c8275356d83cfe2f187cfa9fa408
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# init_h.cuh — 판독 구간 기록

구간은 1행부터 32행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–24 | `#pragma once` (1) 뒤 CUDA 실행 환경·커널 실행 인수·stdio·조립 해·방향·모턴 코드(Morton code)·수준 인덱스·수준 계산·비균일 이웃(nonuniform neighbours)·비균일 접면(nonuniform interfaces)·유령 셀(ghost cell) 유형·압축·경계·점원(point sources) 헤더를 포함한다(3–16). `lis::cuda::acc_nugrid` 이름 공간을 연다(18–23). 이 파일에는 전처리 조건 분기가 없다. |
| 25–32 | 시작 시 18–23행의 `lis::cuda::acc_nugrid` 이름 공간 안. CUDA 커널을 `__global__ void init_h` (25)로 선언한다. 인수는 값으로 전달되는 `AssembledSolution d_assem_sol`이다(27). 선언과 이름 공간을 닫는다(28–32). 커널 본문과 기본 인수 값은 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
