---
file: models/ADCIRC/raw/manuals/website_markdown/home/documentation/users-manual-v53/input-file-descriptions/salinity-boundary-condition-input-fort-36/index.md
lines: 432
sha256: 50d81c994b37551f2fb0b2f2a254bebe0820fd7f02990c40e392ff1b96ade62c
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# Salinity Boundary Condition Input (fort.36) — 판독 구간 기록

구간은 1행부터 432행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–12 | 웹페이지 시작 코드 — New Relic 초기 설정과 브라우저 계측 코드가 있다(1–2). 뒤에는 빈 줄이 이어진다(3–12). |
| 13–77 | 웹페이지 스타일(CSS) / 검색·본문 틀 — 검색 입력란과 버튼, 제목, 본문 글꼴, 컨테이너(container), 머리글과 오른쪽 본문 영역의 스타일을 지정한다(13–77). |
| 78–142 | 웹페이지 스타일 / 본문·링크·위치 표시 — 한 열 본문 영역, 문단, 링크, 위치 표시(breadcrumb), 활성 메뉴, 인용 블록과 두 열 본문 영역의 스타일을 지정한다(78–142). |
| 143–200 | 웹페이지 스타일 / 탐색 메뉴 — 탐색 영역, 메뉴 목록, 항목, 링크와 하위 메뉴의 배치를 지정한다(143–200). 메뉴 구분선 이미지 경로를 참조한다(166). |
| 201–230 | 웹페이지 스타일 / 메뉴 상태 — 마우스를 올린 항목, 열린 하위 메뉴와 현재 페이지 항목의 스타일을 지정한다(201–225). 메뉴 배경 이미지 경로를 참조한다(202). 콘텐츠 높이, 링크 글자 굵기, 태그 표시와 이미지 표시 크기 규칙이 이어진다(226–230). |
| 231–238 | 페이지 제목·메타데이터 — 페이지 제목과 구조화 데이터(JSON-LD)가 있다(232·235). 구조화 데이터는 원문 URL, 게시·수정 시각, 웹사이트, 위치 표시와 검색 동작을 담는다(235). 나머지 행은 빈 줄이다. |
| 239–268 | WordPress 화면 지원 코드 — 이모지(emoji) 설정과 지원 여부 검사 코드가 있다(240–244). 이모지, 버튼, 파일 링크, 색상·글꼴·간격 및 블록 배치 스타일이 이어진다(247–267). 빈 줄도 포함한다. |
| 269–301 | 관리 표시·접속 분석·배경 — 빈 줄, 지원 표시 스타일, Beehive 분석 설정과 사이트 배경 스타일이 있다(269–298). 사이트 배경 이미지 URL을 참조한다(298). 마지막 빈 줄도 포함한다(299–301). |
| 302–320 | 사이트 머리글·Community 메뉴 — 빈 제목 마크업, 사이트 이름, 공식 웹사이트 문구와 탐색 건너뛰기 링크가 있다(302–308). 개발 그룹·협력기관 및 사용자 메뉴를 나열한다(310–320). |
| 321–356 | Documentation 메뉴 — v50·v51·v52·v53 매뉴얼, 입력·출력 설명, 버전 이력, 컴파일·명령행 옵션, FAQ와 관련 문서 링크를 나열한다(321–356). |
| 357–399 | Related software·News·Products·ASGS 메뉴 — 유틸리티(utility), 격자 생성기, 모임 자료, 예보, 사례, 조석 데이터와 ASGS 링크를 나열한다(357–398). 메뉴에는 모임 사진을 가리키는 일반 링크가 있다(366·368·372·373·385·387). 끝 빈 줄도 포함한다(399). |
| 400–405 | Salinity Boundary Condition Input (fort.36) / 적용 조건 — 위치 표시와 염분(salinity) 경계조건 입력 파일 제목이 있다(400–402). fort.15에서 지정하는 파일 읽기 조건을 원문 그대로 옮긴다(404). 원문: `The ADCIRC Salinity Boundary Condition Input File (fort.36) is read in when the [**RES\_BC\_FLAG**](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#RES_BC_FLAG) is set to -2, 2, -4, or 4 in the [fort.15 file](https://adcirc.org/home/documentation/users-manual-v53/input-file-descriptions/model-parameter-and-periodic-boundary-condition-file-fort-15/ "Model Parameter and Periodic Boundary Condition File (fort.15)").` (404). |
| 406–417 | 입력 파일 구조 — 데이터셋(dataset)에 대한 i 반복문 안에 날짜 주석 줄과 해양 경계 절점(node)에 대한 k 반복문을 둔다(406–410). 각 절점의 입력 줄은 k와 SALBC(k,m)의 m=1,NFEN 배열이다(412). 반복 종료와 빈 줄을 포함한다(414–417). 원문 입력 형식과 반복 경계를 그대로 옮긴다. 원문: `for i=1 to numberOfDataSets` (406); `**comment line (date)**` (408); `for k=1 to number\_of\_ocean\_boundary\_nodes` (410); `k, (**SALBC(k,m)**, m=1,NFEN)` (412); `end k loop` (414); `end i loop` (416). |
| 418–432 | 웹페이지 끝 코드 — 빈 줄과 화면 유틸리티 호출이 있다(418–420). 링크 사전 가져오기(prefetch), 쿠키 안내 설정, 슬라이더 표시 보조 코드와 New Relic 페이지 정보가 이어진다(422–432). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 406·410·412: `numberOfDataSets`, `number\_of\_ocean\_boundary\_nodes`, `NFEN`을 반복 상한으로 사용한다. 이 파일 본문에는 이 이름들의 별도 정의가 없다. `SALBC(k,m)`의 단위도 이 파일에 제시하지 않는다(412).
- 166·202·298·366·368·372·373·385·387: CSS의 이미지 경로 3개와 탐색 메뉴의 사진 링크 6개에 대해 그림 파일 없음. `models/ADCIRC/raw/manuals/website_markdown/` 아래에서 해당 로컬 이미지 사본을 찾지 못했다.
