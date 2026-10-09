---
file: models/ADCIRC/raw/manuals/website_markdown/home/documentation/users-manual-v53/output-file-descriptions/depth-averaged-velocity-time-series-specified-velocity-recording-stations-fort-62/index.md
lines: 443
sha256: c0071de3e132094896dc7fc3a415b9b9dc5c4e9385f6c73d0dca36b2f37d01d4
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# Depth-averaged Velocity Time Series at Specified Velocity Recording Stations (fort.62) — 판독 구간 기록

구간은 1행부터 443행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–12 | 페이지 계측 스크립트 — New Relic의 초기화와 압축 JavaScript가 있다(1–2). 뒤에 빈 줄이 이어진다(3–12). |
| 13–70 | 페이지 기본 서식 — 이동 경로 검색 입력, 머리글, 본문, 링크, 페이지 컨테이너와 표제의 CSS 서식을 정한다(13–70). |
| 71–142 | 본문·열 배치 서식 — 본문 영역, 문단, 링크, 오른쪽 열, 이동 경로, 활성 메뉴, 인용문과 다중 열 배치의 CSS가 있다(71–142). |
| 143–228 | 탐색 메뉴 서식 — 상위 메뉴와 하위 메뉴의 배치, 배경 이미지 참조, 마우스가 놓였을 때의 표시, 현재 메뉴 항목, 표제 숨김의 CSS가 있다(143–228). |
| 229–241 | 페이지 제목·구조화 메타데이터 — 빈 줄과 이미지 크기 CSS를 포함한다(229–231). 문서 제목이 있다(232). JSON-LD가 문서 주소, 제목, 발행·수정 시각, 이동 경로와 사이트 검색 정보를 담는다(237). 뒤 빈 줄도 포함한다(238–241). |
| 242–261 | 이모지 표시 스크립트·서식 — WordPress의 이모지 설정, 표시 지원 검사와 관련 스크립트가 있다(242–246). 이모지와 스마일 이미지의 CSS 및 빈 줄이 이어진다(247–261). |
| 262–285 | WordPress 공통 서식 — 자동 생성 표시, 버튼·파일 링크 서식, 종횡비·색·그라데이션·글자 크기·간격·그림자 및 블록 배치의 CSS가 있다(262–269). 뒤 빈 줄을 포함한다(270–285). |
| 286–303 | 관리 표시·접속 통계·페이지 배경 — 관리 표시 CSS가 있다(286–288). 접속 통계 초기화와 설정이 있다(292–298). 페이지 배경 이미지 참조가 있다(300). 사이의 공백 행과 뒤 빈 줄을 포함한다(289–291·299·301–303). |
| 304–322 | 사이트 표제·Community 메뉴 — 내용 없는 최상위 제목 표시가 있다(304). 사이트 이름, 설명과 탐색 건너뛰기 링크가 있다(306–310). 개발자·개발 협력 기관·사용자 메뉴가 이어진다(312–322). |
| 323–358 | Documentation 메뉴 — 사용자 매뉴얼 v50·v51·v52·v53, 입력·출력 파일 설명, 버전 이력, 컴파일·명령행 옵션, FAQ와 SWAN 결합 안내의 링크가 있다(323–348). 예제, 보고서, 이론 자료, 개발자 안내와 특수 기능 자료의 링크가 이어진다(349–358). |
| 359–400 | Related software·News·Products·ASGS 메뉴 — 유틸리티와 격자 생성기 링크가 있다(359–361). 사용자 모임·워크숍·사진·발표·예측 사례의 링크가 있다(362–393). 조석 자료, 격자, 예측 제품과 ASGS 링크가 이어진다(394–400). |
| 401–405 | 문서 이동 경로·제목 — 사이트 이동 경로가 있다(402). 제목은 지정 유속(velocity) 기록 관측소(recording station)에서의 수심 평균(depth-averaged) 유속 시계열(time series) 출력 파일 fort.62를 가리킨다(404). 앞뒤 빈 줄을 포함한다(401·403·405). |
| 406–411 | Depth-averaged Velocity Time Series at Specified Velocity Recording Stations / 출력 대상·형식 — fort.15의 지정에 따라 유속 기록 관측소에서 수심 평균 유속 시계열을 출력한다(406). 굵은 변수명이 출력의 각 행을 나타내며, 빈 줄은 가독성을 위한 것이고 반복문은 여러 출력 행을 나타낸다(408). 매개변수 정의는 링크로 제공한다(408). 아스키(ascii) 또는 이진(binary) 형식은 모델 매개변수 및 주기 경계조건 파일의 NOUTV 설정에 따른다(410). 원문: `Depth-averaged velocity time series output at the velocity recording stations as specified in the [Model Parameter and Periodic Boundary Condition File](https://adcirc.org/home/documentation/users-manual-v53/input-file-descriptions/model-parameter-and-periodic-boundary-condition-file-fort-15).` (406); `Output may be in ascii or binary format depending on how [NOUTV](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#NOUTV) is set in the Model Parameter and Periodic Boundary Condition File` (410). |
| 412–424 | Depth-averaged Velocity Time Series at Specified Velocity Recording Stations / 파일 구조 — 실행 식별 정보가 두 원문 행에 나뉘어 있다(412–413). 출력 제어 관련 행, 시간·반복 단계 행, 관측소 반복문과 관측소별 두 유속 변수의 행을 제시한다(415–423). 변수의 기본값·범위·단위는 이 구간에 없다. 사이의 빈 줄과 반복문 종료 뒤 빈 줄을 포함한다(414·416·418·420·422·424). 파일 형식 원문: `[**RUNDES**](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#RUNDES),  ` (412); `[**RUNID**](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#RUNID), [**AGRID**](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#AGRID)` (413); `[**NTRSPV**](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#NTRSPV), [**NSTAV**](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#NSTAV), **[DTDP](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#DTDP)\*[NSPOOLV](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#NSPOOLV)**, [**NSPOOLV**](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#NSPOOLV), [**IRTYPE**](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#IRTYPE)` (415); `[**TIME**](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#TIME), [**IT**](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#IT)` (417); `for k=1, [NSTAV](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#NSTAV)` (419); `**k**, [**UU00(k), VV00(k)**](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#UU00_VV00)` (421); `end k loop` (423). |
| 425–430 | Depth-averaged Velocity Time Series at Specified Velocity Recording Stations / Note — 이진 출력을 지정하면 관측소 번호를 출력에 넣지 않는다(427). 주의 표시와 빈 줄을 포함한다(425–426·428–430). 원문: `If binary output is specified, the station number (k) is not included in the output.` (427). |
| 431–443 | 페이지 끝 스크립트 — 표시 유틸리티 호출이 있다(431). 사전 읽기 설정이 있다(433). 쿠키 안내 설정과 주석이 있다(436–438). jQuery 표시 상태 변경과 New Relic 정보가 있다(442–443). 사이의 빈 줄을 포함한다. |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 402행: 이동 경로의 Home과 Documentation 사이에 내용 없는 항목을 나타내는 연속 구분자 `»  »`가 있다.
- 408·410–421행: 원문은 매개변수 정의 페이지에 연결한다. 이 파일 안에는 `NOUTV`의 설정값·기본값과 `UU00(k)`·`VV00(k)`의 단위 및 성분 방향이 적혀 있지 않다.

