---
file: models/EFDC/raw/manuals/confluence/spaces/CVLGRID/pages/Grid_Knowledge_Base/Main_toolbar_buttons.md
lines: 84
sha256: 2cb22ce85855cec672889059ed1ed66ed63c9ae62020c97651feef14e3f1cb0d
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Main_toolbar_buttons.md — 판독 구간 기록

구간은 1행부터 84행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | 문서 메타데이터 — 제목 `Main toolbar buttons`, space `CVLGRID`, 원문 URL, 버전과 갱신 시각을 담는다(2–8). |
| 10–17 | 주 도구막대 개요 — 격자 생성·개선의 주요 기능을 모았다고 적는다(10). 그림 1을 열었다(12–14). 프로젝트·입출력·보기·선택·절점 편집·격자·설정·측정·프레임 아이콘이 가로로 나열되어 있다. |
| 18–30 | 주 도구막대 / 프로젝트·보기·편집 — New Project는 작업공간의 모든 자료를 지우고 Load는 프로젝트를 연다(18–19). Save는 전체 프로젝트를 `.GPP`에 저장하며, 원문은 `This is a general layout file, not the grid file loaded into EE.`라고 구분한다(20). Import·Export, Layer Control 표시 토글, 전체 영역 보기, 이전 보기 복원, 객체 선택이 이어진다(21–26). `Mode node`는 격자·폴리라인(polyline)·스플라인(spline) 절점 이동, Add node는 절점 추가, Delete node는 절점 제거를 설명한다(27–29). 다각형(polygon)에 의한 객체 편집도 있다(30). |
| 31–45 | 주 도구막대 / 선·격자·설정 — 새 폴리라인과 스플라인 추가(31–32), Undo·Redo(33–34), 스플라인·직사각형·방사형 격자 생성(35–37), Refine·Coarse·Orthogonalize·Merge(38–41), Global settings·Measurement Tool(42–43), North Arrow와 Scale bar를 추가하는 Frame control(44)을 나열한다. |
| 46–69 | Import 메뉴 / 입력 파일 — Import Grid는 Grid+·RGF·ECOMSED·SEAGRID 등을 연다(46–48). 파일·열 형식 원문을 옮긴다: `*Import EFDC Model*: open the EFDC input file (e.g corners.inp, dxdy.inp, lxly.inp)` (50); `*Import Georeferenced Image*: open a georeferenced background image (e.g \*.jgw, \*.geo)` (52); `*Import Overlay*: open an overlay file as shoreline, polyline, polygon (\*.p2d, \*.shp)` (54); `*Import Splines*: open the splines file (\*.spl), this is a native file created from Grid+` (56); `*Import Labels*: open the label file (\*.dat, \*.p2d), this file has three columns. Two columns for coordinates (X, Y), and the third column is label names.` (58); `*Import Cross-Sections*: open the cross-section file (\*.ldb, \*.p2d), this file has three columns. Two columns are for coordinates (X, Y), and the third column is for elevation.` (60); `*Import DEM*: open the DEM (Digital Elevation Models) file (\*.txt, \*.asc, \*.grd, \*.tb2). DEMs are files that contain either points (vector) or pixels (raster), with each point or pixel having an elevation value.` (62); `*Import Scatter Data*: open the scatter dât file (\*.xyz, \*.dat) this file has three columns. Two columns are for coordinates (X, Y), and the third column is for elevation.` (64). 그림 2를 열었다(66–68). 이 아홉 가져오기 메뉴를 보여 준다. |
| 70–84 | Export 메뉴 / 출력·적용 범위 — 격자 출력 원문: `*Export Grid*: export the selected grid layer to the native grid file of Grid+ (\*.gpc), CVLGrid (\*.cvl), Delft3D (\*.grd), and others.` (72). EFDC 출력은 `corners.inp, dxdy.inp, lxly.inp` 세 파일이며 격자를 편집한 뒤 경계조건을 변경하지 않고 EEMS에서 다시 열 수 있다고 적는다(74). 새 모델 조건 원문: `If the user wants to create a wholly new model, including the EFDC.INP etc, then that should be done in EE rather than in Grid+ .` (74). Shapefile·KML을 관련 GIS/지도 프로그램에서 열 수 있다(76–78). 그래픽 출력 형식은 `\*.png, \*.jpg, and others.`이다(80). 그림 3을 열었다(82–84). Export Grid, Export To EFDC, Export To Shapefile, Export To KML, Export Graphics를 보여 준다. |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 10·46·70행: `#Maintoolbarbuttons-Figure1` 등의 fragment를 참조하지만, 이 Markdown에는 같은 이름의 명시적 앵커가 없다.
- 18–44행: 기능 표의 Buttons 칸은 모든 행에서 비어 있다.
- 27행: 이동 기능을 설명하는 이름이 `Mode node`로 적혀 있다.

