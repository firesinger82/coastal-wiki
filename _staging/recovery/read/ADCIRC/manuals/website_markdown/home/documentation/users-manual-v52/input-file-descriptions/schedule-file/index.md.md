---
file: models/ADCIRC/raw/manuals/website_markdown/home/documentation/users-manual-v52/input-file-descriptions/schedule-file/index.md
lines: 443
sha256: 84c3cdeff14273af1ad9bc748ba8d7b04bb6ed9114f41b3f82a17e70557df3d2
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# index.md — 판독 구간 기록

1–443행을 순서대로 읽었다. 아래 구간은 빈 줄·마크업·스크립트를 포함하며 앞 구간의 다음 행부터 이어진다.

| 구간 | 내용 |
| --- | --- |
| 1–12 | 웹 페이지 감시: New Relic 설정과 브라우저 로더(browser loader)가 있다(1–2). 뒤에는 빈 줄이 있다(3–12). |
| 13–77 | 페이지 스타일시트(CSS): 검색 필드(search field)와 경로 탐색(breadcrumbs), 페이지 머리말(header), 본문(body), 전체 컨테이너(container), 태그(tag), 오른쪽 내용 영역의 배치를 지정한다(13–77). |
| 78–150 | 내용 배치 스타일: 한 열 배치, 문단·링크, 경로 탐색, 문맥 메뉴(context navigation), 인용문(blockquote), 소제목, 왼쪽·오른쪽 내용 영역과 탐색 영역의 스타일이 있다(78–150). |
| 151–230 | 탐색 메뉴(navigation menu) 스타일: 메뉴 목록, 하위 메뉴, 포인터가 올라간 항목, 현재 항목, 태그 표시와 이미지 크기의 스타일이 있다(151–230). 배경 그림 두 개를 참조한다(166·202). 두 로컬 그림 파일 없음. 원문: `background:url(images/primary\_nav\_divider.gif) repeat-y scroll right bottom;` (166); `background: #76a3de url(images/primary\_nav\_bg\_repeat\_on.gif) repeat-x top;` (202). |
| 231–241 | 페이지 제목과 메타데이터(metadata): 페이지 제목(232)과 JSON-LD 형식의 웹 페이지·사이트·경로 탐색 정보(237)가 있다. 공개 시각, 수정 시각, 언어와 검색 동작도 포함한다(237). 사이의 빈 줄도 포함한다. |
| 242–269 | 이모지(emoji)와 WordPress 스타일: 이모지 설정·실행 스크립트가 있다(242–246). 이모지 이미지 스타일(249–259)과 자동 생성 버튼·미리 정의된 스타일(262–269)이 있다. |
| 270–303 | 관리·방문 통계·배경 스타일: 빈 줄, 관리자 표시줄 스타일(286–288), Beehive 방문 통계 스크립트(292–298)가 있다. 페이지 배경 그림을 참조한다(300). 해당 로컬 그림 파일 없음. 원문: `body.custom-background { background-color: #ffffff; background-image: url("https://adcirc.org/wp-content/uploads/sites/2255/2013/03/grid\_bkgrd\_lt\_grey1.jpg"); background-position: left top; background-size: auto; background-repeat: repeat-y; background-attachment: scroll; }` (300). |
| 304–361 | 사이트 머리말과 메뉴: ADCIRC 사이트명(306), 공식 사이트 문구(308), 탐색 건너뛰기 링크(310)가 있다. 커뮤니티 메뉴(312–322), 문서·매뉴얼·보고서 메뉴(323–358), 관련 소프트웨어 메뉴(359–361)가 이어진다. |
| 362–401 | 소식·제품 메뉴: 소식과 워크숍 메뉴(362–393), 제품 메뉴(394–399), ASGS 링크(400)가 있다. 사진 링크는 `ADCIRC2018_Group_Photo2.jpg` (368); `2017ADCIRCUGMGroupPhoto.jpg` (370); `160506-A-Y1769-008-A-1.jpg` (374); `adcircBootCampers2016_small_caption.jpg` (375); `2011_ADCIRC_meeting.jpg` (387); `ADCIRC_Workshop2010_GroupPhoto2.png` (389)이다. 각 링크에 대응하는 로컬 그림 파일 없음. |
| 402–403 | 본문 경로 탐색: Home, Documentation, User’s Manual – v52, Input File Descriptions와 현재 문서명이 이어진다(402). 다음 빈 줄도 포함한다(403). |
| 404–407 | 보(weir) 높이 변경 일정 파일: 첫 행의 nSections는 높이가 변경되어야 하는 기간 수이다(404·406). 다음 각 행은 한 기간의 시작·종료 시각과 종료 높이 ZF를 지정한다(406). 변경 중 모든 보 높이는 시간에 따라 선형 보간(linear interpolation)한다(406). 파일 전체는 Time Varying Weirs 입력 파일에서 이 일정 파일을 참조하는 모든 보 절점에 적용한다(406). 원문: `The first line of the schedule file specifies the parameter nSections, the number of periods in the schedule where weir height should change. Each subsequent line specifies one section, which includes the starting and ending time of the period, and ZF, the weir height at the end of the period. All weir heights are interpolated linearly in time during the change in height. The entire schedule file applies to all weir nodes that reference the schedule file from within the Time Varying Weirs input file.` (406). |
| 408–419 | 시작·종료 시간 매개변수: 일정 시작을 기준으로 높이 변경 기간의 시작·종료를 지정한다(408). 다음 시간 매개변수 중 일부 조합을 각 행에 사용하라고 안내한다(408). 일·시·분·초 단위의 정의를 각각 옮긴다(410–418). 원문: `Use some combination of the following time parameters on each line to specify the start and end of the weir height change period, relative to the start of the schedule.` (408); `**TimeStartDay** – number of days since the beginning of the schedule when the weir height starts to change   ` (410); `**TimeStartHour** – number of hours since the beginning of the schedule when the weir height starts to change   ` (411); `**TimeStartMin** – number of minutes since the beginning of the schedule when the weir height starts to change   ` (412); `**TimeStartSec** – number of seconds since the beginning of the schedule when the weir height starts to change` (413); `**TimeEndDay** – number of days since the beginning of the schedule when the change in weir height is complete  ` (415); `**TimeEndHour** – number of hours since the beginning of the schedule when the change in weir height is complete  ` (416); `**TimeEndMin** – number of minutes since the beginning of the schedule when the change in weir height is complete  ` (417); `**TimeEndSec** – number of seconds since the beginning of the schedule when the change in weir height is complete` (418). |
| 420–427 | 종료 표고(weir elevation)와 변경량: ZF는 변경 종료 시 보 표고이다(420). 단축값별 높이 설정과 Delta 적용 조건을 옮긴다(422–427). 마지막 단축값은 원문 표기를 유지한다(425). 원문: `**ZF** – The weir elevation at the end of this change. Generalized values are available to make it more convenient to apply a single schedule file to many weir nodes. These shortcut values are as follows` (420); `**-99990** – Make the final weir height equal to the mesh bathy/topo elevation at that node  ` (422); `**-99991** – Add a specified amount (specified elsewhere on this line as Delta) to the weir height  ` (423); `**-99992** – Subtract a specified amount (specified elsewhere on this line as Delta) from the weir height   ` (424); `–**99993** – Make the final weir height equal to the original weir height as specified in the fort.14 file (useful for ending a schedule file that will be repeated).` (425); `**Delta** – Add/Subtract this value from the current elevation of the weir when using -99991 or -99992 for ZF.` (427). |
| 428–443 | 페이지 후속 스크립트와 빈 줄: 유틸리티 표시 함수(431), 링크 미리 가져오기(prefetch) 설정(433), 쿠키(cookie) 배너 설정과 마크업(436–438), Soliloquy의 no-js 클래스 제거(442), New Relic 페이지 측정 정보(443)가 있다. |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 166·202·300·368·370·374·375·387·389행: 페이지 배경 그림 참조 세 개와 메뉴의 사진 링크 여섯 개에 대응하는 로컬 그림 파일 없음. 로컬 원문 사본 디렉터리인 models/ADCIRC/raw/manuals에서 해당 그림 파일을 찾지 못했다.
- 422–425행: 앞의 세 단축값은 굵은 글씨 안에 ASCII 하이픈과 숫자를 둔다. 마지막 단축값은 굵은 글씨 밖에 en dash를 둔 `–**99993**`로 표기한다(425).
