---
file: models/ADCIRC/raw/manuals/website_markdown/home/documentation/users-manual-v50/input-file-descriptions/surface-temperature-boundary-values-fort-38/index.md
lines: 457
sha256: 2183fdd20a9d0b768717d2a2cc9976a02ad64570a34b6cb162527d4e858629cc
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
| 403–408 | Surface Temperature Boundary Values (fort.38) / 적용 조건 — 탐색 경로와 절 제목을 포함한다(403–405). 횡방향 온도 경계 조건(lateral temperature boundary condition)을 사용할 때 fort.38을 읽는 RES_BC_FLAG 값과 표면 열유속(surface heat flux) 매개변수화(parameterization)를 제어하는 BCFLAG_TEMP를 적는다(407). 원문: `The surface temperature boundary condition input file (fort.38) is read in when the [**RES\_BC\_FLAG**](../../parameter-definitions#RES_BC_FLAG) is set to -3, 3, -4, or 4 in the [fort.15 file](https://adcirc.org/home/documentation/users-manual-v50/input-file-descriptions/model-parameter-and-periodic-boundary-condition-file-fort-15/ "Model Parameter and Periodic Boundary Condition File (fort.15)") (i.e., when a lateral temperature boundary condition is being used) and its format depends on the [**BCFLAG\_TEMP**](../../parameter-definitions#BCFLAG_TEMP) parameter in the fort.15, which controls the surface heat flux parameterization in ADCIRC.` (407). |
| 409–420 | BCFLAG_TEMP 1 / 입력 형식 — 자료 묶음(data set)마다 전체 수평 격자 노드를 반복하여 노드 번호와 열유속 변수를 읽는 순서를 제시한다(409–419). 원문: `If [**BCFLAG\_TEMP**](../../parameter-definitions#BCFLAG_TEMP)=1 in the fort.15, the format of the fort.38 is as follows:` (409); `for i=1 to numberOfDataSets` (411); `for k=1 to [**NP**](../../parameter-definitions#NP)` (413); `k, **q\_heat(k)**` (415); `end k loop` (417); `end i loop` (419). |
| 421–430 | BCFLAG_TEMP 2 / 입력 형식 — 각 자료 묶음의 전체 노드에서 여섯 열유속 성분을 읽는 암묵적 Fortran 입출력 반복(implicit Fortran i/o loop)을 제시한다(421–429). 괄호가 이 반복을 나타낸다고 적는다(429). 원문: `If [**BCFLAG\_TEMP**](../../parameter-definitions#BCFLAG_TEMP)=2 in the fort.15, the format of the fort.38 is as follows:` (421); `for i=1 to numberOfDataSets` (423); `(K, (**TMP(K,J)**, J=1,6),K=1,[**NP**](../../parameter-definitions#NP))` (425); `end i loop` (427); `where TMP(K,J) is the surface heat flux parameter Jth heat flux component for the Kth horizontal mesh node. The data are read using an implicit Fortran i/o loop, thus the parentheses around the statement.` (429). |
| 431–440 | BCFLAG_TEMP 3 / 입력 형식 — 각 자료 묶음의 전체 노드에서 네 열유속 성분을 읽는 암묵적 Fortran 입출력 반복을 제시한다(431–439). 괄호가 이 반복을 나타낸다고 적는다(439). 원문: `If [**BCFLAG\_TEMP**](../../parameter-definitions#BCFLAG_TEMP)=3 in the fort.15, the format of the fort.38 is as follows:` (431); `for i=1 to numberOfDataSets` (433); `(K, (**TMP(K,J)**, J=1,4),K=1,[**NP**](../../parameter-definitions#NP))` (435); `end i loop` (437); `where TMP(K,J) is the surface heat flux parameter Jth heat flux component for the Kth horizontal mesh node. The data are read using an implicit Fortran i/o loop, thus the parentheses around the statement.` (439). |
| 441–442 | 노드 수 정의·추가 설명 참조 — NP를 전체 2차원 영역(2D fulldomain)의 수평 격자 노드 수로 정의한다(441). 3차원 경압 물리(3D baroclinic physics)와 각 BCFLAG_TEMP 값의 자세한 설명을 fort.15 문서로 연결한다(441). 원문: `In all the above cases, [**NP**](../../parameter-definitions#NP) is the number of nodes in the horizontal mesh (i.e., the 2D fulldomain number of nodes). See the [fort.15](https://adcirc.org/home/documentation/users-manual-v50/input-file-descriptions/model-parameter-and-periodic-boundary-condition-file-fort-15/) documentation on 3D baroclinic physics (particularly the explanation of various [**BCFLAG\_TEMP**](../../parameter-definitions#BCFLAG_TEMP) values) for more details.` (441). |
| 443–457 | 웹 후미 스크립트 — 빈 줄, 유틸리티(utility) 표시 호출, 링크 사전 읽기(prefetch) 규칙, 쿠키(cookie) 안내 설정, jQuery와 New Relic 정보를 포함한다(443–457). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 411·423·433: 자료 묶음 반복의 `numberOfDataSets`를 이 파일에서 정의하지 않는다.
- 415: `q\_heat(k)`의 정의와 단위를 이 파일에서 적지 않는다.
- 425·429·435·439: TMP를 J번째 열유속 성분이라고 설명하지만 여섯 성분 또는 네 성분의 개별 이름과 단위를 이 파일에서 적지 않는다.
