---
file: models/EFDC/raw/manuals/confluence/spaces/EK/pages/EFDC_Explorer_12_Knowledge_Base/EFDC_Explorer_12_User_Guide/2DH_View/Menu_and_Toolbar_Items/Grid_Cell_Selection.md
lines: 45
sha256: 53843325c456f157cd467b989b64547f6499baae26498d9ec1694cf70a625865
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Grid_Cell_Selection.md — 판독 구간 기록

구간은 1행부터 45행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | 메타데이터 — 문서 ID, 제목, space, URL, 버전, 갱신 시각과 문서 계층을 기록한다(1–9). |
| 10–19 | 격자 셀 선택(Grid Cell Selection) 개요 — EE10의 셀 선택 기능을 2DH View 메뉴와 도구 모음에서 제공한다고 적는다(10). 그림 1은 주 메뉴의 Grid Cell Selection 하위 메뉴를 보여 준다(12–14). 그림 2는 도구 모음의 같은 선택 메뉴를 보여 준다(16–18). 두 그림을 직접 열었다. |
| 20–28 | 표 1 / 화면에서 선택 — Icon·Name·Description 표의 첫 다섯 기능을 설명한다(20–28). 이름·조건 원문: `Individual Cells` / `This function allows the user to select a single cell.` (24); `Line Crossing` / `This function allows the user to select multiple cells by drawing a line.` (25); `Inside Rectangle` / `When this function is selected, the user draws a rectangle by LMC and drags so that all cells inside the rectangle are selected.` (26); `Inside Polygon` / `When this function is selected, the user starts by drawing a polygon with LMC, and ends with RMC, so that all cells inside the polygon are selected.` (27); `Inside Circle` / `This option allows the user to draw a circle by LMC and then dragging to the size of the circle required, then all cells inside the circle will be selected.` (28). |
| 29–38 | 표 1 / 파일·조건·선택 관리 — `Crossing Polyline in File`은 파일 폴리라인(polyline)이 가로지르는 셀을 선택한다(29). `Inside Polygons in File`은 파일 다각형 내부 모든 셀을 선택한다(30). `Containing Points in File`은 파일의 점이 위치하는 모든 셀을 선택한다(31). `Using Criteria`의 조건 원문: `This allows the selection of the parameter and a criteria such as greater than, less than or equal to, for a certain value entered by the user.` (32). Apply로 적용한다(32). `Show Selected Cells`는 선택 셀의 `L, I, J cell indices` 표를 표시한다(33). `Invert Selection`은 선택·비선택 상태를 반전한다(34). `Clear Selection`은 기존 선택을 지운다(35). `Save Selection`은 선택을 저장하며 파일 확장자 원문은 `\*.SEL`이다(36). `Load Selection`은 저장한 선택을 읽는다(37). 표 Icon 열은 24–37행 모두 비어 있다. |
| 39–45 | 조건 선택과 선택 셀 표 — 그림 3을 직접 열었다(39–41). Grid Cell Selection by Value 창의 예시 필드는 `Parameter: Bottom Elevation IC`, `Comparison: >`, `Target Value: 15`이다. Apply to의 All Grid Cells와 Select Options의 Reset Current Selection이 선택되어 있으며 상태 표시에는 45개 셀이 선택되었다고 나온다(39행 그림). 이 값은 화면 예시 값이다. 그림 4를 직접 열었다(43–45). 선택 셀 목록의 열은 `#`, `L`, `I`, `J`, 체크 상자이며 완전히 보이는 행 값은 `1 34 5 6`, `2 35 6 6`, `3 36 7 6`, `4 37 8 6`이다. 다음 행은 화면 경계에서 일부 잘려 있다. 격자에는 선택된 사각형 영역이 표시되고 상태 표시는 20개 선택이다(43행 그림). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 24–37: 표 1의 Icon 열이 모두 비어 있다. 메뉴 그림 1·2에는 아이콘이 표시되어 있다.
- 43행 그림 4: Selected Cells 표의 아래 행들이 화면 경계와 스크롤 영역 밖에 있어 전체 목록을 판독할 수 없다.

