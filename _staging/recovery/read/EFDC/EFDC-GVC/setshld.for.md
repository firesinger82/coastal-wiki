---
file: models/EFDC/raw/source_code/EFDC-GVC/setshld.for
lines: 54
sha256: 0ec4faa0a8bd528f183ad1ddfc01d60f659d7ebaba60b551e66b79b5334d2157
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# setshld.for — 판독 구간 기록

구간은 1행부터 54행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–21 | 머리말·SETSHLD(TSC,THETA,D,SSG,DSR,USC) 선언·수정 이력(1–16), EFDC.PAR 포함(17). 주석은 Van Rijn 식을 이용한 비점착성 퇴적물(noncohesive sediment)의 침강(settling)·Shields 기준(Shields criterion)을 적는다(19–20). 구분 주석도 포함한다. |
| 22–49 | 시작 시 6행 SETSHLD 루틴 안. `      VISC=1.E-6` (22); `      GP=(SSG-1.)*9.82` (23); `      TMP=GP/(VISC*VISC)` (24); `      DSR=D*(TMP**0.333333)` (25); `      GPD=GP*D` (26)로 점성계수(viscosity)·수중 중력 계수·입경 관련 무차원 값 DSR을 계산한다. Shields 계수 THETA의 독립 분기는 `      IF(DSR.LE.4.0)THEN` (30)에서 `        THETA=0.24/DSR` (31), `      IF(DSR.GT.4.0.AND.DSR.LE.10.0)THEN` (34)에서 `        THETA=0.14/(DSR**0.64)` (35), `      IF(DSR.GT.10.0.AND.DSR.LE.20.0)THEN` (38)에서 `        THETA=0.04/(DSR**0.1)` (39), `      IF(DSR.GT.20.0.AND.DSR.LE.150.0)THEN` (42)에서 `        THETA=0.013*(DSR**0.29)` (43), `      IF(DSR.GT.150.0)THEN` (46)에서 `        THETA=0.055` (47). 각 ENDIF·구분 주석을 포함한다. |
| 50–54 | 시작 시 6행 SETSHLD 루틴 안. `      TSC=GPD*THETA` (50); `      USC=SQRT(TSC)` (51)로 임계 전단 관련 값과 임계 마찰속도(friction velocity)를 계산한다. 주석·RETURN·END를 포함한다(52–54). 다른 루틴 호출은 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 22–25: VISC=1.E-6, 중력 상수 9.82, 세제곱근 지수 0.333333을 직접 사용한다.
- 30–31·50–51: DSR<=4.0 분기는 DSR로 나눈다. 반환 전 TSC의 제곱근을 계산한다. D·SSG·DSR의 범위를 검사하는 문장은 없다.
