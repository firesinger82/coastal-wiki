---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/input/read_keyword_int.h
lines: 12
sha256: b79d1faa194b9711a2ce4bd47f8d4fde14979d4656a346392636641b5076e85e
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# read_keyword_int.h — 판독 구간 기록

구간은 1행부터 12행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–12 | `#pragma once` (1) 뒤 cstdlib·cstdio·cstring 표준 헤더를 포함한다(3–5). read_keyword_int가 const char* 파일명·키워드(keyword), const int& 비교 문자 수를 받아 int를 반환한다고 선언한다(7–12). 함수 본문과 전처리 조건 분기는 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
