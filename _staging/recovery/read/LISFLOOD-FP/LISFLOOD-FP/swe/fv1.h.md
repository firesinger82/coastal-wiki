---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/swe/fv1.h
lines: 107
sha256: 79341672c2f8c0a6ab084c91eed4ed25d174125c297381c1d34ea08804dfe6d2
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# fv1.h — 판독 구간 기록

구간은 1행부터 107행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–35 | `#pragma once`(1), lisflood·rain 헤더 포함(2–3) 후 fv1 이름공간(namespace)을 연다(5–6). 전체 해석 `solve`(7–18), nodata 배수(20–26), 점원(point source) 갱신(28–34)의 원형이다. solve는 Stage·verbose까지 받고 나머지는 Pars·Solver·BoundCs·Arrays를 받는다. 조건부 전처리 분기·기본 인수값·실행문은 없다. 원문: `#pragma once` (1); `#include "../lisflood.h"` (2); `#include "../rain/rain.h"` (3). |
| 36–64 | 시작 시 5행 fv1 이름공간 안이다. 마찰(36–41), 내부 플럭스(43–48), 경계 플럭스(50–56), 유동 변수 갱신(58–63)을 선언한다. 경계형에만 BoundCs 인수가 추가된다. 계산식과 조건은 없다. |
| 65–89 | 시작 시 5행 fv1 이름공간 안이다. `set_boundary_values`(65–81)는 셀·경계 인덱스 및 부호와 내부·외부 H·HU·HV 참조를 받는다. `Tstep_from_cfl`(83–88)은 Pars·Solver·Arrays로 NUMERIC_TYPE 시간 간격을 반환하는 원형이다. 기본값은 없다. |
| 90–107 | 시작 시 5행 fv1 이름공간 안이다. x·y 바닥 원천항(bed source term) 함수(90–106)는 Pars·Solver·Arrays와 const int i·j를 받고 NUMERIC_TYPE을 반환한다. 이름공간은 107행에서 끝난다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
