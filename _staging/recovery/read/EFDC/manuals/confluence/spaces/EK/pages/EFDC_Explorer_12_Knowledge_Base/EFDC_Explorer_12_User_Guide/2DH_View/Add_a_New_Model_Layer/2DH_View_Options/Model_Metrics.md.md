---
file: models/EFDC/raw/manuals/confluence/spaces/EK/pages/EFDC_Explorer_12_Knowledge_Base/EFDC_Explorer_12_User_Guide/2DH_View/Add_a_New_Model_Layer/2DH_View_Options/Model_Metrics.md
lines: 24
sha256: a5a944ca609cd835113f695c3377e55ef13a2f3b50af89df1538f2e65011d8bc
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Model_Metrics.md — 판독 구간 기록

구간은 1행부터 24행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | 문서 메타데이터 — 제목 `title: "Model Metrics"` (3)을 포함한다. 페이지 ID, space, URL, 버전, 갱신 시각, 문서 경로와 frontmatter 구분자를 포함한다(1–9). |
| 10–15 | Model Metrics / 메뉴 — `Parameter` 드롭다운의 옵션을 그림으로 안내한다(10). 로컬 그림 `models/EFDC/raw/manuals/confluence/spaces/EK/attachments/258998449/2019-06-26_9-23-23_AM.png`을 열었다(12). 그림 1은 Model Metrics 그룹에서 Celerity를 선택하고 매개변수 목록을 펼친 화면이다(12행 그림). 캡션과 빈 줄을 포함한다(14–15). |
| 16–24 | 매개변수 표 — 파속(celerity), CFL 시간 간격(Courant-Friedrichs-Lewy time step), Courant 수(Courant number), Froude 수(Froude Number), 밀도 Froude 수(Froude Density Number), Richardson 수(Richardson Number), Reynolds 수(Reynolds Number)의 표시 의미를 설명한다(18–24). CFL Time Step 설명은 그림 1의 모델에서 `1.5 seconds`를 권장한다(19). Courant # 설명은 적응 시간 간격(adaptive time stepping)의 초기 표시 시간 간격이 `0 seconds`이고 입력한 모델 시간 간격의 Courant 수가 `less than one`이어야 한다고 적는다(20). Reynolds 수 계산은 동점성계수(kinematic viscosity)를 사용한다(24). 표의 헤더·구분선과 모든 데이터 행을 포함한다(16–24). 원문 표 행: `\| *Celerity* \| Displays the computed celerity for each cell. \|` (18); `\| *CFL Time Step* \| Displays the Courant-Friedrichs-Lewy (CFL) time step computed for each cell. This is a good guide to the appropriate time step, especially if using the two time level solution. Generally the lower range of the CFL number is the recommended model time step. So for the model shown in Figure 1, a time step of 1.5 seconds is recommended. \|` (19); `\| *Courant #* \| Displays the Courant numbers for the model based on the time step settings of the model. If adaptive time stepping is specified, the time step used for the initial display of the Courant numbers will be 0 seconds. A *Courant Calculator* is available by setting the focus to the plot and then pressing "T". This allows the user to specify a new time step to be used for the Courant numbers. The Courant number should be less than one for the model time step entered. \|` (20); `\| *Froude* \| Displays the computed Froude Number for each cell. \|` (21); `\| *Froude Density* \| Displays the computed Froude Density Number for each cell \|` (22); `\| *Richardson* \| Displays the computed Richardson Number for each cell. \|` (23); `\| *Reynolds* \| Displays the computed Reynolds Number for each cell at the selected time step for each layer. The kinematic viscosity is used for the computations of the Reynolds number. \|` (24). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 10: 내부 링크는 `#ModelMetrics-Figure1`을 가리킨다. 이 Markdown 파일에는 해당 앵커 정의가 없다.
- 19·12행 그림: 본문은 그림 1의 모델에 `1.5 seconds` 시간 간격을 권장한다. 그림 1은 매개변수 선택 메뉴이다. 그림에는 CFL 계산값의 범위나 `1.5 seconds` 값이 보이지 않는다.
