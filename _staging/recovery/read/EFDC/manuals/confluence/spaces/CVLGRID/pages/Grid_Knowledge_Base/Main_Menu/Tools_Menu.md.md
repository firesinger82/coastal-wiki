---
file: models/EFDC/raw/manuals/confluence/spaces/CVLGRID/pages/Grid_Knowledge_Base/Main_Menu/Tools_Menu.md
lines: 84
sha256: 534ed491c98f923ec762af3605376b381beb7b35b1eebab172350006ec70b79e
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Tools_Menu.md — 판독 구간 기록

구간은 1행부터 84행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | 문서 메타데이터 — 제목 `Tools Menu`, space `CVLGRID`, 원문 URL, 버전과 갱신 시각을 담는다(2–8). |
| 10–22 | Tools Menu 개요·기능 표 — 지리 참조(georeferencing) 배경 지도와 일반 설정 메뉴를 설명한다(10). 표에는 `Image Georeferencing` (18), `Coordinate Conversion` (19), `Unit Conversion` (20), `Settings` (21)가 있다. 각각 지도 참조, 한 점의 좌표계 변환, 길이·면적·체적 등의 단위 변환과 일반 설정을 제공한다. 그림 1을 열었다(12–14). 이 네 메뉴를 보여 준다. |
| 23–40 | Image Georeferencing / 그림 추가·제어점 — 오프라인 또는 사용자 소유 배경 지도를 위해 Google Earth에서 P1·P2를 정하고 `.jpg`로 저장한 뒤 Add Images로 연다(25–29). 기본 동작 원문: `By default, the coordinates of the four corner points of the image are updated in the *Control Points* frame` (31). 행 번호로 점을 선택하고 Find Point·Delete Point·Clear Point·Add Point를 사용한다(31). 그림 2·3을 열었다(33·37). 그림 2의 P1은 `Zone: 48 Q`, `Easting: 590673.00 m E`, `Northing: 2327262.00 m N`; P2는 `Zone: 48 Q`, `Easting: 582870.02 m E`, `Northing: 2329272.26 m N`이다(33). 빨간 화살표는 각 지도점에서 좌표창을 가리킨다(33). 그림 3 표의 열 이름은 `Image X (pixels)`, `Image Y (pixels)`, `World X (m)`, `World Y (m)`, `Error (m)`이다(37). 각 행의 표시값은 `0.000, 0.000, 0.000, 0.000, 0.000` (37, 그림 표 1행); `1919.000, 0.000, 1919.000, 0.000, 0.000` (2행); `1919.000, 1079.000, 1919.000, 1079.000, 0.000` (3행); `0.000, 1079.000, 0.000, 1079.000, 0.000` (4행)이다. |
| 41–49 | Image Georeferencing / World 좌표 입력 — Clear Points로 비운 뒤 스크롤 막대로 P1·P2를 찾는다(41). 설정 원문: `its Image X and Image Y are updated in the *Control Points* frame. Now enter the coordinates for World X and World Y (UTM coordinates) then press the Enter key, and it will jump to the second row.` (43). P2에도 같은 방식으로 UTM 좌표를 넣는다(44). 그림 4를 열었다(46–48). P1의 표시는 `Image X (pixels): 1587.000`, `Image Y (pixels): 674.000`, `World X (m): 590673`, `World Y (m): 2327262`, `Error (m): 2400007.091`이다(46). 빨간 화살표는 오른쪽 세로 막대와 아래 가로 막대를 가리킨다(46). |
| 50–61 | Image Georeferencing / 저장·그림 삭제 — `.geo` 종류로 저장하며 여러 그림에도 좌표를 지정할 수 있다(50·56). 확장자 지시 원문: `Select extension \*.geo for file type then click the *Save* button` (50). Remove Selected Image는 선택 그림을, Remove All Images는 모든 그림을 지운다(56). 그림 5·6을 열었다(52·58). 그림 5는 `Hanoi.geo`, `Georeferenced Files (*.geo)` 저장창과 제어점 표를 보여 준다(52). 표 열 순서는 Image X·Image Y·World X·World Y·Error이며 값은 `1587.000, 674.000, 590673, 2327262, 0.000` (52, 표 1행), `313.000, 342.000, 582870, 2329272, 0.000` (52, 표 2행)이다. 그림 6은 그림 삭제 RMC 메뉴와 `1587.000, 674.000, 590673.000, 2327262.000`, `313.000, 342.000, 582870.000, 2329272.000` 좌표 행을 보여 준다(58). |
| 62–69 | Coordinate Conversion — 입력 투영·단위를 정하고 값을 넣은 뒤 출력 투영·단위를 선택하여 Convert를 누른다(64). 조건 원문: `The *UTM Zone* in the *Convert to Coordinate System*frame must be defined when converting from Longitude, Latitude to UTM zone in meter or foot.` (64). 그림 7을 열었다(66–68). 입력은 `System: NAD83: North American 1983`, `Input: Degree`, `Longitude (°): -73.960782`, `Latitude (°): 40.737637`, `Altitude (m): 0`이다(66). 출력은 같은 System, `Units: Meter`, `X (m): 587746.19557763`, `Y (m): 4510152.28601953`, `Altitude (m): 0.000`이다(66). 추가 표시는 `UTM Zone: Zone 18`, `Central Meridian: -75`, `Longitude: 73°57'38.82"W`, `Latitude: 40°44'15.49"N`, `Scale Factor: 0.9996`이다(66). 이 값은 변환 예제의 화면 표시값이다. |
| 70–77 | Unit Conversion — 변환 종류·원래 단위·입력값·대상 단위·유효숫자 수를 정하고 출력값을 얻는다(72). 예제 설정 원문: `*Convert* (e.g Length)`; `*From Unit* (meter(m))`; `*Input* Value`; `*To Unit* (e.g foot (ft))`; `we can set the number of significant digits by entering a number (e.g 3)`; `*Output Value.*` (모두 72). 그림 8을 열었다(74–76). 표시값은 `Convert: Length`, `From Unit: meter (m)`, `Input Value: 100`, `To Unit: foot (ft)`, `Number of significant digits: 3`, `Output Value: 328.084`이다(74). |
| 78–84 | Settings — Settings에서 Global Settings를 연다(80). 기본값 정의 원문: `The values in this form are the default settings.` (80). 그림 9를 열었다(82–84). 기본값 표시는 `Column Factor: 5`, `Row Factor: 5` (Refinement Factors); `Number of Outer Iterations: 2`, `Number of Inner Iterations: 25`, `Number of Boundary Iterations: 25`, `Grid Orthogonalisation Factor: 0.975`, `Boundary Orthogonalisation Factor: 1` (Grid Orthogonalisation); `Number of Iterations: 20`, `Smoothing Factor: 0.5` (Grid Smoothing); `Attraction & Repulsion Factor: 0.1` (Line Attraction & Repulsion)이다(모두 82). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 10행: 여러 색상 CSS 문자열이 설명 문장 앞에 남아 있다.
- 10·27·31·41·44·50·56·64·72·80행: `#ToolsMenu-Figure1` 등의 fragment를 참조하지만, 이 Markdown에는 같은 이름의 명시적 앵커가 없다.
- 72·74행: 유효숫자 수를 설정한다고 설명하며 화면의 `Number of significant digits`는 `3`이다. 같은 화면의 `Output Value: 328.084`에는 0이 아닌 숫자 여섯 자리가 있다.

