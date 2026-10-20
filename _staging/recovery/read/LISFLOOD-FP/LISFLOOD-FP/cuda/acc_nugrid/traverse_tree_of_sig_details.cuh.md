---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/acc_nugrid/traverse_tree_of_sig_details.cuh
lines: 40
sha256: 3b37a6dda4bbf36cfeda251e1d2eb0158cef753a988e3cd79f470368f9b98b65
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# traverse_tree_of_sig_details.cuh — 판독 구간 기록

구간은 1행부터 40행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–19 | `#pragma once` (1). CUDA 실행·커널 실행 매개변수·CUB block_store·블록 매크로·index_1D·조립 해(assembled solution)·MortonCode·get_lvl_idx·스케일 계수(scale coefficients)를 포함한다(3–11). lis::cuda::acc_nugrid 이름공간(namespace)을 연다(13–18). 전처리 조건 분기는 없다. |
| 20–28 | `__global__ void traverse_tree_of_sig_details` (20)는 CUDA 커널(kernel) 선언이다. bool* d_sig_details, ScaleCoefficients d_scale_coeffs, AssembledSolution d_buf_assem_sol, int num_threads·lev를 받는다(21–27). 기본 인수와 실행 본문은 없다. 빈 줄(28). |
| 29–40 | `__global__ void traverse_tree_of_sig_details_with_n` (29)는 n을 포함하는 이름의 CUDA 커널 선언이다. 인수 형식과 이름은 앞 선언과 같다(30–36). 기본 인수와 본문은 없다. 빈 줄과 세 이름공간 닫기(37–40). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
