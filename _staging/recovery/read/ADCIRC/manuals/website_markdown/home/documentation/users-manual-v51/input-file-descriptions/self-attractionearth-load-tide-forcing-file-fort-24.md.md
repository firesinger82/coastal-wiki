---
file: models/ADCIRC/raw/manuals/website_markdown/home/documentation/users-manual-v51/input-file-descriptions/self-attractionearth-load-tide-forcing-file-fort-24.md
lines: 449
sha256: 6d2d6d376f7079faef1522cd26cf6cf47bf7b4060f0911e9cff85f147f54f049
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# self-attractionearth-load-tide-forcing-file-fort-24.md — 판독 구간 기록

구간은 1행부터 449행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–12 | 웹페이지 계측 스크립트 — New Relic 초기 설정과 압축 JavaScript를 포함한다(1–2). 이후 빈 줄을 포함한다(3–12). |
| 13–77 | 웹페이지 스타일 / 검색·본문·머리말 — CSS가 검색 입력창과 검색 버튼, 본문, 링크, 머리말, 컨테이너, 오른쪽 본문 열을 설정한다(13–77). |
| 78–142 | 웹페이지 스타일 / 한 열 배치·탐색 경로 — CSS가 한 열 본문과 본문 내부 여백, 문단, 링크, 탐색 경로, 활성 탐색 항목, 인용문, 양쪽 열 배치를 설정한다(78–142). |
| 143–200 | 웹페이지 스타일 / 메뉴 — CSS가 기본 메뉴와 중첩 메뉴의 위치, 표시, 색상, 크기를 설정한다(143–200). 배경 장식 이미지의 URL 선언을 포함한다(166). |
| 201–231 | 웹페이지 스타일 / 메뉴 상태 — CSS가 마우스 진입과 현재 메뉴 항목의 표시를 설정한다(201–225). 슬라이드 영역과 머리말 표시, 자동 크기 이미지의 스타일을 포함한다(226–230). 마지막 빈 줄을 포함한다(231). |
| 232–242 | 페이지 제목·구조화 메타데이터 — 제목은 Self Attraction/Earth Load Tide Forcing File (fort.24)이다(232). JSON-LD가 페이지 URL, 발행 시각, V51 탐색 경로, 사이트 검색을 기술한다(237). 빈 줄을 포함한다(233–236·238–242). |
| 243–286 | WordPress 표시 코드 — 이모지 지원 검사와 로딩 스크립트, 이모지·블록 버튼·색상·글꼴·배치 스타일을 포함한다(243–270). 뒤의 빈 줄을 포함한다(271–286). |
| 287–304 | 웹페이지 관리자 표시·접속 통계·배경 — 관리자 지원 표시용 CSS를 포함한다(287–289). 접속 통계용 beehive 스크립트를 포함한다(293–299). 페이지 배경 이미지의 CSS 선언과 빈 줄을 포함한다(300–304). |
| 305–350 | 사이트 머리말·탐색 메뉴 / Community·Documentation — ADCIRC 사이트 머리말과 탐색 건너뛰기 링크를 포함한다(305–311). 개발자·사용자 메뉴와 V50·V51·v52·v53 매뉴얼, 컴파일·명령행 옵션, FAQ, SWAN 결합, 예제 링크를 나열한다(313–350). |
| 351–402 | 탐색 메뉴 / 문헌·관련 소프트웨어·뉴스·제품 — 보고서와 출판물, 유틸리티, 격자 생성기, 워크숍·행사 자료, 폭풍해일 예보, 조석 데이터베이스, 격자, ASGS 링크를 나열한다(351–401). 마지막 빈 줄을 포함한다(402). |
| 403–411 | Self Attraction/Earth Load Tide Forcing File (fort.24) / 적용·형식 — 자기 인력/지구 하중 조석(self attraction/earth load tides)의 적용 조건을 설명한다(407). 속도 정보를 제외한 tea 조화 형식(harmonic format)을 사용한다(409). 분조(constituent) 순서, 위상(phase)·진폭(amplitude) 단위, 절점 인자(nodal factor)와 평형 인수(equilibrium argument)의 적용을 설명한다(409). 굵은 변수명, 빈 줄, 반복 구조, 변수 정의 링크의 의미를 설명한다(411). 원문: `Self attraction/earth load tides are used to force ADCIRC when [NTIP](../../parameter-definitions#NTIP)=2 in the [Model Parameter and Periodic Boundary Condition File](../model-parameter-and-periodic-boundary-condition-file-fort-15).` (407); `The format of this file is identical to the “tea” harmonic format with no velocity information included. Entries are grouped by constituents and must be in the same order as the tidal potential terms listed in the [Model Parameter and Periodic Boundary Condition File](http://adcirc.org/home/documentation/users-manual-v50/input-file-descriptions/model-parameter-and-periodic-boundary-condition-file-fort-15). Phases must be in degrees. Amplitudes must be in units compatible with the units of gravity. These values are modified by the nodal factor and equilibrium argument provided for the tidal potential terms.` (409); `The basic file structure is shown below. Each line of input data is represented by a line containing the input variable name(s) in bold face type. Blank lines are only to enhance readability. Loops indicate multiple lines of input. Definitions of each variable are provided via hot links.` (411). |
| 412–430 | 기본 입력 구조 — 분조별 반복 안에 네 머리말 입력 줄을 둔다(413–421). 각 절점(node)의 번호와 진폭·위상을 읽는 반복을 둔다(423–429). 빈 줄과 반복 종료 줄을 포함한다(412–430). 입력 형식 원문을 아래에 그대로 옮긴다. 원문: `for k=1,[NTIF](../../parameter-definitions#NTIF)` (413); `Alpha line` (415); `Constituent frequency` (417); `1` (419); `Constituent name (e.g., M2)` (421); `for j=1,[NP](../../parameter-definitions#NP)` (423); `**[JN](../../parameter-definitions#JN)**, **[SALTAMP(k,JN)](../../parameter-definitions#SALTAMP)**, **[SALTPHA(k,JN)](../../parameter-definitions#SALTPHA)**` (425); `end j loop` (427); `end k loop` (429). |
| 431–434 | Note / 필수 머리말 — 각 분조의 첫 네 입력 줄은 파일에 반드시 있어야 한다(433). ADCIRC는 판독 시 이 네 줄을 건너뛴다(433). 원문: `**Note:**` (431); `The first four lines (Alpha line, Constituent frequency, 1, Constituent name) for each constituent must be present in the file but they are skipped over during the ADCIRC read.` (433). |
| 435–449 | 웹페이지 뒤쪽 코드 — 빈 줄, 유틸리티 표시 호출, 링크 사전 가져오기 설정, 쿠키 안내 설정, 슬라이드 표시 코드, New Relic 정보를 포함한다(435–449). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 409: fort.15 참조 URL은 `users-manual-v50` 경로이다. 이 페이지의 탐색 경로는 V51이다(403).
