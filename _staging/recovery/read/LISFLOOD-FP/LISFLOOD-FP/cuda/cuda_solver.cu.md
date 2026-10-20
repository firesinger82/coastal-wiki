---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/cuda_solver.cu
lines: 80
sha256: 292ece0dcca5038e005777ea22daf52e924cb12e4bb810088f374f9e0644abeb
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# cuda_solver.cu — 판독 구간 기록

구간은 1행부터 80행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–15 | solver·atomic 헤더를 포함한다(1–2). 전처리 조건 분기는 없다. 상수 메모리(constant memory) 정의는 `__constant__ Geometry lis::cuda::geometry;` (4), `__constant__ Geometry lis::cuda::rain_geometry;` (5), `__constant__ int lis::cuda::pitch;` (6), `__constant__ lis::PhysicalParams lis::cuda::physical_params;` (7), `__constant__ lis::SolverParams lis::cuda::solver_params;` (8), `__constant__ lis::cuda::BoundaryConditions lis::cuda::boundaries;` (9), `__constant__ lis::SamplePoints lis::cuda::sample_points;` (10)이다. 관리 메모리(managed memory)는 `__managed__ NUMERIC_TYPE lis::cuda::dt;` (11), `__managed__ int lis::cuda::sample_buf_idx = 0;` (12)이다. 스레드 블록(thread block)은 `const dim3 lis::cuda::block_size(CUDA_BLOCK_SIZE_X, CUDA_BLOCK_SIZE_Y);` (14)로 만든다. 이 파일에는 블록 크기 매크로 정의가 없다. |
| 16–48 | `__device__ void lis::cuda::update_mass_stats_x` (16)는 x 경계 질량 통계(mass statistics)를 누적한다. `if (i == 0)` (25) 안 `if (FH > C(0.0))` (27)은 `atomicAdd(&(stats->in), time_stage_fraction*FH*cuda::geometry.dy);` (29), `else` (31)는 `atomicAdd(&(stats->out), -time_stage_fraction*FH*cuda::geometry.dy);` (33)이다. `else if (i == cuda::geometry.xsz)` (36) 안 `if (FH < C(0.0))` (38)은 `atomicAdd(&(stats->in), -time_stage_fraction*FH*cuda::geometry.dy);` (40), `else` (42)는 `atomicAdd(&(stats->out), time_stage_fraction*FH*cuda::geometry.dy);` (44)이다. 원자적 덧셈(atomic addition)을 사용한다. |
| 49–80 | `__device__ void lis::cuda::update_mass_stats_y` (49)는 y 경계 통계를 누적한다. `if (j == 0)` (58) 안 `if (FH < C(0.0))` (60)은 `atomicAdd(&(stats->in), -time_stage_fraction*FH*cuda::geometry.dx);` (62), `else` (64)는 `atomicAdd(&(stats->out), time_stage_fraction*FH*cuda::geometry.dx);` (66)이다. `else if (j == cuda::geometry.ysz)` (69) 안 `if (FH > C(0.0))` (71)은 `atomicAdd(&(stats->in), time_stage_fraction*FH*cuda::geometry.dx);` (73), `else` (75)는 `atomicAdd(&(stats->out), -time_stage_fraction*FH*cuda::geometry.dx);` (77)이다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 16–47·49–80: update_mass_stats_x는 인수 j를 본문에서 쓰지 않는다. update_mass_stats_y는 인수 i를 본문에서 쓰지 않는다.
