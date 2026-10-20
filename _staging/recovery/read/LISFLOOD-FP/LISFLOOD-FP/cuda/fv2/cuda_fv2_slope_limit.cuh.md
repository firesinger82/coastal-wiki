---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/fv2/cuda_fv2_slope_limit.cuh
lines: 147
sha256: 6ac97c48ab7c8ffe36924e35c05095b1b092ff90f9fc3b17104a997ca7f878bd
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# cuda_fv2_slope_limit.cuh — 판독 구간 기록

구간은 1행부터 147행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–21 | `#pragma once` (1), LISFLOOD·FV2 Flow·CUDA geometry 헤더 포함(2–4), lis::cuda::fv2 이름 공간(namespace)(6–11). Stencil은 backward/local/forward 각각의 const·slope 여섯 수치 필드를 선언한다(13–20). 조건부 전처리 지시는 없다. |
| 22–52 | 시작 시 6·8·10행 이름 공간·13행 Stencil 안. limit는 `__device__` (22)이며 mesh_delta·stencil_minH를 받는다(23–27). minH_x·minH_y는 `__device__` (29·37) static 함수이고 Flow·i·j를 받는다(30–43). private 평가 함수는 `__device__ NUMERIC_TYPE backward_neg();` (46), `__device__ NUMERIC_TYPE local_pos();` (47), `__device__ NUMERIC_TYPE local_neg();` (48), `__device__ NUMERIC_TYPE forward_pos();` (49). |
| 53–86 | Slopes는 `NUMERIC_TYPE* __restrict__`로 ETA1x·ETA1y·HU1x·HU1y·HV1x·HV1y를 선언한다(53–60). x 스텐실(stencil) 함수 ETA/HU/HV에는 각각 `__device__` (62·71·79)가 있다. ETA는 DEM·H·i·j를, HU/HV는 해당 배열·i·j를 받는다(63–85). |
| 87–123 | 시작 시 6·8·10행 이름 공간·53행 Slopes 안. y 스텐실 함수의 `__device__` (87·96·104) 선언과 인수(88–110). static allocate_device는 Slopes·Geometry 참조를 받고 free_device는 Slopes 참조를 받는다(112–121). 구조체 종료(122). |
| 124–147 | MaxH 클래스(124–143)는 Geometry 참조를 받는 생성자·Flow const 참조를 받는 update·소멸자를 공개한다(127–137). private에는 const int elements·void* temp·size_t bytes가 있다(139–142). 이름 공간 종료(145–147). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
