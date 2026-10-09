---
file: models/ADCIRC/raw/manuals/website_markdown/home/documentation/users-manual-v53/output-file-descriptions/inundation-rising-at-the-end-of-the-run-flag-file-endrisinginun-63/index.md
lines: 444
sha256: d8be55ab71e9794b50f6715f890be2a1fd3bc672f56113f7ea4658d0aa9ccd9e
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# index.md — 판독 구간 기록

구간은 1행부터 444행까지 빈틈없이 이어진다.

| 구간 | 내용 |
| --- | --- |
| 1–12 | 문서 앞 웹 계측 스크립트 — New Relic 초기 설정과 압축된 브라우저 계측(instrumentation) JavaScript가 들어 있다(1–2). 뒤에는 빈 줄이 이어진다(3–12). |
| 13–70 | 사이트 스타일시트(Cascading Style Sheets, CSS) / 검색창·제목·기본 배치 — 검색창과 검색 버튼, 링크와 페이지 제목, 본문 글꼴·색상, 전체 컨테이너(container)와 헤더(header)의 배치를 정한다(13–65). 태그 표시 영역의 스타일도 포함한다(66–70). |
| 71–135 | 사이트 CSS / 본문·링크·경로 표시 — 본문 영역의 배치와 문단·링크 스타일을 정한다(71–114). 경로 표시(breadcrumbs), 활성 탐색 링크, 인용문과 소제목 스타일을 정한다(115–135). |
| 136–200 | 사이트 CSS / 열 배치·탐색 메뉴 — 본문 열과 탐색 영역의 배치를 정한다(136–150). 메뉴 목록과 하위 메뉴의 위치·색상·크기를 정한다(151–200). |
| 201–231 | 사이트 CSS / 메뉴 상태·이미지 크기 — 마우스를 올린 메뉴와 현재 페이지 메뉴의 표시 규칙이 들어 있다(201–225). 콘텐츠 표시 영역, 메뉴 글꼴, 태그 숨김과 이미지의 내재 크기(intrinsic size) 설정을 포함한다(226–231). |
| 232–241 | 페이지 메타데이터 — 페이지 제목이 들어 있다(232). JSON-LD에 이 페이지의 URL·제목·게시 시각과 상위 페이지 경로, 사이트 검색 정보를 담는다(237). 나머지는 빈 줄이다(233–236·238–241). |
| 242–270 | WordPress 스크립트·CSS — 이모지(emoji) 지원 설정과 브라우저 지원 검사 스크립트가 들어 있다(242–246). 이모지 표시, 블록(block) 버튼, 색상·글꼴·간격·배치의 공통 CSS를 포함한다(249–269). 빈 줄도 포함한다. |
| 271–303 | 사이트 설정 / 관리자 표시·방문 계측·배경 — 관리자 지원 표시 스타일이 들어 있다(286–288). 방문 계측 설정이 들어 있다(292–298). 사이트 배경 이미지의 반복 표시 CSS가 들어 있다(300). 주변 빈 줄도 포함한다. |
| 304–358 | 사이트 탐색 / Community·Documentation — 빈 제목 마크업과 ADCIRC 사이트 제목, 탐색 건너뛰기 링크가 들어 있다(304–310). 커뮤니티·개발 기관과 사용자 안내가 들어 있다(312–322). 매뉴얼 판본, 컴파일·실행 옵션, FAQ, 예제, 개발·이론 보고서와 출판물 링크를 나열한다(323–358). |
| 359–401 | 사이트 탐색 / Related software·News·Products·ASGS — 유틸리티와 격자 생성 도구를 연결한다(359–361). 사용자 모임·워크숍·사진·발표자료·폭풍해일 예보 링크를 나열한다(362–393). 조석 데이터베이스·출판물·격자·예보 제품과 ASGS 링크를 나열한다(394–400). 끝의 빈 줄도 포함한다(401). |
| 402–407 | Inundation rising at the end of the run flag file (endrisinginun.63) / 표지 기준 — 상위 경로와 본문 제목이 들어 있다(402–404). 마지막 시간 단계(time step)의 수면고(water surface elevation)를 직전 시간 단계의 수면고와 비교하여 실행 끝에 침수 깊이(inundation depth)가 상승하는 노드에 표지(flag)를 준다고 적는다(406). 상승하는 노드의 표지는 정수 1이고 나머지 모든 노드의 표지는 정수 0이다(406). 비교 기준·값 원문: `The endrisinginun.63 file flags nodes whose inundation depth is rising at the end of the simulation by comparing the water surface elevation on the final time step with the water surface elevation on the previous time step. Nodes with rising inundation levels are flagged with an integer value of 1 and all others are given an integer value of 0.` (406). |
| 408–417 | endrisinginun.63 / 생성 조건·형식·헤더 — fort.15 맨 아래 선택 네임리스트(namelist)의 매개변수를 참으로 설정하면 출력을 활성화한다고 적는다(408). 굵은 변수 이름의 각 줄이 출력 한 줄을 나타내며 빈 줄은 가독성을 위한 것이고 반복은 여러 출력 줄을 나타낸다고 설명한다(410). 변수 정의는 링크로 제공한다고 적는다(410). fort.15 설정에 따라 ASCII 또는 netCDF 형식으로 출력할 수 있다고 적는다(412). 실행·격자 식별자, 첫 값이 1인 헤더, 출력 간격의 곱셈식과 변수 순서를 제시한다(414–416). 생성·형식 조건 원문: `The writing of the endrisinginun.63 output file is activated when the inundationOutput parameter is set to .true. in the optional inundationOutputContol namelist at the bottom of the fort.15 file.` (408); `Output may be in ascii or netCDF format depending on how [NOUTGE](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#NOUTGE) is set in the [Model Parameter and Periodic Boundary Condition File](https://adcirc.org/home/documentation/users-manual-v53/input-file-descriptions/model-parameter-and-periodic-boundary-condition-file-fort-15/).` (412). 헤더·곱셈식 원문: `[**RUNDES**](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#RUNDES), [**RUNID**](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#RUNID), [**AGRID**](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#AGRID)` (414); `1, [**NP**](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#NP), [**DTDP**](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#DTDP)\*[**NSPOOLGE**](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#NSPOOLGE), [**NSPOOLGE**](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#NSPOOLGE), [**IRTYPE**](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#IRTYPE)` (416). |
| 418–425 | endrisinginun.63 / 시각·노드별 표지 — 시각과 시간 단계 변수 뒤 모든 노드에 대한 반복문을 제시한다(418–424). 노드 첨자와 침수 상승 표지의 출력 순서를 제시한다(422). 원문: `[**TIME**](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#TIME), [**IT**](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#IT)` (418); `for k=1,[NP](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#NP)` (420); `**k,** [**endrisinginun(k)**](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#endrisinginun)` (422); `end k loop` (424). 빈 줄도 포함한다. |
| 426–429 | Notes / 출력 시점·실행 범위·대상 영역 — 시간 단계 진행(timestepping)을 마친 뒤 시뮬레이션의 맨 끝에 파일을 쓴다고 적는다(428). 재시작(hot start) 실행에서도 값은 현재 실행만 반영한다고 적는다(428). initiallydry.63이 처음 건조한 것으로 나타낸 영역에서 상승하는 수면고만 표지한다고 적는다(428). 시점·적용 범위 원문: `The endrisinginun.63 file is written at the very end of the simulation, after timestepping is complete. The values only reflect the current run, even if the run was hotstarted. The data in the endrisinginun.63 file only flag rising water surface elevation in areas that are initially dry, according to the initiallydry.63 file.` (428). 제목 마크업과 빈 줄도 포함한다(426–427·429). |
| 430–444 | 페이지 말미 웹 설정 — 빈 줄과 유틸리티 표시 호출이 들어 있다(430–432). 링크 사전 가져오기(prefetch) 규칙이 들어 있다(434). 쿠키 안내문 설정이 들어 있다(437–439). jQuery 표시 클래스 변경과 New Relic 계측 메타데이터가 들어 있다(443–444). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

없음
