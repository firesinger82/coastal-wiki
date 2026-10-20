---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/mra/decoding_all.cuh
lines: 16
sha256: 1e924eb675ada5567a98236dcab26fcd418335b9e0fa56892c0731f2dfd1e476
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# decoding_all.cuh — 판독 구간 기록

구간은 1행부터 16행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–8 | 단일 포함 지시와 블록 수 계산·CUDA 유틸리티·decoding·extra_significance 헤더를 포함한다(1–7). 조건부 전처리 분기는 없다. 원문: `#pragma once` (1). |
| 9–16 | 유의성·정규화 상세 배열 포인터와 Details·ScaleCoefficients·SolverParams 참조를 받는 void decoding_all 원형을 선언한다(9–16). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
