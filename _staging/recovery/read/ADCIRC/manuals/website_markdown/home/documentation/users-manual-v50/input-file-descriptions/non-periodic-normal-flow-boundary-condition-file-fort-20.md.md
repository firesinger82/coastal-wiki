---
file: models/ADCIRC/raw/manuals/website_markdown/home/documentation/users-manual-v50/input-file-descriptions/non-periodic-normal-flow-boundary-condition-file-fort-20.md
lines: 439
sha256: e43cdcf2a16f1647cf3b49d34d89ff5c47e9816738799fe209c8cb65fdb55ac7
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# non-periodic-normal-flow-boundary-condition-file-fort-20.md — 판독 구간 기록

구간은 1행부터 439행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–12 | 웹 계측 스크립트(script) — New Relic 초기화와 압축된 로더 코드가 들어 있다(1–2). 뒤에는 빈 줄이 이어진다(3–12). |
| 13–77 | 웹 스타일시트(stylesheet) / 검색·머리글·본문 — 검색 입력창과 버튼, 글꼴·색상, 머리글, 컨테이너, 오른쪽 콘텐츠 영역의 CSS를 담는다(13–77). |
| 78–135 | 웹 스타일시트 / 단일 열·본문·경로 표시 — 단일 열 레이아웃, 본문 문단·링크, 경로 표시(breadcrumb), 활성 탐색 링크와 인용문의 CSS를 담는다(78–135). |
| 136–176 | 웹 스타일시트 / 콘텐츠·상위 메뉴 — 콘텐츠 영역, 메뉴 영역과 목록, 상위 메뉴 링크의 CSS를 담는다(136–176). |
| 177–228 | 웹 스타일시트 / 하위 메뉴·현재 페이지 — 하위 메뉴 배치, 마우스 진입 표시, 현재 페이지 표시, 슬라이드 영역과 태그 숨김 설정을 담는다(177–228). |
| 229–242 | 페이지 정보. 페이지 제목은 Non-periodic Normal Flow Boundary Condition File (fort.20)이다(232). JSON-LD 메타데이터에는 같은 문서 제목과 수정 시각 2013-07-25T18:57:42가 있다(237). |
| 243–270 | WordPress 표시 코드 — 이모지(emoji) 지원 검사와 로딩 스크립트, 이모지 크기 CSS, 버튼과 전역 색상·비율·간격·레이아웃 CSS를 담는다(243–270). |
| 271–304 | 웹 관리·계측·배경 설정 — 빈 줄, 관리 표시 색상 CSS, 방문 계측 초기화, 본문 배경 이미지 CSS를 포함한다(271–304). |
| 305–342 | 사이트 탐색(navigation) / Community·Documentation — 사이트 이름·소개와 탐색 건너뛰기 링크를 제시한다(305–311). 개발자·협력기관·사용자와 V50부터 v53까지의 매뉴얼 링크를 나열한다(313–342). |
| 343–382 | 사이트 탐색 / 문서·소프트웨어·행사 — 매뉴얼 출력·판본 기록, 컴파일·명령행·FAQ·예제·발행물·관련 소프트웨어와 2020년부터 2014년까지의 행사 링크를 나열한다(343–382). |
| 383–404 | 탐색 메뉴의 구버전 제품·ASGS 항목과 현재 문서의 경로 표시(breadcrumb)를 포함한다(383–403). 현재 문서는 Non-periodic Normal Flow Boundary Condition File (fort.20)이다(403). |
| 405–410 | 비주기 법선 유량(non-periodic normal flow) 경계조건(boundary condition) 파일의 제목과 적용 조건을 설명한다(405–409). 지정된 0이 아닌 법선 유량 경계절점(boundary node)을 위한 파일이다(407). 읽기 조건과 기본 입력 구조 안내는 원문대로 인용한다. 원문: `Non-periodic, normal flow boundary condition file for “specified non-zero normal flow” boundary nodes. This file is only read when a “specified non-zero normal flow” boundary condition has been specified in the [Grid and Boundary Information File](../adcirc-grid-and-boundary-information-file-fort-14) ([IBTYPE](../../parameter-definitions#IBTYPE) =2, 12 or 22) and [NFFR](../../parameter-definitions#NFFR) =0 in the [Model Parameter and Periodic Boundary Condition File](../model-parameter-and-periodic-boundary-condition-file-fort-15).` (407); `The basic file structure is shown below. Each line of input data is represented by a line containing the input variable name(s) in bold face type. Blank lines are only to enhance readability. Loops indicate multiple lines of input. Definitions of each variable are provided via hot links.` (409). |
| 411–418 | 입력 파일 구조. 시간 간격과 경계절점별 유량 입력의 반복문(loop)을 제시한다(411–417). 입력 형식 줄은 원문대로 인용한다. 원문: `[**FTIMINC**](../../parameter-definitions#FTIMINC)` (411); `for k=1,[NFLBN](../../parameter-definitions#NFLBN)` (413); `[**QNIN(k)**](../../parameter-definitions#QNIN)` (415); `end k loop` (417). |
| 419–424 | 주의사항. 첫 법선 유량 값 집합은 TIME=STATIM에 제공된다(421). 추가 집합은 FTIMINC마다 제공된다(421). 전체 모델 실행 기간을 포함할 만큼 충분한 집합을 제공해야 하며, 그렇지 않으면 실행이 중단된다고 명시한다(423). 적용 시각·간격·필수 제공 조건은 원문대로 인용한다. 원문: `The first set of normal flow values is provided at TIME=[STATIM](../../parameter-definitions#STATIM). Additional sets of normal flow values are provided every [FTIMINC](../../parameter-definitions#FTIMINC)` (421); `Enough sets of normal flow values must be provided to extend for the entire model run, otherwise the run will crash!` (423). |
| 425–439 | 문서 뒤의 빈 줄과 웹사이트 스크립트. 유틸리티 표시, 사전 가져오기(prefetch), 쿠키 배너(cookie banner), 슬라이더(slider), New Relic 설정 코드가 있다(425–439). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

없음
