---
file: models/ADCIRC/raw/manuals/website_markdown/home/documentation/users-manual-v53/output-file-descriptions/atmospheric-pressure-time-series-nodes-model-grid-fort-73/index.md
lines: 442
sha256: 565b7d43ad7d4283263a75cf95903c2e6b03364b7ee0d9e6d3df81d6e2c32033
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# index.md — 판독 구간 기록

구간은 1행부터 442행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–12 | 웹 페이지 선행 코드 — New Relic 브라우저 계측(browser instrumentation) 설정과 축약 JavaScript를 포함한다(1–2). 빈 줄을 포함한다(3–12). |
| 13–77 | 웹 페이지 스타일 / 검색·제목·레이아웃 — CSS가 검색 입력과 버튼의 크기를 정한다(13–25). CSS가 링크 색, 글꼴, 제목과 페이지 컨테이너(container), 오른쪽 콘텐츠 영역의 배치를 정한다(26–77). |
| 78–142 | 웹 페이지 스타일 / 콘텐츠·경로·인용 — CSS가 한 열 콘텐츠 영역과 본문 여백을 정한다(78–98). CSS가 링크, 경로 탐색(breadcrumb), 활성 메뉴, 인용문과 다른 콘텐츠 영역의 표시를 정한다(99–142). |
| 143–200 | 웹 페이지 스타일 / 주 메뉴·하위 메뉴 — CSS가 주 메뉴의 배치와 목록 항목의 구분 배경을 정한다(143–167). CSS가 메뉴 링크와 하위 메뉴의 위치, 너비, 표시를 정한다(168–200). |
| 201–231 | 웹 페이지 스타일 / 메뉴 상태·그림 크기 — CSS가 마우스를 올렸을 때 하위 메뉴를 표시한다(201–212). CSS가 현재 페이지 메뉴의 색과 메뉴 글꼴을 정한다(213–228). 자동 크기 이미지의 표시 크기를 정하는 CSS와 빈 줄을 포함한다(229–231). |
| 232–241 | 페이지 제목·구조화 메타데이터(structured metadata) — 제목은 모델 격자(model grid)의 모든 절점(node)에서 기록한 대기압(atmospheric pressure) 시계열(time series) 출력 파일 fort.73이다(232). JSON-LD가 페이지 주소, 제목, 게시·수정 시각, 경로 탐색과 사이트 검색 정보를 담는다(237). 빈 줄을 포함한다(233–241). |
| 242–270 | WordPress 표시 코드 — 이모지(emoji) 표시 지원을 검사하는 설정과 JavaScript를 포함한다(242–246). CSS가 이모지, 버튼, 파일 링크, 색, 글꼴, 간격, 그림자와 블록 레이아웃을 정한다(249–269). 빈 줄을 포함한다(247–270). |
| 271–303 | 사이트 관리·분석·배경 — 관리자 지원 표시의 배경색을 정한다(286–288). 방문 분석 코드를 포함한다(292–298). 웹 페이지 배경 그림의 주소와 배치를 정한다(300). 나머지 행은 빈 줄이다(271–303). |
| 304–358 | 사이트 머리말·문서 메뉴 — ADCIRC 공식 사이트 제목과 탐색 건너뛰기 링크를 포함한다(304–310). 커뮤니티, 개발자, 사용자 메뉴를 포함한다(312–322). 문서 메뉴가 v50부터 v53까지의 사용자 설명서, 컴파일·명령행 옵션, 예제, 보고서와 출판물로 연결된다(323–358). |
| 359–401 | 관련 소프트웨어·소식·제품 메뉴 — 관련 소프트웨어 링크를 포함한다(359–361). 사용자 모임, 발표, 단체 사진, 워크숍과 허리케인 관련 소식 링크를 포함한다(362–393). 제품과 ASGS 링크 및 마지막 빈 줄을 포함한다(394–401). |
| 402–411 | Atmospheric Pressure Time Series at All Nodes in the Model Grid (fort.73) / 개요 — 경로 탐색과 본문 제목을 포함한다(402–404). 문서는 fort.15에서 정한 모델 격자 모든 절점의 대기압 시계열 출력을 설명한다(406). 단위 표기는 `m of water`이다(406). 굵은 변수명 한 줄이 실제 출력 한 줄을 나타낸다(408). 예시의 빈 줄은 가독성을 위한 줄이다(408). 반복문(loop)은 여러 출력 줄을 나타낸다(408). 변수 정의는 링크로 제공한다(408). fort.15의 NOUTGW 설정에 따라 ASCII 또는 이진(binary) 형식으로 출력할 수 있다(410). 단위·적용 조건 원문: `Atmospheric pressure (m of water) time series output at all nodes in the model grid as specified in the [Model Parameter and Periodic Boundary Condition File](https://adcirc.org/home/documentation/users-manual-v53/input-file-descriptions/model-parameter-and-periodic-boundary-condition-file-fort-15).` (406); `Output may be in ascii or binary format depending on how [NOUTGW](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#NOUTGW) is set in the [Model Parameter and Periodic Boundary Condition File](https://adcirc.org/home/documentation/users-manual-v53/input-file-descriptions/model-parameter-and-periodic-boundary-condition-file-fort-15)` (410). |
| 412–423 | fort.73 / 파일 구조 — 첫 출력 줄은 `RUNDES`, `RUNID`, `AGRID`이다(412). 다음 줄은 `NDSETSW`, `NP`, `DTDP`와 `NSPOOLGW`의 곱, `NSPOOLGW`, `IRTYPE`이다(414). `TIME`, `IT` 줄 다음에 `k=1`부터 `NP`까지 반복한다(416–418). 절점별 출력 줄은 `k`, `PR2(k)`이다(420). 반복문 종료와 빈 줄을 포함한다(421–423). 출력 형식·반복 범위 원문: `[**RUNDES**](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#RUNDES), [**RUNID**](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#RUNID), [**AGRID**](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#AGRID)` (412); `[**NDSETSW**](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#NDSETSW), [**NP**](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#NP), **[DTDP](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#DTDP)\***[**NSPOOLGW**](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#NSPOOLGW), [**NSPOOLGW**](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#NSPOOLGW), [**IRTYPE**](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#IRTYPE)` (414); `[**TIME**](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#TIME), [**IT**](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#IT)` (416); `for k=1, [**NP**](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#NP)` (418); `**k**, [**PR2(k)**](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#PR2)` (420); `end k loop` (422). |
| 424–427 | fort.73 / Note — 이진 출력을 지정하면 관측점 번호(station number) k를 출력에 포함하지 않는다고 적는다(426). 제목, 빈 줄과 적용 조건 원문을 포함한다(424–427): `If binary output is specified, the station number (k) is not included in the output.` (426). |
| 428–442 | 사이트 후행 코드 — 빈 줄과 사이트 유틸리티(utility) 표시 호출을 포함한다(428–430). 링크 미리 가져오기(prefetch) 설정을 포함한다(432). 쿠키 안내문 설정과 표시 상태 갱신 코드를 포함한다(435–441). New Relic 페이지 계측 정보를 포함한다(442). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 404·406·426: 제목과 개요는 모델 격자의 모든 절점 출력을 설명한다. 426행의 주석은 출력에서 생략하는 `k`를 `the station number (k)`라고 부른다.
- 414·416–422: 머리말에는 `NDSETSW`가 있다. 파일 구조의 명시적 반복문은 `NP`를 범위로 사용하는 절점 반복문 하나이다. 이 구간은 여러 시각의 자료를 반복하는 별도 문구를 제시하지 않는다.
