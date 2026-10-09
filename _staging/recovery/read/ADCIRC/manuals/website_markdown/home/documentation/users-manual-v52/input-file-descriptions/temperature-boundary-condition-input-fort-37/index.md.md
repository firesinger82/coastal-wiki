---
file: models/ADCIRC/raw/manuals/website_markdown/home/documentation/users-manual-v52/input-file-descriptions/temperature-boundary-condition-input-fort-37/index.md
lines: 432
sha256: 0fb08ca69e0a014413118700a4847b04a5bff3c76f684c5fe800b1ac863afeb5
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# Temperature Boundary Condition Input (fort.37) — 판독 구간 기록

구간은 1행부터 432행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–12 | 웹사이트 계측 스크립트(New Relic) — 계측 초기 설정(1)과 축약된 자바스크립트(JavaScript) 로더(2)를 포함한다. 3–12행은 빈 줄이다. |
| 13–77 | 웹사이트 스타일시트(CSS) / 머리말·배치 — 검색창과 버튼의 표시 규칙(13–25)을 포함한다. 머리말·본문의 글꼴과 색상, 페이지 컨테이너와 콘텐츠 영역의 배치를 지정한다(26–77). |
| 78–142 | 웹사이트 스타일시트 / 본문·링크 — 단일 열 콘텐츠와 본문 영역의 표시 규칙(78–93)을 포함한다. 문단·링크·탐색 경로(breadcrumb)·인용문·다른 콘텐츠 배치의 표시 규칙을 지정한다(94–142). |
| 143–200 | 웹사이트 스타일시트 / 탐색 메뉴 — 메뉴 영역·목록·메뉴 항목의 배치를 지정한다(143–176). 하위 메뉴의 위치·폭·색상·표시 규칙을 지정한다(177–200). |
| 201–231 | 웹사이트 스타일시트 / 메뉴 상태·이미지 크기 — 포인터를 올린 메뉴와 현재 메뉴 항목의 표시 규칙을 지정한다(201–225). 콘텐츠 높이·메뉴 글꼴·태그 숨김 규칙과 자동 크기 이미지 선택자 규칙을 포함한다(226–230). 229·231행은 빈 줄이다. |
| 232–239 | 페이지 제목·메타데이터 — 페이지 제목(232)과 페이지 URL·게시 시각·수정 시각·탐색 경로를 담은 JSON-LD(235)를 포함한다. 나머지 행은 빈 줄이다. |
| 240–268 | WordPress 이모지·블록 표시 — 이모지 설정(241)과 지원 검사·로딩 스크립트(243)를 포함한다. 이모지 표시 스타일(247–257)과 버튼·블록·색상·배치의 자동 생성 스타일(260–267)을 포함한다. 주석과 빈 줄도 이 구간에 포함한다. |
| 269–301 | 관리자 표시·방문 통계·배경 — 빈 줄과 관리자 표시 스타일(284–286)을 포함한다. 방문 통계 초기화(290–296)와 사이트 배경 이미지의 스타일(298)을 포함한다. |
| 302–320 | 사이트 제목·Community 메뉴 — 공식 사이트 제목과 탐색 건너뛰기 링크를 포함한다(302–308). 개발 그룹·개발 협력 기관·사용자 메뉴를 나열한다(310–320). |
| 321–356 | Documentation 메뉴 — 사용자 매뉴얼·컴파일 옵션·FAQ·위키·예제·보고서·논문 링크를 나열한다(321–356). 모델 입력 형식의 기술 본문은 이 구간에 없다. |
| 357–398 | Related software·News·Products·ASGS 메뉴 — 관련 소프트웨어 링크를 나열한다(357–359). 행사·발표 자료·단체 사진·예보·시뮬레이션·제품·ASGS 링크를 나열한다(360–398). 단체 사진은 일반 링크로 적혀 있다. |
| 399–403 | 본문 탐색 경로·제목 — 매뉴얼 내 페이지 위치(400)와 이 페이지의 제목(402)을 표시한다. 나머지 행은 빈 줄이다. |
| 404–405 | Temperature Boundary Condition Input / 적용 조건 — 문서는 온도 경계조건(temperature boundary condition) 입력 파일을 읽는 조건을 제시한다(404). 원문: `The temperature boundary condition input file (fort.37) is read in when the [**RES\_BC\_FLAG**](../../parameter-definitions#RES_BC_FLAG) is set to -3, 3, -4, or 4 in the [fort.15 file](../model-parameter-and-periodic-boundary-condition-file-fort-15/ "Model Parameter and Periodic Boundary Condition File (fort.15)").` (404). |
| 406–419 | 입력 형식 — 자료집합(data set)별 날짜 주석과 해양 경계 절점(ocean boundary node)의 온도 배열을 기록하는 반복 형식을 제시한다(406–416). 418–419행은 빈 줄이다. 원문: `for i=1 to numberOfDataSets` (406); `**comment line (date)**` (408); `for k=1 to number\_of\_ocean\_boundary\_nodes` (410); `k, (**TEMPBC(k,m)**, m=1,NFEN)` (412); `end k loop` (414); `end i loop` (416). |
| 420–432 | 페이지 끝 스크립트 — 사이트 유틸리티 호출(420), 링크 미리 읽기 설정(422), 쿠키 안내문 설정과 주석(425–427)을 포함한다. 표시 클래스 변경(431)과 계측 정보(432)를 포함한다. 나머지 행은 빈 줄이다. |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 412: 입력 형식에 등장하는 `TEMPBC(k,m)`와 `NFEN`의 변수 정의는 이 파일에 없다.
