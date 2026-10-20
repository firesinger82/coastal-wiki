---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/mra/init_eta_temp.cu
lines: 15
sha256: 9f87cfc3addb81abf4bc26daf6e8ae7be0574275a48ac3fb73b9b7c270c666fd
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# init_eta_temp.cu — 판독 구간 기록

구간은 1행부터 15행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | init_eta_temp.cuh 포함과 빈 줄(1–2). `__global__` (3)인 CUDA 커널(kernel) init_eta_temp는 AssembledSolution 값과 real 포인터 d_eta_temp를 받는다(4–9). 이 파일에는 전처리 조건 분기가 없다. |
| 10–15 | 시작 시 4–9행 init_eta_temp 커널 안. `HierarchyIndex idx = blockIdx.x * blockDim.x + threadIdx.x;` (10)로 전역 스레드(thread) 인덱스를 계산한다. `if (idx >= d_assem_sol.length) return;` (12)로 범위를 벗어난 스레드를 종료한다. `d_eta_temp[idx] = d_assem_sol.h0[idx] + d_assem_sol.z0[idx];` (14)로 h0와 z0의 합을 저장한다. 빈 줄과 커널 끝도 포함한다(11·13·15). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
