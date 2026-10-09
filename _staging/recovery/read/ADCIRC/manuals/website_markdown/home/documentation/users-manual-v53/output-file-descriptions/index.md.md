---
file: models/ADCIRC/raw/manuals/website_markdown/home/documentation/users-manual-v53/output-file-descriptions/index.md
lines: 500
sha256: 4a7b928bffb23ee165ea7ad3d728ca74442baafb24bb4e3c31146da0818070a9
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# index.md — 판독 구간 기록

구간은 1행부터 500행까지 빈틈없이 이어진다.

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
| 402–410 | Output File Descriptions / 제목·진단 출력 목록 — 상위 경로와 본문 제목이 들어 있다(402–404). 화면 출력 `fort.6`(406), 일반 진단 출력 `fort.16`(408), 반복 해법(iterative solver) ITPACKV의 2차원 진단 출력 `fort.33`(410) 링크를 나열한다. 빈 줄도 포함한다. |
| 411–425 | Output File Descriptions / 3차원 출력 목록 — 지정 관측점(recording stations)의 3차원 밀도(density)·온도(temperature) 및/또는 염분(salinity) `fort.41`(412), 유속(velocity) `fort.42`(414), 난류(turbulence) `fort.43`(416) 링크를 나열한다. 전체 격자 노드(model grid nodes)의 같은 항목은 각각 `fort.44`(418), `fort.45`(420), `fort.46`(422)이다. 표층(surface layer) 온도 `fort.47` 링크도 들어 있다(424). 빈 줄도 포함한다. |
| 426–443 | Output File Descriptions / 조화성분·시계열 목록 — 지정 관측점의 수위(elevation) 조화성분(harmonic constituents) `fort.51`(426)과 수심 평균 유속(depth-averaged velocity) 조화성분 `fort.52`(428), 전체 격자 노드의 같은 항목 `fort.53`(430)과 `fort.54`(432), 조화성분 진단 `fort.55`(434)를 연결한다. 지정 관측점의 수위·수심 평균 유속 시계열(time series) `fort.61`(436)과 `fort.62`(438), 전체 격자 노드의 같은 항목 `fort.63`(440)과 `fort.64`(442)를 연결한다. 빈 줄도 포함한다. |
| 444–459 | Output File Descriptions / 극값·침수·재시작 목록 — 실행 전체의 최대·최소값 파일(global maximum and minimum files) `maxele.63, maxvel.63, maxwvel.63, maxrs.63, minpr.63`(444), 침수(inundation) 자료 `initiallydry.63`(446), 건조 노드 표지(dry node flagging) `everdried.63`(448), 실행 끝의 침수 상승 표지 `endrisinginun.63`(450), 최대 침수 깊이 `maxinundepth.63`(452), 침수 시간 `inundationtime.63`(454), 노드 습윤·건조 상태(wet/dry state) `nodecode.63`(456), 재시작(hot start) `fort.67, fort.68`(458) 링크를 나열한다. 빈 줄도 포함한다. |
| 460–473 | Output File Descriptions / 기상·수심·보 목록 — 지정 기상 관측점(meteorological recording stations)의 대기압(atmospheric pressure) 시계열 `fort.71`(460)과 바람 속도(wind velocity) 시계열 `fort.72`(462), 전체 격자 노드의 대기압 시계열 `fort.73`(464)과 바람 응력(wind stress) 또는 속도 시계열 `fort.74`(466)를 연결한다. 지정 수심 관측점과 전체 격자 노드의 수심(bathymetry) 시계열 `fort.75`(468)와 `fort.76`(470), 시간 변화 보(weir) 출력 `fort.77`(472)을 연결한다. 빈 줄도 포함한다. |
| 474–485 | Output File Descriptions / 농도·연속식·얼음·요소 상태 목록 — 지정 농도 관측점(concentration recording stations)과 전체 격자 노드의 수심 평균 스칼라 농도(depth-averaged scalar concentration) 시계열 `fort.81`(474)과 `fort.83`(476), 전체 격자 노드의 연속방정식(continuity equation) 원시 가중(primitive weighting) 시계열 `fort.90`(478), 지정 관측점과 전체 격자 노드의 얼음 피복(ice coverage) `fort.91`(480)과 `fort.93`(482), 요소(element)의 습윤·건조 상태 `noff.100`(484)을 연결한다. 빈 줄도 포함한다. |
| 486–500 | 페이지 말미 웹 설정 — 빈 줄과 유틸리티 표시 호출이 들어 있다(486–488). 링크 사전 가져오기(prefetch) 규칙이 들어 있다(490). 쿠키 안내문 설정이 들어 있다(493–495). jQuery 표시 클래스 변경과 New Relic 계측 메타데이터가 들어 있다(499–500). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

없음
