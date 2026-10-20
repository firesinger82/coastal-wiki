---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/acc_nugrid/write_soln_vtk.cuh
lines: 54
sha256: 3323464c33c367a54692999f5e6dc60f8b9622eb095d99a6f5b2e74761324c38
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# write_soln_vtk.cuh — 판독 구간 기록

구간은 1행부터 54행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–16 | `#pragma once` (1). stdio.h·stdlib.h·AssembledSolution.h·cuda_utils.cuh·compact.cuh·get_lvl_idx.cuh를 포함한다(3–8). lis::cuda::acc_nugrid 이름공간을 연다(10–15). 전처리 조건 분기는 없다. |
| 17–29 | 시작 시 10–15행 이름공간 안. Points 구조체(struct)는 NUMERIC_TYPE의 ll_x·ll_y·ul_x·ul_y·lr_x·lr_y·ur_x·ur_y를 저장한다(17–28). 필드 초기값 대입은 없다. |
| 30–40 | 시작 시 10–15행 이름공간 안. `__host__ void write_soln_vtk` (30)를 선언한다. respath·d_assem_sol·pars·lev·depth_thresh·call_gzip·precision을 받는다(32–38). 기본 인수와 실행 본문은 없다. |
| 41–54 | 시작 시 10–15행 이름공간 안. `__host__ void write_soln_vtk_with_n` (41)를 같은 인수 목록으로 선언한다(43–49). 기본 인수와 실행 본문은 없다. 선언·이름공간을 닫는다(50–54). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
