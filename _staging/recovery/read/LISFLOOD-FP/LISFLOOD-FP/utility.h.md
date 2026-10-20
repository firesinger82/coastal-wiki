---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/utility.h
lines: 22
sha256: 17c2c57e84eb42f9abd0455b7f1cc0213ff5c58f9573a4085bf6da00f6a8e552
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# utility.h — 판독 구간 기록

구간은 1행부터 22행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–4 | `#pragma once` (1)와 `#include "lisflood.h"` (3)를 적는다. 조건부 컴파일(conditional compilation) 지시는 없다. 이 파일의 모든 구간에 별도의 전처리 매크로(macro) 조합 조건이 없다. 두 지시 사이와 뒤의 빈 줄을 포함한다(2·4). |
| 5–12 | 전처리 조건 없음. `void *memory_allocate(size_t size);` (5)는 크기 인수를 받는 할당 함수를 선언한다. `NUMERIC_TYPE*memory_allocate_zero_numeric_legacy(size_t size);` (7), `NUMERIC_TYPE*memory_allocate_numeric_legacy(size_t size);` (8)는 수치 배열 할당 함수를 선언한다. `void memory_free_legacy(void** memory);` (9), `void memory_free_legacy(int** memory);` (10), `void memory_free_legacy(NUMERIC_TYPE** memory);` (11)는 세 포인터 형식(pointer type)의 레거시(legacy) 해제 함수를 선언한다. 빈 줄을 포함한다(6·12). 함수 본문이나 기본 인수(default argument)는 없다. |
| 13–19 | 전처리 조건 없음. `void memory_free(void** memory);` (13), `void memory_free(int** memory);` (14), `void memory_free(NUMERIC_TYPE** memory);` (15)는 포인터만 받는 해제 함수를 선언한다. `void memory_free(void** memory, size_t size);` (18)는 포인터와 크기를 받는 동명 함수를 선언한다. 사이와 뒤의 빈 줄을 포함한다(16–17·19). 함수 본문이나 기본 인수는 없다. |
| 20–22 | 전처리 조건 없음. `char *trimwhitespace(char *str);` (20)는 char*를 받아 char*를 반환하는 함수를 선언한다. 빈 줄(21) 뒤의 `void SetArrayValue(int* arr, int value, int length);` (22)는 정수 배열 포인터와 설정값·길이를 받는 함수를 선언한다. 함수 본문이나 기본 인수는 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 9–11 및 utility.cpp 32–52: 이 헤더는 memory_free_legacy의 void**·int**·NUMERIC_TYPE** 인수형을 선언한다. 이번에 함께 판독한 utility.cpp에는 int**·NUMERIC_TYPE** 인수형의 정의가 있다. utility.cpp 전체 1–130행에는 void** 인수형의 정의가 없다.
