---
file: models/ADCIRC/raw/manuals/website_markdown/home/documentation/users-manual-v53/output-file-descriptions/maximum-inundation-depth-file-maxinundepth-63/index.md
lines: 452
sha256: 193b361bb429555805ada55b9551fe914a339ea223d3445d843531b34bcff97c
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# index.md — 판독 구간 기록

구간은 1행부터 452행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–12 | 웹페이지 계측 스크립트 — New Relic 초기화 설정과 브라우저 이벤트 수집·스크립트 적재 코드가 있다(1–2). 이어지는 빈 줄을 포함한다(3–12). |
| 13–77 | 웹페이지 스타일(CSS) / 검색·제목·본문 — 검색 입력란과 버튼의 표시 규칙이 있다(13–25). 머리글·본문·컨테이너·태그·오른쪽 본문 영역의 글꼴·색·배치 규칙이 있다(26–77). |
| 78–142 | 웹페이지 CSS / 본문·링크·경로 표시 — 단일 열 본문과 본문 내부 영역의 배치 규칙이 있다(78–93). 문단·링크·경로 표시(breadcrumbs)·인용문·다른 본문 영역의 표시 규칙과 빈 줄을 포함한다(94–142). |
| 143–200 | 웹페이지 CSS / 탐색 메뉴 — 탐색 영역과 메뉴 목록의 배치·배경·링크 표시 규칙이 있다(143–176). 하위 메뉴의 숨김·위치·너비·높이 규칙이 있다(177–200). |
| 201–230 | 웹페이지 CSS / 메뉴 선택·이미지 배치 — 마우스가 놓인 메뉴와 현재 선택된 메뉴의 표시 규칙이 있다(201–225). 슬라이드 영역·메뉴 글꼴·태그 숨김·이미지의 고유 크기 규칙과 빈 줄을 포함한다(226–230). |
| 231–241 | 페이지 제목·구조화 메타데이터 — 페이지 제목은 Maximum inundation depth file (maxinundepth.63)이다(232). 구조화 데이터(JSON-LD)는 페이지 URL·발행일·수정일·설명·언어·상위 웹사이트·경로 표시·검색 동작을 담는다(237). 주변 빈 줄을 포함한다(231·233–236·238–241). |
| 242–260 | WordPress 이모지(emoji) 설정 — 이모지 자원 경로와 브라우저 지원 검사·스크립트 적재 코드가 있다(242–246). 이모지 이미지의 표시 규칙과 빈 줄을 포함한다(247–260). |
| 261–270 | WordPress 블록 스타일 — 자동 생성 주석과 버튼·파일 버튼 스타일이 있다(262–263). 화면 비율·색·그라데이션·글자 크기·간격·그림자 설정 및 배치 규칙이 있다(266–269). 빈 줄을 포함한다(261·264–265·270). |
| 271–303 | 웹페이지 지원·방문 계측·배경 — 관리자 지원 표시의 배경색 규칙이 있다(286–288). Beehive 방문 계측 초기화와 설정이 있다(292–298). 페이지 배경 이미지의 표시 규칙과 빈 줄을 포함한다(300–303). |
| 304–311 | 웹페이지 머리글 — 내용이 없는 제목 마크업과 빈 줄을 포함한다(304–305·307·309·311). ADCIRC 홈페이지 링크·공식 웹사이트 문구·탐색 건너뛰기 링크가 있다(306·308·310). |
| 312–358 | 웹사이트 탐색 / Community·Documentation — 개발자·협력 기관·사용자 링크가 있다(312–322). 사용자 매뉴얼의 판본별 입력·출력·판본 이력, 컴파일·실행 옵션, FAQ, 예제, 보고서·논문 링크가 있다(323–358). |
| 359–401 | 웹사이트 탐색 / Related software·News·Products·ASGS — 관련 소프트웨어 링크가 있다(359–361). 사용자 모임·워크숍·사진·발표·예보·시뮬레이션 링크가 있다(362–393). 조석 자료·논문·격자·예보 제품과 ASGS 링크 및 마지막 빈 줄을 포함한다(394–401). |
| 402–403 | 본문 경로 표시 — 홈페이지·Documentation·User’s Manual – v53·Output File Descriptions에서 Maximum inundation depth file (maxinundepth.63)로 이어지는 경로 표시와 다음 빈 줄을 포함한다(402–403). |
| 404–409 | Maximum inundation depth file (maxinundepth.63) / 개요·활성화 — 문서는 지면 위 최대 침수 깊이(maximum inundation depth)를 기록한다고 설명한다(404·406). 문서는 초기 건조 영역(initially dry areas)에만 기록한다고 설명한다(406). 침수 깊이의 단위·기록 영역·한 번도 젖지 않은 영역의 값은 원문 그대로 옮긴다: `The maximum inundation depth (maxinundepth.63) file records the peak inundation depth (in meters) above ground that occurred during the simulation. The data are only recorded in areas that are initially dry according to the initiallydry.63 file. The values are -99999.0 if the area was never wet during the simulation.` (406). 출력 활성화 매개변수·값·선택적 이름 목록(namelist)·입력 파일 위치는 원문 그대로 옮긴다: `The writing of the maxinundepth.63 output file is activated when the inundationOutput parameter is set to .true. in the optional inundationOutputContol namelist at the bottom of the fort.15 file.` (408). 제목과 문단 사이의 빈 줄을 포함한다(405·407·409). |
| 410–415 | Maximum inundation depth file / 자료 집합·형식 안내 — 첫 자료 집합(data set)은 최대 침수값을 담는다(410). 둘째 자료 집합은 최대 침수값의 발생 시각을 담는다(410). 자료 집합 수·시각 단위·시각 기준 원문: `The file contains two data sets. The first dataset contains the peak inundation value, and the second data set contains the time of occurrence of the peak inundation value in seconds since cold start.` (410). 구조 안내는 굵은 변수 이름 한 줄이 출력 한 줄을 나타낸다고 설명한다(412). 구조 안내는 가독성을 위한 빈 줄·여러 출력 줄을 나타내는 반복·변수 정의 링크를 설명한다(412). 출력 형식의 적용 조건 원문: `Output may be in ascii or netCDF format depending on how [NOUTGE](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#NOUTGE) is set in the [Model Parameter and Periodic Boundary Condition (fort.15) File](https://adcirc.org/home/documentation/users-manual-v53/input-file-descriptions/model-parameter-and-periodic-boundary-condition-file-fort-15/).` (414). 문단 사이의 빈 줄을 포함한다(411·413·415). |
| 416–425 | Maximum inundation depth file / 머리글·최대 침수값 자료 — 파일 머리글과 첫 자료 집합의 변수 배열·노드 반복을 제시한다(416–424). 출력 형식 원문: `[**RUNDES**](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#RUNDES), [**RUNID**](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#RUNID), [**AGRID**](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#AGRID)` (416); `2, [**NP**](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#NP), [**DTDP**](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#DTDP)\*[**NSPOOLGE**](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#NSPOOLGE), [**NSPOOLGE**](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#NSPOOLGE), [**IRTYPE**](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#IRTYPE)` (418); `[**TIME**](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#TIME), [**IT**](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#IT)` (420); `for k=1,[NP](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#NP)` (422); `**k,** [**maxinundepth(k)**](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#maxinundepth)` (424). 각 출력 형식 줄 사이와 구간 끝의 빈 줄을 포함한다(417·419·421·423·425). |
| 426–433 | Maximum inundation depth file / 최대 침수값 발생 시각 자료 — 둘째 자료 집합의 시각·시간 단계, 노드 반복과 최대 침수 발생 시각 필드를 제시한다(426–432). 출력 형식 원문: `[**TIME**](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#TIME), [**IT**](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#IT)` (426); `for k=1,[NP](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#NP)` (428); `**k,** [**maxinundepth\_time(k)**](https://adcirc.org/home/documentation/users-manual-v53/parameter-definitions#maxinundepth_time)` (430); `end k loop` (432). 각 출력 형식 줄 사이와 구간 끝의 빈 줄을 포함한다(427·429·431·433). |
| 434–437 | Notes / 기록 시점·실행 범위 — 시간 단계 계산(timestepping)이 끝난 뒤 시뮬레이션의 맨 끝에 파일을 쓴다고 설명한다(436). 재시작(hotstart)한 실행에서도 값은 현재 실행만 반영한다고 설명한다(436). 초기 건조 영역에만 최대 침수 깊이를 기록한다는 조건을 다시 명시한다(436). 조건 원문: `The maxinundepth.63 file is written at the very end of the simulation, after timestepping is complete. The values only reflect the current run, even if the run was hotstarted. The data in the maxinundepth.63 file only record maximum inundation depth in areas that are initially dry, according to the initiallydry.63 file.` (436). 절 제목과 빈 줄을 포함한다(434–435·437). |
| 438–452 | 웹페이지 끝부분 — 빈 줄과 표시 보조 함수 호출을 포함한다(438–441). 링크 사전 적재(prefetch) 설정이 있다(442). 쿠키 안내 설정과 주석·빈 줄이 있다(443–450). 슬라이드 컨테이너의 클래스 변경과 New Relic 페이지 계측 정보로 끝난다(451–452). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 422–432행: `for k=1,`로 시작하는 노드 반복은 422행과 428행에 있다. 원문은 첫 반복 뒤에 종료 줄을 표시하지 않고 426행의 다음 자료 집합으로 이어진다. `end k loop`는 432행에만 있다.
