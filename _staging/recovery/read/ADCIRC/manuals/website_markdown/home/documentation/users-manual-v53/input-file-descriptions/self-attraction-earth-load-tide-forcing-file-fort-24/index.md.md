---
file: models/ADCIRC/raw/manuals/website_markdown/home/documentation/users-manual-v53/input-file-descriptions/self-attraction-earth-load-tide-forcing-file-fort-24/index.md
lines: 448
sha256: 8bc22c03717886946dccf473ca031bf52632eb999d1a5d830ebbd1519b46b149
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# Self Attraction/Earth Load Tide Forcing File (fort.24) — 판독 구간 기록

구간은 1행부터 448행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–12 | 웹페이지 시작 코드 — New Relic 초기 설정과 브라우저 계측 코드가 있다(1–2). 뒤에는 빈 줄이 이어진다(3–12). |
| 13–77 | 웹페이지 스타일(CSS) / 검색·본문 틀 — 검색 입력란과 버튼, 제목, 본문 글꼴, 컨테이너(container), 머리글과 오른쪽 본문 영역의 스타일을 지정한다(13–77). |
| 78–142 | 웹페이지 스타일 / 본문·링크·위치 표시 — 한 열 본문 영역, 문단, 링크, 위치 표시(breadcrumb), 활성 메뉴, 인용 블록과 두 열 본문 영역의 스타일을 지정한다(78–142). |
| 143–200 | 웹페이지 스타일 / 탐색 메뉴 — 탐색 영역, 메뉴 목록, 항목, 링크와 하위 메뉴의 배치를 지정한다(143–200). 메뉴 구분선 이미지 경로를 참조한다(166). |
| 201–230 | 웹페이지 스타일 / 메뉴 상태 — 마우스를 올린 항목, 열린 하위 메뉴와 현재 페이지 항목의 스타일을 지정한다(201–225). 메뉴 배경 이미지 경로를 참조한다(202). 콘텐츠 높이, 링크 글자 굵기, 태그 표시와 이미지 표시 크기 규칙이 이어진다(226–230). |
| 231–240 | 페이지 제목·메타데이터 — 페이지 제목과 구조화 데이터(JSON-LD)가 있다(232·237). 구조화 데이터는 원문 URL, 게시 시각, 웹사이트, 위치 표시와 검색 동작을 담는다(237). 나머지 행은 빈 줄이다. |
| 241–270 | WordPress 화면 지원 코드 — 이모지(emoji) 설정과 지원 여부 검사 코드가 있다(242–246). 이모지, 버튼, 파일 링크, 색상·글꼴·간격 및 블록 배치 스타일이 이어진다(249–269). 빈 줄도 포함한다. |
| 271–303 | 관리 표시·접속 분석·배경 — 빈 줄, 지원 표시 스타일, Beehive 분석 설정과 사이트 배경 스타일이 있다(271–300). 사이트 배경 이미지 URL을 참조한다(300). 마지막 빈 줄도 포함한다(301–303). |
| 304–322 | 사이트 머리글·Community 메뉴 — 빈 제목 마크업, 사이트 이름, 공식 웹사이트 문구와 탐색 건너뛰기 링크가 있다(304–310). 개발 그룹·협력기관 및 사용자 메뉴를 나열한다(312–322). |
| 323–358 | Documentation 메뉴 — v50·v51·v52·v53 매뉴얼, 입력·출력 설명, 버전 이력, 컴파일·명령행 옵션, FAQ와 관련 문서 링크를 나열한다(323–358). |
| 359–401 | Related software·News·Products·ASGS 메뉴 — 유틸리티(utility), 격자 생성기, 모임 자료, 예보, 사례, 조석 데이터와 ASGS 링크를 나열한다(359–400). 메뉴에는 모임 사진을 가리키는 일반 링크가 있다(368·370·374·375·387·389). 끝 빈 줄도 포함한다(401). |
| 402–411 | Self Attraction/Earth Load Tide Forcing File (fort.24) / 적용 조건·형식 — 위치 표시와 제목이 있다(402–404). 자체 인력(self attraction)·지구 하중(earth load) 조석(tide)의 적용 조건을 제시한다(406). 속도 정보가 없는 “tea” 조화 형식(harmonic format)을 사용한다(408). 항목은 분조(constituent)별로 묶으며 조석 퍼텐셜(tidal potential) 항과 같은 순서를 따라야 한다(408). 위상(phase)·진폭(amplitude)의 단위 의무와 교점 인자(nodal factor)·평형 인수(equilibrium argument)에 의한 값 수정을 설명한다(408). 굵은 변수명, 빈 줄과 반복문(loop)의 의미를 설명한다(410). 조건·단위·입력 규칙을 원문 그대로 옮긴다. 원문: `Self attraction/earth load tides are used to force ADCIRC when [NTIP](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#NTIP)=2 in the [Model Parameter and Periodic Boundary Condition File](https://adcirc.org/home/documentation/users-manual-v53/input-file-descriptions/model-parameter-and-periodic-boundary-condition-file-fort-15).` (406); `The format of this file is identical to the “tea” harmonic format with no velocity information included. Entries are grouped by constituents and must be in the same order as the tidal potential terms listed in the [Model Parameter and Periodic Boundary Condition File](https://adcirc.org/home/documentation/users-manual-v53/input-file-descriptions/model-parameter-and-periodic-boundary-condition-file-fort-15). Phases must be in degrees. Amplitudes must be in units compatible with the units of gravity. These values are modified by the nodal factor and equilibrium argument provided for the tidal potential terms.` (408); `The basic file structure is shown below. Each line of input data is represented by a line containing the input variable name(s) in bold face type. Blank lines are only to enhance readability. Loops indicate multiple lines of input. Definitions of each variable are provided via hot links.` (410). |
| 412–429 | 입력 파일 구조 — k 반복문 안에 Alpha line, Constituent frequency, 1, Constituent name을 차례로 둔다(412–420). 안쪽 j 반복문은 JN, SALTAMP(k,JN), SALTPHA(k,JN)을 한 줄에 둔다(422–424). 원문 입력 줄·반복 상한·반복 종료와 빈 줄을 포함한다(412–429). 원문: `for k=1,[NTIF](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#NTIF)` (412); `Alpha line` (414); `Constituent frequency` (416); `1` (418); `Constituent name (e.g., M2)` (420); `for j=1,[NP](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#NP)` (422); `**[JN](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#JN)**, **[SALTAMP(k,JN)](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#SALTAMP)**, **[SALTPHA(k,JN)](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#SALTPHA)**` (424); `end j loop` (426); `end k loop` (428). |
| 430–433 | Note / 필수 헤더 줄 — 각 분조의 처음 네 줄은 파일에 반드시 있어야 한다(432). ADCIRC는 읽을 때 이 네 줄을 건너뛴다고 적는다(432). 의무와 읽기 동작을 함께 담은 문장을 그대로 옮긴다. 원문: `**Note:**` (430); `The first four lines (Alpha line, Constituent frequency, 1, Constituent name) for each constituent must be present in the file but they are skipped over during the ADCIRC read.` (432). |
| 434–448 | 웹페이지 끝 코드 — 빈 줄과 화면 유틸리티 호출이 있다(434–436). 링크 사전 가져오기(prefetch), 쿠키 안내 설정, 슬라이더 표시 보조 코드와 New Relic 페이지 정보가 이어진다(438–448). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 412·422: 반복 상한 `NTIF`와 `NP`의 정의를 외부 매개변수 페이지로 연결한다. 이 파일 본문에는 두 이름의 별도 정의가 없다.
- 166·202·300·368·370·374·375·387·389: CSS의 이미지 경로 3개와 탐색 메뉴의 사진 링크 6개에 대해 그림 파일 없음. `models/ADCIRC/raw/manuals/website_markdown/` 아래에서 해당 로컬 이미지 사본을 찾지 못했다.
