---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/acc_nugrid/project_assem_sol.cuh
lines: 31
sha256: bfdcd69689bd139597247fdf69787cdaf6dd133cc4e9182380b7448ac7074bf3
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# project_assem_sol.cuh — 판독 구간 기록

구간은 1행부터 31행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–15 | `#pragma once` (1) 및 트리 순회·역 Z 순서·실수 파일 출력·블록 수·조립 해 재삽입 헤더를 포함한다(3–7). lis::cuda::acc_nugrid 이름공간을 연다(9–14). 이 파일 전체에는 조건부 전처리 분기가 없다. |
| 16–31 | 호스트 함수 선언은 `__host__ AssembledSolution project_assem_sol` (16)이다. mesh_dim·lev 상수 참조, d_sig_details 포인터 참조, ScaleCoefficients 상수 참조, d_buf_assem_sol·d_assem_sol·d_plot_assem_sol 값 인수와 두 MortonCode 포인터를 받는다(17–27). 함수 본문과 기본 인수는 없다. 빈 줄과 이름공간 닫기를 포함한다(28–31). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
