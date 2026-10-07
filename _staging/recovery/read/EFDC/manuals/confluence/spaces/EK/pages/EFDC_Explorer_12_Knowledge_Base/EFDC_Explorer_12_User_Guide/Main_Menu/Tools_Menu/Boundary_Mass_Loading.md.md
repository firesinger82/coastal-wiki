---
file: models/EFDC/raw/manuals/confluence/spaces/EK/pages/EFDC_Explorer_12_Knowledge_Base/EFDC_Explorer_12_User_Guide/Main_Menu/Tools_Menu/Boundary_Mass_Loading.md
lines: 20
sha256: 90d7a0cc2445bc50e2bb180b0ec6e7088d09de99630362c15001a861b277c194
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Boundary_Mass_Loading.md — 판독 구간 기록

구간은 1행부터 20행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | 문서 메타데이터 — 페이지 ID, 제목, space, 원문 URL, 버전, 갱신 시각, 문서 계층 경로와 frontmatter 구분선을 포함한다(1–9). |
| 10–13 | Boundary Mass Loading — 모델 영역에 들어오고 나가는 성분(constituent)의 질량 수지(mass balance) 추정과 모델 보정(calibration) 근거의 필요성을 설명한다(10). Tools에서 Boundary Mass Loading을 선택한다(10). 그림 `2.png`는 해당 메뉴를 강조한다(12). 빈 줄과 그림 마크업을 포함한다(11–13). |
| 14–17 | Mass Loading / 성분 선택 — 드롭다운 목록에서 성분을 고르고 Compute를 누른다(14). 원문: `From this form, the user selects a constituent from the drop-down list and then clicks on the *Compute* button.` (14). 그림 `10-18-2021_11-36-39_AM.png`는 `Begin Time (days): 136.0000`, `End Time (days): 138.0000`, `Constituent: Water`의 Mass Loading 창이다(16, 그림). 빈 줄을 포함한다(15·17). |
| 18–20 | Unit Options / 경계 질량 부하 보고 — 단위를 선택할 수 있는 성분의 적용 조건은 `The unit for some constituents such as sediment, salinity, and toxics can be selected from the drop-down list of the *Unit Options* , as shown in [Boundary Mass Loading#Figure 3](https://eemodelingsystem.atlassian.net/wiki/spaces/EK/pages/2084208660#BoundaryMassLoading-Figure3). After clicking on the *Compute* button, a mass loading report will be shown as [Boundary Mass Loading#Figure 4](https://eemodelingsystem.atlassian.net/wiki/spaces/EK/pages/2084208660#BoundaryMassLoading-Figure4).` (18). 그림 `5-4-2022_1-09-53_PM.png`는 `Begin Time (days): 0.0000`, `End Time (days): 366.0000`, `Constituent: Cohesive Sediments`, `Class: 1 /7 (SED) Class 1`, `Unit Options: Grams (g)`을 보여 준다(20, 그림). 단위 목록은 `Metric Tonnes (MT)`, `Kilograms (kg)`, `Grams (g)`이다(20, 그림). 그림 `5-4-2022_1-17-31_PM.png`는 Flow Boundaries Mass Loading 보고서다(20). 기간은 `2008-01-01 00:00:00 to 2008-01-06 00:00:00`이고 성분 단위는 `Cohesive Sediments (grams)`이다(20, 그림). 표의 열은 `# / Data Series / Loading Factor / Loading Input`이다. 화면에 보이는 행은 `1 / NC-015 / 1.000 / 0.000000`; `2 / NC-019 / 1.000 / 0.000000`; `3 / NC-021 / 1.000 / 0.000000`; `4 / NC-022 / 1.000 / 260.581726`; `5 / NC-023 / 1.000 / 0.000000`; `6 / NC-024 / 1.000 / 0.000000`; `7 / NC-029 / 1.000 / 4075.950195`; `8 / NC-077 / 1.000 / 243241.109375`; `9 / NC-083 / 1.000 / 114525.445313`; `10 / BB-004 / 1.000 / 0.000000`이다(20, 그림). 스크롤 아래의 행은 이 그림에 보이지 않으며 기록하지 않았다. 마지막 빈 줄·두 그림 마크업을 포함한다(19–20). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 10·14·18: `#BoundaryMassLoading-Figure1`부터 `#BoundaryMassLoading-Figure4` 링크가 있다. 이 파일에는 대응 앵커와 그림 번호 캡션이 없다.
- 20(두 그림): 설정 창은 시작 0일·종료 366일을 표시한다. 보고서 창은 2008-01-01부터 2008-01-06까지를 표시한다.

