---
file: models/EFDC/raw/manuals/confluence/spaces/CVLGRID/pages/Grid_Knowledge_Base/Main_toolbar_buttons/Create_a_rectangular_grid.md
lines: 37
sha256: 2d036700b56120dcb4ce18d5749497c25085433f51730c91563e1c54f464b944
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Create_a_rectangular_grid.md — 판독 구간 기록

구간은 1행부터 37행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | 문서 메타데이터 — 제목 `Create a rectangular grid`, space `CVLGRID`, 원문 URL, 버전과 갱신 시각을 담는다(2–8). |
| 10–17 | 직사각형 격자(rectangular grid) 생성 — 두 차원의 구조 격자(structured grid)를 만든다(10). 버튼을 누르면 Rectangular Grid 창이 열린다(16). 그림 1을 열었다(12–14). 빨간 사각형이 직사각형 격자 버튼을 표시한다. |
| 18–24 | Rectangular Grid 설정 — 매개변수 원문: `- *Min. Cell Size (m)*: the dimension of the grid cell in meters along the I and J direction` (18); `- *Growth Factors*: the expansion of the cell dimension in the I or J direction` (19); `- *Number of Cells*: the number of cells to generate a new grid` (20); `- *UTM* Zone: this is the Universal Transverse Mercator (UTM) zone number, from 1 to 60. After entering the location of the focal point, the UTM zone can be updated automatically` (21); `- *Location of Focal Point:* the longitude and latitude in degrees of the focal point in geographic coordinate system` (22); `- *Rotation(deg.) :* the angle in degrees to rotate the grid` (23). |
| 25–30 | 이동·회전·확장 — 중심점(focal point)으로 이동하고 모서리점(corner point)으로 회전하며 측면점(side point)으로 늘리거나 줄인다(25). 확장 원문: `cells are added and have the same size as the previous cells.` (25). 그림 2를 열었다(27–29). I방향 표시는 `Min. Cell Size (m): 100`, `Growth Factors: 0`, `Number of Cells: 10`이며 J방향도 각각 `100`, `0`, `10`이다(27). 공통 표시는 `UTM Zone: 48`, `Longitude (deg.): 105.93558120`, `Latitude (deg.): 21.034626007`, `Rotation (deg.): 0`이다(27, 기본값 여부 본문 명시 없음). |
| 31–37 | 직사각형 격자 그림 — 그림 3·4를 열었다(31·35). 그림 3은 초록 직교 격자선과 빨간 외곽선, 중앙의 Focal Point, 오른쪽 중앙 Side Point, 오른쪽 위 Corner Point를 원으로 강조한다(31). 그림 4의 빨간 화살표는 오른쪽으로 이동한 측면점과 확장 방향을 가리킨다(35). 두 화면의 정보 창은 `Number of cells: 100`, `Dimensions: 11 x 11`이다(31·35). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 10행: 색상 CSS 문자열이 설명 문장 앞에 남아 있다.
- 10·16·25행: `#Createarectangulargrid-Figure1` 등의 fragment를 참조하지만, 이 Markdown에는 같은 이름의 명시적 앵커가 없다.
- 25·31·35행: 본문은 확장 시 셀이 추가된다고 적는다. 그림 3·4의 정보 창은 모두 `Number of cells: 100`, `Dimensions: 11 x 11`로 표시한다.

