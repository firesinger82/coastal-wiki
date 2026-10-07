---
file: models/EFDC/raw/manuals/confluence/spaces/CVLGRID/pages/Grid_Knowledge_Base/Grid_Operation/Grid_Generation.md
lines: 44
sha256: 2342755555c4abe7aac860ad4d043fa5f52d08f67276e5b75b92183b817a8a47
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Grid_Generation.md — 판독 구간 기록

구간은 1행부터 44행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–11 | Grid Generation / 생성 원칙 — 페이지 식별 정보를 포함한다(1–9). CSS 문자열 뒤에 최소 네 스플라인, 서로 한 점에서 교차, 같은 방향 계열 스플라인끼리 교차하지 않음이라는 조건을 제시한다(10). 조건을 고쳐 쓰지 않고 원문대로 옮긴다. 원문: ``[data-colorid=quvi7m283u]{color:#242424} html[data-color-mode=dark] [data-colorid=quvi7m283u]{color:#dbdbdb}[data-colorid=oz6oi4vnvv]{color:#242424} html[data-color-mode=dark] [data-colorid=oz6oi4vnvv]{color:#dbdbdb}[data-colorid=p9sp6iumf4]{color:#242424} html[data-color-mode=dark] [data-colorid=p9sp6iumf4]{color:#dbdbdb}Creating a grid is a straightforward process. The important principle is that for each grid, at least four splines are needed. The splines should intersect each other at only point and the splines in the same orientation should not intersect each other. Follow these steps to create a simple grid:`` (10). |
| 12–17 | Grid Generation / 생성 단계 — 메뉴 또는 도구모음에서 스플라인을 그리고 LMC로 시작하여 RMC로 끝낸다(12–13). 양 끝 스플라인의 교차 의무와 I·J 셀 수 기본값을 보존한다. 원문: ``1. From the *Splines* menu, select *Draw a New Spline* or click on the *Add a new spline* button from the main toolbar ([Figure 2](#GridGeneration-Figure2)).`` (12); ``2. LMC to start drawing a spline, and RMC to end drawing the spline. Draw a second spline close to parallel to the first spline.`` (13); ``3. Next, draw two more splines along each end of the domain. These two splines **must intersect** the previous two splines ([Figure 1](#GridGeneration-Figure1))`` (14); ``4. RMC on the *Splines* layer in the *Layer Control* panel, then select the *Create Grid* option or click on the *Create Grid from Splines* button from the main toolbar, as shown in [Figure 3](#GridGeneration-Figure3)`` (15); ``5. *Create Grid from Splines* form will pop up as shown in [Figure 4](#GridGeneration-Figure4). From this form, the number of grid cells between two splines needs to be defined by entering a number of cells in the I and J directions (default values are 4). [Figure 5](#GridGeneration-Figure5) shows an example of the grid generated.`` (16). |
| 18–37 | Grid Generation / 참조 그림 — 그림 1은 초록 스플라인 네 개가 둘러싼 `Grid will be generated in this area`를 보여 준다(18). 긴 스플라인 아래·위에는 각각 `1`, `2`와 수평 좌우 화살표가 있다(18). 왼쪽·오른쪽 횡단 스플라인에는 각각 `3`, `4`와 경사진 양방향 화살표가 있다(18). 같은 방향의 두 스플라인은 만나지 않고 양 끝 횡단 스플라인이 둘과 교차한다(18). 그림 2는 항공사진 위의 스플라인과 `Draw a New Spline` 메뉴를 보여 준다(22). 그림 3의 빨간 화살표는 도구모음 아이콘에서 `Create Grid ...` 메뉴 쪽으로 향한다(26). 그림 4의 두 그룹 제목은 모두 `Grid Points in I Direction`이며 각각 `Number of Intervals: 4`가 보인다(30). 그림 5는 하천 영역의 주황 곡선형 격자를 보여 준다(34). |
| 38–44 | Tip — 스플라인 사이 계산 영역(computational domain)을 하위 영역으로 나누어 지역별 격자 밀도를 제어할 수 있다(42). 같은 방향 계열의 스플라인 방향을 같게 하면 생성이 더 빠르다고 적는다(44). 원문: ``You can control the intensity of the grid for each region by dividing the computational domain into subregions between splines.`` (42); ``It is faster for grid generation if all splines in the same orientation have the same directions.`` (44). Tip 제목·공백 줄도 포함한다(38–41). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 10행: 본문 앞에 `[data-colorid=...]`로 시작하는 CSS 규칙들이 그대로 붙어 있다.
- 16·30행: 본문은 I·J 방향 입력을 구분하지만 그림 4의 두 그룹 제목은 모두 `Grid Points in I Direction`이다.

