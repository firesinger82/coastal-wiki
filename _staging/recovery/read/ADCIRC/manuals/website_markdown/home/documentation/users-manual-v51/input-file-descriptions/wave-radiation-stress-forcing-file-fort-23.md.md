---
file: models/ADCIRC/raw/manuals/website_markdown/home/documentation/users-manual-v51/input-file-descriptions/wave-radiation-stress-forcing-file-fort-23.md
lines: 447
sha256: e21f1b1b77588df073eddf8145e9080810471753d28573ed6bc1f167e18cc5ee
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# wave-radiation-stress-forcing-file-fort-23.md — 판독 구간 기록

구간은 1행부터 447행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–12 | 웹페이지 계측 스크립트 — New Relic 초기 설정과 압축 JavaScript를 포함한다(1–2). 이후 빈 줄을 포함한다(3–12). |
| 13–77 | 웹페이지 스타일 / 검색·본문·머리말 — CSS가 검색 입력창과 검색 버튼, 본문, 링크, 머리말, 컨테이너, 오른쪽 본문 열을 설정한다(13–77). |
| 78–142 | 웹페이지 스타일 / 한 열 배치·탐색 경로 — CSS가 한 열 본문과 본문 내부 여백, 문단, 링크, 탐색 경로, 활성 탐색 항목, 인용문, 양쪽 열 배치를 설정한다(78–142). |
| 143–200 | 웹페이지 스타일 / 메뉴 — CSS가 기본 메뉴와 중첩 메뉴의 위치, 표시, 색상, 크기를 설정한다(143–200). 배경 장식 이미지의 URL 선언을 포함한다(166). |
| 201–231 | 웹페이지 스타일 / 메뉴 상태 — CSS가 마우스 진입과 현재 메뉴 항목의 표시를 설정한다(201–225). 슬라이드 영역과 머리말 표시, 자동 크기 이미지의 스타일을 포함한다(226–230). 마지막 빈 줄을 포함한다(231). |
| 232–242 | 페이지 제목·구조화 메타데이터 — 제목은 Wave Radiation Stress Forcing File (fort.23)이다(232). JSON-LD가 페이지 URL, 발행·수정 시각, V51 탐색 경로, 사이트 검색을 기술한다(237). 빈 줄을 포함한다(233–236·238–242). |
| 243–286 | WordPress 표시 코드 — 이모지 지원 검사와 로딩 스크립트, 이모지·블록 버튼·색상·글꼴·배치 스타일을 포함한다(243–270). 뒤의 빈 줄을 포함한다(271–286). |
| 287–304 | 웹페이지 관리자 표시·접속 통계·배경 — 관리자 지원 표시용 CSS를 포함한다(287–289). 접속 통계용 beehive 스크립트를 포함한다(293–299). 페이지 배경 이미지의 CSS 선언과 빈 줄을 포함한다(300–304). |
| 305–350 | 사이트 머리말·탐색 메뉴 / Community·Documentation — ADCIRC 사이트 머리말과 탐색 건너뛰기 링크를 포함한다(305–311). 개발자·사용자 메뉴와 V50·V51·v52·v53 매뉴얼, 컴파일·명령행 옵션, FAQ, SWAN 결합, 예제 링크를 나열한다(313–350). |
| 351–402 | 탐색 메뉴 / 문헌·관련 소프트웨어·뉴스·제품 — 보고서와 출판물, 유틸리티, 격자 생성기, 워크숍·행사 자료, 폭풍해일 예보, 조석 데이터베이스, 격자, ASGS 링크를 나열한다(351–401). 마지막 빈 줄을 포함한다(402). |
| 403–408 | Wave Radiation Stress Forcing File (fort.23) / 적용·형식 — 파랑 복사 응력(wave radiation stress)은 단독으로 또는 바람을 포함한 다른 강제력(forcing)과 함께 사용할 수 있다(407). fort.15 선택값의 절댓값에 따른 판독 조건을 설명한다(407). 형식은 재시작(hot start) 후의 PBL 허리케인 기상 입력과 유사하다고 적는다(407). 조건과 비교 대상을 그대로 옮긴다. 원문: `Wave radiation stresses can e used by themselves or in concert with other forcing (including winds) to drive ADCIRC. The wave radiation stress input file is read when ABS([NWS](../../parameter-definitions#NWS))>=100 in the [Model Parameter and Periodic Boundary Condition File](../model-parameter-and-periodic-boundary-condition-file-fort-15). The format is similar to the meteorological input file used when [NWS](../../parameter-definitions#NWS) =-4 (i.e. the PBL hurricane model input format following a hot start).` (407). |
| 409–418 | 기본 입력 구조 — 굵은 변수명과 빈 줄, 변수 정의 링크의 의미를 설명한다(409). 절점(node) 번호와 파랑 복사 응력 성분 입력 줄을 제시한다(411). 이어지는 물음표 세 줄을 그대로 옮긴다(413·415·417). 원문: `The basic file structure is shown below. Each line of input data is represented by a line containing the input variable name(s) in bold face type. Blank lines are only to enhance readability. Definitions of each variable are provided via hot links.` (409); `[**JN**](http://adcirc.org/home/documentation/users-manual-v50/parameter-definitions#JN), [**RSX(JN), RSY(JN)**](../../parameter-definitions#RSX_RSY)` (411); `??????????.` (413); `??????????.` (415); `??????????.` (417). |
| 419–432 | Notes / 자료 수·시간·절점·단위 — 시간 보간(interpolation)을 위해 최소 자료 집합(data set) 수를 요구한다(421). 자료 집합이 하나이면 파일 끝 오류로 실행을 종료한다(421). 일부 절점에 자료를 직접 입력한다(423). 일반 시작(cold start)·재시작 기준 시각과 추가 자료 간격, 시간 보간을 설명한다(425). 고정 폭 입력 형식, 두 번째 열의 종료 표식, 생략 절점의 기본값을 설명한다(427). 응력 단위와 밀도에 의한 환산, 전체 실행 기간의 자료 제공 의무를 설명한다(429–431). 수량·조건·형식·단위를 그대로 옮긴다. 원문: `**Notes:**` (419); `At least two datasets must be present in the file to allow for time interpolation. If only one dataset is present, the run will terminate with an unexpected end-of-file error` (421); `Radiation stresses are input directly to a subset of nodes in the ADCIRC grid (as specified by the node number [JN](../../parameter-definitions#JN)).` (423); `If ADCIRC is cold started, the first set of radiation stress data corresponds to TIME=STATIM. If ADCIRC is hot started, the first set of radiation stress data corresponds to TIME=HOT START TIME. Additional sets of radiation stress data must be provided every [RSTIMINC](../../parameter-definitions#RSTIMINC), where [RSTIMINC](../../parameter-definitions#RSTIMINC) is the radiation stress time interval and is specified in the [Model Parameter and Periodic Boundary Condition File](https://adcirc.org/home/documentation/users-manual-v51/input-file-descriptions/model-parameter-and-periodic-boundary-condition-file-fort-15/). Radiation stresses are interpolated in time to the ADCIRC time step.` (425); `Each data line must have the format I8, 2E13.5.Data input lines are repeated for as many nodes as desired. A line containing the # symbol in column 2 indicates radiation stress data at the next time increment begins on the following line. At each new time, any node that is not specified in the input file is assumed to have zero wave radiation stress.` (427); `Wave radiation stress must be input in units of velocity squared (consistent with the units of gravity). Stress in these units is obtained by dividing stress in units of force/area by the reference density of water.` (429); `Data must be provided for the entire model run, otherwise the run will crash!` (431). |
| 433–447 | 웹페이지 뒤쪽 코드 — 빈 줄, 유틸리티 표시 호출, 링크 사전 가져오기 설정, 쿠키 안내 설정, 슬라이드 표시 코드, New Relic 정보를 포함한다(433–447). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 411: JN의 변수 정의 링크는 `users-manual-v50` 경로이다. 이 페이지의 탐색 경로는 V51이다(403).
- 413·415·417: 기본 입력 구조의 세 줄은 모두 `??????????.`이다. 이 세 줄에는 변수명이나 반복 구문이 없다.
