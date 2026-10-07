---
file: models/EFDC/raw/manuals/confluence/spaces/EK/pages/EFDC_Explorer_12_Knowledge_Base/EFDC_Explorer_12_User_Guide/Model_Control_Form/Modules/Hydrodynamics_Module/General_Ocean_Turbulence_Model_GOTM.md
lines: 60
sha256: 2db9844814c7e51d8fcf424ef9df8decbf2240e91b563276cbfae399d724fefc
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# General_Ocean_Turbulence_Model_GOTM.md — 판독 구간 기록

구간은 1행부터 60행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | General Ocean Turbulence Model (GOTM) / 메타데이터 — 페이지 식별자 `2188541953` (2), 제목·space·URL·버전·갱신 시각·상위 경로와 frontmatter 구분선을 포함한다(1–9). |
| 10–17 | Introduction — 일반 해양 난류 모형(General Ocean Turbulence Model, GOTM)을 자연 수역의 수직 혼합에 관한 1차원 수층 모형으로 소개한다(12). 난류 운동에너지(turbulence kinetic energy, TKE)·길이 척도의 대수적 및 두 방정식 접근, 2차 모형과 3차원 모형 통합 사례를 설명한다(14). 공식 사이트 링크와 절 제목·빈 줄을 포함한다(10–17). 외부 사이트는 이 판독에서 열지 않았다. |
| 18–32 | GOTM turbulence models interface / 프리셋 — EEMS 12부터 GOTM 난류 폐합(turbulence closure)을 사용한다고 적는다(20). GOTM에 익숙하지 않은 사용자는 `Closure Model Presets` (22)를 선택하면 해당 모형의 모든 기본 매개변수로 입력 파일을 생성한다. 선택 원문은 `Mellor - Yamada` (24), `k - ε` (25), `k - ω` (26), `Generic` (27)이다. 구체적인 프리셋 기본값은 본문에 없다. 로컬 `GOTM_GUI_01.png`를 열었다(29). 화면은 GOTM 선택과 Mellor-Yamada 프리셋, 선택되지 않은 Customize GOTM model 체크박스를 보여 준다. 빈 줄·Figure 1 캡션을 포함한다. |
| 33–51 | Customize GOTM / 폐합·방정식 — `Customize GOTM` (33) 선택으로 옵션을 편집한다. `Turbulence Closure`의 선택은 `First-Order`, `Second-Order` (33)이며 기본은 `The *Second-Order* method is set by default` (33)이다. 1차는 TKE와 길이 척도로 확산계수를 계산한다(33). `TKE equation` (35) 선택 원문은 `Algebraic length scale equation` (37); `Differential equation for TKE (k-epsilon style)` (38); `Differential equation for q2/2 (Mellor-Yamada style` (39)이다. `Length Scale Method` (41) 선택 원문은 `Algebraic length scale equation (e.g., parabolic, triangular, etc.)` (43); `Dynamic dissipation rate equation` (44); `Dynamic Mellor-Yamada q2l equation` (45); `Generic length scale (GLS)` (46)이다. 로컬 `GOTM_GUI_02.png`를 열었다(48). 화면은 k-epsilon 프리셋, Second-Order 폐합, TKE 미분방정식과 Dynamic dissipation rate equation 선택을 보여 준다. 빈 줄·Figure 2 캡션을 포함한다. |
| 52–55 | GOTM Boundary Conditions / 매개변수 그림 — 본문은 경계조건과 Turbulence Parameters·Model Parameters·Second-Order Model 탭을 안내한다(52). 54행의 로컬 `GOTM_GUI_03.png`–`GOTM_GUI_06.png` 네 파일을 각각 열었다. 경계조건 화면에서 상·하단 `Type: Logarithmic Law of the Wall`, `TKE Equation BC: Neumann`, `Length Scale Equation BC: Neumann`을 선택한다(54, 그림 03). 난류 표의 원문 행은 `Value of the stability function in the log-law (cm0_fix, dimensionless): 0.5477`; `Turbulent Prandtl-number (Prandtl0_fix, dimensionless): 0.74`; `Constant of the wave-breaking model (cw, dimensionless): 100`; `Compute von Karman constant from model parameters: checked`; `Von Karman constant (kappa, dimensionless): 0.4`; `Compute c3 (E3 for Mellor-Yamada) from steady-state Richardson number: checked`; `Desired steady-state Richardson number (dimensionless): 0.25`; `Apply Galperin et al. (1988) length scale limitation: checked`; `Coefficient for length scale limitation (dimensionless): 0.53`; `Minimum turbulent kinetic energy (m²/s²): 1E-10`; `Minimum dissipation rate (m²/s³): 1E-12`; `Minimum buoyancy variance (m²/s⁴): 1E-10`; `Minimum buoyancy variance destruction rate: 1E-12`이다(54, 그림 04). k-epsilon 표는 `Dissipation equation ce1: 1.44`; `Dissipation equation ce2: 1.92`; `Stable stratification ce3 minus: 0`; `Unstable stratification ce3 plus: 1`; `VSchmidt number for tke diffusivity: 1`; `Schmidt number for dissipation diffusivity: 1.3`; `Wave breaking parameterisation: unchecked`이다(54, 그림 05). 2차 모형 선택은 `Second-Order method: Weak-equilibrium`; `Equation for buoyancy variance: Algebraic`; `Equation for variance destruction method: Algebraic`; `Coefficients of second-order model: Canuto et al. (2001) (version A)`이다(54, 그림 06). 계수 표는 `cc1: 5`; `cc2: 0.8`; `cc3: 1.968`; `cc4: 1.136`; `cc5: 0`; `cc6: 0.4`; `ct1: 5.95`; `ct2: 0.6`; `ct3: 1`; `ct4: 0`; `ct5: 0.3333`; `ctt: 0.72`이다(54, 그림 06). 이 값들은 그림의 표시값이며 본문이 각 값을 기본값이라고 명시하지 않는다. |
| 56–60 | GOTM turbulence models input file — EEMS 10.2부터 JSON(JavaScript Object Notation) 형식을 EFDC+ 입력에 사용하고 확장자를 JNP로 바꾸었다고 설명한다(58). GOTM 입력 원문 파일명은 `gotm\_turb.jnp` (58)이다. JSON 판독기로 표시할 수 있다고 적는다(58). 절 제목·빈 줄과 마지막 단독 `.` (60)를 포함한다. |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 39: `Differential equation for q2/2 (Mellor-Yamada style`에는 닫는 괄호가 없다.
- 52·54: Figure 3–6을 참조하지만 이 Markdown 파일에는 해당 네 그림의 번호 캡션이 없다.
- 54: Minimum buoyancy variance destruction rate 행에는 단위가 표시되어 있지 않다.
- 60: 마지막 행은 단독 마침표이다.

