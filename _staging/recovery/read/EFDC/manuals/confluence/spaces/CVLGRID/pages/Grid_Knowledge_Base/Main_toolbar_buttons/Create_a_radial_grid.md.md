---
file: models/EFDC/raw/manuals/confluence/spaces/CVLGRID/pages/Grid_Knowledge_Base/Main_toolbar_buttons/Create_a_radial_grid.md
lines: 43
sha256: 9795ec53c33b162181a00b8806cdc03ff7a5d3aa2ee804f3d82747a4659f0037
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Create_a_radial_grid.md — 판독 구간 기록

구간은 1행부터 43행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | 문서 메타데이터 — 제목 `Create a radial grid`, space `CVLGRID`, 원문 URL, 버전과 갱신 시각을 담는다(2–8). |
| 10–17 | 방사형 격자(radial grid) 생성 — 주 도구막대 버튼을 누르면 Radial Grid 창이 열린다(10·16). 그림 1을 열었다(12–14). 빨간 사각형이 방사형 격자 버튼을 표시한다. |
| 18–30 | Radial Grid 설정 — I방향 각도와 J방향 반지름 및 중심 좌표를 정의한다(18–29). 매개변수 원문: `- *Start Angle (deg.):* this is the angle in degrees where the grid cell begins.` (20); `- *Stop Angle (deg.):* this is the angle in degrees where the grid cell ends.` (21); `- *Angle Increment (deg)*: the increasing angle in each step.` (22); `- *Min. Radius (m)*: the radius of the curve inside in meters` (26); `- *Max. Radius (m):* the radius of the curve outside in meters` (27); `- *UTM Zone*: this is the Universal Transverse Mercator (UTM) zone number from 1 to 60. After entering the location of the focal point, the UTM zone can be updated automatically.` (28); `- *Location of Focal Point*: the longitude and latitude in degrees of the center point in the geographic coordinate system` (29). |
| 31–36 | 생성·이동·확장 — 레이어를 선택한 상태에서 중심점(focal point)으로 격자를 이동하고 측면점(side point)으로 옆면을 늘리거나 줄인다(31). 원문: `cells are added and have the same size as the previous cells.` (31). 그림 2를 열었다(33–35). 표시값은 `Start Angle (deg.): 90`, `Stop Angle (deg.): 180`, `Angle Increment (deg.): 3`, `Min. Radius (m): 1000`, `Max. Radius (m): 5000`, `UTM Zone: 48`, `Longitude (deg.): 105.88309720`, `Latitude (deg.): 21.019923835`이다(33, 기본값 여부 본문 명시 없음). |
| 37–43 | 방사형 격자 그림 — 그림 3·4를 열었다(37·41). 초록 격자선과 빨간 외곽선으로 원호와 방사 방향이 교차하는 격자를 보여 준다(37). 그림 3의 Focal Point는 원호 중심의 십자 표식, Side Point는 왼쪽 직선 경계 위의 원으로 강조한 점이다(37). 그림 4의 빨간 화살표는 측면점이 왼쪽으로 이동하는 확장 방향을 가리킨다(41). 두 화면의 정보 창은 `Dimensions: 31 x 32`이다(37·41). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 10행: 색상 CSS 문자열이 설명 문장 앞에 남아 있다.
- 10·16·31행: `#Createaradialgrid-Figure1` 등의 fragment를 참조하지만, 이 Markdown에는 같은 이름의 명시적 앵커가 없다.
- 31·37·41행: 본문은 확장 시 셀이 추가된다고 적는다. 그림 3·4의 정보 창은 모두 `Dimensions: 31 x 32`로 표시한다.

