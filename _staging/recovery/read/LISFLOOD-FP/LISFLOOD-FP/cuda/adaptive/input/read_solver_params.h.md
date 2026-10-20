---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/input/read_solver_params.h
lines: 12
sha256: c4b9cc0ff6758aede630664ceacff8a7dd78577c0b3cbd17caa8f13119c34369
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# read_solver_params.h — 판독 구간 기록

구간은 1행부터 12행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–8 | 단일 포함 지시와 정수·실수·불리언 키 판독 헤더, SolverParams 형식을 포함한다(1–7). 조건부 전처리 분기는 없다. 원문: `#pragma once` (1). |
| 9–12 | 입력 파일명을 받아 SolverParams를 반환하는 read_solver_params 원형을 선언한다(9–12). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
