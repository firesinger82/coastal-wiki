---
file: models/ADCIRC/raw/manuals/website_markdown/home/documentation/users-manual-v50/input-file-descriptions/density-initial-condition-input-file-fort-11.md
lines: 559
sha256: d2462d354ecac5603e3539efad301d72306323c602d9f139bc38623e915af2ec
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# input-file-descriptions/density-initial-condition-input-file-fort-11.md — 판독 구간 기록

구간은 1행부터 559행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–12 | 웹사이트 수집 내용 — New Relic 초기 설정과 압축된 브라우저 계측 스크립트가 들어 있다(1–2). 이어지는 빈 줄도 포함한다(3–12). |
| 13–85 | 웹사이트 CSS / 검색·본문 배치 — 검색 필드와 검색 버튼, 제목·본문·링크, 컨테이너·헤더·콘텐츠 영역의 스타일을 정의한다(13–85). 주석도 포함한다. |
| 86–161 | 웹사이트 CSS / 본문·탐색 메뉴 — 콘텐츠 영역·문단·링크·탐색 경로(breadcrumb)·인용문·메뉴의 스타일을 정의한다(86–161). |
| 162–230 | 웹사이트 CSS / 하위 메뉴·그림 배치 — 메뉴 항목의 배경 그림 참조, 하위 메뉴·마우스 반응·현재 페이지 스타일과 그림의 표시 크기 설정을 포함한다(162–230). |
| 231–272 | 페이지 제목·구조화 정보·WordPress 표시 코드 — 페이지 제목과 schema.org의 페이지·탐색 경로·웹사이트 정보를 포함한다(232·237). 이모지(emoji) 지원 검사 스크립트와 이모지·버튼·색상·간격 CSS가 들어 있다(243–270). 빈 줄과 주석도 포함한다. |
| 273–304 | 웹사이트 관리·통계·배경 설정 — 빈 줄, 관리 표시 CSS, Beehive 통계 초기 설정과 배경 그림 URL을 포함한다(273–301). |
| 305–359 | 사이트 공통 탐색 / Community·Documentation — ADCIRC 사이트 제목, Skip Navigation 링크와 개발자·사용자·매뉴얼 V50–v53·컴파일 옵션·예제·보고서·관련 문헌 링크를 나열한다(305–359). |
| 360–402 | 사이트 공통 탐색 / Related software·News·Products·ASGS — 유틸리티·격자 생성기·행사 자료·사진·예보·제품·ASGS 링크를 나열한다(360–401). 마지막 빈 줄도 포함한다(402). |
| 403–410 | Density Initial Condition Input File (fort.11) / 사용 조건 — 탐색 경로와 표제를 포함한다(403·405). 이 파일은 경압(baroclinic) 실행에만 사용한다고 적는다(407). 경압 2DDI 실행은 아직 지원하지 않는다고 적는다(407). 경압 3D 실행 조건과 입력 줄·빈 줄·반복문·변수 정의 링크의 해석을 원문으로 옮긴다(407·409). 원문: `This file is only used for a baroclinic run.Baroclinic 2DDI runs are not yet supported.Baroclinic 3D runs occur if [IDEN](http://adcirc.org/home/documentation/users-manual-v50/parameter-definitions#IDEN) is not equal to 0.` (407); `The basic file structure is shown below. Each line of input data is represented by a line containing the input variable name(s) in bold face type. Blank lines are only to enhance readability. Loops indicate multiple lines of input. Definitions of each variable are provided via hot links.` (409). |
| 411–426 | File structure for a baroclinic 2DDI run / IDEN의 첫 분기 — 헤더 두 줄 뒤 절점 수와 절점별 DASIGT 자료를 입력하는 형식을 제시한다(411–425). 적용 조건과 입력 형식 원문을 옮긴다. 원문: `File structure for a baroclinic 2DDI run:` (411); `If [IDEN](../../parameter-definitions#IDEN) = 1 or -1` (413); `**Header Line 1**` (415); `**Header Line 2**` (417); `**[NVP](../../parameter-definitions#NVP)**` (419); `for k=1 to **[NVP](../../parameter-definitions#NVP)**` (421); `**[jki](../../parameter-definitions#jki),[DASIGT(jki)](../../parameter-definitions#DASIGT)**` (423); `end k loop` (425). |
| 427–440 | 경압 2DDI 형식 / 두 번째 분기 — 헤더 두 줄 뒤 절점 수와 절점별 DASALT 자료를 입력한다(427–439). 적용 조건과 입력 형식 원문을 옮긴다. 원문: `If [IDEN](../../parameter-definitions#IDEN) = 2 or -2` (427); `**Header Line 1**` (429); `**Header Line 2**` (431); `**[NVP](../../parameter-definitions#NVP)**` (433); `for k=1 to **[NVP](../../parameter-definitions#NVP)**` (435); `**[jki](../../parameter-definitions#jki),[DASALT(jki)](../../parameter-definitions#DASALT)**` (437); `end k loop` (439). |
| 441–454 | 경압 2DDI 형식 / 세 번째 분기 — 헤더 두 줄 뒤 절점 수와 절점별 DATEMP 자료를 입력한다(441–453). 적용 조건과 입력 형식 원문을 옮긴다. 원문: `If [IDEN](../../parameter-definitions#IDEN) = 3 or -3` (441); `**Header Line 1**` (443); `**Header Line 2**` (445); `**[NVP](../../parameter-definitions#NVP)**` (447); `for k=1 to **[NVP](../../parameter-definitions#NVP)**` (449); `**[jki](../../parameter-definitions#jki),[DATEMP(jki)](../../parameter-definitions#DATEMP)**` (451); `end k loop` (453). |
| 455–468 | 경압 2DDI 형식 / 네 번째 분기 — 헤더 두 줄 뒤 절점 수와 절점별 DATEMP·DASALT 자료를 함께 입력한다(455–467). 적용 조건과 입력 형식 원문을 옮긴다. 원문: `If [IDEN](../../parameter-definitions#IDEN) = 4 or -4` (455); `**Header Line 1**` (457); `**Header Line 2**` (459); `**[NVP](../../parameter-definitions#NVP)**` (461); `for k=1 to **[NVP](../../parameter-definitions#NVP)**` (463); `**[jki](../../parameter-definitions#jki), [DATEMP(jki)](../../parameter-definitions#DATEMP), [DASALT(jki)](../../parameter-definitions#DASALT)**` (465); `end k loop` (467). |
| 469–488 | File structure for a baroclinic 3D run / 첫 분기 — 헤더 두 줄 뒤 수직 절점 수와 수평 절점 수를 적고 두 겹 반복문으로 SIGT 자료를 입력한다(469–487). 첨자 표기와 적용 조건을 원문으로 유지한다. 원문: `File structure for a baroclinic 3D run:` (469); `If [IDEN](../../parameter-definitions#IDEN) = 1 or -1` (471); `**Header Line 1**` (473); `**Header Line 2**` (475); `**[NVN](../../parameter-definitions#NVN), [NVP](../../parameter-definitions#NVP)**` (477); `for k=1 to **[NVP](../../parameter-definitions#NVP)**` (479); `for j=1 to **[NVN](../../parameter-definitions#NVN)**` (481); `**k, j, [SIGT(NHNN,NVNN)](../../parameter-definitions#SIGT)**` (483); `end j loop` (485); `end k loop` (487). |
| 489–506 | 경압 3D 형식 / 두 번째 분기 — 헤더 두 줄과 두 절점 수 뒤 수평·수직 절점을 반복하며 SAL 자료를 입력한다(489–505). 적용 조건과 입력 형식 원문을 옮긴다. 원문: `If [IDEN](../../parameter-definitions#IDEN) = 2 or -2` (489); `**Header Line 1**` (491); `**Header Line 2**` (493); `**[NVN](../../parameter-definitions#NVN), [NVP](../../parameter-definitions#NVP)**` (495); `for k=1 to **[NVP](../../parameter-definitions#NVP)**` (497); `for j=1 to **[NVN](../../parameter-definitions#NVN)**` (499); `**[k, j](../../parameter-definitions#NHNN), [SAL(k,j)](../../parameter-definitions#SAL)**` (501); `end j loop` (503); `end k loop` (505). |
| 507–524 | 경압 3D 형식 / 세 번째 분기 — 헤더 두 줄과 두 절점 수 뒤 수평·수직 절점을 반복하며 TEMP 자료를 입력한다(507–523). 적용 조건과 입력 형식 원문을 옮긴다. 원문: `If [IDEN](../../parameter-definitions#IDEN) = 3 or -3` (507); `**Header Line 1**` (509); `**Header Line 2**` (511); `**[NVN](../../parameter-definitions#NVN), [NVP](../../parameter-definitions#NVP)**` (513); `for k=1 to **[NVP](../../parameter-definitions#NVP)**` (515); `for j=1 to **[NVN](../../parameter-definitions#NVN)**` (517); `**k, j, [TEMP(k,j)](../../parameter-definitions#TEMP)**` (519); `end j loop` (521); `end k loop` (523). |
| 525–544 | 경압 3D 형식 / 네 번째 분기·수직 순서 — 헤더 두 줄과 두 절점 수 뒤 TEMP·SAL 자료를 함께 입력한다(525–541). 수직 첨자의 저면·수면 위치를 명시한다(543). 이 구간에는 변수의 기본값·단위가 없다. 적용 조건·입력 형식·수직 순서 원문을 옮긴다. 원문: `If [IDEN](../../parameter-definitions#IDEN) = 4 or -4` (525); `**Header Line 1**` (527); `**Header Line 2**` (529); `**[NVN](../../parameter-definitions#NVN), [NVP](../../parameter-definitions#NVP)**` (531); `for k=1 to **[NVP](../../parameter-definitions#NVP)**` (533); `for j=1 to **[NVN](../../parameter-definitions#NVN)**` (535); `**k, j, [TEMP(k,j)](../../parameter-definitions#TEMP),[SAL(k,j)](../../parameter-definitions#SAL)**` (537); `end j loop` (539); `end k loop` (541); `**Note:** j=1 at bottom, j=[NVN](../../parameter-definitions#NVN) at surface` (543). |
| 545–559 | 웹사이트 후처리 — 빈 줄과 화면 유틸리티 호출, 링크 미리 가져오기(prefetch) 설정, 쿠키 안내, jQuery 호출, New Relic 페이지 계측 정보를 포함한다(545–559). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 407·411–467행: 407행은 경압 2DDI 실행을 `not yet supported`라고 적는다. 411–467행은 경압 2DDI 실행의 파일 형식을 제시한다.
- 479–483·501행: 반복문은 `k`, `j`를 사용한다. 483행의 `SIGT`는 `NHNN,NVNN`을 첨자로 적는다. 이 파일은 두 첨자 쌍의 관계를 설명하지 않는다. 501행의 `[k, j]` 링크는 `#NHNN` 한 앵커를 가리킨다.
