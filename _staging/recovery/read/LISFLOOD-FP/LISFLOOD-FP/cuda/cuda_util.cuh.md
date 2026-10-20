---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/cuda_util.cuh
lines: 73
sha256: fb2979c0a8ccc688dd9fb27bbe2927c3b6dcf9323d76ccbe3d84741987797ab7
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# cuda_util.cuh — 판독 구간 기록

구간은 1행부터 73행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–31 | `#pragma once` (1)와 주석 처리된 cuda_runtime.h 포함(3), lis::cuda 이름공간(namespace)(5–8)이다. 전처리 조건 분기는 없다. void 반환 sync·peek(10–11)를 선언한다. CUDA 오류 코드 반환 대체 선언은 주석이다(13–15). 일반 copy(17–22)와 `template<typename T>` (24)의 copy_to_symbol(25–30)은 복사할 바이트 수 count를 받는다. |
| 32–61 | 시작 시 5·7행 lis::cuda 이름공간 안이다. size를 받는 malloc_unified·malloc_pinned·malloc_device(32–45)와 ptr를 받는 free_unified·free_pinned·free_device(47–60)를 선언한다. |
| 62–73 | 시작 시 5·7행 lis::cuda 이름공간 안이다. 현재 장치 번호 조회와 장치 속성 조회를 선언한다(62–68). 이름공간을 닫고 `#include "cuda_util.templates.cu"` (73)로 템플릿 구현을 포함한다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
