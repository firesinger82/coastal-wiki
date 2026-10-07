---
file: models/EFDC/raw/manuals/confluence/spaces/EK/pages/EFDC_Explorer_12_Knowledge_Base/EFDC_Explorer_12_User_Guide/Model_Control_Form/Model_Analysis/Habitat_Analysis/Critical_Limits_Time_Series.md
lines: 28
sha256: 4b0aae0442133810a5a69623e7deff4f02f7eb80312989ee080b3e14e96a5632
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Critical_Limits_Time_Series.md — 판독 구간 기록

구간은 1행부터 28행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | Critical Limits Time Series / 메타데이터 — 페이지 식별자 `274726913` (2), 제목·space·URL·버전·갱신 시각·상위 경로와 frontmatter 구분선을 포함한다(1–9). |
| 10–14 | Critical Limits Series / 기준 설정 — 활성 매개변수 중 최대 다섯 개를 선택하고 각 최소·최대값을 지정한다(10). 원문: `up to five different parameters` (10); `Parameter` (10); `minimum and maximum values for the critical limits` (10); `single layer (enter layer number), a range of layers (eg 1-2), average of a series of layer (eg 2:6), or depth averaged (0).` (10). 저장을 권장하며 `#habitat` 폴더와 `“.HCL”` 확장자를 사용한다(10). `Criteria ID` (12)는 추출 파일명에 붙는다. 로컬 `9-4-2019_11-04-45_AM.jpg`를 열었다(14). 설정 화면의 예시값은 `Water Depth`, `Minimum 0.3`, `Maximum 4`, `Layer 0`, `Velocity`, `Minimum 0`, `Maximum 1.5`, `Layer 2:4`이다(14, 그림). Water Depth의 Series만 선택되어 있다. 시작·끝 날짜는 `2000-07-29 00:00:00`, `2000-08-05 00:00:00`이다(14, 그림). |
| 15–20 | Critical Limits / 셀 판정·추출 — 각 층의 셀이 모든 기준을 만족하면 1, 모두 만족하지 못하거나 건조하면 0으로 설정한다(16). 원문: `If a cell doesn’t meet all the criteria it is set to zero, whereas if a cell does meet all the criteria it is set to one.` (16); `If a cell is dry it is also set to zero.` (16); `Series` (16); `Only one parameter may be output at a time.` (16). 추출 시작·끝 날짜를 설정한다(18). `Cell by Cell` (18)은 모든 셀을 모든 시간 단계에 계산한다. `Sub-Set` (18)에 폴리라인(polyline) 파일을 선택하면 일부 영역만 추출할 수 있다. `Hab\_Results\_Muskellunge Adult.dat` (20)는 composite time, net weighted criteria, area, volume을 저장한다. 가중 기준의 원문은 `weighted average 0 and 1 of all the cells that meet the bathymetry criteria` (20)이다. |
| 21–28 | Critical Limits / 결과·후처리 — 빈 줄·시계열 예시 참조·그림을 포함한다(21–25). 로컬 `9-4-2019_11-02-34_AM.jpg`를 열었다(24). 그래프 x축은 `Time (days)` 210–217, 왼쪽 y축은 `Water Depth (m)` 0.75–3.25, 오른쪽 y축은 `Suitable Habitat Volume (m³)` 0–3750000이다(24, 그림). 범례는 빨강 `Volume`, 파랑 `Area`, 초록 `Water Depth`이다. 그림에는 Area 전용 축이나 단위가 표시되어 있지 않다. 표시 시계열은 자동 저장되지 않으므로 내보내야 한다(26). 후처리 선택은 `Domain Average, Running Averages`, `Single Cell Time Series` (28)이다. 이동평균(running average)은 `the number of days to be applied for the calculation of the running average` (28)를 사용자가 반드시 지정한다. |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 24·26: 본문은 예시 결과를 velocity의 복합 시계열이라고 적지만, 그림의 변수 범례는 `Water Depth`이다.
- 10·22: 본문은 Figure 1과 Figure 2 앵커를 참조하지만 이 Markdown 파일에는 해당 앵커 선언이나 번호 캡션이 없다.

