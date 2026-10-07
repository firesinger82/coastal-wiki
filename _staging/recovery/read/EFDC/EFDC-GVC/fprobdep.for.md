---
file: models/EFDC/raw/source_code/EFDC-GVC/fprobdep.for
lines: 52
sha256: 8195532511be9a0b898b83107743fbc671e48ddf916a0694281b0d55557a35c7
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# fprobdep.for — 판독 구간 기록

구간은 1행부터 52행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–31 | 구분 주석과 `FUNCTION FPROBDEP(TAUD,TAUB)` 선언(1–6). 확률 적분(probability integral)으로 퇴적 확률(probability of deposition)을 계산한다는 주석(10–11). EFDC-FULL 1.0a·수정자·날짜·변경 이력 틀(13–24). IMPLICIT REAL*8 문은 주석 처리(26), `EFDC.PAR` 포함(28). 계산 전제는 TAUB>TAUD라는 주석(30). |
| 32–44 | 시작 시 6행 FPROBDEP 함수 안. `YVAL=2.04*LOG(0.25*((TAUB/TAUD)-1.)*EXP(1.27*TAUD))` (32). INEG=0 초기화(33). `IF(YVAL.LT.0.0)THEN` (34)이면 INEG=1(35), `YVAL=ABS(YVAL)` (36). 이 조건 밖에서 `XVAL=1.0/(1.0+0.3327*YVAL)` (38), `POLYX=XVAL*(0.4632-0.1202*XVAL+0.9373*XVAL*XVAL)` (39), `EXPY=-0.5*YVAL*YVAL` (40), `FUNY=0.3989*EXP(EXPY)` (41), `TMPVAL=1.0-FUNY*POLYX` (42). 부호 복원 조건과 식 `IF(INEG.EQ.1)TMPVAL=1.0-TMPVAL` (43), 반환식 `FPROBDEP=1.0-TMPVAL` (44). |
| 45–52 | 시작 시 6행 FPROBDEP 함수 안. 주석은 0.3989를 `1/SQRT(2*PI)`라고 적는다(46–47). 구분 주석·RETURN·END(49–52). 외부 루틴 CALL 문은 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 30–32: TAUB>TAUD라는 전제는 주석에 있다. TAUD 나눗셈과 LOG 계산 앞에는 TAUD 또는 로그 인수에 대한 실행 조건 검사가 없다.
