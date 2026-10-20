---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/dg2/cuda_dg2_slope_limit.cu
lines: 306
sha256: 15ab8df0127478ae0f8b7b6304880f98b0c11e9fc40bbc1532a167cfa7c2eb0e
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# cuda_dg2_slope_limit.cu — 판독 구간 기록

구간은 1행부터 306행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–14 | DG2 기울기 제한(slope limiting)·solver·공통 solver/util·helper_cuda·CUB 헤더를 포함한다(1–6). 전처리 조건 분기는 없다. `__device__` (8) Stencil::limit는 mesh_delta와 stencil_minH를 받는다(9–14). |
| 15–50 | 시작 시 9행 Stencil::limit 안이다. `if (stencil_minH <= C(0.30)*cuda::dg2::maxH) return local_slope;` (15)로 얕은 영역의 기울기를 그대로 반환한다. backward_neg·local_pos·local_neg·forward_pos를 호출한다(17–20). `NUMERIC_TYPE b_jump = FABS(l_pos - b_neg);` (22), `NUMERIC_TYPE f_jump = FABS(l_neg - f_pos);` (23), `NUMERIC_TYPE norm = FMAX(FABS(local_const-backward_const), FABS(forward_const-local_const));` (25)이다. DS_backward·DS_forward는 C(0.0)으로 초기화한다(27–28). `if (FABS(norm) > C(1e-6))` (30) 안에서 `DS_backward = b_jump/(C(0.5)*mesh_delta*norm);` (32), `DS_forward = f_jump/(C(0.5)*mesh_delta*norm);` (33)를 계산한다. `if (FMAX(DS_backward, DS_forward) >= cuda::solver_params.KrivodonovaThresh)` (36)이면 `return minmod` (38), `(` (39), `local_slope,` (40), `(local_const-backward_const)/SQRT(C(3.0)),` (41), `(forward_const-local_const)/SQRT(C(3.0))` (42), `);` (43)를 반환한다. `else` (45)는 local_slope를 반환한다(47). |
| 51–69 | `__device__` (51) Stencil::minmod의 `if (a*b > C(0.0) && a*c > C(0.0))` (59) 안에서 `NUMERIC_TYPE sign_a = (a > C(0.0)) - (a < C(0.0));` (61), `return sign_a * FMIN(FABS(a), FMIN(FABS(b), FABS(c)));` (62)이다. `else` (64)는 `return C(0.0);` (66)이다. |
| 70–91 | `__device__` (70) minH_x는 i-1·i·i+1의 H·H1x를 읽는다(78–83). `NUMERIC_TYPE b_min = FMIN(backward0 - backward1x, backward0 + backward1x);` (85), `NUMERIC_TYPE l_min = FMIN(local0 - local1x, local0 + local1x);` (86), `NUMERIC_TYPE f_min = FMIN(forward0 - forward1x, forward0 + forward1x);` (87), `return FMIN(b_min, FMIN(l_min, f_min));` (89)로 스텐실(stencil) 최소 수심을 반환한다. |
| 92–113 | `__device__` (92) minH_y는 j+1·j·j-1의 H·H1y를 읽는다(100–105). `NUMERIC_TYPE b_min = FMIN(backward0 - backward1y, backward0 + backward1y);` (107), `NUMERIC_TYPE l_min = FMIN(local0 - local1y, local0 + local1y);` (108), `NUMERIC_TYPE f_min = FMIN(forward0 - forward1y, forward0 + forward1y);` (109), `return FMIN(b_min, FMIN(l_min, f_min));` (111)이다. |
| 114–133 | `__device__ NUMERIC_TYPE lis::cuda::dg2::Stencil::backward_neg()` (114)는 `return backward_const + SQRT(C(3.0))*backward_slope;` (116), `__device__ NUMERIC_TYPE lis::cuda::dg2::Stencil::local_pos()` (119)는 `return local_const - SQRT(C(3.0))*local_slope;` (121), `__device__ NUMERIC_TYPE lis::cuda::dg2::Stencil::local_neg()` (124)는 `return local_const + SQRT(C(3.0))*local_slope;` (126), `__device__ NUMERIC_TYPE lis::cuda::dg2::Stencil::forward_pos()` (129)는 `return forward_const - SQRT(C(3.0))*forward_slope;` (131)이다. |
| 134–153 | `__device__` (134) Slopes::ETA_stencil_x는 수위(elevation) 스텐실을 반환한다. 반환 목록은 `return` (143), `{` (144), `DEM[j*cuda::pitch + i-1] + H[j*cuda::pitch + i-1],` (145), `ETA1x[j*cuda::pitch + i-1],` (146), `DEM[j*cuda::pitch + i] + H[j*cuda::pitch + i],` (147), `ETA1x[j*cuda::pitch + i],` (148), `DEM[j*cuda::pitch + i+1] + H[j*cuda::pitch + i+1],` (149), `ETA1x[j*cuda::pitch + i+1]` (150), `};` (151)이다. |
| 154–191 | `__device__` (154·173) HU_stencil_x·HV_stencil_x는 i-1·i·i+1의 평균 유량과 해당 1x 기울기를 뒤쪽·현재·앞쪽 순서로 각각 묶어 반환한다(162–170·181–189). |
| 192–211 | `__device__` (192) ETA_stencil_y의 반환 목록은 `return` (201), `{` (202), `DEM[(j+1)*cuda::pitch + i] + H[(j+1)*cuda::pitch + i],` (203), `ETA1y[(j+1)*cuda::pitch + i],` (204), `DEM[j*cuda::pitch + i] + H[j*cuda::pitch + i],` (205), `ETA1y[j*cuda::pitch + i],` (206), `DEM[(j-1)*cuda::pitch + i] + H[(j-1)*cuda::pitch + i],` (207), `ETA1y[(j-1)*cuda::pitch + i]` (208), `};` (209)이다. |
| 212–249 | `__device__` (212·231) HU_stencil_y·HV_stencil_y는 j+1·j·j-1의 평균 유량과 해당 1y 기울기를 뒤쪽·현재·앞쪽 순서로 각각 반환한다(220–228·239–247). |
| 250–276 | Slopes::allocate_device는 ETA1x·ETA1y·HU1x·HU1y·HV1x·HV1y에 cuda::GhostRaster::allocate_device를 호출한다(256–261). Slopes::free_device는 같은 6개 배열을 cuda::free_device로 해제한다(269–274). |
| 277–306 | MaxH 생성자는 `elements(lis::GhostRaster::elements(geometry))` (282)를 저장한다. nullptr 작업 포인터로 cub::DeviceReduce::Max를 호출해 bytes를 조회하고 malloc_device로 할당한다(284–291). update는 `checkCudaErrors(cub::DeviceReduce::Max(temp, bytes, flow.H,` (299), `&(cuda::dg2::maxH), elements));` (300)로 최대 수심을 갱신한다. 소멸자는 free_device(temp)를 호출한다(303–306). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 15·30: 제한기 조기 반환 계수 0.30과 norm 비교 임계값 1e-6은 이 함수에 상수로 적혀 있다.
- 30–33: DS 계산의 분모는 mesh_delta를 포함한다. 이 함수에는 mesh_delta가 0인지 검사하는 조건이 없다.
