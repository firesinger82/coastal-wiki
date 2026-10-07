---
file: models/EFDC/raw/source_code/EFDC-GVC/wsmtsbin.for
lines: 71
sha256: ece3a4a4cee51ec9a43b87092b89c78eb6faa3098a8523ebef4c6fa597b88d08
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# wsmtsbin.for — 판독 구간 기록

구간은 1행부터 71행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–35 | `WSMTSBIN` 시작(6). 수정 날짜·버전·변경 기록 틀을 적는다(10–26). 퇴적물(sediment) 시계열(time-series)을 이진 파일(binary file)에 쓰며 ISMTSDT 시간 단계 동안 저서 플럭스(benthic flux)를 평균한다는 주석(28–29). `EFDC.PAR`·`EFDC.CMN`을 포함한다(33–34). 빈 줄을 포함한다(35). |
| 36–49 | 시작 시 6행 WSMTSBIN 루틴 안. ISSDBIN>0이고 MOD(ITNWQ,ISMTSDT)=0이면 출력한다(36–37). NREC4를 증가시키고 TIMEBF/NBFCNT로 평균 시각을 계산한다(38–39). 장치 2의 WQSDTS.BIN을 직접 접근(direct access)·비형식(unformatted)·RECL=MAXRECL4로 연다(40–41). 첫 레코드에서 기존 헤더를 읽고 NDUM·XDUM을 자기 대입한다(43–46). 첫 레코드의 출력 횟수·시각을 갱신하고 기존 XDT·IXDT·NPARM·NCELLS·NLAYERS를 다시 쓴다(47–48). NR6 레코드에 평균 시각을 쓴다(49). 원문 조건·계산식·반복·호출: `IF(ISSDBIN .GT. 0)THEN` (36), `IF( MOD(ITNWQ,ISMTSDT) .EQ. 0 )THEN` (37), `NREC4 = NREC4+1` (38), `TIMTMP = TIMEBF / FLOAT(NBFCNT)` (39), `NDUM=NDUM` (45), `XDUM=XDUM` (46). |
| 50–63 | 시작 시 6행 WSMTSBIN 루틴·36행 IF 참 분기·37행 IF 참 분기 안. 셀 LL=2..LA에서 여덟 저서 플럭스/상태 합을 NBFCNT로 나누어 제자리 평균한다(50–58). BFO2SUM·BFNH4SUM·BFNO3SUM·BFPO4SUM·BFSADSUM·BFCODSUM·BFSMTSUM·BFBSTSUM을 WRITE(2)로 쓴다(60–62). 셀 루프를 닫는다(63). 원문 조건·계산식·반복·호출: `DO LL=2,LA` (50), `BFO2SUM(LL)  = BFO2SUM(LL)  / FLOAT(NBFCNT)` (51), `BFNH4SUM(LL) = BFNH4SUM(LL) / FLOAT(NBFCNT)` (52), `BFNO3SUM(LL) = BFNO3SUM(LL) / FLOAT(NBFCNT)` (53), `BFPO4SUM(LL) = BFPO4SUM(LL) / FLOAT(NBFCNT)` (54), `BFSADSUM(LL) = BFSADSUM(LL) / FLOAT(NBFCNT)` (55), `BFCODSUM(LL) = BFCODSUM(LL) / FLOAT(NBFCNT)` (56), `BFSMTSUM(LL) = BFSMTSUM(LL) / FLOAT(NBFCNT)` (57), `BFBSTSUM(LL) = BFBSTSUM(LL) / FLOAT(NBFCNT)` (58). |
| 64–71 | 시작 시 6행 WSMTSBIN 루틴·36행 IF 참 분기·37행 IF 참 분기 안. INQUIRE의 NEXTREC로 NR6을 얻고 파일을 닫는다(64–65). `CALL WQZERO4`로 누적 배열을 초기화한다(66). 두 출력 조건을 닫고 RETURN·END로 끝낸다(67–71). 원문 조건·계산식·반복·호출: `CALL WQZERO4` (66). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 36–39: 출력 분기의 MOD는 ISMTSDT를 제수로 사용한다. 이 분기 앞에는 ISMTSDT>0 검사가 없다.
- 39·51–58: 평균 시각·누적 값의 분모는 NBFCNT이다. 이 식들 앞에는 NBFCNT>0 검사가 없다.
- 40–41·49·60–64: 파일은 ACCESS='DIRECT'로 연다. 시각 WRITE에는 REC=NR6이 있지만 셀 자료 WRITE(2)에는 REC 지정이 없다. 이어서 NEXTREC를 조회한다.
- 43–46: 첫 레코드 READ 목록에 XDUM이 두 번 있으며 다음 실행문은 NDUM=NDUM·XDUM=XDUM 자기 대입이다.
