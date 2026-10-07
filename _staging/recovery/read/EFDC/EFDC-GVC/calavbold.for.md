---
file: models/EFDC/raw/source_code/EFDC-GVC/calavbold.for
lines: 295
sha256: ff106ac7a81acc401ad78dc5c9572ce80ce98b0433e755de8fab0d4f31adecab
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# calavbold.for — 판독 구간 기록

구간은 1행부터 295행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–47 | 구분 주석과 `SUBROUTINE CALAVBOLD (ISTL)` (6) 입구. 수직 점성계수(vertical viscosity)·확산계수(diffusivity)를 Mellor–Yamada의 Galperin 수정으로 계산한다는 주석이다(8–11). H 정규화·ISGA 기하평균(geometric average) 설명을 포함한다(10–11). 버전·수정일·건조 셀(dry cell) 변경 이력을 포함한다(13–23). `INCLUDE 'EFDC.PAR'` (27); `INCLUDE 'EFDC.CMN'` (28)로 공통 선언을 포함한다. 29행 QQI 선언과 33–43행 계수표는 주석이다. 45행은 Galperin 안정도 함수(stability function) 주석이다. |
| 48–78 | 시작 시 6행 CALAVBOLD 루틴 안. 분기 없이 설정하는 계수·하한은 `SFAV0= 0.392010` (48); `SFAV1= 7.760050` (49); `SFAV2=34.676440` (50); `SFAV3= 6.127200` (51); `SFAB0= 0.493928` (52); `SFAB1=34.676440` (53); `RIQMIN=-0.999/SFAB1` (54). 공통 초기값은 `QQIMAX=1./QQMIN` (57); `AVMAX=AVO` (58); `ABMAX=ABO` (59); `AVMIN=10.` (60); `ABMIN=10.` (61); `RAVBTMP=1.` (65). 배경 계수 가산 여부는 `IF(ISAVBMN.GE.1) RAVBTMP=0.` (66). K=1..KC·L=1..LC(68–69)의 `IF(IMASKDRY(L).EQ.1)THEN` (70)에서 건조 초기화는 `AV(L,K)=AVO*HPI(L)` (71); `AB(L,K)=ABO*HPI(L)` (72). 62–64행 대체 RIQ 한계값은 주석이다. |
| 79–117 | 시작 시 6행 CALAVBOLD 루틴 안. `IF(ISFAVB.EQ.0)THEN` (80)에서 K=1..KS·L=2..LA(82–83), `IF(LMASKDRY(L))THEN` (84) 안의 QQ 역수는 `QQI(L)=1./QQ(L,K)` (86); `QQI(L)=MIN(QQI(L),QQIMAX)` (87). 다음 L 루프(90)의 `IF(LMASKDRY(L))THEN` (91)에서 `RIQ=-GP*HP(L)*DML(L,K)*DML(L,K)*DZIG(K)` (92); `&    *(B(L,K+1)-B(L,K))*QQI(L)` (93); `RIQ=MAX(RIQ,RIQMIN)` (94); `IF(ISLLIM.GE.1) RIQ=MIN(RIQ,RIQMAX)` (95)로 RIQ를 계산·제한한다. 96–100행 대체 안정도 식은 주석이다. 실행식은 `SFAV=SFAV0*(1.+SFAV1*RIQ)/((1.+SFAV2*RIQ)` (101); `&                *(1.+SFAV3*RIQ))` (102); `SFAB=SFAB0/(1.+SFAB1*RIQ)` (103). AB·AV·극값·정규화는 `AB(L,K)=AVCON*SFAB*DML(L,K)*HP(L)*SQRT(QQ(L,K))+RAVBTMP*ABO` (105); `AV(L,K)=AVCON*SFAV*DML(L,K)*HP(L)*SQRT(QQ(L,K))+RAVBTMP*AVO` (106); `AVMAX=MAX(AVMAX,AV(L,K))` (107); `ABMAX=MAX(ABMAX,AB(L,K))` (108); `AVMIN=MIN(AVMIN,AV(L,K))` (109); `ABMIN=MIN(ABMIN,AB(L,K))` (110); `AV(L,K)=AV(L,K)*HPI(L)` (111); `AB(L,K)=SCB(L)*AB(L,K)*HPI(L)` (112). 조건과 루프를 닫는다(113–117). 79행 ISTL 조건은 주석이다. |
| 118–155 | 시작 시 6행 CALAVBOLD 루틴 안. `IF(ISFAVB.EQ.1)THEN` (118)에서 K=1..KS·L=2..LA(120–121), `IF(LMASKDRY(L))THEN` (122) 안의 QQ 역수는 `QQI(L)=1./QQ(L,K)` (124); `QQI(L)=MIN(QQI(L),QQIMAX)` (125). 다음 L 루프(128)의 `IF(LMASKDRY(L))THEN` (129)에서 `RIQ=-GP*HP(L)*DML(L,K)*DML(L,K)*DZIG(K)` (130); `&    *(B(L,K+1)-B(L,K))*QQI(L)` (131); `RIQ=MAX(RIQ,RIQMIN)` (132); `IF(ISLLIM.GE.1) RIQ=MIN(RIQ,RIQMAX)` (133)로 RIQ를 계산·제한한다. 134–138행 대체 안정도 식은 주석이다. 실행식은 `SFAV=SFAV0*(1.+SFAV1*RIQ)/((1.+SFAV2*RIQ)` (139); `&                *(1.+SFAV3*RIQ))` (140); `SFAB=SFAB0/(1.+SFAB1*RIQ)` (141). 임시 확산·점성·극값은 `ABTMP=AVCON*SFAB*DML(L,K)*HP(L)*SQRT(QQ(L,K))+RAVBTMP*ABO` (143); `AVTMP=AVCON*SFAV*DML(L,K)*HP(L)*SQRT(QQ(L,K))+RAVBTMP*AVO` (144); `AVMAX=MAX(AVMAX,AVTMP)` (145); `ABMAX=MAX(ABMAX,ABTMP)` (146); `AVMIN=MIN(AVMIN,AVTMP)` (147); `ABMIN=MIN(ABMIN,ABTMP)` (148). 이전 값과 산술평균(arithmetic average)은 `AV(L,K)=0.5*(AV(L,K)+AVTMP*HPI(L))` (149); `AB(L,K)=SCB(L)*0.5*(AB(L,K)+ABTMP*HPI(L))` (150). 조건과 루프를 닫는다(151–155). |
| 156–193 | 시작 시 6행 CALAVBOLD 루틴 안. `IF(ISFAVB.EQ.2)THEN` (156)에서 K=1..KS·L=2..LA(158–159), `IF(LMASKDRY(L))THEN` (160) 안의 QQ 역수는 `QQI(L)=1./QQ(L,K)` (162); `QQI(L)=MIN(QQI(L),QQIMAX)` (163). 다음 L 루프(166)의 `IF(LMASKDRY(L))THEN` (167)에서 `RIQ=-GP*HP(L)*DML(L,K)*DML(L,K)*DZIG(K)` (168); `&    *(B(L,K+1)-B(L,K))*QQI(L)` (169); `RIQ=MAX(RIQ,RIQMIN)` (170); `IF(ISLLIM.GE.1) RIQ=MIN(RIQ,RIQMAX)` (171)로 RIQ를 계산·제한한다. 172–176행 대체 안정도 식은 주석이다. 실행식은 `SFAV=SFAV0*(1.+SFAV1*RIQ)/((1.+SFAV2*RIQ)` (177); `&                *(1.+SFAV3*RIQ))` (178); `SFAB=SFAB0/(1.+SFAB1*RIQ)` (179). 임시 확산·점성·극값은 `ABTMP=AVCON*SFAB*DML(L,K)*HP(L)*SQRT(QQ(L,K))+RAVBTMP*ABO` (181); `AVTMP=AVCON*SFAV*DML(L,K)*HP(L)*SQRT(QQ(L,K))+RAVBTMP*AVO` (182); `AVMAX=MAX(AVMAX,AVTMP)` (183); `ABMAX=MAX(ABMAX,ABTMP)` (184); `AVMIN=MIN(AVMIN,AVTMP)` (185); `ABMIN=MIN(ABMIN,ABTMP)` (186). 이전 값과 기하평균은 `AV(L,K)=SQRT(AV(L,K)*AVTMP*HPI(L))` (187); `AB(L,K)=SCB(L)*SQRT(AB(L,K)*ABTMP*HPI(L))` (188). 조건과 루프를 닫는다(189–193). |
| 194–226 | 시작 시 6행 CALAVBOLD 루틴 안. 194행 ENDIF와 196–223행 ISTL=2·ND/K/L 루프·대체 안정도·기하평균 경로는 전부 주석이다. 구분 주석을 포함한다(225–226). |
| 227–253 | 시작 시 6행 CALAVBOLD 루틴 안. `IF(ISAVBMN.GE.1)THEN` (227)에서 K=1..KS·L=2..LA(228–229)의 최소계수 적용은 `AVTMP=AVMN*HPI(L)` (230); `ABTMP=ABMN*HPI(L)` (231); `AV(L,K)=MAX(AV(L,K),AVTMP)` (232); `AB(L,K)=MAX(AB(L,K),ABTMP)` (233). 분기 밖 K=1..KS·L=2..LA(242–243), LS=LSC(L)(244)로 남쪽 이웃을 얻는다. 면 점성 역수는 `AVUI(L,K)=2./(AV(L,K)+AV(L-1,K))` (245); `AVVI(L,K)=2./(AV(L,K)+AV(LS,K))` (246). 252행 ISTL 조건은 주석이다. |
| 254–267 | 시작 시 6행 CALAVBOLD 루틴 안. K=2..KS·L=2..LA(254–255)의 난류 확산계수(turbulence diffusivity)는 `AQ(L,K)=0.205*(AV(L,K-1)+AV(L,K))` (257). L=2..LA(261)의 경계식은 `AQ(L,1)=0.205*AV(L,1)` (264); `AQ(L,KC)=0.205*AV(L,KS)` (265). 256·262–263행 0.255 식은 주석이다. 이 계산을 둘러싼 실행 IF는 없다. |
| 268–295 | 시작 시 6행 CALAVBOLD 루틴 안. 268–290행 ELSE·AQ 직접 대입 및 기하평균 대체 경로는 전부 주석이다. 구분 주석 뒤 RETURN·END로 종료한다(292–295). 실행 CALL 문은 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 48–54: 안정도 함수 계수와 RIQMIN은 매 호출 같은 값으로 설정된다. 이 파일에는 ISTOPT(0)에 따른 실행 선택 조건이 없다.
- 6·79·196·252: 인수 ISTL의 실행 참조는 없다. 해당 ISTL 조건은 모두 주석이다.
- 11·80·118·156: 평균 방식 주석은 ISGA를 사용하지만 실행 선택은 ISFAVB를 사용한다. 세 실행 조건에는 N=1에 대한 별도 조건이 없다.
- 86–87·124–125·162–163: QQI는 QQ 역수를 먼저 계산한 뒤 QQMIN 기반 상한을 적용한다. QQMIN을 분모에 더하는 식은 주석이다(85·123·161).
- 149–150·187–188: AB의 평균 결과에는 SCB(L)를 곱한다. AV의 평균 결과에는 SCB(L)를 곱하지 않는다.
- 227–266: 최소계수 적용·면 점성 역수·AQ 계산 루프에는 LMASKDRY 검사가 없다.
- 254–266: AQ는 AV 기반 0.205 식을 직접 대입한다. 해당 계산을 ISTL로 감싸는 조건은 주석 처리되어 있다(252).
