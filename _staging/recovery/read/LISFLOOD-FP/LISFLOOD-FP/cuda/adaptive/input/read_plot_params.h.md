---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/input/read_plot_params.h
lines: 11
sha256: 385fcd8cafdcf2df1ebacd7b7fafb75da3eb9148f1f9706113f86fce63fa1d66
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# read_plot_params.h — 판독 구간 기록

구간은 1행부터 11행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–7 | 단일 포함 지시와 빈 줄이다. 불리언(boolean)·문자열 키 판독 헤더와 PlottingParams 형식을 포함한다(3–6). 조건부 전처리 분기는 없다. 원문: `#pragma once` (1). |
| 8–11 | 입력 파일명 포인터를 받아 PlottingParams를 반환하는 read_plot_params 원형(prototype)만 선언한다(8–11). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
