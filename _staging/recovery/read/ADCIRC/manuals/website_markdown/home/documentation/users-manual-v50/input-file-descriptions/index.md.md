---
file: models/ADCIRC/raw/manuals/website_markdown/home/documentation/users-manual-v50/input-file-descriptions/index.md
lines: 459
sha256: b141d0e1bc80793fdd5ddb123f61ff87dab51cce6390a0935453ac02756268e1
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# input-file-descriptions/index.md — 판독 구간 기록

구간은 1행부터 459행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–12 | 웹사이트 수집 내용 — New Relic 초기 설정과 압축된 브라우저 계측 스크립트가 들어 있다(1–2). 이어지는 빈 줄도 포함한다(3–12). |
| 13–85 | 웹사이트 CSS / 검색·본문 배치 — 검색 필드와 검색 버튼, 제목·본문·링크, 컨테이너·헤더·콘텐츠 영역의 스타일을 정의한다(13–85). 주석도 포함한다. |
| 86–161 | 웹사이트 CSS / 본문·탐색 메뉴 — 콘텐츠 영역·문단·링크·탐색 경로(breadcrumb)·인용문·메뉴의 스타일을 정의한다(86–161). |
| 162–230 | 웹사이트 CSS / 하위 메뉴·그림 배치 — 메뉴 항목의 배경 그림 참조, 하위 메뉴·마우스 반응·현재 페이지 스타일과 그림의 표시 크기 설정을 포함한다(162–230). |
| 231–272 | 페이지 제목·구조화 정보·WordPress 표시 코드 — 페이지 제목과 schema.org의 페이지·탐색 경로·웹사이트 정보를 포함한다(232·237). 이모지(emoji) 지원 검사 스크립트와 이모지·버튼·색상·간격 CSS가 들어 있다(243–270). 빈 줄과 주석도 포함한다. |
| 273–304 | 웹사이트 관리·통계·배경 설정 — 빈 줄, 관리 표시 CSS, Beehive 통계 초기 설정과 배경 그림 URL을 포함한다(273–301). |
| 305–359 | 사이트 공통 탐색 / Community·Documentation — ADCIRC 사이트 제목, Skip Navigation 링크와 개발자·사용자·매뉴얼 V50–v53·컴파일 옵션·예제·보고서·관련 문헌 링크를 나열한다(305–359). |
| 360–402 | 사이트 공통 탐색 / Related software·News·Products·ASGS — 유틸리티·격자 생성기·행사 자료·사진·예보·제품·ASGS 링크를 나열한다(360–401). 마지막 빈 줄도 포함한다(402). |
| 403–410 | Input File Descriptions / 필수 입력 파일 — 탐색 경로와 표제를 포함한다(403·405). 격자·경계 정보 파일과 모델 매개변수·주기 경계조건 파일에 `required` 표시를 붙인다(407·409). 파일명과 필요 조건의 표시를 원문으로 옮긴다. 원문: `[Grid and Boundary Information File (fort.14) – required](adcirc-grid-and-boundary-information-file-fort-14)` (407); `[Model Parameter and Periodic Boundary Condition File (fort.15) – required](model-parameter-and-periodic-boundary-condition-file-fort-15)` (409). |
| 411–428 | 조건부 입력 파일 / 수송·밀도·절점·경계·강제력 — 수송·밀도·절점 속성·비주기 수위·법선 유량·단일/다중 기상 강제력(meteorological forcing)·파랑 복사응력(wave radiation stress)·자기 인력과 지구 하중 조석(self attraction/earth load tide) 파일에 `conditional` 표시를 붙인다(411–427). 각 조건의 세부 옵션은 이 목록에 없다. 파일명과 조건 표시를 원문으로 옮긴다. 원문: `[Passive Scalar Transport Input File (fort.10) – conditional](passive-scalar-transport-input-file-fort-10)` (411); `[Density Initial Condition Input File (fort.11) – conditional](density-initial-condition-input-file-fort-11)` (413); `[Nodal Attributes File (fort.13) – conditional](nodal-attributes-file-fort-13)` (415); `[Non-periodic Elevation Boundary Condition File (fort.19) – conditional](non-periodic-elevation-boundary-condition-file-fort-19)` (417); `[Non-periodic, Normal Flux Boundary Condition File (fort.20) – conditional](non-periodic-normal-flow-boundary-condition-file-fort-20)` (419); `[Single File Meteorological Forcing Input (fort.22) – conditional](single-file-meteorological-forcing-input-fort-22)` (421); `[Multiple File Meterological Forcing Input (fort.200,?..) – conditional](multiple-file-meteorological-forcing-input-fort-200)` (423); `[Wave Radiation Stress Forcing File (fort.23) – conditional](wave-radiation-stress-forcing-file-fort-23)` (425); `[Self Attraction/Earth Load Tide Forcing File (fort.24) – conditional](self-attractionearth-load-tide-forcing-file-fort-24)` (427). |
| 429–444 | 조건부 입력 파일 / 3D 경계·재시작·초기화·지형 — 무운동 경계(level of no motion boundary)·염분·온도·표면 온도·하천 염분과 온도·2DDI hot start·해수면 위 하천 초기화·시간 변화 지형 파일을 나열한다(429–443). 각 항목의 `conditional` 표시와 파일명을 원문으로 옮긴다. 원문: `[Level of No Motion Boundary Condition Input (fort.35) – conditional](level-of-no-motion-boundary-condition-input-fort-35-2/)` (429); `[Salinity Boundary Condition Input (fort.36) – conditional](salinity-boundary-condition-input-fort-36/)` (431); `[Temperature Boundary Condition Input (fort.37) – conditional](temperature-boundary-condition-input-fort-37/)` (433); `[Surface Temperature Boundary Values (fort.38) – conditional](surface-temperature-boundary-values-fort-38/)` (435); `[Salinity and Temperature River Boundary Values (fort.39) – conditional](salinity-and-temperature-river-boundary-values-fort-39/ "Salinity and Temperature River Boundary Values (fort.39)")` (437); `[2DDI Hot Start Files (fort.67 or fort.68) – conditional](hot-start-files-fort-67-or-fort-68)` (439); `[Rivers Above Sea Level Initialization File (fort.88) – conditional](rivers-above-sea-level-initialization-file-fort-88/)` (441); `[Time Varying Bathymetry Input File (fort.141) – conditional](time-varying-bathymetry-input-file-fort-141/)` (443). |
| 445–459 | 웹사이트 후처리 — 빈 줄과 화면 유틸리티 호출, 링크 미리 가져오기(prefetch) 설정, 쿠키 안내, jQuery 호출, New Relic 페이지 계측 정보를 포함한다(445–459). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 423행: 다중 기상 강제력 파일의 번호 표기는 `fort.200,?..`이다. 물음표 뒤 파일 번호 목록은 이 행에 없다.
