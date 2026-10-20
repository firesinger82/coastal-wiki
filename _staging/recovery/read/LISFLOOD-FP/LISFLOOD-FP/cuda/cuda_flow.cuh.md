---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/cuda_flow.cuh
lines: 87
sha256: 32f63da239e843458ec445245de2de17754136d2dd7e5df98b119e7c00bd4055
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# cuda_flow.cuh — 판독 구간 기록

구간은 1행부터 87행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–20 | `#pragma once` (1), lisflood 헤더(2), lis::cuda 이름 공간(namespace)(4–7). FlowVector 구조체는 NUMERIC_TYPE H·HU·HV를 가진다(9–13). `__device__ FlowVector star` (15)는 Z·Zstar를 받는 const 메서드다(16–19). 별도 전처리 조건 분기는 없다. |
| 21–45 | 시작 시 9행 FlowVector 구조체 안. `__host__ __device__` (21) 단항 operator-(22)는 `return { -H, -HU, -HV };` (24). `__device__` (27·30)의 physical_flux_x·physical_flux_y 원형(28·31). private(33)의 `__device__ NUMERIC_TYPE calculate_Hstar` (34)와 `__device__ NUMERIC_TYPE speed` (40)는 각각 Z/Zstar(35–38)와 discharge(41–43)를 받는다. 구조체 종료(44), 빈 줄. |
| 46–65 | 시작 시 4–7행 lis::cuda 이름 공간 안. `__host__ __device__` (46)의 inline operator+(47–51)는 `return { lhs.H+rhs.H, lhs.HU+rhs.HU, lhs.HV+rhs.HV };` (53). `__host__ __device__` (56)의 inline operator-(57–61)는 `return { lhs.H-rhs.H, lhs.HU-rhs.HU, lhs.HV-rhs.HV };` (63). |
| 66–87 | 시작 시 4–7행 lis::cuda 이름 공간 안. `__host__ __device__` (66)의 NUMERIC_TYPE lhs·FlowVector rhs 곱셈(67–71)은 `return { lhs*rhs.H, lhs*rhs.HU, lhs*rhs.HV };` (73). `__host__ __device__` (76)의 FlowVector lhs·NUMERIC_TYPE rhs 나눗셈(77–81)은 `return { lhs.H/rhs, lhs.HU/rhs, lhs.HV/rhs };` (83). 이름 공간 종료(86–87). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 9–44: FlowVector의 H·HU·HV에는 선언부 기본값이 없으며 사용자 정의 생성자도 이 구조체에 없다.
- 77–83: 나눗셈 연산자는 rhs에 대한 0 비교 없이 세 성분을 rhs로 나눈다.
