---
file: models/ADCIRC/raw/manuals/website_markdown/home/documentation/users-manual-v53/input-file-descriptions/nws-values-table/index.md
lines: 440
sha256: ec8668b5f570367191e3f66e02dcec09272e65e976e224ca6d377374bb5d651e
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# index.md — 판독 구간 기록

구간은 1행부터 440행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–12 | 웹페이지 시작 스크립트 — New Relic 브라우저 계측 코드와 뒤 빈 줄을 포함한다(1–12). |
| 13–77 | 웹페이지 CSS / 검색·제목·본문 배치 — 검색 필드, 제목, 본문 글꼴, 컨테이너 및 오른쪽 본문 폭의 표시 규칙을 포함한다(13–77). |
| 78–134 | 웹페이지 CSS / 본문·탐색 위치 — 단일 열 본문, 문단, 링크, 오른쪽 목록, 경로 탐색 및 인용문의 표시 규칙을 포함한다(78–134). |
| 135–200 | 웹페이지 CSS / 메뉴 — 제목 크기, 다중 열 본문 및 탐색 메뉴의 하위 목록 표시 규칙을 포함한다(135–200). |
| 201–230 | 웹페이지 CSS / 메뉴 상태 — 마우스 위치와 현재 페이지에 따른 메뉴 표시 규칙을 포함한다(201–225). 슬라이드 영역, 메뉴 글꼴, 숨김 요소 및 이미지의 표시 규칙을 포함한다(226–230). |
| 231–248 | 페이지 제목·구조화 메타데이터(metadata)·이모지 스크립트 — NWS Values Table 페이지 제목과 페이지 주소, 게시 시각, 경로 탐색 정보를 담은 JSON을 포함한다(232·237). WordPress 이모지 설정과 지원 여부 검사 코드를 포함한다(242–246). |
| 249–285 | 웹페이지 CSS / WordPress 공통 스타일 — 이모지와 버튼 스타일을 포함한다(249–263). 화면 비율, 색, 글꼴 크기, 간격, 그림자 및 블록 배치의 CSS를 포함한다(266–269). 나머지는 빈 줄이다(270–285). |
| 286–303 | 웹페이지 관리·분석·배경 — 관리 표시 스타일을 포함한다(286–289). 방문 분석 설정을 포함한다(292–298). 본문 배경 이미지 설정과 빈 줄을 포함한다(300–303). |
| 304–348 | 웹사이트 머리말·문서 탐색 — ADCIRC 사이트 이름, 탐색 건너뛰기 링크 및 공동체·문서 메뉴를 포함한다(304–327). v50부터 v53까지의 사용자 설명서와 컴파일·명령행·FAQ·SWAN 연결 메뉴를 포함한다(328–348). |
| 349–401 | 웹사이트 탐색 / 자료·소프트웨어·소식·제품 — 예제, 이론 보고서, 개발자 자료 및 관련 소프트웨어의 링크를 포함한다(349–361). 사용자 모임, 예보, 제품 및 ASGS 링크를 포함한다(362–400). 마지막 빈 줄을 포함한다(401). |
| 402–405 | NWS Values Table / 제목 — 경로 탐색과 본문 제목을 포함한다(402–404). 원문: `# NWS Values Table` (404). |
| 406–424 | NWS 값 표 / 기상 자료 형식과 결합 조건 — 빈 머리행과 표 구분행을 포함한다(406–407). 기상 자료(meteorological data) 형식에 따라 파랑(waves)을 끈 경우, fort.23·SWAN·STWAVE 파랑을 함께 사용하는 경우, OWI 유사 형식(OWI-like format)의 얼음 피복(ice coverage)과 fort.24·SWAN·STWAVE 파랑을 함께 사용하는 경우의 값을 제시한다(408). 각 자료 형식의 값 또는 n/a를 행별로 제시한다(409–424). 매 절점·매 시간 단계 또는 WTIMINC마다의 풍응력(wind stress)·풍속(wind velocity) 자료 조건을 제시한다(410–411·414–416). 더 이상 사용할 수 없다고 적은 asymmetric vortex model 행은 모든 열에 n/a를 제시한다(418). 원문: `\|  \|  \|  \|  \|  \|  \|  \|  \|` (406); `\| --- \| --- \| --- \| --- \| --- \| --- \| --- \| --- \|` (407); `\| Meteorological Data Format \| Met. Only  Waves Off \| Met. plus Waves from fort.23 \| Met. plus Waves SWAN \| Met. plus Waves STWAVE \| Met. plus Ice Coverage OWI-like format plus Waves from fort.24 \| Met. plus Ice Coverage OWI-like format plus Waves from SWAN \| Met. plus Ice Coverage OWI-like format plus Waves from STWAVE \|` (408); `\| none \| 0 \| n/a \| n/a \| n/a \| n/a \| n/a \| n/a \|` (409); `\| wind stress, every node, every timestep \| 1 \| 101 \| 301 \| 401 \| 12101 \| 12301 \| 12401 \|` (410); `\| wind stress, every node, every WTIMINC \| 2 \| 102 \| 302 \| 402 \| 12102 \| 12302 \| 12402 \|` (411); `\| US Navy Fleet Numeric \| 3 \| 103 \| 303 \| 403 \| 12103 \| 12303 \| 12403 \|` (412); `\| PBL/JAG \| 4 \| 104 \| 304 \| 404 \| 12104 \| 12304 \| 12404 \|` (413); `\| wind velocity, every node, every WTIMINC \| 5 \| 105 \| 305 \| 405 \| 12105 \| 12305 \| 12405 \|` (414); `\| wind velocity, rectangular grid, every WTIMINC \| 6 \| 106 \| 306 \| 406 \| 12106 \| 12306 \| 12406 \|` (415); `\| wind stress, regular grid, every WTIMINC \| 7 \| 107 \| 307 \| 407 \| 12107 \| 12307 \| 12407 \|` (416); `\| symmetrc vortex model \| 8 \| 108 \| 308 \| 408 \| 12108 \| 12308 \| 12408 \|` (417); `\| asymmetric vortex model (no longer available) \| n/a \| n/a \| n/a \| n/a \| n/a \| n/a \| n/a \|` (418); `\| National Weather Service AVN \| 10 \| 110 \| 310 \| 410 \| 12110 \| 12310 \| 12410 \|` (419); `\| National Weather Service ETA 29km \| 11 \| 111 \| 311 \| 411 \| 12111 \| 12311 \| 12411 \|` (420); `\| Ocean Weather Inc (OWI) \| 12 \| 112 \| 312 \| 412 \| 12112 \| 12312 \| 12412 \|` (421); `\| H\*Wind \| 15 \| 115 \| 315 \| 415 \| 12115 \| 12315 \| 12415 \|` (422); `\| Dynamic Asymmetric Model \| 19 \| 119 \| 319 \| 419 \| 12119 \| 12319 \| 12419 \|` (423); `\| Generalized Asymmetric Holland Model \| 20 \| 120 \| 320 \| 420 \| 12120 \| 12320 \| 12420 \|` (424). |
| 425–440 | 웹페이지 끝 스크립트 — 빈 줄과 유틸리티 표시 호출을 포함한다(425–428). 링크 선행 읽기 설정을 포함한다(430). 쿠키 안내, 슬라이더 표시 및 New Relic 페이지 정보를 포함한다(433–440). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 417: 기상 자료 형식 이름은 `symmetrc vortex model`로 적혀 있다.
