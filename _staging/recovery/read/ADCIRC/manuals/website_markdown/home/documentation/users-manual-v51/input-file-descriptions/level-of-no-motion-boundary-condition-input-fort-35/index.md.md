---
file: models/ADCIRC/raw/manuals/website_markdown/home/documentation/users-manual-v51/input-file-descriptions/level-of-no-motion-boundary-condition-input-fort-35/index.md
lines: 433
sha256: e8f4ede3c36b91e22f4c24ce772db6464f2bd5eb6406f5002867ab519e285700
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# index.md — 판독 구간 기록

구간은 1행부터 433행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–12 | 페이지 선두 스크립트 — New Relic의 초기 설정과 브라우저 계측 로더(JavaScript)를 포함한다(1–2). 뒤의 빈 행을 포함한다(3–12). |
| 13–77 | 사이트 스타일(CSS) / 검색·헤더·본문 — 검색 입력란, 제목, 글꼴, 배경, 컨테이너와 본문 폭을 지정한다(13–77). |
| 78–142 | 사이트 스타일 / 본문·탐색 경로 — 한 열 본문, 문단, 링크, 탐색 경로(breadcrumb), 인용문과 본문 배치를 지정한다(78–142). |
| 143–200 | 사이트 스타일 / 메뉴 — 주 메뉴와 하위 메뉴의 배치, 폭, 배경과 링크 표시를 지정한다(143–200). |
| 201–229 | 사이트 스타일 / 메뉴 상태 — 마우스 포인터와 현재 메뉴 항목의 표시를 지정한다(201–225). 콘텐츠 높이, 메뉴 글자와 숨김 태그 스타일을 포함한다(226–229). |
| 230–240 | 페이지 제목·구조화 메타데이터 — 이미지 크기 CSS와 페이지 제목을 포함한다(230–232). JSON-LD에 페이지 URL, 발행·수정 시각, 사이트와 탐색 경로를 적는다(235). 빈 행도 포함한다. |
| 241–258 | 이모지(emoji) 스크립트·스타일 — WordPress의 이모지 경로, 지원 여부 검사와 대체 스크립트 로드를 포함한다(241–245). 이모지 표시 CSS를 포함한다(248–258). |
| 259–288 | WordPress 스타일 — 자동 생성 버튼 스타일, 색·그라데이션·글자·간격·그림자 프리셋과 레이아웃을 포함한다(261–268). 관리자 지원 표시의 배경과 빈 행을 포함한다(269–288). |
| 289–302 | 분석 스크립트·배경 — Beehive 데이터 계층과 Google Analytics 설정을 포함한다(291–297). 사이트 배경 이미지 CSS를 포함한다(299). 빈 행도 포함한다. |
| 303–321 | 사이트 헤더·Community — 빈 제목 마크업, ADCIRC 사이트명, 공식 사이트 표제와 본문 이동 링크를 포함한다(303–309). 개발자·파트너·사용자 링크를 열거한다(311–321). |
| 322–357 | Documentation 탐색 — 매뉴얼 V50·V51·v52·v53, 입출력 설명, 버전 기록, 컴파일·명령행 옵션, FAQ와 SWAN 결합 안내의 링크를 열거한다(322–347). 예제, 보고서, 이론, 얼음 피복과 부분 영역 모델링 링크를 포함한다(348–357). |
| 358–400 | Related software·News·Products 탐색 — 유틸리티와 격자 생성기(grid generator)의 링크를 포함한다(358–360). 사용자 모임·워크숍·사진·발표 자료·폭풍해일 예제 링크를 열거한다(361–392). 조석 데이터베이스·격자·예보·기름 이동·ASGS 링크와 빈 행을 포함한다(393–400). |
| 401–406 | Level of No Motion Boundary Condition Input / 적용 조건 — 탐색 경로와 제목을 포함한다(401–403). 3차원 경압(baroclinic) 모의에서 무운동면(level of no motion) 경계조건 플래그에 따른 fort.35 읽기 조건을 적는다(405). 원문: `The ADCIRC Level of No Motion Boundary Condition Input File (fort.35) is read in for 3D baroclinic simulations when the [**BCFLAG\_LNM**](https://adcirc.org/home/documentation/users-manual-v51/parameter-definitions#BCFLAG_LNM) (boundary condition flag for the level of no motion) is set to 1 in the [fort.15 file](https://adcirc.org/home/documentation/users-manual-v50/input-file-descriptions/model-parameter-and-periodic-boundary-condition-file-fort-15/ "Model Parameter and Periodic Boundary Condition File (fort.15)"). Its format is as follows:` (405). |
| 407–418 | Level of No Motion Boundary Condition Input / 파일 배치 — 자료 세트(data set)별 반복, 날짜 주석, 해양 경계 노드(ocean boundary node)별 반복과 고도 변화(elevation change) 입력 배치를 제시한다(407–417). 종료문과 빈 행도 포함한다. 원문: `for i=1 to numberOfDataSets` (407); `**comment line (date)**` (409); `for k=1 to number\_of\_ocean\_boundary\_nodes` (411); `**k, elevation\_change**` (413); `end k loop` (415); `end i loop` (417). |
| 419–433 | 사이트 후미 스크립트 — 유틸리티 호출, 링크 사전 가져오기(prefetch), 쿠키 배너 설정, 슬라이더 클래스 변경과 New Relic 정보를 포함한다(421–433). 빈 행과 CDATA 마크업도 포함한다. |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 405: V51 페이지의 fort.15 링크 URL에는 `users-manual-v50`이 들어 있다. 같은 행의 경계조건 플래그 링크 URL에는 `users-manual-v51`이 들어 있다.
- 407·411·413: 입력 형식의 `numberOfDataSets`, `number\_of\_ocean\_boundary\_nodes`, `elevation\_change`에 대한 별도 정의는 이 파일에 없다. `elevation\_change`의 단위와 자료 세트 사이의 시간 간격도 적혀 있지 않다.
