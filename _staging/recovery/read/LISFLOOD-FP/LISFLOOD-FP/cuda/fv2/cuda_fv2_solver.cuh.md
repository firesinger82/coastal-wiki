---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/fv2/cuda_fv2_solver.cuh
lines: 77
sha256: 10ca924a1bcc4fd04563872414113614655ef4cf45e82972e5bdae2a37145a7d
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# cuda_fv2_solver.cuh — 판독 구간 기록

구간은 1행부터 77행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–18 | `#pragma once` (1), FV2 지형·흐름·기울기 제한(slope limiting)·공통 Solver 헤더 포함(2–5). lis::cuda::fv2 이름 공간(namespace)(7–12). `extern __managed__ NUMERIC_TYPE maxH;` (14). `class Solver : public cuda::Solver<Flow>` (16)를 연다. 조건부 전처리 지시는 없다. |
| 19–54 | 시작 시 7·9·11행 이름 공간·16행 클래스 public 구역 안. 생성자는 Flow·DeviceTopography·Geometry·PhysicalParams 참조, manning 포인터, bool limit_slopes, dim3 grid_size를 받는다(19–28). 범람원(floodplain) 유량·얕은 수심 기울기 처리·고스트 셀(ghost cell) 초기화·갱신·균일 강우·최대값 갱신·흐름 갱신·d_U·const 시간 간격 갱신·소멸자를 선언한다(30–53). |
| 55–77 | 시작 시 7·9·11행 이름 공간·16행 클래스 안. private update_ghost_cells는 Flow 참조를 받는다(55–59). U1·Ux·Uint, Uold 참조, DeviceTopography 참조, manning 포인터, Slopes·MaxH·bool friction을 보관한다(62–70). 기본값은 `bool limit_slopes = false;` (71). const dim3 grid_size 선언(72) 뒤 클래스·이름 공간을 닫는다(73–77). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
