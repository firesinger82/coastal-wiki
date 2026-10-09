---
file: models/ADCIRC/raw/manuals/website_markdown/home/documentation/users-manual-v50/input-file-descriptions/salinity-boundary-condition-input-fort-36/index.md
lines: 433
sha256: 2c6229ea71824f45a37b39576d77c2ecb44617e1b503f19e1b3176c545b92585
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# salinity-boundary-condition-input-fort-36/index.md — 판독 구간 기록

구간은 1행부터 433행까지 빈틈없이 이어진다.
그림 로컬 사본의 파일명 검색 범위는 `models/ADCIRC/raw/manuals`이다.

| 구간 | 내용 |
|---|---|
| 1–12 | 웹 페이지 시작부 — New Relic의 브라우저 계측 초기화와 압축된 JavaScript를 포함한다(1–2). 뒤 빈 줄을 포함한다(3–12). |
| 13–77 | 페이지 스타일(CSS) / 검색·헤더·컨테이너 — 검색 필드와 버튼, 본문 글꼴·색, 헤더와 콘텐츠 영역의 배치·크기를 지정한다(13–77). |
| 78–142 | 페이지 스타일(CSS) / 콘텐츠·경로 표시 — 한 열 레이아웃, 콘텐츠 영역과 문단·링크, 경로 표시(breadcrumbs), 활성 메뉴와 인용문의 스타일을 지정한다(78–142). |
| 143–200 | 페이지 스타일(CSS) / 탐색 메뉴 — 메뉴 영역과 항목, 중첩 메뉴와 링크의 배치를 지정한다(143–200). `images/primary\_nav\_divider.gif`를 배경으로 참조한다(166). 이 참조의 로컬 사본은 그림 파일 없음. |
| 201–230 | 페이지 스타일(CSS) / 메뉴 상태·이미지 크기 — 마우스를 올린 메뉴와 현재 페이지 항목의 스타일, 콘텐츠 높이와 이미지의 고유 크기 처리를 지정한다(201–230). `images/primary\_nav\_bg\_repeat\_on.gif`를 배경으로 참조한다(202). 이 참조의 로컬 사본은 그림 파일 없음. |
| 231–240 | 페이지 제목·구조화 메타데이터 — 페이지 제목을 적는다(232). WebPage, BreadcrumbList, WebSite의 URL·발행일·수정일·언어·검색 설정을 JSON으로 포함한다(235). 빈 줄도 포함한다. 원문: `Salinity Boundary Condition Input (fort.36) - ADCIRC` (232). |
| 241–268 | WordPress 표시 코드 — 이모지(emoji) 지원 검사와 표시 설정, 자동 생성된 버튼·색·그라데이션·글자 크기·간격·그림자·배치 스타일을 포함한다(241–268). |
| 269–302 | 관리·방문 분석·배경 — 빈 줄과 관리자 표시 스타일을 포함한다(269–287). 방문 분석 스크립트와 페이지 배경 설정을 포함한다(291–299). 배경 이미지 `grid\_bkgrd\_lt\_grey1.jpg`의 로컬 사본은 그림 파일 없음(299). |
| 303–310 | 사이트 헤더 — 빈 제목 마크업, ADCIRC 링크, 공식 웹 사이트 표제와 탐색 건너뛰기 링크를 포함한다(303–310). |
| 311–321 | Community — 개발 그룹·협력 기관·사용자 안내의 탐색 링크를 열거한다(311–321). |
| 322–357 | Documentation — V50–v53의 입력·출력·버전 이력, 컴파일·명령행 옵션, FAQ, 예제, 보고서·발행물·특수 기능·하위 영역 모델링 안내 링크를 열거한다(322–357). |
| 358–360 | Related software — ADCIRC 유틸리티와 SMS 격자 생성기(grid generator)의 안내 링크를 포함한다(358–360). |
| 361–392 | News — 사용자 모임·부트캠프·워크숍·예측·시뮬레이션의 탐색 링크를 열거한다(361–392). 직접 사진 파일로 연결되는 링크는 `ADCIRC2018_Group_Photo2.jpg` (367), `2017ADCIRCUGMGroupPhoto.jpg` (369), `160506-A-Y1769-008-A-1.jpg` (373), `adcircBootCampers2016_small_caption.jpg` (374), `2011_ADCIRC_meeting.jpg` (386), `ADCIRC_Workshop2010_GroupPhoto2.png` (388)이다. 각 링크의 로컬 사본은 그림 파일 없음. |
| 393–400 | Products·ASGS — 조석 데이터베이스(tidal databases)·발행물·격자·폭풍해일 안내·허리케인 중 표면유 이동과 ASGS의 탐색 링크를 포함한다(393–399). 뒤 빈 줄을 포함한다(400). |
| 401–402 | 본문 앞 경로 표시 — Home, Documentation, User’s Manual – V50, Input File Descriptions와 현재 페이지 제목을 표시한다(401). 뒤 빈 줄을 포함한다(402). |
| 403–406 | Salinity Boundary Condition Input (fort.36) / 읽기 조건 — fort.15에서 `RES\_BC\_FLAG`가 -2, 2, -4 또는 4로 설정되어 있을 때 염분 경계 조건(salinity boundary condition) 파일 fort.36을 읽는다(405). 원문: `The ADCIRC Salinity Boundary Condition Input File (fort.36) is read in when the [**RES\_BC\_FLAG**](../../parameter-definitions#RES_BC_FLAG) is set to -2, 2, -4, or 4 in the [fort.15 file](https://adcirc.org/home/documentation/users-manual-v50/input-file-descriptions/model-parameter-and-periodic-boundary-condition-file-fort-15/ "Model Parameter and Periodic Boundary Condition File (fort.15)").` (405). |
| 407–418 | fort.36 / 입력 구조 — 각 자료 집합의 i 반복문에서 날짜 주석 줄을 쓴다(407–409). 해양 경계 절점(ocean boundary nodes)의 k 반복문에서 k와 `SALBC(k,m)`의 m=1,NFEN 목록을 쓴다(411–415). 바깥 반복문 종료도 포함한다(417). 값의 단위·기본값과 자료 집합의 시간 간격은 이 본문에 없다(405–417). 원문: `for i=1 to numberOfDataSets` (407); `**comment line (date)**` (409); `for k=1 to number\_of\_ocean\_boundary\_nodes` (411); `k, (**SALBC(k,m)**, m=1,NFEN)` (413); `end k loop` (415); `end i loop` (417). |
| 419–433 | 페이지 끝 스크립트·빈 줄 — 유틸리티 표시, 사전 가져오기(prefetch) 규칙, 쿠키 배너(cookie banner), 슬라이드쇼 상태와 New Relic 요청 정보를 포함한다(419–433). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 166행: CSS 메뉴 구분 배경가 `images/primary\_nav\_divider.gif`를 참조한다. 로컬 사본은 그림 파일 없음. `models/ADCIRC/raw/manuals`의 파일명 목록에서 찾지 못해 열지 못했다.
- 202행: CSS 메뉴 상태 배경가 `images/primary\_nav\_bg\_repeat\_on.gif`를 참조한다. 로컬 사본은 그림 파일 없음. `models/ADCIRC/raw/manuals`의 파일명 목록에서 찾지 못해 열지 못했다.
- 299행: CSS 페이지 배경가 `grid\_bkgrd\_lt\_grey1.jpg`를 참조한다. 로컬 사본은 그림 파일 없음. `models/ADCIRC/raw/manuals`의 파일명 목록에서 찾지 못해 열지 못했다.
- 367행: 메뉴의 2018 모임 사진 링크가 `ADCIRC2018_Group_Photo2.jpg`를 참조한다. 로컬 사본은 그림 파일 없음. `models/ADCIRC/raw/manuals`의 파일명 목록에서 찾지 못해 열지 못했다.
- 369행: 메뉴의 2017 모임 사진 링크가 `2017ADCIRCUGMGroupPhoto.jpg`를 참조한다. 로컬 사본은 그림 파일 없음. `models/ADCIRC/raw/manuals`의 파일명 목록에서 찾지 못해 열지 못했다.
- 373행: 메뉴의 2016 모임 사진 링크가 `160506-A-Y1769-008-A-1.jpg`를 참조한다. 로컬 사본은 그림 파일 없음. `models/ADCIRC/raw/manuals`의 파일명 목록에서 찾지 못해 열지 못했다.
- 374행: 메뉴의 2016 부트캠프 사진 링크가 `adcircBootCampers2016_small_caption.jpg`를 참조한다. 로컬 사본은 그림 파일 없음. `models/ADCIRC/raw/manuals`의 파일명 목록에서 찾지 못해 열지 못했다.
- 386행: 메뉴의 2011 워크숍 사진 링크가 `2011_ADCIRC_meeting.jpg`를 참조한다. 로컬 사본은 그림 파일 없음. `models/ADCIRC/raw/manuals`의 파일명 목록에서 찾지 못해 열지 못했다.
- 388행: 메뉴의 2010 워크숍 사진 링크가 `ADCIRC_Workshop2010_GroupPhoto2.png`를 참조한다. 로컬 사본은 그림 파일 없음. `models/ADCIRC/raw/manuals`의 파일명 목록에서 찾지 못해 열지 못했다.
- 407·411·413행: `numberOfDataSets`, `number\_of\_ocean\_boundary\_nodes`, `NFEN`과 `SALBC(k,m)`의 정의는 이 본문에 없다. 405행의 `RES\_BC\_FLAG` 정의 링크 대상은 이번 판독에서 읽지 않았다.
