---
file: models/ADCIRC/raw/manuals/website_markdown/home/documentation/users-manual-v52/output-file-descriptions/wetdry-elemental-state-file-noff-100/index.md
lines: 446
sha256: 1623b2652a9f0c587fd187401e7636bc167e971b508fbe9d5d0ad6016ed6c057
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# index.md — 판독 구간 기록

구간은 1행부터 446행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–12 | 웹페이지 감시 스크립트(New Relic browser monitoring script)가 시작된다(1–2행). 초기 설정과 압축된 JavaScript 로더는 웹페이지 성능·오류·이벤트 수집을 위한 코드다(1–2행). 이 구간은 ADCIRC 출력 파일 본문 앞의 웹페이지 코드다. 코드 뒤의 빈 줄을 포함한다(3–12행). |
| 13–85 | 웹페이지 스타일시트(Cascading Style Sheets, CSS)는 검색 입력란과 버튼, 제목 링크, 본문과 제목 글꼴, 머리말, 컨테이너와 콘텐츠 배치를 설정한다(13–85행). 스타일 주석·중괄호·빈 줄을 포함한다. |
| 86–142 | CSS는 본문 영역의 문단·링크, 오른쪽 열, 이동 경로(breadcrumb), 문맥 탐색 메뉴(context navigation), 인용문과 제목의 표시를 설정한다(86–142행). 스타일 선언과 빈 줄을 포함한다. |
| 143–200 | CSS는 탐색 메뉴의 목록·위치·크기와 하위 메뉴 배치를 설정한다(143–200행). 배경 그림 참조 원문은 `background:url(images/primary\_nav\_divider.gif) repeat-y scroll right bottom;` (166)이다. 이 배경 그림에 해당하는 로컬 파일은 없다. 그림 파일 없음. 스타일 선언과 빈 줄을 포함한다. |
| 201–231 | CSS는 마우스를 올린 링크와 현재 메뉴의 표시, 하위 메뉴의 표시, 콘텐츠 래퍼(wrapper), 태그 스타일과 이미지 크기를 설정한다(201–231행). 배경 그림 참조 원문은 `background: #76a3de url(images/primary\_nav\_bg\_repeat\_on.gif) repeat-x top;` (202)이다. 이 배경 그림에 해당하는 로컬 파일은 없다. 그림 파일 없음. 스타일 선언과 빈 줄을 포함한다. |
| 232–248 | 웹페이지 제목은 `Wet/Dry Elemental State file (noff.100) - ADCIRC` (232)이다. 구조화된 메타데이터(JSON-LD)는 페이지·탐색 경로·사이트 정보를 담는다(237행). 이모지(emoji) 지원 확인과 로딩 스크립트가 이어진다(242–246행). 스크립트 주석과 빈 줄을 포함한다. |
| 249–285 | WordPress의 CSS는 이모지 표시, 버튼·파일 링크, 화면 배치와 색상·글꼴·간격·그림자 프리셋(preset)을 설정한다(249–269행). 인용문 스타일과 뒤의 빈 줄을 포함한다(269–285행). |
| 286–303 | 관리 화면 지원 CSS가 있다(286–288행). Beehive의 Google Analytics 스크립트가 있다(292–298행). 사용자 지정 배경의 그림 참조 원문은 `body.custom-background { background-color: #ffffff; background-image: url("https://adcirc.org/wp-content/uploads/sites/2255/2013/03/grid\_bkgrd\_lt\_grey1.jpg"); background-position: left top; background-size: auto; background-repeat: repeat-y; background-attachment: scroll; }` (300)이다. 이 배경 그림에 해당하는 로컬 파일은 없다. 그림 파일 없음. 주석·스타일·스크립트 사이의 빈 줄을 포함한다. |
| 304–358 | 빈 제목 표식, ADCIRC 링크, 공식 웹사이트 문구와 탐색 건너뛰기 링크가 있다(304–310행). Community 메뉴는 개발자·협력기관·사용자 항목을 나열한다(312–322행). Documentation 메뉴는 사용자 매뉴얼, 입력·출력 설명, 컴파일, 명령행, 질의응답, 예제, 보고서와 이론 문서 등의 링크를 나열한다(323–358행). 목록 마크업과 빈 줄을 포함한다. |
| 359–403 | Related Software, News, Products와 ASGS 메뉴는 관련 소프트웨어, 워크숍·부트캠프·단체 사진, 제품과 운영 안내의 링크를 나열한다(359–400행). 단체 사진 항목은 일반 링크로 표시된다. 현재 출력 파일 문서까지의 이동 경로가 이어진다(402행). 목록 마크업과 빈 줄을 포함한다. |
| 404–413 | 제목은 `# Wet/Dry Elemental State file (noff.100)` (404)이다. `noff.100`은 자료 집합(dataset)이 작성된 시간 단계(time step)에서 요소(element)의 습윤·건조 상태(wet/dry state)를 기록한다(406행). `1`은 습윤 요소를 뜻한다(406행). `0`은 건조 요소를 뜻한다(406행). ADCIRC의 요소 습윤·건조 배열 이름은 `NOFF`다(406행). 자료는 일반적으로 실험적 습윤·건조 알고리즘을 개발하는 ADCIRC 개발자에게만 가치가 있다고 적는다(408행). 파일 작성은 `fort.15` 하단의 선택적 네임리스트(optional namelist)에서 활성화한다(410행). ASCII 형식만 사용할 수 있다(412행). 출력 일정은 전 영역 수면 높이(full domain water surface elevation) 파일 `fort.63`과 같다고 적는다(412행). 출력 일정의 매개변수 연결 문구는 원문 그대로 보존한다. 상태값·배열명·이용 대상·활성화 조건·출력 형식·일정 원문: `The noff.100 file records the wet/dry state of elements where 1 indicates an element is categorized as wet on the time step that the dataset was written while a value of 0 indicates that an element is categorized as dry. The name of the elemental wet/dry array in ADCIRC is NOFF.` (406); `These data are generally only valuable to ADCIRC developers who are working on experimental wet/dry algorithms.` (408); `The writing of the noff.100 output file is activated when the outputNOFF parameter is set to .true. in the optional wetDryContol namelist at the bottom of the fort.15 file.` (410); `Output is only available in the ascii format. The data are produced on the same schedule as the full domain water surface elevation (fort.63) file, i.e., the values of TOUTSGE, TOUTFGE, are used NSPOOLGE.` (412). 문단 사이의 빈 줄도 포함한다. |
| 414–427 | 파일 구조 설명은 굵은 글씨가 출력 변수명을 나타낸다고 적는다(414행). 빈 줄은 가독성을 위한 것이다(414행). 반복문은 여러 출력 행을 나타낸다(414행). 변수 정의는 링크로 제공한다고 적는다(414행). 파일 형식 예시의 머리글·자료 집합 수·요소 수·곱셈식은 `[**RUNDES**](https://adcirc.org/home/documentation/users-manual-v52/parameter-definitions#RUNDES), [**RUNID**](https://adcirc.org/home/documentation/users-manual-v52/parameter-definitions#RUNID), [**AGRID**](https://adcirc.org/home/documentation/users-manual-v52/parameter-definitions#AGRID)` (416); `[**NDSETSE**](https://adcirc.org/home/documentation/users-manual-v52/parameter-definitions#NDSETSE), [**NE**](https://adcirc.org/home/documentation/users-manual-v52/parameter-definitions#NE), [**DTDP**](https://adcirc.org/home/documentation/users-manual-v52/parameter-definitions#DTDP)\*[**NSPOOLGE**](https://adcirc.org/home/documentation/users-manual-v52/parameter-definitions#NSPOOLGE), [**NSPOOLGE**](https://adcirc.org/home/documentation/users-manual-v52/parameter-definitions#NSPOOLGE), [**IRTYPE**](https://adcirc.org/home/documentation/users-manual-v52/parameter-definitions#IRTYPE)` (418)이다. 시각·반복문·요소 상태·반복문 종료 행은 `[**TIME**](https://adcirc.org/home/documentation/users-manual-v52/parameter-definitions#TIME), [**IT**](https://adcirc.org/home/documentation/users-manual-v52/parameter-definitions#IT)` (420); `for i=1,[NE](https://adcirc.org/home/documentation/users-manual-v52/parameter-definitions#NE)` (422); `**i,** [**NOFF(i)**](https://adcirc.org/home/documentation/users-manual-v52/parameter-definitions#NOFF)` (424); `end i loop` (426)이다. 반복문 상한은 `NE`다(422행). 상태 출력 변수 표기는 `NOFF(i)`다(424행). 예시 행 사이의 빈 줄도 포함한다. |
| 428–430 | `Notes` 절은 `noff.100`이 정숫값(integer values)을 담는다고 적는다(430행). 이 파일은 절점(nodal) 자료 대신 요소(elemental) 자료를 생성하는 유일한 ADCIRC 출력 파일이라고 문서가 적는다(430행). 값의 형식과 문서의 유일성 진술 원문: `The noff.100 file contains integer values. It is the only ADCIRC output file that produces elemental (as opposed to nodal) data.` (430). 절 제목과 빈 줄도 포함한다. |
| 431–446 | 문서 본문 뒤의 빈 줄을 포함한다(431–433행). 웹페이지 유틸리티 호출이 있다(434행). 미리 가져오기(prefetch) 주소 설정이 있다(436행). 쿠키 동의 배너(cookie consent banner)의 문구·버튼·표시 설정과 CDATA 주석이 있다(439–441행). 슬라이더 표시 클래스 제거 스크립트가 있다(445행). New Relic 실행 정보와 초기 설정 스크립트가 마지막 행에 있다(446행). 스크립트 사이의 빈 줄을 포함한다. |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- `images/primary\_nav\_divider.gif` 배경 그림 참조가 있다(166행). `models/ADCIRC/raw/manuals/`에서 이 파일명의 로컬 사본을 찾지 못했다. 그림 파일 없음.
- `images/primary\_nav\_bg\_repeat\_on.gif` 배경 그림 참조가 있다(202행). `models/ADCIRC/raw/manuals/`에서 이 파일명의 로컬 사본을 찾지 못했다. 그림 파일 없음.
- `https://adcirc.org/wp-content/uploads/sites/2255/2013/03/grid\_bkgrd\_lt\_grey1.jpg` 배경 그림 참조가 있다(300행). `models/ADCIRC/raw/manuals/`에서 이 파일명의 로컬 사본을 찾지 못했다. 그림 파일 없음.
- 412행은 출력 일정 설명에 `the values of TOUTSGE, TOUTFGE, are used NSPOOLGE.`라고 적는다. 이 문장은 `NSPOOLGE`와 앞의 두 변수 사이의 사용 관계를 문법적으로 완결된 표현으로 제시하지 않는다. 해당 줄의 전체 원문은 `Output is only available in the ascii format. The data are produced on the same schedule as the full domain water surface elevation (fort.63) file, i.e., the values of TOUTSGE, TOUTFGE, are used NSPOOLGE.` (412)이다.
