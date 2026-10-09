---
file: models/ADCIRC/raw/manuals/website_markdown/home/documentation/users-manual-v53/output-file-descriptions/temperature-values-at-the-surface-layer-fort-47/index.md
lines: 420
sha256: ee3d6644b6d4ac72aec3f75bd77a603573f5b93990f7ab867d48565f87a6e338
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# index.md — 판독 구간 기록

구간은 1행부터 420행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–12 | 웹페이지 계측 스크립트 — New Relic 초기화 설정과 브라우저 이벤트 수집·스크립트 적재 코드가 있다(1–2). 이어지는 빈 줄을 포함한다(3–12). |
| 13–77 | 웹페이지 스타일(CSS) / 검색·제목·본문 — 검색 입력란과 버튼의 표시 규칙이 있다(13–25). 머리글·본문·컨테이너·태그·오른쪽 본문 영역의 글꼴·색·배치 규칙이 있다(26–77). |
| 78–142 | 웹페이지 CSS / 본문·링크·경로 표시 — 단일 열 본문과 본문 내부 영역의 배치 규칙이 있다(78–93). 문단·링크·경로 표시(breadcrumbs)·인용문·다른 본문 영역의 표시 규칙과 빈 줄을 포함한다(94–142). |
| 143–200 | 웹페이지 CSS / 탐색 메뉴 — 탐색 영역과 메뉴 목록의 배치·배경·링크 표시 규칙이 있다(143–176). 하위 메뉴의 숨김·위치·너비·높이 규칙이 있다(177–200). |
| 201–230 | 웹페이지 CSS / 메뉴 선택·이미지 배치 — 마우스가 놓인 메뉴와 현재 선택된 메뉴의 표시 규칙이 있다(201–225). 슬라이드 영역·메뉴 글꼴·태그 숨김·이미지의 고유 크기 규칙과 빈 줄을 포함한다(226–230). |
| 231–239 | 페이지 제목·구조화 메타데이터 — 페이지 제목은 Temperature Values at the Surface Layer (fort.47)이다(232). 구조화 데이터(JSON-LD)는 페이지 URL·발행일·수정일·설명·언어·상위 웹사이트·경로 표시·검색 동작을 담는다(235). 주변 빈 줄을 포함한다(231·233–234·236–239). |
| 240–258 | WordPress 이모지(emoji) 설정 — 이모지 자원 경로와 브라우저 지원 검사·스크립트 적재 코드가 있다(240–244). 이모지 이미지의 표시 규칙과 빈 줄을 포함한다(245–258). |
| 259–268 | WordPress 블록 스타일 — 자동 생성 주석과 버튼·파일 버튼 스타일이 있다(260–261). 화면 비율·색·그라데이션·글자 크기·간격·그림자 설정 및 배치 규칙이 있다(264–267). 빈 줄을 포함한다(259·262–263·268). |
| 269–301 | 웹페이지 지원·방문 계측·배경 — 관리자 지원 표시의 배경색 규칙이 있다(284–286). Beehive 방문 계측 초기화와 설정이 있다(290–296). 페이지 배경 이미지의 표시 규칙과 빈 줄을 포함한다(298–301). |
| 302–309 | 웹페이지 머리글 — 내용이 없는 제목 마크업과 빈 줄을 포함한다(302–303·305·307·309). ADCIRC 홈페이지 링크·공식 웹사이트 문구·탐색 건너뛰기 링크가 있다(304·306·308). |
| 310–356 | 웹사이트 탐색 / Community·Documentation — 개발자·협력 기관·사용자 링크가 있다(310–320). 사용자 매뉴얼의 판본별 입력·출력·판본 이력, 컴파일·실행 옵션, FAQ, 예제, 보고서·논문 링크가 있다(321–356). |
| 357–399 | 웹사이트 탐색 / Related software·News·Products·ASGS — 관련 소프트웨어 링크가 있다(357–359). 사용자 모임·워크숍·사진·발표·예보·시뮬레이션 링크가 있다(360–391). 조석 자료·논문·격자·예보 제품과 ASGS 링크 및 마지막 빈 줄을 포함한다(392–399). |
| 400–401 | 본문 경로 표시 — 홈페이지·Documentation·User’s Manual – v53·Output File Descriptions에서 Temperature Values at the Surface Layer (fort.47)로 이어지는 경로 표시와 다음 빈 줄을 포함한다(400–401). |
| 402–405 | Temperature Values at the Surface Layer / 경계 조건·형식·출력 조건 — 제목은 표면층(surface layer)의 온도값 출력 파일을 명시한다(402). 본문은 대기 모델(atmospheric model)의 출력 또는 Surface Temperature Boundary Values File을 통해 제공되는 상부 온도 경계 조건(top temperature boundary condition)을 기록한다고 설명한다(404). 본문은 표면층의 온도값만 기록한다고 설명한다(404). 본문은 출력 형식을 수위 출력 파일 형식과 연결한다(404). 제공 방식·형식 참조·층 범위·매개변수·출력 조건 원문: `The fort.47 file records the top temperature boundary condition that is either provided via output from an atmospheric model or as an input variable into the code via a Surface Temperature Boundary Values File. This output file follows the same format as a [fort.63 file](https://adcirc.org/home/documentation/users-manual-v53/output-file-descriptions/elevation-time-series-nodes-model-grid-fort-63/), as it only records the temperature values for the surface layer. The output file is only provided if the [IDEN](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#IDEN) value in the [Model Parameter and Periodic Boundary Condition File](https://adcirc.org/home/documentation/users-manual-v53/input-file-descriptions/model-parameter-and-periodic-boundary-condition-file-fort-15) is given as a 3 or 4, as ADCIRC evaluates the temperature changes for these two [IDEN](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#IDEN) values` (404). 온도 단위와 기본값은 이 구간 본문에 없다. 제목과 문단 뒤의 빈 줄을 포함한다(403·405). |
| 406–420 | 웹페이지 끝부분 — 빈 줄과 표시 보조 함수 호출을 포함한다(406–409). 링크 사전 적재(prefetch) 설정이 있다(410). 쿠키 안내 설정과 주석·빈 줄이 있다(411–418). 슬라이드 컨테이너의 클래스 변경과 New Relic 페이지 계측 정보로 끝난다(419–420). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

없음
