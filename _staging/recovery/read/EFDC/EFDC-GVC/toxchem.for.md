---
file: models/EFDC/raw/source_code/EFDC-GVC/toxchem.for
lines: 325
sha256: d663011227d537b07ed72d3eda1ed74790f1284b5b7dc991ac197f7f868cc602
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# toxchem.for — 판독 구간 기록

구간은 1행부터 325행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–86 | 머리말과 `SUBROUTINE TOXCHEM` 입구(1–6). EFDC-FULL 1.0a·수정 이력 주석(8–16). 설명 주석은 CALSND의 비점착성 퇴적물(noncohesive sediment) 침강(settling)·퇴적(deposition)·재부유(resuspension)를 적는다(20–21). `INCLUDE 'EFDC.PAR'` (25), `INCLUDE 'EFDC.CMN'` (26). 옛 PMC 선언은 주석(28–31). SSEDTOX1/1A/2/3/4/5/6/7 COMMON 선언은 셀·수층·퇴적층 작업 배열과 시간 간격 DELT 등을 공유한다(33–72). Housatonic 옵션의 온도·풍속·확산·Henry 계수·대기 농도·휘발(volatilization) 작업 배열 COMMON, REAL 전달계수 및 VEL 선언(74–83). 포함 파일 내부는 이 기록의 판독 대상이 아니다. |
| 87–141 | 시작 시 6행 TOXCHEM 안. `IF(ISHOUSATONIC.EQ.0)THEN` (87), `IF(ISTRAN(5).GE.1)THEN` (88) 안 NT=1..NTOX 루프(89). 온도 보정 감쇠(decay)·휘발·광분해(photolysis) 설명과 식은 주석(93–108). K=1..KC·L=2..LA 루프(110–111)에서 `CDECAYW(L,K)=1./(1.+DELT*RKTOXW(NT))` (112). 같은 범위의 두 번째 루프(116–117)에서 `TOX(L,K,NT)=CDECAYW(L,K)*TOX(L,K,NT)` (118). K=1..KB·L=2..LA(122–123)에서 `CDECAYB(L,K)=1./(1.+DELT*RKTOXB(NT))` (124), 다음 같은 범위 루프(128–129)에서 `TOXB(L,K,NT)=CDECAYB(L,K)*TOXB(L,K,NT)` (130). NT 루프와 두 조건 종료(136–138), 구분 주석(139–141). |
| 142–180 | 시작 시 6행 TOXCHEM 안. `IF(ISHOUSATONIC.EQ.1)THEN` (142), `IF(ISTRAN(5).GE.1)THEN` (143)의 NT=1..NTOX 루프(144). 온도 보정식은 주석(148–153). WASP 5의 1990년 휘발 코드라는 주석(156–158). 고정 계수·조건은 `XLAM2 = 4.` (159), `CDRAG = 0.0011` (160), `HENRY(NT)=3.85E-4` (161), `RMOLTX(NT)=320.39` (162), `ATMOS=0.` (163), `W_TEMP=10.0 ! LT mean temp.` (164), `A_TEMP=10.0 ! LT mean temp.` (165), `SWIND=3.5756` (166), `KLT=1.024` (167). `DIFFA=1.9E-4*(RMOLTX(NT)**(-2./3.))` (168), `DIFFW=2.2E-8*(RMOLTX(NT)**(-2./3.))` (169). L=2..LA 루프(170)에서 `UTMP1=50.*(UHDYE(L+1)+UHDYE(L))/(DYP(L)*HP(L))` (171), `VTMP1=50.*(VHDXE(L)+VHDXE(L))/(DXP(L)*HP(L))` (172). `IF(SPB(L).EQ.0)THEN` (173)은 `UTMP1=2.*UTMP1` (174), `VTMP1=2.*VTMP1` (175). `UTMP=CUE(L)*UTMP1+CVE(L)*VTMP1` (177), `VTMP=CUN(L)*UTMP1+CVN(L)*VTMP1` (178), `VEL(L)=SQRT(UTMP*UTMP+VTMP*VTMP)/100.` (179). 유속(velocity) 루프 종료(180). |
| 181–215 | 시작 시 6행 TOXCHEM·142행 Housatonic 분기·143행 독성물질 분기·144행 NT 루프 안. 하천·호수의 계산값 중 최대 전달계수를 고른다는 주석(181–183). `KG=100.  ! (Gas transfer Coefficient for flowing systems, M/D` (186). L=2..LA 루프(187)에서 `STP20 = W_TEMP - 20.` (188), `KAW = HENRY(NT)/(8.206E-05*(W_TEMP + 273.15))` (189), `XX = SQRT (32./RMOLTX(NT))` (191). `IF (HP(L) .LT. 0.61) THEN` (193)은 Owens 식 `XKL = XX*5.349*(VEL(L)**.67)/(HP(L)**.85)` (194). `ELSE` (195)의 내부 조건은 `IF (VEL(L) .LT. 0.518 .OR. HP(L) .GT.` (197); `&                13.584*VEL(L)**2.9135) THEN` (198). 참이면 O'Connor–Dobbins 식 `XKL = SQRT (DIFFW*VEL(L)/HP(L))*86400.` (199). 내부 `ELSE` (200)는 Churchill 식 `XKL = XX*5.049*VEL(L)**.969/HP(L)**.673` (202). 두 조건 종료(203–204), `XKGH = KG * KAW` (205), `KL_RIV = (1./(1./(XKL+1.e-12) + 1./XKGH))*KLT**STP20` (207). 1.e-12가 없는 대체식과 디버깅 조건·출력은 주석(208–214). |
| 216–251 | 시작 시 6행 TOXCHEM·142/143행 두 분기·144행 NT 루프·187행 L 루프 안. 호수·저수지의 공기/물 밀도(density) 및 점성(viscosity) 계산 주석(216–218). `DENA = 0.001293/(1. + 0.00367*A_TEMP)` (220), `DENW = 1. - 8.8E-05*W_TEMP` (221), `XNUA = (1.32 + 0.009*A_TEMP)*10.0` (222), `XNUW = (10.**(1301./(998.333 + 8.1855*` (223); `&          STP20 + 0.00585*STP20**2) -` (224); `&          3.30233)/DENW)*1.E-04` (225). Schmidt 수(Schmidt number) 식은 `SCA = XNUA/DIFFA` (229), `SCW = XNUW/DIFFW` (230). O'Connor 식 `USTAR_VOL = SQRT (CDRAG)*SWIND` (239), `XKL = USTAR_VOL*SQRT (DENA/DENW)*` (240); `1            (.905/XLAM2)*(1./SCW)**.666 + 1.0E-9` (241), `XKG = USTAR_VOL*(.905/XLAM2)*((1./SCA)**.666) + 1.0E-9` (242), `XKGH = XKG*KAW` (243), `KL_LAKE_O = (1./(1./XKL + 1./XKGH))*KLT**STP20*86400.` (244). 0.905 관련 주석(237), 디버깅 조건·출력은 주석(246–250), 빈 줄(245·251). |
| 252–286 | 시작 시 6행 TOXCHEM·142/143행 두 분기·144행 NT 루프·187행 L 루프 안. Mackay 식 `USTAR_VOL = .01*SWIND*SQRT (6.1 + 0.63*SWIND)` (254). `IF (USTAR_VOL .GT. 0.3) XKL = USTAR_VOL*` (255); `1            0.00341*(1./SCW)**.5 + 1.E-06` (256). 별도 조건 `IF (USTAR_VOL .LE. 0.3) XKL = USTAR_VOL**2.2*` (257); `1               0.0144*(1./SCW)**.5 + 1.E-06` (258). `XKG = USTAR_VOL*.0462*(1./SCA)**.666 + 1.E-03` (259), `XKGH = XKG*KAW` (260), `KL_LAKE_M = 0.` (261). Mackay 전달계수의 합성식은 주석(262), 디버깅 블록도 주석(264–268). `KL=MAX(KL_LAKE_O,KL_LAKE_M,KL_RIV)` (271), `KLA = KL/HP(L)/86400.     ! KLA IN SECONDS**-1` (272), `VOLA_TXW(L) = KLA*((TOXFDFW(L,KC,NT)*TOX(L,KC,NT)) -` (274); `+           ATMOS/KAW)` (275). 주석의 암시적 갱신식(276–278) 대신 `TOX(L,KC,NT)=TOX(L,KC,NT)-(VOLA_TXW(L)*DELT)` (279)로 수면층 농도(concentration) 갱신. `IF(ISTOXALL.EQ.1.AND.NT.EQ.1)THEN` (281)이면 `ATOXVOL(L,1)=ATOXVOL(L,1)-DXYP(L)*HP(L)*(VOLA_TXW(L)*DELT)` (282). 조건·L 루프 종료(283·285). |
| 287–325 | 시작 시 6행 TOXCHEM·142/143행 두 분기·144행 NT 루프 안. 광분해 기준률·일사 변수 설명은 주석(287–290). K=1..KC·L=2..LA(292–293)에서 `CDECAYW(L,K)=1./(1.+DELT*RKTOXW(NT))` (294), 다음 같은 범위 루프(298–299)에서 `TOX(L,K,NT)=CDECAYW(L,K)*TOX(L,K,NT)` (300). K=1..KB·L=2..LA(304–305)에서 `CDECAYB(L,K)=1./(1.+DELT*RKTOXB(NT))` (306), 다음 같은 범위 루프(310–311)에서 `TOXB(L,K,NT)=CDECAYB(L,K)*TOXB(L,K,NT)` (312). NT 루프·두 조건 종료(318–320), 구분 주석·RETURN·END(321–325). 이 루틴에는 CALL 문이 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 6·20–21: 실제 루틴 이름은 TOXCHEM이다. 머리말 설명은 CALSND와 비점착성 퇴적물 침강·퇴적·재부유를 적는다.
- 159–167: Housatonic 경로는 매 NT 반복에서 Henry 계수·분자량·물/공기 온도·풍속·대기 농도·전달계수 보정값을 고정값으로 대입한다.
- 171–172: U 방향 보간에는 UHDYE(L+1)와 UHDYE(L)를 사용한다. V 방향 식에는 VHDXE(L)를 두 번 사용한다.
- 254–262·271: Mackay 경로는 XKL·XKG·XKGH를 계산한다. KL_LAKE_M은 0으로 대입한다. 비영 전달계수 합성식은 주석이다. MAX 입력에는 KL_LAKE_M이 남아 있다.
- 272–282: 수면층 휘발 농도 갱신과 누적 플럭스에는 HP(L)를 사용한다. 이 블록에는 DZC(KC) 계수와 TOX 음수 제한 조건이 없다.
- 97–108·152–153·287–312: 온도 보정과 광분해 기준 변수는 주석에 있다. 실행 감쇠식은 RKTOXW/RKTOXB를 사용하며 RKTOXP/SKTOXP를 사용하는 실행식은 없다.
- 87·142·137–138·319–320: ISHOUSATONIC=0과 ISHOUSATONIC=1을 별개 IF로 처리한다. 두 값 이외의 경로는 이 파일에 없다.
