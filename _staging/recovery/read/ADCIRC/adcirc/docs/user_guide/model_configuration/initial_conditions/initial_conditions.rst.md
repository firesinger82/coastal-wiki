---
file: models/ADCIRC/raw/source_code/adcirc/docs/user_guide/model_configuration/initial_conditions/initial_conditions.rst
lines: 37
sha256: 4f05aff2c1c6970c1528519d0a2d7adf6405eb69112d1cd65055daa98a2f7eb8
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# initial_conditions.rst — 판독 구간 기록

구간은 1행부터 37행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–13 | Initial Conditions — 메타 지시문·앵커·제목을 포함한다(1–8). 초기 조건(initial condition)은 시작 시 모델 상태를 지정하며 공간 경계에 적용하는 경계 조건과 유사하다고 설명한다(10–12). 원문: `**Initial conditions** specify the model state at start time. They are similar` (10); ``to `boundary conditions <boundary_conditions>`__, which are applied along the`` (11); `spatial boundaries.` (12). |
| 14–26 | 초기 수위의 속성·경계 조건 — 노드 속성(nodal attribute) sea_surface_height_above_geoid와 initial_river_elevation으로 초기 수위를 수정할 수 있다고 적는다(14–17). 여러 방식으로 수정하면 효과를 합산한다고 적는다(18–19). 수위 지정 경계의 sea_surface_height_above_geoid는 모의 내내 유지되므로 초기·경계 조건 모두가 될 수 있다고 적는다(19–23). 뒤 빈 행을 포함한다(24–26). 원문: ``Initial water elevations in ADCIRC can be modified using `nodal`` (14); ``attributes <nodal_attribute>`__ like`` (15); ``:ref:`sea_surface_height_above_geoid <sea_surface_height_above_geoid>` or`` (16); ``:ref:`initial_river_elevation <initial_river_elevation>`. Boundary conditions`` (17); `also affect initial water elevations. If the water elevation is modified in more` (18); `than one way, their effects are additive. Note that along elevation-specified` (19); `boundary conditions (like a tidal elevation boundary),` (20); ``:ref:`sea_surface_height_above_geoid <sea_surface_height_above_geoid>` persists`` (21); `throughout the simulation, and so it can be both an initial and a boundary` (22); `condition.` (23). |
| 27–37 | raw HTML 표 스타일 — 표 셀의 줄바꿈, 최대 폭, 자동 하이픈 속성을 지정하는 style 태그를 포함한다(27–37). 원문: `.. raw:: html` (27); `   <style>` (29); `   .wrap-table th, .wrap-table td {` (30); `     white-space: normal !important;` (31); `     word-wrap: break-word !important;` (32); `     max-width: 100% !important;` (33); `     overflow-wrap: break-word !important;` (34); `     hyphens: auto !important;` (35); `   }` (36); `   </style>` (37). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

없음
