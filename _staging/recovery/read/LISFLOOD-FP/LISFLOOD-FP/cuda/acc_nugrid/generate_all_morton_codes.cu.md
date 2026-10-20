---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/acc_nugrid/generate_all_morton_codes.cu
lines: 20
sha256: 83960e049eb2cb80ea50b297c16b9ea068ffd154aadd8446dfc78a5714e97fbf
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# generate_all_morton_codes.cu — 판독 구간 기록

구간은 1행부터 20행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–13 | 헤더 포함(1), CUDA 커널(kernel) `__global__ void lis::cuda::acc_nugrid::generate_all_morton_codes` (3) 정의와 모턴 코드(Morton code) 포인터·순서 포인터·격자 폭 인수(4–9). 전처리 조건 분기는 없다. `index_1D idx = blockDim.x * blockIdx.x + threadIdx.x;` (10), `if ( idx >= (mesh_dim * mesh_dim) ) return;` (12)로 스레드 인덱스와 정사각 격자의 범위를 정한다. |
| 14–20 | 시작 시 3행 커널 안. `int x = idx % mesh_dim;` (14), `int y = idx / mesh_dim;` (15)로 행 우선(row-major) 인덱스에서 좌표를 얻는다. 원래 인덱스를 `d_indices[idx]`에 복사한다(17). `d_morton_codes[idx] = generate_morton_code(x, y);` (19)로 각 격자 셀의 모턴 코드를 저장한다. 커널 종료(20). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
