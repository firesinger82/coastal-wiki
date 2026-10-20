---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/dg2/cuda_dg2_slope_limit.cuh
lines: 154
sha256: 5ad29a369115b08e75631cbf02404212c1525c10445f5e79e2dbb78a3b76c5d9
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# cuda_dg2_slope_limit.cuh — 판독 구간 기록

구간은 1행부터 154행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–21 | `#pragma once` (1)와 lisflood·DG2 flow·기하 헤더를 포함한다(2–4). 전처리 조건 분기는 없다. lis::cuda::dg2 이름공간(namespace)에서 Stencil 구조체(struct)를 연다(6–14). 뒤쪽·현재·앞쪽의 상수 계수(constant coefficient)와 기울기(slope) 6개를 보유한다(15–20). |
| 22–59 | 시작 시 13행 Stencil 구조체 안이다. `__device__` (22·29·37) limit·정적 minH_x·정적 minH_y를 선언한다(23–43). private에는 `__device__ NUMERIC_TYPE backward_neg();` (46), `__device__ NUMERIC_TYPE local_pos();` (47), `__device__ NUMERIC_TYPE local_neg();` (48), `__device__ NUMERIC_TYPE forward_pos();` (49), `__device__` (51) minmod(a,b,c)가 있다(52–57). |
| 60–93 | Slopes의 포인터는 `NUMERIC_TYPE* __restrict__ ETA1x;` (62), `NUMERIC_TYPE* __restrict__ ETA1y;` (63), `NUMERIC_TYPE* __restrict__ HU1x;` (64), `NUMERIC_TYPE* __restrict__ HU1y;` (65), `NUMERIC_TYPE* __restrict__ HV1x;` (66), `NUMERIC_TYPE* __restrict__ HV1y;` (67)이다. `__device__` (69·78·86) ETA_stencil_x·HU_stencil_x·HV_stencil_x를 선언한다(70–92). |
| 94–130 | 시작 시 60행 Slopes 구조체 안이다. `__device__` (94·103·111) ETA_stencil_y·HU_stencil_y·HV_stencil_y를 선언한다(95–117). 정적 allocate_device는 Slopes& flow·Geometry를 받고, free_device는 Slopes& slopes를 받는다(119–128). 구조체를 닫는다(129). |
| 131–154 | MaxH는 Geometry를 받는 생성자, const Flow&를 받는 update, 소멸자를 선언한다(134–144). private에는 const elements·void* temp·size_t bytes가 있다(146–150). 세 이름공간을 닫는다(152–154). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
