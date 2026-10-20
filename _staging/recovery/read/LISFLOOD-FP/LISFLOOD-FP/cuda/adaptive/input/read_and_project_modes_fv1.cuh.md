---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/input/read_and_project_modes_fv1.cuh
lines: 18
sha256: 334136be4e99858850e9f74e4160582da2084d5becd0438d3648ee867a1d17e3
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# read_and_project_modes_fv1.cuh — 판독 구간 기록

구간은 1행부터 18행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–10 | `#pragma once` (1) 뒤 CUDA 유틸리티(utility)·AssembledSolution·SolverParams·래스터(raster) 판독·문자열 키 판독 헤더를 포함한다(3–9). 전처리 조건 분기는 없다. |
| 11–18 | `__host__` (11)로 호스트 함수(host function) read_and_project_modes_fv1를 선언한다(12–18). 입력 파일명 포인터와 조립 해(assembled solution)·격자 크기·해법 매개변수의 const 참조를 받는다(14–17). 함수 본문은 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
