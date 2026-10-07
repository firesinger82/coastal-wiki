---
file: models/EFDC/raw/manuals/confluence/spaces/EHG/pages/EEMS_12_Tutorials/How-to_Guides_for_Grid/How_to_Load_a_Grid.md
lines: 36
sha256: 36dd4feb5604c2e9385dd860420f973d9ff8d4d84e2d038d007e7f3ffaff6a21
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# How_to_Load_a_Grid.md — 판독 구간 기록

구간은 1행부터 36행까지 빈틈없이 이어진다.
그림 경로는 원문과 같은 space 폴더를 기준으로 적었다.

| 구간 | 내용 |
|---|---|
| 1–15 | 문서 정보와 격자 가져오기 — 페이지 메타데이터를 포함한다(1–9). Grid+ 기본 격자와 CVLGrid·Delft3D 격자의 확장자를 설명한다(10). 도구막대 Import Grid와 기본 격자의 레이어 메뉴 끌어놓기(drag and drop)를 안내한다(10–14). 확장자와 적용 조건을 원문으로 옮긴다(10). 원문: `Grid+ uses a native grid file with the extension \*.gpc. Besides this, it can also load various other types of grids, such as \*.cvl (grid file made by CVLGrid) and \*.grd (grid file made by Delft3D). To load a grid file,  click the *Import file* button from the main toolbar, then select *Import Grid*, as shown in [Figure 1](#HowtoLoadaGrid-Figure1). A native Grid+  @.gpc file can also be dragged and dropped onto the layer menu on the left of the form. ` (10). 그림 직접 확인: `attachments/2225143815/1.png` — Figure 1(12): 위성 영상과 항만 격자 위에서 Import Grid 메뉴를 빨간 테두리로 강조한 화면. |
| 16–25 | Import Grid / Coordinate System — 파일 형식을 선택한 뒤 Open으로 불러온다(16). Geographic 또는 UTM 좌표계를 올바르게 지정해야 하며, 잘못 지정하면 다시 불러와 다른 좌표계로 저장해야 한다(16). 파일 선택창과 좌표계 창을 포함한다(18–24). 원문: `When selecting the *Import Grid* option, the *Import Grid* form will pop up, as shown in [Figure 2](#HowtoLoadaGrid-Figure2). We browse to the grid file. We can select many types of grids by clicking on the down arrow in the form. After selecting a grid file, click the *Open* button to load the file. After clicking the *Open* button, then the *Coordinate System* form will be displayed, as shown in [Figure 3](#HowtoLoadaGrid-Figure3). It is necessary to define the correct coordinate system for the grid. Select either the Geographic system or UTM system, then click the *OK* button. If the wrong coordinate system is selected, the grid will be located in the incorrect location. It is then necessary to load the grid again and save it with another coordinate system.` (16). 그림 직접 확인: `attachments/2225143815/2.png` — Figure 2(18): Import Grid에서 폴더를 찾아 Open을 누르는 화면이다. 파일 형식 선택값은 `Grid+ (*.gpc;*.cvl)`이다. 그림 직접 확인: `attachments/2225143815/3.png` — Figure 3(22): 좌표계 창에 `Category: UTM, Northern Hemisphere`, `Projection: UTM Zone 18 (78°W - 72°W)`를 표시한다. |
| 26–31 | 끌어놓기로 불러오기 — 파일을 선택하여 Grid+ 작업 공간으로 끌어놓는 대안을 설명한다(26). 불러온 전체 격자 그림과 캡션을 포함한다(28–30). 그림 직접 확인: `attachments/2225143815/4.png` — Figure 4(28): 위성 배경 위에 불러온 항만 격자와 해안선을 분홍색으로 표시한다. |
| 32–36 | Related articles / Filter by label — 선택한 라벨에 항목이 없다는 안내를 포함한다(32–36). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 10: 기본 확장자는 `\*.gpc`로 적지만 같은 행의 끌어놓기 설명은 `@.gpc`로 적는다.
- 10·16: 그림 링크는 `#HowtoLoadaGrid-FigureN` 형식이며 이 Markdown 파일에는 해당 ID를 정의하는 마크업이 없다.

