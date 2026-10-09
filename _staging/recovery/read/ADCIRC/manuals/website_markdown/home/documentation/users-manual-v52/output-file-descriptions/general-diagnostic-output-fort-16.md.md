---
file: models/ADCIRC/raw/manuals/website_markdown/home/documentation/users-manual-v52/output-file-descriptions/general-diagnostic-output-fort-16.md
lines: 463
sha256: 6f07505fdd872e97afeedd633db5abd10e657dd2ae687261f8ceba20ac0ea28d
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# general-diagnostic-output-fort-16.md — 판독 구간 기록

구간은 1행부터 463행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–12 | 웹페이지 계측 스크립트. New Relic 초기화와 브라우저 로더(browser loader)가 들어 있다(1–2). 나머지는 빈 줄이다(3–12). |
| 13–70 | 웹페이지 검색·머리말 스타일. 검색 입력란과 버튼, 제목 링크, 본문 글꼴·색, 머리말과 컨테이너(container)의 스타일시트(CSS) 규칙을 지정한다(13–70). |
| 71–150 | 웹페이지 본문·탐색 스타일. 본문 열과 콘텐츠 영역, 문단·링크, 이동 경로(breadcrumb), 활성 메뉴, 인용문·제목·접근 영역의 표시 규칙이다(71–150). |
| 151–230 | 웹페이지 메뉴 스타일. 메뉴 글꼴·목록·정렬, 하위 메뉴, 마우스 오버(hover)와 현재 페이지 표시, 글라이더(glider), 표어 숨김, 이미지 크기 규칙이다(151–230). 메뉴 배경 참조는 `background:url(images/primary\_nav\_divider.gif) repeat-y scroll right bottom;` (166)와 `background: #76a3de url(images/primary\_nav\_bg\_repeat\_on.gif) repeat-x top;` (202)이다. 두 로컬 그림 파일은 없다. |
| 231–241 | 페이지 제목과 구조화 메타데이터. 제목은 `General Diagnostic Output (fort.16) - ADCIRC` (232)이다. JSON-LD 메타데이터에 페이지 식별자·URL·제목·날짜·이동 경로와 사이트 검색 정보가 들어 있다(237). 앞뒤 빈 줄을 포함한다(231–241). |
| 242–285 | 웹페이지 이모지(emoji)와 공통 스타일. CDATA 경계 주석, WordPress 이모지 설정·처리 스크립트, 이모지 크기, 블록 버튼, 공통 색·크기 등의 프리셋(preset), flex·grid·인용문 스타일이 들어 있다(242–269). 뒤의 빈 줄을 포함한다(270–285). |
| 286–311 | 웹페이지 관리 막대·분석 설정과 사이트 머리말. 관리 막대 스타일(286–288), Beehive의 Google Analytics 설정(292–298), 페이지 배경 `body.custom-background { background-color: #ffffff; background-image: url("https://adcirc.org/wp-content/uploads/sites/2255/2013/03/grid\_bkgrd\_lt\_grey1.jpg"); background-position: left top; background-size: auto; background-repeat: repeat-y; background-attachment: scroll; }` (300)을 포함한다. 배경의 로컬 그림 파일은 없다. ADCIRC 사이트 링크(306), 공식 웹사이트 부제(308), 탐색 건너뛰기 링크(310)와 빈 줄을 포함한다. |
| 312–358 | 공통 탐색 메뉴: Community와 Documentation. 개발자·협력 기관·사용자 링크(312–322)를 나열한다. 사용자 설명서와 컴파일·명령행·질문·SWAN+ADCIRC·보고서·이론·특수 기능·얼음·하위 영역 관련 문서 링크(323–358)를 나열한다. |
| 359–401 | 공통 탐색 메뉴: 관련 소프트웨어·뉴스·제품. 워크숍과 모임, 격자(grid)·조석 데이터베이스·예측·기름 이동·ASGS 등의 링크를 나열한다(359–400). 사진 파일 링크는 `    - [2018 ADCIRC Week Group Photo](https://adcirc.org/wp-content/uploads/sites/2255/2018/04/ADCIRC2018_Group_Photo2.jpg)` (368); `    - [2017 ADCIRC Meeting Group Photo](https://adcirc.org/wp-content/uploads/sites/2255/2017/06/2017ADCIRCUGMGroupPhoto.jpg)` (370); `    - [2016 ADCIRC User’s Group Photo](https://adcirc.org/wp-content/uploads/sites/2255/2016/05/160506-A-Y1769-008-A-1.jpg)` (374); `    - [2016 ADCIRC Boot Camp Group Photo](https://adcirc.org/wp-content/uploads/sites/2255/2016/05/adcircBootCampers2016_small_caption.jpg)` (375); `    - [2011 ADCIRC Workshop Photo](https://adcirc.org/wp-content/uploads/sites/2255/2018/11/2011_ADCIRC_meeting.jpg)` (387); `    - [2010 ADCIRC Workshop Photo](https://adcirc.org/wp-content/uploads/sites/2255/2018/11/ADCIRC_Workshop2010_GroupPhoto2.png)` (389)이다. 이 사진들의 로컬 사본은 모두 없다. 끝의 빈 줄을 포함한다(401). |
| 402–407 | fort.16: 일반 진단 출력(diagnostic output). 이동 경로(402)와 절 제목(404)을 포함한다. 격자·경계 정보 파일 fort.14와 모델 매개변수·주기 경계 조건 파일 fort.15에서 읽은 정보를 되풀이해 출력(echo)한다(406). 처리된 정보와 오류 메시지도 포함한다(406). 끝의 빈 줄을 포함한다(407). |
| 408–415 | fort.16 주의 절과 GFDL 기상 파일의 특징. 주의 절 제목(408) 아래에서 Geophysical Fluid Dynamics Laboratory(GFDL) 형식이 대기 모델 출력을 지원하기 위해 개발되었다고 설명한다(410–411). 중첩 격자(nested grid)의 시간 변화 허용 조건과 더 세밀한 격자가 있을 때의 거친 격자 자료 미저장 조건은 `\* Each ASCII GFDL met file contains one or more nested grid data where the nested grids are allowed to change in time.  ` (413)와 `\* Coarse grid data is not stored where finer nest data is given.` (414)이다. 빈 줄을 포함한다(408–415). |
| 416–422 | ADCIRC fort.22의 GFDL 입력 파일 구조. 대상 파일과 형식을 `The file format of the ADCIRC fort.22 for GFDL is as follows:` (416)으로 밝힌다. 각 입력 줄의 형식은 `Line 1 — ASCII Text Header  ` (418); `Line 2 — Windmultiplier Value (real number)  ` (419); `Line 3 — Maximum Extrapolation distance (m)  ` (420); `Lines 4-end — cycleTime rampValue filename` (421)이다. 수치형 조건과 거리 단위, 자료 줄의 필드 순서를 그대로 옮겼다. 빈 줄을 포함한다(416–422). |
| 423–437 | 실제 GFDL 자료 파일 형식. 형식 소개(423) 뒤에 격자 셀(grid cell) 수와 자료 줄 범위·서식을 `Line 1: Number of grid cells (f10.4) NCELLS  ` (425)와 `Lines 2-NCELLS+1: Have ten columns of data formatted as 10f10.4  ` (426)으로 제시한다. 각 열의 이름·단위·조건은 `1. u (m/sec)  ` (427); `2. v (m/sec)  ` (428); `3. Temperature (K)  ` (429); `4. mixing ratio(kg/kg)  ` (430); `5. storm accum precipitation (cm)  ` (431); `6. sea level pressure (hPa)  ` (432); `7. longitude (decimal deg)  ` (433); `8. latitude (decimal deg)  ` (434); `9. hurricane hour  ` (435); `10. nest number (this is not always present)` (436)이다. 모든 열을 원문 그대로 옮겼다. 끝의 빈 줄을 포함한다(437). |
| 438–447 | fort.22의 GFDL 형식 예제와 경로 인용 규칙. 예제를 소개한다(438). 입력 예제 줄은 `! 1st line is a comment line, max length 1024 characters  ` (440); `1.0 ! 2nd line is a velocity magnitude multiplier  ` (441); `10000.0 ! 3rd line: maximum extrapolation distance (m)  ` (442); `0.0 0.0 “/home/jason/isaac/gfdl/isaac\_gfdl\_file1″ ! time (hours), ramp mult, filename  ` (443); `6.0 0.5 “/home/jason/isaac/gfdl/isaac\_gfdl\_file2″  ` (444); `12.0 1.0 “/home/jason/isaac/gfdl/isaac\_gfdl\_file3″` (445)이다. 예제의 수치와 따옴표 문자를 그대로 옮겼다. 예제 수치를 기본값으로 해석하지 않는다. 순방향 슬래시(forward slash)가 있는 전체 경로를 큰따옴표로 감싸야 하는 조건과 문서가 제시한 Fortran 이유는 `When including the path to the data files, if the full path includes forward slashes (as it would if ADCIRC is executing on Unix or Linux), be sure to surround the full path file name with double quotes as shown in the example above. This is required because Fortran treats a bare forward slash in an input file as an end-of-record character.` (447)이다. 빈 줄을 포함한다(438–447). |
| 448–463 | 웹페이지 바닥의 공통 스크립트와 빈 줄. 유틸리티 표시 호출(451), 링크 미리 가져오기(prefetch) 설정(453), CDATA 경계 주석과 쿠키 안내 설정(456–458), Soliloquy의 jQuery 호출(462), New Relic 계측 정보(463)를 포함한다. |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 166행의 메뉴 구분선 배경: 그림 파일 없음. 해당 파일명의 로컬 사본을 `models/ADCIRC/raw/manuals` 아래에서 찾지 못했다. 원문 참조는 `background:url(images/primary\_nav\_divider.gif) repeat-y scroll right bottom;` (166)이다.
- 202행의 메뉴 선택 배경: 그림 파일 없음. 해당 파일명의 로컬 사본을 `models/ADCIRC/raw/manuals` 아래에서 찾지 못했다. 원문 참조는 `background: #76a3de url(images/primary\_nav\_bg\_repeat\_on.gif) repeat-x top;` (202)이다.
- 300행의 페이지 배경: 그림 파일 없음. 해당 파일명의 로컬 사본을 `models/ADCIRC/raw/manuals` 아래에서 찾지 못했다. 원문 참조는 `body.custom-background { background-color: #ffffff; background-image: url("https://adcirc.org/wp-content/uploads/sites/2255/2013/03/grid\_bkgrd\_lt\_grey1.jpg"); background-position: left top; background-size: auto; background-repeat: repeat-y; background-attachment: scroll; }` (300)이다.
- 368행의 2018 ADCIRC Week 단체 사진 링크: 그림 파일 없음. 해당 파일명의 로컬 사본을 `models/ADCIRC/raw/manuals` 아래에서 찾지 못했다. 원문 참조는 `    - [2018 ADCIRC Week Group Photo](https://adcirc.org/wp-content/uploads/sites/2255/2018/04/ADCIRC2018_Group_Photo2.jpg)` (368)이다.
- 370행의 2017 ADCIRC Meeting 단체 사진 링크: 그림 파일 없음. 해당 파일명의 로컬 사본을 `models/ADCIRC/raw/manuals` 아래에서 찾지 못했다. 원문 참조는 `    - [2017 ADCIRC Meeting Group Photo](https://adcirc.org/wp-content/uploads/sites/2255/2017/06/2017ADCIRCUGMGroupPhoto.jpg)` (370)이다.
- 374행의 2016 ADCIRC 사용자 모임 단체 사진 링크: 그림 파일 없음. 해당 파일명의 로컬 사본을 `models/ADCIRC/raw/manuals` 아래에서 찾지 못했다. 원문 참조는 `    - [2016 ADCIRC User’s Group Photo](https://adcirc.org/wp-content/uploads/sites/2255/2016/05/160506-A-Y1769-008-A-1.jpg)` (374)이다.
- 375행의 2016 ADCIRC Boot Camp 단체 사진 링크: 그림 파일 없음. 해당 파일명의 로컬 사본을 `models/ADCIRC/raw/manuals` 아래에서 찾지 못했다. 원문 참조는 `    - [2016 ADCIRC Boot Camp Group Photo](https://adcirc.org/wp-content/uploads/sites/2255/2016/05/adcircBootCampers2016_small_caption.jpg)` (375)이다.
- 387행의 2011 ADCIRC Workshop 사진 링크: 그림 파일 없음. 해당 파일명의 로컬 사본을 `models/ADCIRC/raw/manuals` 아래에서 찾지 못했다. 원문 참조는 `    - [2011 ADCIRC Workshop Photo](https://adcirc.org/wp-content/uploads/sites/2255/2018/11/2011_ADCIRC_meeting.jpg)` (387)이다.
- 389행의 2010 ADCIRC Workshop 단체 사진 링크: 그림 파일 없음. 해당 파일명의 로컬 사본을 `models/ADCIRC/raw/manuals` 아래에서 찾지 못했다. 원문 참조는 `    - [2010 ADCIRC Workshop Photo](https://adcirc.org/wp-content/uploads/sites/2255/2018/11/ADCIRC_Workshop2010_GroupPhoto2.png)` (389)이다.
- 404행의 페이지 제목과 408행의 주의 절 제목은 fort.16을 가리킨다. 416–447행은 fort.22의 GFDL 입력 형식과 예제를 설명한다.
- 426행은 자료가 열 10개이고 서식이 10f10.4라고 설명한다. 436행은 열 10의 nest number가 항상 있지는 않다고 설명한다. 해당 열이 없을 때의 서식은 이 문서에 따로 제시하지 않는다.
- 443–445행 예제의 파일 경로 앞 문자는 “(U+201C)이고 뒤 문자는 ″(U+2033)이다. 447행은 전체 경로를 double quotes로 감싸도록 요구한다.
