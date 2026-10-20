---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/swe/dg2/friction.h
lines: 21
sha256: d98f26a7052c8e3f53ff6b7f44126a4036c7ffdb5335c6354383daeeec791b82
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# friction.h — 판독 구간 기록

구간은 1행부터 21행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–21 | `#pragma once` (1)로 중복 포함을 막고 ../../lisflood.h를 포함한다(2). dg2 이름공간(namespace)에서 apply_friction은 Pars·Solver·Arrays 포인터를 받는다(4–11). friction은 Solver 포인터·NUMERIC_TYPE H·NUMERIC_TYPE& HU·NUMERIC_TYPE& HV·NUMERIC_TYPE n을 받는다(13–20). 함수 본문·추가 전처리 조건·기본 인수는 없다. 이름공간을 닫는다(21). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
