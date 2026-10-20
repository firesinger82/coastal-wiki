---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/acc_nugrid/get_compaction_flags.cu
lines: 37
sha256: 414c41821b41874ae75019fd5bfdb785bcb14b057919afbbe670f965d3df24c3
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# get_compaction_flags.cu — 판독 구간 기록

구간은 1행부터 37행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–15 | 헤더 포함(1), CUDA 커널(kernel) `__global__ void lis::cuda::acc_nugrid::get_compaction_flags` (3) 정의와 인수(4–9). 전처리 조건 분기는 없다. `index_1D idx = blockIdx.x * blockDim.x + threadIdx.x;` (10), `if (idx >= num_finest_elems) return;` (12)로 스레드 인덱스와 범위를 정한다. 현재 활성 인덱스를 읽는다(14). |
| 16–26 | 시작 시 3행 `get_compaction_flags` 커널 안. `if ( idx < (num_finest_elems - 1) )` (16)이면 오른쪽 활성 인덱스를 읽고(18), `d_compaction_flags.north_east[idx] = !(current == right);` (20)로 연속된 같은 인덱스 묶음의 마지막 위치에 북동 플래그를 둔다. `else` (22)는 배열 마지막 요소의 `north_east[idx]`를 1로 설정한다(24). |
| 27–37 | 시작 시 3행 커널 안. `if (idx > 0)` (27)이면 왼쪽 활성 인덱스를 읽고(29), `d_compaction_flags.south_west[idx] = !(current == left);` (31)로 연속된 같은 인덱스 묶음의 첫 위치에 남서 플래그를 둔다. `else` (33)는 배열 첫 요소의 `south_west[idx]`를 1로 설정한다(35). 조건·커널 종료(36–37). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
