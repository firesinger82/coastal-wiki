---
file: models/EFDC/raw/manuals/confluence/spaces/EK/pages/EFDC_Explorer_12_Knowledge_Base/EFDC_Explorer_12_User_Guide/Model_Control_Form/Modules/Dye.md
lines: 38
sha256: 15a236fff8264eceaba367db5e058e02767e6d123eec4d7cf7783873d9f6c214
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Dye.md — 판독 구간 기록

구간은 1행부터 38행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | Dye / 메타데이터 — 페이지 식별자 `240222322` (2), 제목·space·URL·버전·갱신 시각·상위 경로와 frontmatter 구분선을 포함한다(1–9). |
| 10–15 | Activate the Dye Module — CSS·절 제목·빈 줄과 EFDC+ Modules에서 염료(dye) 모듈을 활성화하는 설명을 포함한다(10–15). 로컬 `d1.png`를 열었다(14). 화면은 Dye 체크박스를 선택한 모듈 설정을 보여 준다. |
| 16–29 | Settings / 클래스·감소·초기조건 — `Number of Dye Classes` (18)로 임의 수의 클래스를 설정하며 EE10 이전에는 모형별 한 클래스만 가능했다고 적는다(18). `ID`, `Type` (20)를 지정한다. 보존성 염료(conservative dye)의 원문은 `Conservative Dye` (22); `so that the dye will not decay.` (22); `All values will be initialized as zero` (22)이다. 사용자는 초기농도를 설정할 수 있다(22). 비보존성 염료(non-conservative dye) 설정 원문은 `either in first-order or linearly (0th order)` (23); `default value of 0th-order decay to one for all options available.` (23); `Setting a negative value will lead to growth.` (23); `1st-order decay rates, temperature adjustment co-efficient, reference temperature, settling velocity`, `initial concentration of the dye` (23)이다. 수령(age of water) 옵션의 원문은 `Age of Water (days)` (24); `the 0th-order decay flag is set to -1` (24); `All other columns will be zero in this option.` (24)이다. `IC Flag` (26)가 체크되어 있으면 `Initial Concentration` (26), 체크되어 있지 않으면 Spatially Varying Conditions 값을 쓴다. 로컬 `5-17-2019_10-06-03_AM.jpg`를 열었다(28). Age 행은 `ID Age`; `Type Age of Water`; `Units days`; `0th-order Decay Rate (1/day) -1.00000`; `1st-order Decay Rate (1/day) 0.00000`; `Temperature Adjustment Co-efficient 0.00`; `Reference Temperature (°C) 0.00`; `Settling Velocity (m/day) 0.000E0`; `Initial Concentration 0.000`; `IC Flag unchecked`를 표시한다(28, 그림). |
| 30–35 | Initial Conditions — Assign으로 공간 가변 초기조건을 설정한다(32). 로컬 `d2.png`를 열었다(34). 빨간 화살표는 Initial Water Column Dye Concentrations 화면에서 Apply Cell Properties: Dye 화면으로 향한다. 오른쪽 화면은 격자·층·클래스·상수/산포자료(scatter data)/프로파일과 보간 선택을 보여 준다. 절 제목·빈 줄을 포함한다. |
| 36–38 | Visualization — 2DH·2DV 보기, 시계열, 수직·종단 프로파일 표시 방법은 Salinity Visualization 설명과 같다고 적는다(38). 절 제목·빈 줄을 포함한다. |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 12·18·32: 본문은 Figure 1–3 앵커를 참조하지만 이 Markdown 파일에는 해당 번호 캡션이나 앵커 선언이 없다.
- 23·24·28: 본문은 0차 감소의 `decay` 및 `flag`를 사용한다. 그림 표 열은 `0th-order Decay Rate (1/day)`라고 적는다.

