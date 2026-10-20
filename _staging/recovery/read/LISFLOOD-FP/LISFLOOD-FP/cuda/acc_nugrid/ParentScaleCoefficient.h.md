---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/acc_nugrid/ParentScaleCoefficient.h
lines: 26
sha256: 364a74f096329f06b86567daba64a658b29a0868d37e1ac1094849625fc39bc3
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# ParentScaleCoefficient.h — 판독 구간 기록

구간은 1행부터 26행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–11 | `#pragma once` (1), lisflood.h 포함(3), `lis::cuda::acc_nugrid` 이름공간(namespace)(5–10), 나머지는 빈 줄. 이 파일의 모든 구간에는 `#if` 계열 전처리 조건 분기가 없다. |
| 12–26 | 부모 스케일 계수(parent scale coefficient) 구조체(struct) ParentScaleCoefficient(12–13)는 NUMERIC_TYPE z0·z1x·z1y·zxy를 선언한다(17–20). eta·qx·qy 선언은 주석(14–16). 생성자·계산식·필드 기본값은 없다. 구조체·이름공간 종료와 빈 줄(21–26). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
