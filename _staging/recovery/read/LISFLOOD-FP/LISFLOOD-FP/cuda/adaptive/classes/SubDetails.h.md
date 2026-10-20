---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/classes/SubDetails.h
lines: 37
sha256: 4f79b5b45cec9710b23d29958e092ddee55e35994689a26a0fea092eef301a13
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# SubDetails.h — 판독 구간 기록

구간은 1행부터 37행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–15 | `#pragma once` (1), CUDA 유틸리티(utility)·실수형 헤더 포함(3–5). 전처리 조건 분기는 없다. alpha·beta·gamma 포인터와 `bool  is_copy_cuda = false;` (12)를 선언한다(7–12). `SubDetails() = default;` (14)로 기본 생성자(default constructor)를 둔다. |
| 16–26 | 개수를 받는 생성자(constructor)에서 `size_t bytes = sizeof(real) * num_details;` (18). `alpha = (num_details > 0) ? (real*)malloc_device(bytes) : nullptr;` (20), `beta  = (num_details > 0) ? (real*)malloc_device(bytes) : nullptr;` (21), `gamma = (num_details > 0) ? (real*)malloc_device(bytes) : nullptr;` (22)로 양수 개수일 때만 장치 메모리(device memory)를 할당한다. 복사 생성자는 멤버를 복사한 뒤 복사 표지를 true로 둔다(25). |
| 27–37 | 소멸자(destructor)의 `if (!is_copy_cuda)` (29) 안에서 alpha·beta·gamma 각각에 CHECK_CUDA_ERROR로 감싼 free_device를 호출한다(31–33). 소멸자와 구조체를 닫는다(34–37). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 9–14: 포인터 세 필드에는 선언 시 초기값이 없고 기본 생성자는 = default이다.
- 20–22·29–33: num_details가 양수가 아니면 포인터는 nullptr이다. 소멸자는 is_copy_cuda만 조건으로 검사한 뒤 세 포인터를 해제한다.
