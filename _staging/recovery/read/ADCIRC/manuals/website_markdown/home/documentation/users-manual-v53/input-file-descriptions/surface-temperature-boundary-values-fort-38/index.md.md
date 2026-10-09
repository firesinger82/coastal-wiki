---
file: models/ADCIRC/raw/manuals/website_markdown/home/documentation/users-manual-v53/input-file-descriptions/surface-temperature-boundary-values-fort-38/index.md
lines: 443
sha256: 8b2034cc12fcebe81a46dd100c142bb73d2c2c00ad9dd8e03adcf8611bc18c9a
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# Surface Temperature Boundary Values (fort.38) — 판독 구간 기록

구간은 1행부터 443행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–39 | 검색·글꼴 스타일 — 검색 필드(search field), 사이트 머리말(header), 본문 및 링크의 스타일시트(Cascading Style Sheets, CSS)을 지정한다(1–39). |
| 40–81 | 페이지 틀 스타일 — 컨테이너(container), 머리말, 태그 표시 및 본문 열의 CSS 스타일을 지정한다(40–81). |
| 82–123 | 본문 요소 스타일 — 문단, 링크, 오른쪽 열, 탐색 경로(breadcrumb), 인용문 및 소제목의 CSS 스타일을 지정한다(82–123). |
| 124–172 | 메뉴 스타일 — 본문 배치와 탐색 메뉴(navigation menu)의 CSS 스타일을 지정한다. 메뉴 구분선의 배경 이미지 URL이 들어 있다(124–172). |
| 173–218 | 하위 메뉴·그림 크기 스타일 — 하위 메뉴(submenu)의 위치 및 상태별 표시를 지정한다. 래퍼(wrapper), 태그 및 본문 그림 크기의 CSS 스타일이 이어진다(173–218). |
| 219–229 | 페이지 제목·검색 메타데이터 — 문서 제목이 나온다(220). 웹페이지, 웹사이트 및 탐색 경로의 구조화 데이터(structured data)가 들어 있다(225). 주변 빈 줄도 이 구간에 포함한다(219–229). |
| 230–248 | 이모지 스크립트·스타일 — 브라우저의 이모지(emoji) 지원 확인, 검사 결과 저장 및 보조 스크립트 로딩 코드가 들어 있다(230–234). 이모지 그림의 CSS 스타일과 빈 줄이 이어진다(235–248). |
| 249–278 | 버튼·파일·관리자 표시 스타일 — 버튼과 파일 블록 및 전역 표시 설정이 들어 있다(250–257). 관리자 막대(admin bar)의 지원 스타일과 주변 빈 줄이 이어진다(258–278). |
| 279–290 | 웹 분석·배경 스타일 — Beehive와 Google Analytics 설정이 들어 있다(280–286). 페이지 배경 이미지의 CSS URL과 빈 줄이 이어진다(287–290). |
| 291–310 | 사이트 머리말·Community 메뉴 — ADCIRC 사이트 이름, 사이트 설명 및 탐색 건너뛰기 링크가 나온다(292–298). 개발자, 관련 연구 그룹 및 사용자 목록의 메뉴가 이어진다(300–310). |
| 311–346 | Documentation 메뉴 — 소개, 구조, 위키, 사용자 매뉴얼 및 입력·출력 파일 설명 링크가 있다(311–346). 컴파일·명령행 옵션, FAQ, 예제, 개발자 안내, 이론 보고서, 특수 기능 및 출판물 등의 링크도 같은 메뉴에 있다(311–346). |
| 347–381 | 관련 소프트웨어·News 메뉴 — 유틸리티와 격자 생성기(grid generator) 링크가 있다(347–349). 사용자 모임, 워크숍(workshop), 발표 자료, 일정, 단체 사진 및 예보·모의 사례 링크가 이어진다(350–381). 단체 사진은 탐색 메뉴의 일반 링크이다. |
| 382–391 | Products 메뉴·본문 진입 — 조석 자료, 출판물, 격자, 예보, 표층 기름 이동 및 ASGS 링크가 있다(382–388). 이 문서의 탐색 경로와 주변 빈 줄이 이어진다(389–391). |
| 392–395 | Surface Temperature Boundary Values (fort.38) — 표면 온도 경계조건(surface temperature boundary condition) 입력 파일의 판독 조건을 설명한다(392–394). 파일 형식은 fort.15의 표면 열 플럭스(surface heat flux) 매개변수에 따라 달라진다(394). 원문: `The surface temperature boundary condition input file (fort.38) is read in when the [**RES\_BC\_FLAG**](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#RES_BC_FLAG) is set to -3, 3, -4, or 4 in the [fort.15 file](https://adcirc.org/home/documentation/users-manual-v53/input-file-descriptions/model-parameter-and-periodic-boundary-condition-file-fort-15/ "Model Parameter and Periodic Boundary Condition File (fort.15)") (i.e., when a lateral temperature boundary condition is being used) and its format depends on the [**BCFLAG\_TEMP**](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#BCFLAG_TEMP) parameter in the fort.15, which controls the surface heat flux parameterization in ADCIRC.` (394). |
| 396–407 | 표면 열 플럭스 옵션 첫 형식 — 데이터 세트(data set)와 수평 격자(horizontal mesh) 노드(node)의 반복 안에서 노드 번호와 데이터 값을 읽는 구조를 제시한다(396–406). 적용 값과 각 입력 형식 줄은 아래 원문과 같다(396–406). 원문: `If [**BCFLAG\_TEMP**](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#BCFLAG_TEMP)=1 in the fort.15, the format of the fort.38 is as follows:` (396); `for i=1 to numberOfDataSets` (398); `for k=1 to [**NP**](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#NP)` (400); `k, **q\_heat(k)**` (402); `end k loop` (404); `end i loop` (406). |
| 408–417 | 표면 열 플럭스 옵션 두 번째 형식 — 열 플럭스 성분(component)별 값을 암시적 Fortran 입출력 반복문(implicit Fortran I/O loop)으로 읽는 형식을 제시한다(408–416). 괄호는 그 반복문 표기라는 설명을 포함한다(416). 성분 번호의 범위와 적용 값은 원문과 같다(408–416). 원문: `If [**BCFLAG\_TEMP**](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#BCFLAG_TEMP)=2 in the fort.15, the format of the fort.38 is as follows:` (408); `for i=1 to numberOfDataSets` (410); `(K, (**TMP(K,J)**, J=1,6),K=1,[**NP**](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#NP))` (412); `end i loop` (414); `where TMP(K,J) is the surface heat flux parameter Jth heat flux component for the Kth horizontal mesh node. The data are read using an implicit Fortran i/o loop, thus the parentheses around the statement.` (416). |
| 418–427 | 표면 열 플럭스 옵션 세 번째 형식 — 다른 성분 번호 범위를 쓰는 암시적 Fortran 입출력 반복문 형식을 제시한다(418–426). 열 플럭스 성분과 수평 격자 노드의 의미를 다시 설명한다(426). 적용 값과 성분 범위는 원문과 같다(418–426). 원문: `If [**BCFLAG\_TEMP**](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#BCFLAG_TEMP)=3 in the fort.15, the format of the fort.38 is as follows:` (418); `for i=1 to numberOfDataSets` (420); `(K, (**TMP(K,J)**, J=1,4),K=1,[**NP**](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#NP))` (422); `end i loop` (424); `where TMP(K,J) is the surface heat flux parameter Jth heat flux component for the Kth horizontal mesh node. The data are read using an implicit Fortran i/o loop, thus the parentheses around the statement.` (426). |
| 428–429 | 공통 노드 수·추가 설명 참조 — 노드 수를 이차원 전체 영역(2D fulldomain)의 노드 수로 설명한다(428). 삼차원 경압 물리(3D baroclinic physics)와 옵션별 상세 설명은 fort.15 문서로 안내한다(428). 원문: `In all the above cases, [**NP**](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#NP) is the number of nodes in the horizontal mesh (i.e., the 2D fulldomain number of nodes). See the [fort.15](../model-parameter-and-periodic-boundary-condition-file-fort-15/) documentation on 3D baroclinic physics (particularly the explanation of various [**BCFLAG\_TEMP**](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#BCFLAG_TEMP) values) for more details.` (428). |
| 430–443 | 웹페이지 끝부분 — 유틸리티 호출과 링크 미리 가져오기(prefetch) 설정이 들어 있다(432–434). 쿠키 안내문과 JavaScript 비활성 표시를 제거하는 jQuery 코드가 이어진다(437–443). 주변 빈 줄도 이 구간에 포함한다(430–443). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 398·410·420행: `numberOfDataSets`가 반복의 상한으로 쓰인다. 이 이름의 정의는 파일 본문에 없다.
- 402행: `q\_heat(k)`가 입력 변수로 제시된다. 이 변수의 뜻과 단위는 파일 본문에 없다.
- 412·416·422·426행: `TMP(K,J)`의 일반적인 뜻은 설명한다. 성분 번호별 물리량 이름과 단위는 제시하지 않는다.
