---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/classes/ParentScaleCoeffs.h
lines: 20
sha256: ac5d53d204850d7b27a938468a7f858754ac834dc852be0d742f9ca062a8978a
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# ParentScaleCoeffs.h — 판독 구간 기록

구간은 1행부터 20행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–13 | `#pragma once` (1), real.h 포함(3). 전처리 조건 분기는 없다. ParentScaleCoeffsHW는 real eta·qx·qy·z를 보유한다(5–12). 초기값·실행 메서드는 없다. |
| 14–20 | ParentScaleCoeffsMW는 ParentScaleCoeffsHW 형식의 _0·_1x·_1y를 보유한다(14–20). 초기값·실행 메서드는 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
