---
file: models/ADCIRC/raw/manuals/website_markdown/home/documentation/users-manual-v52/input-file-descriptions/meteorological-recording-station-location-input-file-met_stat-151/index.md
lines: 436
sha256: ebb6c6bf332f9a1b8a2355a91243feceeaf8a55cea41340e1943d1d9d367cf94
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# index.md — 판독 구간 기록

구간은 1행부터 436행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–12 | 웹 페이지 시작 코드 — New Relic 브라우저 계측 JavaScript를 포함한다(1–2). 뒤 빈 줄을 포함한다(3–12). |
| 13–77 | 웹 페이지 스타일 / 검색창·머리말·컨테이너 — CSS가 검색창, 문서 제목, 본문 글꼴과 컨테이너 크기를 지정한다(13–77). |
| 78–142 | 웹 페이지 스타일 / 본문·탐색 경로 — CSS가 본문 열, 문단, 링크, 탐색 경로(breadcrumbs)와 인용문 표시를 지정한다(78–142). |
| 143–200 | 웹 페이지 스타일 / 메뉴 — CSS가 메뉴와 하위 메뉴 표시를 지정한다(143–200). 메뉴 배경 이미지 경로를 포함한다(166). `images/primary\_nav\_divider.gif` (166): 그림 파일 없음. |
| 201–228 | 웹 페이지 스타일 / 메뉴 선택 상태 — CSS가 메뉴에 마우스를 올린 상태와 현재 페이지 메뉴 표시를 지정한다(201–228). 배경 이미지 경로를 포함한다(202). `images/primary\_nav\_bg\_repeat\_on.gif` (202): 그림 파일 없음. |
| 229–269 | 웹 페이지 제목·메타데이터·WordPress 표시 코드 — 페이지 제목(232), 구조화 메타데이터(JSON-LD)(237), 이모지(emoji) 지원 JavaScript(242–246)와 WordPress 표시 CSS(249–269)를 포함한다. |
| 270–310 | 웹 페이지 분석 코드·배경·사이트 머리말 — 빈 줄, 관리 표시 CSS(286–288), 방문 분석 JavaScript(292–298), 사이트 배경 이미지 CSS(300), ADCIRC 사이트 머리말과 탐색 건너뛰기 링크(304–310)를 포함한다. `https://adcirc.org/wp-content/uploads/sites/2255/2013/03/grid\_bkgrd\_lt\_grey1.jpg` (300): 그림 파일 없음. |
| 311–358 | 사이트 메뉴 / Community·Documentation — 개발자와 사용자 링크(312–322)를 제공한다. 매뉴얼 판본, 컴파일·명령행 옵션, FAQ, 예제와 보고서 링크를 제공한다(323–358). |
| 359–401 | 사이트 메뉴 / Related software·News·Products·ASGS — 유틸리티와 격자 작성 도구 링크(359–361), 행사·사진·발표 자료 링크(362–393), 제품과 ASGS 링크(394–400)를 제공한다. 마지막 빈 줄을 포함한다(401). `https://adcirc.org/wp-content/uploads/sites/2255/2018/04/ADCIRC2018_Group_Photo2.jpg` (368): 그림 파일 없음. `https://adcirc.org/wp-content/uploads/sites/2255/2017/06/2017ADCIRCUGMGroupPhoto.jpg` (370): 그림 파일 없음. `https://adcirc.org/wp-content/uploads/sites/2255/2016/05/160506-A-Y1769-008-A-1.jpg` (374): 그림 파일 없음. `https://adcirc.org/wp-content/uploads/sites/2255/2016/05/adcircBootCampers2016_small_caption.jpg` (375): 그림 파일 없음. `https://adcirc.org/wp-content/uploads/sites/2255/2018/11/2011_ADCIRC_meeting.jpg` (387): 그림 파일 없음. `https://adcirc.org/wp-content/uploads/sites/2255/2018/11/ADCIRC_Workshop2010_GroupPhoto2.png` (389): 그림 파일 없음. |
| 402–409 | Meteorological Recording Station Location Input / 적용 조건·파일 표시법 — 기상 관측소(meteorological recording station) 수인 fort.15의 NSTAM이 음수일 때 met_stat.151을 읽는다고 적는다(406). 굵은 변수명 행, 가독성을 위한 빈 줄, 여러 입력 행을 나타내는 반복문과 변수 정의 링크를 설명한다(408). 원문: `The reading of the met\_stat.151 file is triggered when the number of meteorological recording stations ([NSTAM](https://adcirc.org/home/documentation/users-manual-v52/parameter-definitions#NSTAM)) in the [fort.15 file](https://adcirc.org/home/documentation/users-manual-v52/input-file-descriptions/model-parameter-and-periodic-boundary-condition-file-fort-15/) is set to a negative value.` (406); `The basic file structure is shown below. Each line of input data is represented by a line containing the input variable name(s) in bold face type. Blank lines are only to enhance readability. Loops indicate multiple lines of input. Definitions of each variable are provided via hot links.` (408). |
| 410–417 | met_stat.151 입력 형식 — NSTAM2를 먼저 입력한다(410). k=1부터 NSTAM2까지 반복하며 XEM(k), YEM(k)을 입력한다(412–414). 반복 종료문과 빈 줄을 포함한다(415–417). 입력 형식을 그대로 옮긴다. 원문: `[**NSTAM2**](https://adcirc.org/home/documentation/users-manual-v52/parameter-definitions#NSTAM2)` (410); `for k=1,[NSTAM2](https://adcirc.org/home/documentation/users-manual-v52/parameter-definitions#NSTAM2)` (412); `**[XEM(k)](https://adcirc.org/home/documentation/users-manual-v52/parameter-definitions#XEM)**, **[YEM(k)](https://adcirc.org/home/documentation/users-manual-v52/parameter-definitions#YEM)**` (414); `end k loop` (416). |
| 418–421 | Notes / 관측소 수의 처리 — NSTAM2가 fort.15에서 읽은 NSTAM과 다르면 NSTAM2를 사용한다고 적는다(420). 관측소 수가 NSTAM2보다 적으면 오류로 중단한다고 적는다(420). 관측소 수가 NSTAM2보다 많으면 처음 NSTACM개만 사용한다고 적는다(420). 원문의 파일명 conc_stat.151과 변수명 NSTACM을 그대로 옮긴다. 원문: `**Notes:**` (418); `If the value of NSTAM2 differs from the value of NSTAM (as read from the fort.15 file) the value of NSTAM2 will be used. If there are fewer than NSTAM2 stations listed in the conc\_stat.151 file, ADCIRC will stop with an error. If there are more than NSTAM2 stations listed in the conc\_stat.151 file, only the first NSTACM of them will be used.` (420). |
| 422–436 | 웹 페이지 끝 코드 — 빈 줄과 사이트 유틸리티 호출(424), 문서 링크 미리 가져오기(prefetch) JSON(426), 쿠키(cookie) 안내 설정(429–431), jQuery 표시 코드(435), New Relic 페이지 계측 정보(436)를 포함한다. |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 404·406·420: 제목과 읽기 조건의 파일명은 `met\_stat.151`이다. 관측소 수에 대한 Notes의 파일명은 두 곳 모두 `conc\_stat.151`이다.
- 410–414·420: 입력 변수와 반복 범위는 `NSTAM2`이다. 420행의 초과 관측소 처리에는 `NSTACM`이 적히며 이 파일에서 NSTACM을 정의하지 않는다.
- 410–414: XEM(k)와 YEM(k)의 단위와 좌표계는 이 파일 본문에서 정의하지 않는다. 변수 정의 링크를 제공한다.
- 166: `images/primary\_nav\_divider.gif`의 로컬 사본을 찾지 못했다. 그림 파일 없음. 상대 images 경로와 models/ADCIRC/raw 내 파일명 목록을 확인했다.
- 202: `images/primary\_nav\_bg\_repeat\_on.gif`의 로컬 사본을 찾지 못했다. 그림 파일 없음. 상대 images 경로와 models/ADCIRC/raw 내 파일명 목록을 확인했다.
- 300: `https://adcirc.org/wp-content/uploads/sites/2255/2013/03/grid\_bkgrd\_lt\_grey1.jpg`의 로컬 사본을 찾지 못했다. 그림 파일 없음. 상대 images 경로와 models/ADCIRC/raw 내 파일명 목록을 확인했다.
- 368: `https://adcirc.org/wp-content/uploads/sites/2255/2018/04/ADCIRC2018_Group_Photo2.jpg`의 로컬 사본을 찾지 못했다. 그림 파일 없음. 상대 images 경로와 models/ADCIRC/raw 내 파일명 목록을 확인했다.
- 370: `https://adcirc.org/wp-content/uploads/sites/2255/2017/06/2017ADCIRCUGMGroupPhoto.jpg`의 로컬 사본을 찾지 못했다. 그림 파일 없음. 상대 images 경로와 models/ADCIRC/raw 내 파일명 목록을 확인했다.
- 374: `https://adcirc.org/wp-content/uploads/sites/2255/2016/05/160506-A-Y1769-008-A-1.jpg`의 로컬 사본을 찾지 못했다. 그림 파일 없음. 상대 images 경로와 models/ADCIRC/raw 내 파일명 목록을 확인했다.
- 375: `https://adcirc.org/wp-content/uploads/sites/2255/2016/05/adcircBootCampers2016_small_caption.jpg`의 로컬 사본을 찾지 못했다. 그림 파일 없음. 상대 images 경로와 models/ADCIRC/raw 내 파일명 목록을 확인했다.
- 387: `https://adcirc.org/wp-content/uploads/sites/2255/2018/11/2011_ADCIRC_meeting.jpg`의 로컬 사본을 찾지 못했다. 그림 파일 없음. 상대 images 경로와 models/ADCIRC/raw 내 파일명 목록을 확인했다.
- 389: `https://adcirc.org/wp-content/uploads/sites/2255/2018/11/ADCIRC_Workshop2010_GroupPhoto2.png`의 로컬 사본을 찾지 못했다. 그림 파일 없음. 상대 images 경로와 models/ADCIRC/raw 내 파일명 목록을 확인했다.

