---
file: models/ADCIRC/raw/manuals/website_markdown/home/documentation/users-manual-v51/input-file-descriptions/surface-temperature-boundary-values-fort-38/index.md
lines: 457
sha256: c16080224b15a17b3b546acbdf4ac126813c684f333d80114a2a37cf8e04f946
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
| 232–242 | 페이지 제목·구조화 메타데이터 — 제목은 Surface Temperature Boundary Values (fort.38)이다(232). JSON-LD가 페이지 URL, 발행 시각, V51 탐색 경로, 사이트 검색을 기술한다(237). 빈 줄을 포함한다(233–236·238–242). |
| 243–286 | WordPress 표시 코드 — 이모지 지원 검사와 로딩 스크립트, 이모지·블록 버튼·색상·글꼴·배치 스타일을 포함한다(243–270). 뒤의 빈 줄을 포함한다(271–286). |
| 287–304 | 웹페이지 관리자 표시·접속 통계·배경 — 관리자 지원 표시용 CSS를 포함한다(287–289). 접속 통계용 beehive 스크립트를 포함한다(293–299). 페이지 배경 이미지의 CSS 선언과 빈 줄을 포함한다(300–304). |
| 305–350 | 사이트 머리말·탐색 메뉴 / Community·Documentation — ADCIRC 사이트 머리말과 탐색 건너뛰기 링크를 포함한다(305–311). 개발자·사용자 메뉴와 V50·V51·v52·v53 매뉴얼, 컴파일·명령행 옵션, FAQ, SWAN 결합, 예제 링크를 나열한다(313–350). |
| 351–402 | 탐색 메뉴 / 문헌·관련 소프트웨어·뉴스·제품 — 보고서와 출판물, 유틸리티, 격자 생성기, 워크숍·행사 자료, 폭풍해일 예보, 조석 데이터베이스, 격자, ASGS 링크를 나열한다(351–401). 마지막 빈 줄을 포함한다(402). |
| 403–408 | Surface Temperature Boundary Values (fort.38) / 적용 조건 — 수면 온도 경계 조건(surface temperature boundary condition) 파일의 판독 조건을 설명한다(407). 입력 형식은 수면 열 플럭스 매개변수화(surface heat flux parameterization)를 제어하는 fort.15 설정에 따라 달라진다(407). 판독 조건의 부호와 선택값을 그대로 옮긴다. 원문: `The surface temperature boundary condition input file (fort.38) is read in when the [**RES\_BC\_FLAG**](../../parameter-definitions#RES_BC_FLAG) is set to -3, 3, -4, or 4 in the [fort.15 file](https://adcirc.org/home/documentation/users-manual-v50/input-file-descriptions/model-parameter-and-periodic-boundary-condition-file-fort-15/ "Model Parameter and Periodic Boundary Condition File (fort.15)") (i.e., when a lateral temperature boundary condition is being used) and its format depends on the [**BCFLAG\_TEMP**](../../parameter-definitions#BCFLAG_TEMP) parameter in the fort.15, which controls the surface heat flux parameterization in ADCIRC.` (407). |
| 409–420 | 입력 구조 / BCFLAG_TEMP 1 — 자료 집합(data set)마다 모든 수평 격자 절점(node)의 번호와 열 플럭스(heat flux) 입력값을 나열한다(409–419). 조건·반복·입력 줄을 그대로 옮긴다. 원문: `If [**BCFLAG\_TEMP**](../../parameter-definitions#BCFLAG_TEMP)=1 in the fort.15, the format of the fort.38 is as follows:` (409); `for i=1 to numberOfDataSets` (411); `for k=1 to [**NP**](../../parameter-definitions#NP)` (413); `k, **q\_heat(k)**` (415); `end k loop` (417); `end i loop` (419). |
| 421–430 | 입력 구조 / BCFLAG_TEMP 2 — 자료 집합별로 각 수평 격자 절점의 열 플럭스 성분을 읽는다(421–429). 성분 수와 Fortran 암시적 입출력 반복(implicit Fortran i/o loop), 괄호의 의미를 설명한다(425·429). 입력 줄과 변수 정의를 그대로 옮긴다. 원문: `If [**BCFLAG\_TEMP**](../../parameter-definitions#BCFLAG_TEMP)=2 in the fort.15, the format of the fort.38 is as follows:` (421); `for i=1 to numberOfDataSets` (423); `(K, (**TMP(K,J)**, J=1,6),K=1,[**NP**](../../parameter-definitions#NP))` (425); `end i loop` (427); `where TMP(K,J) is the surface heat flux parameter Jth heat flux component for the Kth horizontal mesh node. The data are read using an implicit Fortran i/o loop, thus the parentheses around the statement.` (429). |
| 431–440 | 입력 구조 / BCFLAG_TEMP 3 — 자료 집합별로 각 수평 격자 절점의 열 플럭스 성분을 읽는다(431–439). 성분 수와 Fortran 암시적 입출력 반복, 괄호의 의미를 설명한다(435·439). 입력 줄과 변수 정의를 그대로 옮긴다. 원문: `If [**BCFLAG\_TEMP**](../../parameter-definitions#BCFLAG_TEMP)=3 in the fort.15, the format of the fort.38 is as follows:` (431); `for i=1 to numberOfDataSets` (433); `(K, (**TMP(K,J)**, J=1,4),K=1,[**NP**](../../parameter-definitions#NP))` (435); `end i loop` (437); `where TMP(K,J) is the surface heat flux parameter Jth heat flux component for the Kth horizontal mesh node. The data are read using an implicit Fortran i/o loop, thus the parentheses around the statement.` (439). |
| 441–442 | 절점 수 정의·상세 문서 참조 — 절점 수는 2차원 전체 계산 영역(2D fulldomain)의 수평 격자 절점 수이다(441). 3차원 경압 물리(baroclinic physics)와 수면 열 플럭스 설정의 자세한 설명은 fort.15 문서를 참조하라고 적는다(441). 원문: `In all the above cases, [**NP**](../../parameter-definitions#NP) is the number of nodes in the horizontal mesh (i.e., the 2D fulldomain number of nodes). See the [fort.15](https://adcirc.org/home/documentation/users-manual-v50/input-file-descriptions/model-parameter-and-periodic-boundary-condition-file-fort-15/) documentation on 3D baroclinic physics (particularly the explanation of various [**BCFLAG\_TEMP**](../../parameter-definitions#BCFLAG_TEMP) values) for more details.` (441). |
| 443–457 | 웹페이지 뒤쪽 코드 — 빈 줄, 유틸리티 표시 호출, 링크 사전 가져오기 설정, 쿠키 안내 설정, 슬라이드 표시 코드, New Relic 정보를 포함한다(443–457). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 407·441: fort.15 링크는 모두 `users-manual-v50` 경로이다. 이 페이지의 탐색 경로는 V51이다(403).
- 411·423·433: 반복 상한 `numberOfDataSets`의 값과 정의는 이 파일에 없다.
- 415: 입력 변수 `q_heat(k)`의 정의와 단위는 이 파일에 없다.
- 425·429·435·439: TMP의 J번째 열 플럭스 성분을 설명한다(429·439). 각 성분의 이름과 단위는 이 파일에 없다.
