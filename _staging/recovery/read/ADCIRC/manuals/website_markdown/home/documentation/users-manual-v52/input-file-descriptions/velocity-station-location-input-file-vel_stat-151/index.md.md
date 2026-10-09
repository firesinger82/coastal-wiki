---
file: models/ADCIRC/raw/manuals/website_markdown/home/documentation/users-manual-v52/input-file-descriptions/velocity-station-location-input-file-vel_stat-151/index.md
lines: 436
sha256: 6620df8d6179d61b219ded9626df15de99255381b26532d3c4812f1489ea8a9b
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# Velocity Station Location input file (vel_stat.151) — 판독 구간 기록

구간은 1행부터 436행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–12 | 웹사이트 계측 스크립트(New Relic) — 계측 초기 설정(1)과 축약된 자바스크립트(JavaScript) 로더(2)를 포함한다. 3–12행은 빈 줄이다. |
| 13–77 | 웹사이트 스타일시트(CSS) / 머리말·배치 — 검색창과 버튼의 표시 규칙(13–25)을 포함한다. 머리말·본문의 글꼴과 색상, 페이지 컨테이너와 콘텐츠 영역의 배치를 지정한다(26–77). |
| 78–142 | 웹사이트 스타일시트 / 본문·링크 — 단일 열 콘텐츠와 본문 영역의 표시 규칙(78–93)을 포함한다. 문단·링크·탐색 경로(breadcrumb)·인용문·다른 콘텐츠 배치의 표시 규칙을 지정한다(94–142). |
| 143–200 | 웹사이트 스타일시트 / 탐색 메뉴 — 메뉴 영역·목록·메뉴 항목의 배치를 지정한다(143–176). 하위 메뉴의 위치·폭·색상·표시 규칙을 지정한다(177–200). |
| 201–231 | 웹사이트 스타일시트 / 메뉴 상태·이미지 크기 — 포인터를 올린 메뉴와 현재 메뉴 항목의 표시 규칙을 지정한다(201–225). 콘텐츠 높이·메뉴 글꼴·태그 숨김 규칙과 자동 크기 이미지 선택자 규칙을 포함한다(226–230). 229·231행은 빈 줄이다. |
| 232–241 | 페이지 제목·메타데이터 — 페이지 제목(232)과 페이지 URL·게시 시각·수정 시각·탐색 경로를 담은 JSON-LD(237)를 포함한다. 나머지 행은 빈 줄이다. |
| 242–270 | WordPress 이모지·블록 표시 — 이모지 설정(243)과 지원 검사·로딩 스크립트(245)를 포함한다. 이모지 표시 스타일(249–259)과 버튼·블록·색상·배치의 자동 생성 스타일(262–269)을 포함한다. 주석과 빈 줄도 이 구간에 포함한다. |
| 271–303 | 관리자 표시·방문 통계·배경 — 빈 줄과 관리자 표시 스타일(286–288)을 포함한다. 방문 통계 초기화(292–298)와 사이트 배경 이미지의 스타일(300)을 포함한다. |
| 304–322 | 사이트 제목·Community 메뉴 — 공식 사이트 제목과 탐색 건너뛰기 링크를 포함한다(304–310). 개발 그룹·개발 협력 기관·사용자 메뉴를 나열한다(312–322). |
| 323–358 | Documentation 메뉴 — 사용자 매뉴얼·컴파일 옵션·FAQ·위키·예제·보고서·논문 링크를 나열한다(323–358). 모델 입력 형식의 기술 본문은 이 구간에 없다. |
| 359–400 | Related software·News·Products·ASGS 메뉴 — 관련 소프트웨어 링크를 나열한다(359–361). 행사·발표 자료·단체 사진·예보·시뮬레이션·제품·ASGS 링크를 나열한다(362–400). 단체 사진은 일반 링크로 적혀 있다. |
| 401–405 | 본문 탐색 경로·제목 — 매뉴얼 내 페이지 위치(402)와 이 페이지의 제목(404)을 표시한다. 나머지 행은 빈 줄이다. |
| 406–409 | Velocity Station Location input file / 적용 조건·표시 규칙 — 유속 기록 지점(velocity recording station) 위치 파일을 읽는 조건을 제시한다(406). 굵은 변수명은 입력 한 행을 나타낸다고 설명한다(408). 빈 줄·반복문·변수 정의 링크의 표시 규칙을 설명한다(408). 원문: `The reading of the vel\_stat.151 file is triggered when the number of velocity recording stations ([NSTAV](https://adcirc.org/home/documentation/users-manual-v52/parameter-definitions#NSTAV)) in the [fort.15 file](https://adcirc.org/home/documentation/users-manual-v52/input-file-descriptions/model-parameter-and-periodic-boundary-condition-file-fort-15/) is set to a negative value.` (406); `The basic file structure is shown below. Each line of input data is represented by a line containing the input variable name(s) in bold face type. Blank lines are only to enhance readability. Loops indicate multiple lines of input. Definitions of each variable are provided via hot links.` (408). |
| 410–417 | 입력 형식 — 지점 수 필드와 지점별 좌표 쌍의 반복 형식을 제시한다(410–416). 변수명은 정의 링크로 연결되어 있다(410–414). 원문: `[**NSTAV2**](https://adcirc.org/home/documentation/users-manual-v52/parameter-definitions#NSTAV2)` (410); `for k=1,[NSTAV2](https://adcirc.org/home/documentation/users-manual-v52/parameter-definitions#NSTAV2)` (412); `**[XEV(k)](https://adcirc.org/home/documentation/users-manual-v52/parameter-definitions#XEV)**, **[YEV(k)](https://adcirc.org/home/documentation/users-manual-v52/parameter-definitions#YEV)**` (414); `end k loop` (416). |
| 418–423 | Notes / 지점 수 처리 — 지점 수 값이 다를 때 사용할 값과 파일 내 지점 수가 부족하거나 초과할 때의 처리 규칙을 제시한다(418–420). 421–423행은 빈 줄이다. 원문: `**Notes:**` (418); `If the value of NSTAV2 differs from the value of NSTAV (as read from the fort.15 file) the value of NSTAV2 will be used. If there are fewer than NSTAV2 stations listed in the vel\_stat.151 file, ADCIRC will stop with an error. If there are more than NSTAV2 stations listed in the vel\_stat.151 file, only the first NSTAV2 of them will be used.` (420). |
| 424–436 | 페이지 끝 스크립트 — 사이트 유틸리티 호출(424), 링크 미리 읽기 설정(426), 쿠키 안내문 설정과 주석(429–431)을 포함한다. 표시 클래스 변경(435)과 계측 정보(436)를 포함한다. 나머지 행은 빈 줄이다. |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 414: 이 파일은 `XEV(k)`와 `YEV(k)`의 좌표 단위를 제시하지 않는다.
