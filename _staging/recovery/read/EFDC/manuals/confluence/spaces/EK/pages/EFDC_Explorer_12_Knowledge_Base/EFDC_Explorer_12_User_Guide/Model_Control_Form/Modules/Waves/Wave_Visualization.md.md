---
file: models/EFDC/raw/manuals/confluence/spaces/EK/pages/EFDC_Explorer_12_Knowledge_Base/EFDC_Explorer_12_User_Guide/Model_Control_Form/Modules/Waves/Wave_Visualization.md
lines: 40
sha256: 7b4dc3afa0de9e8ffce805c6fad68e8ff754cd795b6599f60b7a9c596a18d5ed
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Wave_Visualization.md — 판독 구간 기록

구간은 1행부터 40행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | Wave Visualization — 페이지 메타데이터를 담은 frontmatter이다 (1–9). |
| 10–17 | 2DH View 평면 표시와 애니메이션(animation). 제목 앞에 CSS 텍스트가 남아 있다 (10). 추가 절차와 매개변수 이름 원문: `The wave parameters can be visualized and animated in 2DH View. These can be added to the 2DH View by clicking the*Add* button in the 2DH View’s Layer Control then select *Primary Group: Wave Parameters* and the *Parameters* are available including *Wave Height, Wave Period, Wave Direction, Wave Length, Wave Vector, and Wave Cell* as shown in [Wave Visualization#Figure 1](#Figure1).` (12). `Wave5.png`를 열었다 (14). 그림은 Wave Parameters의 선택 목록을 연 2DH View Option과 격자(grid)별 파장(wave length) 색 지도를 함께 보여 준다 (14). 범례는 `Wave Length (m)`이며 양 끝 값은 `158.20`, `300.00`이다 (14 그림). 표시 시각은 `2009-03-27 12:00`이다 (14 그림). 수치 좌표축과 파향 화살표는 없다 (14 그림). Figure 1 캡션과 빈 줄을 포함한다 (11–17). |
| 18–25 | 시계열(time series) 추출. 한 셀 또는 여러 셀을 선택할 수 있다 (20). L 인덱스(index)를 넣고 Enter를 누르면 I·J 인덱스가 자동으로 채워진다 (20). 해당 원문은 `It is possible to plot the time series for a single cell or multiple cells.` (20); `Entering the L index, and then press the Enter key, the corresponding I and J indices are filled automatically.` (20)이다. 선택 그룹 원문은 `The parameter should be defined in the box, *Primary Group: Wave Parameters*.` (20)이다. 좌·우 화살표로 매개변수를 추가·제거한다 (20). 시작·종료일 적용 조건 원문은 `The user may define the start and stop day for the time series in *Time Series Start/Stop* frame (note that the start and stop days should be within the model's start and end date).` (20)이다. `79.png`와 `2022-05-20_2-29-47_PM.png`를 열었다 (20, 22). 앞 그림은 시계열 버튼의 작은 그래프 아이콘이다 (20). 뒤 그림은 Extract Time Series Data 설정 폼이다 (22). Selected Cells 표의 열은 `No.`, `L`, `I`, `J`이며 보이는 행은 `1 | 174 | 13 | 14`이다 (22 그림). 설정 값은 `Start (day): 2922.000000`, `2003-01-01 00:00:00`, `Stop (day): 2952.000000`, `2003-01-31 00:00:00`이다 (22 그림). Wave Height가 선택되어 있다 (22 그림). 제목·Figure 2 캡션과 빈 줄을 포함한다 (18–25). |
| 26–29 | Figure 3 — 파고(wave height) 시계열. `2022-05-20_2-29-13_PM.png`를 열었다 (26). 제목은 `Caloosahatchee TMDL, Water Quality Calibration - 2003`이며 범례는 빨간 선의 `Cell: 174 (I:13, J:14), Wave Height`이다 (26 그림). 가로축은 `Time (days)`이고 보이는 눈금은 `2922`, `2927`, `2932`, `2937`, `2942`, `2947`이다 (26 그림). 세로축은 `Wave Height (m)`이고 눈금은 `0.0000`, `0.0072`, `0.0144`, `0.0216`, `0.0288`, `0.0360`, `0.0432`, `0.0504`, `0.0576`, `0.0648`, `0.0720`이다 (26 그림). 선은 시간에 따라 여러 봉우리와 낮은 값을 보인다 (26 그림). Figure 3 캡션과 빈 줄을 포함한다 (27–29). |
| 30–37 | 종방향 분포(longitudinal profile) 추출. 프로파일 정의, 매개변수 선택과 예시 원문: `The graphic of wave longitudinal profiles can be visualized by click the *Longitudinal Profile*button or the icon ![](https://eemodelingsystem.atlassian.net/wiki/download/thumbnails/2126086145/1.png?version=1&modificationDate=1653029712779&cacheVersion=1&api=v2&width=24&height=26) of the main toolbar.  [Wave Visualization#Figure 4](#Figure4) show the *Data Extraction for Longitudinal Profile* form. This form is similar to the *Data Extraction for 2DV View* form. Firstly, it is necessary to define the profile using the drape file or I, J indices and then define the parameter to the plot. The parameter should be defined in the box, *Primary Group: Wave Parameters* . Add and remove the parameter can be adjusted by the left and right arrows.  Once everything is ready, click *OK* to generate the plot. [Wave Visualization#Figure 5](#Figure5) shows a longitudinal profile for wave height along with the profile I=56.` (32). 드레이프(drape) 파일 또는 I·J 인덱스로 프로파일을 정의해야 한다 (32). 좌·우 화살표로 매개변수를 추가·제거한다 (32). 예시 프로파일은 `I=56`이다 (32). `1.png`와 `Wave8.png`를 열었다 (32, 34). 앞 그림은 종방향 분포 버튼의 작은 그래프 아이콘이다 (32). 뒤 그림은 Use Drape File·Use I·Use J 선택과 Wave Height 매개변수의 Data Extraction for Longitudinal Profile 화면이며 `Specify I: 56`이 표시된다 (34 그림). 제목·Figure 4 캡션과 빈 줄을 포함한다 (30–37). |
| 38–40 | Figure 5 — 파고 종방향 분포. `Wave9.png`를 열었다 (38). 제목은 `EFDC+ Demonstration, West Lake Toxics`이다 (38 그림). 범례는 `Col: I = 56, Time: 2009-04-07 06:00` 및 빨간 선의 `Wave Height`이다 (38 그림). 가로축은 `Distance (m)`이고 보이는 눈금은 `0`, `167`, `334`, `501`, `667`, `834`, `1001`, `1168`, `1335`, `1502`, `1669`이다 (38 그림). 세로축은 `Significant Wave Height (m)`이고 눈금은 `0.00040`, `0.00055`, `0.00070`, `0.00085`, `0.00100`, `0.00115`, `0.00130`, `0.00145`, `0.00160`, `0.00175`, `0.00190`이다 (38 그림). 선은 거리별로 여러 봉우리·평탄 구간을 보이며 오른쪽 끝에서 내려간다 (38 그림). Figure 5 캡션과 빈 줄을 포함한다 (39–40). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 10행 제목 앞에 CSS 규칙과 팔레트 정의가 본문 텍스트로 남아 있다.
- 12·20·32행의 `#Figure1`–`#Figure5` 참조에 해당하는 명시적 앵커 정의가 이 파일에 없다. Figure 1–5 캡션은 본문에 있다.

