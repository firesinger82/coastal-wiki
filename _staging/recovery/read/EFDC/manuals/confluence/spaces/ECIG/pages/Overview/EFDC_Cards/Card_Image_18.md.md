---
file: models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_18.md
lines: 34
sha256: 9a82e3180b483dea7b998d3a8976a555f03eb54a0e9b91a1cab255781e6fabba
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Card_Image_18.md — 판독 구간 기록

구간은 1행부터 34행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | 문서 메타데이터(metadata) — 페이지 ID(2), 제목(3), space(4), 원문 URL(5), 버전(6), 갱신 시각(7), 문서 계층 경로(8)를 기록한다. `---` 구분자를 포함한다(1·9). |
| 10–23 | C18 PERIODIC FORCING (TIDAL) SURF ELEV OR PRESSURE ON SOUTH OPEN BOUNDARIES / 셀 위치·경계 옵션 — 남쪽 개방 경계(south open boundaries)의 주기 조석 강제력(periodic tidal forcing) 절 제목을 적는다(10). 경계 셀의 I·J 인덱스(index)를 설명한다(12–14). `ISPBS`의 0은 지정 수위(elevation specified), 1은 접선 속도(tangential velocity) 0인 방사·분리 조건(radiation-separation condition), 2는 자유 접선 속도의 방사·분리 조건, 3은 자유 접선 속도의 지정 수위이다(16–22). 매개변수·옵션 원문: `\* IPBS: I CELL INDEX OF BOUNDARY CELL` (12); `\* JPBS: J CELL INDEX OF BOUNDARY CELL` (14); `\* ISPBS: 0 FOR ELEVATION SPECIFIED` (16); `\*            1 FOR RADIATION-SEPARATION CONDITION, ZERO TANGENTIAL VELOCITY` (18); `\*            2 FOR RADIATION-SEPARATION CONDITION, FREE TANGENTIAL VELOCITY` (20); `\*            3 FOR ELEVATION SPECIFIED, FREE TANGENTIAL VELOCITY` (22). 빈 줄을 포함한다. |
| 24–33 | C18 / 적용 강제력·추가 시계열·접선 좌표 — 조화 강제력(harmonic forcing) 번호, 시계열(time series) 강제력 번호, `NPFORT.GE.1`에서의 두 번째 시계열 번호와 경계를 따른 접선 좌표(tangential coordinate)를 설명한다(24–30). 매개변수·조건 원문: `\* NPFORS: APPLY HARMONIC FORCING NUMBER NPFORS` (24); `\* NPSERS: APPLY TIME SERIES FORCING NUMBER NPSERS` (26); `\* NPSERS1: APPLY TIME SERIES FORCING NUMBER NPSERS1 FOR 2ND SERIES (NPFORT.GE.1)` (28); `\* TPCOORDS: TANGENTIAL COORDINATE ALONG BOUNDARY (NPFORT.GE.1)` (30). 주석용 `\*` 줄과 빈 줄을 포함한다(31–33). |
| 34–34 | C18 / 입력 헤더 — 다섯 필드의 헤더만 적는다. 입력 줄 원문: `C18 IPBS  JPBS  ISPBS  NPFORS  NPSERS` (34). 이 파일은 이 헤더에서 끝난다. |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 28·30·34행: 설명에 있는 `NPSERS1`과 `TPCOORDS`가 입력 헤더에는 없다.
- 34행: 입력 헤더 뒤에 수치 입력 예시가 없다.

