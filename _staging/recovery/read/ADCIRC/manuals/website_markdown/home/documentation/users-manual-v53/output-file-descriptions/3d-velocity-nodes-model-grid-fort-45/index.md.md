---
file: models/ADCIRC/raw/manuals/website_markdown/home/documentation/users-manual-v53/output-file-descriptions/3d-velocity-nodes-model-grid-fort-45/index.md
lines: 443
sha256: 139fad089e07a98f9f46f5e93c3d8207240744ac59fa28e390a2c41cbda9e097
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# index.md — 판독 구간 기록

구간은 1행부터 443행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–12 | 웹 페이지 선행 코드 — New Relic 브라우저 계측(browser instrumentation) 설정과 축약 JavaScript를 포함한다(1–2). 빈 줄을 포함한다(3–12). |
| 13–77 | 웹 페이지 스타일 / 검색·제목·레이아웃 — CSS가 검색 입력과 버튼의 크기를 정한다(13–25). CSS가 링크 색, 글꼴, 제목과 페이지 컨테이너(container), 오른쪽 콘텐츠 영역의 배치를 정한다(26–77). |
| 78–142 | 웹 페이지 스타일 / 콘텐츠·경로·인용 — CSS가 한 열 콘텐츠 영역과 본문 여백을 정한다(78–98). CSS가 링크, 경로 탐색(breadcrumb), 활성 메뉴, 인용문과 다른 콘텐츠 영역의 표시를 정한다(99–142). |
| 143–200 | 웹 페이지 스타일 / 주 메뉴·하위 메뉴 — CSS가 주 메뉴의 배치와 목록 항목의 구분 배경을 정한다(143–167). CSS가 메뉴 링크와 하위 메뉴의 위치, 너비, 표시를 정한다(168–200). |
| 201–231 | 웹 페이지 스타일 / 메뉴 상태·그림 크기 — CSS가 마우스를 올렸을 때 하위 메뉴를 표시한다(201–212). CSS가 현재 페이지 메뉴의 색과 메뉴 글꼴을 정한다(213–228). 자동 크기 이미지의 표시 크기를 정하는 CSS와 빈 줄을 포함한다(229–231). |
| 232–241 | 페이지 제목·구조화 메타데이터(structured metadata) — 제목은 모델 격자(model grid)의 모든 절점(node)에서 기록한 3차원 유속(velocity) 출력 파일 fort.45이다(232). JSON-LD가 페이지 주소, 제목, 게시·수정 시각, 경로 탐색과 사이트 검색 정보를 담는다(237). 빈 줄을 포함한다(233–241). |
| 242–270 | WordPress 표시 코드 — 이모지(emoji) 표시 지원을 검사하는 설정과 JavaScript를 포함한다(242–246). CSS가 이모지, 버튼, 파일 링크, 색, 글꼴, 간격, 그림자와 블록 레이아웃을 정한다(249–269). 빈 줄을 포함한다(247–270). |
| 271–303 | 사이트 관리·분석·배경 — 관리자 지원 표시의 배경색을 정한다(286–288). 방문 분석 코드를 포함한다(292–298). 웹 페이지 배경 그림의 주소와 배치를 정한다(300). 나머지 행은 빈 줄이다(271–303). |
| 304–358 | 사이트 머리말·문서 메뉴 — ADCIRC 공식 사이트 제목과 탐색 건너뛰기 링크를 포함한다(304–310). 커뮤니티, 개발자, 사용자 메뉴를 포함한다(312–322). 문서 메뉴가 v50부터 v53까지의 사용자 설명서, 컴파일·명령행 옵션, 예제, 보고서와 출판물로 연결된다(323–358). |
| 359–401 | 관련 소프트웨어·소식·제품 메뉴 — 관련 소프트웨어 링크를 포함한다(359–361). 사용자 모임, 발표, 단체 사진, 워크숍과 허리케인 관련 소식 링크를 포함한다(362–393). 제품과 ASGS 링크 및 마지막 빈 줄을 포함한다(394–401). |
| 402–411 | 3D Velocity at All Nodes in the Model Grid (fort.45) / 개요 — 경로 탐색과 본문 제목을 포함한다(402–404). 문서는 fort.15에서 정한 모델 격자 모든 절점의 유속 시계열(time series) 출력을 설명한다(406). 굵은 변수명 한 줄이 실제 출력 한 줄을 나타낸다(408). 예시의 빈 줄은 가독성을 위한 줄이다(408). 반복문(loop)은 여러 출력 줄을 나타낸다(408). 변수 정의는 링크로 제공한다(408). 출력 형식 원문: `Output will be in ascii format.` (410). |
| 412–428 | fort.45 / 파일 구조 — 첫 출력 줄은 `RUNDES`, `RUNID`, `AGRID`이다(412). 다음 줄은 헤더 변수 목록이다(414). `k` 반복 범위는 `NDSET3DGV`이다(416). `k` 반복문 안에 `TIME`, `IT`와 `SIGMA` 목록을 제시한다(418). `j` 반복 범위는 `NP`이다(420). 절점별 출력 줄은 `J`와 `REAL(Q(j,M))`, `AIMAG(Q(j,M))`, `WZ(j,M)` 목록이다(422). 반복문 종료와 빈 줄을 포함한다(423–428). `k` 반복문 종료 문구는 두 행으로 나뉜다(426–427). 출력 형식·반복 범위 원문: `**[RUNDES](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#RUNDES), [RUNID](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#RUNID), [AGRID](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#AGRID)**` (412); `**[NDSET3DGV](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#NDSET3DGV), [NP](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#NP), [DTDP](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#DTDP)\*[NSPO3DGV](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#NSPO3DGV), [NSPO3DGV](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#NSPO3DGV), [NFEN](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#NFEN), [IRTYPE](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#IRTYPE)**` (414); `for k = 1 to **[NDSET3DGV](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#NDSET3DGV)**` (416); `**[TIME](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#TIME), [IT](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#IT), ([SIGMA(N)](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#SIGMA), [SIGMA(N)](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#SIGMA), [SIGMA(N)](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#SIGMA),N=1,[NFEN](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#NFEN)-1), [SIGMA(NFEN)](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#SIGMA), [SIGMA(NFEN)](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#SIGMA)**` (418); `for j = 1 to **[NP](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#NP)**` (420); `**J, ([REAL(Q(j,M))](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#REAL_QGLO), [AIMAG(Q(j,M))](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#AIMAG_QGLO), [WZ(j,M)](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#WZ_GLO), M=1, [NFEN](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#NFEN))**` (422); `end j loop` (424); `end k  ` (426); `loop` (427). |
| 429–443 | 사이트 후행 코드 — 빈 줄과 사이트 유틸리티(utility) 표시 호출을 포함한다(429–431). 링크 미리 가져오기(prefetch) 설정을 포함한다(433). 쿠키 안내문 설정과 표시 상태 갱신 코드를 포함한다(436–442). New Relic 페이지 계측 정보를 포함한다(443). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 418: 출력 형식은 `SIGMA(N)`을 세 번 적고 `SIGMA(NFEN)`을 두 번 적는다.
- 422: 출력 필드 `J`에는 정의 링크가 없다. 이 문서 본문에는 `J`의 별도 정의가 없다.
