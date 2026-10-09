---
file: models/ADCIRC/raw/manuals/website_markdown/home/documentation/users-manual-v51/output-file-descriptions/general-diagnostic-output-fort-16.md
lines: 464
sha256: 95db4b8148cc64d0f81ea262a160ad683e6fb817953a2cd37ca453be75bb78f8
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# general-diagnostic-output-fort-16.md — 판독 구간 기록

구간은 1행부터 464행까지 빈틈없이 이어진다.

내용 칸의 한국어 설명은 AI 판독 요약이다. 행 번호를 붙인 원문 인용은 백틱으로 구분한다.

| 구간 | 내용 |
|---|---|
| 1–12 | 웹 페이지 시작부 — New Relic의 브라우저 계측 초기화와 JavaScript 로더가 있다(1–2). 그 뒤에 빈 줄이 이어진다(3–12). |
| 13–77 | 페이지 스타일 — 스타일시트(Cascading Style Sheets, CSS)가 검색 입력란·검색 버튼·링크·본문·사이트 제목·전체 컨테이너·오른쪽 콘텐츠 영역의 글꼴, 색, 크기, 여백을 지정한다(13–77). |
| 78–142 | 본문과 탐색 경로 스타일 — 단일 열 콘텐츠, 본문 영역, 문단, 링크, 오른쪽 열 목록, 탐색 경로(breadcrumb), 활성 메뉴, 인용문, 두 열 콘텐츠의 표시 규칙이 있다(78–142). CSS 주석도 포함한다(78·86·90). |
| 143–200 | 주 메뉴와 하위 메뉴 스타일 — 메뉴 영역, 목록, 링크, 하위 메뉴의 위치와 표시 규칙을 지정한다(143–200). 메뉴 구분 배경 그림의 상대 경로가 있다(166). 원문: `background:url(images/primary\_nav\_divider.gif) repeat-y scroll right bottom;` (166). |
| 201–231 | 메뉴 상태와 이미지 표시 스타일 — 마우스를 올린 메뉴, 현재 페이지 메뉴, 구형 HTML 선택자의 표시 규칙이 있다(201–225). 메뉴 배경 그림의 상대 경로가 있다(202). 슬라이드 영역, 굵은 메뉴 글꼴, 숨긴 사이트 부제, 이미지의 내재 크기 규칙이 있다(226–230). 원문: `background: #76a3de url(images/primary\_nav\_bg\_repeat\_on.gif) repeat-x top;` (202). |
| 232–242 | 페이지 제목과 JSON-LD 메타데이터 — 페이지 제목은 `General Diagnostic Output (fort.16) - ADCIRC` (232)이다. `WebPage`, `BreadcrumbList`, `WebSite` 메타데이터가 페이지·사이트 URL과 V51 문서의 탐색 경로를 담는다(237). 게시 시각은 `2015-03-27T14:47:39+00:00`이다(237). 수정 시각은 `2015-03-27T15:14:56+00:00`이다(237). 언어는 `en-US`이고 읽기·검색 동작 정보가 있다(237). 빈 줄도 포함한다(233–242). |
| 243–272 | WordPress 자동 생성 부분 — 이모지(emoji) 자산 위치와 표시 지원 검사 JavaScript가 있다(243–247). 이모지 표시 CSS, 버튼 CSS, 색·그라데이션·글꼴·간격·그림자·배치의 CSS 프리셋이 있다(250–270). 주석과 빈 줄을 포함한다(243–272). |
| 273–304 | 관리 표시와 사이트 계측 — 빈 줄 뒤에 관리 막대의 배경색 CSS가 있다(273–290). Beehive 계측 설정은 `anonymize\_ip`와 `allow\_google\_signals`를 모두 `false`로 적는다(293–299). 사이트 배경 그림 URL과 반복 방향을 지정한다(301). |
| 305–350 | 사이트 제목과 문서 메뉴 — 빈 제목 표시와 ADCIRC 사이트 이름, 공식 사이트 부제, 본문 건너뛰기 링크가 있다(305–311). Community 메뉴에는 개발자·협력 기관·사용자 링크가 있다(313–323). Documentation 메뉴에는 V50·V51·V52·V53 매뉴얼, 컴파일·명령줄 옵션, FAQ, SWAN + ADCIRC, 예제 링크가 있다(324–350). |
| 351–402 | 보고서·소프트웨어·소식·제품 메뉴 — 보고서·개발자 안내·이론·얼음 피복 수정·부분 영역 모델링 링크가 있다(351–359). 관련 소프트웨어 링크가 있다(360–362). 사용자 모임·워크숍·사진·발표·폭풍 해일 예보·Katrina 예제 링크가 있다(363–394). 제품 링크와 ASGS 링크가 있다(395–401). 사진 파일을 직접 가리키는 메뉴 링크가 있다(369·371·375·376·388·390). |
| 403–406 | 문서 탐색 경로와 제목 — 탐색 경로는 Home, Documentation, User’s Manual – V51, Output File Descriptions, 현재 문서의 순서이다(403). 제목은 `# General Diagnostic Output (fort.16)` (405)이다. 빈 줄도 포함한다(404·406). |
| 407–410 | General Diagnostic Output (fort.16) / 출력 개요 — fort.14와 fort.15 참조 파일의 정보를 재출력(echo print)한다(407). 일부 처리된 정보를 제공하고 ADCIRC 오류 메시지를 출력한다(407). 다음 표제는 `Notes for fort.16 file:`이다(409). 원문: `Output file which echo prints information from the [Grid and Boundary Information File](../../input-file-descriptions/adcirc-grid-and-boundary-information-file-fort-14), the [Model Parameter and Periodic Boundary Condition File](../../input-file-descriptions/model-parameter-and-periodic-boundary-condition-file-fort-15), provides some processed information and prints out error messages from ADCIRC.` (407); `**Notes for fort.16 file:**` (409). |
| 411–418 | Notes for fort.16 file / GFDL 형식의 특성 — GFDL(Geophysical Fluid Dynamics Laboratory) 파일 형식은 대기 모델(atmospheric model) 출력을 지원하도록 개발되었다고 적는다(411–412). 각 ASCII GFDL 기상 파일(met file)은 하나 이상의 중첩 격자(nested grid) 데이터를 담는다(414). 중첩 격자는 시간에 따라 바뀔 수 있다(414). 더 세밀한 중첩 격자 데이터가 제공되는 곳에는 거친 격자 데이터를 저장하지 않는다(415). 이어서 GFDL용 ADCIRC fort.22의 형식을 소개한다(417). 원문: `The Geophysical Fluid Dynamics Laboratory (GFDL) file format was developed to support the output from atmospheric models. The files  ` (411); `have the following characteristics:` (412); `\* Each ASCII GFDL met file contains one or more nested grid data where the nested grids are allowed to change in time.  ` (414); `\* Coarse grid data is not stored where finer nest data is given.` (415); `The file format of the ADCIRC fort.22 for GFDL is as follows:` (417). |
| 419–423 | GFDL용 fort.22 입력 형식 — 첫 세 행은 텍스트 머리부, 실수인 바람 배율, 최대 외삽 거리의 순서이다(419–421). 최대 외삽 거리의 단위는 원문에서 `(m)`이다(421). 4행부터 마지막 행까지의 항목은 `cycleTime rampValue filename`이다(422). 기본값이나 허용값 범위는 이 구간에 없다. 원문: `Line 1 — ASCII Text Header  ` (419); `Line 2 — Windmultiplier Value (real number)  ` (420); `Line 3 — Maximum Extrapolation distance (m)  ` (421); `Lines 4-end — cycleTime rampValue filename` (422). |
| 424–438 | 개별 GFDL 데이터 파일 형식 — 첫 행의 셀 수 표기와 `(f10.4)` 형식을 제시한다(426). 데이터 행 범위는 `2-NCELLS+1`이며, 열 개의 열을 `10f10.4` 형식으로 적는다고 설명한다(427). 열별 변수명과 단위를 원문 순서대로 옮긴다(428–437). 열 번째 중첩 번호는 항상 존재하지는 않는다고 적는다(437). 표제와 빈 줄도 포함한다(424–438). 원문: `The file format for each of the actual GFDL files is as follows:` (424); `Line 1: Number of grid cells (f10.4) NCELLS  ` (426); `Lines 2-NCELLS+1: Have ten columns of data formatted as 10f10.4  ` (427); `1. u (m/sec)  ` (428); `2. v (m/sec)  ` (429); `3. Temperature (K)  ` (430); `4. mixing ratio(kg/kg)  ` (431); `5. storm accum precipitation (cm)  ` (432); `6. sea level pressure (hPa)  ` (433); `7. longitude (decimal deg)  ` (434); `8. latitude (decimal deg)  ` (435); `9. hurricane hour  ` (436); `10. nest number (this is not always present)` (437). |
| 439–447 | GFDL용 fort.22 입력 예제 — 첫 행은 최대 길이 1024문자의 주석이라는 예제를 제시한다(441). 다음 두 행의 예제값은 속도 크기 배율과 최대 외삽 거리이다(442–443). 나머지 세 행은 시각, 램프 배율(ramp multiplier), 파일 경로를 적는다(444–446). 시각 단위는 예제 주석의 `time (hours)`이다(444). 이 숫자들을 기본값으로 설명하지는 않는다(439–446). 공백·경로·따옴표·주석을 그대로 옮긴다. 원문: `To illustrate the definitions and descriptions provided, a concrete example of an ADCIRC fort.22 file for GFDL is provided as follows:` (439); `!       1st line is a comment line, max length 1024 characters  ` (441); `1.0     ! 2nd line is a velocity magnitude multiplier  ` (442); `10000.0 ! 3rd line: maximum extrapolation distance (m)  ` (443); `0.0 0.0 “/home/jason/isaac/gfdl/isaac\_gfdl\_file1″ ! time (hours), ramp mult, filename  ` (444); `6.0 0.5 “/home/jason/isaac/gfdl/isaac\_gfdl\_file2″  ` (445); `12.0 1.0 “/home/jason/isaac/gfdl/isaac\_gfdl\_file3″` (446). |
| 448–449 | 데이터 파일 경로의 따옴표 조건 — 데이터 파일의 전체 경로에 슬래시(`/`)가 있으면 전체 경로 파일명을 큰따옴표로 감싸야 한다고 적는다(448). Unix·Linux 실행을 예로 든다(448). Fortran이 따옴표 없는 슬래시를 레코드 종료 문자(end-of-record character)로 취급하기 때문에 필요하다고 적는다(448). 마지막 빈 줄도 포함한다(449). 원문: `When including the path to the data files, if the full path includes forward slashes (as it would if ADCIRC is executing on Unix or Linux), be sure to surround the full path file name with double quotes as shown in the example above. This is required because Fortran treats a bare forward slash in an input file as an end-of-record character.` (448). |
| 450–464 | 사이트 꼬리말 — 빈 줄을 포함한다(450–464). 표시 유틸리티 호출이 있다(452). 링크 사전 가져오기(prefetch) 규칙이 있다(454). UNC 쿠키 안내와 수락 버튼 설정이 있다(457–459). 슬라이드 표시의 `no-js` 클래스를 제거한다(463). New Relic 계측 정보로 파일이 끝난다(464). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 166: CSS 메뉴 배경의 로컬 사본은 그림 파일 없음(`images/primary_nav_divider.gif`). 문서 상대 경로와 URL 경로에 해당하는 폴더를 확인했고, `models/ADCIRC/raw/manuals/`에서 파일명을 검색해도 찾지 못했다.
- 202: CSS 메뉴 배경의 로컬 사본은 그림 파일 없음(`images/primary_nav_bg_repeat_on.gif`). 문서 상대 경로와 URL 경로에 해당하는 폴더를 확인했고, `models/ADCIRC/raw/manuals/`에서 파일명을 검색해도 찾지 못했다.
- 301: CSS 사이트 배경의 로컬 사본은 그림 파일 없음(`grid_bkgrd_lt_grey1.jpg`). 문서 상대 경로와 URL 경로에 해당하는 폴더를 확인했고, `models/ADCIRC/raw/manuals/`에서 파일명을 검색해도 찾지 못했다.
- 369: 2018 모임 사진 링크의 로컬 사본은 그림 파일 없음(`ADCIRC2018_Group_Photo2.jpg`). 문서 상대 경로와 URL 경로에 해당하는 폴더를 확인했고, `models/ADCIRC/raw/manuals/`에서 파일명을 검색해도 찾지 못했다.
- 371: 2017 모임 사진 링크의 로컬 사본은 그림 파일 없음(`2017ADCIRCUGMGroupPhoto.jpg`). 문서 상대 경로와 URL 경로에 해당하는 폴더를 확인했고, `models/ADCIRC/raw/manuals/`에서 파일명을 검색해도 찾지 못했다.
- 375: 2016 모임 사진 링크의 로컬 사본은 그림 파일 없음(`160506-A-Y1769-008-A-1.jpg`). 문서 상대 경로와 URL 경로에 해당하는 폴더를 확인했고, `models/ADCIRC/raw/manuals/`에서 파일명을 검색해도 찾지 못했다.
- 376: 2016 Boot Camp 사진 링크의 로컬 사본은 그림 파일 없음(`adcircBootCampers2016_small_caption.jpg`). 문서 상대 경로와 URL 경로에 해당하는 폴더를 확인했고, `models/ADCIRC/raw/manuals/`에서 파일명을 검색해도 찾지 못했다.
- 388: 2011 워크숍 사진 링크의 로컬 사본은 그림 파일 없음(`2011_ADCIRC_meeting.jpg`). 문서 상대 경로와 URL 경로에 해당하는 폴더를 확인했고, `models/ADCIRC/raw/manuals/`에서 파일명을 검색해도 찾지 못했다.
- 390: 2010 워크숍 사진 링크의 로컬 사본은 그림 파일 없음(`ADCIRC_Workshop2010_GroupPhoto2.png`). 문서 상대 경로와 URL 경로에 해당하는 폴더를 확인했고, `models/ADCIRC/raw/manuals/`에서 파일명을 검색해도 찾지 못했다.
- 409·417·439: `Notes for fort.16 file:` 표제 아래에서 GFDL용 fort.22 입력 형식과 입력 예제를 설명한다.
- 427·437: 427행은 열 개의 데이터 열을 `10f10.4` 형식으로 규정한다. 437행은 열 번째 `nest number`가 항상 존재하지는 않는다고 적는다.
- 444–446·448: 예제 경로를 감싼 문자는 여는 `“`(U+201C)와 닫는 `″`(U+2033)이다. 448행은 경로에 슬래시가 있으면 `double quotes`로 감싸야 한다고 적는다.

