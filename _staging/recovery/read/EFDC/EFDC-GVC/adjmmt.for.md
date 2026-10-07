---
file: models/EFDC/raw/source_code/EFDC-GVC/adjmmt.for
lines: 459
sha256: 3d6c8b23255ffac7f75baf16328156e20ef25c303dd320ee82b492cf5616f8bb
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# adjmmt.for — 판독 구간 기록

구간은 1행부터 459행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–32 | 구분 주석(1–5), `SUBROUTINE ADJMMT` 입구(6). 주석은 EFDC-FULL VERSION 1.0a·2001년 11월 1일 수정 및 평균 질량 수송장(mean mass transport field) 조정을 적는다(8·10·19). `INCLUDE 'EFDC.PAR'` (23), `INCLUDE 'EFDC.CMN'` (24)로 외부 선언을 포함한다. 내부 모드(internal mode)·외부 모드(external mode)를 분리하고 시간 구간 중간으로 평균한다는 주석(28–29)과 빈 주석을 포함한다. 포함 파일 내부는 이 판독 범위에 없다. |
| 33–59 | 시작 시 6행 ADJMMT 루틴 안. `DO L=1,LC` (33)에서 `UHDY2E(L)=0.5*(UHDYE(L)+UHDY1E(L))` (34), `VHDX2E(L)=0.5*(VHDXE(L)+VHDX1E(L))` (35)을 계산한다. `DO K=1,KC` (38)·`DO L=1,LC` (39)에서 `UHDY2(L,K)=0.5*(UHDY(L,K)+UHDY1(L,K))-UHDY2E(L)` (40), `VHDX2(L,K)=0.5*(VHDX(L,K)+VHDX1(L,K))-VHDX2E(L)` (41)으로 외부 모드를 뺀다. `DO K=1,KS` (45)·`DO L=2,LA` (46)에서 LN=LNC(L)을 쓰고, `W2(L,K)=W2(L,K-1)-DZC(K)*DXYIP(L)*` (48); `&        (UHDY2(L+1,K)-UHDY2(L,K)+VHDX2(LN,K)-VHDX2(L,K))` (49)로 수직 성분을 누적한다. 외부 오일러 잔류 수송(Eulerian residual transport)의 발산(divergence) 계산·출력 주석(55–56)을 포함한다. |
| 60–100 | 시작 시 6행 ADJMMT 루틴 안. 표지 100(60), `RNTCMMT=FLOAT(NTSMMT)/FLOAT(NTSPTC)` (62). L=2..LA에서 `DIVERTE(L)=SPB(L)*( ((HLPF(L)-H1P(L))/(RNTCMMT*TIDALP))*DXYP(L)` (65); `&      -QSUMELPF(L)+UHDY2E(L+1)-UHDY2E(L)+VHDX2E(LN)-VHDX2E(L) )` (66)을 계산한다. DIVERTEG=0 초기화(69) 후 `DIVERTEG=DIVERTEG+DIVERTE(L)` (71), `FP(L)=-CC(L)*DIVERTE(L)` (72)을 계산한다. 극값 시작값은 `DIVMAX=-1.E-20` (77), `DIVMIN=1.E+20` (78)이다. `IF(DIVERTE(L).GT.DIVMAX)THEN` (80), `IF(DIVERTE(L).LT.DIVMIN)THEN` (85)에서 극값·격자 I/J를 저장한다. ITER=0(92)으로 시작 진단을 장치 6에 출력한다(93–95). 형식 6001–6003(97–99)과 주석을 포함한다. |
| 101–123 | 시작 시 6행 ADJMMT 루틴 안. 경계 조건(boundary condition)을 넣고 유출량(outflow)을 UHDY1E·VHDX1E에 저장한다는 주석(103). `OPEN(1,FILE='ADJMMT.DIA',STATUS='UNKNOWN')` (109), `CLOSE(1,STATUS='DELETE')` (110), 같은 OPEN(111)으로 진단 파일을 다시 만든다. QE·QW·QN·QS·QT·WTS·WTW·WTE·WTN·WTT를 0으로 초기화한다(113–122). |
| 124–162 | 시작 시 6행 ADJMMT 루틴 안. 동·서·북·남 경계 루프는 각각 `DO LL=1,NPBE` (124), `DO LL=1,NPBW` (131), `DO LL=1,NPBN` (138), `DO LL=1,NPBS` (145)이다. 각 경계 P를 0으로 설정한다(126·133·140·147). 합산식은 `QE=QE+UHDY2E(L)` (127), `WTE=WTE+ABS(UHDY2E(L))` (128), `QW=QW+UHDY2E(L+1)` (134), `WTW=WTW+ABS(UHDY2E(L+1))` (135), `QN=QN+VHDX2E(L)` (141), `WTN=WTN+ABS(VHDX2E(L))` (142), `QS=QS+VHDX2E(LN)` (149), `WTS=WTS+ABS(VHDX2E(LN))` (150)이다. 이어 `QE=ABS(QE)` (153), `QW=ABS(QW)` (154), `QN=ABS(QN)` (155), `QS=ABS(QS)` (156), `QT=1./(QE+QW+QS+QN)` (157)을 계산한다. 보정 계수는 `QE=QE*QT*DIVERTEG/WTE` (158), `QW=QW*QT*DIVERTEG/WTW` (159), `QN=QN*QT*DIVERTEG/WTN` (160), `QS=QS*QT*DIVERTEG/WTS` (161)이다. |
| 163–200 | 시작 시 6행 ADJMMT 루틴 안. 동쪽 루프(163–170)는 `FP(L-1)=FP(L-1)+QE*ABS(UHDY2E(L))*CC(L-1)` (166), `UHDY1E(L)=UHDY2E(L)-QE*ABS(UHDY2E(L))` (167)을 계산한다. 서쪽 루프(172–179)는 `FP(L+1)=FP(L+1)+QW*ABS(UHDY2E(L+1))*CC(L+1)` (175), `UHDY1E(L+1)=UHDY2E(L+1)+QW*ABS(UHDY2E(L+1))` (176)을 계산한다. 북쪽 루프(181–189)는 LS=LSC(L), `FP(LS)=FP(LS)+QN*ABS(VHDX2E(L))*CC(LS)` (185), `VHDX1E(L)=VHDX2E(L)-QN*ABS(VHDX2E(L))` (186)을 사용한다. 남쪽 루프(191–199)는 LN=LNC(L), `FP(LN)=FP(LN)+QS*ABS(VHDX2E(LN))*CC(LN)` (195), `VHDX1E(LN)=VHDX2E(LN)+QS*ABS(VHDX2E(LN))` (196)을 사용한다. 각 루프는 보정식 전후에 원래 UHDY2E 또는 VHDX2E를 진단 파일에 출력한다(165·168·174·177·184·187·194·197). |
| 201–239 | 시작 시 6행 ADJMMT 루틴 안. FPSUM=0(203), L=2..LA에서 `FPSUM=FPSUM+FP(L)` (207)을 누적한다. I/J·CC/CS/CW/CE/CN·FP·QSUMELPF와 FPSUM을 출력하고 파일을 닫는다(204–214). 출력 형식 1110–1150(216–224). 유한차분(finite difference) 퍼텐셜(potential) 방정식의 주석은 `CS(L)*P(LS)+CW(L)*P(L-1)` (230), `+P(L)+CE(L)*P(L+1)` (231), `+CN(L)*P(LN) = FP(L)` (232)이다. 적흑 순서(red-black ordering)의 연속 과완화(successive over relaxation)를 사용하며 제곱오차로 수렴을 판단한다는 주석(234–236)을 포함한다. 이 주석의 이름은 RSQADJ·ITMADJ이다. |
| 240–272 | 시작 시 6행 ADJMMT 루틴 안. ITER=1(240), 표지 200(242), RSQE=0(243). `DO LL=1,NRC` (249)는 LRC의 적색 셀을 사용한다. `RSDE=CS(L)*P(LS)+CW(L)*P(L-1)+P(L)` (253); `&       +CE(L)*P(L+1)+CN(L)*P(LN)-FP(L)` (254), `P(L)=P(L)-RPADJ*RSDE` (255), `RSQE=RSQE+RSDE*RSDE` (256)을 계산한다. `DO LL=1,NBC` (263)는 LBC의 흑색 셀을 사용한다. 해당 식은 `RSDE=CS(L)*P(LS)+CW(L)*P(L-1)+P(L)` (267); `&       +CE(L)*P(L+1)+CN(L)*P(LN)-FP(L)` (268), `P(L)=P(L)-RPADJ*RSDE` (269), `RSQE=RSQE+RSDE*RSDE` (270)이다. 두 루프는 LN·LS를 LNC·LSC에서 가져온다. |
| 273–320 | 시작 시 6행 ADJMMT 루틴 안. `IF(RSQE.LE.RSQMADJ) GOTO 800` (277)은 수렴 조건이다. `IF(ITER .GE. ITRMADJ) GOTO 800` (283)은 반복 횟수 종료 조건이다. 284–314행은 주석 처리된 대안 블록이다. 그 주석의 조건은 `C     IF(ITER .GE. ITRMADJ)THEN` (284)이다. 주석의 외부 수송 보정은 `C     UHDY2E(L)=UHDY2E(L)+HRU(L)*(P(L)-P(L-1))` (288), `C     VHDX2E(L)=VHDX2E(L)+HRV(L)*(P(L)-P(LS))` (289)이며, 경계값 복사 후 `C     GOTO 100` (313)을 적는다. 활성 실행문은 `ITER=ITER+1` (316), `GOTO 200` (317)이다. 구분 주석까지 포함한다(318–320). |
| 321–353 | 시작 시 6행 ADJMMT 루틴 안. 외부 오일러 잔류 수송 보정 주석·표지 800(321–325). L=2..LA에서 `UHDY2E(L)=UHDY2E(L)+HRU(L)*(P(L)-P(L-1))` (329), `VHDX2E(L)=VHDX2E(L)+HRV(L)*(P(L)-P(LS))` (330)을 계산한다. 동·서·북·남 경계 루프(333·338·343·348)는 UHDY1E·VHDX1E에 저장한 보정 경계값을 UHDY2E·VHDX2E로 복사한다(335·340·345·351). |
| 354–376 | 시작 시 6행 ADJMMT 루틴 안. K=1..KC·L=1..LC에서 `UHDY2(L,K)=UHDY2(L,K)+UHDY2E(L)` (356), `VHDX2(L,K)=VHDX2(L,K)+VHDX2E(L)` (357)을 계산한다. 속도는 `U2(L,K)=UHDY2(L,K)/(HMU(L)*DYU(L))` (358), `V2(L,K)=VHDX2(L,K)/(HMV(L)*DXV(L))` (359)이다. `RNTCMMT=FLOAT(NTSMMT)/FLOAT(NTSPTC)` (365), L=2..LA에서 `DIVERTE(L)=SPB(L)*( ((HLPF(L)-H1P(L))/(RNTCMMT*TIDALP))*DXYP(L)` (368); `&      -QSUMELPF(L)+UHDY2E(L+1)-UHDY2E(L)+VHDX2E(LN)-VHDX2E(L) )` (369)로 보정 후 발산을 다시 계산한다. DIVERTEG=0(372), `DIVERTEG=DIVERTEG+DIVERTE(L)` (374)로 전체 값을 누적한다. |
| 377–402 | 시작 시 6행 ADJMMT 루틴 안. `DIVMAX=-1.E-20` (377), `DIVMIN=1.E+20` (378). L=2..LA에서 `IF(DIVERTE(L).GT.DIVMAX)THEN` (380), `IF(DIVERTE(L).LT.DIVMIN)THEN` (385)으로 극값·격자 번호를 저장한다. ITER·전체 발산·극값을 장치 6에 출력한다(392–394). 벡터 퍼텐셜 수송(vector potential transport)·라그랑주 잔류 수송(Lagrangian residual transport) 계산 주석(398–399)과 구분 주석까지 포함한다. |
| 403–425 | 시작 시 6행 ADJMMT 루틴 안. K=1..KC·L=2..LA에서 LS·LN을 설정한다(403–406). HMC를 곱하는 대안 식은 주석 처리되어 있다(407–410). 활성 식은 `UVPT(L,K)=(VPZ(LN,K)-VPZ(L,K))/DYU(L)` (411); `&          -DZIC(K)*(VPY(L,K)-VPY(L,K-1))` (412), `VVPT(L,K)=DZIC(K)*(VPX(L,K)-VPX(L,K-1))` (413); `&          -(VPZ(L+1,K)-VPZ(L,K))/DXV(L)` (414)이다. K=1..KS·L=2..LA에서 `WVPT(L,K)=(VPY(L+1,K)-VPY(L,K))/DXP(L)-(VPX(LN,K)-VPX(L,K))/DYP(L)` (422)을 계산한다. |
| 426–459 | 시작 시 6행 ADJMMT 루틴 안. K=1..KC·L=1..LC에서 `UHLPF(L,K)=UHDY2(L,K)/DYU(L)` (428), `VHLPF(L,K)=VHDX2(L,K)/DXV(L)` (429)을 저장한다. 같은 범위에서 `UHDY2(L,K)=UHDY2(L,K)+UVPT(L,K)*DYU(L)` (435), `VHDX2(L,K)=VHDX2(L,K)+VVPT(L,K)*DXV(L)` (436)을 더한다. K=1..KS·L=1..LC에서 `W2(L,K)=W2(L,K)+WVPT(L,K)` (442), W=W2 복사(443). K=1..KC·L=1..LC에서 `U2(L,K)=UHDY2(L,K)/(HMU(L)*DYU(L))` (449), `V2(L,K)=VHDX2(L,K)/(HMU(L)*DXV(L))` (450)을 계산하고 U·V로 복사한다(451–452). 구분 주석·RETURN·END(455–459). 다른 루틴 호출은 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 45–49: W2의 수직 누적은 K=1에서 W2(L,0)을 읽는다. 이 루틴에는 W2(L,0)을 초기화하는 대입문이 없다.
- 157–161: QT는 네 경계 총량의 합으로 나눈다. QE·QW·QN·QS의 보정식은 각각 WTE·WTW·WTN·WTS로 나눈다. 이 식들 앞에는 분모가 0인지 검사하는 조건이 없다.
- 165–168·174–177·184–187·194–197: 경계 보정식 전후의 두 진단 출력은 UHDY2E 또는 VHDX2E를 출력한다. 사이의 보정 대입은 UHDY1E 또는 VHDX1E에 수행한다.
- 126·133·140·147·253–270: P의 0 대입은 경계 루프에 있다. 적색·흑색 셀 계산은 기존 P를 읽으며, 해당 셀 전체를 초기화하는 대입은 이 루틴에 없다.
- 235–236·277·283: 설명 주석의 수렴·반복 제한 이름은 RSQADJ·ITMADJ이다. 활성 조건문의 이름은 RSQMADJ·ITRMADJ이다.
- 277·283–325: 수렴 조건과 반복 제한 조건은 모두 표지 800으로 이동한다. 반복 제한을 별도로 출력하거나 중단하는 활성 문장은 이 블록에 없다.
- 403–424·433–445: UVPT·VVPT·WVPT를 계산하는 L 범위는 2..LA이다. 이 값을 수송장에 더하는 L 범위는 1..LC이다. 이 파일에는 나머지 L 위치를 초기화하는 문장이 없다.
- 359·450: 첫 V2 계산의 분모는 HMV(L)*DXV(L)이다. 마지막 V2 계산의 분모는 HMU(L)*DXV(L)이다.
