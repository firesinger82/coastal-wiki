---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/cuda_solver.cuh
lines: 141
sha256: a032c08ce125f9702944542ea0c59cf06522ebbab977d58f411c81daf8da475a
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# cuda_solver.cuh — 판독 구간 기록

구간은 1행부터 141행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–28 | `#pragma once` (1), `#define CUDA_BLOCK_SIZE_X 16` (2), `#define CUDA_BLOCK_SIZE_Y 16` (3), `#define CUDA_BLOCK_SIZE 256` (4)를 둔다. 전처리 조건 분기는 없다. 기하·경계·통계·매개변수·표본 헤더를 포함하고 lis::cuda를 연다(6–15). `extern __constant__ Geometry geometry;` (17), `extern __constant__ Geometry rain_geometry;` (18), `extern __constant__ int pitch;` (19), `extern __constant__ PhysicalParams physical_params;` (20), `extern __constant__ SolverParams solver_params;` (21), `extern __constant__ BoundaryConditions boundaries;` (22), `extern __constant__ SamplePoints sample_points;` (23), `extern __managed__ NUMERIC_TYPE dt;` (24), `extern __managed__ int sample_buf_idx;` (25), block_size(27)를 선언한다. |
| 29–48 | 질량 통계용 `__device__` (29·39) 함수 update_mass_stats_x/y를 선언한다. 두 함수의 시간 단계 가중치(time stage fraction) 기본값은 각각 `NUMERIC_TYPE time_stage_fraction = C(1.0)` (36·46)이다. |
| 49–79 | `template<typename F>` (49)의 Solver 추상 클래스(abstract class)는 가상 셀(ghost cell), 균일 강우(uniform rain), 최대장, 얕은 수심 기울기, 범람원(floodplain) 유량, 흐름 상태·시간 간격 갱신과 장치 상태 참조의 순수 가상 함수를 선언한다(53–75). 소멸자(destructor)는 `virtual ~Solver() {};` (77)이다. |
| 80–108 | DynamicTimestep<F>는 dt 참조·기하·max_dt·adaptive_ts·Solver 참조를 받는 생성자, update_dt, 소멸자를 선언한다(84–95). private에는 adaptive·dt·max_dt·const solver 참조·dt_field·const elements·d_temp·bytes가 있다(97–106). 이 선언에는 멤버 초기값이 없다. |
| 109–141 | DynamicTimestepACC<F>는 같은 인수의 생성자, update_dt_ACC와 소멸자를 선언한다(113–124). private 멤버는 앞 클래스와 같은 이름·형식이다(126–135). 이름공간을 닫고 `#include "cuda_solver.templates.cu"` (141)로 구현을 포함한다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 2–4: 스레드 블록의 x·y 크기는 16·16이고 CUDA_BLOCK_SIZE는 별도로 256으로 정의되어 있다.
