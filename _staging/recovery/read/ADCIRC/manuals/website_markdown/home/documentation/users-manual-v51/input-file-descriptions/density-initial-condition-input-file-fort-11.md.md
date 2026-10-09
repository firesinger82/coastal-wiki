---
file: models/ADCIRC/raw/manuals/website_markdown/home/documentation/users-manual-v51/input-file-descriptions/density-initial-condition-input-file-fort-11.md
lines: 559
sha256: 9b90083bf106fb16ef41c8254284aeee18931f563f89d813ae68db12c18fd4d6
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# density-initial-condition-input-file-fort-11.md — 판독 구간 기록

구간은 1행부터 559행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–12 | 웹페이지 계측 코드 — New Relic 초기화·로더와 이벤트·세션·오류·지표 처리 JavaScript 및 뒤 빈 줄을 포함한다(1–12). |
| 13–77 | 웹페이지 스타일(CSS) / 검색·제목·본문 틀 — 검색 입력·버튼, 링크와 제목, 글꼴·색상, 컨테이너와 오른쪽 콘텐츠 영역의 배치를 정의한다(13–77). |
| 78–142 | 웹페이지 스타일 / 콘텐츠·경로·인용 — 단일 열 콘텐츠, 본문 여백, 문단·링크, 오른쪽 목록, 탐색 경로(breadcrumb), 활성 메뉴, 인용문과 콘텐츠 영역을 정의한다(78–142). |
| 143–200 | 웹페이지 스타일 / 메뉴 — 메뉴 영역·항목·하위 메뉴·링크 배치를 정의한다(143–200). 메뉴 구분선 그림 경로는 images/primary_nav_divider.gif이다(166). 로컬 그림 파일 없음. |
| 201–228 | 웹페이지 스타일 / 메뉴 상태 — 마우스 진입·현재 페이지·하위 메뉴 표시와 제목 숨김을 정의한다(201–228). 메뉴 배경 그림 경로는 images/primary_nav_bg_repeat_on.gif이다(202). 로컬 그림 파일 없음. |
| 229–242 | 페이지 제목·구조화 메타데이터 — 자동 이미지 크기 스타일(230), 페이지 제목(232), 페이지 주소·발행일·수정일·언어·탐색 경로·사이트 검색 구조화 데이터(237)와 빈 줄을 포함한다. |
| 243–270 | WordPress 표시 코드 — CDATA 표기와 emoji 지원 검사·스크립트 로딩(243–247), emoji 스타일(250–260), 버튼·파일 링크 및 색·글꼴·간격·그림자·배치 스타일(263–270)을 포함한다. |
| 271–304 | 관리·방문 통계·배경 — 빈 줄, 관리 표시 스타일(287–289), 방문 통계 설정(293–299)과 사이트 배경 이미지 설정(301)을 포함한다. 배경 그림 파일명은 grid_bkgrd_lt_grey1.jpg이다. 로컬 그림 파일 없음. |
| 305–362 | 사이트 제목·탐색 메뉴 / Community·Documentation·Related software — 사이트 제목·탐색 건너뛰기(305–311), 개발·사용자 링크(313–323), V50–V53 설명서·입출력·버전 이력·컴파일·FAQ·보고서 링크(324–359)와 관련 소프트웨어 링크(360–362)를 나열한다. |
| 363–404 | 탐색 메뉴 / News·Products·ASGS·현재 경로 — 사용자 모임·워크숍·예측 링크(363–394), 제품과 ASGS 링크(395–401), 현재 문서의 탐색 경로(403)를 포함한다. 사진 링크(369·371·375·376·388·390)는 각각 2018 모임, 2017 모임, 2016 모임, 2016 Boot Camp, 2011 워크숍, 2010 워크숍 사진을 가리킨다. 이 설명은 링크 이름에 따른 것이다. 로컬 그림 파일 없음. |
| 405–410 | Density Initial Condition Input File (fort.11) / 적용과 읽는 법 — 경압(baroclinic) 실행에서만 사용한다고 적는다(407). 같은 행은 경압 2DDI 미지원과 IDEN이 0이 아닐 때 경압 3D 실행을 명시한다. 굵은 변수 줄은 입력 데이터 한 줄이며 빈 줄은 가독성용이고 루프는 여러 입력 줄을 나타낸다(409). 원문: `# Density Initial Condition Input File (fort.11)` (405); `This file is only used for a baroclinic run.Baroclinic 2DDI runs are not yet supported.Baroclinic 3D runs occur if [IDEN](http://adcirc.org/home/documentation/users-manual-v50/parameter-definitions#IDEN) is not equal to 0.` (407); `The basic file structure is shown below. Each line of input data is represented by a line containing the input variable name(s) in bold face type. Blank lines are only to enhance readability. Loops indicate multiple lines of input. Definitions of each variable are provided via hot links.` (409). |
| 411–426 | 경압 2DDI / IDEN 1 또는 -1 — 두 헤더 줄, NVP, NVP회 반복하는 jki와 DASIGT(jki) 입력을 제시한다(411–425). 이 구간은 미지원 진술과 함께 문서에 제시된 형식이다. 원문: `File structure for a baroclinic 2DDI run:` (411); `If [IDEN](../../parameter-definitions#IDEN) = 1 or -1` (413); `**Header Line 1**` (415); `**Header Line 2**` (417); `**[NVP](../../parameter-definitions#NVP)**` (419); `for k=1 to **[NVP](../../parameter-definitions#NVP)**` (421); `**[jki](../../parameter-definitions#jki),[DASIGT(jki)](../../parameter-definitions#DASIGT)**` (423); `end k loop` (425). |
| 427–440 | 경압 2DDI / IDEN 2 또는 -2 — 두 헤더 줄, NVP, NVP회 반복하는 jki와 DASALT(jki) 입력을 제시한다(427–439). 원문: `If [IDEN](../../parameter-definitions#IDEN) = 2 or -2` (427); `**Header Line 1**` (429); `**Header Line 2**` (431); `**[NVP](../../parameter-definitions#NVP)**` (433); `for k=1 to **[NVP](../../parameter-definitions#NVP)**` (435); `**[jki](../../parameter-definitions#jki),[DASALT(jki)](../../parameter-definitions#DASALT)**` (437); `end k loop` (439). |
| 441–454 | 경압 2DDI / IDEN 3 또는 -3 — 두 헤더 줄, NVP, NVP회 반복하는 jki와 DATEMP(jki) 입력을 제시한다(441–453). 원문: `If [IDEN](../../parameter-definitions#IDEN) = 3 or -3` (441); `**Header Line 1**` (443); `**Header Line 2**` (445); `**[NVP](../../parameter-definitions#NVP)**` (447); `for k=1 to **[NVP](../../parameter-definitions#NVP)**` (449); `**[jki](../../parameter-definitions#jki),[DATEMP(jki)](../../parameter-definitions#DATEMP)**` (451); `end k loop` (453). |
| 455–468 | 경압 2DDI / IDEN 4 또는 -4 — 두 헤더 줄, NVP, NVP회 반복하는 jki·DATEMP(jki)·DASALT(jki) 입력을 제시한다(455–467). 원문: `If [IDEN](../../parameter-definitions#IDEN) = 4 or -4` (455); `**Header Line 1**` (457); `**Header Line 2**` (459); `**[NVP](../../parameter-definitions#NVP)**` (461); `for k=1 to **[NVP](../../parameter-definitions#NVP)**` (463); `**[jki](../../parameter-definitions#jki), [DATEMP(jki)](../../parameter-definitions#DATEMP), [DASALT(jki)](../../parameter-definitions#DASALT)**` (465); `end k loop` (467). |
| 469–488 | 경압 3D / IDEN 1 또는 -1 — 두 헤더 줄, NVN·NVP, NVP 외부 반복과 NVN 내부 반복, k·j·SIGT(NHNN,NVNN) 입력을 제시한다(469–487). 원문: `File structure for a baroclinic 3D run:` (469); `If [IDEN](../../parameter-definitions#IDEN) = 1 or -1` (471); `**Header Line 1**` (473); `**Header Line 2**` (475); `**[NVN](../../parameter-definitions#NVN), [NVP](../../parameter-definitions#NVP)**` (477); `for k=1 to **[NVP](../../parameter-definitions#NVP)**` (479); `for j=1 to **[NVN](../../parameter-definitions#NVN)**` (481); `**k, j, [SIGT(NHNN,NVNN)](../../parameter-definitions#SIGT)**` (483); `end j loop` (485); `end k loop` (487). |
| 489–506 | 경압 3D / IDEN 2 또는 -2 — 두 헤더 줄, NVN·NVP, NVP 외부 반복과 NVN 내부 반복, k·j·SAL(k,j) 입력을 제시한다(489–505). 원문: `If [IDEN](../../parameter-definitions#IDEN) = 2 or -2` (489); `**Header Line 1**` (491); `**Header Line 2**` (493); `**[NVN](../../parameter-definitions#NVN), [NVP](../../parameter-definitions#NVP)**` (495); `for k=1 to **[NVP](../../parameter-definitions#NVP)**` (497); `for j=1 to **[NVN](../../parameter-definitions#NVN)**` (499); `**[k, j](../../parameter-definitions#NHNN), [SAL(k,j)](../../parameter-definitions#SAL)**` (501); `end j loop` (503); `end k loop` (505). |
| 507–524 | 경압 3D / IDEN 3 또는 -3 — 두 헤더 줄, NVN·NVP, NVP 외부 반복과 NVN 내부 반복, k·j·TEMP(k,j) 입력을 제시한다(507–523). 원문: `If [IDEN](../../parameter-definitions#IDEN) = 3 or -3` (507); `**Header Line 1**` (509); `**Header Line 2**` (511); `**[NVN](../../parameter-definitions#NVN), [NVP](../../parameter-definitions#NVP)**` (513); `for k=1 to **[NVP](../../parameter-definitions#NVP)**` (515); `for j=1 to **[NVN](../../parameter-definitions#NVN)**` (517); `**k, j, [TEMP(k,j)](../../parameter-definitions#TEMP)**` (519); `end j loop` (521); `end k loop` (523). |
| 525–544 | 경압 3D / IDEN 4 또는 -4·수직 순서 — 두 헤더 줄, NVN·NVP, NVP 외부 반복과 NVN 내부 반복, k·j·TEMP(k,j)·SAL(k,j) 입력을 제시한다(525–541). 저면은 j=1이고 수면은 j=NVN이라고 적는다(543). 원문: `If [IDEN](../../parameter-definitions#IDEN) = 4 or -4` (525); `**Header Line 1**` (527); `**Header Line 2**` (529); `**[NVN](../../parameter-definitions#NVN), [NVP](../../parameter-definitions#NVP)**` (531); `for k=1 to **[NVP](../../parameter-definitions#NVP)**` (533); `for j=1 to **[NVN](../../parameter-definitions#NVN)**` (535); `**k, j, [TEMP(k,j)](../../parameter-definitions#TEMP),[SAL(k,j)](../../parameter-definitions#SAL)**` (537); `end j loop` (539); `end k loop` (541); `**Note:** j=1 at bottom, j=[NVN](../../parameter-definitions#NVN) at surface` (543). |
| 545–559 | 웹페이지 끝 코드 — 빈 줄, 유틸리티 표시 호출(547), 미리 가져오기 규칙(549), 쿠키 배너(552–554), 슬라이드 표시 초기화와 New Relic 정보(558–559)를 포함한다. |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 166·202·301: CSS에서 참조한 primary_nav_divider.gif, primary_nav_bg_repeat_on.gif, grid_bkgrd_lt_grey1.jpg의 로컬 사본을 raw/manuals 아래에서 찾지 못했다. 그림 파일 없음.
- 369·371·375·376·388·390: 탐색 메뉴의 모임·워크숍 사진 링크 6개의 로컬 사본을 raw/manuals 아래에서 찾지 못했다. 그림 파일 없음.
- 407·411–467: 407행은 경압 2DDI 실행이 아직 지원되지 않는다고 적는다. 411–467행은 경압 2DDI의 IDEN 값별 입력 형식을 제시한다.
- 407: V51 문서의 IDEN 설명 링크는 users-manual-v50/parameter-definitions#IDEN을 가리킨다.
- 413–543: 상대 링크 ../../parameter-definitions를 현재 Markdown 파일의 위치에서 해석하면 home/documentation/parameter-definitions를 가리킨다. 해당 경로, 같은 이름의 .md 파일과 그 경로의 index.md 파일이 없다.
- 479·481·483: 반복 인덱스는 k와 j이다. SIGT 입력 줄의 첨자는 NHNN과 NVNN이다. 두 첨자의 관계 설명은 이 파일에 없다.
- 501: k, j 전체가 parameter-definitions#NHNN에 연결되어 있다.
