---
file: models/ADCIRC/raw/manuals/website_markdown/community/developers/index.md
lines: 419
sha256: 43619c232ef25f653766ed41ee9e71658bf4966e689b065d5316de18dffa5dea
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# index.md — 판독 구간 기록

구간은 1행부터 419행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–12 | 웹페이지 상태 수집 코드: New Relic 초기화와 브라우저 에이전트(browser agent) 로더를 담는다 (1–2). 2행에는 축약된 JavaScript 코드가 이어진다. 뒤의 빈 줄도 포함한다 (3–12). |
| 13–70 | 사이트 스타일: 캐스케이딩 스타일 시트(Cascading Style Sheets, CSS)가 검색 입력란과 버튼, 머리글 링크, 본문 글꼴·배경, 페이지 컨테이너(container), 제목의 글꼴을 지정한다 (13–70). |
| 71–142 | 본문 영역 스타일: 본문 열과 링크, 문단, 상위 페이지 경로(breadcrumb), 선택된 링크, 인용문, 소제목의 표시 규칙을 담는다 (71–142). 링크 스타일 선언이 두 곳에 반복된다 (99–103, 107–111). |
| 143–200 | 탐색 메뉴 스타일: 메뉴 목록·항목과 하위 메뉴의 위치·크기·표시 규칙을 담는다 (143–200). 메뉴 구분선 그림 경로를 참조한다 (166). |
| 201–231 | 메뉴 선택·이미지 표시 스타일: 마우스를 올린 메뉴의 배경 그림을 참조한다 (202). 하위 메뉴 표시와 현재 페이지 메뉴의 스타일을 지정한다 (201–228). 이미지 크기를 조절하는 CSS와 빈 줄을 포함한다 (229–231). |
| 232–240 | 페이지 제목·메타데이터: 제목은 `Developers - ADCIRC`이다 (232). Schema.org 구조화 데이터(structured data)는 `WebPage`의 URL을 `https://adcirc.org/community/developers/`로 적는다 (235). 게시 시각은 `2013-03-01T15:30:22+00:00`이다 (235). 사이트 설명, 상위 페이지 경로와 검색 관련 구조화 데이터 및 빈 줄을 포함한다 (233–240). |
| 241–260 | 이모지(emoji) 지원 코드: WordPress의 이모지 설정, 지원 여부 검사와 관련 스크립트를 담는다 (241–245). 이모지·스마일 이미지의 CSS와 빈 줄을 포함한다 (246–260). |
| 261–284 | WordPress 표시 스타일: 버튼·파일 블록(block), 화면 비율·색상·글꼴·간격·그림자에 관한 전역 스타일을 담는다 (261–284). 플렉스(flex)·그리드(grid) 배치와 인용문 스타일 및 뒤의 빈 줄을 포함한다. |
| 285–302 | 관리·분석·배경 코드: 관리 도구 모음의 색상 CSS를 담는다 (285–287). Google Analytics 초기화 코드가 이어진다 (291–297). 사이트 배경 CSS는 그림 URL을 참조한다 (299). 나머지 빈 줄도 포함한다. |
| 303–310 | 사이트 머리글: 내용 없는 `#` 제목 줄, ADCIRC 홈페이지 링크와 `The Official ADCIRC Web Site`를 담는다 (303–307). 탐색을 건너뛰는 링크는 `[Skip Navigation](#content-well)`이다 (309). 사이의 빈 줄도 포함한다. |
| 311–321 | Community 메뉴: Developers 아래에 Development Group과 Development Partners를 연결한다 (311–314). 개발 협력기관 링크는 Coastal Resilience Center, Naval Research Laboratory, New Orleans District, Seahorse Coastal Consulting, USACE Coastal Hydraulics Laboratory, Water Institute of the Gulf이다 (315–320). Users 링크로 끝난다 (321). |
| 322–348 | Documentation 메뉴: 소개, ADCIRC Architecture와 Wiki 링크를 담는다 (322–326). 사용자 설명서 V50·V51·v52·v53에는 각각 입력 파일 설명, 출력 파일 설명, 버전 이력 링크가 있다 (327–342). 컴파일 시 작업, 명령행 옵션(command-line options), FAQ, SWAN + ADCIRC 실행 및 Example Problems의 링크가 이어진다 (343–348). 이 구간에는 해당 링크의 대상 문서 내용이 실려 있지 않다. |
| 349–360 | Reports and Publications·Related software 메뉴: 소개와 `ADCIRC Architechture`, 개발자 안내서, 이론 보고서, 특수 기능, 얼음 피복 수정, 관련 출판물, 부분영역 모델링(subdomain modeling)의 링크를 담는다 (349–357). 관련 소프트웨어는 ADCIRC Utility Programs와 SMS Grid Generator 링크로 제시한다 (358–360). |
| 361–400 | News·Products·ASGS 메뉴: 2020년부터 2008년까지의 사용자 모임·교육·워크숍 관련 안내, 일정·발표·사진 링크를 담는다 (361–390). 사진 파일 직접 링크는 367행·369행·373행·374행·386행·388행에 있다. 허리케인 폭풍해일(storm surge) 예보와 Katrina 모의 링크가 이어진다 (391–392). Products는 조석 데이터베이스(tidal databases), 관련 출판물, 격자(grid), ADCIRC Surge Guidance System 예보, 허리케인 중 표층 유류 이동의 링크를 담는다 (393–398). ASGS GitHub 링크와 빈 줄로 끝난다 (399–400). |
| 401–406 | Developers 제목: Home → Community → Developers의 상위 페이지 경로를 담는다 (401). 본문 제목은 `Developers`이다 (403). 402행·404–406행은 빈 줄이다. 제목 뒤에는 개발자 소개나 협력기관 설명이 실려 있지 않다 (404–406). |
| 407–419 | 페이지 하단 코드: `show\_utility('white','960px');` 호출을 담는다 (407). 링크 사전 가져오기(prefetch)의 대상·제외 규칙이 이어진다 (409). 쿠키 동의 배너(cookie consent banner)는 UNC 안내 문구, `I Accept`, 개인정보 안내 링크를 담는다 (413). jQuery의 Soliloquy 관련 클래스 제거 코드와 New Relic 정보 객체(object)로 끝난다 (418–419). 사이의 빈 줄도 포함한다. |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 166행: CSS가 참조하는 `images/primary\_nav\_divider.gif`에 대응하는 로컬 그림 파일 없음.
- 202행: CSS가 참조하는 `images/primary\_nav\_bg\_repeat\_on.gif`에 대응하는 로컬 그림 파일 없음.
- 299행: 사이트 배경 URL의 `grid_bkgrd_lt_grey1.jpg`에 대응하는 로컬 그림 파일 없음.
- 367행: 사진 링크의 `ADCIRC2018_Group_Photo2.jpg`에 대응하는 로컬 그림 파일 없음.
- 369행: 사진 링크의 `2017ADCIRCUGMGroupPhoto.jpg`에 대응하는 로컬 그림 파일 없음.
- 373행: 사진 링크의 `160506-A-Y1769-008-A-1.jpg`에 대응하는 로컬 그림 파일 없음.
- 374행: 사진 링크의 `adcircBootCampers2016_small_caption.jpg`에 대응하는 로컬 그림 파일 없음.
- 386행: 사진 링크의 `2011_ADCIRC_meeting.jpg`에 대응하는 로컬 그림 파일 없음.
- 388행: 사진 링크의 `ADCIRC_Workshop2010_GroupPhoto2.png`에 대응하는 로컬 그림 파일 없음.
- 309행: `[Skip Navigation](#content-well)`의 대상 앵커 정의가 이 Markdown 안에 없다. 87행·104행의 같은 이름은 CSS 선택자(selector)이다.
- 403행·404–406행: `Developers` 제목 다음은 빈 줄이며, 407행부터 페이지 하단 코드가 시작한다. 이 문서에는 제목 뒤의 소개 본문이 없다.
