---
file: models/EFDC/raw/manuals/confluence/spaces/CVLGRID/pages/Grid_Knowledge_Base/Grid_Operation/Load_an_Existing_Grid.md
lines: 41
sha256: 1085a9b33b88182e6a90d5cae78043809c135bc80cf564440fe9ddf3c352d594
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Load_an_Existing_Grid.md — 판독 구간 기록

구간은 1행부터 41행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–19 | Load an Existing Grid / 가져오기 — 페이지 식별 정보를 포함한다(1–9). Grid+1.2에서 기존 격자를 불러오는 경로와 호환 형식을 원문대로 옮긴다. 원문: ``Grid+1.2 allows loading an existing grid built under several formats, the most EE-compatible of which are \*.gpc, \*.cvl and \*.grd. To import a grid, navigate towards the *Import Grid* buttons that are accessible in *File* > *Import* ([Figure 1](#LoadanExistingGrid-Figure-1)) or the Toolbars ([Figure 2](#LoadanExistingGrid-Figure-2)). Browse to the file location after *Import Grid* and select to open the grid.`` (10). 그림 1은 File·Import·`Import Grid` 메뉴를 보여 준다(12). 그림 2는 도구모음의 `Import Grid`를 보여 준다(16). |
| 20–29 | Load an Existing Grid / 좌표 정보 유무 — 파일에 투영 정보가 있으면 자동으로 좌표계를 읽어 배경 지도 위에 배치하며 정보가 없으면 왜곡될 수 있다고 설명한다(20). 원문: ``A grid file may or may not contain its projection information. In the former case, Grid+1.2 automatically reads the abided coordinate system and overlays the grid accurately on its geographical location in the background map, for example as in [Figure 3](#LoadanExistingGrid-Figure-3). In the latter case, the grid display is prone to distortion, immediately noticeable in the working domain ([Figure 4](#LoadanExistingGrid-Figure-4)).`` (20). 그림 3은 카스피해(Caspian Sea)에 겹친 노란 격자와 `Curvilinear Grid: 5186`, `Dimensions: 76 × 129`, `Coordinate: UTM Zone 39`를 보여 준다(22). 그림 4는 흰 영역에 가로선으로 보이는 격자와 `Coordinate: UTM Zone 0`을 보여 준다(26). 캡션은 `*.grd` 파일의 투영 정보 미지정이라고 적는다(28). |
| 30–41 | Load an Existing Grid / 좌표계 정의 — 격자 Properties·Coordinate System·Define에서 geographic 또는 UTM 좌표계를 선택한 뒤 Zoom to Layer를 적용한다(30). 예시는 기본값으로 설명하지 않는다. 원문: ``To fix the distortion issue, the user needs to define the projection of the grid. To do this, right-mouse click on the grid layer in the *Layer Control* and then select *Properties*. The *Grid Settings* form will pop up ([Figure 5](#LoadanExistingGrid-Figure-5)). Move to the *Coordinate System* tab, click the *Define* button. Then, the user should select the proper spatial reference, either geographic or UTM coordinate system. In the Caspian Sea case study, for example, the correct coordinate system is *UTM, Northern Hemisphere, UTM Zone 39* ([Figure 6](#LoadanExistingGrid-Figure-6)). Click the OK button to finish projection-defining. Next, right-mouse click on the grid layer in the *Layer Control*, then select *Zoom to Layer* option, the grid will be located in the right place ([Figure 7](#LoadanExistingGrid-Figure-7)).`` (30). 그림 5는 Grid Settings의 Grid Lines 화면이다(32). `Layer Name: Grid`, `Layer Visible` 체크, `Show Lines` 체크, `Style: Solid`, 초록 `Color`, `Width: 1.0`이 보인다(32). 그림 6은 `Projection: UTM, Northern Hemisphere`, `UTM Zone 39 (48°E – 54°E)`와 좌표 참조 정보를 보여 준다(35). 좌표 참조 정보의 예시 줄은 `PROJCS["WGS 84 / UTM zone 39N", GEOGCS["WGS 84", DATUM["World_`; `Geodetic_System_1984", SPHEROID["WGS 84", 6378137, 298.257223563,`; `AUTHORITY["EPSG", "7030"]], AUTHORITY["EPSG", "6326"]],`; `PRIMEM["Greenwich", 0, AUTHORITY["EPSG", "8901"]], UNIT["degree",`; `0.017453292519943295, AUTHORITY["EPSG", "9102"]], AUTHORITY["EPSG",`; `"4326"]], PROJECTION["Transverse_Mercator", AUTHORITY["EPSG",`; `"9807"]], PARAMETER["latitude_of_origin", 0],`; `PARAMETER["central_meridian", 51], PARAMETER["scale_factor", 0.9996],`; `PARAMETER["false_easting", 500000], PARAMETER["false_northing", 0],`; `UNIT["metre", 1, AUTHORITY["EPSG", "9001"]], AXIS["East", EAST],`; `AXIS["North", NORTH], AUTHORITY["EPSG", "32639"]]` (35, 그림 6; 화면 줄바꿈 기준). 그림 7은 카스피해에 겹친 초록 격자를 보여 주지만 좌하단은 `Coordinate: UTM Zone 0`으로 적혀 있다(39). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 30·35·39행: 본문과 좌표 정보 창은 UTM Zone 39를 지정하지만 최종 그림 7의 좌하단에는 `Coordinate: UTM Zone 0`이 표시된다.

