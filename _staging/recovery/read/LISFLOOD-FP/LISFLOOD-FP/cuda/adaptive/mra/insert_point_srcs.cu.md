---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/mra/insert_point_srcs.cu
lines: 28
sha256: f6ad1b3f34a86df4b33f1cd45aec6595891519bed17342168b1d6bfbd0ca54e9
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# insert_point_srcs.cu — 판독 구간 기록

구간은 1행부터 28행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–11 | insert_point_srcs.cuh 포함과 빈 줄(1–2). `__global__` (3)인 CUDA 커널(kernel) insert_point_srcs는 AssembledSolution, PointSources, real dt, real dx_finest를 값으로 받는다(4–11). 이 파일에는 전처리 조건 분기가 없다. |
| 12–19 | 시작 시 4–11행 insert_point_srcs 커널 안. `HierarchyIndex idx = blockIdx.x * blockDim.x + threadIdx.x;` (12)로 전역 스레드(thread) 인덱스를 계산한다. `if (idx >= point_sources.num_srcs) return;` (14)로 점 공급원(point source) 수 밖의 스레드를 종료한다. h_idx에 d_codes[idx]를, src_type에 d_src_types[idx]를 복사한다(16·18). 빈 줄도 포함한다(13·15·17·19). |
| 20–28 | 시작 시 4–11행 insert_point_srcs 커널 안. `if (src_type == HFIX \|\| src_type == HVAR)` (20)일 때 `d_assem_sol.h0[h_idx] = point_sources.d_srcs[idx] - d_assem_sol.z0[idx];` (22)로 수심을 대입한다. 병렬 `else if (src_type == QFIX \|\| src_type == QVAR)` (24)는 `d_assem_sol.h0[h_idx] += point_sources.q_src(dt, dx_finest, idx);` (26)로 q_src 호출 결과를 더한다. 각 분기와 커널 닫기를 포함한다(21·23·25·27–28). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 16·22: h_idx는 point_sources.d_codes[idx]에서 얻는다. 22행 수심 대입은 왼쪽에 h0[h_idx]를 사용하고 오른쪽 지형에는 z0[idx]를 사용한다.
