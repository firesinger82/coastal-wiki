---
file: models/ADCIRC/raw/manuals/website_markdown/home/documentation/users-manual-v53/input-file-descriptions/wave-radiation-stress-forcing-file-fort-23/index.md
lines: 446
sha256: 0bfc9523a712b562f8df5a0a86de6a36af3dea6f2e422725bd9e72b647fa11ab
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# Wave Radiation Stress Forcing File (fort.23) — 판독 구간 기록

구간은 1행부터 446행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–12 | 웹 성능 수집 스크립트와 앞쪽 빈 줄 — New Relic의 브라우저 오류·이벤트·통신 수집용 JavaScript가 들어 있다(1–2). 뒤에는 빈 줄이 이어진다(3–12). |
| 13–51 | 검색·글꼴 스타일 — 검색 필드(search field), 사이트 머리말(header), 본문 및 링크의 스타일시트(Cascading Style Sheets, CSS)을 지정한다(13–51). |
| 52–93 | 페이지 틀 스타일 — 컨테이너(container), 머리말, 태그 표시 및 본문 열의 CSS 스타일을 지정한다(52–93). |
| 94–135 | 본문 요소 스타일 — 문단, 링크, 오른쪽 열, 탐색 경로(breadcrumb), 인용문 및 소제목의 CSS 스타일을 지정한다(94–135). |
| 136–184 | 메뉴 스타일 — 본문 배치와 탐색 메뉴(navigation menu)의 CSS 스타일을 지정한다. 메뉴 구분선의 배경 이미지 URL이 들어 있다(136–184). |
| 185–230 | 하위 메뉴·그림 크기 스타일 — 하위 메뉴(submenu)의 위치 및 상태별 표시를 지정한다. 래퍼(wrapper), 태그 및 본문 그림 크기의 CSS 스타일이 이어진다(185–230). |
| 231–241 | 페이지 제목·검색 메타데이터 — 문서 제목이 나온다(232). 웹페이지, 웹사이트 및 탐색 경로의 구조화 데이터(structured data)가 들어 있다(237). 주변 빈 줄도 이 구간에 포함한다(231–241). |
| 242–260 | 이모지 스크립트·스타일 — 브라우저의 이모지(emoji) 지원 확인, 검사 결과 저장 및 보조 스크립트 로딩 코드가 들어 있다(242–246). 이모지 그림의 CSS 스타일과 빈 줄이 이어진다(247–260). |
| 261–290 | 버튼·파일·관리자 표시 스타일 — 버튼과 파일 블록 및 전역 표시 설정이 들어 있다(262–269). 관리자 막대(admin bar)의 지원 스타일과 주변 빈 줄이 이어진다(270–290). |
| 291–302 | 웹 분석·배경 스타일 — Beehive와 Google Analytics 설정이 들어 있다(292–298). 페이지 배경 이미지의 CSS URL과 빈 줄이 이어진다(299–302). |
| 303–322 | 사이트 머리말·Community 메뉴 — ADCIRC 사이트 이름, 사이트 설명 및 탐색 건너뛰기 링크가 나온다(304–310). 개발자, 관련 연구 그룹 및 사용자 목록의 메뉴가 이어진다(312–322). |
| 323–358 | Documentation 메뉴 — 소개, 구조, 위키, 사용자 매뉴얼 및 입력·출력 파일 설명 링크가 있다(323–358). 컴파일·명령행 옵션, FAQ, 예제, 개발자 안내, 이론 보고서, 특수 기능 및 출판물 등의 링크도 같은 메뉴에 있다(323–358). |
| 359–393 | 관련 소프트웨어·News 메뉴 — 유틸리티와 격자 생성기(grid generator) 링크가 있다(359–361). 사용자 모임, 워크숍(workshop), 발표 자료, 일정, 단체 사진 및 예보·모의 사례 링크가 이어진다(362–393). 단체 사진은 탐색 메뉴의 일반 링크이다. |
| 394–403 | Products 메뉴·본문 진입 — 조석 자료, 출판물, 격자, 예보, 표층 기름 이동 및 ASGS 링크가 있다(394–400). 이 문서의 탐색 경로와 주변 빈 줄이 이어진다(401–403). |
| 404–409 | Wave Radiation Stress Forcing File (fort.23) — 파랑 복사 응력(wave radiation stress)은 단독으로 또는 바람을 포함한 다른 외력(forcing)과 함께 ADCIRC를 구동할 수 있다고 적는다(404–406). 파일을 읽는 조건과 비교 대상 기상 입력 형식(meteorological input format)은 원문과 같다(406). 굵은 변수 이름 줄 및 가독성을 위한 빈 줄의 표기법을 설명한다(408). 변수 정의는 링크로 제공한다고 적는다(408). 원문: `Wave radiation stresses can e used by themselves or in concert with other forcing (including winds) to drive ADCIRC. The wave radiation stress input file is read when ABS([NWS](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#NWS))>=100 in the [Model Parameter and Periodic Boundary Condition File](../model-parameter-and-periodic-boundary-condition-file-fort-15). The format is similar to the meteorological input file used when [NWS](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#NWS) =-4 (i.e. the PBL hurricane model input format following a hot start).` (406); `The basic file structure is shown below. Each line of input data is represented by a line containing the input variable name(s) in bold face type. Blank lines are only to enhance readability. Definitions of each variable are provided via hot links.` (408). |
| 410–417 | 노드별 입력 형식 — 노드(node) 번호와 파랑 복사 응력 성분(component)의 입력 줄을 제시한다(410). 뒤따르는 형식 줄은 물음표로 표시되어 있다(412–416). 각 줄은 원문과 같다(410–416). 원문: `[**JN**](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#JN), [**RSX(JN), RSY(JN)**](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#RSX_RSY)` (410); `??????????.` (412); `??????????.` (414); `??????????.` (416). |
| 418–423 | Notes: 데이터 세트 수·적용 노드 — 시간 보간(time interpolation)을 위해 필요한 최소 데이터 세트(data set) 수를 설명한다(418–420). 데이터 세트가 하나일 때의 예기치 않은 파일 끝(unexpected end-of-file) 오류 종료를 설명한다(420). 복사 응력은 노드 번호로 지정하는 격자(grid)의 일부 노드에 직접 입력한다(422). 수량과 적용 범위는 원문과 같다(420–422). 원문: `**Notes:**` (418); `At least two datasets must be present in the file to allow for time interpolation. If only one dataset is present, the run will terminate with an unexpected end-of-file error` (420); `Radiation stresses are input directly to a subset of nodes in the ADCIRC grid (as specified by the node number [JN](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#JN)).` (422). |
| 424–425 | 시작 시점·입력 시간 간격 — 초기 시작(cold start)과 재시작(hot start)의 첫 데이터 시점을 구분한다(424). 추가 데이터 제공 간격은 fort.15에 지정하며 ADCIRC 시간 단계(time step)에 맞춰 보간한다고 적는다(424). 시점 식과 제공 간격의 매개변수는 원문과 같다(424). 원문: `If ADCIRC is cold started, the first set of radiation stress data corresponds to TIME=STATIM. If ADCIRC is hot started, the first set of radiation stress data corresponds to TIME=HOT START TIME. Additional sets of radiation stress data must be provided every [RSTIMINC](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#RSTIMINC), where [RSTIMINC](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#RSTIMINC) is the radiation stress time interval and is specified in the [Model Parameter and Periodic Boundary Condition File](https://adcirc.org/home/documentation/users-manual-v53/input-file-descriptions/model-parameter-and-periodic-boundary-condition-file-fort-15). Radiation stresses are interpolated in time to the ADCIRC time step.` (424). |
| 426–427 | 자료 줄 형식·다음 시간 구분 — 자료 줄의 Fortran 형식(Fortran format), 입력 노드 수 및 다음 시간 자료의 구분 기호를 설명한다(426). 새 시각에 기재되지 않은 노드의 파랑 복사 응력은 영으로 가정한다고 적는다(426). 형식과 구분 기호의 열 위치는 원문과 같다(426). 원문: `Each data line must have the format I8, 2E13.5.Data input lines are repeated for as many nodes as desired. A line containing the # symbol in column 2 indicates radiation stress data at the next time increment begins on the following line. At each new time, any node that is not specified in the input file is assumed to have zero wave radiation stress.` (426). |
| 428–431 | 응력 단위·전체 실행 구간 자료 — 파랑 복사 응력은 속도 제곱 단위(velocity squared units)로 입력해야 한다고 적는다(428). 중력 단위와의 관계에 관한 괄호 설명은 원문과 같다(428). 힘/면적(force/area) 단위의 응력을 물의 기준 밀도(reference density)로 나누어 이 단위를 얻는다고 적는다(428). 전체 모델 실행 기간에 자료를 제공하지 않으면 실행이 실패한다고 적는다(430). 단위 변환과 자료 제공 의무는 원문과 같다(428–430). 원문: `Wave radiation stress must be input in units of velocity squared (consistent with the units of gravity). Stress in these units is obtained by dividing stress in units of force/area by the reference density of water.` (428); `Data must be provided for the entire model run, otherwise the run will crash!` (430). |
| 432–446 | 웹페이지 끝부분 — 유틸리티 호출과 링크 미리 가져오기(prefetch) 설정이 들어 있다(434–436). 쿠키 안내문, jQuery 코드 및 New Relic 정보가 이어진다(439–446). 주변 빈 줄도 이 구간에 포함한다(432–446). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 406행: 첫 문장에 `can e used`라는 표기가 있다.
- 412·414·416행: 파일 형식 예시의 세 줄이 각각 `??????????.`로 적혀 있다. 그 줄에서 입력 변수나 반복 범위를 판독할 수 없다.
