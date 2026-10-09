---
file: models/ADCIRC/raw/manuals/website_markdown/home/documentation/users-manual-v50/input-file-descriptions/wave-radiation-stress-forcing-file-fort-23.md
lines: 445
sha256: 91f24ee9e562884aeda55d98bab2412c130f2bf3602a50ccba7ec8ea380f0bc6
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# wave-radiation-stress-forcing-file-fort-23.md — 판독 구간 기록

구간은 1행부터 445행까지 빈틈없이 이어진다.

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
| 403–410 | Wave Radiation Stress Forcing File (fort.23) / 적용 조건 — 탐색 경로와 절 제목을 포함한다(403–405). 파랑 복사응력(wave radiation stress)을 단독으로 또는 바람 등 다른 외력(forcing)과 함께 사용할 수 있다고 적는다(407). fort.23을 읽는 NWS 조건과 NWS -4의 기상 입력 형식과 유사하다는 설명을 적는다(407). 굵은 입력 변수명이 입력 자료 한 줄을 나타내며 빈 줄은 가독성을 위한 것이라고 적는다(409). 원문: `Wave radiation stresses can e used by themselves or in concert with other forcing (including winds) to drive ADCIRC. The wave radiation stress input file is read when ABS([NWS](../../parameter-definitions#NWS))>=100 in the [Model Parameter and Periodic Boundary Condition File](../model-parameter-and-periodic-boundary-condition-file-fort-15). The format is similar to the meteorological input file used when [NWS](../../parameter-definitions#NWS) =-4 (i.e. the PBL hurricane model input format following a hot start).` (407); `The basic file structure is shown below. Each line of input data is represented by a line containing the input variable name(s) in bold face type. Blank lines are only to enhance readability. Definitions of each variable are provided via hot links.` (409). |
| 411–420 | 기본 입력 형식 — 노드(node) 번호와 두 복사응력 성분을 입력하는 줄을 제시한다(411). 물음표로 된 줄과 Notes 표제를 포함한다(413–419). 원문: `[**JN**](http://adcirc.org/home/documentation/users-manual-v50/parameter-definitions#JN), [**RSX(JN), RSY(JN)**](../../parameter-definitions#RSX_RSY)` (411); `??????????.` (413); `??????????.` (415); `??????????.` (417). |
| 421–424 | Notes / 입력 노드·시각 — 격자(grid)의 일부 노드에 복사응력을 직접 입력한다고 적는다(421). 초기 기동(cold start)과 재기동(hot start)에 따른 첫 자료 시각을 적는다(423). 추가 자료는 fort.15에 지정된 RSTIMINC 간격마다 제공해야 한다고 적는다(423). ADCIRC 시간 단계(time step)에 맞춰 시간 보간(interpolation)한다고 적는다(423). 원문: `Radiation stresses are input directly to a subset of nodes in the ADCIRC grid (as specified by the node number [JN](../../parameter-definitions#JN)).` (421); `If ADCIRC is cold started, the first set of radiation stress data corresponds to TIME=STATIM. If ADCIRC is hot started, the first set of radiation stress data corresponds to TIME=HOT START TIME. Additional sets of radiation stress data must be provided every [RSTIMINC](../../parameter-definitions#RSTIMINC), where [RSTIMINC](../../parameter-definitions#RSTIMINC) is the radiation stress time interval and is specified in the [Model Parameter and Periodic Boundary Condition File](https://adcirc.org/home/documentation/users-manual-v50/input-file-descriptions/model-parameter-and-periodic-boundary-condition-file-fort-15/). Radiation stresses are interpolated in time to the ADCIRC time step.` (423). |
| 425–426 | Notes / 고정 형식·시간 구분 — 각 자료 줄의 고정 형식(fixed format), 노드별 반복, 다음 시각을 구분하는 기호의 열 위치를 적는다(425). 각 새 시각에 입력되지 않은 노드는 파랑 복사응력이 영이라고 가정한다(425). 원문: `Each data line must have the format I8, 2E13.5.Data input lines are repeated for as many nodes as desired. A line containing the # symbol in column 2 indicates radiation stress data at the next time increment begins on the following line. At each new time, any node that is not specified in the input file is assumed to have zero wave radiation stress.` (425). |
| 427–430 | Notes / 단위·자료 제공 의무 — 복사응력은 중력 단위와 일치하는 속도 제곱(velocity squared) 단위로 입력해야 한다고 적는다(427). 힘/면적(force/area) 단위의 응력을 물의 기준 밀도(reference density)로 나누어 얻는다고 적는다(427). 전체 실행 기간의 자료를 제공해야 하며 그렇지 않으면 실행이 중단된다고 적는다(429). 원문: `Wave radiation stress must be input in units of velocity squared (consistent with the units of gravity). Stress in these units is obtained by dividing stress in units of force/area by the reference density of water.` (427); `Data must be provided for the entire model run, otherwise the run will crash!` (429). |
| 431–445 | 웹 후미 스크립트 — 빈 줄, 유틸리티(utility) 표시 호출, 링크 사전 읽기(prefetch) 규칙, 쿠키(cookie) 안내 설정, jQuery와 New Relic 정보를 포함한다(431–445). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 413–417: 반복 표시가 `??????????.`이며 이 기호의 뜻을 이 파일에서 설명하지 않는다.
