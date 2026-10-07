---
file: models/EFDC/raw/source_code/EFDC-GVC/wqzero4.for
lines: 49
sha256: 5817224b8d8c3fb5b6bb70a62302db3b492914557758ce84f75651e376803565
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# wqzero4.for — 판독 구간 기록

구간은 1행부터 49행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–31 | `WQZERO4` 시작(6). 저서 플럭스(benthic flux) 배열을 0으로 초기화한다는 목적과 작성·수정 날짜·버전·변경 기록 틀을 적는다(10–27). `EFDC.PAR`·`EFDC.CMN`을 포함한다(29–30). |
| 32–44 | 시작 시 6행 WQZERO4 루틴 안. 셀 LL=2..LA 루프에서 BFO2SUM·BFNH4SUM·BFNO3SUM·BFPO4SUM·BFSADSUM·BFCODSUM·BFSMTSUM·BFBSTSUM의 여덟 누적 배열을 0으로 초기화한다(32–44). 층 루프는 없다. 원문 조건·계산식·반복·호출: `DO LL=2,LA` (32), `BFO2SUM(LL)  = 0.0` (36), `BFNH4SUM(LL) = 0.0` (37), `BFNO3SUM(LL) = 0.0` (38), `BFPO4SUM(LL) = 0.0` (39), `BFSADSUM(LL) = 0.0` (40), `BFCODSUM(LL) = 0.0` (41), `BFSMTSUM(LL) = 0.0` (42), `BFBSTSUM(LL) = 0.0` (43). |
| 45–49 | 시작 시 6행 WQZERO4 루틴 안. TIMEBF=0·NBFCNT=0으로 저서 플럭스의 시간 합과 횟수를 초기화한다(45–46). 빈 주석·RETURN·END를 포함한다(47–49). 원문 조건·계산식·반복·호출: `TIMEBF = 0.0` (45), `NBFCNT = 0` (46). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
