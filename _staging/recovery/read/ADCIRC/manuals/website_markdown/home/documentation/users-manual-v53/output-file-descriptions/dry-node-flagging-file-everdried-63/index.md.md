---
file: models/ADCIRC/raw/manuals/website_markdown/home/documentation/users-manual-v53/output-file-descriptions/dry-node-flagging-file-everdried-63/index.md
lines: 454
sha256: c10d9f733880310b562119bed6e67361e18a4f9a781be05e5afa174358e4668c
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# Dry node flagging file (everdried.63) — 판독 구간 기록

구간은 1행부터 454행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–12 | 페이지 계측 스크립트 — New Relic의 초기화와 압축 JavaScript가 있다(1–2). 뒤에 빈 줄이 이어진다(3–12). |
| 13–70 | 페이지 기본 서식 — 이동 경로 검색 입력, 머리글, 본문, 링크, 페이지 컨테이너와 표제의 CSS 서식을 정한다(13–70). |
| 71–142 | 본문·열 배치 서식 — 본문 영역, 문단, 링크, 오른쪽 열, 이동 경로, 활성 메뉴, 인용문과 다중 열 배치의 CSS가 있다(71–142). |
| 143–228 | 탐색 메뉴 서식 — 상위 메뉴와 하위 메뉴의 배치, 배경 이미지 참조, 마우스가 놓였을 때의 표시, 현재 메뉴 항목, 표제 숨김의 CSS가 있다(143–228). |
| 229–241 | 페이지 제목·구조화 메타데이터 — 빈 줄과 이미지 크기 CSS를 포함한다(229–231). 문서 제목이 있다(232). JSON-LD가 문서 주소, 제목, 발행 시각, 이동 경로와 사이트 검색 정보를 담는다(237). 뒤 빈 줄도 포함한다(238–241). |
| 242–261 | 이모지 표시 스크립트·서식 — WordPress의 이모지 설정, 표시 지원 검사와 관련 스크립트가 있다(242–246). 이모지와 스마일 이미지의 CSS 및 빈 줄이 이어진다(247–261). |
| 262–285 | WordPress 공통 서식 — 자동 생성 표시, 버튼·파일 링크 서식, 종횡비·색·그라데이션·글자 크기·간격·그림자 및 블록 배치의 CSS가 있다(262–269). 뒤 빈 줄을 포함한다(270–285). |
| 286–303 | 관리 표시·접속 통계·페이지 배경 — 관리 표시 CSS가 있다(286–288). 접속 통계 초기화와 설정이 있다(292–298). 페이지 배경 이미지 참조가 있다(300). 사이의 공백 행과 뒤 빈 줄을 포함한다(289–291·299·301–303). |
| 304–322 | 사이트 표제·Community 메뉴 — 내용 없는 최상위 제목 표시가 있다(304). 사이트 이름, 설명과 탐색 건너뛰기 링크가 있다(306–310). 개발자·개발 협력 기관·사용자 메뉴가 이어진다(312–322). |
| 323–358 | Documentation 메뉴 — 사용자 매뉴얼 v50·v51·v52·v53, 입력·출력 파일 설명, 버전 이력, 컴파일·명령행 옵션, FAQ와 SWAN 결합 안내의 링크가 있다(323–348). 예제, 보고서, 이론 자료, 개발자 안내와 특수 기능 자료의 링크가 이어진다(349–358). |
| 359–400 | Related software·News·Products·ASGS 메뉴 — 유틸리티와 격자 생성기 링크가 있다(359–361). 사용자 모임·워크숍·사진·발표·예측 사례의 링크가 있다(362–393). 조석 자료, 격자, 예측 제품과 ASGS 링크가 이어진다(394–400). |
| 401–405 | 문서 이동 경로·제목 — 사이트 이동 경로가 있다(402). 제목은 건조 노드(dry node) 표시 파일 everdried.63을 가리킨다(404). 앞뒤 빈 줄을 포함한다(401·403·405). |
| 406–411 | Dry node flagging file / 목적·활성화 조건·두 데이터셋 — 시뮬레이션(simulation) 중 한 번이라도 건조해진 노드를 표시하여 조화 분석(harmonic analysis)을 지원한다(406). 한 시간 단계(time step) 동안만 건조해져도 수위(water surface elevation)에 기록되는 값이 조화 분석 해를 오염시킨다고 설명한다(406). fort.15 하단의 선택 사항인 네임리스트(namelist)에서 출력 매개변수를 설정하면 파일 쓰기를 활성화한다(408). 첫 데이터셋(data set)은 습윤·건조 상태(wet/dry state)를 기록한다(410). 두 번째 데이터셋은 노드가 건조했던 총 시간을 초(seconds) 단위로 기록한다(410). 값과 조건의 원문: `The everdried.63 file was created to support harmonic analysis by flagging all nodes that had ever become dry during the course of a simulation. These data are useful to harmonic analysis because a node that goes dry for a single time step has a -99999 recorded for its water surface elevation, which contaminates the harmonic analysis solution.` (406); `The writing of the everdried.63 output file is activated when the inundationOutput parameter is set to .true. in the optional inundationOutputContol namelist at the bottom of the [fort.15 file](https://adcirc.org/home/documentation/users-manual-v53/input-file-descriptions/model-parameter-and-periodic-boundary-condition-file-fort-15/).` (408); `The file contains two data sets. The first dataset provides information about the wet/dry state, where a node is given a value of -99999.0 if it ever went dry during the simulation, and a value of 1.0 if it was wet for the entire simulation. The second data set lists the total time in seconds that a node was dry during the simulation (0.0 if it was always wet).` (410). |
| 412–415 | Dry node flagging file / 구조 안내·출력 형식 — 굵은 변수명이 출력의 각 행을 나타내며, 빈 줄은 가독성을 위한 것이고 반복문은 여러 출력 행을 나타낸다(412). 변수 정의는 링크로 제공한다(412). 아스키(ascii) 또는 netCDF 형식은 fort.15의 NOUTGE 설정에 따른다(414). 사이와 뒤의 빈 줄을 포함한다(413·415). 출력 조건 원문: `Output may be in ascii or netCDF format depending on how [NOUTGE](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#NOUTGE) is set in the [Model Parameter and Periodic Boundary Condition (fort.15) File](https://adcirc.org/home/documentation/users-manual-v53/input-file-descriptions/model-parameter-and-periodic-boundary-condition-file-fort-15/).` (414). |
| 416–435 | Dry node flagging file / 파일 구조 — 실행 식별 정보, 데이터셋 수를 나타내는 상수와 출력 제어 관련 변수, 첫 데이터셋의 시간·반복 단계 및 노드별 건조 표시 값을 제시한다(416–426). 두 번째 데이터셋에도 시간·반복 단계와 노드 반복문이 있고 노드별 누적 건조 시간 값을 기록한다(428–434). 사이의 빈 줄과 뒤 빈 줄을 포함한다(417·419·421·423·425·427·429·431·433·435). 파일 형식 원문: `[**RUNDES**](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#RUNDES), [**RUNID**](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#RUNID), [**AGRID**](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#AGRID)` (416); `2, [**NP**](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#NP), [**DTDP**](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#DTDP)\*[**NSPOOLGE**](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#NSPOOLGE), [**NSPOOLGE**](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#NSPOOLGE), [**IRTYPE**](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#IRTYPE)` (418); `[**TIME**](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#TIME), [**IT**](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#IT)` (420); `for k=1,[NP](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#NP)` (422); `**k,** [**everdried(k)**](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#everdried)` (424); `end k loop` (426); `[**TIME**](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#TIME), [**IT**](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#IT)` (428); `for k=1,[NP](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#NP)` (430); `**k,** [**driedtime(k)**](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#driedtime)` (432); `end k loop` (434). |
| 436–441 | Dry node flagging file / Notes — 시간 단계 진행(timestepping)이 끝난 뒤 시뮬레이션의 맨 끝에서 파일을 쓴다(438). 재시작(hotstart)한 실행이어도 값은 현재 실행만 반영한다(438). 주의 표시와 빈 줄을 포함한다(436–437·439–441). 적용 범위 원문: `The everdried.63 file is written at the very end of the simulation, after timestepping is complete. The values only reflect the current run, even if the run was hotstarted.` (438). |
| 442–454 | 페이지 끝 스크립트 — 표시 유틸리티 호출이 있다(442). 사전 읽기 설정이 있다(444). 쿠키 안내 설정과 주석이 있다(447–449). jQuery 표시 상태 변경과 New Relic 정보가 있다(453–454). 사이의 빈 줄을 포함한다. |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 402행: 이동 경로의 Home과 Documentation 사이에 내용 없는 항목을 나타내는 연속 구분자 `»  »`가 있다.
- 412·414·418행: 원문은 변수 정의 페이지에 연결한다. 이 파일 안에는 `NOUTGE`의 설정값·기본값과 `DTDP`·`NSPOOLGE`·`IRTYPE`의 정의가 적혀 있지 않다.

