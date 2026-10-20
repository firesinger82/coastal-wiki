---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/acc_nugrid/ScaleCoefficients.h
lines: 72
sha256: 5e828e2f95579f3d5966290335349f0f3b716537fb560a4fc05f5d14792c29ac
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# ScaleCoefficients.h — 판독 구간 기록

구간은 1행부터 72행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–27 | `#pragma once` (1), cuda_utils·lisflood 포함(3–4), `lis::cuda::acc_nugrid` 이름공간(namespace)(6–11). 스케일 계수(scale coefficient) 구조체(struct) ScaleCoefficients(13–14)는 활성 NUMERIC_TYPE* h·v·z0·z1x·z1y·n0(15–16·21–23·25), `bool  is_copy = false;` (26)를 보유한다. qx·qy·q3·q4·zxy 선언은 주석(17–20·24). 이 파일의 모든 구간에는 `#if` 계열 전처리 조건 분기가 없다. |
| 28–49 | 시작 시 13행 ScaleCoefficients 구조체 안. 생성자(constructor)는 num_all_elems·non_uniform_n을 받는다(28–29). `size_t bytes = sizeof(NUMERIC_TYPE) * num_all_elems;` (30). h·v·z0·z1x·z1y에 `(NUMERIC_TYPE*)malloc_device(bytes)`를 할당한다(32–33·38–40). q 계열·zxy 할당은 주석(34–37·41). `n0 = (non_uniform_n) ? (NUMERIC_TYPE*)malloc_device(bytes) : nullptr;` (43). is_copy 재설정은 주석(45). 복사 생성자(copy constructor)는 `ScaleCoefficients(const ScaleCoefficients& original) { *this = original; is_copy = true; }` (48). |
| 50–72 | 시작 시 13행 구조체 안. 소멸자(destructor)(50–51)의 `if (!is_copy)` (52)에서 h·v·z0·z1x·z1y·n0에 free_device를 호출한다(54–55·60–62·64). q 계열·zxy 해제는 주석(56–59·63). 블록·구조체·이름공간 종료와 빈 줄(65–72). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 28–46: 생성자는 배열을 할당하지만 배열 원소를 채우는 문장을 포함하지 않는다.
- 43·52–64: non_uniform_n이 거짓이면 n0는 nullptr다. 원본 소멸자는 별도 n0 조건 없이 free_device(n0)를 호출한다.
