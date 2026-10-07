---
file: models/EFDC/raw/manuals/confluence/spaces/EK/pages/Data_Format_B-8_Google_Earth_KML_file.md
lines: 14
sha256: 656ce46aca1d3155b7082c6a4abfdf1ef51b8e92d4fb59fdf4ca9189c444926e
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Data_Format_B-8_Google_Earth_KML_file.md — 판독 구간 기록

구간은 1행부터 14행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | 메타데이터 — 페이지 제목은 `"Data Format B-8 Google Earth KML file"` (3)이다. `id: 1585709183` (2), `space: EK` (4), `version: 2` (6), `updated: 2021-11-10T04:10:35.659Z` (7)를 기록한다. 원문 URL (5)과 문서 경로 (8)가 있다. 1·9행은 frontmatter 구분선이다. |
| 10–11 | Google Earth KML file — KML은 Google Earth 같은 Earth browser에서 지리 자료(geographic data)를 표시하는 파일 형식이라고 적는다 (10). XML 표준을 기반으로 중첩 요소(element)와 속성(attribute)을 갖는 태그(tag) 구조를 사용한다 (10). 구조 원문: `KML is a file format used to display geographic data in an Earth browser such as Google Earth. KML uses a tag-based structure with nested elements and attributes and is based on the XML standard.` (10). 11행의 빈 줄을 포함한다. |
| 12–14 | Example — 예시 표제 (12), 빈 줄 (13), 그림 참조 (14)를 포함한다. 로컬 `attachments/1585709183/B-10.png`를 열었다 (14). Notepad++의 `BotElevation.kml` 화면은 `Bottom Elevation` 문서와 셀 폴리곤의 스타일·좌표를 보여 준다 (14). 탭과 공백의 구분은 이미지에서 확정하지 못했다. 그림에서 완전하게 보이는 입력 예시 1–28행: `  <?xml version='1.0' encoding='UTF-8'?>` (14, 그림 예시 1행); `  <kml xmlns="http://www.opengis.net/kml/2.2" xmlns:gx="http://www.google.com/kml/ext/2.2" xmlns:kml="http://www.opengis.net/kml/2.2" xmlns:atom="http://www.w3.org/2005/Atom">` (14, 그림 예시 2행); `    <Document>` (14, 그림 예시 3행); `      <name>Bottom Elevation</name>` (14, 그림 예시 4행); `      <description>Generated with EEMS by DSI, LLC</description>` (14, 그림 예시 5행); `      <open>1</open>` (14, 그림 예시 6행); `      <Placemark>` (14, 그림 예시 7행); `        <name>Cell 2 (43,3)</name>` (14, 그림 예시 8행); `        <visibility>1</visibility>` (14, 그림 예시 9행); `        <Style id="Cell_1">` (14, 그림 예시 10행); `          <LineStyle>` (14, 그림 예시 11행); `            <color>FFD3D3D3</color>` (14, 그림 예시 12행); `            <width>1</width>` (14, 그림 예시 13행); `            <labelVisibility>1</labelVisibility>` (14, 그림 예시 14행); `          </LineStyle>` (14, 그림 예시 15행); `          <PolyStyle>` (14, 그림 예시 16행); `            <color>FF0000FF</color>` (14, 그림 예시 17행); `            <fill>1</fill>` (14, 그림 예시 18행); `            <outline>1</outline>` (14, 그림 예시 19행); `          </PolyStyle>` (14, 그림 예시 20행); `        </Style>` (14, 그림 예시 21행); `        <styleUrl>#Cell_1</styleUrl>` (14, 그림 예시 22행); `        <Polygon>` (14, 그림 예시 23행); `          <extrude>0</extrude>` (14, 그림 예시 24행); `          <tessellate>0</tessellate>` (14, 그림 예시 25행); `          <altitudeMode>relativeToSeaFloor</altitudeMode>` (14, 그림 예시 26행); `          <outerBoundaryIs>` (14, 그림 예시 27행); `            <LinearRing>` (14, 그림 예시 28행). 예시 29행에서 완전하게 보이는 앞 세 좌표까지의 접두부(prefix): `              <coordinates>-80.764866131941,26.6807886241599,-1.500 -80.764869136544,26.6891223518377,-1.500 -80.755702111774,26.6891249359289,-1.500` (14, 그림 예시 29행 일부). 29행의 오른쪽 나머지는 그림 밖에 있어 전사하지 않았다. 입력 예시 30–43행: `            </LinearRing>` (14, 그림 예시 30행); `          </outerBoundaryIs>` (14, 그림 예시 31행); `        </Polygon>` (14, 그림 예시 32행); `      </Placemark>` (14, 그림 예시 33행); `      <Placemark>` (14, 그림 예시 34행); `        <name>Cell 3 (44,3)</name>` (14, 그림 예시 35행); `        <visibility>1</visibility>` (14, 그림 예시 36행); `        <Style id="Cell_2">` (14, 그림 예시 37행); `          <LineStyle>` (14, 그림 예시 38행); `            <color>FFD3D3D3</color>` (14, 그림 예시 39행); `            <width>1</width>` (14, 그림 예시 40행); `            <labelVisibility>1</labelVisibility>` (14, 그림 예시 41행); `          </LineStyle>` (14, 그림 예시 42행); `          <PolyStyle>` (14, 그림 예시 43행). 화면 밖의 태그와 좌표는 전사하지 않았다. |

수식 전사: 0개. 매개변수·입력 필드 이름 전사: 21개 (`version`, `encoding`, `xmlns`, `xmlns:gx`, `xmlns:kml`, `xmlns:atom`, `name`, `description`, `open`, `visibility`, `id`, `color`, `width`, `labelVisibility`, `fill`, `outline`, `styleUrl`, `extrude`, `tessellate`, `altitudeMode`, `coordinates`).
이 집계는 전사한 이름의 종류 수이다. 예시 값은 기본값으로 간주하지 않았다.
참조 그림 1개를 로컬 파일로 직접 열어 확인했다.

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 14 (그림 예시 29·43행): 29행의 좌표는 그림 오른쪽 경계를 넘어가므로 한 행 전체와 닫는 태그가 보이지 않는다. 그림 아래쪽은 43행 `<PolyStyle>`에서 끝나므로 뒤의 XML 내용은 보이지 않는다.
