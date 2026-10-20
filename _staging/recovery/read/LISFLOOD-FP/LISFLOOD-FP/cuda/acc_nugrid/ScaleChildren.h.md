---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/acc_nugrid/ScaleChildren.h
lines: 24
sha256: a7e4f61e8bf8b3c011c0fc97b1cb7d8586fd1fd802031bfc42c7d8b32b9330a7
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# ScaleChildren.h — 판독 구간 기록

구간은 1행부터 24행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–12 | `#pragma once` (1), cuda_runtime.h·lisflood.h 포함(3–4), `lis::cuda::acc_nugrid` 이름공간(namespace)(6–11), 나머지는 빈 줄. 이 파일의 모든 구간에는 `#if` 계열 전처리 조건 분기가 없다. |
| 13–24 | ScaleChildren 구조체(struct)(13–14)는 자식 스케일 계수(child scale coefficient) NUMERIC_TYPE child_0·child_1·child_2·child_3를 선언한다(15–18). 생성자·계산식·필드 기본값은 없다. 구조체·이름공간 종료와 빈 줄(19–24). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
