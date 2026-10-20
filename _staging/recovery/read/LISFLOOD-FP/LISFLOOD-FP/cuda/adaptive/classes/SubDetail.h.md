---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/classes/SubDetail.h
lines: 44
sha256: fc3885304949d5b809a2ce18ced64cbb49e31a4e862f552eb3404cfccd223970
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# SubDetail.h — 판독 구간 기록

구간은 1행부터 44행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | `#pragma once` (1) 뒤 CUDA 실행시간(runtime)·수학·실수형 헤더를 포함한다(3–7). 전처리 조건 분기는 없다. |
| 10–27 | SubDetailHW는 `real`형 alpha·beta·gamma 상세 계수(detail coefficient)를 보유한다(10–14). 장치 함수(device function) 선언은 `__device__  __forceinline__ real get_max()` (16). `real max_detail = C(0.0);` (18) 뒤 `max_detail = max( abs(alpha), abs(beta) );` (20)와 `max_detail = max( abs(gamma), max_detail);` (21)로 절댓값 최댓값을 계산하여 반환한다(23). 구조체 종료와 빈 줄(24–27). |
| 28–44 | SubDetailMW는 SubDetailHW형 `_0`·`_1x`·`_1y`를 보유한다(28–32). 장치 함수 선언은 `__device__  __forceinline__ real get_max()` (34). `real max_detail = C(0.0);` (36) 뒤 `max_detail = max( _0.get_max(), _1x.get_max() );` (38)와 `max_detail = max(_1y.get_max(), max_detail);` (39)로 세 하위 묶음의 최댓값을 계산하여 반환한다(41). 메서드와 구조체 종료(42–44). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
