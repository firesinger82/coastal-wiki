---
file: models/ADCIRC/raw/manuals/website_markdown/home/documentation/users-manual-v51/output-file-descriptions/wind-stress-or-velocity-time-series-at-all-nodes-in-the-model-grid-fort-74.md
lines: 430
sha256: 20e2eb8c564c5ebffa1250471b0173b0c56a46c0e8f4316fa125fcfdc1c0eaed
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# wind-stress-or-velocity-time-series-at-all-nodes-in-the-model-grid-fort-74.md — 판독 구간 기록

구간은 1행부터 430행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–65 | 웹페이지 스타일(CSS) — 검색 입력·버튼, 제목, 본문 글꼴, 컨테이너, 헤더 및 오른쪽 콘텐츠 영역의 표시 규칙이다(1–65). 모델 매개변수 정의는 없다. |
| 66–130 | 웹페이지 스타일(CSS) — 단일 열 콘텐츠, 본문·링크, 경로 표시, 활성 메뉴, 인용문 및 양쪽 열 콘텐츠 영역의 표시 규칙이다(66–130). |
| 131–164 | 웹페이지 스타일(CSS) — 탐색 메뉴의 폭, 목록, 구분 배경 및 링크 표시 규칙이다(131–164). `images/primary\_nav\_divider.gif`는 메뉴 구분 배경 참조이다(154). 해당 상대 경로의 그림 파일 없음. |
| 165–218 | 웹페이지 스타일(CSS) — 하위 메뉴 위치·폭, 마우스 올림 및 현재 메뉴 표시 규칙이다(165–213). 슬라이드 영역·메뉴 글꼴·태그 숨김·자동 이미지 크기 규칙을 포함한다(214–218). `images/primary\_nav\_bg\_repeat\_on.gif`는 메뉴 배경 참조이다(190). 해당 상대 경로의 그림 파일 없음. |
| 219–230 | 페이지 제목·구조화 메타데이터(JSON-LD) — fort.74 페이지 제목, 원문 주소, 공개 시각 `2015-03-27T15:23:21+00:00`, 탐색 경로 및 사이트 검색 정의를 포함한다(220·225). 빈 줄을 포함한다(219–230). |
| 231–249 | 이모지 지원 스크립트·스타일 — WordPress의 이모지 지원 검사, 캐시·워커·스크립트 로딩 및 이모지 표시 규칙이다(231–248). 빈 줄을 포함한다(249). |
| 250–274 | WordPress 자동 생성 스타일 — 버튼, 파일 버튼, 화면 비율·색·색상 변화·글꼴·간격·그림자 사전 설정 및 배치 규칙이다(251–258). 뒤의 빈 줄을 포함한다(259–274). |
| 275–300 | 관리 표시·통계·사이트 머리말 — 관리 표시 배경색, 방문 통계 초기화 및 사용자 지정 배경을 포함한다(275–289). 사이트 제목·설명·탐색 건너뛰기 링크를 포함한다(293–299). 배경 참조 `https://adcirc.org/wp-content/uploads/sites/2255/2013/03/grid\_bkgrd\_lt\_grey1.jpg`의 로컬 그림 파일 없음(289). |
| 301–337 | 사이트 탐색 / Community·Documentation — 개발자·사용자, V50·V51·v52·v53 매뉴얼, 컴파일·명령행 옵션, FAQ 및 SWAN+ADCIRC 링크 목록이다(301–337). 각 링크 대상의 내용은 이 구간에 없다. |
| 338–389 | 사이트 탐색 / 예제·문헌·소프트웨어·소식·Products·ASGS — 예제, 보고서, 유틸리티, 모임, 조석 데이터베이스 및 제품 링크 목록이다(338–389). 모임 사진 링크는 357·359·363·364·376·378행에 있다. 이 사진 링크들의 로컬 그림 파일 없음. |
| 390–398 | fort.74 / 제목·출력 개요 — 경로 표시와 제목을 포함한다(391–393). 모델 격자(grid)의 모든 절점(node)에서 바람 속도(wind velocity) 또는 바람 응력(wind stress)의 시계열(time series)을 출력하며 fort.15에서 지정한다고 설명한다(395). 굵은 변수명 한 줄은 출력 한 줄을 나타내고, 빈 줄은 가독성을 위한 것이며, 반복문은 여러 출력 줄을 뜻한다고 설명한다(397). |
| 399–411 | fort.74 / 출력 형식·변수 순서 — `NOUTGW` 설정에 따라 ASCII 또는 이진(binary) 출력을 선택한다(399). 실행 설명·실행 식별자·격자 식별자, 헤더, 시간 및 `k=1`부터 `NP`까지의 절점 출력 순서를 제시한다(401–411). 원문 출력 형식과 적용 조건: `Output may be in ascii or binary format depending on how [NOUTGW](../../parameter-definitions#NOUTGW) is set in the [Model Parameter and Periodic Boundary Condition File](../../input-file-descriptions/model-parameter-and-periodic-boundary-condition-file-fort-15)` (399); `[**RUNDES**](../../parameter-definitions#RUNDES), [**RUNID**](../../parameter-definitions#RUNID), [**AGRID**](../../parameter-definitions#AGRID)` (401); `[**NDSETSW**](../../parameter-definitions#NDSETSW), [**NP**](../../parameter-definitions#NP), **[DTDP](../../parameter-definitions#DTDP)\***[**NSPOOLGW**](../../parameter-definitions#NSPOOLGW), [**NSPOOLGW**](../../parameter-definitions#NSPOOLGW), [**IRTYPE**](../../parameter-definitions#IRTYPE)` (403); `[**TIME**](../../parameter-definitions#TIME), [**IT**](../../parameter-definitions#IT)` (405); `for k=1, [**NP**](../../parameter-definitions#NP)` (407); `**k**, [**WVNXOUT(k), WVNYOUT(k)**](../../parameter-definitions#WVNXOUT_WVNYOUT)` (409); `end k loop` (411). |
| 412–430 | fort.74 / 이진 출력 주의·페이지 스크립트 — 이진 출력을 지정하면 `k`를 출력에 포함하지 않는다고 적는다(415). 유틸리티 표시, 미리 가져오기, 쿠키 알림 설정 및 슬라이드 요소 초기화를 포함한다(419–430). 원문 조건: `If binary output is specified, the station number (k) is not included in the output.` (415). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 154·190·289행: 메뉴 배경 두 개와 페이지 배경 한 개를 참조한다. 지정 상대 경로와 로컬 website_markdown 파일 목록에서 해당 그림 파일을 찾지 못했다. 그림 파일 없음.
- 357·359·363·364·376·378행: 모임 사진을 일반 링크로 참조한다. 로컬 website_markdown 파일 목록에 해당 사진 파일이 없다. 그림 파일 없음.
- 393·395·407·415행: 제목·개요는 모델 격자의 모든 절점을 대상으로 하고 `k` 반복문의 끝은 `NP`이다. 415행은 같은 `k`를 `the station number (k)`라고 부른다.
