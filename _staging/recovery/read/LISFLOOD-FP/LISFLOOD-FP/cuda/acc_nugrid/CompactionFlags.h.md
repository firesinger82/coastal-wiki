---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/acc_nugrid/CompactionFlags.h
lines: 41
sha256: bce13780bc374979d80aced2d6ae50233dc38e73310af063cf924ace9e0dfe88
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# CompactionFlags.h — 판독 구간 기록

구간은 1행부터 41행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–17 | `#pragma once` (1), cuda_utils.cuh 포함(3), `lis::cuda::acc_nugrid` 이름공간(namespace)(5–10). 구조체(struct) CompactionFlags(12–13)는 bool* north_east·south_west(14–15), `bool  is_copy = false;` (16)를 보유한다. 이 파일의 모든 구간에는 `#if` 계열 전처리 조건 분기가 없다. |
| 18–27 | 시작 시 12행 CompactionFlags 구조체 안. 생성자(constructor)는 num_finest_elems를 받고(18–19), `size_t bytes = sizeof(bool) * num_finest_elems;` (20), `north_east = (bool*)malloc_device(bytes);` (22), `south_west = (bool*)malloc_device(bytes);` (23)를 실행한다. `CompactionFlags(const CompactionFlags& original) { *this = original; is_copy = true; }` (26)는 복사 생성자(copy constructor)다. 25·27행은 빈 줄. |
| 28–41 | 시작 시 12행 구조체 안. 소멸자(destructor)(28–29)의 `if (!is_copy)` (30)에서 free_device(north_east)·free_device(south_west)를 호출한다(32–33). 블록·구조체·이름공간 종료와 빈 줄(34–41). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 18–24: 생성자는 두 bool 배열을 할당하지만 원소 값을 설정하는 문장을 포함하지 않는다.
