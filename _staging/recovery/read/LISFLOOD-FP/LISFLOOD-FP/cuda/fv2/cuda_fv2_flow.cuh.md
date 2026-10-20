---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/fv2/cuda_fv2_flow.cuh
lines: 186
sha256: e31b5c56bc49ae52afa5054d303bae2a3f56a2979a8dfb7fce417074e2ddceed
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# cuda_fv2_flow.cuh — 판독 구간 기록

구간은 1행부터 186행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–29 | `#pragma once` (1)과 헤더 포함(2–4), lis::cuda::fv2 이름 공간(namespace)(6–11), 두 계수 형식의 전방 선언(13–14). FlowCoeffs는 아홉 NUMERIC_TYPE 성분을 보유한다(16–26). `FlowCoeffs() = default;` (28)이며 필드 선언에 기본값은 없다. 조건부 전처리 지시는 없다. |
| 30–78 | 시작 시 6·8·10행 이름 공간·16행 FlowCoeffs 구조체 안. 두 생성자는 `__host__ __device__` (30·44). 아홉 수치 또는 FlowCoeffsRef를 받는다(31–48). set_0·get_0·neg_x·pos_x·neg_y·pos_y·operator+=는 각각 `__device__` (50·56·59·62·65·68·72)로 선언한다. 구조체 종료(77). |
| 79–102 | `__host__ __device__` (79)의 inline operator+는 `return { lhs.H + rhs.H, lhs.H1x + rhs.H1x, lhs.H1y + rhs.H1y,` (86), `lhs.HU + rhs.HU, lhs.HU1x + rhs.HU1x, lhs.HU1y + rhs.HU1y,` (87), `lhs.HV + rhs.HV, lhs.HV1x + rhs.HV1x, lhs.HV1y + rhs.HV1y };` (88). `__host__ __device__` (91)의 inline operator*는 `return { lhs * rhs.H, lhs * rhs.H1x, lhs * rhs.H1y,` (98), `lhs * rhs.HU, lhs * rhs.HU1x, lhs * rhs.HU1y,` (99), `lhs * rhs.HV, lhs * rhs.HV1x, lhs * rhs.HV1y };` (100). |
| 103–127 | FlowCoeffsRef는 아홉 NUMERIC_TYPE 참조를 보유한다(103–113). 대입 연산자는 `__host__ __device__` (115), set_0는 `__device__` (121)로 선언한다. |
| 128–164 | Flow는 `NUMERIC_TYPE* __restrict__` 형태로 아홉 흐름 성분(130–138)과 maxH·totalHtm·maxHtm·initHtm(140–143)을 선언한다. 고정 메모리(pinned memory)·장치 메모리 할당 함수를 선언한다(145–155). `__host__ __device__ FlowCoeffsRef operator[]` (157)는 idx를 받아 `return { H[idx], H1x[idx], H1y[idx], HU[idx], HU1x[idx], HU1y[idx],` (162), `HV[idx], HV1x[idx], HV1y[idx] };` (163)로 참조 묶음을 반환한다. |
| 165–186 | 시작 시 6·8·10행 이름 공간·128행 Flow 구조체 안. static copy는 dst·src·geometry를 받는다(166–171). static free_pinned·free_device는 Flow 참조를 받는다(173–181). 구조체·이름 공간을 닫는다(182–186). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 18–28: FlowCoeffs의 기본 생성자는 default 선언이다. 아홉 수치 필드에는 멤버 기본 초기값이 없다.
