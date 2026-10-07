---
file: models/EFDC/raw/manuals/confluence/spaces/CVLGRID/pages/Grid_Knowledge_Base/Layer_Control/Overlay_Layer_RMC_Options.md
lines: 63
sha256: 22187ab41e9d67b66370ed948bcba003c66e996c4d9b5eff46c05ea2af618a6d
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Overlay_Layer_RMC_Options.md — 판독 구간 기록

구간은 1행부터 63행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | 문서 메타데이터 — 제목 `Overlay Layer: RMC Options`, space `CVLGRID`, 원문 URL, 버전과 갱신 시각을 담는다(2–8). |
| 10–28 | 오버레이(overlay) 레이어의 오른쪽 마우스 클릭(RMC) 메뉴 — 트리 제목에서 메뉴를 연다(10). 표의 행은 `Properties` (20), `Zoom to Layer` (21), `Save As` (22), `Remove` (23), `Create New Spline Layer` (24), `Create New Overlay Layer` (25), `Turn All Layers Off` (26), `Turn All Layers On` (27)이다. 각각 속성 설정, 해당 레이어 확대, 외부 파일 저장, 삭제, 새 레이어 생성과 전체 레이어 숨김·표시를 설명한다(20–27). 그림 1을 로컬에서 열었다(12–14). 위성 배경 위 하천 경계의 파란 선과 제어점 및 오버레이 RMC 메뉴를 보여 준다. |
| 29–43 | Overlay Properties — RMC의 Properties에서 속성을 연다(31). 설정 설명 원문: `- *Layer Name*: show the name of the layer, a new name can be entered here` (33); `- *Visible*: unchecking this box will hide the overlay layer (the light bulb of the layer in the Control Panel is also turned off)` (34); `- *Show in*` (35); `- *Selectable*` (36); `- *Editable*` (37); `- *Show Lines*: unchecking this box will hide the overlay lines` (38); `- *Line Settings*: allows the changing of setting style, color, and thickness of the lines.` (39). 그림 2를 열었다(41–43). Line Style 탭에 `Style: Solid`, `Width: 1.0`, `Close Polygon`, `Smooth`가 보인다(41, 그림 표시값이며 기본값 여부는 본문에 없다). |
| 44–56 | Overlay Properties의 추가 화면 — 그림 3–5를 모두 열었다(45·49·53). Data Points 탭은 `Show Markers`, `OpenGL Point`, `Style: Square`, `Size: 8.0`, `Pixels`, `Meters`, `Fill Color`, `Outline Color`, `Outline Thickness: 1.0`을 보여 준다(45, 그림 표시값). Labels 탭은 `Show Labels`와 `Label Options`를 보여 준다(49). Distance Labeling 탭에는 `Show Distance Labels`, `Number of Labels: 0`, `Units: Kilometers`, `Interval: 1 (km)`, `Value for First Point: 0 (km)`, Generate와 Reverse가 보인다(53, 그림 표시값). |
| 57–63 | Save As — 파일 종류·이름·폴더를 지정한 다음 Save를 누른다(59). 기본 확장자 원문: `Define the file type (\*.p2d is the default extension for overlay) then enter a file name.` (59). 그림 6을 열었다(61–63). 저장창은 `overlay.p2d`와 `Overlay Files (*.p2d;*.ldb;*.bln;*.xyz;*.dat;*.txt;*.shp;*.mif;*.kml;*.kmz)`를 보여 준다(61). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 10·16·31·59행: `#OverlayLayer:RMCOptions-Figure1` 등의 fragment를 참조하지만, 이 Markdown에는 같은 이름의 명시적 앵커가 없다.
- 35–37행: `Show in`, `Selectable`, `Editable`의 이름만 있고 기능 설명은 없다.
- 59행: 링크 표시는 `Figure 6`이지만 링크 대상은 `#OverlayLayer:RMCOptions-Figure5`이다.

