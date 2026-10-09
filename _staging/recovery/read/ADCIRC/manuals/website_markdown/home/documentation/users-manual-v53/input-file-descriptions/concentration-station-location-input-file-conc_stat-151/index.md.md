---
file: models/ADCIRC/raw/manuals/website_markdown/home/documentation/users-manual-v53/input-file-descriptions/concentration-station-location-input-file-conc_stat-151/index.md
lines: 436
sha256: 264556e44218f246ed1a87b407c062de3423ec086300faee64a8f833b1ccc430
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# index.md — 판독 구간 기록

구간은 1행부터 436행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–12 | 사이트 계측 코드 — New Relic 초기화 코드와 축소된 JavaScript 로더를 포함한다(1–2). 이어지는 빈 줄도 이 구간에 포함한다(3–12). |
| 13–77 | 사이트 서식 / 검색·머리글·기본 배치 — CSS(Cascading Style Sheets)는 검색창, 링크, 본문, 머리글, 컨테이너와 오른쪽 콘텐츠의 서식을 지정한다(13–77). |
| 78–142 | 사이트 서식 / 본문·경로 탐색 — CSS는 단일 열 콘텐츠, 문단, 링크, 경로 탐색과 활성 메뉴, 인용문 및 다중 열 콘텐츠의 서식을 지정한다(78–142). |
| 143–200 | 사이트 서식 / 주 메뉴 — CSS는 주 메뉴와 중첩 메뉴의 위치·표시·서식을 지정한다(143–200). 메뉴 구분선 배경은 `images/primary\_nav\_divider.gif`를 참조한다(166). 해당 로컬 그림 파일 없음. |
| 201–231 | 사이트 서식 / 메뉴 상태·이미지 크기 — CSS는 마우스가 올라간 메뉴, 현재 메뉴, 슬라이더와 태그의 표시 및 이미지의 내재 크기를 지정한다(201–230). 메뉴 배경은 `images/primary\_nav\_bg\_repeat\_on.gif`를 참조한다(202). 해당 로컬 그림 파일 없음. |
| 232–248 | 페이지 제목·메타데이터·이모지 코드 — 페이지 제목은 Concentration Station Location input file (conc\_stat.151)이다(232). 구조화된 메타데이터(metadata)는 문서 URL, 경로 탐색, 언어와 게시 정보를 담는다(237). WordPress의 이모지 설정과 지원 검사 코드 및 빈 줄을 포함한다(242–248). |
| 249–285 | 사이트 서식 / WordPress 기본값 — 이모지, 블록 버튼과 파일 버튼의 CSS를 포함한다(249–263). 색상·그라데이션·글자 크기·간격·그림자 및 배치 프리셋(preset) CSS와 이어지는 빈 줄을 포함한다(264–285). |
| 286–303 | 사이트 지원·분석·배경 — 관리자 지원 표시의 CSS를 포함한다(286–288). 방문 분석 초기화 코드와 사이트 배경 CSS를 포함한다(292–300). 배경은 `grid\_bkgrd\_lt\_grey1.jpg`를 참조한다(300). 해당 로컬 그림 파일 없음. 이어지는 빈 줄도 포함한다(301–303). |
| 304–358 | 사이트 머리글·Community·Documentation — 빈 제목 마크업, ADCIRC 사이트 이름과 탐색 건너뛰기 링크를 포함한다(304–310). 개발자·개발 기관·사용자 메뉴를 포함한다(312–322). 사용자 매뉴얼, 입출력 문서, 변경 이력, 컴파일·명령행 옵션, 예제와 기술 보고서의 링크를 포함한다(323–358). |
| 359–401 | 사이트 메뉴 / Related software·News·Products·ASGS — 관련 도구, 사용자 모임·워크숍 자료, 예보·모의 사례, 제품과 ASGS 링크를 포함한다(359–400). 메뉴 사진 링크는 2018·2017·2016·2011·2010년 행사 사진을 가리킨다(368·370·374–375·387·389). 해당 로컬 그림 파일 없음. 마지막 빈 줄도 포함한다(401). |
| 402–409 | Concentration Station Location input file (conc_stat.151) / 적용 조건·표기 규칙 — 농도(concentration) 기록 지점 수가 음수일 때 이 파일을 읽는다고 적는다(406). 굵은 변수 행은 입력 행을 나타낸다(408). 빈 줄은 가독성을 위한 것이다(408). 반복문은 여러 입력 행을 나타낸다(408). 변수 정의는 링크로 제공한다(408). 적용 조건 원문: `The reading of the conc\_stat.151 file is triggered when the number of concentration recording stations ([NSTAC](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#NSTAE)) in the [fort.15 file](https://adcirc.org/home/documentation/users-manual-v53/input-file-descriptions/model-parameter-and-periodic-boundary-condition-file-fort-15/) is set to a negative value.` (406). |
| 410–417 | 입력 파일 구조 — 지점 수 뒤에 각 지점의 두 좌표 입력 행을 반복하는 구조를 제시한다(410–416). 이름·반복 범위·입력 행 원문: `[**NSTAC2**](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#NSTAC2)` (410); `for k=1,[NSTAC2](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#NSTAC2)` (412); `**[XEC(k)](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#XEC)**, **[YEC(k)](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#YEC)**` (414); `end k loop` (416). |
| 418–421 | Notes / 지점 수 처리 — 두 파일의 지점 수가 다르면 이 파일의 지점 수를 사용한다고 적는다(420). 나열된 지점이 부족하면 오류로 중단한다고 적는다(420). 지점이 많으면 처음 지정된 수만 사용한다고 적는다(420). 조건·수량 원문: `If the value of NSTAC2 differs from the value of NSTAC (as read from the fort.15 file) the value of NSTAC2 will be used. If there are fewer than NSTAC2 stations listed in the conc\_stat.151 file, ADCIRC will stop with an error. If there are more than NSTAC2 stations listed in the conc\_stat.151 file, only the first NSTAC2 of them will be used.` (420). |
| 422–436 | 사이트 말미 코드 — 유틸리티 표시, 문서 링크 사전 가져오기(prefetch) 규칙, 쿠키 안내 설정, 슬라이더 초기화와 New Relic 계측 정보를 포함한다(422–436). 중간 빈 줄과 주석 마크업도 포함한다. |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 166·202: CSS 배경이 참조하는 `images/primary\_nav\_divider.gif`와 `images/primary\_nav\_bg\_repeat\_on.gif`의 그림 파일 없음. 문서 상대 경로와 `models/ADCIRC/raw/`의 파일명을 확인했다.
- 300: CSS 배경이 참조하는 `grid\_bkgrd\_lt\_grey1.jpg`의 그림 파일 없음. `models/ADCIRC/raw/`의 파일명을 확인했다.
- 368·370·374–375·387·389: 메뉴 사진 링크의 `ADCIRC2018_Group_Photo2.jpg`, `2017ADCIRCUGMGroupPhoto.jpg`, `160506-A-Y1769-008-A-1.jpg`, `adcircBootCampers2016_small_caption.jpg`, `2011_ADCIRC_meeting.jpg`, `ADCIRC_Workshop2010_GroupPhoto2.png`의 그림 파일 없음. `models/ADCIRC/raw/`의 파일명을 확인했다.
- 310: `[Skip Navigation](#content-well)`을 포함하지만 이 Markdown 파일에 `content-well` 앵커를 정의한 마크업은 없다.
- 406: 링크 문구는 `NSTAC`인데 링크 대상의 조각 식별자는 `#NSTAE`이다. 링크 대상 문서의 내용은 이번 판독 범위에 포함하지 않았다.
