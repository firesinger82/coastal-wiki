---
file: models/ADCIRC/raw/manuals/website_markdown/home/documentation/users-manual-v53/output-file-descriptions/wetdry-state-nodes-nodecode-63/index.md
lines: 444
sha256: 201941cf6ca45edcb4573d21ed7cb66a62ec690cfb89aa7d63411c34e9af3d39
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# index.md — 판독 구간 기록

구간은 1행부터 444행까지 빈틈없이 이어진다.

내용 칸의 한국어 설명은 AI 판독 요약이다. `원문:` 뒤의 백틱 문자열은 원문 인용이다.

| 구간 | 내용 |
|---|---|
| 1–12 | 사이트 스크립트 — New Relic의 초기 설정과 축약된 JavaScript가 들어 있다(1–2). 뒤의 빈 줄도 이 구간에 포함한다(3–12). ADCIRC 출력 파일의 변수 설명은 이 구간에 없다. |
| 13–85 | 사이트 기본 스타일 — 스타일시트(CSS)는 검색 입력칸, 제목, 본문, 링크, 페이지 컨테이너와 콘텐츠 영역의 표시 속성을 지정한다(13–85). 출력 파일의 데이터 형식을 설명하는 절은 아니다. |
| 86–142 | 사이트 본문 스타일 — CSS는 콘텐츠 영역, 문단, 링크, 경로 표시(breadcrumbs), 활성 메뉴, 인용문과 다른 콘텐츠 영역의 표시 속성을 지정한다(86–142). 주석도 이 구간에 포함한다(86·90). |
| 143–200 | 사이트 메뉴 스타일 — CSS는 메뉴 영역과 하위 메뉴의 배치, 글자와 링크 표시 속성을 지정한다(143–200). 메뉴 배경은 `images/primary\_nav\_divider.gif`를 참조한다(166). 로컬 사본을 찾지 못했다. 그림 파일 없음. |
| 201–231 | 사이트 메뉴 강조 스타일 — CSS는 링크를 가리킬 때의 배경, 하위 메뉴 표시와 현재 메뉴 항목의 글자색을 지정한다(201–225). 슬라이드 영역, 메뉴 글자, 태그 표시와 이미지 크기의 스타일도 들어 있다(226–230). 배경 참조 `images/primary\_nav\_bg\_repeat\_on.gif`의 로컬 사본을 찾지 못했다(202). 그림 파일 없음. 마지막 빈 줄도 포함한다(231). |
| 232–241 | 페이지 제목·구조화 메타데이터 — 페이지 제목을 적는다(232). JSON은 페이지 주소, 문서 경로, 언어, 게시 정보와 사이트 검색 정보를 적는다(237). 빈 줄도 이 구간에 포함한다(233–236·238–241). |
| 242–290 | 사이트 이모지·공통 스타일 — WordPress 이모지(emoji) 설정과 지원 여부를 검사하는 JavaScript가 들어 있다(242–246). 이모지, 버튼, 색상, 글꼴 크기, 여백, 그림자와 블록 배치의 CSS도 들어 있다(249–269). 관리 표시줄의 스타일과 빈 줄을 포함한다(270–290). |
| 291–303 | 사이트 방문 분석·배경 스타일 — 방문 분석용 데이터층과 설정 호출이 들어 있다(292–298). 본문 배경 스타일은 `https://adcirc.org/wp-content/uploads/sites/2255/2013/03/grid\_bkgrd\_lt\_grey1.jpg`를 참조한다(300). 로컬 사본을 찾지 못했다. 그림 파일 없음. 빈 줄도 이 구간에 포함한다(291·299·301–303). |
| 304–322 | 사이트 제목·Community 메뉴 — 빈 제목 마크업, ADCIRC 사이트 제목, 공식 사이트 문구와 탐색 생략 링크를 적는다(304–310). Community 메뉴는 개발자, 개발 협력 기관과 사용자 링크를 나열한다(312–322). |
| 323–358 | Documentation 메뉴 — 사용자 설명서와 위키, 버전별 입출력 설명 및 이력, 컴파일·명령행 옵션, 자주 묻는 질문, 실행 안내와 예제의 링크를 나열한다(323–349). 보고서, 이론, 특수 기능, 출판물과 하위 영역 모델링의 링크도 나열한다(350–358). |
| 359–401 | Related software·News·Products·ASGS 메뉴 — 관련 소프트웨어 링크를 나열한다(359–361). 소식 메뉴에는 회의, 워크숍, 발표, 일정, 사진과 허리케인 계산 관련 링크가 있다(362–393). 사진 링크가 가리키는 파일의 로컬 사본을 찾지 못했다(368·370·374·375·387·389). 그림 파일 없음. 제품과 ASGS 링크 및 마지막 빈 줄도 포함한다(394–401). |
| 402–405 | 문서 경로·절 제목 — 경로 표시는 User’s Manual – v53의 Output File Descriptions 아래에 이 문서를 둔다(402). 절 제목 원문: `# Wet/Dry State of Nodes (nodecode.63)` (404). 뒤의 빈 줄도 포함한다(405). |
| 406–407 | Wet/Dry State of Nodes / 상태 값 — `nodecode.63`은 데이터셋(dataset)을 쓴 시간 단계(timestep)의 절점(node) 습윤·건조 상태(wet/dry state)를 기록한다(406). 값 `1`은 습윤으로 분류된 절점이고 값 `0`은 건조로 분류된 절점이다(406). 문서는 이 데이터가 일반적으로 실험적 습윤·건조 알고리즘을 다루는 ADCIRC 개발자에게만 가치가 있다고 적는다(406). 상태 값과 한정 문구의 원문: `The nodecode.63 file records the wet/dry state of nodes where 1 indicates a node is categorized as wet on the timestep that the dataset was written while a value of 0 indicates that a node is categorized as dry. These data are generally only valuable to ADCIRC developers who are working on experimental wet/dry algorithms.` (406). |
| 408–409 | Wet/Dry State of Nodes / 출력 활성화 — 문서는 `fort.15` 하단의 선택적 이름목록(namelist)에서 출력을 활성화하는 조건을 적는다(408). 매개변수 이름, 설정값과 이름목록 이름의 원문: `The writing of the nodecode.63 output file is activated when the outputNodeCode parameter is set to .true. in the optional wetDryContol namelist at the bottom of the fort.15 file.` (408). |
| 410–411 | Wet/Dry State of Nodes / 형식·출력 일정 — 출력은 ASCII 형식만 가능하다(410). 문서는 전 영역 수면고(water surface elevation) 출력 `fort.63`과 같은 일정으로 데이터를 생성한다고 적는다(410). 일정 관련 매개변수 링크와 문장 순서를 그대로 옮긴다. 원문: `Output is only available in the ascii format. The data are produced on the same schedule as the full domain water surface elevation (fort.63) file, i.e., the values of [TOUTSGE](https://adcirc.org/home/documentation/users-manual-v52/parameter-definitions#TOUTSGE), [TOUTFGE](https://adcirc.org/home/documentation/users-manual-v52/parameter-definitions#TOUTFGE), are used [NSPOOLGE](https://adcirc.org/home/documentation/users-manual-v52/parameter-definitions#NSPOOLGE).` (410). |
| 412–413 | Wet/Dry State of Nodes / 기본 파일 구조 안내 — 굵은 변수 이름을 적은 문서의 한 행은 출력의 한 행을 나타낸다(412). 빈 줄은 가독성을 위한 것이다(412). 반복문은 여러 출력 행을 나타낸다(412). 변수 정의는 링크로 제공한다고 적는다(412). |
| 414–417 | Wet/Dry State of Nodes / 파일 머리행 — 문서는 머리행의 변수 배열을 두 행으로 제시한다(414·416). 두 번째 행에는 `DTDP`와 `NSPOOLGE`의 곱셈 표기가 있다(416). 변수 배열과 곱셈 표기의 원문: `[**RUNDES**](https://adcirc.org/home/documentation/users-manual-v52/parameter-definitions#RUNDES), [**RUNID**](https://adcirc.org/home/documentation/users-manual-v52/parameter-definitions#RUNID), [**AGRID**](https://adcirc.org/home/documentation/users-manual-v52/parameter-definitions#AGRID)` (414); `[**NDSETSE**](https://adcirc.org/home/documentation/users-manual-v52/parameter-definitions#NDSETSE), **[NP](https://adcirc.org/home/documentation/users-manual-v52/parameter-definitions#NP)**, **[DTDP](https://adcirc.org/home/documentation/users-manual-v52/parameter-definitions#DTDP)**\***[NSPOOLGE](https://adcirc.org/home/documentation/users-manual-v52/parameter-definitions#NSPOOLGE)**, **[NSPOOLGE](https://adcirc.org/home/documentation/users-manual-v52/parameter-definitions#NSPOOLGE)**, **[IRTYPE](https://adcirc.org/home/documentation/users-manual-v52/parameter-definitions#IRTYPE)**` (416). |
| 418–425 | Wet/Dry State of Nodes / 시각 행·절점 반복 — 문서는 `TIME`, `IT` 행 뒤에 `k`를 `1`부터 `NP`까지 반복하는 구조를 제시한다(418–424). 반복 안의 출력 행은 `k`와 `nodecode(k)`를 적는다(422). 문서의 빈 줄과 반복 종료 행도 포함한다(419·421·423–425). 출력 형식 원문: `[**TIME**](https://adcirc.org/home/documentation/users-manual-v52/parameter-definitions#TIME), [**IT**](https://adcirc.org/home/documentation/users-manual-v52/parameter-definitions#IT)` (418); `for k=1,[NP](https://adcirc.org/home/documentation/users-manual-v52/parameter-definitions#NP)` (420); `**k,** [**nodecode(k)**](https://adcirc.org/home/documentation/users-manual-v52/parameter-definitions#nodecode)` (422); `end k loop` (424). |
| 426–429 | Notes — 문서는 `nodecode.63`의 값이 정수(integer)라고 적는다(428). 제목 마크업과 빈 줄도 포함한다(426–429). 원문: `The nodecode.63 file contains integer values.` (428). |
| 430–444 | 사이트 하단 스크립트 — 화면 유틸리티 호출, 링크 사전 가져오기(prefetch) 설정, 쿠키(cookie) 안내 설정, 슬라이드 표시 클래스 변경과 New Relic 정보를 포함한다(432·434·437–439·443–444). 나머지 빈 줄도 이 구간에 포함한다(430–431·433·435–436·440–442). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

