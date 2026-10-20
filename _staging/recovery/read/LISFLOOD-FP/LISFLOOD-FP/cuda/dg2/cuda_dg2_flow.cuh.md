---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/dg2/cuda_dg2_flow.cuh
lines: 209
sha256: 4a4883db292d1fd082384aa731a2569a0fba73e6a1b0dd745d95f3a020550d73
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# cuda_dg2_flow.cuh — 판독 구간 기록

구간은 1행부터 209행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–29 | `#pragma once` (1)와 lisflood·공통 flow·기하 헤더를 포함한다(2–4). 전처리 조건 분기는 없다. lis::cuda::dg2 이름공간(namespace)과 두 전방 선언(forward declaration)이다(6–14). FlowCoeffs는 H/HU/HV의 0차·1x·1y 계수(coefficient) 9개를 보유한다(16–26). `FlowCoeffs() = default;` (28)이다. |
| 30–67 | 시작 시 16행 FlowCoeffs 구조체(struct) 안이다. `__host__ __device__` (30·44) 생성자는 9개 값 또는 FlowCoeffsRef를 받는다(31–48). `__device__` (50·56·62) set_0·set_1x·set_1y는 FlowVector를 받는다(51–66). |
| 68–101 | 시작 시 16행 FlowCoeffs 구조체 안이다. `__device__` (68·71·74·77·80·83·86·89·92·95)는 get_0, 네 면 상태(face state), 네 가우스 점(Gauss point), operator+=에 붙는다(69–99). 구조체를 닫는다(100). |
| 102–125 | `__host__ __device__` (102·114)의 inline 연산자이다. 덧셈은 `return { lhs.H+rhs.H, lhs.H1x+rhs.H1x, lhs.H1y+rhs.H1y,` (109), `lhs.HU+rhs.HU, lhs.HU1x+rhs.HU1x, lhs.HU1y+rhs.HU1y,` (110), `lhs.HV+rhs.HV, lhs.HV1x+rhs.HV1x, lhs.HV1y+rhs.HV1y };` (111)이다. 스칼라(scalar) 곱은 `return { lhs*rhs.H, lhs*rhs.H1x, lhs*rhs.H1y,` (121), `lhs*rhs.HU, lhs*rhs.HU1x, lhs*rhs.HU1y,` (122), `lhs*rhs.HV, lhs*rhs.HV1x, lhs*rhs.HV1y };` (123)이다. |
| 126–150 | FlowCoeffsRef는 9개 NUMERIC_TYPE 참조를 보유한다(128–136). `__host__ __device__` (138) 대입 연산자와 `__device__` (144) set_0을 선언한다(139–148). |
| 151–179 | Flow의 상태 포인터는 `NUMERIC_TYPE* __restrict__ H;` (153), `NUMERIC_TYPE* __restrict__ H1x;` (154), `NUMERIC_TYPE* __restrict__ H1y;` (155), `NUMERIC_TYPE* __restrict__ HU;` (156), `NUMERIC_TYPE* __restrict__ HU1x;` (157), `NUMERIC_TYPE* __restrict__ HU1y;` (158), `NUMERIC_TYPE* __restrict__ HV;` (159), `NUMERIC_TYPE* __restrict__ HV1x;` (160), `NUMERIC_TYPE* __restrict__ HV1y;` (161)이다. 추가 포인터는 `NUMERIC_TYPE* __restrict__ maxH;` (163), `NUMERIC_TYPE* __restrict__ totalHtm;` (164), `NUMERIC_TYPE* __restrict__ maxHtm;` (165), `NUMERIC_TYPE* __restrict__ initHtm;` (166)이다. 정적 할당 함수 allocate_pinned·allocate_device를 선언한다(168–178). |
| 180–209 | 시작 시 151행 Flow 구조체 안이다. `__host__ __device__ FlowCoeffsRef operator[]` (180)는 idx의 H/HU/HV 9개 계수 참조를 중괄호 초기화(brace initialization)로 반환한다(185–186). copy·free_pinned·free_device를 선언한다(189–204). 구조체·이름공간을 닫는다(205–209). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 18–28: FlowCoeffs의 수치 멤버 선언에는 기본값이 없다. 인수 없는 생성자는 = default로 선언되어 있다.
