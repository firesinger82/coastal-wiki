---
file: models/EFDC/raw/manuals/confluence/spaces/EK/pages/EFDC_Explorer_12_Knowledge_Base/EFDC_Explorer_12_User_Guide/Model_Control_Form/Modules/Temperature.md
lines: 37
sha256: 9c5f19c0d8f33bcbdb9acb922347e8e0b68838499e82a5cf474a3da8c0db778a
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Temperature.md — 판독 구간 기록

구간은 1행부터 37행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | 문서 메타데이터. Temperature의 식별자·제목·space·URL·버전·갱신 시각·계층 경로가 있다 (2–8). |
| 10–15 | Activate the Temperature Module. 제목 앞에 색상 CSS가 있다 (10). EFDC+ Modules에서 Temperature를 활성화한다 (12). 14행 그림은 Temperature 선택 상자를 강조한 모듈 화면이다. Model Selection은 Use EFDC+ Model이며 수송 옵션은 `Upwind Difference; Anti-Diffusion Correction; Flux Limitation` (14행 그림)이다. |
| 16–31 | Settings. Temperature 우클릭으로 Settings·Initial Conditions·Time Series를 선택한다 (18). 20행 그림은 그 메뉴와 요약 화면이다. 표시값은 `Equilibrium Temp (CE-QUAL-W2 Method)` (20행 그림); `Atmospheric: 0; Mean: 22.23 °C; Min: 22.23 °C; Max: 22.23 °C; Temperature Time-series: 1` (20행 그림)이다. 본문은 다섯 탭 `Surface Heat Exchange` (24); `Initial Conditions` (25); `Boundary Condition` (26); `Ice` (27); `General` (28)을 연결한다 (22–28). 30행 그림은 Surface Heat Exchange 설정 화면이다. 표시값은 `Surface Heat Exchange Sub-model: Equilibrium Temp (CE-QUAL-W2 Method)` (30행 그림); `Minimum Fraction Absorbed in the Top Layer: 0.3` (30행 그림); `Light Extinction Coefficients in Units of 1/m per g/m³ Unless Otherwise Specified (EFDC+)` (30행 그림); `Background: 0.5 (1/m)` (30행 그림); `Light Extinction for TSS: 0.052` (30행 그림); `Coefficient for DOM: 0` (30행 그림); `Coefficient for POC: 1` (30행 그림); `Coefficient for Chl-a: 0.031` (30행 그림); `Chl-a Exponent: 1` (30행 그림)이다. |
| 32–37 | Initial Conditions. 수온을 상수 또는 공간별 값으로 지정하고 층을 선택한다 (34). XYZ·수직 프로필 자료와 역거리 가중(Inverse Distance Weighting, IDW) 보간 옵션을 설명한다 (34). 초기 저상 온도는 `Uniform Bed Temperature` (35)또는 `Use Spatially Variable Bed Temp and Thickness` (35)로 설정한다. 37행 첫 그림은 초기 조건 폼이며 `Const./Avg. Value: 20.000` (37행 그림); `Uniform Bed Temperature (°C): 0` (37행 그림); `Uniform Thermal Thickness (m): 1` (37행 그림)이다. 두 공간 변동 상자는 미선택이다. 둘째 그림은 Assign에서 Apply Cell Properties: Temp로 향하는 빨간 화살표를 보여 준다. `All grid cells; For All Layers; Constant: 0; Replacement` (37행 그림); `For A Specific Layer: 1` (37행 그림)이며 특정 층 선택은 미선택이다. 셋째 그림은 저상 온도 공간 변동 상자를 선택하고 Bed Temp에서 Apply Cell Properties: Bed Temperature를 연 화면이다. `All grid cells; Constant: 0; Centroid Interp.` (37행 그림)가 선택되며, 대안은 Scatter (XYZ) data·Avg. Value·Max. Value·Min. Value이다. 폴리곤 및 자료 목록은 비어 있다 (37행 그림). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 절 제목 앞에 색상 CSS가 남아 있다 (10).
- Figure 2 링크가 `http://eemodelingsystem.atlassian.net#Figure 1`을 가리킨다 (18). Figure 3 링크는 `#Figure2`를 가리킨다 (22).
- 공간 변동 수온 설명의 `they should check the box and press The`에는 누를 버튼 이름이 없다 (34).
- 본문은 Temperature Parameters에 다섯 탭이 있다고 적는다 (22–28). 37행 그림 세 장은 Bottom Heat Exchange·Initial Conditions·Ice의 세 탭을 보여 준다.

