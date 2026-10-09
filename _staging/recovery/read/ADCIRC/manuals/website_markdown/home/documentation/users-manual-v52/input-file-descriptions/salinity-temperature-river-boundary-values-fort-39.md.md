---
file: models/ADCIRC/raw/manuals/website_markdown/home/documentation/users-manual-v52/input-file-descriptions/salinity-temperature-river-boundary-values-fort-39.md
lines: 438
sha256: 8c5f2fcfcfe71ef89889ae65af9eca1b0e1ad002d454494f2d27ff37e94794dc
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# salinity-temperature-river-boundary-values-fort-39.md — 판독 구간 기록

1–438행을 순서대로 읽었다. 아래 구간은 빈 줄·마크업·스크립트를 포함하며 앞 구간의 다음 행부터 이어진다.

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
| 404–407 | 하천 염분·온도 경계값(salinity and temperature river boundary values) 파일의 적용 조건: fort.14에 경압 하천 경계(baroclinic river boundary)가 있고 IBTYPE=122이며 IDEN이 양수일 때 fort.39를 읽는다(404·406). 원문: `The salinity and temperature river boundary condition file (fort.39) is read in when the [mesh file (fort.14)](../adcirc-grid-and-boundary-information-file-fort-14/) contains a baroclinic river boundary ([**IBTYPE**](https://adcirc.org/home/documentation/users-manual-v52/parameter-definitions#IBTYPE)=122) and [**IDEN**](https://adcirc.org/home/documentation/users-manual-v52/parameter-definitions#IDEN) is positive.` (406). |
| 408–419 | 입력 형식: RIVBCTIMINC와 RIVBCSTATIM 다음에 데이터 집합과 하천 경계 절점(river boundary node)의 반복문을 둔다(408–412). 각 절점에 bc(j,k) 값의 반복 입력을 둔다(414–418). 원문의 굵은 글씨 마크업(markup)도 그대로 옮긴다(414). 원문: `**RIVBCTIMINC, RIVBCSTATIM**` (408); `for i=1 to numberOfDataSets` (410); `for j=1 to number\_of\_river\_boundary\_nodes` (412); `**(**bc(j,k)**, k=1,NFEN)**` (414); `end j loop` (416); `end i loop` (418). |
| 420–422 | 시간 변수와 IDEN별 경계값: RIVBCTIMINC는 경계 조건 데이터 집합 사이의 시간 간격이고 단위는 초이다(420). RIVBCSTATIM은 경계 조건 데이터 시작 시각이며 콜드 스타트(cold start) 시각을 기준으로 한 초 단위이다(420). IDEN=2이면 bc(j,k)에 염분 값을 사용하도록 안내한다(422). IDEN=3이면 온도 값을 사용하도록 안내한다(422). IDEN=4이면 bc(j,k)를 salbc(j,k),tempbc(j,k)로 바꾸도록 안내한다(422). 원문: `where RIVBCTIMINC is the time increment (in seconds) between the boundary condition datasets; RIVBCSTATIM is the time (in seconds) when the boundary condition data start, relative to the cold start time.` (420); `The bc(j,k) values depend on the value of [**IDEN**](https://adcirc.org/home/documentation/users-manual-v52/parameter-definitions#IDEN). If IDEN=2, then the salinity boundary condition values should be used for bc(j,k). If IDEN=3, then the temperature boundary condition values should be used for bc(j,k). If IDEN=4, then the bc(j,k) should be replaced with salbc(j,k),tempbc(j,k).` (422). |
| 423–438 | 페이지 후속 스크립트와 빈 줄: 유틸리티 표시 함수(426), 링크 미리 가져오기(prefetch) 설정(428), 쿠키(cookie) 배너 설정과 마크업(431–433), Soliloquy의 no-js 클래스 제거(437), New Relic 페이지 측정 정보(438)가 있다. |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 166·202·300·368·370·374·375·387·389행: 페이지 배경 그림 참조 세 개와 메뉴의 사진 링크 여섯 개에 대응하는 로컬 그림 파일 없음. 로컬 원문 사본 디렉터리인 models/ADCIRC/raw/manuals에서 해당 그림 파일을 찾지 못했다.
- 410·412·414행: 반복 상한인 `numberOfDataSets`, `number\_of\_river\_boundary\_nodes`, `NFEN`의 정의는 이 파일 본문에 없다.
- 406·422행: 파일을 읽는 조건은 `IDEN`이 양수인 경우로 제시한다(406). `bc(j,k)`의 선택 설명은 `IDEN=2`, `IDEN=3`, `IDEN=4`에 대해서만 제시한다(422).
