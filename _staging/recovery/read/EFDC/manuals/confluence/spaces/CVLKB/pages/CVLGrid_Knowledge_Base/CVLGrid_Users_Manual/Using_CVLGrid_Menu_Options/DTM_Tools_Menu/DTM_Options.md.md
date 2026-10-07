---
file: models/EFDC/raw/manuals/confluence/spaces/CVLKB/pages/CVLGrid_Knowledge_Base/CVLGrid_Users_Manual/Using_CVLGrid_Menu_Options/DTM_Tools_Menu/DTM_Options.md
lines: 50
sha256: 17413c7537e43b1325d9b8a77e8faef2abbb8f149ea1f722764e422889691ad8
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# DTM_Options.md — 판독 구간 기록

구간은 1행부터 50행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | 메타데이터 — Confluence 페이지의 식별자, 제목, space, URL, 버전, 갱신 시각, 문서 계층과 frontmatter 경계 표식이다(1–9). |
| 10–14 | DTM Options / File controls — `Options`를 선택한 뒤 DTM 파일을 찾아 선택하고 `Load`로 불러온다. 적용 절차 원문: `When the *Options* is selected a window in appears allowing the user browse to the DTM file and load it as shown in [Figure 1](#DTMOptions-Figure1). When a file has been selected, click the *Load* button to load the information.` (10). Figure 1의 로컬 그림을 직접 열었다(12). `File Controls` 창은 DTM 파일 경로, `Browse`, `Load`, `Save`, `Blanking Elevation Value: -999`, 체크된 `Display DTM Map`, `Min Valid El: -1000`, `Max Valid El: 10000`, `Scale It`, `Sub Set`를 보여 준다. 파일 이름 예시는 `West Lake Bathymetry Raw Data 2009.p2d`이다(12). 캡션과 빈 줄을 포함한다(11–14). |
| 15–23 | 결측 표고·표시·유효 범위 — 옵션 제목과 설명 원문: `*Blanking Elevation Value*  ` (15); ` This option selects what value to fill in missing elevation data points. -999 is the standard input for missing values.` (16); `*Display DTM Map*  ` (18); ` This option displays the data file in the workspace when checked.` (19); `*Min and Max Valid Elevation*  ` (21); ` These two input boxes let the user adjust the range of elevation values allowed by DTM Tool. By default, this range is usually set to -1,000 m minimum and 10,000 m maximum. The user can use this range to isolate unwanted elevations or to encompass all the elevation points in a very wide range.` (22). `-999`는 결측값의 표준 입력이라고 적는다. 체크할 때 데이터 파일을 작업 공간에 표시한다. 유효 표고 범위의 기본 설정은 보통 최소 `-1,000 m`, 최대 `10,000 m`라고 적는다. 원치 않는 표고를 제외하거나 모든 점을 포괄하도록 범위를 조정할 수 있다. 빈 줄도 포함한다(15–23). |
| 24–32 | Load Options / DTM Utilities — 옵션 제목과 조건 원문: `*Load Options*  ` (24); ` This frame allows the user to attach data to the data already loaded by clicking the *Append Data* box. The user can also adjust the size of the data points in the workspace by changing the value in the *Diameter of DTM Points* input box.` (25); `*DTM Utilities*  ` (27); ` This frame offers two options to the user. The *Scale It* button allows the user to input a conversion factor that will convert the units from meters to another unit such as feet. The input window is shown in [Figure 2](#DTMOptions-Figure2).` (28). `Append Data`를 클릭하면 기존에 불러온 데이터에 추가한다. `Diameter of DTM Points`는 작업 공간의 점 크기를 바꾼다(25). `Scale It`은 미터에서 다른 단위로 변환할 계수를 입력하는 창을 연다(28). Figure 2의 로컬 그림을 직접 열었다(30). 창 제목은 `XY Units for Topo Grid`이다. 안내는 `Enter the X-Y Conversion Factor (e.g. 3.281):`이다. 입력칸의 예시값은 `1`이다(30). 캡션과 빈 줄을 포함한다(29–32). |
| 33–37 | Sub Set / DTM clipping window — `Sub Set`으로 잘라내기(clipping) 창을 연다(33). Figure 3의 로컬 그림을 직접 열었다(35). `Clip DTM/Grid (Maintain Spacing Settings)` 창은 원본 파일, 결측 표고, 유효 표고, 현재 자료 사용, X/Y 최소·최대 잘라내기 사각형, 선택적 잘라내기 파일, 출력 파일, 선택 반전과 실행 버튼을 보여 준다. 그림의 문구는 `Clipping Range (Always Used. Updates the NX and NY to the clipping rectangle)`이며, 파일 선택 문구는 `Clipping file is optional. Used for clipping to irregular shapes.`이다. 원본의 예시 표고값은 `Blanking Elevation Value: -999`, `Min Valid El: -1000`, `Max Valid El: 10000`이다. `Use Current Data`는 체크되어 있고 `Invert Selection`은 체크되지 않았다(35). 캡션과 빈 줄을 포함한다(34–37). |
| 38–45 | Clipping Region / 영역 결정·선택 반전·저장 — 제목과 적용 조건을 원문대로 옮긴다: `*Clipping Region*  ` (38); ` The user is able to enter Min and Max values for X and Y of two defined points for clipping rectangle. If the *Set to Data* button is selected, the fields for X/YMin and X/Y Max values will fill in automatically based on DTM data file loaded. If the *Set to Current View* button is selected, the clipping region will be generated base on the screen view set by the user.` (39); `The user can also define the clipping region by browsing to the desired file then loading. The region outside of the clipping line will be cropped. In case the *Invert Selection* check box is selected, the region outside of the clipping line will be retained.` (41); `The user can save the region after clipping by browsing to the desired directory and naming the output file. Then click the *Apply Clipping* button for the changes to take effect.  ` (43). 두 점의 X·Y 최소·최대로 잘라내기 사각형을 지정한다. `Set to Data`는 불러온 데이터에 따라 범위를 채운다. `Set to Current View`는 현재 화면을 기준으로 범위를 만든다(39). 파일로 잘라내기 경계를 불러올 수도 있다. 일반 선택에서는 잘라내기 선 밖의 영역을 제거한다. `Invert Selection`을 선택한 경우에는 선 밖의 영역을 남긴다(41). 출력 디렉터리와 파일 이름을 정하고 `Apply Clipping`을 눌러 변경을 적용한다(43). 44행은 폴리라인(polyline) 잘라내기 전후 그림을 참조한다. 빈 줄을 포함한다(38–45). |
| 46–50 | Figures 5–6 / 잘라내기 전후 — 로컬 그림 두 개를 각각 직접 열었다(46·49). Figure 5는 DTM 자료 전체와 남길 영역을 둘러싼 초록 `Spline4` 잘라내기 선을 보여 준다. 표고 범례(legend)의 표기는 `Elevation (m)`, 파랑 끝값은 `3.33`, 빨강 끝값은 `5.22`이다. 축척 표기는 `600 Meters`이다(46–47). Figure 6은 잘라내기 뒤 남은 부분을 보여 준다. 표고 범례의 표기는 `Elevation (m)`, 파랑 끝값은 `3.43`, 빨강 끝값은 `5.21`이다. 축척 표기는 `400 Meters`이다(49–50). 두 그림에는 수평·수직 눈금 축이 없다. |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 10·28·33·44: `#DTMOptions-Figure1`, `#DTMOptions-Figure2`, `#DTMOptions-Figure3`, `#DTMOptions-Figure5`, `#DTMOptions-Figure6` 내부 링크가 있다. 13·31·36·47·50행의 캡션에는 대응하는 앵커 정의가 없다.
- 24–25·12: 본문은 `Load Options`, `Append Data`, `Diameter of DTM Points`를 설명한다. 12행의 File Controls 그림에는 이 이름의 프레임과 입력 항목이 표시되지 않는다.
- 13·31·36·47·50: 그림 번호는 1·2·3·5·6 순서이다. 이 파일에는 Figure 4 그림과 캡션이 없다.

