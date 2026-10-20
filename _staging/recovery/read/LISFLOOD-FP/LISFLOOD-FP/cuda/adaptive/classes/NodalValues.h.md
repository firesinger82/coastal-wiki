---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/classes/NodalValues.h
lines: 38
sha256: 819ae202ae9681fec171a8313254b3758eb509736e4e9ba53be717475ab1fded
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# NodalValues.h — 판독 구간 기록

구간은 1행부터 38행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–24 | `#pragma once` (1), CUDA 유틸리티·real.h 포함(3–5). 전처리 조건 분기는 없다. NodalValues는 real* h·qx·qy·z와 is_copy_cuda=false를 보유한다(7–13). 생성자의 바이트 식 `size_t bytes = sizeof(real) * interface_dim * interface_dim;` (17). 네 배열에 malloc_device를 호출한다(19–22). |
| 25–38 | 시작 시 7–8행 NodalValues 구조체 안. 복사 생성자는 *this=original 뒤 is_copy_cuda=true(25). 소멸자의 `if (!is_copy_cuda)` (29)일 때 `CHECK_CUDA_ERROR( free_device(h)  );`<br>`CHECK_CUDA_ERROR( free_device(qx) );`<br>`CHECK_CUDA_ERROR( free_device(qy) );`<br>`CHECK_CUDA_ERROR( free_device(z)  );` (31–34)로 네 배열을 해제한다. 소멸자·구조체 종료(35–38). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 15–23: 생성자는 장치 배열 네 개를 할당하지만 원소 값을 초기화하는 문장은 없다.
