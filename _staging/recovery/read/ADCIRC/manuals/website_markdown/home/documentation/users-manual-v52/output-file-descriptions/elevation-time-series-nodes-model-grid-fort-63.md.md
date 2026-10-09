---
file: models/ADCIRC/raw/manuals/website_markdown/home/documentation/users-manual-v52/output-file-descriptions/elevation-time-series-nodes-model-grid-fort-63.md
lines: 442
sha256: 1e1e0be59e5a111754cb88c8add425e57879a735c66483eaa164396d28381de8
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# elevation-time-series-nodes-model-grid-fort-63.md — 판독 구간 기록

구간은 1행부터 442행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–12 | 웹페이지 계측 스크립트. New Relic 초기화와 브라우저 로더(browser loader)가 들어 있다(1–2). 나머지는 빈 줄이다(3–12). |
| 13–70 | 웹페이지 검색·머리말 스타일. 검색 입력란과 버튼, 제목 링크, 본문 글꼴·색, 머리말과 컨테이너(container)의 스타일시트(CSS) 규칙을 지정한다(13–70). |
| 71–150 | 웹페이지 본문·탐색 스타일. 본문 열과 콘텐츠 영역, 문단·링크, 이동 경로(breadcrumb), 활성 메뉴, 인용문·제목·접근 영역의 표시 규칙이다(71–150). |
| 151–230 | 웹페이지 메뉴 스타일. 메뉴 글꼴·목록·정렬, 하위 메뉴, 마우스 오버(hover)와 현재 페이지 표시, 글라이더(glider), 표어 숨김, 이미지 크기 규칙이다(151–230). 메뉴 배경 참조는 `background:url(images/primary\_nav\_divider.gif) repeat-y scroll right bottom;` (166)와 `background: #76a3de url(images/primary\_nav\_bg\_repeat\_on.gif) repeat-x top;` (202)이다. 두 로컬 그림 파일은 없다. |
| 231–241 | 페이지 제목과 구조화 메타데이터. 제목은 `Elevation Time Series at All Nodes in the Model Grid (fort.63) - ADCIRC` (232)이다. JSON-LD 메타데이터에 페이지 식별자·URL·제목·날짜·이동 경로와 사이트 검색 정보가 들어 있다(237). 앞뒤 빈 줄을 포함한다(231–241). |
| 242–285 | 웹페이지 이모지(emoji)와 공통 스타일. CDATA 경계 주석, WordPress 이모지 설정·처리 스크립트, 이모지 크기, 블록 버튼, 공통 색·크기 등의 프리셋(preset), flex·grid·인용문 스타일이 들어 있다(242–269). 뒤의 빈 줄을 포함한다(270–285). |
| 286–311 | 웹페이지 관리 막대·분석 설정과 사이트 머리말. 관리 막대 스타일(286–288), Beehive의 Google Analytics 설정(292–298), 페이지 배경 `body.custom-background { background-color: #ffffff; background-image: url("https://adcirc.org/wp-content/uploads/sites/2255/2013/03/grid\_bkgrd\_lt\_grey1.jpg"); background-position: left top; background-size: auto; background-repeat: repeat-y; background-attachment: scroll; }` (300)을 포함한다. 배경의 로컬 그림 파일은 없다. ADCIRC 사이트 링크(306), 공식 웹사이트 부제(308), 탐색 건너뛰기 링크(310)와 빈 줄을 포함한다. |
| 312–358 | 공통 탐색 메뉴: Community와 Documentation. 개발자·협력 기관·사용자 링크(312–322)를 나열한다. 사용자 설명서와 컴파일·명령행·질문·SWAN+ADCIRC·보고서·이론·특수 기능·얼음·하위 영역 관련 문서 링크(323–358)를 나열한다. |
| 359–401 | 공통 탐색 메뉴: 관련 소프트웨어·뉴스·제품. 워크숍과 모임, 격자(grid)·조석 데이터베이스·예측·기름 이동·ASGS 등의 링크를 나열한다(359–400). 사진 파일 링크는 `    - [2018 ADCIRC Week Group Photo](https://adcirc.org/wp-content/uploads/sites/2255/2018/04/ADCIRC2018_Group_Photo2.jpg)` (368); `    - [2017 ADCIRC Meeting Group Photo](https://adcirc.org/wp-content/uploads/sites/2255/2017/06/2017ADCIRCUGMGroupPhoto.jpg)` (370); `    - [2016 ADCIRC User’s Group Photo](https://adcirc.org/wp-content/uploads/sites/2255/2016/05/160506-A-Y1769-008-A-1.jpg)` (374); `    - [2016 ADCIRC Boot Camp Group Photo](https://adcirc.org/wp-content/uploads/sites/2255/2016/05/adcircBootCampers2016_small_caption.jpg)` (375); `    - [2011 ADCIRC Workshop Photo](https://adcirc.org/wp-content/uploads/sites/2255/2018/11/2011_ADCIRC_meeting.jpg)` (387); `    - [2010 ADCIRC Workshop Photo](https://adcirc.org/wp-content/uploads/sites/2255/2018/11/ADCIRC_Workshop2010_GroupPhoto2.png)` (389)이다. 이 사진들의 로컬 사본은 모두 없다. 끝의 빈 줄을 포함한다(401). |
| 402–410 | fort.63: 모델 격자 전체 절점(node)의 수위 시계열(time series). 이동 경로(402)와 절 제목(404)을 포함한다. fort.15의 지정에 따라 모델 격자의 모든 절점에서 수위 시계열을 출력한다(406). 굵은 변수 줄·빈 줄·반복문과 변수 정의 링크의 읽는 방법을 설명한다(408). ASCII 또는 이진(binary) 출력의 적용 조건은 `Output may be in ascii or binary format depending on how [NOUTGE](https://adcirc.org/home/documentation/users-manual-v52/parameter-definitions#NOUTGE) is set in the [Model Parameter and Periodic Boundary Condition File](../../input-file-descriptions/model-parameter-and-periodic-boundary-condition-file-fort-15)` (410)이다. |
| 411–422 | 출력 파일 구조. 파일 첫머리의 두 줄은 `[**RUNDES**](https://adcirc.org/home/documentation/users-manual-v52/parameter-definitions#RUNDES), [**RUNID**](https://adcirc.org/home/documentation/users-manual-v52/parameter-definitions#RUNID), [**AGRID**](https://adcirc.org/home/documentation/users-manual-v52/parameter-definitions#AGRID)` (412)와 `[**NDSETSE**](https://adcirc.org/home/documentation/users-manual-v52/parameter-definitions#NDSETSE), [**NP**](https://adcirc.org/home/documentation/users-manual-v52/parameter-definitions#NP), **[DTDP](https://adcirc.org/home/documentation/users-manual-v52/parameter-definitions#DTDP)\*[NSPOOLGE](https://adcirc.org/home/documentation/users-manual-v52/parameter-definitions#NSPOOLGE)**, [**NSPOOLGE**](https://adcirc.org/home/documentation/users-manual-v52/parameter-definitions#NSPOOLGE), [**IRTYPE**](https://adcirc.org/home/documentation/users-manual-v52/parameter-definitions#IRTYPE)` (414)이다. 두 번째 줄에는 곱 표현이 들어 있다(414). 이어지는 줄은 `[**TIME**](https://adcirc.org/home/documentation/users-manual-v52/parameter-definitions#TIME), [**IT**](https://adcirc.org/home/documentation/users-manual-v52/parameter-definitions#IT)` (416)이다. 절점 반복문, 절점 번호와 수위 출력 줄, 반복문 종료는 `for k=1, [NP](https://adcirc.org/home/documentation/users-manual-v52/parameter-definitions#NP)` (418); `**k**, [**ETA2(k)**](https://adcirc.org/home/documentation/users-manual-v52/parameter-definitions#ETA2)` (420); `end k loop` (422)이다. 각 변수 이름과 곱 표현을 원문 그대로 옮겼다. 빈 줄을 포함한다(411–422). |
| 423–426 | 이진 출력 주의사항. 주의 제목(424)과 빈 줄을 포함한다. 조건과 절점 번호의 제외는 `If binary output is specified, the node number (k) is not included in the output.` (426)이다. |
| 427–442 | 웹페이지 바닥의 공통 스크립트와 빈 줄. 유틸리티 표시 호출(430), 링크 미리 가져오기(prefetch) 설정(432), CDATA 경계 주석과 쿠키 안내 설정(435–437), Soliloquy의 jQuery 호출(441), New Relic 계측 정보(442)를 포함한다. |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 166행의 메뉴 구분선 배경: 그림 파일 없음. 해당 파일명의 로컬 사본을 `models/ADCIRC/raw/manuals` 아래에서 찾지 못했다. 원문 참조는 `background:url(images/primary\_nav\_divider.gif) repeat-y scroll right bottom;` (166)이다.
- 202행의 메뉴 선택 배경: 그림 파일 없음. 해당 파일명의 로컬 사본을 `models/ADCIRC/raw/manuals` 아래에서 찾지 못했다. 원문 참조는 `background: #76a3de url(images/primary\_nav\_bg\_repeat\_on.gif) repeat-x top;` (202)이다.
- 300행의 페이지 배경: 그림 파일 없음. 해당 파일명의 로컬 사본을 `models/ADCIRC/raw/manuals` 아래에서 찾지 못했다. 원문 참조는 `body.custom-background { background-color: #ffffff; background-image: url("https://adcirc.org/wp-content/uploads/sites/2255/2013/03/grid\_bkgrd\_lt\_grey1.jpg"); background-position: left top; background-size: auto; background-repeat: repeat-y; background-attachment: scroll; }` (300)이다.
- 368행의 2018 ADCIRC Week 단체 사진 링크: 그림 파일 없음. 해당 파일명의 로컬 사본을 `models/ADCIRC/raw/manuals` 아래에서 찾지 못했다. 원문 참조는 `    - [2018 ADCIRC Week Group Photo](https://adcirc.org/wp-content/uploads/sites/2255/2018/04/ADCIRC2018_Group_Photo2.jpg)` (368)이다.
- 370행의 2017 ADCIRC Meeting 단체 사진 링크: 그림 파일 없음. 해당 파일명의 로컬 사본을 `models/ADCIRC/raw/manuals` 아래에서 찾지 못했다. 원문 참조는 `    - [2017 ADCIRC Meeting Group Photo](https://adcirc.org/wp-content/uploads/sites/2255/2017/06/2017ADCIRCUGMGroupPhoto.jpg)` (370)이다.
- 374행의 2016 ADCIRC 사용자 모임 단체 사진 링크: 그림 파일 없음. 해당 파일명의 로컬 사본을 `models/ADCIRC/raw/manuals` 아래에서 찾지 못했다. 원문 참조는 `    - [2016 ADCIRC User’s Group Photo](https://adcirc.org/wp-content/uploads/sites/2255/2016/05/160506-A-Y1769-008-A-1.jpg)` (374)이다.
- 375행의 2016 ADCIRC Boot Camp 단체 사진 링크: 그림 파일 없음. 해당 파일명의 로컬 사본을 `models/ADCIRC/raw/manuals` 아래에서 찾지 못했다. 원문 참조는 `    - [2016 ADCIRC Boot Camp Group Photo](https://adcirc.org/wp-content/uploads/sites/2255/2016/05/adcircBootCampers2016_small_caption.jpg)` (375)이다.
- 387행의 2011 ADCIRC Workshop 사진 링크: 그림 파일 없음. 해당 파일명의 로컬 사본을 `models/ADCIRC/raw/manuals` 아래에서 찾지 못했다. 원문 참조는 `    - [2011 ADCIRC Workshop Photo](https://adcirc.org/wp-content/uploads/sites/2255/2018/11/2011_ADCIRC_meeting.jpg)` (387)이다.
- 389행의 2010 ADCIRC Workshop 단체 사진 링크: 그림 파일 없음. 해당 파일명의 로컬 사본을 `models/ADCIRC/raw/manuals` 아래에서 찾지 못했다. 원문 참조는 `    - [2010 ADCIRC Workshop Photo](https://adcirc.org/wp-content/uploads/sites/2255/2018/11/ADCIRC_Workshop2010_GroupPhoto2.png)` (389)이다.
