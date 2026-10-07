---
file: models/EFDC/raw/source_code/EFDC-GVC/csndzeq.for
lines: 74
sha256: 7cb74db2a2be8578bbfe6998066efbac4db05a6cbc8f1a2c7234ea4ea6b0b75b
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# csndzeq.for — 판독 구간 기록

구간은 1행부터 74행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–37 | 구분 주석과 `REAL FUNCTION CSNDZEQ(SNDDIA,GPDIASED,TAUR,TAUB,SNDDMX,DEP,` (6); `&    IOPT,SSG,WS)` (7) 선언. EFDC-FULL 1.0a·2001-11-01 수정 표기, 빈 변경 이력 양식(9–18), EFDC.PAR 포함(20). 바닥 부근 기준 농도(near-bed reference concentration)의 기준 높이(reference height) 계산 주석(22). SNDDIA=모래 입경, SSG=비중(specific gravity), WS=침강 속도(settling velocity), TAUR=물 밀도로 정규화한 임계 Shields 응력(critical Shields stress), TAUB=물 밀도로 정규화한 바닥 응력(bed stress), SIGPHI=phi 크기 표준편차(standard deviation), SNDDMX=D90 또는 최대 입경이라는 주석(24–31). 옵션 1은 Garcia·Parker 1991 문헌(33–36). |
| 38–53 | 시작 시 6–7행 CSNDZEQ 함수 안. `IF(IOPT.EQ.1)THEN` (38)에서 고정 반환값 `CSNDZEQ=0.05` (39). 옵션 2의 Smith·McLean 1977 문헌 주석(42–45). `IF(IOPT.EQ.2)THEN` (47)에서 `TMPVAL=26.3*SNDDMX*(TAUB-TAUR)/GPDIASED` (48); `TMPVAL=TMPVAL*SNDDIA/SNDDMX` (49); `TMPVAL=TMPVAL/DEP` (50); `CSNDZEQ=MAX(TMPVAL,0.01)` (51). 계산 높이를 DEP로 나눈 뒤 하한 0.01을 적용한다(50–51). ENDIF·주석(40–41·52–53). |
| 54–74 | 시작 시 6–7행 CSNDZEQ 함수 안. 옵션 3의 Van Rijn 1984 문헌(54–57). `IF(IOPT.EQ.3)THEN` (59)에서 `REY=1.E4*SNDDIA*( (9.8*(SSG-1.))**0.333 )` (60); `IF(REY.LE.10.) TAURS=(4.*WS/REY)**2` (61); `IF(REY.GT.10.) TAURS=0.016*WS*WS` (62); `VAL=(TAUB/TAURS)-1.` (63). 입력 TAUR 사용 대체식은 주석 `C        VAL=(TAUB/TAUR)-1.` (64). 이어 `VAL=MAX(VAL,0.)` (65); `VAL1=1.-EXP(-0.5*VAL)` (66); `VAL1=0.11*VAL1*(25.-VAL)` (67); `ZEQ1=0.5*VAL1*(DEP**0.7)*(SNDDMX**0.3)` (68); `ZEQ1=ZEQ1/DEP` (69); `CSNDZEQ=MAX(ZEQ1,0.01)` (70). VAL 하한은 0이며 결과 ZEQ1/DEP의 하한은 0.01이다. ENDIF·주석·RETURN·END(71–74). 호출문은 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 30·6–7: SIGPHI는 인수 설명 주석에 있지만 함수 인수 목록과 실행식에는 없다.
- 38–73: 반환값을 대입하는 경로는 IOPT=1..3이다. 다른 옵션에 대한 기본 반환값 대입은 없다.
- 48–51·60–70: 옵션 2는 GPDIASED/SNDDMX/DEP를 분모에 사용한다. 옵션 3은 REY/TAURS/DEP를 분모에 사용한다. 이 분기들에는 해당 분모가 0인지 검사하는 조건이 없다.
- 63–70: 옵션 3은 VAL을 0 이상으로 제한한다. 뒤의 VAL1 식에는 25.-VAL 인수가 있고 VAL의 상한 제한문은 없다. 최종 반환값에는 하한 0.01을 적용한다.

