---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/classes/CompactionFlags.h
lines: 30
sha256: 54d9259336baa34336bd1b2e4a5dfadb8122d23de4fa9dd15c0f4f64b5b42035
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# CompactionFlags.h — 판독 구간 기록

구간은 1행부터 30행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–18 | `#pragma once` (1), CUDA 유틸리티 포함(3). 전처리 조건 분기는 없다. CompactionFlags는 bool* north_east·south_west와 is_copy_cuda=false를 보유한다(5–9). 생성자의 바이트 식 `size_t bytes = sizeof(bool) * num_finest_elems;` (13). 두 포인터를 malloc_device로 할당한다(15–16). |
| 19–30 | 시작 시 5–6행 CompactionFlags 구조체 안. 복사 생성자는 *this=original 뒤 is_copy_cuda=true로 설정한다(19). 소멸자의 `if (!is_copy_cuda)` (23)이면 `CHECK_CUDA_ERROR( free_device(north_east) );`<br>`CHECK_CUDA_ERROR( free_device(south_west) );` (25–26)으로 두 포인터를 해제한다. 메서드·구조체 종료(27–30). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 11–17: 생성자는 두 bool 장치 배열을 할당하지만 원소 값을 초기화하는 문장은 없다.
