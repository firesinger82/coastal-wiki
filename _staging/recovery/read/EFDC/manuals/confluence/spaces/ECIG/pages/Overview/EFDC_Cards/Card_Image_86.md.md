---
file: models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_86.md
lines: 24
sha256: 70f36a9560dca6221b82783e6aa8ca601209834d8e807b09170712d2bb9f78c0
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Card_Image_86.md — 판독 구간 기록

구간은 1행부터 24행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | 원문 메타데이터(frontmatter) — 문서 ID·제목·space·URL·버전·갱신 시각·계층 경로를 적는다(1–9). |
| 10–22 | C86 CONTROLS FOR WRITING TO TIME SERIES FILES — 시계열(time series) 파일의 시작·종료 시나리오(start-stop scenario) 번호, 시나리오별 종료·시작 쌍(stop-start pair) 수, 시작·종료 시각을 정의한다(10·14–20). 시각 설명의 저장 간격(save interval) 이름과 번호 범위 문자열을 원문 그대로 옮긴다(14·18–20). 설명 없이 남은 주석 값과 주석 표식·빈 줄을 포함한다(11–22). 원문: `C86 CONTROLS FOR WRITING TO TIME SERIES FILES` (10); `\* ITSSS: START-STOP SCENARIO NUMBER 1.GE.ISSS.LE.NTSSTSP` (14); `\* MTSSS: NUMBER OF STOP-START PAIRS FOR SCENARIO ISSS` (16); `\* TSSTRT: STARTING TIME FOR SCENARIO ITSSS, SAVE INTERVAL MTSSS` (18); `\* TSSTOP: STOPING TIME FOR SCENARIO ITSSS, SAVE INTERVAL MTSSS` (20); `\*                                  -1000.` (22). |
| 23–24 | C86 입력 열 제목 — 시나리오 번호·쌍 수·시각·주석 열을 제시한다(24). 앞 빈 줄을 포함한다(23). 원문: `C86 ISSS MTSSS TSSTRT TSSTOP COMMENT` (24). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 14–20·24행: 시나리오 번호의 정의 이름과 시각 설명은 `ITSSS`를 쓰지만 범위·쌍 수 설명·입력 열 제목은 `ISSS`를 쓴다. `NTSSTSP`의 정의는 이 파일에 없다. 범위 문자열의 첫 비교는 `1.GE.ISSS`로 적는다.
- 18–20행: 시작·종료 시각의 단위를 이 파일에 적지 않는다.
- 22행: 이름이나 설명이 없는 주석 값 `-1000.`이 있다.
- 24행: `COMMENT` 열이 있으나 이 파일에는 해당 열의 설명이 없다.

