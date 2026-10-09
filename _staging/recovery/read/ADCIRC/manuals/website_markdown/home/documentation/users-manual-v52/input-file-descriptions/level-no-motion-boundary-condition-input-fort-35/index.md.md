---
file: models/ADCIRC/raw/manuals/website_markdown/home/documentation/users-manual-v52/input-file-descriptions/level-no-motion-boundary-condition-input-fort-35/index.md
lines: 432
sha256: 7f6d012d93430a9e2ee391e5f109c77bf2775ffdf6e493c1a8e54b803618c71c
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# index.md — 판독 구간 기록

구간은 1행부터 432행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–12 | 웹 페이지 시작 코드 — New Relic 브라우저 계측 JavaScript를 포함한다(1–2). 뒤 빈 줄을 포함한다(3–12). |
| 13–77 | 웹 페이지 스타일 / 검색창·머리말·컨테이너 — CSS가 검색창, 문서 제목, 본문 글꼴과 컨테이너 크기를 지정한다(13–77). |
| 78–142 | 웹 페이지 스타일 / 본문·탐색 경로 — CSS가 본문 열, 문단, 링크, 탐색 경로(breadcrumbs)와 인용문 표시를 지정한다(78–142). |
| 143–200 | 웹 페이지 스타일 / 메뉴 — CSS가 메뉴와 하위 메뉴 표시를 지정한다(143–200). 메뉴 배경 이미지 경로를 포함한다(166). `images/primary\_nav\_divider.gif` (166): 그림 파일 없음. |
| 201–228 | 웹 페이지 스타일 / 메뉴 선택 상태 — CSS가 메뉴에 마우스를 올린 상태와 현재 페이지 메뉴 표시를 지정한다(201–228). 배경 이미지 경로를 포함한다(202). `images/primary\_nav\_bg\_repeat\_on.gif` (202): 그림 파일 없음. |
| 229–267 | 웹 페이지 제목·메타데이터·WordPress 표시 코드 — 페이지 제목(232), 구조화 메타데이터(JSON-LD)(235), 이모지(emoji) 지원 JavaScript(240–244)와 WordPress 표시 CSS(247–267)를 포함한다. |
| 268–308 | 웹 페이지 분석 코드·배경·사이트 머리말 — 빈 줄, 관리 표시 CSS(284–286), 방문 분석 JavaScript(290–296), 사이트 배경 이미지 CSS(298), ADCIRC 사이트 머리말과 탐색 건너뛰기 링크(302–308)를 포함한다. `https://adcirc.org/wp-content/uploads/sites/2255/2013/03/grid\_bkgrd\_lt\_grey1.jpg` (298): 그림 파일 없음. |
| 309–356 | 사이트 메뉴 / Community·Documentation — 개발자와 사용자 링크(310–320)를 제공한다. 매뉴얼 판본, 컴파일·명령행 옵션, FAQ, 예제와 보고서 링크를 제공한다(321–356). |
| 357–399 | 사이트 메뉴 / Related software·News·Products·ASGS — 유틸리티와 격자 작성 도구 링크(357–359), 행사·사진·발표 자료 링크(360–391), 제품과 ASGS 링크(392–398)를 제공한다. 마지막 빈 줄을 포함한다(399). `https://adcirc.org/wp-content/uploads/sites/2255/2018/04/ADCIRC2018_Group_Photo2.jpg` (366): 그림 파일 없음. `https://adcirc.org/wp-content/uploads/sites/2255/2017/06/2017ADCIRCUGMGroupPhoto.jpg` (368): 그림 파일 없음. `https://adcirc.org/wp-content/uploads/sites/2255/2016/05/160506-A-Y1769-008-A-1.jpg` (372): 그림 파일 없음. `https://adcirc.org/wp-content/uploads/sites/2255/2016/05/adcircBootCampers2016_small_caption.jpg` (373): 그림 파일 없음. `https://adcirc.org/wp-content/uploads/sites/2255/2018/11/2011_ADCIRC_meeting.jpg` (385): 그림 파일 없음. `https://adcirc.org/wp-content/uploads/sites/2255/2018/11/ADCIRC_Workshop2010_GroupPhoto2.png` (387): 그림 파일 없음. |
| 400–417 | Level of No Motion Boundary Condition Input — 무운동면(level of no motion) 경계조건(boundary condition) 파일 fort.35의 적용 조건을 제시한다(404). 3차원 경압(baroclinic) 모의에서 BCFLAG_LNM을 1로 설정하면 읽는다고 적는다(404). 자료 집합 반복마다 날짜 주석 행을 먼저 두고, 해양 경계 노드(ocean boundary node) 반복마다 k와 elevation_change를 둔다(406–416). 파일 형식과 반복 종료문을 원문 그대로 옮긴다. 원문: `The ADCIRC Level of No Motion Boundary Condition Input File (fort.35) is read in for 3D baroclinic simulations when the [**BCFLAG\_LNM**](https://adcirc.org/home/documentation/users-manual-v52/parameter-definitions#BCFLAG_LNM) (boundary condition flag for the level of no motion) is set to 1 in the [fort.15 file](https://adcirc.org/home/documentation/users-manual-v50/input-file-descriptions/model-parameter-and-periodic-boundary-condition-file-fort-15/ "Model Parameter and Periodic Boundary Condition File (fort.15)"). Its format is as follows:` (404); `for i=1 to numberOfDataSets` (406); `**comment line (date)**` (408); `for k=1 to number\_of\_ocean\_boundary\_nodes` (410); `**k, elevation\_change**` (412); `end k loop` (414); `end i loop` (416). |
| 418–432 | 웹 페이지 끝 코드 — 빈 줄과 사이트 유틸리티 호출(420), 문서 링크 미리 가져오기(prefetch) JSON(422), 쿠키(cookie) 안내 설정(425–427), jQuery 표시 코드(431), New Relic 페이지 계측 정보(432)를 포함한다. |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 404: 이 파일의 탐색 경로와 제목은 v52 매뉴얼에 속한다(400–402). 본문의 fort.15 링크는 `users-manual-v50` 경로를 사용한다.
- 406–412: numberOfDataSets와 number_of_ocean_boundary_nodes의 지정 방법, 날짜 주석의 형식, elevation_change의 단위를 이 파일에서 정의하지 않는다.
- 166: `images/primary\_nav\_divider.gif`의 로컬 사본을 찾지 못했다. 그림 파일 없음. 상대 images 경로와 models/ADCIRC/raw 내 파일명 목록을 확인했다.
- 202: `images/primary\_nav\_bg\_repeat\_on.gif`의 로컬 사본을 찾지 못했다. 그림 파일 없음. 상대 images 경로와 models/ADCIRC/raw 내 파일명 목록을 확인했다.
- 298: `https://adcirc.org/wp-content/uploads/sites/2255/2013/03/grid\_bkgrd\_lt\_grey1.jpg`의 로컬 사본을 찾지 못했다. 그림 파일 없음. 상대 images 경로와 models/ADCIRC/raw 내 파일명 목록을 확인했다.
- 366: `https://adcirc.org/wp-content/uploads/sites/2255/2018/04/ADCIRC2018_Group_Photo2.jpg`의 로컬 사본을 찾지 못했다. 그림 파일 없음. 상대 images 경로와 models/ADCIRC/raw 내 파일명 목록을 확인했다.
- 368: `https://adcirc.org/wp-content/uploads/sites/2255/2017/06/2017ADCIRCUGMGroupPhoto.jpg`의 로컬 사본을 찾지 못했다. 그림 파일 없음. 상대 images 경로와 models/ADCIRC/raw 내 파일명 목록을 확인했다.
- 372: `https://adcirc.org/wp-content/uploads/sites/2255/2016/05/160506-A-Y1769-008-A-1.jpg`의 로컬 사본을 찾지 못했다. 그림 파일 없음. 상대 images 경로와 models/ADCIRC/raw 내 파일명 목록을 확인했다.
- 373: `https://adcirc.org/wp-content/uploads/sites/2255/2016/05/adcircBootCampers2016_small_caption.jpg`의 로컬 사본을 찾지 못했다. 그림 파일 없음. 상대 images 경로와 models/ADCIRC/raw 내 파일명 목록을 확인했다.
- 385: `https://adcirc.org/wp-content/uploads/sites/2255/2018/11/2011_ADCIRC_meeting.jpg`의 로컬 사본을 찾지 못했다. 그림 파일 없음. 상대 images 경로와 models/ADCIRC/raw 내 파일명 목록을 확인했다.
- 387: `https://adcirc.org/wp-content/uploads/sites/2255/2018/11/ADCIRC_Workshop2010_GroupPhoto2.png`의 로컬 사본을 찾지 못했다. 그림 파일 없음. 상대 images 경로와 models/ADCIRC/raw 내 파일명 목록을 확인했다.

