---
file: models/EFDC/raw/source_code/EFDC-GVC/setstvel.for
lines: 48
sha256: 6d46f4df3287a8dfd915447586082dac41c63d6f552a65d5246bd3210425f2da
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# setstvel.for — 판독 구간 기록

구간은 1행부터 48행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–23 | 머리말·FUNCTION SETSTVEL(D,SSG) 선언·버전·수정 이력(1–18), EFDC.PAR 포함(19), Van Rijn 식의 비점착성 퇴적물(noncohesive sediment) 침강(settling)·Shields 기준(Shields criterion) 주석(21–22)을 포함한다. |
| 24–44 | 시작 시 6행 SETSTVEL 함수 안. `      VISC=1.E-6` (24); `      GP=(SSG-1.)*9.82` (25); `      GPD=GP*D` (26); `      SQGPD=SQRT(GPD)` (27); `      RD=SQGPD*D/VISC` (28)로 점성계수(viscosity)·수중 중력 계수·RD를 계산한다. 침강속도(settling velocity)는 `      IF(D.LT.1.0E-4)THEN` (32)에서 `        WSET=SQGPD*RD/18.` (33), `      IF(D.GE.1.0E-4.AND.D.LT.1.E-3)THEN` (36)에서 `        TMP=SQRT(1.+0.01*RD*RD)-1.` (37); `        WSET=10.0*SQGPD*TMP/RD` (38), `      IF(D.GE.1.E-3)THEN` (41)에서 `        WSET=1.1*SQGPD` (42)를 사용한다. 세 조건은 독립 IF다. ENDIF·구분 주석을 포함한다. |
| 45–48 | 시작 시 6행 SETSTVEL 함수 안. WSET를 함수 반환값에 복사한다(45). 주석·RETURN·END를 포함한다(46–48). 다른 루틴 호출은 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 24–25: VISC는 1.E-6, 중력 상수는 9.82로 고정되어 있다.
- 27–28·36–38: GP*D의 제곱근을 조건 분기 전에 계산한다. 중간 입경 분기는 RD로 나눈다. 이 파일에는 SSG·D의 입력 범위 검사나 RD=0 검사가 없다.
