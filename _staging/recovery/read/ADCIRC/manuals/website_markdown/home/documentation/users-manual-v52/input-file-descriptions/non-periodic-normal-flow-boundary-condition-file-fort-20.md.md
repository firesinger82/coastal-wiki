---
file: models/ADCIRC/raw/manuals/website_markdown/home/documentation/users-manual-v52/input-file-descriptions/non-periodic-normal-flow-boundary-condition-file-fort-20.md
lines: 438
sha256: 48b8a522399ed3c0da7b49ef7b30a109f9ec0e958101e5dc3735a5d0cbfe689d
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# non-periodic-normal-flow-boundary-condition-file-fort-20.md — 판독 구간 기록

구간은 1행부터 438행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–12 | 웹 계측 스크립트·공백 — New Relic의 초기화와 브라우저 계측 JavaScript가 들어 있다(1–2). 뒤 공백을 포함한다(3–12). |
| 13–85 | 사이트 스타일 / 검색·제목·본문 틀 — 검색창과 검색 버튼, 제목과 링크, 본문 글꼴과 컨테이너의 CSS가 들어 있다(13–85). |
| 86–142 | 사이트 스타일 / 본문·경로·인용문 — 본문 영역, 링크, 경로 안내, 활성 메뉴, 인용문과 두 열 배치의 CSS가 들어 있다(86–142). |
| 143–184 | 사이트 스타일 / 메뉴 배치 — 메뉴의 위치와 목록, 링크, 하위 메뉴의 CSS가 들어 있다(143–184). |
| 185–230 | 사이트 스타일 / 메뉴 상태·이미지 — 하위 메뉴와 마우스 이동 상태, 활성 항목과 이미지 크기의 CSS가 들어 있다(185–230). |
| 231–241 | 페이지 제목·구조화 메타데이터 — 페이지 제목은 Non-periodic Normal Flow Boundary Condition File (fort.20)이다(232). JSON-LD는 페이지 URL, 발행·수정 시각, 경로 안내와 검색 동작을 적는다(237). 공백을 포함한다. |
| 242–270 | WordPress 표시 스크립트·스타일 — 이모지(emoji) 지원 검사와 표시 CSS가 들어 있다(242–259). 버튼과 파일 블록, 색상·글꼴·간격의 CSS 설정이 이어진다(262–269). |
| 271–303 | 지원 표시·방문 계측·배경 스타일 — 지원 표시의 CSS와 Google 방문 계측 설정이 들어 있다(286–298). 웹페이지 배경 CSS와 공백을 포함한다(300–303). |
| 304–358 | 사이트 탐색 / 커뮤니티·문서 — 사이트 제목과 탐색 건너뛰기 링크가 있다(304–310). 개발자·사용자, 매뉴얼 버전, 실행·이론·관련 문서의 탐색 링크가 이어진다(312–358). |
| 359–403 | 사이트 탐색 / 소프트웨어·소식·제품·경로 — 관련 소프트웨어, 모임과 발표, 제품, ASGS의 탐색 링크가 있다(359–400). 현재 페이지의 경로 안내와 공백을 포함한다(401–403). |
| 404–409 | Non-periodic Normal Flow Boundary Condition File (fort.20) — 0이 아닌 법선 유량(normal flow)을 지정한 경계 절점의 비주기 경계 조건을 입력한다(406). fort.14의 IBTYPE와 fort.15의 NFFR 적용 조건을 그대로 옮긴다(406). 굵은 변수 행, 가독성용 빈 행, 반복문과 정의 링크의 의미를 설명한다(408). 원문: `Non-periodic, normal flow boundary condition file for “specified non-zero normal flow” boundary nodes. This file is only read when a “specified non-zero normal flow” boundary condition has been specified in the [Grid and Boundary Information File](../adcirc-grid-and-boundary-information-file-fort-14) ([IBTYPE](https://adcirc.org/home/documentation/users-manual-v52/parameter-definitions#IBTYPE) =2, 12 or 22) and [NFFR](https://adcirc.org/home/documentation/users-manual-v52/parameter-definitions#NFFR) =0 in the [Model Parameter and Periodic Boundary Condition File](../model-parameter-and-periodic-boundary-condition-file-fort-15).` (406); `The basic file structure is shown below. Each line of input data is represented by a line containing the input variable name(s) in bold face type. Blank lines are only to enhance readability. Loops indicate multiple lines of input. Definitions of each variable are provided via hot links.` (408). |
| 410–417 | 기본 입력 형식 — FTIMINC를 먼저 입력한다(410). NFLBN 반복문에서 QNIN(k)를 입력한다(412–416). 입력 행과 반복문을 그대로 옮긴다. 원문: `[**FTIMINC**](https://adcirc.org/home/documentation/users-manual-v52/parameter-definitions#FTIMINC)` (410); `for k=1,[NFLBN](https://adcirc.org/home/documentation/users-manual-v52/parameter-definitions#NFLBN)` (412); `[**QNIN(k)**](https://adcirc.org/home/documentation/users-manual-v52/parameter-definitions#QNIN)` (414); `end k loop` (416). |
| 418–423 | Notes / 첫 시각·간격·전체 기간 — 첫 법선 유량 자료 세트의 시각과 추가 자료 간격을 그대로 옮긴다(420). 전체 모델 실행 기간을 채울 만큼 자료를 제공해야 한다(422). 그렇지 않으면 실행이 중단된다고 적는다(422). 원문: `**Notes:**` (418); `The first set of normal flow values is provided at TIME=[STATIM](https://adcirc.org/home/documentation/users-manual-v52/parameter-definitions#STATIM). Additional sets of normal flow values are provided every [FTIMINC](https://adcirc.org/home/documentation/users-manual-v52/parameter-definitions#FTIMINC)` (420); `Enough sets of normal flow values must be provided to extend for the entire model run, otherwise the run will crash!` (422). |
| 424–438 | 페이지 말미 스크립트·공백 — 유틸리티 표시와 페이지 사전 읽기(prefetch) 설정이 들어 있다(426–428). 쿠키 안내, 슬라이드 표시와 New Relic 페이지 계측 설정을 포함한다(431–438). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

없음
