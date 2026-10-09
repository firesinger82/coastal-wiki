---
file: models/ADCIRC/raw/manuals/website_markdown/home/documentation/users-manual-v52/output-file-descriptions/temperature-values-surface-layer-fort-47.md
lines: 420
sha256: 1ff4a0a6ae683bbef1404de7fe2c5327a89145f57c7e754d9db4aa602848cc76
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# temperature-values-surface-layer-fort-47.md — 판독 구간 기록

구간은 1행부터 420행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–12 | 웹페이지 감시 스크립트(New Relic browser monitoring script)가 시작된다(1–2행). 초기 설정과 압축된 JavaScript 로더는 웹페이지 성능·오류·이벤트 수집을 위한 코드다(1–2행). 이 구간은 ADCIRC 출력 파일 본문 앞의 웹페이지 코드다. 코드 뒤의 빈 줄을 포함한다(3–12행). |
| 13–85 | 웹페이지 스타일시트(Cascading Style Sheets, CSS)는 검색 입력란과 버튼, 제목 링크, 본문과 제목 글꼴, 머리말, 컨테이너와 콘텐츠 배치를 설정한다(13–85행). 스타일 주석·중괄호·빈 줄을 포함한다. |
| 86–142 | CSS는 본문 영역의 문단·링크, 오른쪽 열, 이동 경로(breadcrumb), 문맥 탐색 메뉴(context navigation), 인용문과 제목의 표시를 설정한다(86–142행). 스타일 선언과 빈 줄을 포함한다. |
| 143–200 | CSS는 탐색 메뉴의 목록·위치·크기와 하위 메뉴 배치를 설정한다(143–200행). 배경 그림 참조 원문은 `background:url(images/primary\_nav\_divider.gif) repeat-y scroll right bottom;` (166)이다. 이 배경 그림에 해당하는 로컬 파일은 없다. 그림 파일 없음. 스타일 선언과 빈 줄을 포함한다. |
| 201–231 | CSS는 마우스를 올린 링크와 현재 메뉴의 표시, 하위 메뉴의 표시, 콘텐츠 래퍼(wrapper), 태그 스타일과 이미지 크기를 설정한다(201–231행). 배경 그림 참조 원문은 `background: #76a3de url(images/primary\_nav\_bg\_repeat\_on.gif) repeat-x top;` (202)이다. 이 배경 그림에 해당하는 로컬 파일은 없다. 그림 파일 없음. 스타일 선언과 빈 줄을 포함한다. |
| 232–246 | 웹페이지 제목은 `Temperature Values at the Surface Layer (fort.47) - ADCIRC` (232)이다. 구조화된 메타데이터(JSON-LD)는 페이지·탐색 경로·사이트 정보를 담는다(235행). 이모지(emoji) 지원 확인과 로딩 스크립트가 이어진다(240–244행). 스크립트 주석과 빈 줄을 포함한다. |
| 247–283 | WordPress의 CSS는 이모지 표시, 버튼·파일 링크, 화면 배치와 색상·글꼴·간격·그림자 프리셋(preset)을 설정한다(247–267행). 인용문 스타일과 뒤의 빈 줄을 포함한다(267–283행). |
| 284–301 | 관리 화면 지원 CSS가 있다(284–286행). Beehive의 Google Analytics 스크립트가 있다(290–296행). 사용자 지정 배경의 그림 참조 원문은 `body.custom-background { background-color: #ffffff; background-image: url("https://adcirc.org/wp-content/uploads/sites/2255/2013/03/grid\_bkgrd\_lt\_grey1.jpg"); background-position: left top; background-size: auto; background-repeat: repeat-y; background-attachment: scroll; }` (298)이다. 이 배경 그림에 해당하는 로컬 파일은 없다. 그림 파일 없음. 주석·스타일·스크립트 사이의 빈 줄을 포함한다. |
| 302–356 | 빈 제목 표식, ADCIRC 링크, 공식 웹사이트 문구와 탐색 건너뛰기 링크가 있다(302–308행). Community 메뉴는 개발자·협력기관·사용자 항목을 나열한다(310–320행). Documentation 메뉴는 사용자 매뉴얼, 입력·출력 설명, 컴파일, 명령행, 질의응답, 예제, 보고서와 이론 문서 등의 링크를 나열한다(321–356행). 목록 마크업과 빈 줄을 포함한다. |
| 357–401 | Related Software, News, Products와 ASGS 메뉴는 관련 소프트웨어, 워크숍·부트캠프·단체 사진, 제품과 운영 안내의 링크를 나열한다(357–398행). 단체 사진 항목은 일반 링크로 표시된다. 현재 출력 파일 문서까지의 이동 경로가 이어진다(400행). 목록 마크업과 빈 줄을 포함한다. |
| 402–404 | 제목은 `# Temperature Values at the Surface Layer (fort.47)` (402)이다. `fort.47`은 최상부 온도 경계조건(top temperature boundary condition)을 기록한다(404행). 이 조건은 대기 모델(atmospheric model) 출력으로 제공되거나 표면 온도 경계값 파일(Surface Temperature Boundary Values File)을 통해 코드의 입력 변수로 제공된다(404행). 출력 파일은 표층(surface layer)의 온도값만 기록한다(404행). 파일 형식은 `fort.63`과 같다고 적는다(404행). `fort.15`의 `IDEN` 값이 `3` 또는 `4`인 경우에만 출력 파일을 제공한다(404행). ADCIRC가 이 두 `IDEN` 값에서 온도 변화를 계산한다고 적는다(404행). 이 파일 본문에는 온도 단위와 실제 파일 형식 예시가 없다(404행). 설명·입력 경로·적용 조건 원문: `The fort.47 file records the top temperature boundary condition that is either provided via output from an atmospheric model or as an input variable into the code via a Surface Temperature Boundary Values File. This output file follows the same format as a [fort.63 file](../elevation-time-series-nodes-model-grid-fort-63/), as it only records the temperature values for the surface layer. The output file is only provided if the [IDEN](https://adcirc.org/home/documentation/users-manual-v52/parameter-definitions#IDEN) value in the [Model Parameter and Periodic Boundary Condition File](../../input-file-descriptions/model-parameter-and-periodic-boundary-condition-file-fort-15) is given as a 3 or 4, as ADCIRC evaluates the temperature changes for these two [IDEN](https://adcirc.org/home/documentation/users-manual-v52/parameter-definitions#IDEN) values` (404). 제목과 설명 사이의 빈 줄도 포함한다. |
| 405–420 | 문서 본문 뒤의 빈 줄을 포함한다(405–407행). 웹페이지 유틸리티 호출이 있다(408행). 미리 가져오기(prefetch) 주소 설정이 있다(410행). 쿠키 동의 배너(cookie consent banner)의 문구·버튼·표시 설정과 CDATA 주석이 있다(413–415행). 슬라이더 표시 클래스 제거 스크립트가 있다(419행). New Relic 실행 정보와 초기 설정 스크립트가 마지막 행에 있다(420행). 스크립트 사이의 빈 줄을 포함한다. |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- `images/primary\_nav\_divider.gif` 배경 그림 참조가 있다(166행). `models/ADCIRC/raw/manuals/`에서 이 파일명의 로컬 사본을 찾지 못했다. 그림 파일 없음.
- `images/primary\_nav\_bg\_repeat\_on.gif` 배경 그림 참조가 있다(202행). `models/ADCIRC/raw/manuals/`에서 이 파일명의 로컬 사본을 찾지 못했다. 그림 파일 없음.
- `https://adcirc.org/wp-content/uploads/sites/2255/2013/03/grid\_bkgrd\_lt\_grey1.jpg` 배경 그림 참조가 있다(298행). `models/ADCIRC/raw/manuals/`에서 이 파일명의 로컬 사본을 찾지 못했다. 그림 파일 없음.
- 404행의 상대경로 `../elevation-time-series-nodes-model-grid-fort-63/`는 현재 파일 위치에서 `models/ADCIRC/raw/manuals/website_markdown/home/documentation/users-manual-v52/elevation-time-series-nodes-model-grid-fort-63`로 해석된다. 해당 경로와 `.md` 파일 및 `index.md` 파일은 로컬에 없다.
- 404행의 상대경로 `../../input-file-descriptions/model-parameter-and-periodic-boundary-condition-file-fort-15`는 현재 파일 위치에서 `models/ADCIRC/raw/manuals/website_markdown/home/documentation/input-file-descriptions/model-parameter-and-periodic-boundary-condition-file-fort-15`로 해석된다. 해당 경로와 `.md` 파일 및 `index.md` 파일은 로컬에 없다.
