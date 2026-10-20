---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/zorder/generate_all_morton_codes.cu
lines: 21
sha256: 248d4b19d82919b15efec9fa421b959525677bdd2cd8e9a43a010b288808d2d3
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# generate_all_morton_codes.cu — 판독 구간 기록

구간은 1행부터 21행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–10 | `generate_all_morton_codes.cuh`를 포함한다(1). 빈 줄(2) 뒤 `__global__` (3) 커널(kernel) `generate_all_morton_codes`를 정의한다(4–10). 인수는 모턴 코드(Morton code) 출력 배열 `MortonCode* d_morton_codes`, 인덱스 배열 `int* d_indices`, 격자 한 변 크기 `int mesh_dim`이다(6–8). 전처리 조건 분기는 없다. |
| 11–21 | 시작 시 4행 커널 본문 안이다. 스레드 인덱스(thread index)는 `HierarchyIndex idx = blockDim.x * blockIdx.x + threadIdx.x;` (11)이다. 빈 줄(12) 뒤 `if ( idx >= (mesh_dim * mesh_dim) ) return;` (13)로 제곱 격자 범위 밖 스레드를 종료한다. 빈 줄(14) 뒤 `Coordinate x = idx % mesh_dim;` (15), `Coordinate y = idx / mesh_dim;` (16)로 좌표를 구한다. 빈 줄(17) 뒤 `d_indices[idx] = idx;` (18)로 원래 인덱스를 저장한다. 빈 줄(19) 뒤 `d_morton_codes[idx] = generate_morton_code(x, y);` (20)로 좌표에 대한 모턴 코드를 저장한다. 커널 종료(21)이다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 8·13–16: `mesh_dim`은 `int` 인수이며 범위 검사는 `mesh_dim * mesh_dim`과의 비교이다. 이 커널에는 `mesh_dim`의 부호 또는 곱셈 결과의 정수 범위를 확인하는 별도 조건이 없다.
