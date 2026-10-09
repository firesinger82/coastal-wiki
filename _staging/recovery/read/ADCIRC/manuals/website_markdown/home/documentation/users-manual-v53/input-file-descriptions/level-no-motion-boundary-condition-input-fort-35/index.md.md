---
file: models/ADCIRC/raw/manuals/website_markdown/home/documentation/users-manual-v53/input-file-descriptions/level-no-motion-boundary-condition-input-fort-35/index.md
lines: 432
sha256: 2296048cd42e84e38c827559589f4de846cc40f5e501c491b921591cdaa0b5a0
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# Level of No Motion Boundary Condition Input (fort.35) — 판독 구간 기록

구간은 1행부터 432행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–12 | 웹 계측 스크립트와 빈 줄 — New Relic 브라우저 계측 설정과 로더(loader) 코드가 들어 있다(1–2). 뒤 빈 줄도 이 구간에 포함한다(3–12). |
| 13–77 | 사이트 표시 스타일 / 머리말과 본문 — CSS(Cascading Style Sheets)가 검색 필드, 머리말, 글꼴, 배경, 컨테이너와 오른쪽 본문 영역의 표시를 정한다(13–77). |
| 78–142 | 사이트 표시 스타일 / 본문과 탐색 경로 — 단일 열 본문, 문단, 링크, 탐색 경로(breadcrumb), 인용문과 다중 열 본문의 CSS가 들어 있다(78–142). |
| 143–184 | 사이트 표시 스타일 / 주 메뉴 — 주 메뉴 영역, 목록, 메뉴 항목, 링크와 하위 메뉴 배치의 CSS가 들어 있다(143–184). |
| 185–225 | 사이트 표시 스타일 / 하위 메뉴와 현재 페이지 — 하위 메뉴 크기, 마우스를 올린 상태, 현재 페이지와 이전 브라우저용 선택자의 CSS가 들어 있다(185–225). |
| 226–267 | 페이지 제목·구조화 메타데이터와 WordPress 표시 코드 — 제목은 Level of No Motion Boundary Condition Input (fort.35)이다(232). JSON-LD에 v53 페이지 주소와 게시 시각을 둔다(235). 이모지(emoji) 지원 검사와 블록 표시 스타일을 포함한다(240–267). |
| 268–308 | 사이트 설정과 머리말 — 관리자 표시 CSS, 방문 분석 설정, 배경 이미지 CSS와 빈 줄이 들어 있다(268–301). ADCIRC 사이트 이름, 공식 웹사이트 표기와 본문으로 건너뛰는 링크가 이어진다(302–308). |
| 309–358 | 사이트 탐색 메뉴 / Community·Documentation·Related software — 개발자, 사용자, 사용자 매뉴얼 판본, 컴파일·명령줄 옵션, FAQ, 예제, 보고서, 출판물과 관련 소프트웨어 링크를 나열한다(310–358). |
| 359–401 | 사이트 탐색 메뉴 / News·Products·ASGS와 탐색 경로 — 격자 생성기, 모임 자료, 뉴스, 제품, ASGS 링크가 이어진다(359–398). 현재 v53 입력 파일 설명 페이지의 탐색 경로를 표시한다(400). |
| 402–405 | Level of No Motion Boundary Condition Input / 적용 조건 — 무운동 수심(level of no motion) 경계 입력 파일을 읽는 3차원 경압(baroclinic) 모의 조건과 fort.15의 플래그(flag) 값을 제시한다(404). 적용 조건 원문: `The ADCIRC Level of No Motion Boundary Condition Input File (fort.35) is read in for 3D baroclinic simulations when the [**BCFLAG\_LNM**](https://adcirc.org/home/documentation/users-manual-v52/parameter-definitions#BCFLAG_LNM) (boundary condition flag for the level of no motion) is set to 1 in the [fort.15 file](https://adcirc.org/home/documentation/users-manual-v50/input-file-descriptions/model-parameter-and-periodic-boundary-condition-file-fort-15/ "Model Parameter and Periodic Boundary Condition File (fort.15)"). Its format is as follows:` (404). |
| 406–417 | Level of No Motion Boundary Condition Input / 입력 형식 — 자료 집합별 반복에서 날짜 주석을 쓰고 해양 경계 절점(ocean boundary node)별로 k와 elevation_change를 읽는 형식을 제시한다(406–416). 두 반복의 종료 줄도 적는다(414–416). 입력 형식·변수명·반복 원문: `for i=1 to numberOfDataSets` (406); `**comment line (date)**` (408); `for k=1 to number\_of\_ocean\_boundary\_nodes` (410); `**k, elevation\_change**` (412); `end k loop` (414); `end i loop` (416). |
| 418–432 | 사이트 끝부분과 스크립트 — 빈 줄, utility 호출, 링크 사전 가져오기(prefetch) 규칙, 쿠키 안내문 설정, jQuery 클래스 제거와 New Relic 페이지 계측 정보가 들어 있다(418–432). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 404: BCFLAG_LNM 정의 링크는 `users-manual-v52` 주소를 사용한다. fort.15 링크는 `users-manual-v50` 주소를 사용한다. 현재 페이지의 탐색 경로는 v53이다(400). 링크 대상의 본문은 이번 판독에서 읽지 않았다.
- 406–412: 입력 형식은 `numberOfDataSets`, `number\_of\_ocean\_boundary\_nodes`, `elevation\_change`를 사용한다. 이 파일에는 이 이름의 정의가 없다. elevation_change의 단위와 기준면도 제시하지 않는다.
