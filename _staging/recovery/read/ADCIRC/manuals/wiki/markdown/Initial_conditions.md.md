---
file: models/ADCIRC/raw/manuals/wiki/markdown/Initial_conditions.md
lines: 7
sha256: 5d5f20568de1a0687fb2599276a70bcf2509349c05de4c838ed078e808d7ed9a
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# Initial_conditions.md — 판독 구간 기록

구간은 1행부터 7행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–7 | Initial conditions — 초기조건(initial conditions)은 시작 시각의 모델 상태를 지정한다(5). 경계조건(boundary conditions)은 공간 경계에 적용된다고 설명한다(5). 초기 수위는 절점 속성과 경계조건으로 수정할 수 있다(7). 둘 이상으로 수정하면 효과는 합산된다고 적는다(7). 수위 지정 경계에서는 sea_surface_height_above_geoid가 모의 전체에 지속되어 초기조건과 경계조건 모두가 될 수 있다(7). 제목·판본·빈 줄을 포함한다(1–7). 원문: ``Initial water elevations in ADCIRC can be modified using [nodal attributes](/Nodal_attribute) like `[sea_surface_height_above_geoid](/Sea_surface_height_above_geoid)` or `[initial_river_elevation](/Initial_river_elevation)`.  Boundary conditions also affect initial water elevations.  If the water elevation is modified in more than one way, their effects are additive.  Note that along elevation-specified boundary conditions (like a tidal elevation boundary), `sea_surface_height_above_geoid` persists throughout the simulation, and so it can be both an initial and a boundary condition.`` (7). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 7행: `sea_surface_height_above_geoid`와 `initial_river_elevation`의 Markdown 링크 표기가 백틱 내부에 있다.
