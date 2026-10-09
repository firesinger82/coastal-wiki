---
file: models/ADCIRC/raw/manuals/website_markdown/home/documentation/users-manual-v52/input-file-descriptions/elevation-station-location-input-file-elev_stat-151/index.md
lines: 436
sha256: 431ed3c47189409095c20dd47dd3175fe0e1605bddb009fbb15d1d1bcb74654d
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# index.md (elevation-station-location-input-file-elev_stat-151) — 판독 구간 기록

구간은 1행부터 436행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–12 | 웹사이트 머리 부분 — New Relic 초기화와 축소된 브라우저 계측 JavaScript가 들어 있다(1–2). 이어지는 빈 줄을 포함한다(3–12). |
| 13–70 | 웹사이트 스타일 — 검색 필드, 제목, 본문 글꼴·색, 컨테이너(container), 머리 부분과 태그 표시 스타일을 정의한다(13–70). |
| 71–142 | 웹사이트 스타일 — 본문 열과 문단·링크, 이동 경로(breadcrumb), 활성 메뉴, 인용 블록과 제목의 스타일을 정의한다(71–142). |
| 143–200 | 웹사이트 메뉴 스타일 — 메뉴 배치와 하위 메뉴 숨김·위치·크기를 정의한다(143–200). 배경 그림 참조의 로컬 파일은 그림 파일 없음(166). |
| 201–225 | 웹사이트 메뉴 스타일 — 마우스 올림의 배경과 하위 메뉴 펼침, 현재 페이지의 글자색을 정의한다(201–225). 배경 그림 참조의 로컬 파일은 그림 파일 없음(202). |
| 226–270 | 페이지 제목·메타데이터(metadata)와 WordPress 스타일 — 수위 관측점(elevation station) 위치 입력 파일 제목(232), 구조화된 웹페이지·이동 경로(breadcrumb)·검색 데이터(237), 이모지(emoji) 지원 스크립트(242–246), 이모지·버튼·색·간격·그림자 스타일(249–269)을 포함한다. |
| 271–303 | 사이트 지원·계측·배경 — 관리 막대 색(286–288), 방문 계측 초기화(292–298), 배경 그림 URL과 반복 표시 스타일(300)을 포함한다. 배경의 로컬 그림은 그림 파일 없음. 빈 줄을 포함한다. |
| 304–358 | 사이트 머리 부분과 탐색 메뉴 — ADCIRC 사이트 제목과 탐색 건너뛰기 링크(304–310), 개발자·사용자와 설명서, 컴파일 옵션, FAQ, 예제·보고서·출판물 링크를 나열한다(312–358). 링크 대상 본문은 이 구간에 없다. |
| 359–402 | 사이트 탐색 메뉴와 이동 경로 — 관련 소프트웨어, 모임·발표·단체 사진·태풍 뉴스, 조석 데이터·격자·예측·ASGS 링크를 나열한다(359–400). elev_stat.151 설명까지의 이동 경로를 표시한다(402). 단체 사진 링크 6개의 로컬 그림은 그림 파일 없음(368·370·374–375·387·389). |
| 403–409 | Elevation Station Location input file (elev_stat.151) / 읽기 조건 — fort.15의 수위 기록 관측점 수가 음수일 때 이 파일을 읽는다고 설명한다(404–406). 입력 한 줄은 변수 이름이 적힌 한 줄로 표시하고 빈 줄은 가독성 용도로만 쓴다고 적는다(408). 반복은 여러 입력 줄을 뜻하며 변수 정의는 링크로 제공한다고 적는다(408). 읽기 조건을 원문 그대로 옮긴다. 원문: `The reading of the elev\_stat.151 file is triggered when the number of elevation recording stations ([NSTAE](https://adcirc.org/home/documentation/users-manual-v52/parameter-definitions#NSTAE)) in the [fort.15 file](https://adcirc.org/home/documentation/users-manual-v52/input-file-descriptions/model-parameter-and-periodic-boundary-condition-file-fort-15/) is set to a negative value.` (406). |
| 410–417 | 입력 파일 형식 — 관측점 수, 그 수만큼 반복하는 관측점별 두 좌표, 반복 종료를 순서대로 제시한다(410–416). 변수 이름과 반복 범위를 원문 그대로 옮긴다. 원문: `[**NSTAE2**](https://adcirc.org/home/documentation/users-manual-v52/parameter-definitions#NSTAE2)` (410); `for k=1,[NSTAE2](https://adcirc.org/home/documentation/users-manual-v52/parameter-definitions#NSTAE2)` (412); `**[XEL(k)](https://adcirc.org/home/documentation/users-manual-v52/parameter-definitions#XEL)**, **[YEL(k)](https://adcirc.org/home/documentation/users-manual-v52/parameter-definitions#YEL)**` (414); `end k loop` (416). |
| 418–421 | Notes / 관측점 수가 다른 경우 — 두 관측점 수가 다르면 파일의 NSTAE2를 사용한다고 적는다(420). 파일에 열거한 관측점이 NSTAE2보다 적으면 오류로 중단한다고 적는다(420). 더 많으면 처음 NSTAE2개만 사용한다고 적는다(420). 조건과 수량을 원문 그대로 옮긴다. 원문: `If the value of NSTAE2 differs from the value of NSTAE (as read from the fort.15 file) the value of NSTAE2 will be used. If there are fewer than NSTAE2 stations listed in the elev\_stat.151 file, ADCIRC will stop with an error. If there are more than NSTAE2 stations listed in the elev\_stat.151 file, only the first NSTAE2 of them will be used.` (420). |
| 422–436 | 웹사이트 끝부분 — 빈 줄과 유틸리티 표시 호출(422–424), 사전 읽기(prefetch) 규칙(426), 쿠키 안내 설정(429–431), 슬라이더의 no-js 클래스 제거와 New Relic 계측 정보(435–436)를 포함한다. |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 166: CSS의 `images/primary\_nav\_divider.gif`는 그림 파일 없음.
- 202: CSS의 `images/primary\_nav\_bg\_repeat\_on.gif`는 그림 파일 없음.
- 300: CSS의 `grid\_bkgrd\_lt\_grey1.jpg` 배경은 그림 파일 없음.
- 368: 일반 링크의 `ADCIRC2018_Group_Photo2.jpg`는 그림 파일 없음.
- 370: 일반 링크의 `2017ADCIRCUGMGroupPhoto.jpg`는 그림 파일 없음.
- 374: 일반 링크의 `160506-A-Y1769-008-A-1.jpg`는 그림 파일 없음.
- 375: 일반 링크의 `adcircBootCampers2016_small_caption.jpg`는 그림 파일 없음.
- 387: 일반 링크의 `2011_ADCIRC_meeting.jpg`는 그림 파일 없음.
- 389: 일반 링크의 `ADCIRC_Workshop2010_GroupPhoto2.png`는 그림 파일 없음.
