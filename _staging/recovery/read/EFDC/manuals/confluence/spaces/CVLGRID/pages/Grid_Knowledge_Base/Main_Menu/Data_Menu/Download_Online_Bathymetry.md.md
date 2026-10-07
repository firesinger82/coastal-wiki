---
file: models/EFDC/raw/manuals/confluence/spaces/CVLGRID/pages/Grid_Knowledge_Base/Main_Menu/Data_Menu/Download_Online_Bathymetry.md
lines: 56
sha256: 8b913d1143f02c2b2b824db4d25e3df21a089a52951fdc1e5b689148254790c3
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Download_Online_Bathymetry.md — 판독 구간 기록

구간은 1행부터 56행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | 문서 메타데이터 — 제목 `Download Online Bathymetry`, space `CVLGRID`, 원문 URL, 버전과 갱신 시각을 담는다(2–8). |
| 10–17 | 다운로드 자료·영역·좌표계 — Grid+에서 GEBCO 자료를 내려받는다고 적는다(10). 해상도·단위 원문: `The GEBCO\_2021 Grid is a global terrain model for ocean and land, providing elevation data in meters on a 15 arc-second interval grid.` (10). 영역 파일 원문: `The overlay file can be in different formats, such as land boundary (\*.LDB), \*.kml, \*.kmz, \*.shp` (12). 좌표계 원문: `The file coordinates can be in a geographic coordinate system (Latitude, Longitude) or the Universal Transverse Mercator (UTM) coordinate system.` (14). |
| 18–29 | 1. Open the overlay file — 오버레이(overlay) 파일을 연 뒤 다각형(polygon) 레이어 RMC의 Zoom to Layer를 사용한다(18·24). 그림 1·2를 열었다(20·26). 그림 1은 Import Overlay 메뉴와 해안을 감싼 빨간 다각형을 보여 준다(20). 그림 2는 polygon 레이어의 Zoom to Layer 메뉴를 보여 준다(26). |
| 30–47 | 2. Access Data menu — Download Online Bathymetry를 열고 GEBCO 2021을 선택한 뒤 Data Extraction Limits의 Update를 누른다(32–36). 선택·조건 원문: `Select Data Set: GEBCO 2021` (34); `Check on Using Polygon File and browse to the file. If the polygon file differs from the file loaded and displayed in the Layer Control, it should click the Update button again.` (38). Download를 누른다(40). 그림 3·4를 열었다(42·46). 그림 3은 다운로드 메뉴를 보여 준다. 그림 4의 `Data Set: GEBCO 2021`, `Data Field: elevation: Bottom Elevation`이 보인다(46). Spatial Information의 Longitude는 `Min.: -179.998`, `Max.: 179.998`, `Interval: 0.004167`, `#: 86400`, Latitude는 `Min.: -89.998`, `Max.: 89.998`, `Interval: 0.004167`, `#: 43200`이다(46). Data Extraction Limits의 Longitude는 `Min.: -75.114841`, `Max.: -74.192597`, `#: 221`, Latitude는 `Min.: 38.221408`, `Max.: 39.362236`, `#: 273`이다(46). `Time Zone: 0`, 선택된 `Using Polygon File`, 경로 `M:\EEMS\Testing\Grid+\Online_Bath\polygon.ldb`, 미선택 `Save Log File`이 보인다(46). 이 값들은 그림 표시값이며 기본값 여부는 본문에 없다. |
| 48–51 | 다운로드 결과 — 지정 영역의 수심 자료를 내려받아 elevation 레이어를 추가한다고 적는다(48). 그림 5를 열었다(50). 위성 배경에 빨간 영역 다각형과 사각형 고도 래스터(raster)가 겹쳐 있으며 색상은 빨강·노랑·초록·파랑이고 숫자 범례는 없다. |
| 52–56 | 3. Export bathymetry to a file — elevation 레이어의 Save As에서 Export DEM을 열고 이름·종류를 지정한 뒤 Save를 누른다(54). 그림 6·7을 모두 열었다(56, 같은 원문 행의 두 그림). 그림 6은 elevation 레이어의 Save As 메뉴를 보여 준다. 그림 7에는 `File name: Bathymetry.xyz`와 `ArcGIS ASCII Grid (*.asc)`, `Surfer ASCII Grid (*.grd)`, `TB2 Grid (*.tb2)`, `XYZ Data File (*.xyz)`가 보인다(56). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

없음

