---
file: models/EFDC/raw/manuals/confluence/spaces/EK/pages/EFDC_Explorer_12_Knowledge_Base/EFDC_Explorer_12_User_Guide/Main_Menu/Models_Menu/Create_Warm_Start_Model.md
lines: 20
sha256: 9f0630a0f01d160463fe3e7fa3abd3977dfd272764ccc16889141145b1b714e9
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Create_Warm_Start_Model.md — 판독 구간 기록

구간은 1행부터 20행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | 문서 메타데이터 — 페이지 식별자, 제목, space, URL, 버전, 갱신 시각과 문서 계층을 기록한다(2–8). |
| 10–13 | Create Warm Start / 용도와 초기 조건 — 지정 시각의 초기 조건(initial condition)을 만들어 진단·민감도 분석(diagnostic/sensitivity analysis)에 사용할 수 있다고 적는다(10). Model의 Create Warm Start를 선택하고 원하는 시각의 상태를 저장한다(10). warm start 모델은 수층과 퇴적물 하상 상태를 사용하지만 운동량(momentum)은 포함하지 않으므로 모든 유속 값이 0인 정지 상태에서 시작한다(12). 부정 조건과 유속 값을 원문 그대로 옮긴다. 원문: `This function allows the user to create the initial conditions for the model at a specified time. This is useful for diagnostic and sensitivity analyses, allowing the user to understand key processes in the system. To use this option, click on the *Model* menu then select *Create Warm Start*option as shown in [Figure 1](#CreateWarmStartModel-Figure). The user goes to the desired time and saves the current model conditions as presented [Figure 2](#CreateWarmStartModel-Figure2).` (10); `In this case, the new *Warm Start* model would begin with the water column and sediment bed conditions at specified. A *Warm Start* model is different from a *Hot Start* model because the momentum is not included. Therefore model would begin from a quiescent system as all velocity values are zero.` (12). |
| 14–17 | Figure 1 / 메뉴 화면 — 로컬 `models/EFDC/raw/manuals/confluence/spaces/EK/attachments/246646053/1-12-2021_11-48-06_AM.png`를 직접 열었으며 Model 메뉴의 Create Warm Start 항목을 빨간 사각형으로 표시한 화면을 보여 준다(14). 캡션도 포함한다(16). 원문: `![](https://eemodelingsystem.atlassian.net/wiki/download/thumbnails/246646053/1-12-2021%2011-48-06%20AM.png?version=1&modificationDate=1610426947761&cacheVersion=1&api=v2&width=800&height=618)` (14); `**Figure 1. Create warm start model (1).**` (16). |
| 18–20 | Figure 2 / 생성 폼 — 로컬 `models/EFDC/raw/manuals/confluence/spaces/EK/attachments/246646053/warmstart.jpg`를 직접 열었으며 초기 조건 시각·시뮬레이션 기간·새 제목과 Save As a New Project 버튼을 보여 준다(18). 화면 값은 `Specify IC Using Model Output at: 2012-07-01 00:00:00`, `Duration of Simulation (days): 180`, `New Run Title: Lake T`이고 `Create Restart File (unavailable)`는 비활성 상태이다(18, 그림). 캡션도 포함한다(20). 원문: `![](https://eemodelingsystem.atlassian.net/wiki/download/attachments/246646053/warmstart.jpg?version=1&modificationDate=1557732498783&cacheVersion=1&api=v2)` (18); `**Figure 2. Create warm start model (2).**` (20). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 10: `#CreateWarmStartModel-Figure`와 `#CreateWarmStartModel-Figure2` 링크에 대응하는 앵커 정의가 이 파일에는 없다.
- 12: 수층·하상 상태의 시각을 설명하는 구절이 `at specified.`로 끝난다.
