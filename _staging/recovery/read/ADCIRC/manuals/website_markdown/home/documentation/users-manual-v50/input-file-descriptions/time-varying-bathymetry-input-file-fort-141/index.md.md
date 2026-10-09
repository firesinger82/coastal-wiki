---
file: models/ADCIRC/raw/manuals/website_markdown/home/documentation/users-manual-v50/input-file-descriptions/time-varying-bathymetry-input-file-fort-141/index.md
lines: 457
sha256: 01ae41d9fee41a2bbe7d8f34dec996aefcf0af24af2cf7a8bffac9f714c61229
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# index.md — 판독 구간 기록

구간은 1행부터 457행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–12 | 웹 계측 스크립트 — New Relic 초기 설정과 로더(loader)를 포함한다(1–2). 나머지는 빈 줄이다(3–12). |
| 13–77 | 웹 스타일(style) — 검색 입력칸, 검색 버튼, 제목, 본문, 컨테이너(container), 헤더(header), 태그와 우측 콘텐츠 영역의 CSS를 포함한다(13–77). |
| 78–142 | 웹 스타일 — 한 열 콘텐츠, 콘텐츠 내부, 문단, 링크, 탐색 경로(breadcrumb), 인용문과 좌우 콘텐츠 영역의 CSS를 포함한다(78–142). |
| 143–184 | 웹 메뉴 스타일 — 접근 메뉴와 최상위 항목의 배치, 배경 이미지 URL, 링크와 첫 하위 메뉴 위치의 CSS를 포함한다(143–184). |
| 185–230 | 웹 메뉴 스타일 — 하위 메뉴, 마우스 올림 상태, 현재 페이지 표시와 이미지 고유 크기 CSS를 포함한다(185–230). |
| 231–242 | 페이지 제목·메타데이터(metadata) — 페이지 제목을 적는다(232). JSON-LD에 원문 URL, 게시·수정 시각, 탐색 경로와 검색 기능을 적는다(237). 빈 줄도 포함한다(231–242). |
| 243–286 | WordPress 스크립트·스타일 — 이모지(emoji) 지원 검사, 이모지 표시, 블록 버튼, 색·비율·글꼴·간격·그림자 프리셋(preset)과 레이아웃(layout) CSS를 포함한다(243–270). 뒤 빈 줄도 포함한다(271–286). |
| 287–304 | 관리·분석·배경 설정 — 지원 표시 CSS, Beehive 분석 설정과 사이트 배경 이미지 CSS를 포함한다(287–301). 빈 줄도 포함한다(302–304). |
| 305–350 | 사이트 머리글·문서 메뉴 — ADCIRC 링크와 공식 사이트 표제를 적는다(305–309). 탐색 생략 링크, 커뮤니티(community), 사용자 설명서 V50–v53, 컴파일·명령행 문서와 예제 메뉴를 나열한다(311–350). |
| 351–402 | 사이트 자료·뉴스 메뉴 — 보고서·관련 소프트웨어·사용자 모임·허리케인(hurricane) 예제·제품과 ASGS 링크를 나열한다(351–401). 빈 줄도 포함한다(402). |
| 403–408 | Time Varying Bathymetry Input File (fort.141) / 적용 조건 — 탐색 경로와 절 제목을 포함한다(403–405). fort.14의 NDDT가 0이 아니면 시간 변화 수심(time varying bathymetry) 입력을 사용한다(407). NDDT에 따라 두 파일 형식이 있다고 적는다(407). 원문: `The ADCIRC Time Varying Bathymetry Input File (fort.141) is used by ADCIRC whenever the [NDDT](../../parameter-definitions#NDDT) value in the fort.14 is nonzero. There are two variations of this file, depending on the value of [NDDT](../../parameter-definitions#NDDT).` (407). |
| 409–424 | Full Domain Bathymetry Change / 전체 영역 수심 변화 — NDDT가 ±1이면 각 자료 묶음(data set)이 전체 영역을 포함한다(411). 각 묶음의 모든 노드(node)에 대해 노드 번호와 수심 입력 행을 제시한다(413–421). NP와 j를 정의하고 depth(j)의 의미를 fort.14의 DP 정의에 연결한다(423). 원문: `If [NDDT](../../parameter-definitions#NDDT) is +/-1, then each bathymetry dataset in the file covers the full domain, and the file format is as follows:` (411); `for i=1 to numDataSets` (413); `for j=1 to **[NP](../../parameter-definitions#NP)**` (415); `**j, depth(j)**` (417); `end j loop` (419); `end i loop` (421); `where NP is the number of nodes in the horizontal mesh, j is the node number, and depth(j) has the same meaning as [DP](../../parameter-definitions#DP) in the mesh file (fort.14).` (423). |
| 425–442 | Limited Area Bathymetry Change / 일부 영역 수심 변화 — NDDT가 ±2이면 각 자료 묶음이 영역 일부만 포함한다(427). 구분 행과 areaNodes 반복의 노드 번호·수심 형식을 제시한다(429–439). 구분 행의 두 번째 열에 #를 두어 자료 묶음별 기록 수를 다르게 할 수 있다고 설명한다(441). 원문: `If [NDDT](../../parameter-definitions#NDDT) is +/-2, then each dataset in the fort.141 file covers only part of the domain, and the file format is as follows:` (427); `for i=1 to numDataSets` (429); `” #”` (431); `for j=1 to areaNodes` (433); `**j, depth(j)**` (435); `end j loop` (437); `end i loop` (439); `The separation between datasets is achieved by placing a hash mark (“#”) in the second column of a line. This formatting allows each dataset to have a different number of records, thus enabling simulations where the number of nodes that change their bathymetry varies over time.` (441). |
| 443–457 | 웹 후미 스크립트 — 빈 줄, 유틸리티(utility) 표시 호출, 링크 사전 읽기(prefetch) 규칙, 쿠키(cookie) 안내 설정, jQuery와 New Relic 정보를 포함한다(443–457). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 413·429·433: 반복 범위 `numDataSets`와 `areaNodes`의 별도 정의를 이 파일에서 제시하지 않는다.
- 407·411·427: NDDT의 0 여부와 ±1·±2별 공간 범위를 설명하지만 자료 묶음에 적용하는 시각 또는 시간 간격을 이 파일에서 제시하지 않는다.
- 423: depth(j)의 의미를 다른 파일의 DP 정의에 연결하며 이 파일에서 수심 단위를 적지 않는다.
