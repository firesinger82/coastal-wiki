---
file: models/EFDC/raw/manuals/confluence/spaces/CVLKB/pages/CVLGrid_Knowledge_Base/CVLGrid_Users_Manual/Using_CVLGrid_Menu_Options/CVLGrid_Settings.md
lines: 40
sha256: 91d3076cae1ead4e48d5f95b60257c009c0a795440855e2a6b730c0030b8848d
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# CVLGrid_Settings.md — 판독 구간 기록

구간은 1행부터 40행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | 메타데이터 — Confluence 페이지의 식별자, 제목, space, URL, 버전, 갱신 시각, 문서 계층과 frontmatter 경계 표식이다(1–9). |
| 10–14 | CVLGrid Settings / 접근과 Grid Generation — 격자 생성(grid generation)의 기본 설정, 직교화(orthogonalization), 평활화(smoothing), 축척(scale) 설정을 조정한다(10). 10행의 로컬 버튼 아이콘을 직접 열었다. 아이콘은 작은 격자와 중심 표시를 보여 준다. Figure 1의 로컬 그림을 직접 열었다(12). `Grid Generation` 탭의 예시값은 `I-Cells: 10`, `J-Cells: 10`, `XMin: 0`, `YMin: 0`, `XMax: 13.67708`, `YMax: 8.27083`이다. `Auto Set`은 체크되어 있다. `RHS Type`은 `Laplace (Recommended)`이다. `Sorenson (a,b,c,d)`의 네 칸은 각각 `10`이며 비활성 표시이다. 직교화 반복 수는 `10`, 경계 조정 반복 수는 `1`, `Ratio of moving points`는 `0.85`, `Maximum number of sub-segments`는 `500`이다. `Maintain original border after orthogonalization`은 체크되어 있다(12). 캡션과 빈 줄을 포함한다(11–14). |
| 15–27 | Grid Generation / 설정 표 — 표의 각 이름, 설명, 기본값, 범위, 적용 조건을 그대로 옮긴다: `*I-Cells*` — `Specifies number of cells in the I (X) direction.` (17); `*J-Cells*` — `Specifies number of cells in the J (Y) direction.` (18); `*Scale Settings*` — `*Auto Set* is set as default for viewing. The X and Y values can be manually adjusted by unchecking the *Auto Set* box and typing in the desired values in the input boxes. When *Apply* is selected the workspace is refreshed and zoomed in or out based on the X and Y coordinate limitations.` (19); `*RHS Type*` — `There are two optional choices for grid generation: Laplace and Sorenson.` (20); `*Sorenson (a, b, c, d)*` — `These are Sorenson coefficients. The user is able to put the coefficients when Sorenson option is chosen for the equation solving option. For *RHS Type*. *a* and *c* for P; *b* and *d* for Q. When a, b, c, d is greater than 100 the Sorenson tends to Laplace methodology in generating grid.` (21); `*Number of Orthogonalization Iterations per Operation*` — `Specifies the number of iterations to perform during calculation.` (22); `*Number of Iterations of Boundary Adjustment*` — `Specifies the number of times to move the boundary points. CVLGrid automatically sets these to 10 and 1 respectively. This is recommended if the grid is very large as it can reduce calculation time.` (23); `*Ratio of Moving Points*` — `Ratio of moving node grid on a segment on the border. 0< ratio <=1` (24); `*Maintain Original Border after Orthogonalization*` — `Keep grid nodes on the border close to the border as possible when orthogonalize is used` (25); `*Maximum Number of Sub-segments*` — `Specifies the maximum number of sub-segments` (26). `Auto Set`의 기본 설정과 수동 좌표 입력 조건은 19행에 있다. Sorenson 계수 `a`, `c`는 `P`에 사용한다. `b`, `d`는 `Q`에 사용한다(21). 계수의 선택 조건과 100 초과 조건은 인용문에 그대로 남겼다. 23행은 앞의 두 반복 수를 각각 `10`, `1`로 자동 설정한다고 적는다. 이동 비율 범위는 `0< ratio <=1`이다(24). 표 머리글·구분선과 빈 줄을 포함한다(15–27). |
| 28–30 | General settings / Figure 2 — 로컬 그림을 직접 열었다(28). `General` 탭의 `Spline Method`는 `Catmull-Rom`이다. `Divisions`의 예시값은 `10`이다. `Distribute Symbols`의 예시값은 `0.2`이다. `Number of Smoothing Iterations per Operation`의 예시값은 `5`이다. `Line Selected Formatting`에는 분홍 선과 두 검은 사각형 기호가 보인다(28). 캡션과 빈 줄을 포함한다(29–30). |
| 31–38 | General settings / 설정 표 — 스플라인(spline), 분할, 선택 선 서식, 기호 간격, 평활화 반복 수를 설명한다. 표의 각 이름·설명·범위·기본값 원문: `*Spline Method*` — `There are two optional choices for setting the spline type: *B-Spline* and *Catmull-Rom*.` (33); `*Divisions*` — `Number of point division between two spline points when draw a spline. 1<= Division <=100` (34); `*Line Selected Formatting*` — `Allows the user to format attributes of line and symbol when clicking on this image , a *Line Formatting* frame appears as [Figure 3](#CVLGridSettings-Figure3).` (35); `*Distribute Symbols*` — `Delta value to display space between point symbols in polyline. Default value is 0.2 inch.` (36); `*Number of Smoothing Iterations per Operation*` — `Specifies the number of iterations for smoothing` (37). `Spline Method`의 선택지는 `B-Spline`, `Catmull-Rom`이다(33). 분할 범위는 `1<= Division <=100`이다(34). 기호 간격의 기본값은 `0.2 inch`이다(36). 표 머리글·구분선과 빈 줄을 포함한다(31–38). |
| 39–40 | Line formatting / Figure 3 — 로컬 그림을 직접 열었다(39). `Line Format` 창은 `Thickness`, `Style`, `Symbol`, `Color` 설정을 보여 준다. 두께 예시값은 `.015`이며 단위는 `Inches`이다. 선 스타일 표시값은 `Solid`이다. 미리보기에는 분홍 선과 끝의 사각형 기호가 있다(39). 캡션을 포함한다(40). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 10·35: 내부 링크 `#CVLGridSettings-Figure1`, `#CVLGridSettings-Figure2`, `#CVLGridSettings-Figure3`가 있다. 13·29·40행의 캡션에는 대응하는 앵커 정의가 없다.
- 21: Sorenson 계수 설명에 `P`, `Q`를 사용한다. 이 문서에는 `P`, `Q`의 정의나 해당 방정식이 없다.

