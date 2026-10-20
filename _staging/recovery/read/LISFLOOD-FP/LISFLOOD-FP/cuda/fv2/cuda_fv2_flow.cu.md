---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/fv2/cuda_fv2_flow.cu
lines: 225
sha256: 6ae74229edbf9e5c7eb4cba178fbf5b3de2425c47ed44f988c7a771d59e50e6f
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# cuda_fv2_flow.cu — 판독 구간 기록

구간은 1행부터 225행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–45 | 헤더 포함(1–2). `__host__ __device__` (4) FlowCoeffs 생성자는 H·H1x·H1y·HU·HU1x·HU1y·HV·HV1x·HV1y의 아홉 인수를 같은 이름의 필드에 복사한다(5–27). `__host__ __device__` (29) 복사 생성자는 FlowCoeffsRef의 아홉 참조 값을 필드에 복사한다(30–44). 조건부 전처리 지시는 없다. |
| 46–92 | 장치 함수(device function) `__device__` (46)의 set_0는 H/HU/HV만 복사한다(47–55). `__device__` (58)의 get_0는 `return { H, HU, HV };` (61). `__device__` (64) neg_x는 `return { H + C(0.5) * H1x, HU + C(0.5) * HU1x,` (67), `HV + C(0.5) * HV1x };` (68). `__device__` (71) pos_x는 `return { H - C(0.5) * H1x, HU - C(0.5) * HU1x,` (74), `HV - C(0.5) * HV1x };` (75). `__device__` (78) neg_y는 `return { H + C(0.5) * H1y, HU + C(0.5) * HU1y,` (81), `HV + C(0.5) * HV1y };` (82). `__device__` (85) pos_y는 `return { H - C(0.5) * H1y, HU - C(0.5) * HU1y,` (88), `HV - C(0.5) * HV1y };` (89). |
| 93–141 | `__device__` (93)의 operator+=는 `H += rhs.H;` (99), `H1x += rhs.H1x;` (100), `H1y += rhs.H1y;` (101), `HU += rhs.HU;` (102), `HU1x += rhs.HU1x;` (103), `HU1y += rhs.HU1y;` (104), `HV += rhs.HV;` (105), `HV1x += rhs.HV1x;` (106), `HV1y += rhs.HV1y;` (107)를 계산하고 *this를 반환한다(109). `__host__ __device__` (112)의 FlowCoeffsRef::operator=는 아홉 성분을 복사하고 *this를 반환한다(113–129). `__device__` (131)의 FlowCoeffsRef::set_0는 H/HU/HV만 복사한다(132–140). |
| 142–175 | Flow::allocate_pinned는 아홉 성분마다 `cuda::GhostRaster::allocate_pinned(geometry)` (148–156)를 호출한다. Flow::allocate_device도 아홉 성분마다 `cuda::GhostRaster::allocate_device(geometry)` (165–173)를 호출한다. 조건·루프 없이 호출을 나열한다. |
| 176–193 | Flow::copy는 H·H1x·H1y·HU·HU1x·HU1y·HV·HV1x·HV1y에 대해 `cuda::GhostRaster::copy`를 각각 호출한다(183–191). 전달 인수는 각 dst 포인터·src 포인터·geometry이다. |
| 194–225 | Flow::free_pinned는 아홉 성분에 `cuda::free_pinned`를 각각 호출한다(199–207). Flow::free_device는 아홉 성분에 `cuda::free_device`를 각각 호출한다(215–223). 마지막 빈 줄을 포함한다(225). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 148–173·183–191·199–223: 할당·복사·해제 루틴은 아홉 흐름 성분을 처리한다. Flow 헤더의 maxH·totalHtm·maxHtm·initHtm 포인터에 대한 처리는 이 파일에 없다.
