---
file: models/ADCIRC/raw/manuals/website_markdown/home/documentation/users-manual-v51/input-file-descriptions/salinity-and-temperature-river-boundary-values-fort-39/index.md
lines: 439
sha256: 92865cf717ea5e29d3fec7c967d6209ab50d94851e89060676a0b4a7f979e4f0
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# salinity-and-temperature-river-boundary-values-fort-39/index.md — 판독 구간 기록

구간은 1행부터 439행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–12 | 웹 계측 스크립트(JavaScript) — New Relic 초기화와 브라우저 계측 로더가 들어 있다(1–2). 뒤의 빈 줄도 포함한다(3–12). |
| 13–77 | 사이트 스타일(CSS) / 검색·머리말·본문 — 검색 필드와 버튼, 링크, 글꼴, 머리말, 컨테이너 및 오른쪽 본문 영역의 표시 규칙을 적는다(13–77). |
| 78–150 | 사이트 스타일(CSS) / 본문·탐색 영역 — 단일 열 본문, 문단, 링크, 탐색 경로(breadcrumb), 인용문 및 메뉴 영역의 표시 규칙을 적는다(78–150). |
| 151–230 | 사이트 스타일(CSS) / 메뉴 — 메뉴 항목과 하위 메뉴, 마우스 위치에 따른 표시 및 이미지 크기 규칙을 적는다(151–230). 배경 이미지 URL이 있다(166·202). |
| 231–247 | 페이지 제목·구조화 메타데이터 — 페이지 제목(232)과 페이지 주소·게시일·탐색 경로를 담은 JSON-LD(237)가 있다. WordPress 이모지(emoji) 설정과 지원 판정 스크립트를 포함한다(243–247). |
| 248–286 | WordPress 스타일 — 이모지 표시(250–260), 버튼(263–264), 색상·종횡비·글자 크기·간격·그림자 및 배치 설정(267–270)을 적는다. 뒤의 빈 줄도 포함한다(271–286). |
| 287–304 | 관리 표시·사이트 계측·배경 — 관리 표시 색상(287–289), Beehive/Google 계측 설정(293–299), 사이트 배경 이미지 URL(301)을 포함한다. 빈 줄도 포함한다. |
| 305–323 | 사이트 머리말·Community 메뉴 — 빈 제목 표식(305), 사이트 이름과 설명(307·309), 탐색 건너뛰기 링크(311), 개발자·협력 기관·사용자 링크(313–323)가 있다. |
| 324–359 | Documentation 메뉴 — V50·V51·v52·v53 사용자 매뉴얼과 입력·출력 설명, 버전 이력, 컴파일·명령행 옵션 및 FAQ 링크를 나열한다(324–349). 예제·보고서·이론·특수 기능·관련 출판물·하위 영역 모델링 링크도 포함한다(350–359). |
| 360–394 | Related software·News 메뉴 — 유틸리티(utility)와 격자 생성기(grid generator) 링크(360–362), 사용자 모임·워크숍의 발표·일정·단체 사진 및 허리케인(hurricane) 관련 페이지 링크를 나열한다(363–394). 단체 사진은 탐색용 일반 링크로 적혀 있다. |
| 395–404 | Products·ASGS 메뉴·현재 페이지 탐색 경로 — 조석 데이터베이스(tidal database), 출판물, 격자, 예측 및 표층 기름 이동 링크(395–400), ASGS 링크(401), 현재 문서의 탐색 경로(403)를 포함한다. |
| 405–408 | Salinity and Temperature River Boundary Values (fort.39) / 읽기 조건 — 염분(salinity)·수온(temperature) 하천 경계 파일은 fort.14 격자 파일(mesh file)에 경압 하천 경계(baroclinic river boundary)가 있고 IBTYPE = 122이며 IDEN이 양수일 때 읽는다(407). 원문이 연결하는 fort.14 문서는 V50 경로이다. 원문: `The salinity and temperature river boundary condition file (fort.39) is read in when the [mesh file (fort.14)](https://adcirc.org/home/documentation/users-manual-v50/input-file-descriptions/adcirc-grid-and-boundary-information-file-fort-14/) contains a baroclinic river boundary ([**IBTYPE**](../../parameter-definitions#IBTYPE)=122) and [**IDEN**](../../parameter-definitions#IDEN) is positive.` (407). |
| 409–420 | 기본 입력 구조 / 시각 설정·중첩 반복 — RIVBCTIMINC와 RIVBCSTATIM을 먼저 적는다(409). 바깥 반복은 i = 1부터 numberOfDataSets까지이며 안쪽 반복은 j = 1부터 number_of_river_boundary_nodes까지이다(411·413). 각 자료 줄은 bc(j,k), k=1,NFEN 형식이다(415). 입력 줄의 강조 표식과 두 반복 종료 줄을 원문 그대로 옮긴다(415·417·419). 원문: `**RIVBCTIMINC, RIVBCSTATIM**` (409); `for i=1 to numberOfDataSets` (411); `for j=1 to number\_of\_river\_boundary\_nodes` (413); `**(**bc(j,k)**, k=1,NFEN)**` (415); `end j loop` (417); `end i loop` (419). |
| 421–424 | 시간 단위·IDEN별 자료 값 — RIVBCTIMINC는 경계 자료 집합 사이의 시간 간격이며 초 단위이다. RIVBCSTATIM은 콜드 스타트(cold start) 시각을 기준으로 경계 자료가 시작되는 초 단위 시각이다(421). IDEN = 2이면 bc(j,k)에 염분 값을 쓰고 IDEN = 3이면 수온 값을 쓴다. IDEN = 4이면 bc(j,k)를 salbc(j,k),tempbc(j,k)로 바꾸어야 한다(423). 정의와 적용 조건을 원문 그대로 옮긴다. 원문: `where RIVBCTIMINC is the time increment (in seconds) between the boundary condition datasets; RIVBCSTATIM is the time (in seconds) when the boundary condition data start, relative to the cold start time.` (421); `The bc(j,k) values depend on the value of [**IDEN**](../../parameter-definitions#IDEN). If IDEN=2, then the salinity boundary condition values should be used for bc(j,k). If IDEN=3, then the temperature boundary condition values should be used for bc(j,k). If IDEN=4, then the bc(j,k) should be replaced with salbc(j,k),tempbc(j,k).` (423). |
| 425–439 | 사이트 후처리 스크립트·쿠키 안내 — 유틸리티 표시 호출(427), 사전 가져오기(prefetch) 규칙(429), 쿠키 동의 안내 설정(432–434), jQuery 클래스 변경(438) 및 New Relic 정보(439)가 있다. 빈 줄도 포함한다. |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 403·407행: 현재 문서의 탐색 경로는 User’s Manual – V51이다. 407행의 fort.14 링크는 `users-manual-v50` 경로를 사용한다.
- 415행: 반복 상한 기호 `NFEN`이 있지만 이 파일에는 그 정의가 없다. 이 입력 줄의 `NFEN`에는 정의 링크도 없다.
- 407·423행: 파일 읽기 조건은 IDEN이 양수인 경우로 적혀 있다. bc(j,k) 값 선택 설명은 IDEN=2·3·4에 대해서만 적혀 있다.
