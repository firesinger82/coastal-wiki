---
file: models/ShorelineS/raw/source_code/shorelines/functions/get_fields.m
lines: 41
sha256: 8725e0109731a847ddc92eca325b56e00976937e0f47c606118cdb13881076ba
reader: codex gpt-6.1-sol
read_date: 2026-10-12
---

# get_fields.m — 판독 구간 기록

구간은 1행부터 41행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–34 | 함수 시그니처 `function [fieldnm] = get_fields(datastructure)` (1). 구조체의 필드 이름을 셀 문자열로 반환한다는 주석(4–5). 저작권·연락처·LGPL 2.1 이상·무보증·빈 줄(7–34). |
| 35–41 | Octave 조건 `if (isoctave)` (35)이면 fieldnames 호출 `fieldnm=fieldnames(datastructure);` (36). 대체 경로 `else` (37)에서는 fields 호출 `fieldnm=fields(datastructure);` (38). 분기·함수 종료·빈 줄(39–41). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
