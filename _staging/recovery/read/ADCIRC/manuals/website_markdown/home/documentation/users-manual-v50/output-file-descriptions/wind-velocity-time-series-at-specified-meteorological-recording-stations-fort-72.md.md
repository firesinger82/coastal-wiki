---
file: models/ADCIRC/raw/manuals/website_markdown/home/documentation/users-manual-v50/output-file-descriptions/wind-velocity-time-series-at-specified-meteorological-recording-stations-fort-72.md
lines: 443
sha256: cacd3c37125f6841d86de329cd4eb9383dfbde30756aa014b4fa31ce95412d07
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# wind-velocity-time-series-at-specified-meteorological-recording-stations-fort-72.md — 판독 구간 기록

구간은 1행부터 443행까지 빈틈없이 이어진다.

본문 원문은 행별로 인용한다. 표 안에서 인용문의 세로줄은 Markdown 이스케이프로 표시한다. 수식 이미지의 식은 LaTeX로 전사한다.

| 구간 | 내용 |
|---|---|
| 1–12 | 웹페이지 계측 스크립트 — New Relic 초기 설정과 압축된 로더 JavaScript가 있다(1–2). 뒤 빈 줄을 포함한다(3–12). |
| 13–77 | 웹페이지 CSS / 검색·헤더·컨테이너 — 검색창과 검색 버튼, 제목과 본문 글꼴, 페이지 컨테이너, 헤더, 태그와 오른쪽 콘텐츠 영역의 표시 설정이 있다(13–77). |
| 78–142 | 웹페이지 CSS / 본문·링크·경로 — 단일 열 본문, 문단, 링크, 오른쪽 목록, 탐색 경로(breadcrumb), 활성 메뉴, 인용문과 다중 열 본문의 표시 설정이 있다(78–142). |
| 143–200 | 웹페이지 CSS / 탐색 메뉴 — 상위 메뉴와 하위 메뉴의 너비, 위치, 숨김과 링크 표시를 정의한다(143–200). 배경 이미지 URL이 있다(166). |
| 201–230 | 웹페이지 CSS / 메뉴 상태 — 마우스가 올라간 메뉴와 현재 메뉴 항목의 표시를 정의한다(201–225). 슬라이더 높이, 메뉴 글꼴, 태그 숨김과 자동 크기 이미지 설정을 포함한다(226–230). 배경 이미지 URL이 있다(202). |
| 231–242 | 페이지 제목·구조화 메타데이터 — 페이지 제목(232)과 페이지 URL, 발행·수정 시각, 탐색 경로, 웹사이트와 검색 동작의 JSON-LD 메타데이터가 있다(237). 빈 줄을 포함한다. 로그층 수식 이미지의 URL을 기본 이미지와 썸네일로도 참조한다(237). 본문에서 같은 이름의 로컬 AVIF 사본을 확인했다(1369). |
| 243–270 | WordPress 표시 코드 — 이모지(emoji) 지원 검사와 로더 JavaScript, CDATA 표기와 자동 생성 주석을 포함한다(243–247). 이모지, 버튼, 색상·비율·글꼴·간격·그림자, 레이아웃과 인용문 CSS를 포함한다(250–270). |
| 271–304 | 페이지 계측·배경 — 빈 줄과 관리자 표시 CSS를 포함한다(271–292). Beehive 계측 설정이 있다(293–299). 페이지 배경 이미지 URL과 배경 표시 CSS가 있다(301). |
| 305–359 | 사이트 머리말·문서 탐색 — 빈 제목 마크업(305), ADCIRC 사이트 제목과 설명(307–309), 탐색 건너뛰기 링크(311)를 포함한다. 공동체·개발자·사용자 메뉴(313–323)와 사용자 설명서, 입출력 문서, 버전 이력, 예제, 보고서, 논문과 특별 기능 링크를 포함한다(324–359). |
| 360–402 | 관련 소프트웨어·소식·제품 탐색 — 유틸리티와 격자 생성기 링크(360–362), 사용자 모임·워크숍 자료와 사진 링크(363–394), 제품·예측·격자·표면 유류 이동과 ASGS 링크(395–401)를 포함한다. 사진은 일반 링크로 제시된다. |
| 403–406 | 탐색 경로·본문 제목 — V50 설명서에서 현재 페이지까지의 탐색 경로(403)와 본문 제목(405), 빈 줄을 포함한다. |
| 407–412 | Wind Velocity Time Series / 출력 설명 — fort.15에서 정한 기상 관측소의 풍속(wind velocity) 또는 응력(stress) 시계열을 출력한다고 적는다(407). 굵은 변수명 줄이 실제 출력 줄에 대응하며 빈 줄은 가독성용이고 반복문은 여러 출력 줄을 뜻한다고 설명한다(409). NOUTM에 따른 ASCII·이진(binary) 형식 조건을 제시한다(411). 원문: `Wind velocity or stress time series output at the meteorological recording stations as specified in the [Model Parameter and Periodic Boundary Condition File](../../input-file-descriptions/model-parameter-and-periodic-boundary-condition-file-fort-15).` (407); `The basic file structure is shown below. Each line of output is represented by a line containing the output variable name(s) in bold face type. Blank lines are to enhance readability. Loops indicate multiple lines of output. Definitions of each variable are provided via hot links.` (409); `Output may be in ascii or binary format depending on how [NOUTM](http://adcirc.org/home/documentation/users-manual-v50/parameter-definitions#NOUTM) is set in the [Model Parameter and Periodic Boundary Condition File](../../input-file-descriptions/model-parameter-and-periodic-boundary-condition-file-fort-15)` (411). |
| 413–424 | fort.72 파일 구조 — 실행·격자 식별자 줄(413), 자료 수·관측소 수·시간 간격 곱·출력 간격·기록 유형 줄(415), 모델 시각·단계 번호 줄(417)을 제시한다. 관측소 반복문의 시작·풍속 또는 응력 성분 줄·종료를 포함한다(419–423). 원문: `[**RUNDES**](http://adcirc.org/home/documentation/users-manual-v50/parameter-definitions#RUNDES), [**RUNID**](http://adcirc.org/home/documentation/users-manual-v50/parameter-definitions#RUNID), [**AGRID**](http://adcirc.org/home/documentation/users-manual-v50/parameter-definitions#AGRID)` (413); `[**NTRSPM**](http://adcirc.org/home/documentation/users-manual-v50/parameter-definitions#NTRSPM), [**NSTAM**](http://adcirc.org/home/documentation/users-manual-v50/parameter-definitions#NSTAM), **[DTDP](http://adcirc.org/home/documentation/users-manual-v50/parameter-definitions#DTDP)\***[**NSPOOLM**](http://adcirc.org/home/documentation/users-manual-v50/parameter-definitions#NSPOOLM), [**NSPOOLM**](http://adcirc.org/home/documentation/users-manual-v50/parameter-definitions#NSPOOLM), [**IRTYPE**](http://adcirc.org/home/documentation/users-manual-v50/parameter-definitions#IRTYPE)` (415); `[**TIME**](http://adcirc.org/home/documentation/users-manual-v50/parameter-definitions#TIME), [**IT**](http://adcirc.org/home/documentation/users-manual-v50/parameter-definitions#IT)` (417); `for k=1, [NSTAM](http://adcirc.org/home/documentation/users-manual-v50/parameter-definitions#NSTAM)` (419); `**k**, **[RMU00(k), RMV00(k)](http://adcirc.org/home/documentation/users-manual-v50/parameter-definitions#RMU00_RMV00)**` (421); `end k loop` (423). |
| 425–428 | Note / 이진 출력 — 이진 출력일 때 관측소 번호 k를 출력에 포함하지 않는다고 명시한다(425–427). 원문: `**Note:**` (425); `If binary output is specified, the station number (k) is not included in the output.` (427). |
| 429–443 | 웹페이지 꼬리말 — 빈 줄과 유틸리티 표시 호출(429–431), 링크 사전 가져오기(prefetch) 설정(433), 쿠키 안내문·CDATA 표기(436–438), 슬라이더 클래스 제거와 New Relic 계측 정보(442–443)를 포함한다. |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 166·202·301: CSS는 `images/primary\_nav\_divider.gif`, `images/primary\_nav\_bg\_repeat\_on.gif`, `grid\_bkgrd\_lt\_grey1.jpg`를 배경으로 참조한다. ADCIRC 폴더의 파일명 검색에서 해당 로컬 사본을 찾지 못했다. 그림 파일 없음.
- 413·415·417·421: 변수 정의 링크는 `parameter-definitions#RUNDES`, `#NTRSPM`, `#TIME`, `#RMU00_RMV00` 등의 조각 이름을 사용한다. 함께 판독한 parameter-definitions.md에는 이 이름의 명시적 앵커나 해당 제목이 없다.
