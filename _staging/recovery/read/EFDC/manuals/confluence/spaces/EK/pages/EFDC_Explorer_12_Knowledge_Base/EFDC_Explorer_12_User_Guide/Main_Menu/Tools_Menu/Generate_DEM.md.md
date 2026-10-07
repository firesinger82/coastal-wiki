---
file: models/EFDC/raw/manuals/confluence/spaces/EK/pages/EFDC_Explorer_12_Knowledge_Base/EFDC_Explorer_12_User_Guide/Main_Menu/Tools_Menu/Generate_DEM.md
lines: 20
sha256: 5dab34dcb3dab499df4c10b2233920c73a59ca2a706e9637a6ec78491e3d1a8b
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Generate_DEM.md — 판독 구간 기록

구간은 1행부터 20행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | 문서 메타데이터 — 페이지 ID, 제목, space, 원문 URL, 버전, 갱신 시각, 문서 계층 경로와 frontmatter 구분선을 포함한다(1–9). |
| 10–13 | Generate DEM / 메뉴 — Tools에서 Generate DEM을 선택한다(10). 그림 `10-13-2021_1-32-37_PM.png`는 해당 메뉴를 강조한다(12). 빈 줄·마크업을 포함한다(11–13). |
| 14–17 | Generate DEM / 자료·해상도·출력 — 수치 표고 자료(digital elevation data)를 불러오고 셀 크기·셀 수를 바꾸는 관계, 파일 이름 패턴과 TB2 형식을 그대로 옮긴다: `Once the option is selected, the *Generate DEM* form will appear as shown in [Generate DEM#Figure 2](https://eemodelingsystem.atlassian.net/wiki/spaces/EK/pages/2082832412#GenerateDEM-Figure2). From this form, the user can click on *Add File* then browse to the digital elevation data file (terrain\*.xyz) from the Data folder. Once loaded, the coordinates of the *Lower-Left* and *Upper-Right* points will be updated as well as the *Cell Size* and *Number of Cells,* the user can change the *Cell Size* then click on the Calculator symbol to update the *Number of Cells* and vice versa. The more cells the higher resolution of the DEM file. The output format for the generated DEM files is TB2, click the *Generate DEM* button to start generating DEM file.` (14). 그림 `12-4-2020_2-43-37_PM.png`는 Data Files의 `terrain [19825 KB]`와 DEM Options를 보여 준다(16). X Direction·Y Direction 열에서 `Lower-Left (m): 487683.78125 / 3401278.75`, `Upper-Right (m): 512039.1875 / 3422095.75`, `Cell Size (m): 50 / 50`, `Number of Cells: 488 / 417`이다(16, 그림). `Sink with Current Model`은 체크되어 있다(16, 그림). `Output Format`의 선택은 `TB2 Grid Format`이며 목록에는 `ArcGIS ASCII Grid`, `Surfer ASCII Grid`도 보인다(16, 그림). `Interpolation Algorithm`의 `Inverse Distance Weighting (IDW)`·`Delaunay Triangulation`·`Kriging`은 비활성 상태다(16, 그림). 빈 줄·마크업을 포함한다(15·17). |
| 18–20 | Export DEM / 저장 — Generate DEM 뒤 파일 이름과 디렉터리를 정해 Save를 누른다(18). 파일 이름 예시는 `*File Name* (e.g DEM)` (18). 그림 `12-3-2020_4-21-01_PM.png`는 Data 폴더의 `File name: DEM.tb2`, `Save as type: TB2 Grid (*.tb2)` 저장 창이다(20, 그림). 빈 줄·마지막 그림 마크업을 포함한다(19–20). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 10·14·18: `#GenerateDEM-Figure1`부터 `#GenerateDEM-Figure3` 링크가 있다. 이 파일에는 대응 앵커와 그림 번호 캡션이 없다.
- 14·16(그림): 본문은 생성 DEM의 출력 형식을 TB2라고 적는다. 그림의 출력 목록은 TB2 Grid Format과 ArcGIS ASCII Grid·Surfer ASCII Grid를 함께 표시한다.
