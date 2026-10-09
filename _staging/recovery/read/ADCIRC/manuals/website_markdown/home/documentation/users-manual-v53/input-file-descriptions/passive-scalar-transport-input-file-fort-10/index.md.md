---
file: models/ADCIRC/raw/manuals/website_markdown/home/documentation/users-manual-v53/input-file-descriptions/passive-scalar-transport-input-file-fort-10/index.md
lines: 454
sha256: 6bb2af199d6572cb53965e94db5ad5e3f59df096f6a5ff0c8ce81e6392f79d97
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# Passive Scalar Transport Input File (fort.10) — 판독 구간 기록

구간은 1행부터 454행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–12 | 웹페이지 시작 코드 — New Relic 초기 설정과 브라우저 계측 코드가 있다(1–2). 뒤에는 빈 줄이 이어진다(3–12). |
| 13–77 | 웹페이지 스타일(CSS) / 검색·본문 틀 — 검색 입력란과 버튼, 제목, 본문 글꼴, 컨테이너(container), 머리글과 오른쪽 본문 영역의 스타일을 지정한다(13–77). |
| 78–142 | 웹페이지 스타일 / 본문·링크·위치 표시 — 한 열 본문 영역, 문단, 링크, 위치 표시(breadcrumb), 활성 메뉴, 인용 블록과 두 열 본문 영역의 스타일을 지정한다(78–142). |
| 143–200 | 웹페이지 스타일 / 탐색 메뉴 — 탐색 영역, 메뉴 목록, 항목, 링크와 하위 메뉴의 배치를 지정한다(143–200). 메뉴 구분선 이미지 경로를 참조한다(166). |
| 201–230 | 웹페이지 스타일 / 메뉴 상태 — 마우스를 올린 항목, 열린 하위 메뉴와 현재 페이지 항목의 스타일을 지정한다(201–225). 메뉴 배경 이미지 경로를 참조한다(202). 콘텐츠 높이, 링크 글자 굵기, 태그 표시와 이미지 표시 크기 규칙이 이어진다(226–230). |
| 231–240 | 페이지 제목·메타데이터 — 페이지 제목과 구조화 데이터(JSON-LD)가 있다(232·237). 구조화 데이터는 원문 URL, 게시·수정 시각, 웹사이트, 위치 표시와 검색 동작을 담는다(237). 나머지 행은 빈 줄이다. |
| 241–270 | WordPress 화면 지원 코드 — 이모지(emoji) 설정과 지원 여부 검사 코드가 있다(242–246). 이모지, 버튼, 파일 링크, 색상·글꼴·간격 및 블록 배치 스타일이 이어진다(249–269). 빈 줄도 포함한다. |
| 271–303 | 관리 표시·접속 분석·배경 — 빈 줄, 지원 표시 스타일, Beehive 분석 설정과 사이트 배경 스타일이 있다(271–300). 사이트 배경 이미지 URL을 참조한다(300). 마지막 빈 줄도 포함한다(301–303). |
| 304–322 | 사이트 머리글·Community 메뉴 — 빈 제목 마크업, 사이트 이름, 공식 웹사이트 문구와 탐색 건너뛰기 링크가 있다(304–310). 개발 그룹·협력기관 및 사용자 메뉴를 나열한다(312–322). |
| 323–358 | Documentation 메뉴 — v50·v51·v52·v53 매뉴얼, 입력·출력 설명, 버전 이력, 컴파일·명령행 옵션, FAQ와 관련 문서 링크를 나열한다(323–358). |
| 359–401 | Related software·News·Products·ASGS 메뉴 — 유틸리티(utility), 격자 생성기, 모임 자료, 예보, 사례, 조석 데이터와 ASGS 링크를 나열한다(359–400). 메뉴에는 모임 사진을 가리키는 일반 링크가 있다(368·370·374·375·387·389). 끝 빈 줄도 포함한다(401). |
| 402–407 | Passive Scalar Transport Input File (fort.10) / 설명 — 위치 표시와 수동 스칼라(passive scalar) 수송 입력 파일 제목이 있다(402–404). 굵은 변수명이 입력 데이터 한 줄을 나타낸다(406). 빈 줄은 가독성만을 위한 것이다(406). 반복문(loop)은 입력 여러 줄을 나타낸다(406). 각 변수의 정의는 링크로 제공한다고 적는다(406). 원문: `The basic file structure is shown below. Each line of input data is represented by a line containing the input variable name(s) in bold face type. Blank lines are only to enhance readability. Loops indicate multiple lines of input. Definitions of each variable are provided via hot links.` (406). |
| 408–421 | File structure for a 2DDI run — 헤더(header) 두 줄 뒤에 NVP를 둔다(408–414). k 반복문은 jki와 DACONC(jki)를 한 줄에 둔다(416–420). 원문 입력 형식과 반복 경계를 그대로 옮긴다. 원문: `File structure for a 2DDI run:` (408); `**Header Line 1**` (410); `**Header Line 2**` (412); `**[NVP](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#NVP)**` (414); `for k=1 to **[NVP](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#NVP)**` (416); `**[jki](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#jki),[DACONC(jki)](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#DACONC)**` (418); `end k loop` (420). |
| 422–439 | File structure for a 3D run — 헤더 두 줄 뒤에 NVN과 NVP를 한 줄에 둔다(422–428). 바깥 k 반복문 안에 j 반복문을 둔다(430–432). 안쪽 반복문은 NHNN, NVNN, CONC(NHNN,NVNN)을 한 줄에 둔다(434). 반복 종료와 빈 줄을 포함한다(436–439). 원문 입력 형식과 반복 경계를 그대로 옮긴다. 원문: `File structure for a 3D run:` (422); `**Header Line 1**` (424); `**Header Line 2**` (426); `**[NVN](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#NVN), [NVP](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#NVP)**` (428); `for k=1 to **[NVP](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#NVP)**` (430); `for j=1 to **[NVN](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#NVN)**` (432); `**[NHNN](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#NHNN),[NVNN](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#NVNN),[CONC(NHNN,NVNN)](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#CONC)**` (434); `end j loop` (436); `end k loop` (438). |
| 440–454 | 웹페이지 끝 코드 — 빈 줄과 화면 유틸리티 호출이 있다(440–442). 링크 사전 가져오기(prefetch), 쿠키 안내 설정, 슬라이더 표시 보조 코드와 New Relic 페이지 정보가 이어진다(444–454). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 414·418·428·434: `NVP`, `jki`, `DACONC(jki)`, `NVN`, `NHNN`, `NVNN`, `CONC(NHNN,NVNN)`의 정의는 외부 매개변수 페이지 링크로만 제시한다. 이 파일 본문에는 해당 이름의 정의·기본값·범위·단위가 없다.
- 166·202·300·368·370·374·375·387·389: CSS의 이미지 경로 3개와 탐색 메뉴의 사진 링크 6개에 대해 그림 파일 없음. `models/ADCIRC/raw/manuals/website_markdown/` 아래에서 해당 로컬 이미지 사본을 찾지 못했다.
