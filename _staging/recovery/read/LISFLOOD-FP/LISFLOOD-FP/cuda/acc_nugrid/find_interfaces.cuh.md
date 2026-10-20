---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/acc_nugrid/find_interfaces.cuh
lines: 33
sha256: d53df4db7cb6535f05b158ececa0c5869c80a9cc39124b867527a16eb2ff01dc
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# find_interfaces.cuh — 판독 구간 기록

구간은 1행부터 33행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–16 | `#pragma once` (1), CUDA 실행 환경·장치 실행 매개변수·표준 출력 및 조립 해·방향·모턴 코드(Morton code)·수준·비균일 이웃·고스트 셀(ghost cell)·좌표 복원·경계·비균일 접면(interface) 헤더를 포함한다(3–15). 전처리 조건 분기는 없다. |
| 17–33 | `lis::cuda::acc_nugrid` 이름 공간(namespace)(17–22) 안에 `__global__ void find_interfaces` (24)를 선언한다. 비균일 이웃·조립 해·비균일 접면을 값으로 받으며 기본값은 없다(25–29). 이름 공간 종료(31–33). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
