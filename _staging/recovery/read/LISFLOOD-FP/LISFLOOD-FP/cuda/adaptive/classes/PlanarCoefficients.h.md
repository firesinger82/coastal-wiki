---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/classes/PlanarCoefficients.h
lines: 59
sha256: 6885ce5c47934904a27e3ab547349e9e328b29a0ed915472ef0020751e8e50a4
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# PlanarCoefficients.h — 판독 구간 기록

구간은 1행부터 59행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–25 | `#pragma once` (1), cuda_runtime.h·real.h 포함(3–5). 전처리 조건 분기는 없다. PlanarCoefficients는 real _0·_1x·_1y를 보유한다(7–11). `__device__` (13)의 대입 연산자 선언 `inline PlanarCoefficients operator=` (14)는 rhs의 세 성분을 복사하고 *this를 반환한다(15–24). |
| 26–40 | 시작 시 7–8행 PlanarCoefficients 구조체 안. `__device__` (26)의 누적 덧셈 선언 `inline PlanarCoefficients operator+=` (27)은 rhs를 받아(28–31) 세 성분 계산식 `_0  += rhs._0;`<br>`_1x += rhs._1x;`<br>`_1y += rhs._1y;` (32–34)을 실행한다. *this 반환·메서드·구조체 종료(36–39). |
| 41–59 | 구조체 밖 `__device__` (41)의 operator*(42–47)는 실수와 세 계수의 곱 `return { lhs * rhs._0, lhs * rhs._1x, lhs * rhs._1y };` (48)을 반환한다. `__device__` (51)의 operator+(52–57)는 성분별 합 `return { lhs._0 + rhs._0,  lhs._1x + rhs._1x,  lhs._1y + rhs._1y };` (58)을 반환한다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 14·23·27·36: operator=와 operator+=는 PlanarCoefficients를 반환형으로 선언한다. 두 연산자는 *this를 값으로 반환한다.
