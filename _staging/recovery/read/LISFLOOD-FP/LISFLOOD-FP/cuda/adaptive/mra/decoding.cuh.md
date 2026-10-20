---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/mra/decoding.cuh
lines: 30
sha256: b52563da9597859da671dd916ed41b5f4f4cfa702591d96818b0a7676534fb6e
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# decoding.cuh — 판독 구간 기록

구간은 1행부터 30행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–19 | 단일 포함 지시와 CUDA 런타임·실행 매개변수, CUB 스캔, SolverParams·HierarchyIndex·Details·ScaleCoefficients·블록 매크로 헤더를 포함한다(1–12). 계층 시작 인덱스·부모/상세 읽기·복원·계수 저장 헤더를 포함한다(14–18). 조건부 전처리 분기는 없다. 원문: `#pragma once` (1). |
| 20–30 | SINGLE_BLOCK 불리언 템플릿의 __global__ decoding 원형이다(20–30). 유의성 배열과 Details·ScaleCoefficients·SolverParams를 값으로 받고 level·num_threads를 정수로 받는다. 원문: `template <bool SINGLE_BLOCK>` (20); `__global__` (21). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
