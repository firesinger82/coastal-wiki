---
file: models/ADCIRC/raw/manuals/website_markdown/home/documentation/users-manual-v51/input-file-descriptions/temperature-boundary-condition-input-fort-37/index.md
lines: 433
sha256: 22ee7c7d60d74acf28b49019148f5783869a33774e991c5d27bd555fa66b7efc
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# index.md — 판독 구간 기록

구간은 1행부터 433행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–12 | 웹페이지 계측 스크립트 — New Relic 초기 설정과 압축 JavaScript를 포함한다(1–2). 이후 빈 줄을 포함한다(3–12). |
| 13–77 | 웹페이지 스타일 / 검색·본문·머리말 — CSS가 검색 입력창과 검색 버튼, 본문, 링크, 머리말, 컨테이너, 오른쪽 본문 열을 설정한다(13–77). |
| 78–142 | 웹페이지 스타일 / 한 열 배치·탐색 경로 — CSS가 한 열 본문과 본문 내부 여백, 문단, 링크, 탐색 경로, 활성 탐색 항목, 인용문, 양쪽 열 배치를 설정한다(78–142). |
| 143–200 | 웹페이지 스타일 / 메뉴 — CSS가 기본 메뉴와 중첩 메뉴의 위치, 표시, 색상, 크기를 설정한다(143–200). 배경 장식 이미지의 URL 선언을 포함한다(166). |
| 201–231 | 웹페이지 스타일 / 메뉴 상태 — CSS가 마우스 진입과 현재 메뉴 항목의 표시를 설정한다(201–225). 슬라이드 영역과 머리말 표시, 자동 크기 이미지의 스타일을 포함한다(226–230). 마지막 빈 줄을 포함한다(231). |
| 232–240 | 페이지 제목·구조화 메타데이터 — 제목은 Temperature Boundary Condition Input (fort.37)이다(232). JSON-LD가 페이지 URL, 발행 시각, V51 탐색 경로, 사이트 검색을 기술한다(235). 빈 줄을 포함한다(233–234·236–240). |
| 241–284 | WordPress 표시 코드 — 이모지 지원 검사와 로딩 스크립트, 이모지·블록 버튼·색상·글꼴·배치 스타일을 포함한다(241–268). 뒤의 빈 줄을 포함한다(269–284). |
| 285–302 | 웹페이지 관리자 표시·접속 통계·배경 — 관리자 지원 표시용 CSS를 포함한다(285–287). 접속 통계용 beehive 스크립트를 포함한다(291–297). 페이지 배경 이미지의 CSS 선언과 빈 줄을 포함한다(298–302). |
| 303–348 | 사이트 머리말·탐색 메뉴 / Community·Documentation — ADCIRC 사이트 머리말과 탐색 건너뛰기 링크를 포함한다(303–309). 개발자·사용자 메뉴와 V50·V51·v52·v53 매뉴얼, 컴파일·명령행 옵션, FAQ, SWAN 결합, 예제 링크를 나열한다(311–348). |
| 349–400 | 탐색 메뉴 / 문헌·관련 소프트웨어·뉴스·제품 — 보고서와 출판물, 유틸리티, 격자 생성기, 워크숍·행사 자료, 폭풍해일 예보, 조석 데이터베이스, 격자, ASGS 링크를 나열한다(349–399). 마지막 빈 줄을 포함한다(400). |
| 401–406 | Temperature Boundary Condition Input (fort.37) / 적용 조건 — 온도 경계 조건(temperature boundary condition) 파일을 읽는 fort.15 선택값을 설명한다(405). 판독 조건의 부호와 선택값을 그대로 옮긴다. 원문: `The temperature bounday condition input file (fort.37) is read in when the [**RES\_BC\_FLAG**](../../parameter-definitions#RES_BC_FLAG) is set to -3, 3, -4, or 4 in the [fort.15 file](https://adcirc.org/home/documentation/users-manual-v50/input-file-descriptions/model-parameter-and-periodic-boundary-condition-file-fort-15/ "Model Parameter and Periodic Boundary Condition File (fort.15)").` (405). |
| 407–418 | 기본 입력 구조 — 자료 집합(data set)마다 날짜 주석 줄을 둔다(407–409). 해양 경계 절점(ocean boundary node)에 대한 반복 안에 절점 번호와 온도 입력 배열을 둔다(411–417). 반복 상한과 배열 첨자 범위를 포함한 입력 줄을 그대로 옮긴다. 원문: `for i=1 to numberOfDataSets` (407); `**comment line (date)**` (409); `for k=1 to number\_of\_ocean\_boundary\_nodes` (411); `k, (**TEMPBC(k,m)**, m=1,NFEN)` (413); `end k loop` (415); `end i loop` (417). |
| 419–433 | 웹페이지 뒤쪽 코드 — 빈 줄, 유틸리티 표시 호출, 링크 사전 가져오기 설정, 쿠키 안내 설정, 슬라이드 표시 코드, New Relic 정보를 포함한다(419–433). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 405: fort.15 링크는 `users-manual-v50` 경로이다. 이 페이지의 탐색 경로는 V51이다(401).
- 407·411·413: 반복 상한 `numberOfDataSets`·`number\_of\_ocean\_boundary\_nodes`·`NFEN`의 값과 정의는 이 파일에 없다.
- 413: 입력 배열 `TEMPBC(k,m)`의 정의와 온도 단위는 이 파일에 없다.
