---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/classes/Tracer.h
lines: 32
sha256: 68157d338f680c95a706321c03980afc667042582905819ad0f25304c5836ab9
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# Tracer.h — 판독 구간 기록

구간은 1행부터 32행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–8 | `#pragma once` (1) 및 CUDA 유틸리티(utility) 헤더 포함(3). 전처리 조건 `#if _USE_TRACER == 1` (5)의 참 쪽에서 NVTX(NVIDIA Tools Extension) 헤더를 포함한다(7). |
| 9–27 | 시작 시 5행 `_USE_TRACER == 1` 전처리 참 분기 안. Tracer 생성자(constructor)는 nvtxRangePushA(label)을 호출한다(9–14). 소멸자(destructor)는 CHECK_CUDA_ERROR로 감싼 peek()와 sync()를 실행한 뒤 nvtxRangePop()을 호출한다(16–22). `#define TRACE(name) Tracer tracer(name);` (26)은 이름을 받아 tracer 지역 객체를 선언한다. |
| 28–32 | `#else` (28)는 5행 `_USE_TRACER == 1`이 성립하지 않는 컴파일 분기다. `#define TRACE(name)` (30)은 빈 확장이다. `#endif` (32)로 조건을 닫는다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 5·26–30: TRACE의 두 정의는 _USE_TRACER == 1 여부에 따라 달라진다. 대상 소스 트리의 CMakeLists.txt·config.default.cmake·makefile·*.mk 검색에서는 _USE_TRACER 정의를 찾지 못했다. 실제 빌드 값은 확인하지 않았다.
