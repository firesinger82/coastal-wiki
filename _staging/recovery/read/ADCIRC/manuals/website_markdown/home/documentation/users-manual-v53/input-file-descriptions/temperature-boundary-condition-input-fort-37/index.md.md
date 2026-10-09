---
file: models/ADCIRC/raw/manuals/website_markdown/home/documentation/users-manual-v53/input-file-descriptions/temperature-boundary-condition-input-fort-37/index.md
lines: 432
sha256: 837583e3b647b025966d88809f40a613bfe2af179a1c2324936ee1d40a4e2fd3
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# Temperature Boundary Condition Input (fort.37) — 판독 구간 기록

구간은 1행부터 432행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–12 | 웹 성능 수집 스크립트와 앞쪽 빈 줄 — New Relic의 브라우저 오류·이벤트·통신 수집용 JavaScript가 들어 있다(1–2). 뒤에는 빈 줄이 이어진다(3–12). |
| 13–51 | 검색·글꼴 스타일 — 검색 필드(search field), 사이트 머리말(header), 본문 및 링크의 스타일시트(Cascading Style Sheets, CSS)을 지정한다(13–51). |
| 52–93 | 페이지 틀 스타일 — 컨테이너(container), 머리말, 태그 표시 및 본문 열의 CSS 스타일을 지정한다(52–93). |
| 94–135 | 본문 요소 스타일 — 문단, 링크, 오른쪽 열, 탐색 경로(breadcrumb), 인용문 및 소제목의 CSS 스타일을 지정한다(94–135). |
| 136–184 | 메뉴 스타일 — 본문 배치와 탐색 메뉴(navigation menu)의 CSS 스타일을 지정한다. 메뉴 구분선의 배경 이미지 URL이 들어 있다(136–184). |
| 185–230 | 하위 메뉴·그림 크기 스타일 — 하위 메뉴(submenu)의 위치 및 상태별 표시를 지정한다. 래퍼(wrapper), 태그 및 본문 그림 크기의 CSS 스타일이 이어진다(185–230). |
| 231–239 | 페이지 제목·검색 메타데이터 — 문서 제목이 나온다(232). 웹페이지, 웹사이트 및 탐색 경로의 구조화 데이터(structured data)가 들어 있다(235). 주변 빈 줄도 이 구간에 포함한다(231–239). |
| 240–258 | 이모지 스크립트·스타일 — 브라우저의 이모지(emoji) 지원 확인, 검사 결과 저장 및 보조 스크립트 로딩 코드가 들어 있다(240–244). 이모지 그림의 CSS 스타일과 빈 줄이 이어진다(245–258). |
| 259–288 | 버튼·파일·관리자 표시 스타일 — 버튼과 파일 블록 및 전역 표시 설정이 들어 있다(260–267). 관리자 막대(admin bar)의 지원 스타일과 주변 빈 줄이 이어진다(268–288). |
| 289–300 | 웹 분석·배경 스타일 — Beehive와 Google Analytics 설정이 들어 있다(290–296). 페이지 배경 이미지의 CSS URL과 빈 줄이 이어진다(297–300). |
| 301–320 | 사이트 머리말·Community 메뉴 — ADCIRC 사이트 이름, 사이트 설명 및 탐색 건너뛰기 링크가 나온다(302–308). 개발자, 관련 연구 그룹 및 사용자 목록의 메뉴가 이어진다(310–320). |
| 321–356 | Documentation 메뉴 — 소개, 구조, 위키, 사용자 매뉴얼 및 입력·출력 파일 설명 링크가 있다(321–356). 컴파일·명령행 옵션, FAQ, 예제, 개발자 안내, 이론 보고서, 특수 기능 및 출판물 등의 링크도 같은 메뉴에 있다(321–356). |
| 357–391 | 관련 소프트웨어·News 메뉴 — 유틸리티와 격자 생성기(grid generator) 링크가 있다(357–359). 사용자 모임, 워크숍(workshop), 발표 자료, 일정, 단체 사진 및 예보·모의 사례 링크가 이어진다(360–391). 단체 사진은 탐색 메뉴의 일반 링크이다. |
| 392–401 | Products 메뉴·본문 진입 — 조석 자료, 출판물, 격자, 예보, 표층 기름 이동 및 ASGS 링크가 있다(392–398). 이 문서의 탐색 경로와 주변 빈 줄이 이어진다(399–401). |
| 402–405 | Temperature Boundary Condition Input (fort.37) — 온도 경계조건(temperature boundary condition) 입력 파일의 판독 조건을 설명한다(402–404). 적용 값은 fort.15의 매개변수에 대한 아래 원문과 같다(404). 원문: `The temperature boundary condition input file (fort.37) is read in when the [**RES\_BC\_FLAG**](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#RES_BC_FLAG) is set to -3, 3, -4, or 4 in the [fort.15 file](../model-parameter-and-periodic-boundary-condition-file-fort-15/ "Model Parameter and Periodic Boundary Condition File (fort.15)").` (404). |
| 406–417 | 데이터 세트·경계 노드별 입력 형식 — 데이터 세트마다 날짜를 담은 주석 줄(comment line)이 있다(406–408). 해양 경계 노드(ocean boundary node) 반복 안에서 노드 번호와 온도 값을 읽는 입력 구조를 제시한다(410–416). 변수와 반복 범위는 아래 원문과 같다(406–416). 원문: `for i=1 to numberOfDataSets` (406); `**comment line (date)**` (408); `for k=1 to number\_of\_ocean\_boundary\_nodes` (410); `k, (**TEMPBC(k,m)**, m=1,NFEN)` (412); `end k loop` (414); `end i loop` (416). |
| 418–432 | 웹페이지 끝부분 — 유틸리티 호출과 링크 미리 가져오기(prefetch) 설정이 들어 있다(420–422). 쿠키 안내문, jQuery 코드 및 New Relic 정보가 이어진다(425–432). 주변 빈 줄도 이 구간에 포함한다(418–432). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 406·410행: `numberOfDataSets`와 `number\_of\_ocean\_boundary\_nodes`가 반복의 상한으로 쓰인다. 이 이름들의 별도 정의는 파일 본문에 없다.
- 412행: `NFEN`이 반복의 상한으로 쓰인다. 이 기호의 정의는 파일 본문에 없다.
- 412행: `TEMPBC(k,m)`이 입력 변수로 제시된다. 이 변수의 정의와 단위는 파일 본문에 없다.
