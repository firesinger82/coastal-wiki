---
file: models/ADCIRC/raw/manuals/website_markdown/home/documentation/users-manual-v51/input-file-descriptions/index.md
lines: 459
sha256: 1f2f8f7107edb6146e89f4784b4c7acb2b8e1fda8885a7e02b85da6447429bef
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# index.md — 판독 구간 기록

구간은 1행부터 459행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–12 | 페이지 선두 스크립트 — New Relic의 초기 설정과 브라우저 계측 로더(JavaScript)를 포함한다(1–2). 뒤의 빈 행을 포함한다(3–12). |
| 13–77 | 사이트 스타일(CSS) / 검색·헤더·본문 — 검색 입력란, 제목, 글꼴, 배경, 컨테이너와 본문 폭을 지정한다(13–77). |
| 78–142 | 사이트 스타일 / 본문·탐색 경로 — 한 열 본문, 문단, 링크, 탐색 경로(breadcrumb), 인용문과 본문 배치를 지정한다(78–142). |
| 143–200 | 사이트 스타일 / 메뉴 — 주 메뉴와 하위 메뉴의 배치, 폭, 배경과 링크 표시를 지정한다(143–200). |
| 201–229 | 사이트 스타일 / 메뉴 상태 — 마우스 포인터와 현재 메뉴 항목의 표시를 지정한다(201–225). 콘텐츠 높이, 메뉴 글자와 숨김 태그 스타일을 포함한다(226–229). |
| 230–242 | 페이지 제목·구조화 메타데이터 — 이미지 크기 CSS와 페이지 제목을 포함한다(230–232). JSON-LD에 페이지 URL, 발행·수정 시각, 사이트와 탐색 경로를 적는다(237). 빈 행도 포함한다. |
| 243–260 | 이모지(emoji) 스크립트·스타일 — WordPress의 이모지 경로, 지원 여부 검사와 대체 스크립트 로드를 포함한다(243–247). 이모지 표시 CSS를 포함한다(250–260). |
| 261–290 | WordPress 스타일 — 자동 생성 버튼 스타일, 색·그라데이션·글자·간격·그림자 프리셋과 레이아웃을 포함한다(263–270). 관리자 지원 표시의 배경과 빈 행을 포함한다(271–290). |
| 291–304 | 분석 스크립트·배경 — Beehive 데이터 계층과 Google Analytics 설정을 포함한다(293–299). 사이트 배경 이미지 CSS를 포함한다(301). 빈 행도 포함한다. |
| 305–323 | 사이트 헤더·Community — 빈 제목 마크업, ADCIRC 사이트명, 공식 사이트 표제와 본문 이동 링크를 포함한다(305–311). 개발자·파트너·사용자 링크를 열거한다(313–323). |
| 324–359 | Documentation 탐색 — 매뉴얼 V50·V51·v52·v53, 입출력 설명, 버전 기록, 컴파일·명령행 옵션, FAQ와 SWAN 결합 안내의 링크를 열거한다(324–349). 예제, 보고서, 이론, 얼음 피복과 부분 영역 모델링 링크를 포함한다(350–359). |
| 360–402 | Related software·News·Products 탐색 — 유틸리티와 격자 생성기(grid generator)의 링크를 포함한다(360–362). 사용자 모임·워크숍·사진·발표 자료·폭풍해일 예제 링크를 열거한다(363–394). 조석 데이터베이스·격자·예보·기름 이동·ASGS 링크와 빈 행을 포함한다(395–402). |
| 403–406 | Input File Descriptions / 제목 — V51 입력 파일 설명의 탐색 경로와 제목을 포함한다(403–405). 빈 행도 포함한다. |
| 407–410 | Input File Descriptions / 필수 파일 — 격자·경계 파일과 모델 매개변수·주기 경계조건 파일을 필수(required)로 표시한다(407–409). 원문: `[Grid and Boundary Information File (fort.14) – required](adcirc-grid-and-boundary-information-file-fort-14)` (407); `[Model Parameter and Periodic Boundary Condition File (fort.15) – required](model-parameter-and-periodic-boundary-condition-file-fort-15)` (409). |
| 411–429 | Input File Descriptions / 조건부 파일 — 수동 스칼라(passive scalar), 밀도 초기조건, 절점 속성(nodal attributes), 비주기 수위·수직 유량, 기상 강제력(meteorological forcing), 파랑 복사응력(wave radiation stress), 자기 인력·지구 하중 조석(self attraction/earth load tide)과 얼음 피복의 입력 링크를 조건부(conditional)로 열거한다(411–429). 원문: `[Passive Scalar Transport Input File (fort.10) – conditional](passive-scalar-transport-input-file-fort-10)` (411); `[Density Initial Condition Input File (fort.11) – conditional](density-initial-condition-input-file-fort-11)` (413); `[Nodal Attributes File (fort.13) – conditional](nodal-attributes-file-fort-13)` (415); `[Non-periodic Elevation Boundary Condition File (fort.19) – conditional](non-periodic-elevation-boundary-condition-file-fort-19)` (417); `[Non-periodic, Normal Flux Boundary Condition File (fort.20) – conditional](non-periodic-normal-flow-boundary-condition-file-fort-20)` (419); `[Meteorological Forcing Data (fort.22) – conditional](https://adcirc.org/home/documentation/users-manual-v51/input-file-descriptions/single-file-meteorological-forcing-input-fort-22/)` (421); `[Multiple File Meterological Forcing Input (fort.200,?..) – conditional](multiple-file-meteorological-forcing-input-fort-200)` (423); `[Wave Radiation Stress Forcing File (fort.23) – conditional](wave-radiation-stress-forcing-file-fort-23)` (425); `[Self Attraction/Earth Load Tide Forcing File (fort.24) – conditional](self-attractionearth-load-tide-forcing-file-fort-24)` (427); `[Ice Coverage Input Files (fort.25, 225/227) – conditional](https://adcirc.org/home/documentation/users-manual-v51/input-file-descriptions/ice-coverage-input-files-fort-25-fort-225fort-227/)` (429). |
| 430–444 | Input File Descriptions / 조건부 경계·재시작·지형 — 무운동면(level of no motion), 염분·온도·표층 온도·하천 경계, 2DDI 재시작(hot start)과 시간 변화 수심(bathymetry) 파일의 링크를 조건부로 열거한다(431–443). 각 제목과 파일 번호, 빈 행을 포함한다. 원문: `[Level of No Motion Boundary Condition Input (fort.35) – conditional](https://adcirc.org/home/documentation/users-manual-v51/input-file-descriptions/level-of-no-motion-boundary-condition-input-fort-35/)` (431); `[Salinity Boundary Condition Input (fort.36) – conditional](salinity-boundary-condition-input-fort-36/)` (433); `[Temperature Boundary Condition Input (fort.37) – conditional](temperature-boundary-condition-input-fort-37/)` (435); `[Surface Temperature Boundary Values (fort.38) – conditional](surface-temperature-boundary-values-fort-38/)` (437); `[Salinity and Temperature River Boundary Values (fort.39) – conditional](salinity-and-temperature-river-boundary-values-fort-39/ "Salinity and Temperature River Boundary Values (fort.39)")` (439); `[2DDI Hot Start Files (fort.67 or fort.68) – conditional](hot-start-files-fort-67-or-fort-68)` (441); `[Time Varying Bathymetry Input File (fort.141) – conditional](time-varying-bathymetry-input-file-fort-141/)` (443). |
| 445–459 | 사이트 후미 스크립트 — 유틸리티 호출, 링크 사전 가져오기(prefetch), 쿠키 배너 설정, 슬라이더 클래스 변경과 New Relic 정보를 포함한다(447–459). 빈 행과 CDATA 마크업도 포함한다. |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 423: 링크 제목의 기상 강제력 표기는 `Meterological`이다. 같은 제목의 파일 목록 표기는 `(fort.200,?..)`로 끝난다.
