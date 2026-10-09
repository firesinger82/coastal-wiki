---
file: models/ADCIRC/raw/source_code/adcirc/docs/tools/metget.rst
lines: 24
sha256: 488d3344d53838caabff58df32190df057a6ebbc045815f4c352a74e679d78a6
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# metget.rst — 판독 구간 기록

구간은 1행부터 24행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–7 | MetGet — `:orphan:` 지시문과 제목을 포함한다(1–4). 여러 자료원의 기상 자료(meteorological data)를 조회(query)·형식화(format)·혼합(blend)해 ADCIRC 등 유체역학 모델(hydrodynamic model)의 기상 강제력을 획득·개발하는 애플리케이션으로 소개한다(6). 원문: `:orphan:` (1); `MetGet` (3); `======` (4); `MetGet is an application which allows users to query, format, and blend meteorological data from various sources to be used in hydrodynamic modeling applications. It serves as a meteorological forcing acquisition and development system specifically designed for hydrodynamic models like ADCIRC.` (6). |
| 8–17 | Key Features — 기상 자료 조회·형식화·혼합, ADECK 폭풍 경로 자료(storm track data) 접근, 지정 해역의 활동 중인 폭풍 조회를 열거한다(10–14). 명령줄 인터페이스(command-line interface)와 맞춤 애플리케이션용 Python 클라이언트 라이브러리(client library)를 설명한다(15–16). 원문: `**Key Features:**` (8); `* Query meteorological data from various sources` (10); `* Format data for use in hydrodynamic models` (11); `* Blend meteorological data from multiple sources` (12); `* Access to storm track data (ADECK)` (13); `* View all active storms in specified basins` (14); `* Command-line interface for easy integration` (15); `* Python client library for custom applications` (16). |
| 18–24 | Links / 라이선스·개발·연계 — GitHub 저장소를 연결한다(18–20). MIT 라이선스, 개발 기관 The Water Institute와 Floodwater 예측 시스템 연계를 적는다(22). 마지막 빈 줄과 공백 줄을 포함한다(23–24). 원문: `**Links:**` (18); `* GitHub Repository: https://github.com/waterinstitute/MetGet` (20); `MetGet is available under the MIT license and is developed by The Water Institute. It works in tandem with the Floodwater forecasting system.` (22). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

없음

