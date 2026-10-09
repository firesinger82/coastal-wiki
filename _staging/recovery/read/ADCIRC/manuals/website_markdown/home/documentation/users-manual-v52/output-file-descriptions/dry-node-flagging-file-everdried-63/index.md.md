---
file: models/ADCIRC/raw/manuals/website_markdown/home/documentation/users-manual-v52/output-file-descriptions/dry-node-flagging-file-everdried-63/index.md
lines: 454
sha256: 40c450ff3902bccfb8558ed730da594b5735321b3c2f7d9cd17dbf04030c782f
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# index.md — 판독 구간 기록

구간은 1행부터 454행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–12 | 웹사이트 계측 스크립트 — New Relic 초기화 설정과 브라우저 계측 로더 JavaScript가 있다(1–2). 이어지는 빈 줄을 포함한다(3–12). |
| 13–70 | 웹사이트 스타일 / 검색·머리말 — 검색 입력과 버튼, 링크, 본문 글꼴·색상, 머리말과 페이지 컨테이너의 CSS가 있다(13–70). |
| 71–142 | 웹사이트 스타일 / 본문·탐색 경로 — 본문 열 배치, 문단, 링크, 오른쪽 목록, 탐색 경로(breadcrumbs), 인용문과 제목의 CSS가 있다(71–142). |
| 143–176 | 웹사이트 스타일 / 주 메뉴 — 메뉴 영역, 목록, 목록 항목과 링크의 CSS가 있다(143–176). 메뉴 구분선 배경 이미지 경로가 있다(166). |
| 177–230 | 웹사이트 스타일 / 하위 메뉴 — 하위 메뉴 배치, 마우스 포인터를 올렸을 때의 배경, 현재 메뉴 항목, 메뉴 글꼴과 이미지 크기 처리의 CSS가 있다(177–230). 메뉴 배경 이미지 경로가 있다(202). |
| 231–241 | 페이지 제목·구조화 메타데이터 — 페이지 제목이 있다(232). JSON-LD는 페이지 주소, 제목, 게시·수정 시각, 탐색 경로와 사이트 검색 정보를 담는다(237). 빈 줄을 포함한다(231·233–236·238–241). |
| 242–260 | 웹사이트 이모지 처리 — WordPress 이모지 자원 설정과 지원 여부 검사 JavaScript가 있다(242–246). 이모지 표시 CSS와 빈 줄을 포함한다(247–260). |
| 261–285 | 웹사이트 전역 스타일 — 자동 생성 표시와 버튼·파일 버튼 CSS가 있다(262–263). 화면 비율, 색상, 그라데이션, 글자 크기, 간격, 그림자와 배치의 전역 CSS가 있다(266–269). 빈 줄을 포함한다(261·264–265·270–285). |
| 286–303 | 웹사이트 관리·접속 분석·배경 — 관리 막대 CSS가 있다(286–288). Beehive 접속 분석 초기화와 설정 JavaScript가 있다(292–298). 페이지 배경 이미지 URL을 포함하는 CSS와 빈 줄이 있다(300–303). |
| 304–322 | 사이트 머리말·Community 메뉴 — 빈 제목 마크업, ADCIRC 사이트 링크, 공식 웹사이트 표제와 탐색 건너뛰기 링크가 있다(304–310). 개발 그룹, 협력 기관과 사용자 메뉴를 나열한다(312–322). |
| 323–358 | Documentation 메뉴 — 사용자 설명서, 컴파일 옵션, FAQ, 위키와 버전별 입력·출력·버전 이력 링크를 나열한다(323–348). 예제, 보고서, 개발자 안내서, 이론 보고서, 특수 기능과 관련 출판물 링크를 나열한다(349–358). |
| 359–393 | Related software·News 메뉴 — 유틸리티와 격자 생성기(grid generator) 링크가 있다(359–361). 사용자 모임의 발표·사진·일정과 폭풍해일 예측·허리케인 모의 링크를 나열한다(362–393). |
| 394–403 | Products·ASGS 메뉴·본문 탐색 경로 — 조석 데이터베이스(tidal databases), 출판물, 격자, 예측과 유류 이동 모의 링크가 있다(394–399). ASGS 링크와 현재 v52 출력 문서까지의 탐색 경로가 있다(400–402). 빈 줄을 포함한다(401·403). |
| 404–411 | Dry node flagging file (`everdried`.63) / 목적·활성화·자료 — 모의 중 한 번이라도 건조해진 절점(dry node)을 표시하여 조화 분석(harmonic analysis)을 지원한다(406). 한 시간 단계(time step)라도 건조해진 절점의 수위(water surface elevation)에 기록된 -99999가 조화 분석 해를 오염시킨다고 설명한다(406). 파일 생성 조건은 408행에 있다. 첫 자료집합(data set)은 습윤/건조 상태(wet/dry state)를 나타낸다(410). 두 번째 자료집합은 절점이 건조했던 총 시간을 초 단위로 나타낸다(410). 조건·값·단위 원문: `The everdried.63 file was created to support harmonic analysis by flagging all nodes that had ever become dry during the course of a simulation. These data are useful to harmonic analysis because a node that goes dry for a single time step has a -99999 recorded for its water surface elevation, which contaminates the harmonic analysis solution.` (406); `The writing of the everdried.63 output file is activated when the inundationOutput parameter is set to .true. in the optional inundationOutputContol namelist at the bottom of the [fort.15 file](https://adcirc.org/home/documentation/users-manual-v52/input-file-descriptions/model-parameter-and-periodic-boundary-condition-file-fort-15/).` (408); `The file contains two data sets. The first dataset provides information about the wet/dry state, where a node is given a value of -99999.0 if it ever went dry during the simulation, and a value of 1.0 if it was wet for the entire simulation. The second data set lists the total time in seconds that a node was dry during the simulation (0.0 if it was always wet).` (410) |
| 412–415 | `everdried`.63 / 구조 안내·형식 — 각 굵은 변수명 줄은 출력 한 줄에 대응한다(412). 빈 줄은 가독성을 위한 것이며 반복문은 여러 출력 줄을 나타낸다(412). `NOUTGE` 설정에 따라 ASCII 또는 netCDF 형식으로 출력할 수 있다(414). 조건 원문: `Output may be in ascii or netCDF format depending on how [NOUTGE](https://adcirc.org/home/documentation/users-manual-v52/parameter-definitions#NOUTGE) is set in the [Model Parameter and Periodic Boundary Condition (fort.15) File](https://adcirc.org/home/documentation/users-manual-v52/input-file-descriptions/model-parameter-and-periodic-boundary-condition-file-fort-15/).` (414) |
| 416–427 | `everdried`.63 / 첫 자료집합 — `RUNDES`, `RUNID`, `AGRID` 다음에 2, `NP`, `DTDP`와 `NSPOOLGE`의 곱, `NSPOOLGE`, `IRTYPE`를 제시한다(416–418). `TIME`, `IT` 다음에 k를 1부터 `NP`까지 반복하여 k, `everdried(k)`를 쓴다(420–426). 이 구간의 변수 기본값·정의는 본문에 제시되지 않는다. 형식 원문: `[**RUNDES**](https://adcirc.org/home/documentation/users-manual-v52/parameter-definitions#RUNDES), [**RUNID**](https://adcirc.org/home/documentation/users-manual-v52/parameter-definitions#RUNID), [**AGRID**](https://adcirc.org/home/documentation/users-manual-v52/parameter-definitions#AGRID)` (416); `2, [**NP**](https://adcirc.org/home/documentation/users-manual-v52/parameter-definitions#NP), [**DTDP**](https://adcirc.org/home/documentation/users-manual-v52/parameter-definitions#DTDP)\*[**NSPOOLGE**](https://adcirc.org/home/documentation/users-manual-v52/parameter-definitions#NSPOOLGE), [**NSPOOLGE**](https://adcirc.org/home/documentation/users-manual-v52/parameter-definitions#NSPOOLGE), [**IRTYPE**](https://adcirc.org/home/documentation/users-manual-v52/parameter-definitions#IRTYPE)` (418); `[**TIME**](https://adcirc.org/home/documentation/users-manual-v52/parameter-definitions#TIME), [**IT**](https://adcirc.org/home/documentation/users-manual-v52/parameter-definitions#IT)` (420); `for k=1,[NP](https://adcirc.org/home/documentation/users-manual-v52/parameter-definitions#NP)` (422); `**k,** [**everdried(k)**](https://adcirc.org/home/documentation/users-manual-v52/parameter-definitions#everdried)` (424); `end k loop` (426) |
| 428–435 | `everdried`.63 / 두 번째 자료집합 — `TIME`, `IT` 다음에 k를 1부터 `NP`까지 반복하여 k, `driedtime(k)`를 쓴다(428–434). 반복문 종료와 빈 줄을 포함한다(434–435). 형식 원문: `[**TIME**](https://adcirc.org/home/documentation/users-manual-v52/parameter-definitions#TIME), [**IT**](https://adcirc.org/home/documentation/users-manual-v52/parameter-definitions#IT)` (428); `for k=1,[NP](https://adcirc.org/home/documentation/users-manual-v52/parameter-definitions#NP)` (430); `**k,** [**driedtime(k)**](https://adcirc.org/home/documentation/users-manual-v52/parameter-definitions#driedtime)` (432); `end k loop` (434) |
| 436–441 | `everdried`.63 / Notes — 시간 적분(timestepping)이 완료된 모의 종료 시점에 파일을 쓴다(438). 핫스타트(hotstarted) 실행인 경우에도 값은 현재 실행만 반영한다(438). 주석 표제와 빈 줄을 포함한다(436–441). 조건 원문: `The everdried.63 file is written at the very end of the simulation, after timestepping is complete. The values only reflect the current run, even if the run was hotstarted.` (438) |
| 442–454 | 웹사이트 후처리 — 화면 유틸리티 호출과 링크 사전 로드(prefetch) 설정이 있다(442–444). 쿠키 동의 안내 설정과 주석이 있다(447–449). jQuery 표시 처리와 New Relic 페이지 정보가 마지막 행까지 이어진다(453–454). 빈 줄을 포함한다(443·445–446·450–452). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 408: 선택적 namelist 이름은 `inundationOutputContol`로 적혀 있다. 이름의 끝부분은 `Contol`이다.
