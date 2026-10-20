---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/acc/cuda_acc_solver.cuh
lines: 83
sha256: ae28aeff75ab39cc9809f142ab6101be461b303fcfdd475e389fd93dbebae046
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# cuda_acc_solver.cuh — 판독 구간 기록

구간은 1행부터 83행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–21 | `#pragma once` (1), lisflood·params·stats·Flow·sample·기반 Solver·MaxH 헤더 포함(2–8), `lis::cuda::acc` 이름공간(namespace) 시작(10–15). 이 파일의 모든 구간에는 `#if` 계열 전처리 조건 분기가 없다. 통합 메모리(managed memory) 외부 선언은 `extern __managed__ NUMERIC_TYPE maxH;` (17), `extern __managed__ NUMERIC_TYPE totalHtm;` (18), `extern __managed__ NUMERIC_TYPE maxHtm;` (19), `extern __managed__ NUMERIC_TYPE initHtm;` (20). |
| 22–60 | `class Solver : public cuda::Solver<Flow>` (22)는 Flow 템플릿(template) 기반 클래스를 상속한다. 공개 생성자 인수는 Flow&·DEM·manning·Geometry&·PhysicalParams&·dim3(25–33). FloodplainQ·zero_thin_depth_slopes·zero_ghost_cells·update_ghost_cells·update_uniform_rain·updateMaxFieldACC를 선언한다(35–45). update_flow_variables는 MassStats*를 받아 Flow&를 반환한다(47–50). d_U도 Flow&를 반환한다(52). update_dt_per_element는 NUMERIC_TYPE*를 받는 const 메서드(method)다(54–57). 소멸자(destructor) 선언과 빈 줄(59–60). 본문·기본 인수값은 없다. |
| 61–83 | 시작 시 22행 Solver 클래스 안. private 멤버는 Flow U1(62), Flow& Uold·U(65–66), DEM·manning 포인터(67–68), MaxH maxH(71), bool friction(73), const dim3 grid_size(74). U2 선언은 주석(63). 클래스 종료(75), 빈 줄(76–80), 이름공간 종료(81–83). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
