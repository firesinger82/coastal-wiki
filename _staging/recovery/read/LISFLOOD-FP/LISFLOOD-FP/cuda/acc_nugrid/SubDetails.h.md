---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/acc_nugrid/SubDetails.h
lines: 49
sha256: a6c4c3a8d56235753443854f50fb13a7a6a63338d3b31270f9b01a4751733051
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# SubDetails.h — 판독 구간 기록

구간은 1행부터 49행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–21 | `#pragma once` (1), cuda_utils·lisflood 포함(3–4), `lis::cuda::acc_nugrid` 이름공간(namespace)(6–11). SubDetails 구조체(struct)(13–14)는 NUMERIC_TYPE* alpha·beta·gamma(15–17), `bool  is_copy = false;` (18)를 보유한다. `SubDetails() = default; //new` (20)는 기본 생성자(default constructor) 선언이다. 이 파일의 모든 구간에는 `#if` 계열 전처리 조건 분기가 없다. |
| 22–34 | 시작 시 13행 구조체 안. num_details를 받는 생성자(constructor)(22–23)의 `size_t bytes = sizeof(NUMERIC_TYPE) * num_details;` (24). `alpha = (NUMERIC_TYPE*)malloc_device(bytes);` (26), `beta  = (NUMERIC_TYPE*)malloc_device(bytes);` (27), `gamma = (NUMERIC_TYPE*)malloc_device(bytes);` (28). is_copy 재설정은 주석(30). 복사 생성자(copy constructor) `SubDetails(const SubDetails& original) { *this = original; is_copy = true; }` (33). |
| 35–49 | 시작 시 13행 구조체 안. 소멸자(destructor)(35–36)의 `if (!is_copy)` (37)에서 free_device(alpha)·free_device(beta)·free_device(gamma)를 호출한다(39–41). 블록·구조체·이름공간 종료와 빈 줄(42–49). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 15–20·35–43: alpha·beta·gamma 선언에는 초기값이 없다. 명시적으로 default 처리한 기본 생성자에도 포인터 초기화식이 없다. 소멸자는 is_copy가 거짓이면 세 포인터를 free_device에 전달한다.
- 22–31: 크기 인수 생성자는 배열을 할당하지만 배열 원소를 채우는 문장을 포함하지 않는다.
