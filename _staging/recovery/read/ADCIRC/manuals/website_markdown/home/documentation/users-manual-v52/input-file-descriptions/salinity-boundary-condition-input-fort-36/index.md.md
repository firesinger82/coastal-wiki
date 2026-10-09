---
file: models/ADCIRC/raw/manuals/website_markdown/home/documentation/users-manual-v52/input-file-descriptions/salinity-boundary-condition-input-fort-36/index.md
lines: 432
sha256: 0aa195251a4689f842f4b71a313b979198bff2355c24bffad5d9a2229af94358
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# index.md — 판독 구간 기록

1–432행을 순서대로 읽었다. 아래 구간은 빈 줄·마크업·스크립트를 포함하며 앞 구간의 다음 행부터 이어진다.

| 구간 | 내용 |
| --- | --- |
| 1–12 | 웹 페이지 감시: New Relic 설정과 브라우저 로더(browser loader)가 있다(1–2). 뒤에는 빈 줄이 있다(3–12). |
| 13–77 | 페이지 스타일시트(CSS): 검색 필드(search field)와 경로 탐색(breadcrumbs), 페이지 머리말(header), 본문(body), 전체 컨테이너(container), 태그(tag), 오른쪽 내용 영역의 배치를 지정한다(13–77). |
| 78–150 | 내용 배치 스타일: 한 열 배치, 문단·링크, 경로 탐색, 문맥 메뉴(context navigation), 인용문(blockquote), 소제목, 왼쪽·오른쪽 내용 영역과 탐색 영역의 스타일이 있다(78–150). |
| 151–230 | 탐색 메뉴(navigation menu) 스타일: 메뉴 목록, 하위 메뉴, 포인터가 올라간 항목, 현재 항목, 태그 표시와 이미지 크기의 스타일이 있다(151–230). 배경 그림 두 개를 참조한다(166·202). 두 로컬 그림 파일 없음. 원문: `background:url(images/primary\_nav\_divider.gif) repeat-y scroll right bottom;` (166); `background: #76a3de url(images/primary\_nav\_bg\_repeat\_on.gif) repeat-x top;` (202). |
| 231–239 | 페이지 제목과 메타데이터(metadata): 페이지 제목(230)과 JSON-LD 형식의 웹 페이지·사이트·경로 탐색 정보(235)가 있다. 공개 시각, 수정 시각, 언어와 검색 동작도 포함한다(235). 사이의 빈 줄도 포함한다. |
| 240–267 | 이모지(emoji)와 WordPress 스타일: 이모지 설정·실행 스크립트가 있다(240–244). 이모지 이미지 스타일(247–257)과 자동 생성 버튼·미리 정의된 스타일(260–267)이 있다. |
| 268–301 | 관리·방문 통계·배경 스타일: 빈 줄, 관리자 표시줄 스타일(284–286), Beehive 방문 통계 스크립트(290–296)가 있다. 페이지 배경 그림을 참조한다(298). 해당 로컬 그림 파일 없음. 원문: `body.custom-background { background-color: #ffffff; background-image: url("https://adcirc.org/wp-content/uploads/sites/2255/2013/03/grid\_bkgrd\_lt\_grey1.jpg"); background-position: left top; background-size: auto; background-repeat: repeat-y; background-attachment: scroll; }` (298). |
| 302–359 | 사이트 머리말과 메뉴: ADCIRC 사이트명(304), 공식 사이트 문구(306), 탐색 건너뛰기 링크(308)가 있다. 커뮤니티 메뉴(310–320), 문서·매뉴얼·보고서 메뉴(321–356), 관련 소프트웨어 메뉴(357–359)가 이어진다. |
| 360–399 | 소식·제품 메뉴: 소식과 워크숍 메뉴(360–391), 제품 메뉴(392–397), ASGS 링크(398)가 있다. 사진 링크는 `ADCIRC2018_Group_Photo2.jpg` (366); `2017ADCIRCUGMGroupPhoto.jpg` (368); `160506-A-Y1769-008-A-1.jpg` (372); `adcircBootCampers2016_small_caption.jpg` (373); `2011_ADCIRC_meeting.jpg` (385); `ADCIRC_Workshop2010_GroupPhoto2.png` (387)이다. 각 링크에 대응하는 로컬 그림 파일 없음. |
| 400–401 | 본문 경로 탐색: Home, Documentation, User’s Manual – v52, Input File Descriptions와 현재 문서명이 이어진다(400). 다음 빈 줄도 포함한다(401). |
| 402–405 | 염분 경계 조건(salinity boundary condition) 입력 파일의 적용 조건: fort.15의 RES_BC_FLAG가 문서에 나열된 값일 때 fort.36을 읽는다(402·404). 원문: `The ADCIRC Salinity Boundary Condition Input File (fort.36) is read in when the [**RES\_BC\_FLAG**](https://adcirc.org/home/documentation/users-manual-v52/parameter-definitions#RES_BC_FLAG) is set to -2, 2, -4, or 4 in the [fort.15 file](../model-parameter-and-periodic-boundary-condition-file-fort-15/ "Model Parameter and Periodic Boundary Condition File (fort.15)").` (404). |
| 406–416 | 입력 형식: 데이터 집합(dataset) 반복문 안에 날짜 주석 행을 둔다(406·408). 해양 경계 절점(ocean boundary node) 반복문 안에 절점 번호와 SALBC(k,m) 값을 둔다(410–416). 원문: `for i=1 to numberOfDataSets` (406); `**comment line (date)**` (408); `for k=1 to number\_of\_ocean\_boundary\_nodes` (410); `k, (**SALBC(k,m)**, m=1,NFEN)` (412); `end k loop` (414); `end i loop` (416). |
| 417–432 | 페이지 후속 스크립트와 빈 줄: 유틸리티 표시 함수(420), 링크 미리 가져오기(prefetch) 설정(422), 쿠키(cookie) 배너 설정과 마크업(425–427), Soliloquy의 no-js 클래스 제거(431), New Relic 페이지 측정 정보(432)가 있다. |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 166·202·298·366·368·372·373·385·387행: 페이지 배경 그림 참조 세 개와 메뉴의 사진 링크 여섯 개에 대응하는 로컬 그림 파일 없음. 로컬 원문 사본 디렉터리인 models/ADCIRC/raw/manuals에서 해당 그림 파일을 찾지 못했다.
- 406·410·412행: 반복 상한인 `numberOfDataSets`, `number\_of\_ocean\_boundary\_nodes`, `NFEN`의 정의는 이 파일 본문에 없다.
