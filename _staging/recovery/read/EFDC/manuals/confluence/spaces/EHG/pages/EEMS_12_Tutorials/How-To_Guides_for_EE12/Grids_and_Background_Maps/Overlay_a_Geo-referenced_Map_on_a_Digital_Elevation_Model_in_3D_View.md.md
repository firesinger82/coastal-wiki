---
file: models/EFDC/raw/manuals/confluence/spaces/EHG/pages/EEMS_12_Tutorials/How-To_Guides_for_EE12/Grids_and_Background_Maps/Overlay_a_Geo-referenced_Map_on_a_Digital_Elevation_Model_in_3D_View.md
lines: 50
sha256: 83d80b5e4d154358dfb39922c15e53e833ae7d7070afe48f3de51e9c61012821
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Overlay_a_Geo-referenced_Map_on_a_Digital_Elevation_Model_in_3D_View.md — 판독 구간 기록

구간은 1행부터 50행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–13 | 메타데이터와 안내 범위이다(1–13). Google Earth의 지리참조 지도(geo-referenced map)를 3D 보기에서 수치표고모델(digital elevation model, DEM) 표면에 입히는 안내이다(10). 예제는 DM-13이다(12). |
| 14–27 | Generate DEM 절이다(14–27). DM-13의 2DH View에서 Layer Control의 Generate DEM을 선택한다(16, 18). 화면의 `Bottom Elevation (m)` 범례 양 끝은 `10.000`, `10.000`이다(18). 입력 파일 패턴은 `terrain\*.xyz`, 출력 형식은 `TB2`이다(20). 좌표·해상도 설정과 셀 수의 관계는 `Once the option is selected, the *Generate DEM* form will appear as shown in [Figure 2](https://eemodelingsystem.atlassian.net/wiki/spaces/EHG/pages/1133215756#OverlayaGeo-referencedMaponaDigitalElevationModelin3DView-Figure2). From this form, the user can click on *Add File* then browse to the digital elevation data file (terrain\*.xyz) from the Data folder. Once loaded, the coordinates of the *Lower-Left* and *Upper-Right* points will be updated as well as the *Cell Size* and *Number of Cells,* the user can change the *Cell Size* then click on the Calculator symbol to update the *Number of Cells* and vice versa. The more cells the higher resolution of the DEM file. The output format for the generated DEM files is TB2, click the *Generate DEM* button to start generating DEM file.` (20). Generate DEM 그림의 X Direction / Y Direction 값은 `Lower-Left (m)`: `487683.78125` / `3401278.75`, `Upper-Right (m)`: `512039.1875` / `3422095.75`, `Cell Size (m)`: `50` / `50`, `Number of Cells`: `488` / `417`이다(22). `Sink with Current Model`은 선택되어 있다(22). `Interpolation Algorithm`의 `Inverse Distance Weighting (IDW)`, `Delaunay Triangulation`, `Kriging`은 비활성 상태이다(22). `Output Format`은 `TB2 Grid Format`이 선택되어 있고 `ArcGIS ASCII Grid`, `Surfer ASCII Grid`도 표시된다(22). 저장 예시는 `File Name`의 `DEM`이다(24). 저장 화면은 `DEM.tb2`와 `TB2 Grid (*.tb2)`를 보여 준다(26). |
| 28–37 | Load a DEM file in 3D View 절이다(28–37). 외부 레이어 가져오기로 Data 폴더의 `DEM.tb2`를 연다(30). 그림은 Open External Layer의 파일 선택과 DEM 레이어가 추가된 3D 지형을 보여 준다(32). 지형 범례는 `DEM`, 값은 `10.000`–`1561.477`, `Vertical Exaggeration: 5`이다(32). 격자와 DEM이 맞지 않는다고 설명한다(34). DEM 레이어를 오른쪽 클릭하여 Properties를 여는 그림이다(36). |
| 38–45 | DEM 방향 반전과 수직 배율(vertical exaggeration) 조정이다(38–45). DEM Layer Properties에서 `Flip`을 누른다(38, 40). 속성 그림의 `Layer Name`은 `DEM`이다(40). `Visible`, `Show in Legend`, `Show as Raster`, 비활성 `Shaded Relief`는 선택되어 있다(40). `Single Color`, `Reverse`, `Use Overlay Image`는 선택되어 있지 않다(40). `Min. Value`는 `10.0000`, `Max. Value`는 `1561.4770`, `Automatic`은 선택되어 있다(40). `Color Ramp`는 `Default`이고 낮은 값은 파랑, 높은 값은 빨강이다(40). `Under Range`는 파랑, `Over Range`는 빨강이다(40). `Flip North - South`와 `Sink with Current Model`은 선택되어 있다(40). `Vertical Exaggeration`은 `0.2`, `Datum Adjustment`는 `0`, `Sink Factor`는 `1.5`, `Sink Offset`은 `-2`이다(40). DEM Info 표는 `DEM Size` = `245 × 209`, `Cell Size (m)` = `100.000 × 100.000`, `X Range (m)` = `487683.781 - 512083.781`, `Y Range (m)` = `3401278.750 - 3422078.750`를 표시한다(40). 아래 `Z Range (m)` 행의 값 `10.000 - 1561.477`은 화면 하단에서 일부 잘려 보인다(40). 본문은 두 창에서 `Vertical Scale Modifier`를 바꾼다고 적는다(42). 3D View Settings 그림은 `Main Title` = `EFDC+ Testing`, `Sub Title` = `3 Gorges Dam`, `Easting Scale Modifier` = `1`, `Northing Scale Modifier` = `1`, `Vertical Scale Modifier` = `1`을 보여 준다(44). 주 제목의 `Visible`은 선택되어 있고 부제의 `Visible`과 `Draw Axes`는 선택되어 있지 않다(44). URL 파일명의 괄호를 제거한 로컬 사본을 열었다(44). |
| 46–50 | Use Overlay Image 절이다(46–50). `Use Overlay Image`를 선택하고 Map-Images 폴더의 `map\_geo.jgw`를 연다(48). 첫 그림은 해당 옵션 선택과 `map_geo.jgw` 경로를 보여 준다(50). 속성 값과 DEM Info 표는 앞 그림과 같다(40, 50). 두 번째 그림은 위성 영상이 지형 표면에 입혀지고 흰 모델 격자가 겹친 3D 지형을 보여 준다(50). 범례는 `DEM`, 값은 `10.000`–`1561.477`, `Vertical Exaggeration: 5`이다(50). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- Figure 1–10의 URL은 조각 식별자를 사용하지만 이 파일에는 대응하는 명시적 앵커가 없다(16, 20, 24, 30, 34, 38, 42, 48).
- 본문은 DEM Layer Properties에서도 `Vertical Scale Modifier`를 바꾼다고 적지만 해당 그림의 항목 이름은 `Vertical Exaggeration`이다(40, 42).
- 44행 URL의 파일명은 `9-17-2020 9-42-07 AM(1).png`이다. 지정된 변환 경로에는 파일이 없다. 폴더 목록에서 확인한 `9-17-2020_9-42-07_AM1.png`를 열었다(44).
