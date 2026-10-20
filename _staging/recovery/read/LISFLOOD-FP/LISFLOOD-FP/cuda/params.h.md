---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/params.h
lines: 64
sha256: eb67b04a2b9a49e24808751c7d13c9b9d9812ec45849be855c0ff9104efa8a7a
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# params.h — 판독 구간 기록

구간은 1행부터 64행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–21 | `#pragma once` (1), lis 이름 공간(namespace)(2–3). SolverParams는 nodata_elevation·cfl·max_dt·DepthThresh·SpeedThresh·KrivodonovaThresh·MaxHflow·RouteSfThresh·theta·InitTstep의 NUMERIC_TYPE 필드와 routing·voutput의 int 필드를 선언한다(5–18). `SolverParams() {};` (20). 조건부 전처리 지시는 없다. |
| 22–43 | 시작 시 2행 이름 공간·5행 SolverParams 안. ::Pars·::Solver·::States 참조를 받는 생성자(22–27). nodata_elevation은 pars, cfl·DepthThresh·SpeedThresh·KrivodonovaThresh·MaxHflow·theta는 solver, routing·voutput은 states에서 복사한다(29–39). `max_dt(solver.InitTstep),` (31), `RouteSfThresh(pars.RouteSfThresh),` (37), `InitTstep(solver.InitTstep)` (40). 생성자 본문은 비어 있고 구조체를 닫는다(41–42). |
| 44–64 | PhysicalParams는 NUMERIC_TYPE g·manning을 선언한다(44–47). `PhysicalParams() {};` (49). 인수 생성자는 ::Pars·::Solver를 받아 `g(solver.g),` (57), `manning(pars.FPn)` (58)으로 복사한다. 구조체 종료·빈 줄·이름 공간 종료(60–64). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 7–20·46–49: 두 기본 생성자의 본문은 비어 있다. 필드 선언에는 기본 초기값이 없다.
- 31·40: max_dt와 InitTstep은 모두 solver.InitTstep에서 복사한다.
