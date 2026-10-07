---
file: models/EFDC/raw/manuals/confluence/spaces/EK/pages/EFDC_Explorer_12_Knowledge_Base/EFDC_Explorer_12_User_Guide/Model_Control_Form/Modules/Temperature_EEMS12/Initial_Conditions_Temperature_EEMS12.md
lines: 20
sha256: eaaf808f89de8610f5731ed3ccfa679f5fb4ae1f21ba12c5890f47fe0d29e58e
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Initial_Conditions_Temperature_EEMS12.md — 판독 구간 기록

구간은 1행부터 20행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | 문서 메타데이터. Initial Conditions (Temperature) (EEMS12)의 식별자·제목·space·URL·버전·갱신 시각·계층 경로가 있다 (2–8). |
| 10–13 | 초기 조건(Initial Conditions) 진입 방법. Temperature Parameters 폼 또는 Temperature 모듈 우클릭으로 접근하며 Temperature IC 설명을 연결한다 (10). 12행 첫 그림은 수온과 저상 온도의 공간 변동 상자를 모두 선택한 초기 조건 폼이다. 비활성 표시값은 `Constant/Average Value: 20.000` (12행 그림); `Uniform Bed Temperature (°C): 15` (12행 그림); `Uniform Thermal Thickness (m): 1` (12행 그림)이다. 둘째 그림은 우클릭 메뉴와 요약 화면이다. Settings가 강조되었다. `Surface Heat Exchange Submodel: No Atmospheric Linkage; Solar Radiation: Ignored; Surface Evaporative Losses: Ignored` (12행 그림); `Number of Atmospheric Series: 0; Mean: 20.00 °C; Min: 20.00 °C; Max: 20.00 °C` (12행 그림)이다. |
| 14–20 | 수온과 저상 온도 초기화. 수온의 `Assign` (16)에서 `Constant` (16)·XYZ·수직 프로필(Profile Data) 자료를 선택하며 층을 지정한다. 다각형 적용과 교체·최대·최소 보간을 설명한다 (16). More…는 역거리 가중(Inverse Distance Weighting, IDW) 차수·이웃점·사분면 수를 제공한다 (16). 저상 온도는 `Uniform Bed Temperature` (18) 또는 `Use Spatially Variable Bed Temp and Thickness` (18)를 사용한다. 20행 첫 그림은 두 공간 변동 상자가 미선택인 초기 조건 폼이며 `Constant/Average Value: 20.000` (20행 그림); `Uniform Bed Temperature (°C): 0` (20행 그림); `Uniform Thermal Thickness (m): 1` (20행 그림)이다. 둘째 그림의 Assign 버튼에서 Apply Cell Properties: Temp로 빨간 화살표가 향한다. 원래 폼은 `Constant/Average Value: 20.000; Uniform Bed Temperature (°C): 15; Uniform Thermal Thickness (m): 1` (20행 그림)이다. 배정 창은 `All grid cells; For All Layers; Constant: 0; Replacement` (20행 그림)를 선택했다. 특정 층 입력은 `For A Specific Layer: 1` (20행 그림)이고 해당 선택지는 미선택이다. From Scatter (XYZ) Data·From Profile Data와 Maximum value·Minimum value 선택지가 있다 (20행 둘째 그림). 셋째 그림은 Use Spatially Variable Bed Temperature and Thickness를 선택하고 Bed Temperatures에서 Apply Cell Properties: Bed Temperature로 향하는 빨간 화살표를 보여 준다. 원래 폼은 `Constant/Average Value: 20.000; Uniform Bed Temperature (°C): 15; Uniform Thermal Thickness (m): 1` (20행 그림)이다. 배정 창은 `All grid cells; Constant: 0; Centroid Interp.` (20행 그림)를 선택했고 Scatter (XYZ) data·Avg. Value·Max. Value·Min. Value 대안이 있다. 폴리곤·자료 파일 목록은 모두 비어 있다 (20행 그림). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 본문은 두 주요 영역을 말하지만 그 문장에서 Initial Conditions for Water Temperature만 이름을 적는다 (14). 저상 온도 설명은 18행에 있다.
- 다각형 배정 설명의 `they should check the box and press The`에는 누를 버튼 이름이 없다 (16).

