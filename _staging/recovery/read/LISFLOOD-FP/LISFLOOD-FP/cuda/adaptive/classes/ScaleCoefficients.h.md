---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/classes/ScaleCoefficients.h
lines: 74
sha256: e94389f17662c57d6f2affcb00a10a9acd8386ec1122f86879b3ac4c06d3a676
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# ScaleCoefficients.h — 판독 구간 기록

구간은 1행부터 74행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–26 | `#pragma once` (1) 뒤 CUDA 유틸리티(utility)·실수형·해법 종류 헤더를 포함한다(3–6). 전처리 조건 분기는 없다. 구조체는 `eta`·`qx`·`qy`·`z` 각각의 0·1x·1y 계수(coefficient) 포인터를 선언한다(8–23). 복사 표지 기본값은 `bool is_copy_cuda = false;` (25). |
| 27–50 | 생성자(constructor)는 전체 원소 수와 해법 종류를 받는다(27–31). `size_t bytes = sizeof(real) * num_all_elems;` (33). 0계수 4개는 `(real*)malloc_device(bytes)`로 할당한다(35–38). `eta1x = (solver_type == MWDG2) ? (real*)malloc_device(bytes) : nullptr;` (40), `qx1x  = (solver_type == MWDG2) ? (real*)malloc_device(bytes) : nullptr;` (41), `qy1x  = (solver_type == MWDG2) ? (real*)malloc_device(bytes) : nullptr;` (42), `z1x   = (solver_type == MWDG2) ? (real*)malloc_device(bytes) : nullptr;` (43). y 방향은 `eta1y = (solver_type == MWDG2) ? (real*)malloc_device(bytes) : nullptr;` (45), `qx1y  = (solver_type == MWDG2) ? (real*)malloc_device(bytes) : nullptr;` (46), `qy1y  = (solver_type == MWDG2) ? (real*)malloc_device(bytes) : nullptr;` (47), `z1y   = (solver_type == MWDG2) ? (real*)malloc_device(bytes) : nullptr;` (48). |
| 51–74 | 복사 생성자(copy constructor)는 `*this = original`로 멤버를 복사하고 복사 표지를 true로 둔다(51). 소멸자(destructor)의 `if (!is_copy_cuda)` (55) 안에서 12개 계수 포인터 모두에 `CHECK_CUDA_ERROR( free_device(...) )`를 호출한다(57–70). 구조체를 닫는다(74). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 33–48: 장치 메모리(device memory)를 할당하지만 이 생성자에는 계수 배열의 값 초기화가 없다.
- 40–48·55–70: MWDG2가 아니면 고차 계수 포인터는 nullptr이다. 소멸자의 해제 호출에는 solver_type 또는 nullptr를 검사하는 별도 조건이 없다.
