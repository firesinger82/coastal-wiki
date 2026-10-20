---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/neighbours/load_soln_and_nghbr_coeffs.cu
lines: 104
sha256: a03b7e90d2cd0339093f1c2adc397da055cf8e0ab9bda5f2d18255a2161c3197
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# load_soln_and_nghbr_coeffs.cu — 판독 구간 기록

구간은 1행부터 104행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–26 | 헤더 포함(1), `__global__` (3) 지정의 커널(kernel) load_soln_and_nghbr_coeffs 입구·인수 선언(4–11). 이웃(neighbour), 스케일 계수(scale coefficient), 조립 해(assembled solution), SolverParams를 받는다(6–9). 조건부 전처리 분기는 없다. `HierarchyIndex idx = blockIdx.x * blockDim.x + threadIdx.x;` (12) 뒤 `if (idx >= d_assem_sol.length) return;` (14)로 길이를 검사한다. 내부와 네 방향의 활성 계층 인덱스(index)를 읽고(16–20), `north = (north == -1) ? 0 : north;`<br>`east  = (east  == -1) ? 0 : east;`<br>`south = (south == -1) ? 0 : south;`<br>`west  = (west  == -1) ? 0 : west;` (22–25)로 이웃 -1 인덱스를 지역 변수에서 0으로 치환한다. |
| 27–51 | 시작 시 3–11행 커널 안. `d_assem_sol.h0[idx]  = d_scale_coeffs.eta0[soln] - d_scale_coeffs.z0[soln];` (27)로 내부 평균 깊이를 계산한다. 내부 qx0·qy0·z0는 대응 스케일 계수에서 복사한다(28–30). `d_neighbours.north.h0[idx]  = d_scale_coeffs.eta0[north] - d_scale_coeffs.z0[north];` (32), `d_neighbours.east.h0[idx]  = d_scale_coeffs.eta0[east] - d_scale_coeffs.z0[east];` (37), `d_neighbours.south.h0[idx]  = d_scale_coeffs.eta0[south] - d_scale_coeffs.z0[south];` (42), `d_neighbours.west.h0[idx]  = d_scale_coeffs.eta0[west] - d_scale_coeffs.z0[west];` (47)로 북·동·남·서 평균 깊이를 계산한다. 각 이웃의 qx0·qy0·z0도 대응 계층 위치에서 복사한다(33–35·38–40·43–45·48–50). |
| 52–78 | 시작 시 3–11행 커널 안. `if (solver_params.solver_type == MWDG2)` (52)이면 `d_assem_sol.h1x[idx]  = d_scale_coeffs.eta1x[soln] - d_scale_coeffs.z1x[soln];` (54)로 내부 1x 깊이 계수를 계산한다. 내부 qx1x·qy1x·z1x를 복사한다(55–57). `d_neighbours.north.h1x[idx]  = d_scale_coeffs.eta1x[north] - d_scale_coeffs.z1x[north];` (59), `d_neighbours.east.h1x[idx]  = d_scale_coeffs.eta1x[east] - d_scale_coeffs.z1x[east];` (64), `d_neighbours.south.h1x[idx]  = d_scale_coeffs.eta1x[south] - d_scale_coeffs.z1x[south];` (69), `d_neighbours.west.h1x[idx]  = d_scale_coeffs.eta1x[west] - d_scale_coeffs.z1x[west];` (74)로 네 이웃의 1x 깊이 계수를 계산한다. 각 이웃의 qx1x·qy1x·z1x는 스케일 계수에서 복사한다(60–62·65–67·70–72·75–77). |
| 79–104 | 시작 시 3–11행 커널·52행 MWDG2 참 분기 안. `d_assem_sol.h1y[idx]  = d_scale_coeffs.eta1y[soln] - d_scale_coeffs.z1y[soln];` (79)로 내부 1y 깊이 계수를 계산한다. 내부 qx1y·qy1y·z1y를 복사한다(80–82). `d_neighbours.north.h1y[idx]  = d_scale_coeffs.eta1y[north] - d_scale_coeffs.z1y[north];` (84), `d_neighbours.east.h1y[idx]  = d_scale_coeffs.eta1y[east] - d_scale_coeffs.z1y[east];` (89), `d_neighbours.south.h1y[idx]  = d_scale_coeffs.eta1y[south] - d_scale_coeffs.z1y[south];` (94), `d_neighbours.west.h1y[idx]  = d_scale_coeffs.eta1y[west] - d_scale_coeffs.z1y[west];` (99)로 네 이웃의 1y 깊이 계수를 계산한다. 각 이웃의 qx1y·qy1y·z1y는 대응 계층 위치에서 복사한다(85–87·90–92·95–97·100–102). 분기·커널 종료(103–104). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 22–25·32–50: 이웃 인덱스 -1은 지역 변수에서 0으로 바꾸며 d_neighbours의 act_idcs 자체는 수정하지 않는다. 해당 이웃 값도 스케일 계수 0번 위치에서 읽는다.
- 27·32·37·42·47: 평균 깊이는 eta0 - z0를 그대로 대입한다. 이 식들에는 max(C(0.0), ...) 같은 음수 제한이 없다.
