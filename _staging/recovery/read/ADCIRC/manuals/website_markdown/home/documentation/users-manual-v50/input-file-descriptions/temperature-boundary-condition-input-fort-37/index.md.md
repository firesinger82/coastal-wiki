---
file: models/ADCIRC/raw/manuals/website_markdown/home/documentation/users-manual-v50/input-file-descriptions/temperature-boundary-condition-input-fort-37/index.md
lines: 433
sha256: 97706dc2919c59ceb9e686c505f0288563747b91d4c17ac7694d6a00ef753319
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# index.md — 판독 구간 기록

구간은 1행부터 433행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–12 | 웹 계측 스크립트 — New Relic 초기 설정과 로더(loader)를 포함한다(1–2). 나머지는 빈 줄이다(3–12). |
| 13–77 | 웹 스타일(style) — 검색 입력칸, 검색 버튼, 제목, 본문, 컨테이너(container), 헤더(header), 태그와 우측 콘텐츠 영역의 CSS를 포함한다(13–77). |
| 78–142 | 웹 스타일 — 한 열 콘텐츠, 콘텐츠 내부, 문단, 링크, 탐색 경로(breadcrumb), 인용문과 좌우 콘텐츠 영역의 CSS를 포함한다(78–142). |
| 143–184 | 웹 메뉴 스타일 — 접근 메뉴와 최상위 항목의 배치, 배경 이미지 URL, 링크와 첫 하위 메뉴 위치의 CSS를 포함한다(143–184). |
| 185–230 | 웹 메뉴 스타일 — 하위 메뉴, 마우스 올림 상태, 현재 페이지 표시와 이미지 고유 크기 CSS를 포함한다(185–230). |
| 231–240 | 페이지 제목·메타데이터(metadata) — 페이지 제목을 적는다(232). JSON-LD에 원문 URL, 게시·수정 시각, 탐색 경로(breadcrumb)와 검색 기능을 적는다(235). 빈 줄도 포함한다(231–240). |
| 241–284 | WordPress 스크립트·스타일(style) — 이모지(emoji) 지원 검사, 이모지 표시, 블록 버튼, 색·비율·글꼴·간격·그림자 프리셋(preset)과 레이아웃(layout) CSS를 포함한다(241–268). 뒤 빈 줄도 포함한다(269–284). |
| 285–302 | 관리·분석·배경 설정 — 지원 표시 CSS, Beehive 분석 설정과 사이트 배경 이미지 CSS를 포함한다(285–299). 빈 줄도 포함한다(300–302). |
| 303–348 | 사이트 머리글·문서 메뉴 — ADCIRC 링크와 공식 사이트 표제를 적는다(303–307). 탐색 생략 링크, 커뮤니티(community), 사용자 설명서 V50–v53, 컴파일·명령행 문서와 예제 메뉴를 나열한다(309–348). |
| 349–400 | 사이트 자료·뉴스 메뉴 — 보고서·관련 소프트웨어·사용자 모임·허리케인(hurricane) 예제·제품과 ASGS 링크를 나열한다(349–399). 빈 줄도 포함한다(400). |
| 401–406 | Temperature Boundary Condition Input (fort.37) / 적용 조건 — 탐색 경로와 절 제목을 포함한다(401–403). fort.15의 RES_BC_FLAG가 지정된 네 값 중 하나일 때 온도 경계 조건(temperature boundary condition) 입력을 읽는다고 적는다(405). 원문: `The temperature bounday condition input file (fort.37) is read in when the [**RES\_BC\_FLAG**](../../parameter-definitions#RES_BC_FLAG) is set to -3, 3, -4, or 4 in the [fort.15 file](https://adcirc.org/home/documentation/users-manual-v50/input-file-descriptions/model-parameter-and-periodic-boundary-condition-file-fort-15/ "Model Parameter and Periodic Boundary Condition File (fort.15)").` (405). |
| 407–418 | 입력 형식 — 자료 묶음(data set)마다 날짜 주석 행을 읽는다(407–409). 해양 경계 노드(ocean boundary node)를 반복하고 각 노드의 NFEN 범위 TEMPBC 배열을 읽는 형식을 제시한다(411–417). 원문: `for i=1 to numberOfDataSets` (407); `**comment line (date)**` (409); `for k=1 to number\_of\_ocean\_boundary\_nodes` (411); `k, (**TEMPBC(k,m)**, m=1,NFEN)` (413); `end k loop` (415); `end i loop` (417). |
| 419–433 | 웹 후미 스크립트 — 빈 줄, 유틸리티(utility) 표시 호출, 링크 사전 읽기(prefetch) 규칙, 쿠키(cookie) 안내 설정, jQuery와 New Relic 정보를 포함한다(419–433). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 407·411: 반복 범위 `numberOfDataSets`와 `number\_of\_ocean\_boundary\_nodes`의 별도 정의를 이 파일에서 제시하지 않는다.
- 413: TEMPBC의 단위와 NFEN의 의미를 이 파일에서 정의하지 않는다.
