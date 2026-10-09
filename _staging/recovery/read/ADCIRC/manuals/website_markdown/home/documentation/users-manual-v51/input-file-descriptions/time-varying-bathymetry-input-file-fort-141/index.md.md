---
file: models/ADCIRC/raw/manuals/website_markdown/home/documentation/users-manual-v51/input-file-descriptions/time-varying-bathymetry-input-file-fort-141/index.md
lines: 457
sha256: 76d0b82b290b6f541701aee318c312d582b1c8dbbaf20b5acbdf04f5dd2e418e
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# index.md — 판독 구간 기록

구간은 1행부터 457행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–12 | 웹페이지 계측 스크립트 — New Relic 초기 설정과 압축 JavaScript를 포함한다(1–2). 이후 빈 줄을 포함한다(3–12). |
| 13–77 | 웹페이지 스타일 / 검색·본문·머리말 — CSS가 검색 입력창과 검색 버튼, 본문, 링크, 머리말, 컨테이너, 오른쪽 본문 열을 설정한다(13–77). |
| 78–142 | 웹페이지 스타일 / 한 열 배치·탐색 경로 — CSS가 한 열 본문과 본문 내부 여백, 문단, 링크, 탐색 경로, 활성 탐색 항목, 인용문, 양쪽 열 배치를 설정한다(78–142). |
| 143–200 | 웹페이지 스타일 / 메뉴 — CSS가 기본 메뉴와 중첩 메뉴의 위치, 표시, 색상, 크기를 설정한다(143–200). 배경 장식 이미지의 URL 선언을 포함한다(166). |
| 201–231 | 웹페이지 스타일 / 메뉴 상태 — CSS가 마우스 진입과 현재 메뉴 항목의 표시를 설정한다(201–225). 슬라이드 영역과 머리말 표시, 자동 크기 이미지의 스타일을 포함한다(226–230). 마지막 빈 줄을 포함한다(231). |
| 232–242 | 페이지 제목·구조화 메타데이터 — 제목은 Time Varying Bathymetry Input File (fort.141)이다(232). JSON-LD가 페이지 URL, 발행 시각, V51 탐색 경로, 사이트 검색을 기술한다(237). 빈 줄을 포함한다(233–236·238–242). |
| 243–286 | WordPress 표시 코드 — 이모지 지원 검사와 로딩 스크립트, 이모지·블록 버튼·색상·글꼴·배치 스타일을 포함한다(243–270). 뒤의 빈 줄을 포함한다(271–286). |
| 287–304 | 웹페이지 관리자 표시·접속 통계·배경 — 관리자 지원 표시용 CSS를 포함한다(287–289). 접속 통계용 beehive 스크립트를 포함한다(293–299). 페이지 배경 이미지의 CSS 선언과 빈 줄을 포함한다(300–304). |
| 305–350 | 사이트 머리말·탐색 메뉴 / Community·Documentation — ADCIRC 사이트 머리말과 탐색 건너뛰기 링크를 포함한다(305–311). 개발자·사용자 메뉴와 V50·V51·v52·v53 매뉴얼, 컴파일·명령행 옵션, FAQ, SWAN 결합, 예제 링크를 나열한다(313–350). |
| 351–402 | 탐색 메뉴 / 문헌·관련 소프트웨어·뉴스·제품 — 보고서와 출판물, 유틸리티, 격자 생성기, 워크숍·행사 자료, 폭풍해일 예보, 조석 데이터베이스, 격자, ASGS 링크를 나열한다(351–401). 마지막 빈 줄을 포함한다(402). |
| 403–408 | Time Varying Bathymetry Input File (fort.141) / 적용 조건 — 시간 변화 수심(time varying bathymetry) 파일을 사용하는 조건과 두 형식을 소개한다(407). 원문이 설정 파일로 적은 fort.14와 비영(nonzero) 조건을 그대로 옮긴다. 원문: `The ADCIRC Time Varying Bathymetry Input File (fort.141) is used by ADCIRC whenever the [NDDT](../../parameter-definitions#NDDT) value in the fort.14 is nonzero. There are two variations of this file, depending on the value of [NDDT](../../parameter-definitions#NDDT).` (407). |
| 409–424 | Full Domain Bathymetry Change / 전체 영역 수심 변화 — 선택값의 절댓값에 따라 자료 집합(data set)이 전체 영역을 덮는 조건을 설명한다(411). 모든 수평 격자 절점(node)의 절점 번호와 수심 입력 줄을 제시한다(413–421). 절점 수·번호를 정의하고 수심의 의미는 fort.14 변수와 같다고 적는다(423). 적용 조건과 반복·입력·정의를 그대로 옮긴다. 원문: `**Full Domain Bathymetry Change**` (409); `If [NDDT](../../parameter-definitions#NDDT) is +/-1, then each bathymetry dataset in the file covers the full domain, and the file format is as follows:` (411); `for i=1 to numDataSets` (413); `for j=1 to **[NP](../../parameter-definitions#NP)**` (415); `**j, depth(j)**` (417); `end j loop` (419); `end i loop` (421); `where NP is the number of nodes in the horizontal mesh, j is the node number, and depth(j) has the same meaning as [DP](../../parameter-definitions#DP) in the mesh file (fort.14).` (423). |
| 425–442 | Limited Area Bathymetry Change / 부분 영역 수심 변화 — 자료 집합이 영역 일부만 덮는 조건을 설명한다(427). 자료 집합 구분 표식과 부분 영역의 절점 번호·수심 입력 반복을 제시한다(429–439). 자료 집합 구분을 위해 줄의 두 번째 열에 해시 표식(hash mark)을 두어야 한다(441). 이 형식은 자료 집합마다 기록 수를 달리할 수 있게 한다(441). 입력 줄과 표식 위치를 그대로 옮긴다. 원문: `**Limited Area Bathymetry Change**` (425); `If [NDDT](../../parameter-definitions#NDDT) is +/-2, then each dataset in the fort.141 file covers only part of the domain, and the file format is as follows:` (427); `for i=1 to numDataSets` (429); `” #”` (431); `for j=1 to areaNodes` (433); `**j, depth(j)**` (435); `end j loop` (437); `end i loop` (439); `The separation between datasets is achieved by placing a hash mark (“#”) in the second column of a line. This formatting allows each dataset to have a different number of records, thus enabling simulations where the number of nodes that change their bathymetry varies over time.` (441). |
| 443–457 | 웹페이지 뒤쪽 코드 — 빈 줄, 유틸리티 표시 호출, 링크 사전 가져오기 설정, 쿠키 안내 설정, 슬라이드 표시 코드, New Relic 정보를 포함한다(443–457). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 413·429·433: 반복 상한 `numDataSets`와 `areaNodes`의 값과 명시적 정의는 이 파일에 없다.
- 417·423·435: 수심 `depth(j)`의 의미는 fort.14의 DP를 참조한다(423). 수심의 단위와 양의 방향은 이 파일 본문에 명시하지 않는다.