그림 파일의 로컬 사본은 `models/ADCIRC/raw/manuals/`에서 파일명으로 검색했다. 문서와 같은 폴더는 `ls`로 확인했다.

- 408행: 출력 활성화 문장은 선택적 이름목록의 이름을 `wetDryContol`로 표기한다. 이 기록은 그 표기를 그대로 옮겼다.
- 410행: 일정 설명 문장에서 `are used` 바로 뒤에 `NSPOOLGE` 링크가 놓여 있다. 문서는 두 부분을 잇는 단어나 구두점을 적지 않았다.
- 402·410·414·416·418·420·422행: 문서 경로 표시는 v53이다(402). 일정과 출력 변수의 정의 링크는 v52 경로를 가리킨다(410·414·416·418·420·422). 링크 대상 문서의 본문은 이번 판독 범위에 없다.
- 412–422행: 문서는 출력 변수의 정의를 링크로 안내한다(412). 이 파일 안에는 `RUNDES`, `RUNID`, `AGRID`, `NDSETSE`, `NP`, `DTDP`, `NSPOOLGE`, `IRTYPE`, `TIME`, `IT`의 개별 정의와 단위가 없다(414·416·418·420).
- 166행: 그림 파일 없음. CSS 배경 참조 `images/primary\_nav\_divider.gif`의 로컬 사본을 찾지 못했다.
- 202행: 그림 파일 없음. CSS 배경 참조 `images/primary\_nav\_bg\_repeat\_on.gif`의 로컬 사본을 찾지 못했다.
- 300행: 그림 파일 없음. CSS 배경 참조 `grid\_bkgrd\_lt\_grey1.jpg`의 로컬 사본을 찾지 못했다.
- 368행: 그림 파일 없음. 탐색 메뉴의 사진 링크가 가리키는 `ADCIRC2018_Group_Photo2.jpg`의 로컬 사본을 찾지 못했다.
- 370행: 그림 파일 없음. 탐색 메뉴의 사진 링크가 가리키는 `2017ADCIRCUGMGroupPhoto.jpg`의 로컬 사본을 찾지 못했다.
- 374행: 그림 파일 없음. 탐색 메뉴의 사진 링크가 가리키는 `160506-A-Y1769-008-A-1.jpg`의 로컬 사본을 찾지 못했다.
- 375행: 그림 파일 없음. 탐색 메뉴의 사진 링크가 가리키는 `adcircBootCampers2016_small_caption.jpg`의 로컬 사본을 찾지 못했다.
- 387행: 그림 파일 없음. 탐색 메뉴의 사진 링크가 가리키는 `2011_ADCIRC_meeting.jpg`의 로컬 사본을 찾지 못했다.
- 389행: 그림 파일 없음. 탐색 메뉴의 사진 링크가 가리키는 `ADCIRC_Workshop2010_GroupPhoto2.png`의 로컬 사본을 찾지 못했다.
