---
file: models/EFDC/raw/manuals/confluence/spaces/EK/pages/EFDC_Explorer_12_Knowledge_Base/EFDC_Explorer_12_User_Guide/Model_Control_Form/Model_Analysis.md
lines: 32
sha256: a6b9cdc9eb99765ffb74443f7c20d2c618a672a5aa8dcea49691eca6bce2bec7
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Model_Analysis.md — 판독 구간 기록

구간은 1행부터 32행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | Model Analysis — 문서 식별자, 제목, space, URL, 판본, 갱신 시각과 문서 계층의 frontmatter(1–9). |
| 10–20 | Model Analysis / 보정 플롯 종류 — 보정(calibration) 기능 메뉴와 여섯 종류의 플롯을 소개한다(10–17). 원문 목록: `Time Series Comparisons` (12); `Correlation Plots` (13); `Vertical Profile Comparisons` (14); `High-Frequency Time Series` (15); `Flux Comparisons` (16); `Cruise Plot Comparisons` (17). 각 플롯에 수층 모델 결과와 실측자료의 연결(linkage)이 필요하다(19). 필수 조건 원문: `For each of these, the user needs to provide a linkage of the water column model results to measured data.` (19) 빈 줄을 포함한다(11,18,20). |
| 21–29 | 좌·우클릭 메뉴 — 왼쪽 클릭(LMC)은 요약을 표시하고 오른쪽 클릭(RMC)은 플롯·오차통계·보정 시계열 정의 메뉴를 연다(21–26). 메뉴 이름 원문: `*View Time-Series Plots*` (23) `*View Correlation Plots*` (24) `*Calculate Error Statistics*` (25) `*Define Calibration Series*` (26) 오차통계는 전체 또는 개별 연결마다 계산하고 보고할 통계를 선택해 텍스트로 저장한다(25). 보정 정의는 모델 매개변수와 실측 시계열을 연결하고 플롯 사용·제외 및 플롯·통계 생성을 지정한다(26). `2019-05-15_3-58-24_PM.jpg`을 열었다(28). 그림은 Model Analysis 탐색 트리와 해당 네 메뉴이다. Time Series Comparisons 표 열은 `#`, `Name`, `X (m)`, `Y (m)`, `Parameter`, `Layer`, `File name`이다. 보이는 첫 행은 `1, Forebay, 314063, 3941267.5, Water Surface Elevation, Depth Averaged`이고 셋째 행은 `3, CLP06, 323156, 3956550, Temperature, Code -6`이다. 둘째 행 일부와 긴 파일 경로는 팝업 또는 화면 경계에 가려져 있다. 빈 줄과 그림을 포함한다(27–29). |
| 30–32 | 플롯 스타일 저장·추가 비교 — 설정파일의 플롯별 대응 원문: `The plot styles are saved in the EFDC+ Explorer configuration file "CalForm\_TS.EE," "CalForm\_CP.EE" and "CalForm\_VP.EE" for the time series, correlation and vertical profile plots respectively.` (30) `In addition, the file "CalForm\_MMA.EE" contains plot styles for the time series option of *Min-Avg-Max* plots` (30) 현재 연결 방식은 모델·자료 비교의 한 방법이며 시계열 플롯의 Import Data로 거의 모든 모델 매개변수와 자료를 비교할 수 있다고 적는다(32). 빈 줄과 Time Series Graphing 링크를 포함한다(30–32). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 10: Figure 1 링크는 `https://eemodelingsystem.atlassian.net/wiki/pages/resumedraft.action?draftId=2380092#ModelCalibration-Figure1`의 초안 재개 URL이다.
