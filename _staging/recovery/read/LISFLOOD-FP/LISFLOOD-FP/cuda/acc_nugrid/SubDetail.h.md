---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/acc_nugrid/SubDetail.h
lines: 48
sha256: 87a2222db942a846ea0dfc8f7da30a27086f7a85d23838e3102d808d61c57be4
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# SubDetail.h — 판독 구간 기록

구간은 1행부터 48행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–27 | `#pragma once` (1), CUDA·math.h·lisflood 포함(3–5), `lis::cuda::acc_nugrid` 이름공간(namespace)(7–12). SubDetail 구조체(struct)(14–15)는 NUMERIC_TYPE의 alpha_11·alpha_21·alpha_12(16–18), beta_11·beta_21·beta_12(20–22), gamma_11·gamma_21·gamma_12(24–26)를 선언한다. 필드 기본값은 없다. 이 파일의 모든 구간에는 `#if` 계열 전처리 조건 분기가 없다. |
| 28–48 | 시작 시 14행 SubDetail 구조체 안. `__device__  __forceinline__ NUMERIC_TYPE get_max()` (28). 30–31행의 이전 최대 상세계수(detail) 식은 주석이다. 활성 식은 `NUMERIC_TYPE max_detail = FMAX(FABS(alpha_11), FABS(alpha_12));` (33), `max_detail = FMAX(FABS(alpha_21), max_detail);` (34), `max_detail = FMAX(FABS(beta_11), max_detail);` (35), `max_detail = FMAX(FABS(beta_12), max_detail);` (36), `max_detail = FMAX(FABS(beta_21), max_detail);` (37), `max_detail = FMAX(FABS(gamma_11), max_detail);` (38), `max_detail = FMAX(FABS(gamma_12), max_detail);` (39), `max_detail = FMAX(FABS(gamma_21), max_detail);` (40). 아홉 필드의 절댓값 최댓값을 반환한다(42). 메서드(method)·구조체·이름공간 종료와 빈 줄(43–48). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
