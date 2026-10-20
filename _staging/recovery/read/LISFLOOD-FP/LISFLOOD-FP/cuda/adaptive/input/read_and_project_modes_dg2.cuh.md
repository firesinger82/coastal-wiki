---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/input/read_and_project_modes_dg2.cuh
lines: 22
sha256: a5edf1be73aad8744e265ab90af1221d20448a9416413479adf2db2888f531d3
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# read_and_project_modes_dg2.cuh — 판독 구간 기록

구간은 1행부터 22행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–12 | `#pragma once` (1) 뒤 CUDA 유틸리티(utility)·SimulationParams·래스터(raster) 판독·문자열 키 판독·블록 수 계산·모드 투영(modal projection) 헤더를 포함한다(3–11). 전처리 조건 분기는 없다. |
| 13–22 | `__host__` (13)로 호스트 함수(host function) read_and_project_modes_dg2를 선언한다(14–22). 매개변수는 const char* 입력 파일명과 AssembledSolution·NodalValues·SimulationParams·SolverParams·int 격자 크기의 const 참조다(16–21). 함수 본문은 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
