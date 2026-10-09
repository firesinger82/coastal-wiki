---
file: models/ADCIRC/raw/manuals/website_markdown/home/documentation/users-manual-v53/input-file-descriptions/schedule-file/index.md
lines: 443
sha256: 790554bc613c6bce009f26acf0fc6e564ab9fd9c0e5059674c7b72c3c941db26
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# Schedule File — 판독 구간 기록

구간은 1행부터 443행까지 빈틈없이 이어진다.

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
| 402–407 | Schedule File / 입력 구성·적용 대상 — 위치 표시와 제목이 있다(402–404). 첫 줄은 보(weir) 높이 변경 기간 수 nSections를 지정한다(406). 이후 각 줄은 변경 기간의 시작·종료 시각과 기간 종료 시 보 높이 ZF를 포함한다(406). 높이 변경 동안 모든 보 높이를 시간에 대해 선형 보간(linear interpolation)한다고 적는다(406). Time Varying Weirs 입력 파일에서 이 일정 파일을 참조하는 모든 보 절점(node)에 전체 일정 파일을 적용한다(406). 원문: `The first line of the schedule file specifies the parameter nSections, the number of periods in the schedule where weir height should change. Each subsequent line specifies one section, which includes the starting and ending time of the period, and ZF, the weir height at the end of the period. All weir heights are interpolated linearly in time during the change in height. The entire schedule file applies to all weir nodes that reference the schedule file from within the Time Varying Weirs input file.` (406). |
| 408–419 | 시작·종료 시간 매개변수 — 각 줄에서 아래 시간 매개변수를 조합하여 일정 시작에 대한 보 높이 변경 기간의 시작·종료 시각을 지정한다(408). 시작 시각 4개와 종료 시각 4개의 이름·시간 기준·단위를 행마다 그대로 옮긴다(410–418). 빈 줄도 포함한다. 원문: `Use some combination of the following time parameters on each line to specify the start and end of the weir height change period, relative to the start of the schedule.` (408); `**TimeStartDay** – number of days since the beginning of the schedule when the weir height starts to change   ` (410); `**TimeStartHour** – number of hours since the beginning of the schedule when the weir height starts to change   ` (411); `**TimeStartMin** – number of minutes since the beginning of the schedule when the weir height starts to change   ` (412); `**TimeStartSec** – number of seconds since the beginning of the schedule when the weir height starts to change` (413); `**TimeEndDay** – number of days since the beginning of the schedule when the change in weir height is complete  ` (415); `**TimeEndHour** – number of hours since the beginning of the schedule when the change in weir height is complete  ` (416); `**TimeEndMin** – number of minutes since the beginning of the schedule when the change in weir height is complete  ` (417); `**TimeEndSec** – number of seconds since the beginning of the schedule when the change in weir height is complete` (418). |
| 420–428 | ZF·단축 값·Delta — ZF는 이번 변경 종료 시 보 표고(elevation)이다(420). 여러 보 절점에 한 일정 파일을 적용하기 위한 단축 값(shortcut value)들을 나열한다(422–425). Delta 사용 조건과 보의 현재 표고에 대한 처리도 그대로 옮긴다(427). 각 단축 값의 표기와 의미를 수정하지 않고 옮긴다. 원문: `**ZF** – The weir elevation at the end of this change. Generalized values are available to make it more convenient to apply a single schedule file to many weir nodes. These shortcut values are as follows` (420); `**-99990** – Make the final weir height equal to the mesh bathy/topo elevation at that node  ` (422); `**-99991** – Add a specified amount (specified elsewhere on this line as Delta) to the weir height  ` (423); `**-99992** – Subtract a specified amount (specified elsewhere on this line as Delta) from the weir height   ` (424); `–**99993** – Make the final weir height equal to the original weir height as specified in the fort.14 file (useful for ending a schedule file that will be repeated).` (425); `**Delta** – Add/Subtract this value from the current elevation of the weir when using -99991 or -99992 for ZF.` (427). |
| 429–443 | 웹페이지 끝 코드 — 빈 줄과 화면 유틸리티 호출이 있다(429–431). 링크 사전 가져오기(prefetch), 쿠키 안내 설정, 슬라이더 표시 보조 코드와 New Relic 페이지 정보가 이어진다(433–443). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 422–425: 앞 세 단축 값은 굵은 표시 안에 하이픈을 둔 `**-99990**`, `**-99991**`, `**-99992**`이다. 마지막 단축 값의 원문 표기는 굵은 표시 밖에 en dash를 둔 `–**99993**`이다(425).
- 420·427: 이 파일은 `ZF`와 `Delta`를 표고 및 표고 변화량으로 설명한다. 이 파일 본문에는 두 값의 길이 단위와 표고 기준면을 명시하지 않는다.
- 166·202·300·368·370·374·375·387·389: CSS의 이미지 경로 3개와 탐색 메뉴의 사진 링크 6개에 대해 그림 파일 없음. `models/ADCIRC/raw/manuals/website_markdown/` 아래에서 해당 로컬 이미지 사본을 찾지 못했다.
