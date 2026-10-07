---
file: models/EFDC/raw/manuals/confluence/spaces/EK/pages/EFDC_Explorer_12_Knowledge_Base/EFDC_Explorer_12_User_Guide/Model_Control_Form/Modules/Sediment/SEDZLJ_Sediment_Model/Erosion_Rates_Option_2.md
lines: 42
sha256: 14af632323c4bc75c6214eb4cf8a7d054ddcd8d46baa12507eafe1a597998f88
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Erosion_Rates_Option_2.md — 판독 구간 기록

구간은 1행부터 42행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | 문서 메타데이터. Erosion Rates Option 2의 식별자·제목·space·URL·버전·갱신 시각·계층 경로가 있다 (2–8). |
| 10–19 | Option 2의 선택 조건과 식. 10행에는 색상 CSS가 본문 앞에 남아 있다. SEDFlume 자료의 전단응력과 침식률 관계를 Jones and Lick (2001)의 방법으로 정의할 수 있을 때 `Equation (E = A\*Tau^n` (10) 옵션을 선택한다. 12행 그림의 식은 `E=\begin{cases}A(\tau_b)^n&\text{for }\tau_b>\tau_{cr}\\0&\text{otherwise}\end{cases}\tag{1}` (12행 그림)이다. 기호 정의는 `*E* is erosion rate (cm/s), *τb* is bed shear stress (N/m2), *τcr* is critical shear stress (N/m2), and *A* and *n* are the fitted parameters based on the SEDFlume core data.` (12)이다. `(*A*, *n*, and *τcr*)` (14)와 최대 침식률 `(*Emax*)` (14)를 사용하며, 높은 전단응력에서 지나치게 큰 값을 예측하지 않도록 층별 최대 침식률을 둔다 (14). 16행 그림은 Equation and Bed Properties by Core ID를 선택했다. 표시값은 `# Sediment Bed Layers: 7; # Sediment Classes: 6` (16행 그림); `Date/Time to Start Sediment Transport (days): 1` (16행 그림); `Deposition Limit of Water Column Sediments (0-1): 1` (16행 그림); `Maximum Deposition Layer Thickness (m): 1` (16행 그림); `Minimum Water Depth for Shear Stress Updates (m): 0.1` (16행 그림); `Sediment Timestep (s): 1` (16행 그림); `Options: Not Used` (16행 그림)이다. 화면의 식 `E=A*Tau^n` (16행 그림)은 LaTeX로 `E=A*\mathrm{Tau}^{n}`이다. 세 계산 옵션·핫스타트·진단 출력·BEDMAP.INP 적용은 미선택이다 (16행 그림). |
| 20–27 | 활성층(active layer)·퇴적층(deposited layer)의 D50별 침식 계수 표. `Erosion Multiplier (*A*), Erosion Exponent (*n*), and Maximum Erosion Rate (cm/s)` (20)를 입력한다. `The lookup table for critical shear stresses (*τcr*) in a*ctive & deposited bed layers* is specified in the *Sediment Bed* tap.` (22)이다. 24행 그림의 열은 `Size (μm) / Erosion Multiplier (A) / Erosion Exponent (n) / Maximum Erosion Rate (cm/s)` (24행 그림)이다. 각 행은 `0.1 / 0.004084 / 2.151 / 0.5` (24행 그림); `40 / 0.004084 / 2.151 / 0.5` (24행 그림); `125 / 0.004084 / 2.151 / 0.5` (24행 그림); `275 / 0.00316 / 2.183 / 0.5` (24행 그림); `800 / 0.000865 / 2.45 / 0.5` (24행 그림); `2400 / 8.8E-05 / 3.958 / 0.5` (24행 그림); `6000 / 1.3E-05 / 8.37 / 0.5` (24행 그림); `10000 / 6E-06 / 12.64 / 0.5` (24행 그림)이다. |
| 28–42 | Core Definitions의 코어별 물성·침식 계수. 코어 수·이름·위치를 지정한다 (28–38). `*Water Density* can be specified as 1 g/cm3, and *Sediment Density* can usually be determined as 2.65 g/cm3.` (32)이다. 물성 단위는 `critical shear stress (dynes/cm2), dry bulk density (g/cm3), layer thickness (cm), and grain size fractions (%)` (34)이며, 좌표는 `Easting (m) and Northing (m)` (38)이다. 침식 계수 항목은 `Erosion Multiplier (*A*), Erosion Exponent (*n*), and Maximum Erosion Rate (cm/s)` (36)이다. 40행 그림은 `Number of SEDFlume Cores: 3; Riverine; 1 / # 3` (40행 그림); `Water Density (g/cm³): 1; Sediment Density (g/cm³): 2.65` (40행 그림); `Easting (meters): 270677; Northing (meters): 1675088` (40행 그림)이다. 물성 표의 열은 `Layer / Critical Shear Stress (dynes/cm²) / Dry Density (g/cm³) / Thickness (cm) / D1=40 (μm) / D2=125 (μm) / D3=275 (μm) / D4=800 (μm) / D5=2400 (μm) / D6=6000 (μm)` (40행 그림)이다. 각 행은 `Active 1 / 0.1 / 0.801 / 0 / 10 / 50 / 30 / 7 / 2 / 1` (40행 그림); `Deposited 2 / 0.1 / 0.801 / 0 / 10 / 50 / 30 / 7 / 2 / 1` (40행 그림); `3 / 3 / 0.801 / 15 / 10 / 50 / 30 / 7 / 2 / 1` (40행 그림); `4 / 3.5 / 0.801 / 15 / 10 / 50 / 30 / 7 / 2 / 1` (40행 그림); `5 / 4 / 0.801 / 15 / 10 / 50 / 30 / 7 / 2 / 1` (40행 그림); `6 / 5 / 0.801 / 15 / 10 / 50 / 30 / 7 / 2 / 1` (40행 그림); `7 / 999 / 0.801 / 40 / 10 / 50 / 30 / 7 / 2 / 1` (40행 그림)이다. SEDFlume 침식률 표의 열은 `Layer / Erosion Multiplier (A) / Erosion Exponent (n) / Maximum Erosion Rate (cm/s)` (40행 그림)이며 각 행은 `Layer 1 / 0.00244 / 2.32 / 0.5` (40행 그림); `Layer 2 / 0.00244 / 2.32 / 0.5` (40행 그림); `Layer 3 / 0.00244 / 2.32 / 0.5` (40행 그림); `Layer 4 / 0.0004 / 3.7 / 0.5` (40행 그림); `Layer 5 / 0.00034 / 2.76 / 0.5` (40행 그림); `Layer 6 / 0.00096 / 2.43 / 0.5` (40행 그림); `Layer 7 / 0.00056 / 2.92 / 0.5` (40행 그림)이다. |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 본문 앞에 색상 CSS가 남아 있다 (10).
- 본문은 Erosion Rates 화면을 Figure 4로 부른다 (20). 실제 캡션은 Figure 2이다 (26).
- 식의 전단응력 정의는 `N/m2`이다 (12). 코어 물성과 그림 표는 `dynes/cm2` 또는 `dynes/cm²`이다 (34, 40행 그림). 단위 변환 설명은 이 파일에 없다 (1–42).

