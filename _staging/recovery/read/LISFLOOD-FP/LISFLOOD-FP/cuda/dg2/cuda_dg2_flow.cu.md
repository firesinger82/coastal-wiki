---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/dg2/cuda_dg2_flow.cu
lines: 269
sha256: 94b20379172a0702367196568ebf828ec8f74822b4b8ccf173b13cb6731628af
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# cuda_dg2_flow.cu — 판독 구간 기록

구간은 1행부터 269행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–45 | DG2 flow·util 헤더를 포함한다(1–2). 전처리 조건 분기는 없다. `__host__ __device__` (4·29) 생성자는 수심 H·유량 HU/HV와 1x·1y 계수(coefficient) 9개를 저장한다(5–27). 두 번째 생성자는 FlowCoeffsRef의 같은 9개 값을 복사한다(30–44). |
| 46–84 | `__device__` (46·57·68) set_0·set_1x·set_1y는 FlowVector의 H/HU/HV를 해당 계수에 복사한다(47–77). `__device__` (79) get_0은 `return { H, HU, HV };` (82)로 0차 계수를 반환한다. |
| 85–112 | `__device__` (85·92·99·106) neg_x·pos_x·neg_y·pos_y는 면 상태(face state)를 재구성한다. 식은 `return { H + SQRT(C(3.0))*H1x, HU + SQRT(C(3.0))*HU1x,` (88), `HV + SQRT(C(3.0))*HV1x };` (89); `return { H - SQRT(C(3.0))*H1x, HU - SQRT(C(3.0))*HU1x,` (95), `HV - SQRT(C(3.0))*HV1x };` (96); `return { H + SQRT(C(3.0))*H1y, HU + SQRT(C(3.0))*HU1y,` (102), `HV + SQRT(C(3.0))*HV1y };` (103); `return { H - SQRT(C(3.0))*H1y, HU - SQRT(C(3.0))*HU1y,` (109), `HV - SQRT(C(3.0))*HV1y };` (110)이다. |
| 113–136 | `__device__` (113·119·125·131) gauss_lower_x·gauss_upper_x·gauss_lower_y·gauss_upper_y는 가우스 점(Gauss point) 상태를 반환한다. 식은 `return { H - H1x, HU - HU1x, HV - HV1x };` (116), `return { H + H1x, HU + HU1x, HV + HV1x };` (122), `return { H - H1y, HU - HU1y, HV - HV1y };` (128), `return { H + H1y, HU + HU1y, HV + HV1y };` (134)이다. |
| 137–155 | `__device__` (137) FlowCoeffs::operator+=는 `H += rhs.H;` (143), `H1x += rhs.H1x;` (144), `H1y += rhs.H1y;` (145), `HU += rhs.HU;` (146), `HU1x += rhs.HU1x;` (147), `HU1y += rhs.HU1y;` (148), `HV += rhs.HV;` (149), `HV1x += rhs.HV1x;` (150), `HV1y += rhs.HV1y;` (151)를 수행하고 *this를 반환한다(153). |
| 156–185 | `__host__ __device__` (156) FlowCoeffsRef::operator=는 우변의 9개 값을 참조 대상에 복사한 뒤 *this를 반환한다(157–173). `__device__` (175) FlowCoeffsRef::set_0은 H/HU/HV만 복사한다(176–184). |
| 186–219 | Flow::allocate_pinned는 H·H1x·H1y·HU·HU1x·HU1y·HV·HV1x·HV1y 각각에 cuda::GhostRaster::allocate_pinned를 호출한다(186–201). allocate_device는 같은 9개 필드에 cuda::GhostRaster::allocate_device를 호출한다(203–218). |
| 220–237 | Flow::copy는 같은 이름의 dst·src 필드 9쌍에 cuda::GhostRaster::copy를 호출한다(227–235). |
| 238–269 | Flow::free_pinned는 9개 필드 각각을 cuda::free_pinned로 해제한다(243–251). free_device는 같은 9개 필드를 cuda::free_device로 해제한다(259–267). 마지막 빈 줄을 포함한다(269). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 186–268: 이 파일의 Flow 할당·복사·해제 루틴은 H·HU·HV의 0차·1x·1y 필드만 처리한다. maxH·totalHtm·maxHtm·initHtm은 이 파일 본문에 등장하지 않는다.
