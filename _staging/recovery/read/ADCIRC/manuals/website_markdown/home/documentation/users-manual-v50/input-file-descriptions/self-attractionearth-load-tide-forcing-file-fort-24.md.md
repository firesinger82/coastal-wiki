---
file: models/ADCIRC/raw/manuals/website_markdown/home/documentation/users-manual-v50/input-file-descriptions/self-attractionearth-load-tide-forcing-file-fort-24.md
lines: 449
sha256: ba1d1e14dd89afa3d30e25bf50ba5aa6cc04ac2ba633804a2344269807a10127
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# self-attractionearth-load-tide-forcing-file-fort-24.md — 판독 구간 기록

구간은 1행부터 449행까지 빈틈없이 이어진다.
그림 로컬 사본의 파일명 검색 범위는 `models/ADCIRC/raw/manuals`이다.

| 구간 | 내용 |
|---|---|
| 1–12 | 웹 페이지 시작부 — New Relic의 브라우저 계측 초기화와 압축된 JavaScript를 포함한다(1–2). 뒤 빈 줄을 포함한다(3–12). |
| 13–77 | 페이지 스타일(CSS) / 검색·헤더·컨테이너 — 검색 필드와 버튼, 본문 글꼴·색, 헤더와 콘텐츠 영역의 배치·크기를 지정한다(13–77). |
| 78–142 | 페이지 스타일(CSS) / 콘텐츠·경로 표시 — 한 열 레이아웃, 콘텐츠 영역과 문단·링크, 경로 표시(breadcrumbs), 활성 메뉴와 인용문의 스타일을 지정한다(78–142). |
| 143–200 | 페이지 스타일(CSS) / 탐색 메뉴 — 메뉴 영역과 항목, 중첩 메뉴와 링크의 배치를 지정한다(143–200). `images/primary\_nav\_divider.gif`를 배경으로 참조한다(166). 이 참조의 로컬 사본은 그림 파일 없음. |
| 201–230 | 페이지 스타일(CSS) / 메뉴 상태·이미지 크기 — 마우스를 올린 메뉴와 현재 페이지 항목의 스타일, 콘텐츠 높이와 이미지의 고유 크기 처리를 지정한다(201–230). `images/primary\_nav\_bg\_repeat\_on.gif`를 배경으로 참조한다(202). 이 참조의 로컬 사본은 그림 파일 없음. |
| 231–242 | 페이지 제목·구조화 메타데이터 — 페이지 제목을 적는다(232). WebPage, BreadcrumbList, WebSite의 URL·발행일·수정일·언어·검색 설정을 JSON으로 포함한다(237). 빈 줄도 포함한다. 원문: `Self Attraction/Earth Load Tide Forcing File (fort.24) - ADCIRC` (232). |
| 243–270 | WordPress 표시 코드 — 이모지(emoji) 지원 검사와 표시 설정, 자동 생성된 버튼·색·그라데이션·글자 크기·간격·그림자·배치 스타일을 포함한다(243–270). |
| 271–304 | 관리·방문 분석·배경 — 빈 줄과 관리자 표시 스타일을 포함한다(271–289). 방문 분석 스크립트와 페이지 배경 설정을 포함한다(293–301). 배경 이미지 `grid\_bkgrd\_lt\_grey1.jpg`의 로컬 사본은 그림 파일 없음(301). |
| 305–312 | 사이트 헤더 — 빈 제목 마크업, ADCIRC 링크, 공식 웹 사이트 표제와 탐색 건너뛰기 링크를 포함한다(305–312). |
| 313–323 | Community — 개발 그룹·협력 기관·사용자 안내의 탐색 링크를 열거한다(313–323). |
| 324–359 | Documentation — V50–v53의 입력·출력·버전 이력, 컴파일·명령행 옵션, FAQ, 예제, 보고서·발행물·특수 기능·하위 영역 모델링 안내 링크를 열거한다(324–359). |
| 360–362 | Related software — ADCIRC 유틸리티와 SMS 격자 생성기(grid generator)의 안내 링크를 포함한다(360–362). |
| 363–394 | News — 사용자 모임·부트캠프·워크숍·예측·시뮬레이션의 탐색 링크를 열거한다(363–394). 직접 사진 파일로 연결되는 링크는 `ADCIRC2018_Group_Photo2.jpg` (369), `2017ADCIRCUGMGroupPhoto.jpg` (371), `160506-A-Y1769-008-A-1.jpg` (375), `adcircBootCampers2016_small_caption.jpg` (376), `2011_ADCIRC_meeting.jpg` (388), `ADCIRC_Workshop2010_GroupPhoto2.png` (390)이다. 각 링크의 로컬 사본은 그림 파일 없음. |
| 395–402 | Products·ASGS — 조석 데이터베이스(tidal databases)·발행물·격자·폭풍해일 안내·허리케인 중 표면유 이동과 ASGS의 탐색 링크를 포함한다(395–401). 뒤 빈 줄을 포함한다(402). |
| 403–404 | 본문 앞 경로 표시 — Home, Documentation, User’s Manual – V50, Input File Descriptions와 현재 페이지 제목을 표시한다(403). 뒤 빈 줄을 포함한다(404). |
| 405–412 | Self Attraction/Earth Load Tide Forcing File (fort.24) / 적용·형식 — fort.15의 `NTIP=2`일 때 자기 인력/지구 하중 조석(self attraction/earth load tides)을 ADCIRC 강제력(forcing)으로 사용한다(407). 속도 정보가 없는 “tea” 조화 형식(harmonic format)과 같다고 적는다(409). 항목은 분조(constituents)별로 묶어 조석 퍼텐셜(tidal potential) 항과 같은 순서로 둬야 한다(409). 위상(phases)은 도 단위여야 한다(409). 진폭(amplitudes)은 중력(gravity) 단위와 호환되어야 한다(409). 값은 절점 계수(nodal factor)와 평형 인수(equilibrium argument)로 수정된다고 적는다(409). 입력 한 줄과 굵은 변수 줄, 가독성용 빈 줄, 반복문과 변수 정의 링크의 관계를 설명한다(411). 원문: `Self attraction/earth load tides are used to force ADCIRC when [NTIP](../../parameter-definitions#NTIP)=2 in the [Model Parameter and Periodic Boundary Condition File](../model-parameter-and-periodic-boundary-condition-file-fort-15).` (407); `The format of this file is identical to the “tea” harmonic format with no velocity information included. Entries are grouped by constituents and must be in the same order as the tidal potential terms listed in the [Model Parameter and Periodic Boundary Condition File](http://adcirc.org/home/documentation/users-manual-v50/input-file-descriptions/model-parameter-and-periodic-boundary-condition-file-fort-15). Phases must be in degrees. Amplitudes must be in units compatible with the units of gravity. These values are modified by the nodal factor and equilibrium argument provided for the tidal potential terms.` (409); `The basic file structure is shown below. Each line of input data is represented by a line containing the input variable name(s) in bold face type. Blank lines are only to enhance readability. Loops indicate multiple lines of input. Definitions of each variable are provided via hot links.` (411). |
| 413–430 | fort.24 / 분조별 입력 구조 — k를 1부터 `NTIF`까지 반복한다(413). 각 분조에 Alpha line, Constituent frequency, `1`, Constituent name을 둔다(415–421). j를 1부터 `NP`까지 반복하며 `JN`, `SALTAMP(k,JN)`, `SALTPHA(k,JN)`을 입력한다(423–427). 바깥 반복문 종료도 포함한다(429). 기본값은 이 본문에 없다(407–433). 원문: `for k=1,[NTIF](../../parameter-definitions#NTIF)` (413); `Alpha line` (415); `Constituent frequency` (417); `1` (419); `Constituent name (e.g., M2)` (421); `for j=1,[NP](../../parameter-definitions#NP)` (423); `**[JN](../../parameter-definitions#JN)**, **[SALTAMP(k,JN)](../../parameter-definitions#SALTAMP)**, **[SALTPHA(k,JN)](../../parameter-definitions#SALTPHA)**` (425); `end j loop` (427); `end k loop` (429). |
| 431–434 | Note / 필수 헤더 네 줄 — 각 분조의 첫 네 줄은 파일에 반드시 있어야 한다(433). ADCIRC는 읽기 과정에서 이 네 줄을 건너뛴다(433). 원문: `**Note:**` (431); `The first four lines (Alpha line, Constituent frequency, 1, Constituent name) for each constituent must be present in the file but they are skipped over during the ADCIRC read.` (433). |
| 435–449 | 페이지 끝 스크립트·빈 줄 — 유틸리티 표시, 사전 가져오기(prefetch) 규칙, 쿠키 배너(cookie banner), 슬라이드쇼 상태와 New Relic 요청 정보를 포함한다(435–449). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 166행: CSS 메뉴 구분 배경가 `images/primary\_nav\_divider.gif`를 참조한다. 로컬 사본은 그림 파일 없음. `models/ADCIRC/raw/manuals`의 파일명 목록에서 찾지 못해 열지 못했다.
- 202행: CSS 메뉴 상태 배경가 `images/primary\_nav\_bg\_repeat\_on.gif`를 참조한다. 로컬 사본은 그림 파일 없음. `models/ADCIRC/raw/manuals`의 파일명 목록에서 찾지 못해 열지 못했다.
- 301행: CSS 페이지 배경가 `grid\_bkgrd\_lt\_grey1.jpg`를 참조한다. 로컬 사본은 그림 파일 없음. `models/ADCIRC/raw/manuals`의 파일명 목록에서 찾지 못해 열지 못했다.
- 369행: 메뉴의 2018 모임 사진 링크가 `ADCIRC2018_Group_Photo2.jpg`를 참조한다. 로컬 사본은 그림 파일 없음. `models/ADCIRC/raw/manuals`의 파일명 목록에서 찾지 못해 열지 못했다.
- 371행: 메뉴의 2017 모임 사진 링크가 `2017ADCIRCUGMGroupPhoto.jpg`를 참조한다. 로컬 사본은 그림 파일 없음. `models/ADCIRC/raw/manuals`의 파일명 목록에서 찾지 못해 열지 못했다.
- 375행: 메뉴의 2016 모임 사진 링크가 `160506-A-Y1769-008-A-1.jpg`를 참조한다. 로컬 사본은 그림 파일 없음. `models/ADCIRC/raw/manuals`의 파일명 목록에서 찾지 못해 열지 못했다.
- 376행: 메뉴의 2016 부트캠프 사진 링크가 `adcircBootCampers2016_small_caption.jpg`를 참조한다. 로컬 사본은 그림 파일 없음. `models/ADCIRC/raw/manuals`의 파일명 목록에서 찾지 못해 열지 못했다.
- 388행: 메뉴의 2011 워크숍 사진 링크가 `2011_ADCIRC_meeting.jpg`를 참조한다. 로컬 사본은 그림 파일 없음. `models/ADCIRC/raw/manuals`의 파일명 목록에서 찾지 못해 열지 못했다.
- 390행: 메뉴의 2010 워크숍 사진 링크가 `ADCIRC_Workshop2010_GroupPhoto2.png`를 참조한다. 로컬 사본은 그림 파일 없음. `models/ADCIRC/raw/manuals`의 파일명 목록에서 찾지 못해 열지 못했다.
- 413·423·425행: `NTIF`, `NP`, `JN`, `SALTAMP(k,JN)`, `SALTPHA(k,JN)`의 정의는 이 본문에 없다. 이름은 별도 매개변수 정의 링크로 연결된다. 링크 대상 문서는 이번 판독에서 읽지 않았다.
