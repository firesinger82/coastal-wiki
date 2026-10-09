---
file: models/ADCIRC/raw/manuals/website_markdown/home/documentation/users-manual-v50/output-file-descriptions/elevation-time-series-at-all-nodes-in-the-model-grid-fort-63.md
lines: 443
sha256: 95bf1dadff5e1a12782f57ba6fd04dd5a42f036bbd519aea86034a469be997f8
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# elevation-time-series-at-all-nodes-in-the-model-grid-fort-63.md — 판독 구간 기록

구간은 1행부터 443행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–12 | 페이지 계측 코드 — New Relic의 초기 설정과 브라우저 계측용 JavaScript 코드가 들어 있다(1–2). 3–12행은 빈 줄이다. |
| 13–77 | 페이지 CSS / 검색·머리말·배치 — 검색 필드와 버튼, 제목과 본문 글꼴, 링크 색상, 컨테이너와 머리말 및 콘텐츠 영역의 표시 규칙을 적는다(13–77). |
| 78–134 | 페이지 CSS / 콘텐츠·링크·이동 경로 — 한 열 콘텐츠 영역, 문단과 링크, 이동 경로(breadcrumb), 선택된 메뉴와 인용문 표시 규칙을 적는다(78–134). |
| 135–200 | 페이지 CSS / 메뉴 배치 — 제목과 콘텐츠 영역, 상위 메뉴와 하위 메뉴의 크기·색상·위치를 적는다(135–200). 메뉴 구분선 배경 `images/primary\_nav\_divider.gif`를 참조한다(166). 해당 로컬 그림 파일 없음. |
| 201–230 | 페이지 CSS / 메뉴 상태·이미지 크기 — 메뉴 위에 포인터를 놓았을 때와 현재 페이지 메뉴의 표시 규칙을 적는다(201–225). 기타 표시 규칙과 이미지의 고유 크기 설정을 포함한다(226–230). 메뉴 배경 `images/primary\_nav\_bg\_repeat\_on.gif`를 참조한다(202). 해당 로컬 그림 파일 없음. |
| 231–242 | 페이지 제목·구조화 메타데이터 — 문서의 페이지 제목을 적는다(232). JSON-LD는 문서 URL과 이름, 게시·수정 시각, 이동 경로, 언어 및 사이트 검색 정보를 담는다(237). 사이와 뒤의 빈 줄을 포함한다(231·233–236·238–242). |
| 243–260 | WordPress 이모지 표시 — CDATA 표기와 이모지(emoji) 자산의 기본 URL, 지원 여부 검사 코드, 이모지 이미지용 CSS를 포함한다(243–260). |
| 261–286 | WordPress 공통 CSS — 버튼과 파일 링크의 표시 규칙을 적는다(263–264). 화면 비율·색상·그라데이션·글꼴·여백·그림자와 배치 규칙을 적는다(267–270). 앞뒤의 빈 줄을 포함한다(261–262·265–266·271–286). |
| 287–304 | 관리 표시·접속 계측·페이지 배경 — 관리 표시용 CSS와 Beehive 접속 계측 설정을 포함한다(287–299). 페이지 배경 이미지 `grid\_bkgrd\_lt\_grey1.jpg`를 참조한다(301). 해당 로컬 그림 파일 없음. 사이와 뒤의 빈 줄을 포함한다(290–292·300·302–304). |
| 305–359 | 사이트 머리말·Community·Documentation 메뉴 — 빈 제목 마크업과 사이트 제목 및 설명을 적는다(305–311). 개발자와 사용자, 매뉴얼 V50–V53, 컴파일·명령행 옵션, FAQ, 예제, 보고서와 출판물에 대한 메뉴 링크를 나열한다(313–359). |
| 360–402 | Related software·News·Products·ASGS 메뉴 — 관련 소프트웨어와 연도별 회의·워크숍, 예보와 예제, 조석 데이터베이스(tidal databases), 격자 및 ASGS 링크를 나열한다(360–401). 사진 링크는 `ADCIRC2018_Group_Photo2.jpg` (369), `2017ADCIRCUGMGroupPhoto.jpg` (371), `160506-A-Y1769-008-A-1.jpg` (375), `adcircBootCampers2016_small_caption.jpg` (376), `2011_ADCIRC_meeting.jpg` (388), `ADCIRC_Workshop2010_GroupPhoto2.png` (390)이다. 각 링크의 로컬 그림 파일 없음. 402행은 빈 줄이다. |
| 403–410 | Elevation Time Series at All Nodes in the Model Grid (fort.63) — 이동 경로와 제목을 적는다(403–405). 모델 격자(grid)의 모든 절점(nodes)에서 수위(elevation) 시계열(time series)을 출력한다고 설명하며 fort.15를 참조한다(407). 굵은 변수 이름은 출력 한 줄을 나타낸다(409). 빈 줄은 가독성을 위한 것이며 반복문은 여러 출력 줄을 나타낸다(409). 변수 정의는 링크로 제공한다고 적는다(409). 원문: `Elevation time series output at all nodes in the model grid as specified in the [Model Parameter and Periodic Boundary Condition File](../../input-file-descriptions/model-parameter-and-periodic-boundary-condition-file-fort-15).` (407). |
| 411–424 | fort.63 출력 형식 — `NOUTGE` 설정에 따른 ASCII 또는 이진(binary) 형식 조건을 적는다(411). 실행 식별 정보, 출력 헤더(header), 시각·시간 단계(time step)와 절점별 수위 변수의 출력 순서를 제시한다(413–423). 절점 반복 범위와 출력 간격 곱셈식은 원문을 그대로 옮긴다(415·419). 원문: `Output may be in ascii or binary format depending on how [NOUTGE](../../parameter-definitions#NOUTGE) is set in the [Model Parameter and Periodic Boundary Condition File](http://adcirc.org/home/documentation/users-manual-v50/input-file-descriptions/model-parameter-and-periodic-boundary-condition-file-fort-15)` (411); `[**RUNDES**](../../parameter-definitions#RUNDES), [**RUNID**](../../parameter-definitions#RUNID), [**AGRID**](../../parameter-definitions#AGRID)` (413); `[**NDSETSE**](../../parameter-definitions#NDSETSE), [**NP**](../../parameter-definitions#NP), **[DTDP](https://adcirc.org/home/documentation/users-manual-v50/parameter-definitions/#DTDP)\*[NSPOOLGE](../../parameter-definitions#NSPOOLGE)**, [**NSPOOLGE**](../../parameter-definitions#NSPOOLGE), [**IRTYPE**](../../parameter-definitions#IRTYPE)` (415); `[**TIME**](../../parameter-definitions#TIME), [**IT**](../../parameter-definitions#IT)` (417); `for k=1, [NP](../../parameter-definitions#NP)` (419); `**k**, [**ETA2(k)**](../../parameter-definitions#ETA2)` (421); `end k loop` (423). |
| 425–427 | Note / 이진 출력 조건 — 이진 출력을 지정하면 절점 번호 `k`를 출력에 포함하지 않는다고 적는다(427). 원문: `If binary output is specified, the node number (k) is not included in the output.` (427). |
| 428–443 | 페이지 후속 코드 — 빈 줄과 `show\_utility` 호출을 포함한다(428–431). 링크 사전 가져오기(prefetch) 설정과 쿠키 안내문 설정을 포함한다(433·436–438). jQuery 호출과 New Relic 계측 정보를 포함한다(442–443). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 166·202·301행: CSS가 참조하는 `primary_nav_divider.gif`, `primary_nav_bg_repeat_on.gif`, `grid_bkgrd_lt_grey1.jpg`의 로컬 그림 파일 없음. 문서 상대 경로와 URL 경로에 해당하는 폴더가 없으며 `models/ADCIRC/raw/manuals/`에서 파일명으로도 찾지 못했다.
- 369·371·375–376·388·390행: 메뉴 사진 링크의 `ADCIRC2018_Group_Photo2.jpg`, `2017ADCIRCUGMGroupPhoto.jpg`, `160506-A-Y1769-008-A-1.jpg`, `adcircBootCampers2016_small_caption.jpg`, `2011_ADCIRC_meeting.jpg`, `ADCIRC_Workshop2010_GroupPhoto2.png`의 로컬 그림 파일 없음. `models/ADCIRC/raw/manuals/`에서 각 파일명으로 찾지 못했다.
- 403행: 이동 경로에서 `[Home](https://adcirc.org)` 다음에 항목명 없이 `»  »`가 이어진다.
- 411·413–421행: `NOUTGE`와 출력 변수의 정의는 `parameter-definitions` 링크로 연결되어 있다. 변수의 기본값·단위·상세 정의는 이 파일 본문에 없다.
