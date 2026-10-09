---
file: models/ADCIRC/raw/manuals/website_markdown/home/documentation/users-manual-v52/input-file-descriptions/nws-values-table/index.md
lines: 440
sha256: 332ba1ab0fefb658661a6fc0855289ee8f56e5b2898f543ec4c98df9a5fa5b9e
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# index.md — 판독 구간 기록

구간은 1행부터 440행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–12 | 웹 계측 스크립트·공백 — New Relic의 초기화와 브라우저 계측 JavaScript가 들어 있다(1–2). 뒤 공백을 포함한다(3–12). |
| 13–85 | 사이트 스타일 / 검색·제목·본문 틀 — 검색창과 검색 버튼, 제목과 링크, 본문 글꼴과 컨테이너의 CSS가 들어 있다(13–85). |
| 86–142 | 사이트 스타일 / 본문·경로·인용문 — 본문 영역, 링크, 경로 안내, 활성 메뉴, 인용문과 두 열 배치의 CSS가 들어 있다(86–142). |
| 143–184 | 사이트 스타일 / 메뉴 배치 — 메뉴의 위치와 목록, 링크, 하위 메뉴의 CSS가 들어 있다(143–184). |
| 185–230 | 사이트 스타일 / 메뉴 상태·이미지 — 하위 메뉴와 마우스 이동 상태, 활성 항목과 이미지 크기의 CSS가 들어 있다(185–230). |
| 231–241 | 페이지 제목·구조화 메타데이터 — 페이지 제목은 NWS Values Table이다(232). JSON-LD는 페이지 URL, 발행 시각, 경로 안내와 검색 동작을 적는다(237). 이 JSON-LD에는 dateModified 항목이 없다(237). 공백을 포함한다. |
| 242–270 | WordPress 표시 스크립트·스타일 — 이모지(emoji) 지원 검사와 표시 CSS가 들어 있다(242–259). 버튼과 파일 블록, 색상·글꼴·간격의 CSS 설정이 이어진다(262–269). |
| 271–303 | 지원 표시·방문 계측·배경 스타일 — 지원 표시의 CSS와 Google 방문 계측 설정이 들어 있다(286–298). 웹페이지 배경 CSS와 공백을 포함한다(300–303). |
| 304–358 | 사이트 탐색 / 커뮤니티·문서 — 사이트 제목과 탐색 건너뛰기 링크가 있다(304–310). 개발자·사용자, 매뉴얼 버전, 실행·이론·관련 문서의 탐색 링크가 이어진다(312–358). |
| 359–403 | 사이트 탐색 / 소프트웨어·소식·제품·경로 — 관련 소프트웨어, 모임과 발표, 제품, ASGS의 탐색 링크가 있다(359–400). 현재 페이지의 경로 안내와 공백을 포함한다(401–403). |
| 404–408 | NWS Values Table / 제목·열 구성 — NWS 값 표의 제목과 표 마크업(markup)을 포함한다(404–408). 열은 기상 자료 형식, 기상만 사용, fort.23·SWAN·STWAVE 파랑 결합, OWI 형태 해빙 피복(ice coverage) 및 fort.24·SWAN·STWAVE 파랑 결합을 구분한다(408). 열 제목을 원문 그대로 옮긴다. 원문: `# NWS Values Table` (404); `\|  \|  \|  \|  \|  \|  \|  \|  \|` (406); `\| --- \| --- \| --- \| --- \| --- \| --- \| --- \| --- \|` (407); `\| Meteorological Data Format \| Met. Only  Waves Off \| Met. plus Waves from fort.23 \| Met. plus Waves SWAN \| Met. plus Waves STWAVE \| Met. plus Ice Coverage OWI-like format plus Waves from fort.24 \| Met. plus Ice Coverage OWI-like format plus Waves from SWAN \| Met. plus Ice Coverage OWI-like format plus Waves from STWAVE \|` (408). |
| 409–416 | NWS Values Table / 자료 없음·절점·격자 입력 — none, 절점별 바람 응력(wind stress), US Navy Fleet Numeric, PBL/JAG와 풍속(wind velocity), 직사각형·규칙 격자 자료의 값을 제시한다(409–416). 시간 단계(timestep)와 WTIMINC의 구분, 각 결합 열의 숫자 및 n/a를 행마다 그대로 옮긴다. 기본값이나 추가 허용 범위는 이 구간에 적혀 있지 않다. 원문: `\| none \| 0 \| n/a \| n/a \| n/a \| n/a \| n/a \| n/a \|` (409); `\| wind stress, every node, every timestep \| 1 \| 101 \| 301 \| 401 \| 12101 \| 12301 \| 12401 \|` (410); `\| wind stress, every node, every WTIMINC \| 2 \| 102 \| 302 \| 402 \| 12102 \| 12302 \| 12402 \|` (411); `\| US Navy Fleet Numeric \| 3 \| 103 \| 303 \| 403 \| 12103 \| 12303 \| 12403 \|` (412); `\| PBL/JAG \| 4 \| 104 \| 304 \| 404 \| 12104 \| 12304 \| 12404 \|` (413); `\| wind velocity, every node, every WTIMINC \| 5 \| 105 \| 305 \| 405 \| 12105 \| 12305 \| 12405 \|` (414); `\| wind velocity, rectangular grid, every WTIMINC \| 6 \| 106 \| 306 \| 406 \| 12106 \| 12306 \| 12406 \|` (415); `\| wind stress, regular grid, every WTIMINC \| 7 \| 107 \| 307 \| 407 \| 12107 \| 12307 \| 12407 \|` (416). |
| 417–424 | NWS Values Table / 기상 모델·자료 형식 — 대칭 와류 모델(symmetric vortex model), 더 이상 사용할 수 없는 비대칭 와류 모델(asymmetric vortex model), AVN·ETA·OWI·H*Wind·Dynamic Asymmetric Model·Generalized Asymmetric Holland Model의 값이 이어진다(417–424). 원문의 symmetrc 표기와 no longer available 조건 및 각 열의 숫자·n/a를 행마다 그대로 옮긴다. 기본값이나 추가 허용 범위는 이 구간에 적혀 있지 않다. 원문: `\| symmetrc vortex model \| 8 \| 108 \| 308 \| 408 \| 12108 \| 12308 \| 12408 \|` (417); `\| asymmetric vortex model (no longer available) \| n/a \| n/a \| n/a \| n/a \| n/a \| n/a \| n/a \|` (418); `\| National Weather Service AVN \| 10 \| 110 \| 310 \| 410 \| 12110 \| 12310 \| 12410 \|` (419); `\| National Weather Service ETA 29km \| 11 \| 111 \| 311 \| 411 \| 12111 \| 12311 \| 12411 \|` (420); `\| Ocean Weather Inc (OWI) \| 12 \| 112 \| 312 \| 412 \| 12112 \| 12312 \| 12412 \|` (421); `\| H\*Wind \| 15 \| 115 \| 315 \| 415 \| 12115 \| 12315 \| 12415 \|` (422); `\| Dynamic Asymmetric Model \| 19 \| 119 \| 319 \| 419 \| 12119 \| 12319 \| 12419 \|` (423); `\| Generalized Asymmetric Holland Model \| 20 \| 120 \| 320 \| 420 \| 12120 \| 12320 \| 12420 \|` (424). |
| 425–440 | 페이지 말미 스크립트·공백 — 유틸리티 표시와 페이지 사전 읽기(prefetch) 설정이 들어 있다(428–430). 쿠키 안내, 슬라이드 표시와 New Relic 페이지 계측 설정을 포함한다(433–440). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 406–408: 표의 첫 행은 빈 셀만 포함한다(406). 표 구분선은 다음 행에 있다(407). 실제 열 제목은 구분선 다음 행에 있다(408).
- 417: 모델 이름은 `symmetrc vortex model`로 적혀 있다.
