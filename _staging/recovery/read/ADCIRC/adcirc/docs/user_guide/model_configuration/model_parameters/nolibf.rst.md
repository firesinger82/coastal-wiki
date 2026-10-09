---
file: models/ADCIRC/raw/source_code/adcirc/docs/user_guide/model_configuration/model_parameters/nolibf.rst
lines: 55
sha256: d5c9f7c28363454175f06e4b864b186987fffc2c96ab46bc791317a09ed53dc4
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# nolibf.rst — 판독 구간 기록

구간은 1행부터 55행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–19 | NOLIBF / Parameter Summary — 메타데이터·앵커·제목을 포함한다(1–8). 2DDI의 저면 응력(bottom stress) 매개화를 선택하며 3D에서는 명시해야 하지만 무시된다는 조건을 옮긴다(10–12). 표 안내를 포함한다(14–18). 원문: `` **NOLIBF** is a parameter in the :ref:`fort.15 file <fort15>` controlling the `` (10); ` type of bottom stress parameterization used in a 2DDI ADCIRC run. This parameter ` (11); ` must be specified but is ignored in a 3D run. ` (12). |
| 20–41 | Parameter Summary / 표 — NOLIBF=0 선형 마찰(linear friction), 1 이차 마찰(quadratic friction), 2 혼합 비선형 마찰(hybrid nonlinear friction)의 이름·식·필수 입력을 행마다 옮긴다(25–40). 선형 계수 단위 [1/T], 무차원 C_f와 tau_b 식, FFACTOR 혼합식을 그대로 유지한다. 원문: ` .. list-table:: ` (20); `    :header-rows: 1 ` (21); `    :widths: 10 20 50 20 ` (22); `    :class: wrap-table ` (23); `    * - NOLIBF Value ` (25); `      - Description ` (26); `      - Details ` (27); `      - Other Required Inputs ` (28); `    * - 0 ` (29); `      - linear bottom friction law ` (30); ``      - uses a spatially constant linear bottom friction, :math:`\tau_b` of dimensions [1/T] `` (31); ``      - `FFACTOR <FFACTOR>`__ `` (32); `    * - 1 ` (33); `      - quadratic bottom friction law ` (34); ``      - can specify a spatially constant or spatially varying dimensionless coefficient, :math:`C_f`; in which :math:`\tau_b = C_f\|U\|/H` `` (35); ``      - `FFACTOR <FFACTOR>`__ `` (36); `    * - 2 ` (37); `      - hybrid nonlinear bottom friction law ` (38); `      - In deep water, the friction coefficient is constant and a quadratic bottom friction law results. In shallow water the friction coefficient increases as the depth decreases (e.g. as in a Manning-type friction law). The friction coefficient is determined as: FFACTOR =FFACTORMIN*[1+(HBREAK/H)**FTHETA]**(FGAMMA/FTHETA) ` (39); ``      - `FFACTORMIN <FFACTORMIN>`__, `HBREAK <HBREAK>`__, `FTHETA <FTHETA>`__, `FGAMMA <FGAMMA>`__ `` (40). |
| 42–55 | Usage Notes — NWP에서 이차 마찰·Manning·Chézy 절점 속성을 선택하면 NOLIBF=1이어야 한다는 조건과 다른 값에서 ADCIRC가 중지된다는 원문을 옮긴다(47–51). 3D 공간 마찰은 bottom_roughness_length 속성으로 지정해야 한다는 권고를 옮기고 마지막 빈 줄을 포함한다(53–55). 원문: `` In the :ref:`NWP <nwp>` section, if the user selects `` (47); ` quadratic_friction_coefficient_at_sea_floor, mannings_n_at_sea_floor, or ` (48); ` chezy_friction_coefficient_at_sea_floor, then NOLIBF must be 1 (nonlinear ` (49); ` friction formulation) since all those formulations are nonlinear. If the NOLIBF ` (50); ` were anything other than 1, it is an error that will cause ADCIRC to stop. ` (51); ` For 3D ADCIRC runs, spatially varying bottom friction should be specified using ` (53); `` the :ref:`bottom_roughness_length <bottom_roughness_length>` nodal attribute. `` (54). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

없음
