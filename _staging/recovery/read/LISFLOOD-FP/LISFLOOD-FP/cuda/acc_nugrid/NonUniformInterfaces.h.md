---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/acc_nugrid/NonUniformInterfaces.h
lines: 58
sha256: 2c0d0b934ead8d400608ab68ca0d8f9a0cbee20240c1ca7a76e6abf1ffcceedf
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# NonUniformInterfaces.h — 판독 구간 기록

구간은 1행부터 58행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–24 | `#pragma once` (1), cuda_utils·lisflood·index_1D 포함(3–5), `lis::cuda::acc_nugrid` 이름공간(namespace)(7–12). 비균일 격자 접면(non-uniform interface) 구조체(struct) NonUniformInterfaces(14–15)는 NUMERIC_TYPE* q_vol·dx·dx_sum(16–18), int* nghbrs·nghbr_counts·load_idcs(19–21), int length·bool is_copy(22–23)를 선언한다. 이 파일의 모든 구간에는 `#if` 계열 전처리 조건 분기가 없다. |
| 25–41 | 시작 시 14행 NonUniformInterfaces 구조체 안. 생성자(constructor)는 num_interfaces를 받고(25–26), `size_t bytes_real = num_interfaces * sizeof(NUMERIC_TYPE);` (27), `size_t bytes_int  = num_interfaces * sizeof(int);` (28)를 계산한다. q_vol·dx·dx_sum에는 `(NUMERIC_TYPE*)malloc_device(bytes_real)` (30–32), nghbrs·nghbr_counts·load_idcs에는 `(int*)malloc_device(bytes_int)` (33–35)를 대입한다. length=num_interfaces·is_copy=false(36–37). 복사 생성자(copy constructor)는 `NonUniformInterfaces(const NonUniformInterfaces& original) { *this = original; is_copy = true; }` (40). |
| 42–58 | 시작 시 14행 구조체 안. 소멸자(destructor)(42–43)의 `if (!is_copy)` (44)에서 q_vol·dx·dx_sum·nghbrs·nghbr_counts·load_idcs에 free_device를 호출한다(46–51). 블록·구조체·이름공간 종료와 빈 줄(52–58). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 25–38: 생성자는 여섯 배열을 할당하지만 원소 값을 채우는 문장을 포함하지 않는다.
