---
file: models/EFDC/raw/source_code/EFDC-GVC/wwqtso.for
lines: 115
sha256: 2163f7be1382b07c5f009275a5ace993e1fc28652eb2b8217efc9964794eecc7
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# wwqtso.for — 판독 구간 기록

구간은 1행부터 115행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–32 | 구분 주석 뒤 `SUBROUTINE WWQTSO` (5)로 루틴을 시작한다. 2001년 수정일, EFDC-FULL 1.0a, 빈 변경 이력 및 시계열(time series) 출력 목적을 적는다(9–27). 25행 WQCHLX 역수 문구는 주석이다. `INCLUDE 'EFDC.PAR'` (29); `INCLUDE 'EFDC.CMN'` (30)로 공통 선언을 포함한다. 포함 파일 내부는 이번 판독 대상에 포함하지 않았다. `TINDAY=TINDAY` (31)은 TINDAY 자기 대입이다. 구분 주석을 포함한다(32). |
| 33–41 | 시작 시 5행 WWQTSO 루틴 안. `OPEN(1,FILE='WQWCTS.OUT',STATUS='UNKNOWN',POSITION='APPEND')` (33)로 단위 1의 WQWCTS.OUT에 추가 기록을 준비한다. `IF(ISDYNSTP.EQ.0)THEN` (35) 참 분기의 출력 시간 식은 `TIMTMP=DT*FLOAT(N)+TCON*TBEGIN` (36); `TIMTMP=TIMTMP/TCTMSR  ` (37)이다. `ELSE` (38) 분기는 `TIMTMP=TIMESEC/TCTMSR  ` (39)으로 출력 시간을 구한다. 조건 종료와 구분 주석을 포함한다(34·40–41). |
| 42–56 | 시작 시 5행 WWQTSO 루틴 안. K=1 문구는 주석이다(42). `DO M=1,IWQTS` (43); `DO K=1,KC` (44)로 지정 출력 지점과 K층을 순회하고 LL=LWQTS(M)를 복사한다(45). `DO NW=1,NWQV` (46); `WQVO(LL,K,NW) = WQVO(LL,K,NW)*0.5` (47)로 1..NWQV의 WQVO를 반으로 덮어쓴다. 엽록소(chlorophyll) 합계와 조류별 변환식은 `CHLWQ = WQVO(LL,K,1)*WQCHLC + WQVO(LL,K,2)*WQCHLD` (49); `*      + WQVO(LL,K,3)*WQCHLG` (50); `CHLC = WQVO(LL,K,1)*WQCHLC` (51); `CHLD = WQVO(LL,K,2)*WQCHLD` (52); `CHLG = WQVO(LL,K,3)*WQCHLG` (54)이다. `C          CHLCD = CHLC + CHLD` (53)은 비실행 주석이다. 조류 합계와 총유기탄소(total organic carbon) 식은 `TBWQ = WQVO(LL,K,1)+WQVO(LL,K,2)+WQVO(LL,K,3)` (55); `TOCWQ = WQVO(LL,K,4)+WQVO(LL,K,5)+WQVO(LL,K,6) + TBWQ` (56)이다. NW 루프 종료를 포함한다(48). M·K 루프는 다음 구간에 이어진다. |
| 57–69 | 시작 시 5행 WWQTSO 루틴·43행 M 루프·44행 K 루프 안. `IF(IWQSRP.EQ.1)THEN` (57)일 때 산소 비음수 제한, 용존·입자 금속 및 인산염(phosphate)·가용 규소(available silica) 분배식을 `O2WQ = MAX(WQVO(LL,K,19), 0.0)` (58); `TAMDWQ = MIN( WQTAMDMX*EXP(-WQKDOTAM*O2WQ), WQVO(LL,K,20) )` (59); `TAMPWQ = WQVO(LL,K,20) - TAMDWQ` (60); `PO4DWQ = WQVO(LL,K,10) / (1.0 + WQKPO4P*TAMPWQ)` (61); `SADWQ = WQVO(LL,K,17) / (1.0 + WQKSAP*TAMPWQ)` (62)로 계산한다. `ELSE IF(IWQSRP.EQ.2)THEN` (63) 분기는 총퇴적물 SEDT를 사용하는 `PO4DWQ = WQVO(LL,K,10) / (1.0 + WQKPO4P*SEDT(LL,K))` (64); `SADWQ = WQVO(LL,K,17) / (1.0 + WQKSAP*SEDT(LL,K))` (65)이다. `ELSE` (66) 분기는 PO4DWQ와 SADWQ를 WQVO의 10·17번 항목에서 그대로 복사한다(67–68). 조건을 닫는다(69). |
| 70–82 | 시작 시 5행 WWQTSO 루틴·43행 M 루프·44행 K 루프 안. 인산염 비음수 제한 및 조류 인·탄소 비는 `XPO4DWQ = MAX(PO4DWQ,0.0)` (70); `APCWQ = 1.0 / (WQCP1PRM + WQCP2PRM*EXP(-WQCP3PRM*XPO4DWQ))` (71)이다. 총인(total phosphorus)과 총질소(total nitrogen) 식은 `TPWQ = WQVO(LL,K,7)+WQVO(LL,K,8)+WQVO(LL,K,9)+WQVO(LL,K,10)` (72); `*      + APCWQ*TBWQ` (73); `TNWQ = WQVO(LL,K,11)+WQVO(LL,K,12)+WQVO(LL,K,13)+WQVO(LL,K,14)` (74); `*      +WQVO(LL,K,15) + WQANCC*WQVO(LL,K,1)+WQANCD*WQVO(LL,K,2)` (75); `*      +WQANCG*WQVO(LL,K,3)` (76)이다. `IF(IWQSI.EQ.1)THEN` (77)일 때 총규소(total silica)를 `TSIWQ = WQVO(LL,K,16)+WQVO(LL,K,17) + WQASCD*WQVO(LL,K,2)` (78)로 계산하고, `ELSE` (79) 분기는 `TSIWQ = 0.0` (80)으로 둔다. 조건 종료와 구분 주석을 포함한다(81–82). |
| 83–97 | 시작 시 5행 WWQTSO 루틴·43행 M 루프·44행 K 루프 안. 5일 생화학적 산소요구량(five-day biochemical oxygen demand, BOD5) 추가 이력 주석 뒤 IZ=IWQZMAP(LL,K)를 복사한다(83–85). 탄소·조류 및 암모니아 항을 포함한 식은 `BOD5 = 2.67 * ( WQVO(LL,K,5)*(1.0-EXP(-5.0*WQKLC))` (86); `+           + WQVO(LL,K,6)*(1.0-EXP(-5.0*WQKDC(IZ)))` (87); `+           + WQVO(LL,K,18)*(1.0-EXP(-5.0*WQKCD(IZ)))` (88); `+           + WQVO(LL,K,1)*(1.0-EXP(-5.0*WQBMRC(IZ)))` (89); `+           + WQVO(LL,K,2)*(1.0-EXP(-5.0*WQBMRD(IZ)))` (90); `+           + WQVO(LL,K,3)*(1.0-EXP(-5.0*WQBMRG(IZ))) )` (91); `+           + 4.57 * WQVO(LL,K,14)*(1.0-EXP(-5.0*WQNITM))` (92)이다. BOD5=0.0 문구는 `C MRM          BOD5=0.0       ! JI, 10/2/97` (94)처럼 주석이다. TAM·TMP 제거, 규조류(diatoms)·녹조류(green algae) 및 남조류(cyanobacteria) 출력 변경 주석을 포함한다(95–97). |
| 98–115 | 시작 시 5행 WWQTSO 루틴·43행 M 루프·44행 K 루프 안. `WRITE(1,71) IL(LL),JL(LL),K,TIMTMP, CHLWQ,TOCWQ,WQVO(LL,K,6),` (98); `+      TPWQ, WQVO(LL,K,9), WQVO(LL,K,10), PO4DWQ, CHLC, TNWQ,` (99); `+      (WQVO(LL,K,NW),NW=13,15), TSIWQ, (WQVO(LL,K,NW),NW=16,17),` (100); `+      SADWQ, BOD5, WQVO(LL,K,19), CHLD, CHLG, WQVO(LL,K,NWQV)` (101)로 격자 I·J, K, 출력 시간, 엽록소·탄소·인·질소·규소·BOD5·산소·조류 및 NWQV 항목을 고정된 순서로 기록한다. 다른 과거 출력 목록은 주석이다(103–106). K·M 루프를 닫고 `CLOSE(1)` (110)로 단위 1을 닫는다(107–110). `71 FORMAT(3I5,F11.5, 1P, 21E11.3)` (112)은 정수 3개, 시간 및 1P를 적용한 지수 형식 21개를 지정한다. 구분 주석과 RETURN·END를 포함한다(102·109·111·113–115). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 31·35–39: TINDAY=TINDAY는 실행되는 자기 대입이다. 실제 출력 시간 TIMTMP의 식에는 TINDAY를 사용하지 않는다.
- 46–47: WQVO의 1..NWQV 항목을 직접 0.5배로 덮어쓴다. 이 루틴에는 반값 이전 값을 복구하는 대입이 없다.
- 59–65·71: 금속 분배식은 MIN을 사용한다. 인산염·가용 규소 분배식과 APCWQ 식에는 분모가 있다. 이 계산 블록에는 분모의 0 여부를 검사하는 조건이 없다.
- 98–101·112: 실행 WRITE는 고정된 출력 목록을 사용한다. 이 출력 블록에는 ISTRWQ 선택 조건이 없다. 실행 FORMAT은 1P와 21E11.3을 사용한다.
