---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/classes/Details.h
lines: 45
sha256: e10cb3ecd809fdf273d09f89ea2e0b5babb8855e7e500df87dca9b801465633f
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# Details.h — 판독 구간 기록

구간은 1행부터 45행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–22 | `#pragma once` (1), SubDetails.h·SolverTypes.h 포함(3–4). 전처리 조건 분기는 없다. Details는 eta·qx·qy·z의 0·1x·1y에 해당하는 SubDetails 멤버 12개를 보유한다(6–21). |
| 23–45 | 시작 시 6–7행 Details 구조체 안. 생성자는 num_details·solver_type을 받는다(23–27). 0계수 네 멤버는 num_details로 생성한다(29–32). 1x·1y의 모든 조건부 초기화 `eta1x( (solver_type == MWDG2) ? num_details : 0 ),`<br>`qx1x ( (solver_type == MWDG2) ? num_details : 0 ),`<br>`qy1x ( (solver_type == MWDG2) ? num_details : 0 ),`<br>`z1x  ( (solver_type == MWDG2) ? num_details : 0 ),`<br>`eta1y( (solver_type == MWDG2) ? num_details : 0 ),`<br>`qx1y ( (solver_type == MWDG2) ? num_details : 0 ),`<br>`qy1y ( (solver_type == MWDG2) ? num_details : 0 ),`<br>`z1y  ( (solver_type == MWDG2) ? num_details : 0 )` (34–42). MWDG2이면 num_details, 그 밖에는 0을 각 SubDetails 생성자에 전달한다. 본문은 비어 있다(43). MWDG2의 정의·값은 이 파일에 없다. 구조체 종료(45). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
