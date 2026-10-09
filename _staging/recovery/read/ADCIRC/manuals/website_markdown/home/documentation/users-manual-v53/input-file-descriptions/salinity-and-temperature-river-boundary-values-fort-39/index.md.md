---
file: models/ADCIRC/raw/manuals/website_markdown/home/documentation/users-manual-v53/input-file-descriptions/salinity-and-temperature-river-boundary-values-fort-39/index.md
lines: 438
sha256: 155261b98b980ef2ed4a294e39151d8e45ec65f5662c33f6731d865483cc4722
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# Salinity and Temperature River Boundary Values (fort.39) — 판독 구간 기록

구간은 1행부터 438행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–12 | 웹페이지 시작 코드 — New Relic 초기 설정과 브라우저 계측 코드가 있다(1–2). 뒤에는 빈 줄이 이어진다(3–12). |
| 13–77 | 웹페이지 스타일(CSS) / 검색·본문 틀 — 검색 입력란과 버튼, 제목, 본문 글꼴, 컨테이너(container), 머리글과 오른쪽 본문 영역의 스타일을 지정한다(13–77). |
| 78–142 | 웹페이지 스타일 / 본문·링크·위치 표시 — 한 열 본문 영역, 문단, 링크, 위치 표시(breadcrumb), 활성 메뉴, 인용 블록과 두 열 본문 영역의 스타일을 지정한다(78–142). |
| 143–200 | 웹페이지 스타일 / 탐색 메뉴 — 탐색 영역, 메뉴 목록, 항목, 링크와 하위 메뉴의 배치를 지정한다(143–200). 메뉴 구분선 이미지 경로를 참조한다(166). |
| 201–230 | 웹페이지 스타일 / 메뉴 상태 — 마우스를 올린 항목, 열린 하위 메뉴와 현재 페이지 항목의 스타일을 지정한다(201–225). 메뉴 배경 이미지 경로를 참조한다(202). 콘텐츠 높이, 링크 글자 굵기, 태그 표시와 이미지 표시 크기 규칙이 이어진다(226–230). |
| 231–240 | 페이지 제목·메타데이터 — 페이지 제목과 구조화 데이터(JSON-LD)가 있다(232·237). 구조화 데이터는 원문 URL, 게시 시각, 웹사이트, 위치 표시와 검색 동작을 담는다(237). 나머지 행은 빈 줄이다. |
| 241–270 | WordPress 화면 지원 코드 — 이모지(emoji) 설정과 지원 여부 검사 코드가 있다(242–246). 이모지, 버튼, 파일 링크, 색상·글꼴·간격 및 블록 배치 스타일이 이어진다(249–269). 빈 줄도 포함한다. |
| 271–303 | 관리 표시·접속 분석·배경 — 빈 줄, 지원 표시 스타일, Beehive 분석 설정과 사이트 배경 스타일이 있다(271–300). 사이트 배경 이미지 URL을 참조한다(300). 마지막 빈 줄도 포함한다(301–303). |
| 304–322 | 사이트 머리글·Community 메뉴 — 빈 제목 마크업, 사이트 이름, 공식 웹사이트 문구와 탐색 건너뛰기 링크가 있다(304–310). 개발 그룹·협력기관 및 사용자 메뉴를 나열한다(312–322). |
| 323–358 | Documentation 메뉴 — v50·v51·v52·v53 매뉴얼, 입력·출력 설명, 버전 이력, 컴파일·명령행 옵션, FAQ와 관련 문서 링크를 나열한다(323–358). |
| 359–401 | Related software·News·Products·ASGS 메뉴 — 유틸리티(utility), 격자 생성기, 모임 자료, 예보, 사례, 조석 데이터와 ASGS 링크를 나열한다(359–400). 메뉴에는 모임 사진을 가리키는 일반 링크가 있다(368·370·374·375·387·389). 끝 빈 줄도 포함한다(401). |
| 402–407 | Salinity and Temperature River Boundary Values (fort.39) / 적용 조건 — 위치 표시와 하천 염분(salinity)·수온(temperature) 경계값 제목이 있다(402–404). 격자(mesh) 파일 fort.14에 경압성(baroclinic) 하천 경계가 있고 IDEN이 양수일 때 이 파일을 읽는다(406). 적용 조건 문장을 그대로 옮긴다. 원문: `The salinity and temperature river boundary condition file (fort.39) is read in when the [mesh file (fort.14)](../adcirc-grid-and-boundary-information-file-fort-14/) contains a baroclinic river boundary ([**IBTYPE**](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#IBTYPE)=122) and [**IDEN**](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#IDEN) is positive.` (406). |
| 408–419 | 입력 파일 구조 — RIVBCTIMINC와 RIVBCSTATIM을 한 줄에 둔다(408). 데이터셋(dataset)에 대한 i 반복문 안에 하천 경계 절점(node)에 대한 j 반복문을 둔다(410–412). 각 절점에서 k=1,NFEN에 대한 bc(j,k) 배열을 읽는 구조를 제시한다(414). 반복 종료와 빈 줄을 포함한다(416–419). 원문: `**RIVBCTIMINC, RIVBCSTATIM**` (408); `for i=1 to numberOfDataSets` (410); `for j=1 to number\_of\_river\_boundary\_nodes` (412); `**(**bc(j,k)**, k=1,NFEN)**` (414); `end j loop` (416); `end i loop` (418). |
| 420–423 | 시간 매개변수·IDEN별 경계값 — RIVBCTIMINC는 경계조건 데이터셋 사이의 시간 간격이다(420). RIVBCSTATIM은 초기 시작(cold start) 시각에 대한 경계조건 데이터 시작 시각이다(420). 두 시간의 단위는 초(seconds)이다(420). IDEN 값별로 염분, 수온 또는 두 배열을 사용하는 문장을 그대로 옮긴다(422). 원문: `where RIVBCTIMINC is the time increment (in seconds) between the boundary condition datasets; RIVBCSTATIM is the time (in seconds) when the boundary condition data start, relative to the cold start time.` (420); `The bc(j,k) values depend on the value of [**IDEN**](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#IDEN). If IDEN=2, then the salinity boundary condition values should be used for bc(j,k). If IDEN=3, then the temperature boundary condition values should be used for bc(j,k). If IDEN=4, then the bc(j,k) should be replaced with salbc(j,k),tempbc(j,k).` (422). |
| 424–438 | 웹페이지 끝 코드 — 빈 줄과 화면 유틸리티 호출이 있다(424–426). 링크 사전 가져오기(prefetch), 쿠키 안내 설정, 슬라이더 표시 보조 코드와 New Relic 페이지 정보가 이어진다(428–438). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 410·412·414: `numberOfDataSets`, `number\_of\_river\_boundary\_nodes`, `NFEN`을 반복 상한으로 사용한다. 이 파일 본문에는 이 이름들의 별도 정의가 없다.
- 166·202·300·368·370·374·375·387·389: CSS의 이미지 경로 3개와 탐색 메뉴의 사진 링크 6개에 대해 그림 파일 없음. `models/ADCIRC/raw/manuals/website_markdown/` 아래에서 해당 로컬 이미지 사본을 찾지 못했다.
