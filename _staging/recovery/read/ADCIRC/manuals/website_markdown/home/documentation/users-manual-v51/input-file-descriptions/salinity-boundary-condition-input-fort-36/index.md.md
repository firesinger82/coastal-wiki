---
file: models/ADCIRC/raw/manuals/website_markdown/home/documentation/users-manual-v51/input-file-descriptions/salinity-boundary-condition-input-fort-36/index.md
lines: 433
sha256: bfe9b8692fa9402914e8e7bb18b3275c4cbc10fc0eb8d15311382f35cac24912
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# salinity-boundary-condition-input-fort-36/index.md — 판독 구간 기록

구간은 1행부터 433행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–12 | 웹 계측 스크립트(JavaScript) — New Relic 초기화와 브라우저 계측 로더가 들어 있다(1–2). 뒤의 빈 줄도 포함한다(3–12). |
| 13–77 | 사이트 스타일(CSS) / 검색·머리말·본문 — 검색 필드와 버튼, 링크, 글꼴, 머리말, 컨테이너 및 오른쪽 본문 영역의 표시 규칙을 적는다(13–77). |
| 78–150 | 사이트 스타일(CSS) / 본문·탐색 영역 — 단일 열 본문, 문단, 링크, 탐색 경로(breadcrumb), 인용문 및 메뉴 영역의 표시 규칙을 적는다(78–150). |
| 151–230 | 사이트 스타일(CSS) / 메뉴 — 메뉴 항목과 하위 메뉴, 마우스 위치에 따른 표시 및 이미지 크기 규칙을 적는다(151–230). 배경 이미지 URL이 있다(166·202). |
| 231–245 | 페이지 제목·구조화 메타데이터 — 페이지 제목(232)과 페이지 주소·게시일·탐색 경로를 담은 JSON-LD(235)가 있다. WordPress 이모지(emoji) 설정과 지원 판정 스크립트를 포함한다(241–245). |
| 246–284 | WordPress 스타일 — 이모지 표시(248–258), 버튼(261–262), 색상·종횡비·글자 크기·간격·그림자 및 배치 설정(265–268)을 적는다. 뒤의 빈 줄도 포함한다(269–284). |
| 285–302 | 관리 표시·사이트 계측·배경 — 관리 표시 색상(285–287), Beehive/Google 계측 설정(291–297), 사이트 배경 이미지 URL(299)을 포함한다. 빈 줄도 포함한다. |
| 303–321 | 사이트 머리말·Community 메뉴 — 빈 제목 표식(303), 사이트 이름과 설명(305·307), 탐색 건너뛰기 링크(309), 개발자·협력 기관·사용자 링크(311–321)가 있다. |
| 322–357 | Documentation 메뉴 — V50·V51·v52·v53 사용자 매뉴얼과 입력·출력 설명, 버전 이력, 컴파일·명령행 옵션 및 FAQ 링크를 나열한다(322–347). 예제·보고서·이론·특수 기능·관련 출판물·하위 영역 모델링 링크도 포함한다(348–357). |
| 358–392 | Related software·News 메뉴 — 유틸리티(utility)와 격자 생성기(grid generator) 링크(358–360), 사용자 모임·워크숍의 발표·일정·단체 사진 및 허리케인(hurricane) 관련 페이지 링크를 나열한다(361–392). 단체 사진은 탐색용 일반 링크로 적혀 있다. |
| 393–402 | Products·ASGS 메뉴·현재 페이지 탐색 경로 — 조석 데이터베이스(tidal database), 출판물, 격자, 예측 및 표층 기름 이동 링크(393–398), ASGS 링크(399), 현재 문서의 탐색 경로(401)를 포함한다. |
| 403–406 | Salinity Boundary Condition Input (fort.36) — 염분(salinity) 경계 조건(boundary condition) 입력 파일의 제목(403)과 읽기 조건(405)을 적는다. RES_BC_FLAG가 -2, 2, -4 또는 4로 설정되었을 때 읽는다는 조건을 그대로 옮긴다. 원문: `The ADCIRC Salinity Boundary Condition Input File (fort.36) is read in when the [**RES\_BC\_FLAG**](../../parameter-definitions#RES_BC_FLAG) is set to -2, 2, -4, or 4 in the [fort.15 file](https://adcirc.org/home/documentation/users-manual-v50/input-file-descriptions/model-parameter-and-periodic-boundary-condition-file-fort-15/ "Model Parameter and Periodic Boundary Condition File (fort.15)").` (405). |
| 407–418 | 입력 파일 형식 — 자료 묶음(data set)의 반복문(loop)(407) 안에 날짜를 적는 주석 줄(409)이 있다. 바다 경계 절점(ocean boundary node)을 순회하는 반복문(411) 안에 절점 번호 k와 SALBC(k,m) 입력 줄(413)을 적는다. 두 반복문의 종료 줄도 포함한다(415·417). 원문: `for i=1 to numberOfDataSets` (407); `**comment line (date)**` (409); `for k=1 to number\_of\_ocean\_boundary\_nodes` (411); `k, (**SALBC(k,m)**, m=1,NFEN)` (413); `end k loop` (415); `end i loop` (417). |
| 419–433 | 페이지 후반부·사이트 스크립트 — 빈 줄(419–420), 유틸리티 표시 호출(421), 사전 가져오기(prefetch) 설정(423), 쿠키 안내 설정(426–428), 슬라이더(slider) 표시 조정(432), New Relic 계측 정보(433)를 포함한다. |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 401·405행: 현재 문서의 탐색 경로는 User’s Manual – V51이다. 405행의 fort.15 링크는 `users-manual-v50` 경로를 사용한다.
- 413행: 반복 상한 기호 `NFEN`이 있지만 이 파일에는 그 정의가 없다. 이 입력 줄의 `NFEN`에는 정의 링크도 없다.
