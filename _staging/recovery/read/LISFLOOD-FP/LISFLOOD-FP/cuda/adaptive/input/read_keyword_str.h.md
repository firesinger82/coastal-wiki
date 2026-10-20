---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/input/read_keyword_str.h
lines: 13
sha256: 88b7be6b350bbdc11c3332e34d45334ca1f908f5e2f0983c8efb26fc508acc5b
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# read_keyword_str.h — 판독 구간 기록

구간은 1행부터 13행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–13 | `#pragma once` (1) 뒤 cstdlib·cstdio·cstring 표준 헤더를 포함한다(3–5). read_keyword_str가 const char* 파일명·키워드(keyword), const int& 비교 문자 수, char* 출력 버퍼를 받으며 반환형은 void라고 선언한다(7–13). 함수 본문과 전처리 조건 분기는 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
