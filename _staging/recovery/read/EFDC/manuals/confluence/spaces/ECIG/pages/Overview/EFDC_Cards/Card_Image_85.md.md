---
file: models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_85.md
lines: 20
sha256: aad4e3619de1a5ad7bc17166b3a262f1dd8b84f9146daffec76e5a3e49b7c247
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Card_Image_85.md — 판독 구간 기록

구간은 1행부터 20행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | 원문 메타데이터(frontmatter) — 문서 ID·제목·space·URL·버전·갱신 시각·계층 경로를 적는다(1–9). |
| 10–18 | C85 CONTROLS FOR WRITING TO TIME SERIES FILES — 시계열(time series) 파일의 시작·종료 시나리오(start-stop scenario) 번호와 시나리오별 종료·시작 쌍(stop-start pair) 수를 정의한다(10·14–16). 번호의 범위 문자열과 시나리오 이름은 원문 그대로 옮긴다(14–16). 주석 표식과 빈 줄을 포함한다(11–18). 원문: `C85 CONTROLS FOR WRITING TO TIME SERIES FILES` (10); `\* ITSSS: START-STOP SCENARIO NUMBER 1.GE.ISSS.LE.NTSSTSP` (14); `\* MTSSTSP: NUMBER OF STOP-START PAIRS FOR SCENARIO ISSS` (16). |
| 19–20 | C85 입력 열 제목 — 시나리오 번호와 쌍 수의 열 제목을 제시한다(20). 앞 빈 줄을 포함한다(19). 원문: `C85 ITSSS MTSSTSP` (20). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 14–16행: 정의 이름은 `ITSSS`지만 범위와 다음 설명의 시나리오 이름은 `ISSS`이다. `ISSS`와 `NTSSTSP`의 정의는 이 파일에 없다. 범위 문자열의 첫 비교는 `1.GE.ISSS`로 적는다.

