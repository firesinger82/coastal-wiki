---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/input/read_save_interval.h
lines: 13
sha256: f237fa0735dbc4604ce027d19f9daf5dd98aea43ce56e9d6ade2e16c354cd4dc
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# read_save_interval.h — 판독 구간 기록

구간은 1행부터 13행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–8 | 단일 포함 지시와 C 표준 입출력·종료·문자열 헤더, SaveInterval 형식을 포함한다(1–7). 조건부 전처리 분기는 없다. 원문: `#pragma once` (1). |
| 9–13 | 입력 파일명과 간격 유형 문자열을 받는 read_save_interval 원형을 선언한다(9–13). 반환 형식은 SaveInterval이다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
