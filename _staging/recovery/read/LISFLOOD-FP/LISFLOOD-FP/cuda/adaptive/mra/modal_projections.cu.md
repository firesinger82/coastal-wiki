---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/mra/modal_projections.cu
lines: 88
sha256: aa8ca8228ad7b9974ee5b8fbab409076d686b77cc68887a40dec4e234701fabf
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# modal_projections.cu — 판독 구간 기록

구간은 1행부터 88행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–27 | modal_projections.cuh 포함과 빈 줄(1–2). 머리말 주석은 정사각형 공유 메모리(shared memory) 블록을 사용한 모드 투영(modal projection)을 설명한다(3–26). 4행 4열 블록 배치 예를 든다(9–19). 1차원 배열로 정사각형을 표현하며 스레드(thread) 수 예로 64, 256, 1024를 적는다(20–21). SHARED_MEMORY_BLOCK_DIM은 스레드 수의 제곱근이라는 주석과 mesh_dim / SHARED_MEMORY_BLOCK_DIM 및 shared_memory_blocks_per_side 설명이 이어진다(22–25). 이 구간의 수치는 주석에 적힌 예이며 실제 매크로 정의문은 아니다. 빈 줄도 포함한다(27). 이 파일에는 전처리 조건 분기가 없다. |
| 28–50 | `__global__` (28)인 modal_projections는 NodalValues, AssembledSolution, SolverParams, mesh_dim, interface_dim을 값으로 받는다(29–37). t_idx에 threadIdx.x를 복사한다(38). `HierarchyIndex idx   = blockDim.x * blockIdx.x + t_idx;` (39), `if ( idx >= d_assem_sol.length ) return;` (41)로 유효 전역 인덱스만 처리한다. `Coordinate x = idx % mesh_dim;` (43), `Coordinate y = idx / mesh_dim;` (44)로 셀 좌표를 구한다. 네 절점 인덱스 원문은 `HierarchyIndex SW =  y      * interface_dim + x;` (46), `HierarchyIndex SE =  y      * interface_dim + x + 1;` (47), `HierarchyIndex NW = (y + 1) * interface_dim + x;` (48), `HierarchyIndex NE = (y + 1) * interface_dim + x + 1;` (49)이다. 빈 줄도 포함한다. |
| 51–75 | 시작 시 29–37행 modal_projections 커널(kernel) 안. h, qx, qy, z의 SW, SE, NW, NE 절점값을 지역 변수에 복사한다(51–69). 네 점 평균 모드의 원문은 `d_assem_sol.h0[idx]  = C(0.25) * (h_NW  + h_NE  + h_SE  + h_SW );` (71), `d_assem_sol.qx0[idx] = C(0.25) * (qx_NW + qx_NE + qx_SE + qx_SW);` (72), `d_assem_sol.qy0[idx] = C(0.25) * (qy_NW + qy_NE + qy_SE + qy_SW);` (73), `d_assem_sol.z0[idx]  = C(0.25) * (z_NW  + z_NE  + z_SE  + z_SW );` (74)이다. 이 대입들은 solver_type 분기 밖에 있다. 빈 줄도 포함한다(55·60·65·70·75). |
| 76–88 | 시작 시 29–37행 modal_projections 커널 안. `if (solver_params.solver_type == MWDG2)` (76)일 때만 1x와 1y 모드를 계산한다. x 방향 식 원문은 `d_assem_sol.h1x[idx]  = (h_NE  - h_NW  + h_SE  - h_SW ) / ( C(4.0) * sqrt( C(3.0) ) );` (78), `d_assem_sol.qx1x[idx] = (qx_NE - qx_NW + qx_SE - qx_SW) / ( C(4.0) * sqrt( C(3.0) ) );` (79), `d_assem_sol.qy1x[idx] = (qy_NE - qy_NW + qy_SE - qy_SW) / ( C(4.0) * sqrt( C(3.0) ) );` (80), `d_assem_sol.z1x[idx]  = (z_NE  - z_NW  + z_SE  - z_SW ) / ( C(4.0) * sqrt( C(3.0) ) );` (81)이다. y 방향 식 원문은 `d_assem_sol.h1y[idx]  = (h_NE  - h_SE  + h_NW  - h_SW ) / ( C(4.0) * sqrt( C(3.0) ) );` (83), `d_assem_sol.qx1y[idx] = (qx_NE - qx_SE + qx_NW - qx_SW) / ( C(4.0) * sqrt( C(3.0) ) );` (84), `d_assem_sol.qy1y[idx] = (qy_NE - qy_SE + qy_NW - qy_SW) / ( C(4.0) * sqrt( C(3.0) ) );` (85), `d_assem_sol.z1y[idx]  = (z_NE  - z_SE  + z_NW  - z_SW ) / ( C(4.0) * sqrt( C(3.0) ) );` (86)이다. 빈 줄, 분기 끝과 커널 끝도 포함한다(82·87–88). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 3–26·28–88: 머리말은 정사각형 공유 메모리 블록 사용을 설명한다. 커널 본문에는 공유 메모리 선언과 스레드 동기화 호출이 없다.
