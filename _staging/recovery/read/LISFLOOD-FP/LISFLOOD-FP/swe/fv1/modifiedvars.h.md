---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/swe/fv1/modifiedvars.h
lines: 161
sha256: 0ff195fcc8ae31d81e292060a082cc7586b0d93d742a75fcb4c28e5e88d796fb
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# modifiedvars.h — 판독 구간 기록

구간은 1행부터 161행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–53 | `#pragma once`(1), lisflood 헤더 포함(2) 후 fv1 이름공간(namespace)을 연다(4–5). 수정 지형(modified topography) 초기화(6–10)와 수정 수심 갱신(12–16), HU의 x·y 양쪽 수정값 함수 네 개(18–52)를 선언한다. 조건부 전처리 분기·실행문·기본 인수값은 없다. 원문: `#pragma once` (1); `#include "../../lisflood.h"` (2). |
| 54–100 | 시작 시 4행 fv1 이름공간 안이다. HV의 네 수정값 함수(54–88)와 공통 `discharge_star`(90–99) 원형이다. 공통형은 수정 수심 배열과 유량 성분 배열, Pars·Solver·Arrays·i·j를 받는다. 반환형은 NUMERIC_TYPE이다. |
| 101–143 | 시작 시 4행 fv1 이름공간 안이다. 네 방향 Zdagger 원형(101–131)과 공통형(133–142)을 선언한다. 공통형은 면 지형 배열과 지형 면 인덱스·수면고 셀 인덱스를 따로 받는다. 조건·식은 없다. |
| 144–161 | 시작 시 4행 fv1 이름공간 안이다. 수면고(water surface elevation) 함수 `eta`(144–150)와 성분 속도 함수 `speed`(152–160)를 선언한다. 이름공간을 161행에서 닫는다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
