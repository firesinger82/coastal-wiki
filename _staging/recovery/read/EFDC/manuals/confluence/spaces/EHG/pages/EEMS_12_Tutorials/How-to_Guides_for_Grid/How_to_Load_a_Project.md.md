---
file: models/EFDC/raw/manuals/confluence/spaces/EHG/pages/EEMS_12_Tutorials/How-to_Guides_for_Grid/How_to_Load_a_Project.md
lines: 28
sha256: 0ce266c93091bea264e1b0bca3f9b48808eeae5810d2b50fe1f52cda7afd1e3a
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# How_to_Load_a_Project.md — 판독 구간 기록

구간은 1행부터 28행까지 빈틈없이 이어진다.
그림 경로는 원문과 같은 space 폴더를 기준으로 적었다.

| 구간 | 내용 |
|---|---|
| 1–11 | 문서 정보와 프로젝트 파일 — 페이지 메타데이터를 포함한다(1–9). 프로젝트 파일(project file)의 격자·스플라인, 중첩도(overlay)·디지털 지형 모형(DTM)의 전체 경로 저장과 주석 레이어(annotation layer) 표시를 설명한다(10). 확장자를 원문 그대로 옮긴다(10). 원문: `Grid+ uses several file types to develop a grid for use in EFDC. The .gpp file is a Grid+ project file that saves all the files the user has loaded, including the actual grid (.gpp) and splines (.spl).  In addition, if the user has any overlays (e.g. shoreline files) or DTM (e.g. bathymetry XYZ data), the full path name is saved in the .gpp file. The annotation layers will be added to the display when the .gpp file is opened.` (10). |
| 12–23 | Open Project / 끌어놓기 — File의 Open Project 또는 Ctrl+O로 프로젝트를 선택하면 격자·스플라인 등 파일을 불러온다(12). Windows Explorer에서 프로젝트 파일을 작업 공간으로 끌어놓는 방법도 제시한다(14). 메뉴와 파일 선택창의 그림·캡션을 포함한다(16–22). 원문: `To load a Grid+ project file (\*.gpp), the user should click the *File* menu and select *Open Project* (or use shortcut keys Ctrl+O), as shown in [Figure 1](#HowtoLoadaProject-Figure1). As a result, the *Open* form will pop up. Browse to the Grid+ project file and click the *Open* button, as shown in [Figure 2](#HowtoLoadaProject-Figure2). After clicking *Open* button, the Grid+ will load all files, such as the grid (.gpc), splines (\*.spl), etc.` (12). 그림 직접 확인: `attachments/246579797/7.png` — Figure 1(16): File 메뉴의 Open Project와 `Ctrl+O`를 강조한 화면. 그림 직접 확인: `attachments/246579797/8.png` — Figure 2(20): `File name: NY_harbor.gpp`, 파일 형식 `Grid+ Project (*.gpp)`를 선택하여 Open을 누르는 화면. |
| 24–28 | Related articles / Filter by label — 선택한 라벨에 항목이 없다는 안내를 포함한다(24–28). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 10·12: 10행은 실제 격자 확장자를 `.gpp`라고 적는다. 12행은 불러올 격자 확장자를 `.gpc`라고 적는다.
- 12: 그림 링크는 `#HowtoLoadaProject-FigureN` 형식이며 이 Markdown 파일에는 해당 ID를 정의하는 마크업이 없다.

