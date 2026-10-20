---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/input/read_cell_size.h
lines: 7
sha256: 8582d8e76f414594952c7cd9d3699ec89a09953ebde867e8ca1392a54db6b0b4
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# read_cell_size.h — 판독 구간 기록

구간은 1행부터 7행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–7 | `#pragma once` (1), 실수형 헤더 포함(3), 문자열 키 판독 헤더 포함(5), 빈 줄. read_cell_size가 const char* 입력 파일명을 받아 real을 반환한다고 선언한다(7). 함수 본문과 전처리 조건 분기는 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
