---
file: models/ADCIRC/raw/manuals/website_markdown/home/documentation/users-manual-v52/output-file-descriptions/wind-stress-velocity-time-series-nodes-model-grid-fort-74.md
lines: 442
sha256: 84c581173608be716657cb8ff7b8e0d3a3bb7c4c7f1a78c18a7ee0f935daa328
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# wind-stress-velocity-time-series-nodes-model-grid-fort-74.md — 판독 구간 기록

구간은 1행부터 442행까지 빈틈없이 이어진다.
한국어 설명은 AI 판독 기록이다. “원문” 뒤의 백틱은 해당 행의 원문 인용이다. “그림 판독”은 직접 확인한 로컬 그림의 내용이다.

| 구간 | 내용 |
|---|---|
| 1–12 | 웹사이트 초기 스크립트 — New Relic 초기화 설정과 로더 JavaScript가 들어 있다(1–2). 뒤 빈 줄도 이 구간에 포함한다(3–12). |
| 13–77 | 웹사이트 CSS / 검색·제목·배치 — 검색 입력과 버튼, 링크와 본문, 헤더(header), 컨테이너(container), 오른쪽 콘텐츠 영역의 표시 규칙을 적는다(13–77). |
| 78–141 | 웹사이트 CSS / 본문·탐색 경로 — 단일 열 콘텐츠와 본문 문단, 링크, 탐색 경로(breadcrumb), 인용문과 제목의 표시 규칙을 적는다(78–141). |
| 142–200 | 웹사이트 CSS / 메뉴 — 주 메뉴와 하위 메뉴의 배치, 색상, 크기 및 배경 이미지 경로를 적는다(142–200). |
| 201–230 | 웹사이트 CSS / 메뉴 상태·이미지 크기 — 메뉴를 가리켰을 때와 현재 페이지의 표시 규칙을 적는다(201–225). 슬라이드 영역과 태그 표시, 이미지의 내재 크기 규칙도 포함한다(226–230). |
| 231–241 | 페이지 제목·구조화 메타데이터(metadata) — 페이지 제목을 적는다(232). JSON-LD에는 해당 문서의 URL, 게시·수정 시각, 탐색 경로와 사이트 검색 정의가 들어 있다(237). 빈 줄도 포함한다(231·233–236·238–241). |
| 242–270 | WordPress 표시 보조 코드 — 이모지(emoji) 설정과 지원 판별 스크립트를 적는다(242–246). 이모지와 블록의 CSS, 색상·글꼴·간격 등 표시 사전 설정도 들어 있다(249–269). |
| 271–303 | 웹사이트 관리·접속 통계·배경 — 빈 줄과 관리 표시 CSS를 포함한다(271–291). 접속 통계 초기화와 페이지 배경의 표시 규칙을 적는다(292–300). |
| 304–358 | 사이트 머리말·문서 메뉴 — 빈 제목 마크업(markup)과 사이트 명칭, 탐색 건너뛰기 링크를 포함한다(304–310). 커뮤니티, 개발자, 사용자, 판본별 매뉴얼, 컴파일·실행 옵션, 보고서 및 특수 기능의 메뉴 링크를 적는다(312–358). |
| 359–403 | 관련 소프트웨어·행사·제품 메뉴와 문서 위치 — 관련 소프트웨어와 행사·사진 링크를 나열한다(359–393). 제품과 ASGS 메뉴가 이어진다(394–400). 현재 문서의 탐색 경로를 적는다(402). 빈 줄도 포함한다(401·403). |
| 404–411 | Wind Stress or Velocity Time Series at All Nodes in the Model Grid (fort.74) / 출력 대상·형식 — 모형 격자(model grid)의 모든 절점(node)에 대한 풍속(wind velocity) 또는 바람 응력(wind stress) 시계열을 설명한다(404–406). 파일 구조에서 굵은 변수 이름 한 줄이 출력 한 줄을 나타내며, 반복문은 여러 출력 줄을 뜻한다고 적는다(408). ASCII 또는 바이너리(binary) 출력의 선택은 `NOUTGW` 설정에 따른다(410).<br>원문: `# Wind Stress or Velocity Time Series at All Nodes in the Model Grid (fort.74)` (404).<br>원문: `Wind velocity or stress time series output at all nodes in the model grid as specified in the [Model Parameter and Periodic Boundary Condition File](../../input-file-descriptions/model-parameter-and-periodic-boundary-condition-file-fort-15).` (406).<br>원문: `The basic file structure is shown below. Each line of output is represented by a line containing the output variable name(s) in bold face type. Blank lines are to enhance readability. Loops indicate multiple lines of output. Definitions of each variable are provided via hot links.` (408).<br>원문: `Output may be in ascii or binary format depending on how [NOUTGW](https://adcirc.org/home/documentation/users-manual-v52/parameter-definitions#NOUTGW) is set in the [Model Parameter and Periodic Boundary Condition File](../../input-file-descriptions/model-parameter-and-periodic-boundary-condition-file-fort-15)` (410). |
| 412–423 | fort.74 / 파일 구조 — 실행·격자 식별자, 자료 세트 수와 절점 수, 출력 시간 간격과 레코드 종류(record type), 모형 시각과 계산 단계 번호를 순서대로 제시한다(412–416). 절점별 풍속 또는 바람 응력의 두 성분을 반복 출력하는 형식도 적는다(418–422). 원문의 곱셈 표현과 변수 이름을 그대로 옮긴다(414·420).<br>원문: `[**RUNDES**](https://adcirc.org/home/documentation/users-manual-v52/parameter-definitions#RUNDES), [**RUNID**](https://adcirc.org/home/documentation/users-manual-v52/parameter-definitions#RUNID), [**AGRID**](https://adcirc.org/home/documentation/users-manual-v52/parameter-definitions#AGRID)` (412).<br>원문: `[**NDSETSW**](https://adcirc.org/home/documentation/users-manual-v52/parameter-definitions#NDSETSW), [**NP**](https://adcirc.org/home/documentation/users-manual-v52/parameter-definitions#NP), **[DTDP](https://adcirc.org/home/documentation/users-manual-v52/parameter-definitions#DTDP)\***[**NSPOOLGW**](https://adcirc.org/home/documentation/users-manual-v52/parameter-definitions#NSPOOLGW), [**NSPOOLGW**](https://adcirc.org/home/documentation/users-manual-v52/parameter-definitions#NSPOOLGW), [**IRTYPE**](https://adcirc.org/home/documentation/users-manual-v52/parameter-definitions#IRTYPE)` (414).<br>원문: `[**TIME**](https://adcirc.org/home/documentation/users-manual-v52/parameter-definitions#TIME), [**IT**](https://adcirc.org/home/documentation/users-manual-v52/parameter-definitions#IT)` (416).<br>원문: `for k=1, [**NP**](https://adcirc.org/home/documentation/users-manual-v52/parameter-definitions#NP)` (418).<br>원문: `**k**, [**WVNXOUT(k), WVNYOUT(k)**](https://adcirc.org/home/documentation/users-manual-v52/parameter-definitions#WVNXOUT_WVNYOUT)` (420).<br>원문: `end k loop` (422). |
| 424–429 | fort.74 / 바이너리 출력 주의 — 바이너리 출력을 지정하면 번호 `k`를 출력에 포함하지 않는다고 적는다(424–426). 뒤 빈 줄도 포함한다(427–429).<br>원문: `**Note:**` (424).<br>원문: `If binary output is specified, the station number (k) is not included in the output.` (426). |
| 430–442 | 웹사이트 꼬리 스크립트 — 유틸리티 호출, 링크 사전 가져오기(prefetch) 설정, 쿠키 안내, 슬라이드 표시 클래스 변경과 New Relic 실행 정보를 적는다(430–442). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 418·426행: 반복문은 `for k=1, NP`로 모든 격자 절점의 번호를 사용한다. 바이너리 출력 주의 문장은 같은 `k`를 `station number (k)`라고 부른다.
