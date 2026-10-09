---
file: models/ADCIRC/raw/manuals/website_markdown/home/documentation/users-manual-v53/input-file-descriptions/meteorological-recording-station-location-input-file-met_stat-151/index.md
lines: 436
sha256: a349093ec391cc927c3b06a05ee54a4effec31fe2e3a86129e542fb643c42ce1
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# Meteorological Recording Station Location Input file (met\_stat.151) — 판독 구간 기록

구간은 1행부터 436행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–12 | 웹 계측 스크립트와 빈 줄 — New Relic 브라우저 계측 설정과 로더(loader) 코드가 들어 있다(1–2). 뒤 빈 줄도 이 구간에 포함한다(3–12). |
| 13–77 | 사이트 표시 스타일 / 머리말과 본문 — CSS(Cascading Style Sheets)가 검색 필드, 머리말, 글꼴, 배경, 컨테이너와 오른쪽 본문 영역의 표시를 정한다(13–77). |
| 78–142 | 사이트 표시 스타일 / 본문과 탐색 경로 — 단일 열 본문, 문단, 링크, 탐색 경로(breadcrumb), 인용문과 다중 열 본문의 CSS가 들어 있다(78–142). |
| 143–184 | 사이트 표시 스타일 / 주 메뉴 — 주 메뉴 영역, 목록, 메뉴 항목, 링크와 하위 메뉴 배치의 CSS가 들어 있다(143–184). |
| 185–225 | 사이트 표시 스타일 / 하위 메뉴와 현재 페이지 — 하위 메뉴 크기, 마우스를 올린 상태, 현재 페이지와 이전 브라우저용 선택자의 CSS가 들어 있다(185–225). |
| 226–269 | 페이지 제목·구조화 메타데이터와 WordPress 표시 코드 — 제목은 Meteorological Recording Station Location Input file (met\_stat.151)이다(232). JSON-LD에 v53 페이지 주소와 게시 시각을 둔다(237). 이모지(emoji) 지원 검사와 블록 표시 스타일을 포함한다(242–269). |
| 270–310 | 사이트 설정과 머리말 — 관리자 표시 CSS, 방문 분석 설정, 배경 이미지 CSS와 빈 줄이 들어 있다(270–303). ADCIRC 사이트 이름, 공식 웹사이트 표기와 본문으로 건너뛰는 링크가 이어진다(304–310). |
| 311–360 | 사이트 탐색 메뉴 / Community·Documentation·Related software — 개발자, 사용자, 사용자 매뉴얼 판본, 컴파일·명령줄 옵션, FAQ, 예제, 보고서, 출판물과 관련 소프트웨어 링크를 나열한다(312–360). |
| 361–403 | 사이트 탐색 메뉴 / News·Products·ASGS와 탐색 경로 — 격자 생성기, 모임 자료, 뉴스, 제품, ASGS 링크가 이어진다(361–400). 현재 v53 입력 파일 설명 페이지의 탐색 경로를 표시한다(402). |
| 404–408 | 기상 관측소(meteorological recording station) 위치 파일의 읽기 조건과 형식 안내 — fort.15의 관측소 수 NSTAM을 음수로 설정하면 met_stat.151을 읽는다(406). 굵은 변수명으로 한 입력 행을 표시한다(408). 빈 줄은 가독성을 위한 것이고 반복문(loop)은 여러 입력 행을 나타낸다(408). 변수 정의는 링크로 제공한다(408). 조건과 형식 안내 원문: `The reading of the met\_stat.151 file is triggered when the number of meteorological recording stations ([NSTAM](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#NSTAM)) in the [fort.15 file](https://adcirc.org/home/documentation/users-manual-v53/input-file-descriptions/model-parameter-and-periodic-boundary-condition-file-fort-15/) is set to a negative value.` (406); `The basic file structure is shown below. Each line of input data is represented by a line containing the input variable name(s) in bold face type. Blank lines are only to enhance readability. Loops indicate multiple lines of input. Definitions of each variable are provided via hot links.` (408). |
| 409–417 | 기본 입력 구조 — NSTAM2 다음에 각 관측소의 XEM(k), YEM(k) 쌍을 입력한다(410–416). 반복 범위와 입력 행을 원문 그대로 옮긴다. `[**NSTAM2**](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#NSTAM2)` (410); `for k=1,[NSTAM2](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#NSTAM2)` (412); `**[XEM(k)](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#XEM)**, **[YEM(k)](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#YEM)**` (414); `end k loop` (416). |
| 418–421 | Notes / 관측소 수의 불일치 처리 — NSTAM2와 fort.15에서 읽은 NSTAM이 다르면 NSTAM2를 사용한다(420). 같은 행은 conc_stat.151에 열거된 관측소가 NSTAM2보다 적으면 ADCIRC가 오류로 중단한다고 적는다(420). 더 많으면 처음 NSTACM개만 사용한다고 적는다(420). 파일명과 변수명을 원문 그대로 유지한다. `If the value of NSTAM2 differs from the value of NSTAM (as read from the fort.15 file) the value of NSTAM2 will be used. If there are fewer than NSTAM2 stations listed in the conc\_stat.151 file, ADCIRC will stop with an error. If there are more than NSTAM2 stations listed in the conc\_stat.151 file, only the first NSTACM of them will be used.` (420). |
| 422–436 | 사이트 후처리 코드와 빈 줄 — 빈 줄, 유틸리티(utility) 호출, 사전 가져오기(prefetch) 설정, 쿠키(cookie) 알림 문구, jQuery 처리와 New Relic 계측 정보가 이어진다(422–436). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 제목과 읽기 조건은 `met\_stat.151`을 대상으로 한다(404, 406). Notes의 관측소 부족·초과 설명은 `conc\_stat.151`을 대상으로 적혀 있다(420). 같은 파일 안에서 두 파일명이 다르게 쓰인다.
- 입력 구조와 Notes의 비교 조건은 `NSTAM2`를 사용한다(410, 412, 420). Notes의 초과 관측소 처리 문장은 `only the first NSTACM of them will be used.`라고 적는다(420). 이 문서 안에는 `NSTACM`의 정의가 없다.
