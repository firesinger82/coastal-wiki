---
file: models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_15.md
lines: 36
sha256: 140e78fad0cea85922153383ec588b238603a8ea473895648abb8c40fbab7f04
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Card_Image_15.md — 판독 구간 기록

구간은 1행부터 36행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | 문서 메타데이터(metadata) — 페이지 ID(2), 제목(3), space(4), 원문 URL(5), 버전(6), 갱신 시각(7), 문서 계층 경로(8)를 기록한다. `---` 구분자를 포함한다(1·9). |
| 10–19 | C15 PERIODIC FORCING (TIDAL) CONSTITUENT SYMBOLS AND PERIODS — 주기 조석 강제력(periodic tidal forcing)의 성분 기호(constituent symbol)와 주기를 설명한다(10). `SYMBOL`은 문자 변수(character variable)의 강제력 기호이며 조석에는 NOS 기호를 사용한다고 적는다(14). `PERIOD`의 단위는 초이다(16). 매개변수·단위 원문: `\* SYMBOL: FORCING SYMBOL (CHARACTER VARIABLE) FOR TIDES, THE NOS SYMBOL` (14); `\* PERIOD: FORCING PERIOD IN SECONDS` (16). 주석용 `\*` 줄과 빈 줄을 포함한다. |
| 20–36 | C15 / 입력 예시 — `SYMBOL PERIOD` 헤더와 `'Q1'`, `'O1'`, `'P1'`, `'K1'`, `'N2'`, `'M2'`, `'S2'`, `'K2'`의 주기 값을 초 단위로 적는다(20–36). 주기는 원문 자릿수를 유지했다. 입력 줄 원문: `C15 SYMBOL PERIOD` (20); `               'Q1'  96725.8` (22); `               'O1'  92949.87` (24); `               'P1'  86637.38` (26); `               'K1'  86163.91` (28); `               'N2'  45570.1` (30); `               'M2'  44714.17` (32); `               'S2'  43200` (34); `               'K2'  43082.1` (36). 줄 사이 빈 줄을 포함한다. |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 14행: `NOS SYMBOL`을 언급한다. 이 파일에는 `NOS`의 풀이나 정의가 없다.

