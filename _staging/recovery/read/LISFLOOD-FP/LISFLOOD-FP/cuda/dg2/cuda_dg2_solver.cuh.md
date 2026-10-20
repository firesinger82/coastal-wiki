---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/dg2/cuda_dg2_solver.cuh
lines: 88
sha256: 349b1dfa558ee68b9c8ba29347596f877f7b8d5f590447c4c335c5b6252ed5eb
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# cuda_dg2_solver.cuh — 판독 구간 기록

구간은 1행부터 88행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–15 | `#pragma once` (1), DG2 지형·흐름·기울기 제한(slope limiting)·공통 solver 헤더를 포함한다(2–5). 전처리 조건 분기는 없다. lis::cuda::dg2 이름공간(namespace)을 연다(7–12). 최대 수심의 관리 메모리(managed memory) 선언은 `extern __managed__ NUMERIC_TYPE maxH;` (14)이다. |
| 16–55 | `class Solver : public cuda::Solver<Flow>` (16)의 생성자는 Flow·DeviceTopography·Manning 포인터·기하·PhysicalParams·limit_slopes·grid_size를 받는다(19–28). 범람원(floodplain) 유량·가상 셀(ghost cell) 초기화/갱신·균일 강우(uniform rain)·얕은 수심 기울기·ACC 최대장·흐름 변수·장치 상태 참조·셀별 시간 간격과 소멸자를 선언한다(30–54). update_dt_per_element는 const 함수이다(49–52). |
| 56–88 | 시작 시 16행 Solver 클래스 안이다. private update_ghost_cells·zero_thin_depth_slopes는 Flow를 받으며, zero_perimeter_slopes는 DEM·Flow를 받는다(57–71). U1·Ux·Uint와 Uold 참조, DEM 참조, Manning 포인터, Slopes, MaxH, friction, `bool limit_slopes = false;` (82), const grid_size를 보유한다(73–83). 클래스·이름공간을 닫는다(84–88). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
