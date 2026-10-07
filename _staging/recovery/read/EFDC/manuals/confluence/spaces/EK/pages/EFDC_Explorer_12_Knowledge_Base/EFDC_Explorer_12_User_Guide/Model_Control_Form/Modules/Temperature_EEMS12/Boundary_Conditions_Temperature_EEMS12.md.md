---
file: models/EFDC/raw/manuals/confluence/spaces/EK/pages/EFDC_Explorer_12_Knowledge_Base/EFDC_Explorer_12_User_Guide/Model_Control_Form/Modules/Temperature_EEMS12/Boundary_Conditions_Temperature_EEMS12.md
lines: 30
sha256: 17264278dc2f98cdd89964c2ed12db41d48cda917c078d8dc63f60acb8f9fe61
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Boundary_Conditions_Temperature_EEMS12.md — 판독 구간 기록

구간은 1행부터 30행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | 문서 메타데이터. Boundary Conditions (Temperature) (EEMS12)의 식별자·제목·space·URL·버전·갱신 시각·계층 경로가 있다 (2–8). |
| 10–13 | Boundary Condition 폼 개요. 본문 앞에 색상 CSS가 있다 (10). 대기(Atmospheric Data)·수온(Temperature Data)·얼음(Ice Data) 옵션을 소개한다 (10). 12행 그림은 대기와 수온 시계열 설정이며 `Atmospheric Time Series: 1` (12행 그림); `Temperature Time Series: 1` (12행 그림); `Use Computed Solar Radiation to Overwrite Input Solar Radiation` (12행 그림)이다. 계산 일사량 사용은 미선택이며 Series Weighting은 비활성이다. Shade Factors 버튼이 있다 (12행 그림). |
| 14–21 | Atmospheric Data의 수평 압력 경사. 큰 연안 시스템의 압력 변동을 수리 계산에 반영한다고 적는다 (16–20). 적용 조건은 `EFDC+ has been updated for the pressure solution in the CALEXP2T and CALEXP routines. The modification does not make any contributions to the hydrodynamic field when the number of pressure series (NASER) is less than two, because the horizontal gradient components of atmospheric pressure (pa) are always zero. However, if pa is not a constant in the computational domain, then gradients are computed and these will impact the external solution pressure field. This approach does not violate the hydro-static assumption.` (18)이다. `CALEXP2T and CALEXP` (18) 루틴, `NASER` (18)와 `pa` (18)를 명시한다. 두 개 미만의 압력 시계열은 기여하지 않으며 공간적으로 일정하지 않은 압력은 외부 압력 해에 영향을 준다. 정수압 가정(hydro-static assumption)을 위반하지 않는다고 적는다 (18). |
| 22–25 | 대기 시계열과 공간 가중. Edit로 시계열을 수정하고 여러 시계열일 때 Series Weighting을 사용한다 (22). 24행 첫 그림은 `Select Series: ASER_1; Series Name: ASER_1; 1 / # 3; # of Points: 119225` (24행 그림)이다. 표의 열은 `Time (days) / Atmospheric Pressure (mbar) / Dry Bulb Temperature (°C) / Relative Humidity (-) / Rainfall (m/day) / Evaporation (m/day) / Solar Radiation (W/m²) / Cloud Cover (-)` (24행 그림)이다. 보이는 행은 `40543.000 / 973.9 / 2.22 / 0.620 / 0.00000 / 0.00000 / 0.0 / 0.000` (24행 그림); `40543.037 / 973.3 / 0.00 / 0.730 / 0.00000 / 0.00000 / 0.0 / 0.933` (24행 그림); `40543.078 / 973.9 / -1.67 / 0.580 / 0.00000 / 0.00000 / 0.0 / 0.228` (24행 그림); `40543.113 / 974.3 / -2.78 / 0.690 / 0.00000 / 0.00000 / 0.0 / 0.983` (24행 그림); `40543.119 / 974.3 / -2.78 / 0.690 / 0.00000 / 0.00000 / 0.0 / 0.438` (24행 그림); `40543.120 / 974.3 / -2.78 / 0.690 / 0.00000 / 0.00000 / 0.0 / 0.488` (24행 그림); `40543.125 / 974.3 / -2.78 / 0.690 / 0.00000 / 0.00000 / 0.0 / 0.923` (24행 그림); `40543.137 / 973.9 / -3.89 / 0.540 / 0.00000 / 0.00000 / 0.0 / 0.548` (24행 그림); `40543.162 / 973.9 / -5.56 / 0.600 / 0.00000 / 0.00000 / 0.0 / 0.000` (24행 그림); `40543.203 / 974.6 / -6.11 / 0.620 / 0.00000 / 0.00000 / 0.0 / 0.000` (24행 그림)이다. 둘째 그림은 `Number of Maps: 4; Inverse Distance Power: 2` (24행 그림)이다. 시간·품질 지수 표의 열은 `# / From / To / ASER_1 / ASER_2 / ASER_3` (24행 그림)이고 행은 `1 / 40543.000 / 41028.590 / 1 / 0 / 1` (24행 그림); `2 / 41028.590 / 42882.668 / 1 / 1 / 1` (24행 그림); `3 / 42882.668 / 43829.703 / 1 / 0 / 1` (24행 그림); `4 / 43829.703 / 43829.730 / 0 / 0 / 1` (24행 그림)이다. 관측소 표의 열은 `# / StationID / Start / End / Easting / Northing / Longitude / Latitude` (24행 그림)이다. 각 행은 `1 / ASER_1 / 40543.00 / 43829.70 / 310079 / 4779083 / -89.335362 / 43.140672` (24행 그림); `2 / ASER_2 / 41028.59 / 42882.67 / 304250 / 4774605 / -89.4054 / 43.0989` (24행 그림); `3 / ASER_3 / 40543.00 / 43829.73 / 303033 / 4773651 / -89.42 / 43.09` (24행 그림)이다. |
| 26–30 | Temperature Data. Edit로 수온 시계열을 편집하며 외력(External Forcing) 문서 링크를 제공한다 (28). 30행 그림은 `Select Series: Buoy; Series Name: Buoy; Number of Series: 2; # of Points: 4882` (30행 그림)이다. View All Layers가 선택되어 있다. 완전히 보이는 표의 열은 `Time (days) / Layer 1 (°C) / Layer 2 (°C) / Layer 3 (°C) / Layer 4 (°C) / Layer 5 (°C) / Layer 6 (°C) / Layer 7 (°C) / Layer 8 (°C)` (30행 그림)이다. 각 행은 `39447 / 0.50000 / 0.50000 / 0.50000 / 0.50000 / 0.50000 / 0.50000 / 0.50000 / 0.50000` (30행 그림); `39448 / 0.50000 / 0.50000 / 0.50000 / 0.50000 / 0.50000 / 0.50000 / 0.50000 / 0.50000` (30행 그림); `39449 / 0.50000 / 0.50000 / 0.50000 / 0.50000 / 0.50000 / 0.50000 / 0.50000 / 0.50000` (30행 그림); `39450 / 0.18000 / 0.18000 / 0.18000 / 0.18000 / 0.18000 / 0.18000 / 0.18000 / 0.18000` (30행 그림); `39451 / 6.45000 / 6.45000 / 6.45000 / 6.45000 / 6.45000 / 6.45000 / 6.45000 / 6.45000` (30행 그림); `39452 / 8.59000 / 8.59000 / 8.59000 / 8.59000 / 8.59000 / 8.59000 / 8.59000 / 8.59000` (30행 그림); `39453 / 6.97000 / 6.97000 / 6.97000 / 6.97000 / 6.97000 / 6.97000 / 6.97000 / 6.97000` (30행 그림); `39454 / 5.43000 / 5.43000 / 5.43000 / 5.43000 / 5.43000 / 5.43000 / 5.43000 / 5.43000` (30행 그림); `39455 / 3.50000 / 3.50000 / 3.50000 / 3.50000 / 3.50000 / 3.50000 / 3.50000 / 3.50000` (30행 그림); `39456 / 4.73000 / 4.73000 / 4.73000 / 4.73000 / 4.73000 / 4.73000 / 4.73000 / 4.73000` (30행 그림); `39457 / 3.20000 / 3.20000 / 3.20000 / 3.20000 / 3.20000 / 3.20000 / 3.20000 / 3.20000` (30행 그림)이다. 오른쪽 추가 층 제목과 값은 잘렸다 (30행 그림). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 본문 앞에 색상 CSS가 남아 있다 (10).
- 본문은 Ice Data를 설명 대상으로 포함한다 (10). 폼 그림에는 Ice Data 프레임이 없으며 이후 소절도 대기와 수온만 있다 (12행 그림, 14–30).
- Figure 2 링크는 같은 문서 경로만 가리키며 그림 앵커가 없다 (22).
- 수온 표 오른쪽 추가 층의 제목과 값이 잘렸다 (30행 그림).

