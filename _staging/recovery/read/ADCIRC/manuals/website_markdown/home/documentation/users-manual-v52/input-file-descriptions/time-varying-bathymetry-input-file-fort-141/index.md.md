---
file: models/ADCIRC/raw/manuals/website_markdown/home/documentation/users-manual-v52/input-file-descriptions/time-varying-bathymetry-input-file-fort-141/index.md
lines: 456
sha256: 26f2bab11098465f2df4f7245a2e7f76d400a8ca5fab38e97a437b9c417989af
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# Time Varying Bathymetry Input File (fort.141) — 판독 구간 기록

구간은 1행부터 456행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–12 | 웹사이트 계측 스크립트(New Relic) — 계측 초기 설정(1)과 축약된 자바스크립트(JavaScript) 로더(2)를 포함한다. 3–12행은 빈 줄이다. |
| 13–77 | 웹사이트 스타일시트(CSS) / 머리말·배치 — 검색창과 버튼의 표시 규칙(13–25)을 포함한다. 머리말·본문의 글꼴과 색상, 페이지 컨테이너와 콘텐츠 영역의 배치를 지정한다(26–77). |
| 78–142 | 웹사이트 스타일시트 / 본문·링크 — 단일 열 콘텐츠와 본문 영역의 표시 규칙(78–93)을 포함한다. 문단·링크·탐색 경로(breadcrumb)·인용문·다른 콘텐츠 배치의 표시 규칙을 지정한다(94–142). |
| 143–200 | 웹사이트 스타일시트 / 탐색 메뉴 — 메뉴 영역·목록·메뉴 항목의 배치를 지정한다(143–176). 하위 메뉴의 위치·폭·색상·표시 규칙을 지정한다(177–200). |
| 201–231 | 웹사이트 스타일시트 / 메뉴 상태·이미지 크기 — 포인터를 올린 메뉴와 현재 메뉴 항목의 표시 규칙을 지정한다(201–225). 콘텐츠 높이·메뉴 글꼴·태그 숨김 규칙과 자동 크기 이미지 선택자 규칙을 포함한다(226–230). 229·231행은 빈 줄이다. |
| 232–241 | 페이지 제목·메타데이터 — 페이지 제목(232)과 페이지 URL·게시 시각·수정 시각·탐색 경로를 담은 JSON-LD(237)를 포함한다. 나머지 행은 빈 줄이다. |
| 242–270 | WordPress 이모지·블록 표시 — 이모지 설정(243)과 지원 검사·로딩 스크립트(245)를 포함한다. 이모지 표시 스타일(249–259)과 버튼·블록·색상·배치의 자동 생성 스타일(262–269)을 포함한다. 주석과 빈 줄도 이 구간에 포함한다. |
| 271–303 | 관리자 표시·방문 통계·배경 — 빈 줄과 관리자 표시 스타일(286–288)을 포함한다. 방문 통계 초기화(292–298)와 사이트 배경 이미지의 스타일(300)을 포함한다. |
| 304–322 | 사이트 제목·Community 메뉴 — 공식 사이트 제목과 탐색 건너뛰기 링크를 포함한다(304–310). 개발 그룹·개발 협력 기관·사용자 메뉴를 나열한다(312–322). |
| 323–358 | Documentation 메뉴 — 사용자 매뉴얼·컴파일 옵션·FAQ·위키·예제·보고서·논문 링크를 나열한다(323–358). 모델 입력 형식의 기술 본문은 이 구간에 없다. |
| 359–400 | Related software·News·Products·ASGS 메뉴 — 관련 소프트웨어 링크를 나열한다(359–361). 행사·발표 자료·단체 사진·예보·시뮬레이션·제품·ASGS 링크를 나열한다(362–400). 단체 사진은 일반 링크로 적혀 있다. |
| 401–405 | 본문 탐색 경로·제목 — 매뉴얼 내 페이지 위치(402)와 이 페이지의 제목(404)을 표시한다. 나머지 행은 빈 줄이다. |
| 406–407 | Time Varying Bathymetry Input File / 적용 조건 — 문서는 시간 변화 지형(bathymetry) 입력 파일의 사용 조건과 형식 구분을 제시한다(406). 원문: `The ADCIRC Time Varying Bathymetry Input File (fort.141) is used by ADCIRC whenever the [NDDT](https://adcirc.org/home/documentation/users-manual-v52/parameter-definitions#NDDT) value in the fort.14 is nonzero. There are two variations of this file, depending on the value of [NDDT](https://adcirc.org/home/documentation/users-manual-v52/parameter-definitions#NDDT).` (406). |
| 408–423 | Full Domain Bathymetry Change — 전 영역 지형 자료집합의 입력 형식을 제시한다(408–420). 본문은 수평 격자(horizontal mesh)의 절점 수와 절점 번호를 설명한다(422). 수심 값의 뜻은 격자 파일의 변수 정의로 연결한다(422). 원문: `**Full Domain Bathymetry Change**` (408); `If [NDDT](https://adcirc.org/home/documentation/users-manual-v52/parameter-definitions#NDDT) is +/-1, then each bathymetry dataset in the file covers the full domain, and the file format is as follows:` (410); `for i=1 to numDataSets` (412); `for j=1 to **[NP](https://adcirc.org/home/documentation/users-manual-v52/parameter-definitions#NP)**` (414); `**j, depth(j)**` (416); `end j loop` (418); `end i loop` (420); `where NP is the number of nodes in the horizontal mesh, j is the node number, and depth(j) has the same meaning as [DP](https://adcirc.org/home/documentation/users-manual-v52/parameter-definitions#DP) in the mesh file (fort.14).` (422). |
| 424–443 | Limited Area Bathymetry Change — 일부 영역의 지형 자료집합을 기록하는 입력 형식을 제시한다(424–438). 자료집합별 레코드 수가 달라질 수 있는 구분자 형식을 설명한다(440). 442–443행은 빈 줄이다. 원문: `**Limited Area Bathymetry Change**` (424); `If [NDDT](https://adcirc.org/home/documentation/users-manual-v52/parameter-definitions#NDDT) is +/-2, then each dataset in the fort.141 file covers only part of the domain, and the file format is as follows:` (426); `for i=1 to numDataSets` (428); `” #”` (430); `for j=1 to areaNodes` (432); `**j, depth(j)**` (434); `end j loop` (436); `end i loop` (438); `The separation between datasets is achieved by placing a hash mark (“#”) in the second column of a line. This formatting allows each dataset to have a different number of records, thus enabling simulations where the number of nodes that change their bathymetry varies over time.` (440). |
| 444–456 | 페이지 끝 스크립트 — 사이트 유틸리티 호출(444), 링크 미리 읽기 설정(446), 쿠키 안내문 설정과 주석(449–451)을 포함한다. 표시 클래스 변경(455)과 계측 정보(456)를 포함한다. 나머지 행은 빈 줄이다. |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 412·428·432: 반복 상한에 쓰는 `numDataSets`와 `areaNodes`의 값이나 값을 지정하는 방법은 이 파일에 없다.
- 430: 구분자 예시는 `” #”`로 적혀 있으며 양끝 따옴표가 모두 오른쪽 쌍따옴표(U+201D)이다.
