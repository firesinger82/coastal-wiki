---
file: models/ADCIRC/raw/manuals/website_markdown/home/documentation/users-manual-v53/input-file-descriptions/velocity-station-location-input-file-vel_stat-151/index.md
lines: 436
sha256: 00830b10ed8ddd237c1804055590467fed93f4735b64dda8e01530b580f79461
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# Velocity Station Location input file (vel\_stat.151) — 판독 구간 기록

구간은 1행부터 436행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–12 | 웹 성능 수집 스크립트와 앞쪽 빈 줄 — New Relic의 브라우저 오류·이벤트·통신 수집용 JavaScript가 들어 있다(1–2). 뒤에는 빈 줄이 이어진다(3–12). |
| 13–51 | 검색·글꼴 스타일 — 검색 필드(search field), 사이트 머리말(header), 본문 및 링크의 스타일시트(Cascading Style Sheets, CSS)을 지정한다(13–51). |
| 52–93 | 페이지 틀 스타일 — 컨테이너(container), 머리말, 태그 표시 및 본문 열의 CSS 스타일을 지정한다(52–93). |
| 94–135 | 본문 요소 스타일 — 문단, 링크, 오른쪽 열, 탐색 경로(breadcrumb), 인용문 및 소제목의 CSS 스타일을 지정한다(94–135). |
| 136–184 | 메뉴 스타일 — 본문 배치와 탐색 메뉴(navigation menu)의 CSS 스타일을 지정한다. 메뉴 구분선의 배경 이미지 URL이 들어 있다(136–184). |
| 185–230 | 하위 메뉴·그림 크기 스타일 — 하위 메뉴(submenu)의 위치 및 상태별 표시를 지정한다. 래퍼(wrapper), 태그 및 본문 그림 크기의 CSS 스타일이 이어진다(185–230). |
| 231–241 | 페이지 제목·검색 메타데이터 — 문서 제목이 나온다(232). 웹페이지, 웹사이트 및 탐색 경로의 구조화 데이터(structured data)가 들어 있다(237). 주변 빈 줄도 이 구간에 포함한다(231–241). |
| 242–260 | 이모지 스크립트·스타일 — 브라우저의 이모지(emoji) 지원 확인, 검사 결과 저장 및 보조 스크립트 로딩 코드가 들어 있다(242–246). 이모지 그림의 CSS 스타일과 빈 줄이 이어진다(247–260). |
| 261–290 | 버튼·파일·관리자 표시 스타일 — 버튼과 파일 블록 및 전역 표시 설정이 들어 있다(262–269). 관리자 막대(admin bar)의 지원 스타일과 주변 빈 줄이 이어진다(270–290). |
| 291–302 | 웹 분석·배경 스타일 — Beehive와 Google Analytics 설정이 들어 있다(292–298). 페이지 배경 이미지의 CSS URL과 빈 줄이 이어진다(299–302). |
| 303–322 | 사이트 머리말·Community 메뉴 — ADCIRC 사이트 이름, 사이트 설명 및 탐색 건너뛰기 링크가 나온다(304–310). 개발자, 관련 연구 그룹 및 사용자 목록의 메뉴가 이어진다(312–322). |
| 323–358 | Documentation 메뉴 — 소개, 구조, 위키, 사용자 매뉴얼 및 입력·출력 파일 설명 링크가 있다(323–358). 컴파일·명령행 옵션, FAQ, 예제, 개발자 안내, 이론 보고서, 특수 기능 및 출판물 등의 링크도 같은 메뉴에 있다(323–358). |
| 359–393 | 관련 소프트웨어·News 메뉴 — 유틸리티와 격자 생성기(grid generator) 링크가 있다(359–361). 사용자 모임, 워크숍(workshop), 발표 자료, 일정, 단체 사진 및 예보·모의 사례 링크가 이어진다(362–393). 단체 사진은 탐색 메뉴의 일반 링크이다. |
| 394–403 | Products 메뉴·본문 진입 — 조석 자료, 출판물, 격자, 예보, 표층 기름 이동 및 ASGS 링크가 있다(394–400). 이 문서의 탐색 경로와 주변 빈 줄이 이어진다(401–403). |
| 404–409 | Velocity Station Location input file (vel_stat.151) — 유속 관측소(velocity station) 위치 입력 파일의 판독 조건을 설명한다(404–406). 굵은 변수 이름 줄, 가독성을 위한 빈 줄 및 반복문(loop)을 사용하는 파일 구조 표기법을 설명한다(408). 변수 정의는 링크로 제공한다고 적는다(408). 적용 조건은 원문과 같다(406). 원문: `The reading of the vel\_stat.151 file is triggered when the number of velocity recording stations ([NSTAV](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#NSTAV)) in the [fort.15 file](https://adcirc.org/home/documentation/users-manual-v53/input-file-descriptions/model-parameter-and-periodic-boundary-condition-file-fort-15/) is set to a negative value.` (406); `The basic file structure is shown below. Each line of input data is represented by a line containing the input variable name(s) in bold face type. Blank lines are only to enhance readability. Loops indicate multiple lines of input. Definitions of each variable are provided via hot links.` (408). |
| 410–417 | 관측소 수·좌표 입력 형식 — 관측소 개수 줄 다음에 위치 좌표(coordinate)의 반복 입력이 이어지는 구조를 제시한다(410–416). 변수 이름과 반복 범위는 원문과 같다(410–416). 원문: `[**NSTAV2**](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#NSTAV2)` (410); `for k=1,[NSTAV2](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#NSTAV2)` (412); `**[XEV(k)](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#XEV)**, **[YEV(k)](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#YEV)**` (414); `end k loop` (416). |
| 418–421 | Notes — 입력 파일의 관측소 수와 fort.15의 값이 다를 때 사용할 값을 설명한다(418–420). 기재된 관측소가 지정 수보다 적을 때의 오류 종료와 많을 때의 사용 범위를 설명한다(420). 각 조건과 수량은 원문과 같다(420). 원문: `**Notes:**` (418); `If the value of NSTAV2 differs from the value of NSTAV (as read from the fort.15 file) the value of NSTAV2 will be used. If there are fewer than NSTAV2 stations listed in the vel\_stat.151 file, ADCIRC will stop with an error. If there are more than NSTAV2 stations listed in the vel\_stat.151 file, only the first NSTAV2 of them will be used.` (420). |
| 422–436 | 웹페이지 끝부분 — 유틸리티 호출과 링크 미리 가져오기(prefetch) 설정이 들어 있다(424–426). 쿠키 안내문, jQuery 코드 및 New Relic 정보가 이어진다(429–436). 주변 빈 줄도 이 구간에 포함한다(422–436). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

없음
