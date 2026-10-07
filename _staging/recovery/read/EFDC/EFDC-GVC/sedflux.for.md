---
file: models/EFDC/raw/source_code/EFDC-GVC/sedflux.for
lines: 79
sha256: 1b41e229ec786034706c1fa20e5268434859263579fb9727e208e9e1a34aec15
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# sedflux.for — 판독 구간 기록

구간은 1행부터 79행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–23 | 구분 주석과 `FUNCTION SEDFLUX(SMSOD1)` 선언(1–8). NH4·NO3·H2S/CH4 질량 수지(mass balance)와 플럭스(flux)를 푼다는 주석(10). COMMON/BPMNNHC/에 농도·계수·플럭스·산소 요구량 변수를 둔다(14–20). `RSMSS = SMSOD1 / (SMO20+ 1.E-18)` (22)로 교환 관련 값을 계산한다. 빈 줄·주석도 포함한다. |
| 24–43 | 시작 시 6행 SEDFLUX 함수 안. NH4 계산은 `RRNH4 = SK1NH4SM/(RSMSS+ 1.E-18)` (26), `A11NH4 = RSMSS*SMFD1NH4 + A1NH4SM + RRNH4` (27), `B11NH4 = RSMSS*B1NH4SM` (28)이다. B22NH4를 복사하고 `CALL SOLVSMBE(RSM1NH4,RSM2NH4,A11NH4,A22NH4SM,A1NH4SM,A2NH4SM,` (30), 연속행 `     *  B11NH4,B22NH4)` (31)을 호출한다. `RJNITSM = RRNH4 * RSM1NH4` (32)로 질산화(nitrification)를 계산한다. NO3 계산은 `RRNO3 = SK1NO3SM/(RSMSS+ 1.E-18)` (36), `A11NO3 = RSMSS + A1NO3SM + RRNO3` (37), `B11NO3 = RJNITSM + RSMSS*B1NO3SM` (38)이다. B22NO3 복사 뒤 `CALL SOLVSMBE(RSM1NO3,RSM2NO3,A11NO3,A22NO3SM,A1NO3SM,A2NO3SM,` (40), `     *  B11NO3,B22NO3)` (41)을 호출한다. `RJDENSM = RRNO3*RSM1NO3 + RK2NO3SM*RSM2NO3` (42)로 탈질(denitrification)을 계산한다. |
| 44–59 | 시작 시 6행 SEDFLUX 함수 안. H2S/CH4 주석(44–45) 뒤 `SMJ2H2S = MAX(SMO2JC - SMO2NO3*RJDENSM, 0.0)` (46)로 요구량을 0 이상으로 제한한다. `IF(SMSAL0.GT.SMCSHSCH)THEN` (47)의 참 분기는 `RRH2S = SK1H2SSM/(RSMSS+ 1.E-18)` (48), `SMTT1 = RSMSS*SMFD1H2S` (49), `A11H2S = SMTT1 + A1H2SSM + RRH2S` (50), `B22H2S = B2H2SSM + SMJ2H2S` (52)이다. B11H2S 복사(51)와 `CALL SOLVSMBE(RSM1H2S,RSM2H2S,A11H2S,A22H2SSM,A1H2SSM,A2H2SSM,` (53), `     *    B11H2S,B22H2S)` (54) 호출 뒤 `AQJH2SSM = SMTT1*RSM1H2S` (55), `CSODSM = RRH2S*RSM1H2S` (56)을 계산한다. CH4 수중·기체 플럭스는 0으로 둔다(57–58). `ELSE` (59)는 다음 구간으로 이어진다. |
| 60–72 | 시작 시 6행 SEDFLUX 함수·47행 염분 조건의 59행 ELSE 안. `CSODMSM = MIN( SQRT(SMCH4S*SMJ2H2S), SMJ2H2S )` (60), `SMTT2 = SMK1CH4 / (RSMSS+ 1.E-18)` (61)을 계산한다. `IF(SMTT2.LT.80.0)THEN` (62)이면 `SMTT3 = EXP(SMTT2)` (63), `SMSECH = 2.0 / (SMTT3 + 1.0/SMTT3)` (64)이다. `ELSE` (65)는 SMSECH=0(66)이다. 내부 분기 뒤 `AQJCH4SM = CSODMSM*SMSECH` (68), `CSODSM = CSODMSM - AQJCH4SM` (69), `GJCH4SM = SMJ2H2S - CSODMSM` (70)을 계산하고 AQJH2SSM=0(71)으로 둔다. 염분 분기를 닫는다(72). |
| 73–79 | 시작 시 6행 SEDFLUX 함수 안이며 염분 분기 밖. `RNSODSM = SMO2NH4*RJNITSM` (74), `SMSOD = CSODSM + RNSODSM` (75), `SEDFLUX = SMSOD - SMSOD1` (76)로 총 저질 산소 요구량(sediment oxygen demand)의 입력값 대비 잔차를 반환한다. 주석·RETURN·END를 포함한다(73·77–79). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 22·26·36·48·61: 분모 보정 상수는 1.E-18로 고정되어 있다.
- 62–66: SMTT2가 80.0 이상이면 지수함수를 계산하지 않고 SMSECH를 0으로 둔다.
- 47–72: H2S 참 분기는 RSM1H2S·RSM2H2S를 SOLVSMBE에 전달한다. ELSE 분기에는 두 COMMON 변수의 대입이나 SOLVSMBE 호출이 없다.
