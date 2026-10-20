---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/zorder/copy_finest_coefficients.cu
lines: 35
sha256: 31f2964bb710ba2b2771f3892251879c4da71eefae205c167dc1ec7907604afb
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# copy_finest_coefficients.cu — 판독 구간 기록

구간은 1행부터 35행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–11 | `copy_finest_coefficients.cuh`를 포함한다(1). 빈 줄(2) 뒤 `__global__` (3) 커널(kernel) `copy_finest_coefficients`를 정의한다(4–11). 인수는 `AssembledSolution d_assem_sol`, `ScaleCoefficients d_scale_coeffs`, `SolverParams solver_params`, `HierarchyIndex finest_lvl_idx`이다(6–9). 전처리 조건 분기는 없다. |
| 12–22 | 시작 시 4행 커널 본문 안이다. 전역 스레드 인덱스(global thread index) 식은 `HierarchyIndex idx = blockDim.x * blockIdx.x + threadIdx.x;` (12)이다. 빈 줄(13) 뒤 `if ( idx >= d_assem_sol.length ) return;` (14)로 길이 밖의 스레드를 종료한다. 빈 줄(15) 뒤 계층 인덱스(hierarchy index)는 `HierarchyIndex h_idx = finest_lvl_idx + idx;` (16)이다. 빈 줄(17) 뒤 가장 세밀한 수준(finest level)의 상수 계수는 `d_scale_coeffs.eta0[h_idx] = d_assem_sol.h0[idx] + d_assem_sol.z0[idx];` (18)로 계산한다. `qx0`, `qy0`, `z0`는 원본의 같은 이름 필드를 `idx`에서 읽어 `h_idx`에 복사한다(19–21). 마지막은 빈 줄(22)이다. |
| 23–35 | 시작 시 4행 커널 본문 안이며 14행 조기 반환을 통과했다. `if (solver_params.solver_type == MWDG2)` (23)가 참인 블록(24)에서 `d_scale_coeffs.eta1x[h_idx] = d_assem_sol.h1x[idx] + d_assem_sol.z1x[idx];` (25)로 x 방향 1차 계수를 계산한다. `qx1x`, `qy1x`, `z1x`는 대응 필드를 복사한다(26–28). 빈 줄(29) 뒤 `d_scale_coeffs.eta1y[h_idx] = d_assem_sol.h1y[idx] + d_assem_sol.z1y[idx];` (30)로 y 방향 1차 계수를 계산한다. `qx1y`, `qy1y`, `z1y`는 대응 필드를 복사한다(31–33). 조건·커널을 닫는다(34–35). 이 조건의 `else`는 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 14·16–33: 조기 반환 조건은 `d_assem_sol.length`만 사용한다. `finest_lvl_idx + idx`로 얻은 대상 인덱스가 `d_scale_coeffs`의 저장 범위 안인지 검사하는 별도 조건은 이 커널에 없다.
