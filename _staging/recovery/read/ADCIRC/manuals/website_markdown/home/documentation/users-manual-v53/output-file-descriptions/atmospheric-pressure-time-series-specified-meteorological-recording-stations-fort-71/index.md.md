---
file: models/ADCIRC/raw/manuals/website_markdown/home/documentation/users-manual-v53/output-file-descriptions/atmospheric-pressure-time-series-specified-meteorological-recording-stations-fort-71/index.md
lines: 442
sha256: 98dbf1a1df7c33f5c4cb129c80d1474d2465fdf26489ec405969a31dccbd0760
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
| 232–241 | 페이지 제목·메타데이터(metadata) — 제목은 지정 기상 관측점(meteorological recording stations)의 대기압(atmospheric pressure) 시계열(time series) 출력 파일 fort.71을 가리킨다(232). JSON-LD가 페이지 URL, 제목, 게시·수정 시각, 설명, 경로 탐색과 사이트 검색 항목을 담는다(237). 나머지 행은 빈 줄이다(233–241). |
| 242–270 | WordPress 표시 코드 — 이모지(emoji) 표시 지원을 검사하는 설정과 JavaScript를 포함한다(242–246). CSS가 이모지, 버튼, 파일 링크, 색, 글꼴, 간격, 그림자와 블록 레이아웃을 정한다(249–269). 빈 줄을 포함한다(247–270). |
| 271–303 | 사이트 관리·분석·배경 — 관리자 지원 표시의 배경색을 정한다(286–288). 방문 분석 코드를 포함한다(292–298). 웹 페이지 배경 그림의 주소와 배치를 정한다(300). 나머지 행은 빈 줄이다(271–303). |
| 304–358 | 사이트 머리말·문서 메뉴 — ADCIRC 공식 사이트 제목과 탐색 건너뛰기 링크를 포함한다(304–310). 커뮤니티, 개발자, 사용자 메뉴를 포함한다(312–322). 문서 메뉴가 v50부터 v53까지의 사용자 설명서, 컴파일·명령행 옵션, 예제, 보고서와 출판물로 연결된다(323–358). |
| 359–401 | 관련 소프트웨어·소식·제품 메뉴 — 관련 소프트웨어 링크를 포함한다(359–361). 사용자 모임, 발표, 단체 사진, 워크숍과 허리케인 관련 소식 링크를 포함한다(362–393). 제품과 ASGS 링크 및 마지막 빈 줄을 포함한다(394–401). |
| 402–411 | 본문 / fort.71 설명·출력 형식 — 경로 탐색과 본문 제목을 포함한다(402–404). fort.15에서 지정한 기상 관측점의 대기압 시계열 출력이다(406). 출력 구조에서 굵은 변수 이름이 있는 한 줄은 출력 한 줄을 나타낸다(408). 빈 줄은 가독성을 높이기 위한 것이다(408). 반복문(loop)은 여러 출력 줄을 나타낸다(408). 변수 정의는 링크로 제공한다고 설명한다(408). ASCII(ascii) 또는 이진(binary) 형식은 fort.15의 `NOUTM` 설정에 달려 있다(410). 적용 조건 원문: `Output may be in ascii or binary format depending on how [NOUTM](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#NOUTM) is set in the [Model Parameter and Periodic Boundary Condition File](https://adcirc.org/home/documentation/users-manual-v53/input-file-descriptions/model-parameter-and-periodic-boundary-condition-file-fort-15)` (410). |
| 412–423 | 본문 / 헤더(header)·관측점별 기록 — 첫 출력 줄은 `RUNDES`, `RUNID`, `AGRID`이다(412). 다음 줄은 `NTRSPM`, `NSTAM`, `DTDP`와 `NSPOOLM`의 곱, `NSPOOLM`, `IRTYPE`이다(414). `TIME`, `IT` 줄 다음에 `k=1`부터 `NSTAM`까지 반복한다(416–418). 각 반복의 출력 줄은 `k`, `RMP00(k)`이다(420). 반복은 422행에서 끝난다. 파일 구조 원문: `[**RUNDES**](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#RUNDES), [**RUNID**](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#RUNID), [**AGRID**](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#AGRID)` (412); `[**NTRSPM**](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#NTRSPM), [**NSTAM**](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#NSTAM), [**DTDP**](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#DTDP)\*[**NSPOOLM**](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#NSPOOLM), [**NSPOOLM**](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#NSPOOLM), [**IRTYPE**](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#IRTYPE)` (414); `[**TIME**](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#TIME), [**IT**](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#IT)` (416); `for k=1, [**NSTAM**](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#NSTAM)` (418); `**k**, [**RMP00(k)**](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#RMP00)` (420); `end k loop` (422). |
| 424–427 | 본문 / Note·이진 출력 조건 — 이진 출력이 지정되면 관측점 번호 `k`를 출력에 포함하지 않는다(426). 적용 조건 원문: `If binary output is specified, the station number (k) is not included in the output.` (426). |
| 428–442 | 사이트 끝부분 — 유틸리티 표시 호출을 포함한다(430). 사전 가져오기(prefetch) 설정을 포함한다(432). 쿠키 안내(cookie banner)의 문구와 수락 버튼 설정을 포함한다(435–437). jQuery 표시 처리와 New Relic 페이지 계측 정보를 포함한다(441–442). 빈 줄도 포함한다(428–442). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 헤더에는 `NTRSPM`이 있다(414). 표시된 구조에서 명시한 반복문은 `for k=1, [**NSTAM**](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#NSTAM)` (418)부터 `end k loop` (422)까지이다. 여러 시각의 기록을 반복하는 별도 반복문은 본문 구조에 적혀 있지 않다(412–422).
