---
file: models/ADCIRC/raw/manuals/website_markdown/home/documentation/users-manual-v51/input-file-descriptions/non-periodic-normal-flow-boundary-condition-file-fort-20.md
lines: 439
sha256: c87534a484bb893d38909ad1c859de056a8db92ecd1bb3dc0b3e6c208d66a586
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# non-periodic-normal-flow-boundary-condition-file-fort-20.md — 판독 구간 기록

구간은 1행부터 439행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–12 | 웹 계측 스크립트(JavaScript) — New Relic 초기화와 브라우저 계측 로더가 들어 있다(1–2). 뒤의 빈 줄도 포함한다(3–12). |
| 13–77 | 사이트 스타일(CSS) / 검색·머리말·본문 — 검색 필드와 버튼, 링크, 글꼴, 머리말, 컨테이너 및 오른쪽 본문 영역의 표시 규칙을 적는다(13–77). |
| 78–150 | 사이트 스타일(CSS) / 본문·탐색 영역 — 단일 열 본문, 문단, 링크, 탐색 경로(breadcrumb), 인용문 및 메뉴 영역의 표시 규칙을 적는다(78–150). |
| 151–230 | 사이트 스타일(CSS) / 메뉴 — 메뉴 항목과 하위 메뉴, 마우스 위치에 따른 표시 및 이미지 크기 규칙을 적는다(151–230). 배경 이미지 URL이 있다(166·202). |
| 231–247 | 페이지 제목·구조화 메타데이터 — 페이지 제목(232)과 페이지 주소·게시일·탐색 경로를 담은 JSON-LD(237)가 있다. WordPress 이모지(emoji) 설정과 지원 판정 스크립트를 포함한다(243–247). |
| 248–286 | WordPress 스타일 — 이모지 표시(250–260), 버튼(263–264), 색상·종횡비·글자 크기·간격·그림자 및 배치 설정(267–270)을 적는다. 뒤의 빈 줄도 포함한다(271–286). |
| 287–304 | 관리 표시·사이트 계측·배경 — 관리 표시 색상(287–289), Beehive/Google 계측 설정(293–299), 사이트 배경 이미지 URL(301)을 포함한다. 빈 줄도 포함한다. |
| 305–323 | 사이트 머리말·Community 메뉴 — 빈 제목 표식(305), 사이트 이름과 설명(307·309), 탐색 건너뛰기 링크(311), 개발자·협력 기관·사용자 링크(313–323)가 있다. |
| 324–359 | Documentation 메뉴 — V50·V51·v52·v53 사용자 매뉴얼과 입력·출력 설명, 버전 이력, 컴파일·명령행 옵션 및 FAQ 링크를 나열한다(324–349). 예제·보고서·이론·특수 기능·관련 출판물·하위 영역 모델링 링크도 포함한다(350–359). |
| 360–394 | Related software·News 메뉴 — 유틸리티(utility)와 격자 생성기(grid generator) 링크(360–362), 사용자 모임·워크숍의 발표·일정·단체 사진 및 허리케인(hurricane) 관련 페이지 링크를 나열한다(363–394). 단체 사진은 탐색용 일반 링크로 적혀 있다. |
| 395–404 | Products·ASGS 메뉴·현재 페이지 탐색 경로 — 조석 데이터베이스(tidal database), 출판물, 격자, 예측 및 표층 기름 이동 링크(395–400), ASGS 링크(401), 현재 문서의 탐색 경로(403)를 포함한다. |
| 405–410 | Non-periodic Normal Flow Boundary Condition File (fort.20) / 용도·읽기 조건 — 0이 아닌 법선 유량(normal flow)을 지정하는 경계 절점의 비주기적(non-periodic) 입력 파일이다(407). fort.14에 해당 경계 조건이 있고 IBTYPE이 2·12·22 중 하나이며 fort.15의 NFFR가 0일 때만 읽는다(407). 굵은 변수 이름의 각 줄이 입력 자료 한 줄이며 빈 줄은 가독성용이고 반복문은 여러 입력 줄을 뜻한다(409). 원문: `Non-periodic, normal flow boundary condition file for “specified non-zero normal flow” boundary nodes. This file is only read when a “specified non-zero normal flow” boundary condition has been specified in the [Grid and Boundary Information File](../adcirc-grid-and-boundary-information-file-fort-14) ([IBTYPE](../../parameter-definitions#IBTYPE) =2, 12 or 22) and [NFFR](../../parameter-definitions#NFFR) =0 in the [Model Parameter and Periodic Boundary Condition File](../model-parameter-and-periodic-boundary-condition-file-fort-15).` (407); `The basic file structure is shown below. Each line of input data is represented by a line containing the input variable name(s) in bold face type. Blank lines are only to enhance readability. Loops indicate multiple lines of input. Definitions of each variable are provided via hot links.` (409). |
| 411–418 | 기본 입력 구조 — FTIMINC를 적은 다음 k = 1부터 NFLBN까지 QNIN(k)를 한 줄씩 적는다(411–417). 입력 변수·반복 범위·반복 종료 줄을 원문 그대로 옮긴다. 원문: `[**FTIMINC**](../../parameter-definitions#FTIMINC)` (411); `for k=1,[NFLBN](../../parameter-definitions#NFLBN)` (413); `[**QNIN(k)**](../../parameter-definitions#QNIN)` (415); `end k loop` (417). |
| 419–424 | Notes / 자료 시각·전체 실행 기간 — 첫 법선 유량 값 집합은 TIME=STATIM에 제공하며 후속 집합은 FTIMINC마다 제공한다(421). 전체 모델 실행 기간을 덮도록 충분한 값 집합을 제공해야 하며 그렇지 않으면 실행이 중단된다고 명시한다(423). 원문: `The first set of normal flow values is provided at TIME=[STATIM](../../parameter-definitions#STATIM). Additional sets of normal flow values are provided every [FTIMINC](../../parameter-definitions#FTIMINC)` (421); `Enough sets of normal flow values must be provided to extend for the entire model run, otherwise the run will crash!` (423). |
| 425–439 | 사이트 후처리 스크립트·쿠키 안내 — 유틸리티 표시 호출(427), 사전 가져오기(prefetch) 규칙(429), 쿠키 동의 안내 설정(432–434), jQuery 클래스 변경(438) 및 New Relic 정보(439)가 있다. 빈 줄도 포함한다. |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

없음
