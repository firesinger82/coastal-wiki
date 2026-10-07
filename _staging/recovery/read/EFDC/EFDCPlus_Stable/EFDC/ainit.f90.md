---
file: models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/ainit.f90
lines: 386
sha256: db9a6a02f9285b335144ba45c70f7da43bb34ae034108dcf8ee2736721ca7082
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# ainit.f90 — 판독 구간 기록

구간은 1행부터 386행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–25 | EFDC+ 안내·웹사이트·저장소 주소·2021–2024 DSI 저작권·GNU GPLv2 머리말(1–8). `SUBROUTINE AINIT` 시작(9). 배열의 0 설정을 VARZEROINT·VARZEROREAL로 옮겼다는 변경 주석(11–13). GLOBAL·Variables_WQ·Variables_MPI와 turbulence의 eps_min·k_min을 가져온다(15–19). implicit none과 지역 정수를 선언한다(21–24). |
| 26–76 | 시작 시 9행 AINIT 루틴 안. 끝 인덱스 1·LC의 ZBR/ZBRE는 ZBRADJ, HMP/HMU/HMV/HWQ/H2WQ는 HMIN, DXP/DXU/DXV는 DX, DYP/DYU/DYV는 DY, MVEGL은 1로 초기화한다(27–59). 격자 면적(grid cell area) 식은 `DXYP(1) = DX*DY` (40), `DXYP(LC) = DX*DY` (57). BELV(1)은 BELV(2), BELV(LC)는 BELV(LA)에서 복사하고 BELV0에 전체 BELV를 복사한다(42·59–60). `if( ISGWIE == 0 ) DAGWZ = 0.` (62). `do L = 2,LA` (63)에서 I/J를 IL/JL에서 복사하고 KBT=1, `BELAGW(L) = BELV(L) - DAGWZ` (67), ZBRE=ZBR로 설정한다. 좌표 변환 계수(coordinate transformation coefficient) CUE/CVN=1, CVE/CUN=0으로 설정한다(69–72). KBT(1)·KBT(LC)=1(74–75). |
| 77–96 | 시작 시 9행 AINIT 루틴 안. 첫 `do L = 2,LA` (77)에서 서쪽·남쪽 인덱스를 LWC·LSC에서 얻는다(78–79). `DXU(L) = 0.5*(DXP(L)+DXP(LW))` (80), `DYU(L) = 0.5*(DYP(L)+DYP(LW))` (81), `DXV(L) = 0.5*(DXP(L)+DXP(LS))` (82), `DYV(L) = 0.5*(DYP(L)+DYP(LS))` (83). 두 번째 `do L = 2,LA` (86)에서는 `HMU(L) = 0.5*(DXP(L)*DYP(L)*HMP(L)+DXP(LW)*DYP(LW)*HMP(LW))/(DXU(L)*DYU(L))` (89), `HMV(L) = 0.5*(DXP(L)*DYP(L)*HMP(L)+DXP(LS)*DYP(LS)*HMP(LS))/(DXV(L)*DYV(L))` (90)로 면 수심(face depth)을 계산한다. HMU/HMV의 인덱스 1은 2에서, LC는 LA에서 복사한다(93–96). |
| 97–137 | 시작 시 9행 AINIT 루틴 안. `do L = 1,LC` (97)에서 CC/CCC=1. `P(L) = G*(HMP(L)+BELV(L))` (100), `P1(L) = G*(HMP(L)+BELV(L))` (101). HP/HU/HV와 HWQ/H1P/H1U/H1V/H2WQ를 HMP/HMU/HMV에서 복사한다(102–104·108–111·114). 역수 식은 `HPI(L) = 1./HP(L)` (105), `HUI(L) = 1./HU(L)` (106), `HVI(L) = 1./HV(L)` (107), `H1UI(L) = 1./H1U(L)` (112), `H1VI(L) = 1./H1V(L)` (113). SCB/SPB/SUB/SVB/SWB, STCUV/STCAP/STBX/STBY, SAAX/SAAY/SCAX/SCAY/SBX/SBY/SDX/SDY=1, LMASKDRY=.TRUE.(115–132). 루프 뒤 LOPENBCDRY=.FALSE.와 RADKE=SWRATNF를 설정한다(135–136). |
| 138–175 | 시작 시 9행 AINIT 루틴 안. 개방 수역(open water) 기본 설정에서 `if( ISVEG > 0 )then` (139)이면 NV=0, `PVEGZ(NV)  = 1.` (141). 144–175행은 전체가 주석이다. 비실행 조건 `!      if( IS1DCHAN == 1 )then` (144)과 LC까지의 반복문 및 FAD/WPD/DADH 계열 1, SRF 계열 0 설정이 남아 있다(145–175). |
| 176–210 | 시작 시 9행 AINIT 루틴 안. `do K = 1,KS` (176)·`do L = 1,LC` (177)에서 AV=AVO, AB=ABO, QQL/QQL1/QQL2=QQLMIN, DML=DMLMIN(178·181–185). `AVVI(L,K) = 1./AVO` (179), `AVUI(L,K) = 1./AVO` (180). 별도 `do K = 1,KC` (189)·`do L = 1,LC` (190)에서 AH/AHC=AHO, AQ=AVO, CTURBB1=CTURB, CTURBB2=CTURB2B, TEM/TEM1=TEMO로 초기화한다(191–199). `if( ISWQFLUX == 1 )then` (202)이면 K=1..KC·L=1..LC에서 AHULPF/AHVLPF=AHO(203–208). |
| 211–242 | 시작 시 9행 AINIT 루틴 안. 점착성 퇴적물(cohesive sediment) 반복 수는 `NTMPC = max(NSED,1)` (211). NS=1..NTMPC·K=1..KC·L=1..LC에서 SED/SED1=SEDO(NS)(212–220). 비점착성 퇴적물(noncohesive sediment) 반복 수는 `NTMPN = max(NSND,1)` (222). NX=1..NTMPN에서 `NS = NX+NTMPC` (224), K=1..KC·L=1..LC의 SND/SND1=SEDO(NS)(223–232). NT=1..NTOX·K=1..KC·L=1..LC에서 TOX/TOX1=TOXINTW(NT)(233–241). |
| 243–258 | 시작 시 9행 AINIT 루틴 안. `do K = 0,KC` (243)·`do L = 1,LC` (244)에서 QQ/QQ1/QQ2=QQMIN(246–248), `QQSQR(L,K) = SQRT(QQMIN)` (249). 두 루프 안에서 `if( ISGOTM > 0 )then` (250)이면 난류 운동에너지(turbulent kinetic energy) TKE3D/TKE3D1=k_min, 소산율(dissipation rate) EPS3D/EPS3D1=eps_min으로 설정한다(251–254). 조건과 두 루프를 닫는다(255–257). |
| 259–290 | 시작 시 9행 AINIT 루틴 안. `if( MDCHH >= 1 )then` (259), `do NMD = 1,MDCHH` (260)에서 LHOST/LCHNU/LCHNV를 대응 배열에서 복사한다(261–263). `if( PMDCH(NMD) < 0.0) PMDCH(NMD) = HWET` (267). `if( MDCHTYP(NMD) == 1 )then` (271)의 X방향 수로(channel)는 `if( CHANLEN(NMD) < 0.0 )then` (272)이면 `CHANLEN(NMD) = 0.25*DYP(LHOST)` (273), `else` (274)이면 `CHANLEN(NMD) = CHANLEN(NMD)-0.5*DYP(LCHNU)` (275). 별도 `if( MDCHTYP(NMD) == 2 )then` (281)의 Y방향 수로는 `if( CHANLEN(NMD) < 0.0 )then` (282)이면 `CHANLEN(NMD) = 0.25*DXP(LHOST)` (283), `else` (284)이면 `CHANLEN(NMD) = CHANLEN(NMD)-0.5*DXP(LCHNV)` (285). 조건·루프를 닫는다(286–289). |
| 291–315 | 시작 시 9행 AINIT 루틴 안. 퇴적물·독성물질의 유기탄소(organic carbon) 초기화 주석(291). IVAL=0에서 NT=1..NTOX를 반복하고 `if( ISTOC(NT) > 0 ) IVAL = 1` (294). `if( IVAL == 0 .and. ISTRAN(5) > 0 )then` (297)이면 Kd 접근만 사용하는 모델이라는 주석(298). NS=1..NSED+NSND·K=1..KB·L=1..LC에서 `STFPOCB(L,K,NS) = 1.0` (302). 같은 조건의 별도 NS·K=1..KC·L 루프에서는 `STFPOCW(L,K,NS) = 1.0` (310). |
| 316–345 | 시작 시 9행 AINIT 루틴 안. `if( IVAL == 1 .and. ISTRAN(5) > 0 )then` (316)은 fPOC·POC·DOC 사용 시 초기화한다는 주석을 둔다(317). `if( ISTDOCB == 0 )then  !   ISTDOCB == 1 STDOCB IS INITIALIZED FROM DOCB.INP` (320)이면 K=1..KB·L=1..LC의 STDOCB=STDOCBC(321–325). `if( ISTPOCB == 0 )then  !   ISTPOCB == 1 STPOCB IS INITIALIZED FROM POCB.INP` (328)이면 같은 범위의 STPOCB=STPOCBC(329–333). `if( ISTPOCB /= 3 )then` (336)이면 NS=1..NSED+NSND·K=1..KB·L=1..LC에서 STFPOCB=FPOCBST(NS,1)(338–344). ISTPOCB=3은 FPOCB.INP에서 초기화한다는 주석이 있다(337). |
| 346–376 | 시작 시 9행 AINIT 루틴·316행 IVAL=1 및 ISTRAN(5)>0 참 분기 안. 수층(water column)의 `if( ISTDOCW == 0 )then` (348)이면 K=1..KC·L=1..LC에서 STDOCW=STDOCWC(349–353). `if( ISTPOCW == 0 )then` (356) 안에서 `if( STPOCWC <= 0.0 ) STPOCWC = 1E-12` (357), K=1..KC·L=1..LC의 STPOCW=STPOCWC(358–363). 별도 `if( ISTPOCW /= 3 )then` (366)이면 NS=1..NSED+NSND·K=1..KC·L=1..LC에서 STFPOCW=FPOCWST(NS,1)(368–374). 367행 주석은 ISTPOCW=3일 때 STFPOCB를 FPOCW.INP에서 초기화한다고 적는다. 316행 조건을 닫는다(376). |
| 377–386 | 시작 시 9행 AINIT 루틴 안. QCTL의 NQCTYP=3·4용 새 변수라는 주석(378). `LOWCHORDU = -9999.` (379), `LOWCHORDV = -9999.` (380), NLOWCHORD=0(381). return(383), AINIT 종료(385), 마지막 빈 줄(386). 이 파일에는 다른 루틴의 call 문장이 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 23·64–65: 지역 I·J는 선언과 IL/JL 복사 이후 이 루틴에서 참조되지 않는다.
- 89–90·105–113·179–180: 격자 면적·수심·AVO를 분모에 사용한다. 해당 계산 앞에는 분모가 0인지 검사하는 조건이 없다.
- 211·222–228: NSED와 NSND가 0이어도 해당 반복 수는 각각 최소 1이다. SND 초기값의 SEDO 인덱스는 NX+NTMPC를 사용한다.
- 341·371: STFPOCB와 STFPOCW 초기화는 모든 K에 각각 FPOCBST(NS,1)와 FPOCWST(NS,1)을 복사한다.
- 366–371: 수층 주석은 STFPOCB를 FPOCW.INP에서 초기화한다고 적는다(367). 해당 실행문은 STFPOCW에 대입한다(371).
- 357·379–380: STPOCWC의 비양수 대체값은 1E-12로 고정되어 있다. LOWCHORDU·LOWCHORDV의 초기값은 -9999.로 고정되어 있다.
