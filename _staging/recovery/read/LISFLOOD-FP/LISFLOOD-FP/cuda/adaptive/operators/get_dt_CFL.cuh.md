---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/operators/get_dt_CFL.cuh
lines: 14
sha256: 0d74b0ae101e6511bebb911ca5d02b52bf6aae0ab12bd70220d0065d0ec581c8
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# get_dt_CFL.cuh — 판독 구간 기록

구간은 1행부터 14행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|

| 1–8 | `#pragma once`와 CUB 장치 축약(reduction)·CUDA 유틸리티·실수 형식 헤더를 포함한다(1–7). 전처리 조건 분기는 없다. 원문: `#pragma once` (1). |
| 9–14 | CUDA 호스트 함수(host function) `get_dt_CFL`을 선언한다(9–14). 장치 CFL(Courant–Friedrichs–Lewy) 배열 포인터의 참조와 상수 정수 해 길이 참조를 받고 real을 반환한다(10–13). 실행 본문과 기본 인수는 없다. 원문: `__host__` (9). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
