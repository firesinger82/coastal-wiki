---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/classes/FlowCoeffs.h
lines: 104
sha256: f5a465d3eb6113033ae2b0fe32d1c27230b9654874ad4b6a8953fb73c1c9ef1e
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# FlowCoeffs.h — 판독 구간 기록

구간은 1행부터 104행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–24 | `#pragma once` (1). FlowVector·PlanarCoefficients·LegendreBasis·eval_loc_face_val_dg2 헤더를 포함한다(3–6). 전처리 조건 분기는 없다. FlowCoeffs는 PlanarCoefficients h·qx·qy를 보유한다(8–12). `__host__ __device__` (14)의 local_face_val(15–16)은 세 필드를 같은 basis로 평가하여 FlowVector를 반환한다. 반환 전체 `return`<br>`{`<br>`eval_loc_face_val_dg2(h,  basis),`<br>`eval_loc_face_val_dg2(qx, basis),`<br>`eval_loc_face_val_dg2(qy, basis)`<br>`};` (17–22). |
| 25–57 | 시작 시 8–9행 FlowCoeffs 구조체 안. 장치 한정자 `__device__` (25)·`__device__` (36)·`__device__` (47)가 각각 set_0·set_1x·set_1y에 붙는다(26–30·37–41·48–52). 각 메서드는 FlowVector v의 h·qx·qy를 같은 이름의 _0·_1x·_1y 필드에 복사한다(31–33·42–44·53–55). |
| 58–85 | 시작 시 8–9행 FlowCoeffs 구조체 안. `__device__` (58)의 대입 연산자(operator) 선언 `inline FlowCoeffs operator=` (59)는 h·qx·qy를 rhs에서 복사하고 *this를 반환한다(60–69). `__device__` (71)의 누적 덧셈 연산자 `inline FlowCoeffs operator+=` (72)는 성분별 `h  += rhs.h;`<br>`qx += rhs.qx;`<br>`qy += rhs.qy;` (77–79) 후 *this를 반환한다(81). 구조체 종료(84). |
| 86–104 | 구조체 밖 자유 연산자(free operator). `__device__` (86)의 실수 좌측 곱 operator*(87–92)는 `return { lhs * rhs.h, lhs * rhs.qx, lhs * rhs.qy };` (93)을 반환한다. `__device__` (96)의 FlowCoeffs 덧셈 operator+(97–102)는 `return { lhs.h + rhs.h, lhs.qx + rhs.qx,  lhs.qy + rhs.qy };` (103)을 반환한다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 59·68·72·81: operator=와 operator+=의 반환형은 모두 FlowCoeffs이다. 두 연산자는 *this를 값으로 반환한다.
