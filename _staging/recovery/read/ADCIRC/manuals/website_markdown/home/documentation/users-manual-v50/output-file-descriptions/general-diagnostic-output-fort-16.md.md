---
file: models/ADCIRC/raw/manuals/website_markdown/home/documentation/users-manual-v50/output-file-descriptions/general-diagnostic-output-fort-16.md
lines: 421
sha256: 0c2ce2073789befa0176e4ac2c2ee1038c1afb2c56a0dad03adba6863e8c1d28
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# general-diagnostic-output-fort-16.md — 판독 구간 기록

구간은 1행부터 421행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–12 | 페이지 계측 코드 — New Relic의 초기 설정과 브라우저 계측용 JavaScript 코드가 들어 있다(1–2). 3–12행은 빈 줄이다. |
| 13–77 | 페이지 CSS / 검색·머리말·배치 — 검색 필드와 버튼, 제목과 본문 글꼴, 링크 색상, 컨테이너와 머리말 및 콘텐츠 영역의 표시 규칙을 적는다(13–77). |
| 78–134 | 페이지 CSS / 콘텐츠·링크·이동 경로 — 한 열 콘텐츠 영역, 문단과 링크, 이동 경로(breadcrumb), 선택된 메뉴와 인용문 표시 규칙을 적는다(78–134). |
| 135–200 | 페이지 CSS / 메뉴 배치 — 제목과 콘텐츠 영역, 상위 메뉴와 하위 메뉴의 크기·색상·위치를 적는다(135–200). 메뉴 구분선 배경 `images/primary\_nav\_divider.gif`를 참조한다(166). 해당 로컬 그림 파일 없음. |
| 201–230 | 페이지 CSS / 메뉴 상태·이미지 크기 — 메뉴 위에 포인터를 놓았을 때와 현재 페이지 메뉴의 표시 규칙을 적는다(201–225). 기타 표시 규칙과 이미지의 고유 크기 설정을 포함한다(226–230). 메뉴 배경 `images/primary\_nav\_bg\_repeat\_on.gif`를 참조한다(202). 해당 로컬 그림 파일 없음. |
| 231–240 | 페이지 제목·구조화 메타데이터 — 문서의 페이지 제목을 적는다(232). JSON-LD는 문서 URL과 이름, 게시·수정 시각, 이동 경로, 언어 및 사이트 검색 정보를 담는다(235). 사이와 뒤의 빈 줄을 포함한다(231·233–234·236–240). |
| 241–258 | WordPress 이모지 표시 — CDATA 표기와 이모지(emoji) 자산의 기본 URL, 지원 여부 검사 코드, 이모지 이미지용 CSS를 포함한다(241–258). |
| 259–284 | WordPress 공통 CSS — 버튼과 파일 링크의 표시 규칙을 적는다(261–262). 화면 비율·색상·그라데이션·글꼴·여백·그림자와 배치 규칙을 적는다(265–268). 앞뒤의 빈 줄을 포함한다(259–260·263–264·269–284). |
| 285–302 | 관리 표시·접속 계측·페이지 배경 — 관리 표시용 CSS와 Beehive 접속 계측 설정을 포함한다(285–297). 페이지 배경 이미지 `grid\_bkgrd\_lt\_grey1.jpg`를 참조한다(299). 해당 로컬 그림 파일 없음. 사이와 뒤의 빈 줄을 포함한다(288–290·298·300–302). |
| 303–357 | 사이트 머리말·Community·Documentation 메뉴 — 빈 제목 마크업과 사이트 제목 및 설명을 적는다(303–309). 개발자와 사용자, 매뉴얼 V50–V53, 컴파일·명령행 옵션, FAQ, 예제, 보고서와 출판물에 대한 메뉴 링크를 나열한다(311–357). |
| 358–400 | Related software·News·Products·ASGS 메뉴 — 관련 소프트웨어와 연도별 회의·워크숍, 예보와 예제, 조석 데이터베이스(tidal databases), 격자 및 ASGS 링크를 나열한다(358–399). 사진 링크는 `ADCIRC2018_Group_Photo2.jpg` (367), `2017ADCIRCUGMGroupPhoto.jpg` (369), `160506-A-Y1769-008-A-1.jpg` (373), `adcircBootCampers2016_small_caption.jpg` (374), `2011_ADCIRC_meeting.jpg` (386), `ADCIRC_Workshop2010_GroupPhoto2.png` (388)이다. 각 링크의 로컬 그림 파일 없음. 400행은 빈 줄이다. |
| 401–406 | General Diagnostic Output (fort.16) — 이동 경로와 일반 진단 출력(general diagnostic output) 제목을 적는다(401–403). 격자 및 경계 정보(grid and boundary information) 파일 fort.14와 모델 매개변수 및 주기 경계조건(model parameter and periodic boundary condition) 파일 fort.15의 정보를 반복 출력(echo print)한다고 설명한다(405). 일부 처리된 정보와 ADCIRC의 오류 메시지도 출력한다고 설명한다(405). 원문: `Output file which echo prints information from the [Grid and Boundary Information File](../../input-file-descriptions/adcirc-grid-and-boundary-information-file-fort-14), the [Model Parameter and Periodic Boundary Condition File](../../input-file-descriptions/model-parameter-and-periodic-boundary-condition-file-fort-15), provides some processed information and prints out error messages from ADCIRC.` (405). |
| 407–421 | 페이지 후속 코드 — 빈 줄과 `show\_utility` 호출을 포함한다(407–409). 링크 사전 가져오기(prefetch) 설정과 쿠키 안내문 설정을 포함한다(411·414–416). jQuery 호출과 New Relic 계측 정보를 포함한다(420–421). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 166·202·299행: CSS가 참조하는 `primary_nav_divider.gif`, `primary_nav_bg_repeat_on.gif`, `grid_bkgrd_lt_grey1.jpg`의 로컬 그림 파일 없음. 문서 상대 경로와 URL 경로에 해당하는 폴더가 없으며 `models/ADCIRC/raw/manuals/`에서 파일명으로도 찾지 못했다.
- 367·369·373–374·386·388행: 메뉴 사진 링크의 `ADCIRC2018_Group_Photo2.jpg`, `2017ADCIRCUGMGroupPhoto.jpg`, `160506-A-Y1769-008-A-1.jpg`, `adcircBootCampers2016_small_caption.jpg`, `2011_ADCIRC_meeting.jpg`, `ADCIRC_Workshop2010_GroupPhoto2.png`의 로컬 그림 파일 없음. `models/ADCIRC/raw/manuals/`에서 각 파일명으로 찾지 못했다.
- 401행: 이동 경로에서 `[Home](https://adcirc.org)` 다음에 항목명 없이 `»  »`가 이어진다.
