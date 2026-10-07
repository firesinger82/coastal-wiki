---
file: models/EFDC/raw/manuals/confluence/spaces/EK/pages/EFDC_Explorer_12_Knowledge_Base/EFDC_Explorer_12_User_Guide/Model_Control_Form/Initial_Conditions/Contaminant_-_Water_Column_IC.md
lines: 18
sha256: 79de5fa70048985201de3a0176d8093fb984b126ac052f607e6a70c20ca179c7
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Contaminant_-_Water_Column_IC.md — 판독 구간 기록

구간은 1행부터 18행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | Contaminant - Water Column IC — 문서 식별자, 제목, space, URL, 판본, 갱신 시각과 문서 계층의 frontmatter(1–9). |
| 10–15 | Contaminant - Water Column IC / Note — CSS 선언 뒤 Modules의 오염물질 거동(contaminant fate) 옵션을 선택할 때 수층 오염물질 항목을 활성화한다고 설명한다(10). 활성화 조건 원문: `When the contaminant fate option has been selected in the*Modules* item in the navigation tree the *Contaminants - Water Column* option will be enabled` (10) 초기 EE의 contaminant·chemical fate(ChemFate) 명칭은 toxics였다고 적는다(10). 추가 필수 조건 원문: `The sediment module must also be selected for the ChemFate options to be available.` (14) Note 제목과 빈 줄을 포함한다(11–15). |
| 16–18 | 수층 오염물질 초기값 설정 — 분류 드롭다운과 상수 입력, Assign의 다각형 배정을 설명한다(16). 입력 명칭·방법 원문: `The user can set the initial condition to a constant value by specifying a value in the *Constant IC* (formerly *WC Toxic IC)* text box.` (16) `Users are able to select to apply cell properties for a specific layer or all layers and also edit a single class or all classes in the model.` (16) 자료 형식은 Bathymetry 링크를 참조한다(16). 빈 줄과 그림을 포함한다(17–18). `Toxic.jpg`을 열었다(18). Toxics - Water Column 메뉴에서 초기조건 양식으로, Assign에서 다각형 배정 양식으로 향하는 화살표가 있다. 예제의 `Toxic: TOX_1`, `WC Toxic IC: 0`, `WC Toxic IC Avg: 0`을 표시한다. 다각형 양식은 `All grid cells`, `For All Layers`, `Constant: 0`, `Replacement`, `A Specific Class: TOX_1`이 선택되어 있다. 나머지 옵션은 `Only grid cells inside polygons`, `A Specific Layer: 1`, `From Scatter (XYZ) Data`, `From Profile Data`, `Maximum value`, `Minimum value`, `For All Classes`이다. 저질 쪽 비활성 선택지는 `Total Concentration (ug/L)`, `Mass Tox/Sed (mg/kg)`이며 `Bed Toxic IC: 0`, `Bed Toxic IC Avg: 0`이다. 파일 목록은 비어 있다. |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 10: Figure 1 링크의 fragment는 `#Figure1`이다. 이 파일에는 해당 anchor 정의가 없다.
