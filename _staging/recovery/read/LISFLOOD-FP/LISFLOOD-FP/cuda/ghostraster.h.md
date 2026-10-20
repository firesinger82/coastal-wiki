---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/ghostraster.h
lines: 22
sha256: 7301bb682e584268b6518f0c05cf6c4488fe69f94a8bc59382020542658b8d69
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# ghostraster.h — 판독 구간 기록

구간은 1행부터 22행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | `#pragma once` (1), LISFLOOD·geometry 헤더 포함(2–3), lis 이름 공간(namespace)(5–6)과 GhostRaster 구조체(8–9). 조건부 전처리 지시는 없다. |
| 10–22 | 시작 시 5행 이름 공간·8행 구조체 안. 모든 메서드는 static이며 Geometry 참조를 받는다. elements·elements_H·elements_Q, pitch·offset, pitch_ACC·offset_ACC는 int를 반환한다(10–16). allocate·allocate_H는 NUMERIC_TYPE*를 반환한다(17–18). 구조체·이름 공간 종료와 빈 줄(19–22). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
