---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/classes/FinestGrid.h
lines: 39
sha256: 57d8160de16fd54ea48ad1fe99fde42e2feec515a0185216bb2d7faba02ed7b1
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# FinestGrid.h — 판독 구간 기록

구간은 1행부터 39행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–25 | `#pragma once` (1), CUDA 유틸리티·real.h 포함(3–5). 전처리 조건 분기는 없다. FinestGrid는 real* h·qx·qy·z와 is_copy_cuda=false를 보유한다(7–14). 생성자의 바이트 수 `size_t bytes = sizeof(real) * num_finest_elems;` (18). 네 포인터에 malloc_pinned를 호출한다(20–23). |
| 26–39 | 시작 시 7–8행 FinestGrid 구조체 안. 복사 생성자는 *this=original 뒤 is_copy_cuda=true(26). 소멸자의 `if (!is_copy_cuda)` (30) 안에서 페이지 고정(pinned) 메모리 해제 루틴을 호출한다. 호출 전체 `CHECK_CUDA_ERROR( free_pinned(h)  );`<br>`CHECK_CUDA_ERROR( free_pinned(qx) );`<br>`CHECK_CUDA_ERROR( free_pinned(qy) );`<br>`CHECK_CUDA_ERROR( free_pinned(z)  );` (32–35). 소멸자·구조체 종료(36–39). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 16–24: 생성자는 네 배열에 malloc_pinned를 호출하지만 원소 값을 초기화하는 문장은 없다.
