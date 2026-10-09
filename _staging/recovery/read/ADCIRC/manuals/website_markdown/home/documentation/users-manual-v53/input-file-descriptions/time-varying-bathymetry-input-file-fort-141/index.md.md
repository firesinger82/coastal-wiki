---
file: models/ADCIRC/raw/manuals/website_markdown/home/documentation/users-manual-v53/input-file-descriptions/time-varying-bathymetry-input-file-fort-141/index.md
lines: 456
sha256: d8547efa80a0f3f20f6da51444e64bd11545ff478fcae8d3aabad433c2d2fd23
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# Time Varying Bathymetry Input File (fort.141) — 판독 구간 기록

구간은 1행부터 456행까지 빈틈없이 이어진다.

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
| 404–407 | Time Varying Bathymetry Input File (fort.141) — 시간 변화 수심(time varying bathymetry) 입력 파일을 사용하는 조건을 설명한다(404–406). 문서는 fort.14의 매개변수 값에 따라 입력 형식이 달라진다고 적는다(406). 조건과 형식 종류 수는 아래 원문과 같다(406). 원문: `The ADCIRC Time Varying Bathymetry Input File (fort.141) is used by ADCIRC whenever the [NDDT](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#NDDT) value in the fort.14 is nonzero. There are two variations of this file, depending on the value of [NDDT](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#NDDT).` (406). |
| 408–423 | Full Domain Bathymetry Change — 전체 영역(full domain)을 대상으로 하는 수심 데이터 세트(data set)의 형식을 제시한다(408–420). 노드(node) 수, 노드 번호 및 수심 변수의 의미를 설명한다(422). 수심 변수는 fort.14의 변수 정의로 연결한다(422). 적용 값과 입력 형식은 원문과 같다(410–422). 원문: `If [NDDT](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#NDDT) is +/-1, then each bathymetry dataset in the file covers the full domain, and the file format is as follows:` (410); `for i=1 to numDataSets` (412); `for j=1 to **[NP](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#NP)**` (414); `**j, depth(j)**` (416); `end j loop` (418); `end i loop` (420); `where NP is the number of nodes in the horizontal mesh, j is the node number, and depth(j) has the same meaning as [DP](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#DP) in the mesh file (fort.14).` (422). |
| 424–441 | Limited Area Bathymetry Change — 영역 일부(limited area)를 대상으로 하는 수심 데이터 세트 형식을 제시한다(424–438). 해시 기호(hash mark)를 이용한 데이터 세트 구분을 설명한다(440). 이 구분 형식은 데이터 세트마다 다른 레코드(record) 수를 허용한다(440). 적용 값, 입력 줄 및 구분 기호의 열 위치는 원문과 같다(426–440). 원문: `If [NDDT](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#NDDT) is +/-2, then each dataset in the fort.141 file covers only part of the domain, and the file format is as follows:` (426); `for i=1 to numDataSets` (428); `” #”` (430); `for j=1 to areaNodes` (432); `**j, depth(j)**` (434); `end j loop` (436); `end i loop` (438); `The separation between datasets is achieved by placing a hash mark (“#”) in the second column of a line. This formatting allows each dataset to have a different number of records, thus enabling simulations where the number of nodes that change their bathymetry varies over time.` (440). |
| 442–456 | 웹페이지 끝부분 — 유틸리티 호출과 링크 미리 가져오기(prefetch) 설정이 들어 있다(444–446). 쿠키 안내문, jQuery 코드 및 New Relic 정보가 이어진다(449–456). 주변 빈 줄도 이 구간에 포함한다(442–456). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 412·428·432행: `numDataSets`와 `areaNodes`가 반복의 상한으로 쓰인다. 이 이름들의 별도 정의는 파일 본문에 없다.
- 430행: 데이터 세트 구분 줄은 `” #”`로 적혀 있다. 440행의 설명은 둘째 열에 해시 기호를 놓으라고 적는다. 430행의 따옴표를 입력 파일에 포함하는지는 본문에 명시하지 않는다.
