---
file: models/ADCIRC/raw/manuals/website_markdown/home/documentation/users-manual-v50/input-file-descriptions/level-of-no-motion-boundary-condition-input-fort-35-2/index.md
lines: 433
sha256: 87b4069b62680602e9c14681472ea484f0bdceae280cbb0de8abd8c159219aec
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# index.md — 판독 구간 기록

구간은 1행부터 433행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–12 | 웹 계측 스크립트(script) — New Relic 초기화와 압축된 로더 코드가 들어 있다(1–2). 뒤에는 빈 줄이 이어진다(3–12). |
| 13–77 | 웹 스타일시트(stylesheet) / 검색·머리글·본문 — 검색 입력창과 버튼, 글꼴·색상, 머리글, 컨테이너, 오른쪽 콘텐츠 영역의 CSS를 담는다(13–77). |
| 78–135 | 웹 스타일시트 / 단일 열·본문·경로 표시 — 단일 열 레이아웃, 본문 문단·링크, 경로 표시(breadcrumb), 활성 탐색 링크와 인용문의 CSS를 담는다(78–135). |
| 136–176 | 웹 스타일시트 / 콘텐츠·상위 메뉴 — 콘텐츠 영역, 메뉴 영역과 목록, 상위 메뉴 링크의 CSS를 담는다(136–176). |
| 177–228 | 웹 스타일시트 / 하위 메뉴·현재 페이지 — 하위 메뉴 배치, 마우스 진입 표시, 현재 페이지 표시, 슬라이드 영역과 태그 숨김 설정을 담는다(177–228). |
| 229–240 | 문서 제목·구조화 메타데이터(metadata) — 이미지 크기 CSS와 fort.35 페이지 제목을 포함한다(230–232). JSON-LD는 페이지 주소, 발행·수정 시각, V50 경로와 웹사이트 검색 정보를 담는다(235). 나머지는 빈 줄이다. |
| 241–268 | WordPress 표시 코드 — 이모지(emoji) 지원 검사와 로딩 스크립트, 이모지 크기 CSS, 버튼과 전역 색상·비율·간격·레이아웃 CSS를 담는다(241–268). |
| 269–302 | 웹 관리·계측·배경 설정 — 빈 줄, 관리 표시 색상 CSS, 방문 계측 초기화, 본문 배경 이미지 CSS를 포함한다(269–302). |
| 303–340 | 사이트 탐색(navigation) / Community·Documentation — 사이트 이름과 소개, 탐색 건너뛰기 링크를 제시한다(303–309). 개발자·협력기관·사용자와 V50부터 v53까지의 매뉴얼 링크를 나열한다(311–340). |
| 341–380 | 사이트 탐색 / 문서·소프트웨어·행사 — 매뉴얼 출력·판본 기록, 컴파일·명령행·FAQ·예제·발행물·관련 소프트웨어와 2020년부터 2014년까지의 행사 링크를 나열한다(341–380). |
| 381–402 | 사이트 탐색 / 이전 행사·제품·문서 경로 — 이전 행사·폭풍해일 예측·제품·격자·ASGS 링크를 나열한다(381–399). 현재 fort.35 문서의 경로 표시와 빈 줄을 포함한다(400–402). |
| 403–418 | Level of No Motion Boundary Condition Input (fort.35) — 무운동 수위(level of no motion) 경계조건 파일을 3차원 경압(baroclinic) 모의에서 읽는 조건과 데이터셋·해양 경계 절점(ocean boundary node)별 중첩 입력 형식을 제시한다(403–417). 적용 조건과 입력 형식 원문을 아래에 옮긴다. 원문: `The ADCIRC Level of No Motion Boundary Condition Input File (fort.35) is read in for 3D baroclinic simulations when the [**BCFLAG\_LNM**](https://adcirc.org/home/documentation/users-manual-v50/parameter-definitions/#BCFLAG_LMN) (boundary condition flag for the level of no motion) is set to 1 in the [fort.15 file](https://adcirc.org/home/documentation/users-manual-v50/input-file-descriptions/model-parameter-and-periodic-boundary-condition-file-fort-15/ "Model Parameter and Periodic Boundary Condition File (fort.15)"). Its format is as follows:` (405); `for i=1 to numberOfDataSets` (407); `**comment line (date)**` (409); `for k=1 to number\_of\_ocean\_boundary\_nodes` (411); `**k, elevation\_change**` (413); `end k loop` (415); `end i loop` (417). |
| 419–433 | 웹페이지 후처리 코드 — 빈 줄, 유틸리티 호출, 링크 사전 가져오기(prefetch) 설정, 쿠키 안내 설정, 슬라이드 표시 클래스 처리와 New Relic 계측 정보를 담는다(419–433). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 405: 표시된 매개변수 이름은 `BCFLAG\_LNM`이며 연결 주소의 앵커(anchor)는 `#BCFLAG_LMN`이다.
- 407·411·413: 본문은 `numberOfDataSets`, `number\_of\_ocean\_boundary\_nodes`, `elevation\_change`의 값·단위·시간 간격을 정의하지 않는다.
