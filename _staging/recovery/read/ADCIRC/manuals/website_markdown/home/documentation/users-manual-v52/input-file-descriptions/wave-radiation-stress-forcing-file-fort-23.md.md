---
file: models/ADCIRC/raw/manuals/website_markdown/home/documentation/users-manual-v52/input-file-descriptions/wave-radiation-stress-forcing-file-fort-23.md
lines: 446
sha256: e6c114cdb2b1fafe52194f3f340f5654e8c64ac9a33a3fa5d0f50f446a773368
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# Wave Radiation Stress Forcing File (fort.23) — 판독 구간 기록

구간은 1행부터 446행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–12 | 웹사이트 계측 스크립트(New Relic) — 계측 초기 설정(1)과 축약된 자바스크립트(JavaScript) 로더(2)를 포함한다. 3–12행은 빈 줄이다. |
| 13–77 | 웹사이트 스타일시트(CSS) / 머리말·배치 — 검색창과 버튼의 표시 규칙(13–25)을 포함한다. 머리말·본문의 글꼴과 색상, 페이지 컨테이너와 콘텐츠 영역의 배치를 지정한다(26–77). |
| 78–142 | 웹사이트 스타일시트 / 본문·링크 — 단일 열 콘텐츠와 본문 영역의 표시 규칙(78–93)을 포함한다. 문단·링크·탐색 경로(breadcrumb)·인용문·다른 콘텐츠 배치의 표시 규칙을 지정한다(94–142). |
| 143–200 | 웹사이트 스타일시트 / 탐색 메뉴 — 메뉴 영역·목록·메뉴 항목의 배치를 지정한다(143–176). 하위 메뉴의 위치·폭·색상·표시 규칙을 지정한다(177–200). |
| 201–231 | 웹사이트 스타일시트 / 메뉴 상태·이미지 크기 — 포인터를 올린 메뉴와 현재 메뉴 항목의 표시 규칙을 지정한다(201–225). 콘텐츠 높이·메뉴 글꼴·태그 숨김 규칙과 자동 크기 이미지 선택자 규칙을 포함한다(226–230). 229·231행은 빈 줄이다. |
| 232–241 | 페이지 제목·메타데이터 — 페이지 제목(232)과 페이지 URL·게시 시각·수정 시각·탐색 경로를 담은 JSON-LD(237)를 포함한다. 나머지 행은 빈 줄이다. |
| 242–270 | WordPress 이모지·블록 표시 — 이모지 설정(243)과 지원 검사·로딩 스크립트(245)를 포함한다. 이모지 표시 스타일(249–259)과 버튼·블록·색상·배치의 자동 생성 스타일(262–269)을 포함한다. 주석과 빈 줄도 이 구간에 포함한다. |
| 271–303 | 관리자 표시·방문 통계·배경 — 빈 줄과 관리자 표시 스타일(286–288)을 포함한다. 방문 통계 초기화(292–298)와 사이트 배경 이미지의 스타일(300)을 포함한다. |
| 304–322 | 사이트 제목·Community 메뉴 — 공식 사이트 제목과 탐색 건너뛰기 링크를 포함한다(304–310). 개발 그룹·개발 협력 기관·사용자 메뉴를 나열한다(312–322). |
| 323–358 | Documentation 메뉴 — 사용자 매뉴얼·컴파일 옵션·FAQ·위키·예제·보고서·논문 링크를 나열한다(323–358). 모델 입력 형식의 기술 본문은 이 구간에 없다. |
| 359–400 | Related software·News·Products·ASGS 메뉴 — 관련 소프트웨어 링크를 나열한다(359–361). 행사·발표 자료·단체 사진·예보·시뮬레이션·제품·ASGS 링크를 나열한다(362–400). 단체 사진은 일반 링크로 적혀 있다. |
| 401–405 | 본문 탐색 경로·제목 — 매뉴얼 내 페이지 위치(402)와 이 페이지의 제목(404)을 표시한다. 나머지 행은 빈 줄이다. |
| 406–409 | Wave Radiation Stress Forcing File / 적용 조건·표시 규칙 — 파랑 복사응력(wave radiation stress)을 단독 또는 다른 외력(forcing)과 함께 사용할 수 있다고 설명한다(406). 파일 읽기 조건과 비교 대상인 기상 입력 형식을 제시한다(406). 굵은 변수명·빈 줄·정의 링크의 표시 규칙을 설명한다(408). 원문: `Wave radiation stresses can e used by themselves or in concert with other forcing (including winds) to drive ADCIRC. The wave radiation stress input file is read when ABS([NWS](https://adcirc.org/home/documentation/users-manual-v52/parameter-definitions#NWS))>=100 in the [Model Parameter and Periodic Boundary Condition File](../model-parameter-and-periodic-boundary-condition-file-fort-15). The format is similar to the meteorological input file used when [NWS](https://adcirc.org/home/documentation/users-manual-v52/parameter-definitions#NWS) =-4 (i.e. the PBL hurricane model input format following a hot start).` (406); `The basic file structure is shown below. Each line of input data is represented by a line containing the input variable name(s) in bold face type. Blank lines are only to enhance readability. Definitions of each variable are provided via hot links.` (408). |
| 410–417 | 입력 형식 — 절점 번호와 복사응력 성분의 레코드를 제시한다(410). 뒤 세 행에는 물음표로 된 원문 표기가 남아 있다(412·414·416). 원문: `[**JN**](http://adcirc.org/home/documentation/users-manual-v50/parameter-definitions#JN), [**RSX(JN), RSY(JN)**](https://adcirc.org/home/documentation/users-manual-v52/parameter-definitions#RSX_RSY)` (410); `??????????.` (412); `??????????.` (414); `??????????.` (416). |
| 418–425 | Notes / 자료집합·절점·시각 — 시간 보간에 필요한 자료집합 수와 부족 시 종료 조건을 제시한다(420). 입력 대상 절점의 선택 방법을 설명한다(422). 초기 시작(cold start)·재시작(hot start)의 첫 시각과 추가 자료의 시간 간격 및 계산 시간 간격으로의 보간 규칙을 제시한다(424). 원문: `**Notes:**` (418); `At least two datasets must be present in the file to allow for time interpolation. If only one dataset is present, the run will terminate with an unexpected end-of-file error` (420); `Radiation stresses are input directly to a subset of nodes in the ADCIRC grid (as specified by the node number [JN](https://adcirc.org/home/documentation/users-manual-v52/parameter-definitions#JN)).` (422); `If ADCIRC is cold started, the first set of radiation stress data corresponds to TIME=STATIM. If ADCIRC is hot started, the first set of radiation stress data corresponds to TIME=HOT START TIME. Additional sets of radiation stress data must be provided every [RSTIMINC](https://adcirc.org/home/documentation/users-manual-v52/parameter-definitions#RSTIMINC), where [RSTIMINC](https://adcirc.org/home/documentation/users-manual-v52/parameter-definitions#RSTIMINC) is the radiation stress time interval and is specified in the [Model Parameter and Periodic Boundary Condition File](https://adcirc.org/home/documentation/users-manual-v52/input-file-descriptions/model-parameter-and-periodic-boundary-condition-file-fort-15/). Radiation stresses are interpolated in time to the ADCIRC time step.` (424). |
| 426–433 | Notes / 레코드 형식·단위·기간 — 고정 폭 레코드 형식과 다음 시각을 표시하는 구분자, 지정하지 않은 절점의 복사응력 처리를 제시한다(426). 속도 제곱 단위와 기준 물 밀도(reference density of water)를 사용하는 변환 방법을 제시한다(428). 전체 실행 기간에 대한 입력 의무와 누락 시 결과를 적는다(430). 431–433행은 빈 줄이다. 원문: `Each data line must have the format I8, 2E13.5.Data input lines are repeated for as many nodes as desired. A line containing the # symbol in column 2 indicates radiation stress data at the next time increment begins on the following line. At each new time, any node that is not specified in the input file is assumed to have zero wave radiation stress.` (426); `Wave radiation stress must be input in units of velocity squared (consistent with the units of gravity). Stress in these units is obtained by dividing stress in units of force/area by the reference density of water.` (428); `Data must be provided for the entire model run, otherwise the run will crash!` (430). |
| 434–446 | 페이지 끝 스크립트 — 사이트 유틸리티 호출(434), 링크 미리 읽기 설정(436), 쿠키 안내문 설정과 주석(439–441)을 포함한다. 표시 클래스 변경(445)과 계측 정보(446)를 포함한다. 나머지 행은 빈 줄이다. |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 406: 첫 문장의 원문 표기는 `can e used`이다.
- 410·422: 입력 형식의 `JN` 정의 링크는 v50 매개변수 페이지를 가리킨다. 뒤 설명의 `JN` 정의 링크는 v52 매개변수 페이지를 가리킨다.
- 412·414·416: 입력 형식의 세 행은 모두 `??????????.`로 적혀 있다.
