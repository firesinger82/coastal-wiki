---
file: models/ADCIRC/raw/manuals/website_markdown/home/documentation/users-manual-v53/output-file-descriptions/ice-coverage-fields-at-specified-recording-stations-fort-91/index.md
lines: 438
sha256: c9b25d666abf7a35a1b94b5105127d058ee871a5e1c449fcd8ebfad6b6263915
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# index.md — 판독 구간 기록

구간은 1행부터 438행까지 빈틈없이 이어진다.

| 구간 | 내용 |
| --- | --- |
| 1–12 | 문서 앞 웹 계측 스크립트 — New Relic 초기 설정과 압축된 브라우저 계측(instrumentation) JavaScript가 들어 있다(1–2). 뒤에는 빈 줄이 이어진다(3–12). |
| 13–70 | 사이트 스타일시트(Cascading Style Sheets, CSS) / 검색창·제목·기본 배치 — 검색창과 검색 버튼, 링크와 페이지 제목, 본문 글꼴·색상, 전체 컨테이너(container)와 헤더(header)의 배치를 정한다(13–65). 태그 표시 영역의 스타일도 포함한다(66–70). |
| 71–135 | 사이트 CSS / 본문·링크·경로 표시 — 본문 영역의 배치와 문단·링크 스타일을 정한다(71–114). 경로 표시(breadcrumbs), 활성 탐색 링크, 인용문과 소제목 스타일을 정한다(115–135). |
| 136–200 | 사이트 CSS / 열 배치·탐색 메뉴 — 본문 열과 탐색 영역의 배치를 정한다(136–150). 메뉴 목록과 하위 메뉴의 위치·색상·크기를 정한다(151–200). |
| 201–231 | 사이트 CSS / 메뉴 상태·이미지 크기 — 마우스를 올린 메뉴와 현재 페이지 메뉴의 표시 규칙이 들어 있다(201–225). 콘텐츠 표시 영역, 메뉴 글꼴, 태그 숨김과 이미지의 내재 크기(intrinsic size) 설정을 포함한다(226–231). |
| 232–241 | 페이지 메타데이터 — 페이지 제목이 들어 있다(232). JSON-LD에 이 페이지의 URL·제목·게시 시각과 상위 페이지 경로, 사이트 검색 정보를 담는다(237). 나머지는 빈 줄이다(233–236·238–241). |
| 242–270 | WordPress 스크립트·CSS — 이모지(emoji) 지원 설정과 브라우저 지원 검사 스크립트가 들어 있다(242–246). 이모지 표시, 블록(block) 버튼, 색상·글꼴·간격·배치의 공통 CSS를 포함한다(249–269). 빈 줄도 포함한다. |
| 271–303 | 사이트 설정 / 관리자 표시·방문 계측·배경 — 관리자 지원 표시 스타일이 들어 있다(286–288). 방문 계측 설정이 들어 있다(292–298). 사이트 배경 이미지의 반복 표시 CSS가 들어 있다(300). 주변 빈 줄도 포함한다. |
| 304–358 | 사이트 탐색 / Community·Documentation — 빈 제목 마크업과 ADCIRC 사이트 제목, 탐색 건너뛰기 링크가 들어 있다(304–310). 커뮤니티·개발 기관과 사용자 안내가 들어 있다(312–322). 매뉴얼 판본, 컴파일·실행 옵션, FAQ, 예제, 개발·이론 보고서와 출판물 링크를 나열한다(323–358). |
| 359–401 | 사이트 탐색 / Related software·News·Products·ASGS — 유틸리티와 격자 생성 도구를 연결한다(359–361). 사용자 모임·워크숍·사진·발표자료·폭풍해일 예보 링크를 나열한다(362–393). 조석 데이터베이스·출판물·격자·예보 제품과 ASGS 링크를 나열한다(394–400). 끝의 빈 줄도 포함한다(401). |
| 402–407 | Ice Coverage Fields at Specified Recording Stations (fort.91) / 생성 조건 — 상위 경로와 본문 제목이 들어 있다(402–404). 얼음 피복(ice coverage) 입력 기능을 활성화했다면 fort.15에 지정한 기상 기록 관측점(meteorological recording stations)의 출력 제어에 따라 fort.91을 생성한다고 적는다(406). 적용 조건과 설정 원문: `If the ice coverage input feature of ADCIRC has been activated, the fort.91 output file will be produced according to the output control specifications for specified meteorological recording stations ([NOUTM](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#NOUTM), etc) as specified in the [Model Parameter and Periodic Boundary Condition File](https://adcirc.org/home/documentation/users-manual-v53/input-file-descriptions/model-parameter-and-periodic-boundary-condition-file-fort-15).` (406). |
| 408–415 | fort.91 / 파일 구조·형식·헤더 — 굵은 변수 이름의 각 줄이 출력 한 줄을 나타낸다고 설명한다(408). 빈 줄은 가독성을 위한 것이며 반복은 여러 출력 줄을 나타낸다고 설명한다(408). 변수 정의는 링크로 제공한다고 적는다(408). fort.15의 설정에 따라 ASCII 또는 이진 형식(binary format)으로 출력할 수 있다고 적는다(410). 실행·격자 식별자와 데이터셋·관측점 수, 출력 간격의 곱셈식과 헤더 변수 순서를 제시한다(412–414). 조건·형식 원문: `Output may be in ascii or binary format depending on how [NOUTM](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#NOUTM) is set in the [Model Parameter and Periodic Boundary Condition File](https://adcirc.org/home/documentation/users-manual-v53/input-file-descriptions/model-parameter-and-periodic-boundary-condition-file-fort-15)` (410). 헤더·곱셈식 원문: `[**RUNDES**](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#RUNDES), [**RUNID**](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#RUNID), [**AGRID**](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#AGRID)` (412); `[**NDSET**](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#NDSET), [**NSTAM**](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#NSTAM), [**DTDP**](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#DTDP)\*[**NSPOOLM**](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#NSPOOLM), [**NSPOOLM**](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#NSPOOLM), [**IRTYPE**](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#IRTYPE)` (414). |
| 416–423 | fort.91 / 시각·관측점별 얼음 피복 — 시각과 시간 단계(time step) 변수 뒤 지정 기상 관측점에 대한 반복문을 제시한다(416–422). 관측점 첨자와 얼음 피복 변수의 출력 순서를 제시한다(420). 원문: `[**TIME**](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#TIME), [**IT**](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#IT)` (416); `for k=1, [**NSTAM**](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#NSTAM)` (418); `**k**, [**RMICE00(k)**](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#RMICE00)` (420); `end k loop` (422). 빈 줄도 포함한다. |
| 424–438 | 페이지 말미 웹 설정 — 빈 줄과 유틸리티 표시 호출이 들어 있다(424–426). 링크 사전 가져오기(prefetch) 규칙이 들어 있다(428). 쿠키 안내문 설정이 들어 있다(431–433). jQuery 표시 클래스 변경과 New Relic 계측 메타데이터가 들어 있다(437–438). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

없음
