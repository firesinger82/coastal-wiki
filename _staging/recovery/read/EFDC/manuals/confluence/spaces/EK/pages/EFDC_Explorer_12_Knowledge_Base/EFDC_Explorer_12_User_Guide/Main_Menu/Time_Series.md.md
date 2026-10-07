---
file: models/EFDC/raw/manuals/confluence/spaces/EK/pages/EFDC_Explorer_12_Knowledge_Base/EFDC_Explorer_12_User_Guide/Main_Menu/Time_Series.md
lines: 32
sha256: fd3875ba02ca9d254e9c932454d24e2a215999c1c6ce5f8a690cfd6fefd960c8
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Time_Series.md — 판독 구간 기록

구간은 1행부터 32행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | 문서 메타데이터 — 페이지 ID, 제목, space, 원문 URL, 버전, 갱신 시각, 문서 계층 경로와 frontmatter 구분선을 포함한다(1–9). |
| 10–17 | Time Series — 시계열(time series) 그래프 도구를 XY 그래프와 2DV View에도 사용한다고 설명한다(10). 2DV View는 다른 그래프 서브루틴을 사용한다고 적는다(10). CSS와 Figure 1 참조를 포함한다(10). 그림 `EE10_204b.png`는 여러 입력 자료와 모델 유량(discharge)을 비교한다(12). 가로축은 `Time (days)`이며 표시 시각은 `2009-09-20 22`, `2009-09-21 04`, `2009-09-21 10`, `2009-09-21 16`이다. 세로축은 `Discharge (m3/s)`이며 눈금은 −200–800, 간격은 100이다. 범례는 청록선 `Lay Releases (1Min)`, 빨간 네모 `Childersburg: Data`, 초록선 `Logan Martin Releases (1Min)`, 파란선 `Childersburg: Model`이다(12, 그림). 도구 모음 접근 조건은 `If no time series window has been created yet, the only option available to the user is *New Time Series* and *New Blank Plot* button.` (14). 그림 `79.png`는 곡선 그래프 아이콘이다(14). 그림 `EE10_156.png`는 New Time Series·New Blank Plot 메뉴를 보여 준다(16). 빈 줄·그림 마크업을 포함한다(11–17). |
| 18–23 | 새 시계열 / 선택 셀 평균 / 매개변수 선택 — New Blank Plot은 빈 그래프를 열고 New Time Series는 셀·매개변수 설정 창을 연다(18). 평균 설정과 적용 순서는 `The *Average Selected Cells* checkbox to plot the time series of averaging parameter values from multiple cells selected.` (18); `Note that after selecting the checkbox, the user needs to click the *Update* button and then click the *OK* button.` (18). 그림 `21.png`는 선택 셀 목록, 수심 매개변수와 평균 체크 항목을 보여 준다(20). 그림 `22.png`는 빨간 `Avg Cells, Water Depth` 곡선이다(20). 가로축은 `Time (days)`이고 눈금은 337.983–726.445이다. 세로축은 `Water Depth (m)`이고 눈금은 5.25–7.75, 간격은 0.25이다(20, 그림). 셀 수와 인덱스 입력 조건은 `To define the cells in the plot, the user should enter the number of cells into the box highlighted in Figure 3, then enter the L index of the cells, and then press enter (alternatively, enter the corresponding I and J).` (22). 선택 이름은 `*Primary Group,*` (22); `*Parameter*` (22); `*Parameters to Plot*` (22). 왼쪽 화살표로 매개변수를 추가하고 오른쪽 화살표로 제거한다(22). 여러 매개변수를 선택할 수 있고 배치를 저장·불러올 수 있다(22). 기간 조건은 `The user may define the start and stop day for the time series in *Time Series Start/Stop* frame (note that the start and stop days should be within the model's start and end date).` (22). |
| 24–32 | Series Options / Toolbar menu / 자료 교환 — 축·제목·범례에서 오른쪽 마우스 클릭으로 편집·재설정하며 Series Options로 연결한다(24). 현재 창 조건은 `When the *Time Serie*s window is selected as the current window, clicking on *Time Series*on the main toolbar will show additional items ([Figure 5](#Figure5)).` (28). 추가 항목 기능은 2DV View의 도구 모음과 같다고 적는다(28). 그림 `EE10_158.png`는 서식·설정·오차 통계·자료 가져오기/내보내기·이미지 생성·배치 저장/불러오기 메뉴를 보여 준다(30). Import Data Series·Export Data Series로 다른 모델이나 시계열과 비교할 자료를 파일로 옮긴다(32). 기본 확장자·수량은 `A "DAT" file (the default extension) can contain almost unlimited series.` (32). 파일 형식은 Appendix B 링크로 안내하며 이 문서에 형식 예시 줄은 없다(32). 수층(water column)·퇴적물(sediments)·경계 강제력(boundary forcing) 시계열을 다루고 보정(calibration)용 사용자 자료 시계열을 만들 수 있다고 적는다(32). 절 제목·빈 줄·링크·마크업을 포함한다(24–32). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 10·14·18·28: `#Figure1`부터 `#Figure5` 링크가 있다. 이 파일에는 대응 앵커와 해당 번호의 캡션이 없다.

