---
file: models/ADCIRC/raw/manuals/wiki/markdown/NOLIBF.md
lines: 106
sha256: 5d7d3f92aa1f5e8279e938cbca001e07b291da7f29191fca120643c4b5bf6cd0
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# NOLIBF.md — 판독 구간 기록

구간은 1행부터 106행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–18 | NOLIBF / Parameter Summary — NOLIBF는 2차원 수심 적분(two-dimensional depth-integrated, 2DDI) ADCIRC의 저면 응력(bottom stress) 매개화를 선택하는 필수 fort.15 입력이다(5). 3차원 실행에서도 지정해야 하지만 그 값은 무시한다(5). 표의 값·설명·세부사항·추가 입력 열 제목, 제목·판본·빈 줄을 포함한다(1–18). 원문: `NOLIBF is a parameter in the [fort.15 file](/Fort.15_file) controlling the type of bottom stress parameterization used in a 2DDI ADCIRC run. This parameter must be specified but is ignored in a 3D run. ` (5). |
| 19–40 | Parameter Summary / 값 0 — 공간적으로 일정한 선형 저면 마찰(linear bottom friction)을 사용한다(19–23). 기호 τ_b와 차원 [1/T]를 적는다(24–37). 추가 필수 입력은 FFACTOR이다(39). 원문의 값·이름·차원·LaTeX를 그대로 옮긴다. 원문: `0` (19); `linear bottom friction law` (21); `uses a spatially constant linear bottom friction, ` (23); `    {\displaystyle \tau _{b}}` (35); ` of dimensions [1/T]` (37); `[FFACTOR](/index.php?title=FFACTOR&action=edit&redlink=1)` (39). |
| 41–93 | Parameter Summary / 값 1 — 이차 저면 마찰(quadratic bottom friction)의 무차원(dimensionless) 계수 Cf는 공간적으로 일정하거나 변할 수 있다(41–57). τ_b 계산식을 제시한다(59–89). 추가 필수 입력은 FFACTOR이다(92). 수식의 분해된 마크업(markup)도 구간에 포함한다(46–90). 원문: `1` (41); `quadratic bottom friction law` (43); `can specify a spatially constant or spatially varying dimensionless coefficient, ` (45); `    {\displaystyle C_{f}}` (57); `; in which ` (59); `    {\displaystyle \tau _{b}=C_{f}\|U\|/H}` (89); `[FFACTOR](/index.php?title=FFACTOR&action=edit&redlink=1)` (92). |
| 94–101 | Parameter Summary / 값 2 — 혼합 비선형 저면 마찰(hybrid nonlinear bottom friction)을 사용한다(94–96). 심해에서는 계수가 일정하여 이차 마찰법칙이 되고 천해에서는 수심이 작아질수록 계수가 커진다(98). FFACTOR 계산식과 필수 입력 FFACTORMIN·HBREAK·FTHETA·FGAMMA를 제시한다(98–100). 원문: `2` (94); `hybrid nonlinear bottom friction law` (96); `In deep water, the friction coefficient is constant and a quadratic bottom friction law results. In shallow water the friction coefficient increases as the depth decreases (e.g. as in a Manning-type friction law). The friction coefficient is determined as: FFACTOR=FFACTORMIN*[1+(HBREAK/H)**FTHETA]**(FGAMMA/FTHETA)` (98); `[FFACTORMIN](/index.php?title=FFACTORMIN&action=edit&redlink=1), [HBREAK](/index.php?title=HBREAK&action=edit&redlink=1), [FTHETA](/index.php?title=FTHETA&action=edit&redlink=1), [FGAMMA](/index.php?title=FGAMMA&action=edit&redlink=1)` (100). |
| 102–106 | Usage Notes — 세 가지 비선형 마찰 절점 속성(nodal attribute)을 NWP에서 선택하면 NOLIBF는 반드시 1이어야 하며 다른 값이면 ADCIRC가 중단된다(104). 3차원의 공간 변화 저면 마찰은 fort.13의 bottom_roughness_length로 지정해야 한다고 적는다(106). 원문: `In the [NWP](/index.php?title=NWP&action=edit&redlink=1) section, if the user selects quadratic_friction_coefficient_at_sea_floor, mannings_n_at_sea_floor, or chezy_friction_coefficient_at_sea_floor, then NOLIBF must be 1 (nonlinear friction formulation) since all those formulations are nonlinear. If the NOLIBF were anything other than 1, it is an error that will cause ADCIRC to stop.` (104); `For 3D ADCIRC runs, spatially varying bottom friction should be specified using the [bottom_roughness_length](/Fort.13_file#Bottom_Roughness) [fort.13 file](/Fort.13_file) nodal attribute.` (106). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 89행: 수식의 `U`와 `H`는 이 파일에서 정의하지 않는다.
- 39·92·100행: FFACTOR, FFACTORMIN, HBREAK, FTHETA, FGAMMA 링크에 `action=edit&redlink=1`이 있다.
