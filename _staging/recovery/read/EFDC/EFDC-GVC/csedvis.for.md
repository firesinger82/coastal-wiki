---
file: models/EFDC/raw/source_code/EFDC-GVC/csedvis.for
lines: 43
sha256: c6e7d092eb30c8727446c806d0913401cd79fe17132539960906bf10c8d20957
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# csedvis.for — 판독 구간 기록

구간은 1행부터 43행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–27 | 구분 주석과 `REAL FUNCTION CSEDVIS(SED)` (6) 선언. EFDC-FULL 1.0a·2001-11-01 수정 표기, 빈 변경 이력 양식(8–17), EFDC.PAR 포함(19). 고농도 응집성 퇴적물(cohesive sediment)·물 혼합물의 동점성계수(kinematic viscosity)를 계산한다는 주석(21–22). Mehta·Jiang 1990 문헌 표기(24–26). |
| 28–43 | 시작 시 6행 CSEDVIS 함수 안. 하부 구간 `IF(SED.LE.25667.) VISR=0.116883E-3*SED` (28), 상부 구간 `IF(SED.GE.36667.) VISR=1.52646E-6*SED+3.125` (30). 중간 구간 `IF(SED.GT.25667.0.AND.SED.LT.36667.0)THEN` (32) 안에서 `WTL=(36667.-SED)/11000.` (33); `WTH=(SED-25667.)/11000.` (34); `VISL=0.116883E-3*25667` (35); `VISH=1.52646E-6*36667.+3.125` (36); `VISR=WTL*VISL+WTH*VISH` (37)로 두 끝값을 선형 보간(linear interpolation)한다. SED=25667은 하부식, SED=36667은 상부식에 포함한다(28·30). 분기 종료 후 `CSEDVIS=1.E-6*(10.**VISR)` (40). 주석·RETURN·END(38–43). 호출문은 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 28–40: 농도 구간 경계 25667.·36667., 보간 분모 11000., 점도 변환 계수 1.E-6은 실행식에 직접 적힌 상수이다.

