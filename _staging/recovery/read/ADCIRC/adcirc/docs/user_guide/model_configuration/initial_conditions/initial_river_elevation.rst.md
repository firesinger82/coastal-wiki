---
file: models/ADCIRC/raw/source_code/adcirc/docs/user_guide/model_configuration/initial_conditions/initial_river_elevation.rst
lines: 16
sha256: b1b02bcebb1918712a9d8968e7e6f50eb9fd8f5bff38fbe3c24e97619a868834
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# initial_river_elevation.rst — 판독 구간 기록

구간은 1행부터 16행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–7 | Initial River Elevation — 앵커·제목을 포함한다(1–4). initial_river_elevation은 지정 노드의 초기 수면 고도를 설정한다(6). 수위 지정 경계의 이 속성 값은 모의 시작 이후 유지되지 않는다(6). 두 수위 속성을 모두 지정하면 합을 사용한다(6). 주어진 노드 값이 0보다 큰 경우만 현재 적용한다고 적으며 괄호 안에 depth less than zero를 적는다(6). 원문: ``The :ref:`initial_river_elevation` nodal attribute is used to set the initial water surface elevation at specified nodes. This attribute is functionally identical to the :ref:`sea_surface_height_above_geoid` attribute, except that any values assigned to elevation-specified boundary conditions in this attribute **do not** persist after the start of the simulation. As a result, this attribute is more appropriate for initializing rivers. If both attributes are specified, then the assigned elevation is their sum. Currently, this attribute is only applied if the value supplied at a given node is above zero (i.e. depth less than zero). From cstart.F:`` (6). |
| 8–15 | cstart.F 코드 예제 — `where` 조건, eta2 합산식, `end where` 및 뒤 빈 행을 포함한다(8–15). 코드의 부등호와 상수·변수 이름을 그대로 옮긴다(10–12). 원문: `   .. code-block:: ` (8); `      where (River_et_WSE.GT.0.d0)` (10); `         eta2 = eta2 + River_et_WSE` (11); `      end where` (12). |
| 16–16 | cold start의 하천 수위 — ADCIRC는 기본적으로 음의 수심인 정점을 시작 시 마른 것으로 가정한다고 적는다(16). 평균 해수면 위 하상의 내륙 하천에서는 이 가정이 해당하지 않는다고 설명한다(16). 이 속성은 콜드 스타트(cold start) 초기 하천 수위를 제공하며 보통 내륙 경계의 플럭스 또는 수위 경계 조건과 함께 사용한다고 적는다(16). 원문: ``ADCIRC assumes by default that vertices with negative depths will be dry when the simulation starts. This is, of course, not the case for an inland river whose bed is above mean sea level. This nodal attribute is used in those cases to provide the initial water surface elevation of the river at cold start, and is typically used in conjunction with a flux or elevation :ref:`boundary condition <boundary_conditions>` at the inland boundary. See also :ref:`initial conditions <initial_conditions>`.   `` (16). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

없음
