---
file: models/EFDC/raw/manuals/confluence/spaces/EK/pages/Graphics.md
lines: 53
sha256: e763f66537b507c35fa9050600e9faaebd6b8298e19e401369955d946e5d3b1b
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Graphics.md — 판독 구간 기록

구간은 1행부터 53행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | 앞부분 메타데이터. `title: "Graphics"` (3) 및 페이지 ID, space, URL, 버전, 갱신 시각과 문서 경로를 포함한다(1–9). |
| 10–15 | Graphics 개요. 이미지(image)와 애니메이션을 생성하는 기능을 소개한다(10). 그림 12는 Graphics 메뉴의 `Generate Image` (12)와 `Generate Animation` (12) 항목이다. Figure 1 캡션을 포함한다(14). |
| 16–27 | Generate Image. 이미지명·저장 폴더를 선택하며 기본 폴더, 창별 이미지와 단일 이미지의 차이, 내보낼 창 선택, 둘 이상의 창을 고를 때만 활성화되는 Arrange Windows 및 배치 항목을 원문으로 옮긴다: `- *Export Options* : the user should select a name for the image and select the folder to save the image by clicking the *Browse*button. By default, the image will be saved in the *#analysis* folder of the active model.` (20) `- *Separated Images:* if the option is selected, each window is exported into individual images` (21) `- *Single Image:* if the option is selected, all window is exported into a single image.` (22) `- *Select window to export*: all available windows with details information are listed in the form, and the user can check the box for the interested window to export.` (23) `- If more than one window is selected in the *Select window to export* frame, the *Arrange Windows* button is available. The *Arrange Windows* form is shown in [Figure 3](#Graphics-Figure3). The user is able to select *No.of Rows, No.of Columns, Column Width* and *Row Height.*` (24) OK를 누르면 이미지 내보내기를 시작한다(26). |
| 28–31 | Generate Image 설정 화면. 그림 28의 Generate Graphics 창에서 `Separated Images` (28)가 선택되며 `Single Image` (28)는 선택되지 않았다. 내보낼 창 목록에는 2DV View와 2DH View 두 창이 선택되어 있다. Export to File의 보이는 파일명은 `2DV_Temperature.png` (28)이고 경로에 `#analysis` (28)가 보인다. `List All Windows` (28)는 선택되지 않았다. Figure 2 캡션을 포함한다(30). |
| 32–35 | 이미지용 Arrange Windows. 그림 32의 설정 값은 `No. of Rows: 1` (32), `No. of Columns: 2` (32), `Column Width: 960` (32), `Row Height: 872` (32)이다. `Show Fom Border` (32)가 선택되어 있다. 미리보기는 1행·2열이며 왼쪽에 파랑·초록 중심과 빨간 가장자리의 평면 격자 지도가, 오른쪽에 위쪽 빨강·아래쪽 파랑의 수직 단면이 있다. 미리보기 안 그래프의 축 글자와 눈금 값은 작아서 판독할 수 없다(32). Figure 3 캡션을 포함한다(34). |
| 36–46 | Generate Animation. 애니메이션명·저장 폴더, 기본 *.avi 형식과 #analysis 폴더, 창 선택 및 시간 범위·초기 프레임(initial frame) 조건을 보존한다. `- *Export Options* : the user should select a name for the animation and select the folder to save the animation by clicking the *Browse*button. By default, the animation will be saved in the format of *\*.avi* file in the *#analysis* folder of the active model.` (40) `- *Select window to export*: all available windows with details information are listed in the form, and the user can check the box for the interested window to export.` (41) `- *AVI File Options:*the user can set up the exporting file. *Animation Timing*: the time for the AVI file needs to be inside the model timing. It is able to add *Grid, Symbols* *and Labels* or *Background image* by checking the box in *Initial Frame Options*.` (42) `- If more than one window is selected in the *Select window to export* frame, the *Arrange Windows* button is available. The *Arrange Windows* form is shown in [Figure 5](#Graphics-Figure5). The user is able to select *No.of Rows, No.of Columns, Column Width* and *Row Height.*` (43) Animation Timing은 모델 시간 범위 안이어야 한다. 마지막 실행 문구는 마크업까지 그대로 `*Finally, click *OK* button to start exporting images.*` (45)이다. |
| 47–50 | Generate Animation 설정 화면. 그림 47의 Export to File 경로에는 `#animations` (47)와 `TS_Temperature (Depth Avg.).avi` (47)가 보인다. 선택 창은 Time Series 및 2DH View 두 개이다. 시간·프레임(frame) 설정 값은 `Start Animation (days): 41120.000000` (47), `2012-08-01 00:00:00` (47), `Stop Animation (days): 41620.000147` (47), `2013-12-14 00:00:12` (47), `Number of Time Steps to Skip: 1` (47), `Frame Rate: 2` (47), `Number of snapshots to display: 2` (47)이다. Compressed AVI는 선택되어 있다. Grid, Symbols and Labels, Background image 및 List All Windows는 선택되지 않았다. Figure 4 캡션을 포함한다(49). |
| 51–53 | 애니메이션용 Arrange Windows. 그림 51의 설정은 `No. of Rows: 1` (51), `No. of Columns: 2` (51), `Column Width: 960` (51), `Row Height: 872` (51)이다. `Show Fom Border` (51)가 선택되어 있다. 왼쪽 미리보기는 파랑 중심과 빨강 가장자리의 격자 지도이다. 오른쪽 미리보기는 빨간 시계열 곡선이 내려갔다 올라간 뒤 다시 내려가는 그래프이다. 축 글자와 눈금 값은 작아서 판독할 수 없다(51). 그림 앞뒤 굵게 표시와 Figure 5 캡션의 연속 별표 마크업을 포함한다(51–53). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- Generate Animation 절의 마지막 실행 안내는 `*Finally, click *OK* button to start exporting images.*` (45)이다. 애니메이션 절에서 결과를 `images` (45)라고 적는다(36, 45).
- Arrange Windows의 그림 두 개에서 내부 그래프는 작은 미리보기로 들어 있다. 축 글자와 눈금 값을 판독할 수 없다(32, 51).

