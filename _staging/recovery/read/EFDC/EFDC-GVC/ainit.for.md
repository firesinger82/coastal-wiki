---
file: models/EFDC/raw/source_code/EFDC-GVC/ainit.for
lines: 832
sha256: 67114c5b751eb2d75bec4673b038a7c6ac3f2c28db9cf0806c77e7bbeb33718c
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# ainit.for — 판독 구간 기록

구간은 1행부터 832행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–34 | 구분 주석과 `SUBROUTINE AINIT` 입구(1–6). EFDC-FULL 1.0a 및 수정일 주석(8–10). 변경 기록은 건조 셀 수송 우회 마스크(transport bypass mask)와 수로 길이 초기화 변경을 적는다(14–21). `INCLUDE 'EFDC.PAR'` (26), `INCLUDE 'EFDC.CMN'` (27). 배열 초기화 안내와 구분 주석(29–34). 포함 파일 내부는 이번 판독 대상이 아니다. |
| 35–71 | 시작 시 6행 AINIT 안. 경계 인덱스 1과 LC에서 ZBR·ZBRE=ZBRADJ, 깊이 배열=HMIN, 격자 길이 배열=DX 또는 DY, MVEGL=1로 초기화한다(35–69). 면적 식은 `DXYP(1)=DX*DY` (50), `DXYP(LC)=DX*DY` (68). BELV는 각각 2와 LA 인덱스에서 복사한다(52·70). 끝 주석(71). |
| 72–94 | 시작 시 6행 AINIT 안. `IF(ISGWIE.EQ.0) DAGWZ=0.` (72). L=2..LA 루프(73–91)에서 I·J를 IL·JL에서 가져온다(74–75). `BELAGW(L)=BELV(L)-DAGWZ` (81), ZBRE에 ZBR 복사(82), `DLON(L)=CDLON1+(CDLON2*FLOAT(I)+CDLON3)/60.` (84), `DLAT(L)=CDLAT1+(CDLAT2*FLOAT(J)+CDLAT3)/60.` (86). 좌표 방향 계수 CUE·CVN=1, CVE·CUN=0(87–90). 깊이 평균 및 특정 경위도 식은 주석 처리되어 있다(76–80·83·85). 구분 주석(92–94). |
| 95–114 | 시작 시 6행 AINIT 안. L=2..LA에서 LS=LSC(L)(95–101). `DXU(L)=0.5*(DXP(L)+DXP(L-1))` (97), `DYU(L)=0.5*(DYP(L)+DYP(L-1))` (98), `DXV(L)=0.5*(DXP(L)+DXP(LS))` (99), `DYV(L)=0.5*(DYP(L)+DYP(LS))` (100). 다음 L 루프(103–111)의 면 깊이는 `HMU(L)=0.5*(DXP(L)*DYP(L)*HMP(L)+DXP(L-1)*DYP(L-1)*HMP(L-1))` (107), `&           /(DXU(L)*DYU(L))` (108), `HMV(L)=0.5*(DXP(L)*DYP(L)*HMP(L)+DXP(LS )*DYP(LS)*HMP(LS ))` (109), `&           /(DXV(L)*DYV(L))` (110). 단순 평균 대체식은 주석(105–106). 끝 구분 주석(112–114). |
| 115–164 | 시작 시 6행 AINIT 안. L=1..LC 루프를 연다(115). 행렬 계수·힘·유량·작업 배열 대부분을 0으로, CC·CCC를 1로 초기화한다(116–141·144–149·164). `P(L)=G*(HMP(L)+BELV(L))` (142), `P1(L)=G*(HMP(L)+BELV(L))` (143). `HP(L)=HMP(L)+PDGINIT` (150), `HU(L)=HMU(L)+PDGINIT` (151), `HV(L)=HMV(L)+PDGINIT` (152), `HPI(L)=1./HP(L)` (153), `HUI(L)=1./HU(L)` (154), `HVI(L)=1./HV(L)` (155). 수질·이전 시각 깊이 식은 `HWQ(L)=HMP(L)+PDGINIT` (156), `H1P(L)=HMP(L)+PDGINIT` (157), `H2P(L)=HMP(L)+PDGINIT` (158), `H1U(L)=HMU(L)+PDGINIT` (159), `H1V(L)=HMV(L)+PDGINIT` (160), `H1UI(L)=1./H1U(L)` (161), `H1VI(L)=1./H1V(L)` (162), `H2WQ(L)=HMP(L)+PDGINIT` (163). |
| 165–210 | 시작 시 6행 AINIT·115행 L 루프 안. HRU·HRV=0(165–166). 셀·면 마스크와 여러 계수 SCB부터 SDY까지를 1로 초기화한다(167–185). 바닥·표면 힘, 적분 유량, 교차 속도, 작업 배열, RIFTR·EVAPSW를 0으로 초기화한다(186–210). |
| 211–244 | 시작 시 6행 AINIT·115행 L 루프 안. EVAPGW=0(211). QQL·QQL1·QQL2의 수직 인덱스 0과 KC, DML의 0과 KC를 0으로 설정한다(212–219). 지하수·폐기물 유량과 부피, 바닥 교환 배열 6개를 0으로 설정한다(220–229). IMASKDRY=0, LMASKDRY=.TRUE.(231–232). GVCSCLP/U/V 및 역계수=1.0, KGVCP/U/V/W=1(233–242). L 루프 종료와 주석(243–244). |
| 245–268 | 시작 시 6행 AINIT 안. NS=1..NSED 및 L=1..LC에서 SEDFBEBKB·SEDFBECHB·SEDFBECHW=0(245–251). NS=1..NSND 및 같은 L 범위에서 대응 SND 배열=0(253–259). NT=1..NTOX 및 같은 L 범위에서 대응 TOX 배열=0(261–267). 각 루프 사이 주석과 끝 주석도 포함한다. |
| 269–310 | 시작 시 6행 AINIT 안. NT=1..NTOX, K=1..KB, L=1..LC에서 TOXB·TOXB1에 TOXBINIT 복사(269–276). NS=1..NSED의 같은 K·L 범위에서 SEDB·SEDB1에 SEDBINIT 복사(278–285). NS=1..NSND에서 `NX=NS+NSED` (287)를 대입하고 같은 K·L 범위에서 SNDB·SNDB1에 SNDBINIT 복사(286–294). 빈 줄·주석(295–296). SEDFDTAP·SEDFDTAN은 NSED×LC 범위, SNDFDTAP·SNDFDTAN은 NSND×LC 범위에서 0.0으로 초기화한다(297–309). 끝 주석(310). |
| 311–333 | 시작 시 6행 AINIT 안. L=1..LC에서 방향별 CSR/CWR/CER/CNR, CSB/CWB/CEB/CNB와 CC 접두 대응 배열, FPR·FPB를 0으로 초기화한다(311–329). ISCDRY·NATDRY=0(330–331). 루프 종료·주석(332–333). |
| 334–372 | 시작 시 6행 AINIT 안. `IF(IS1DCHAN.EQ.1)THEN` (334). 참 분기의 L=1..LC 루프에서 FADYP·FADXP·WPDYP·WPDXP, FADYU·WPDYU·FADXV·WPDXV, DADH와 각 이전값을 1로 초기화한다(335–355). SRFXP/SRFYP/SRFXV/SRFYU 및 이전값은 0으로 초기화한다(356–363). 루프·분기 종료(364–365). 별도 L=1..NLRPD 루프에서 NLRPDL=1(367–369). 끝 구분 주석(370–372). |
| 373–401 | 시작 시 6행 AINIT 안. K=1..KS, L=1..LC 루프(373–398). UUU·VVV=0, AV=AVO, AB=ABO, ABLPF·ABEFF=0(376–385). 역계수는 `AVVI(L,K)=1./AVO` (381), `AVUI(L,K)=1./AVO` (382). QQL·QQL1·QQL2=QQLMIN, DML=DMLMIN, WIRT·WTLPF=0(390–395). AMCW·AMSW 및 AMCAB 계열 대입은 주석 처리(378–379·386–389). 루프 종료와 구분 주석(397–401). |
| 402–447 | 시작 시 6행 AINIT 안. K=1..KC, L=1..LC 루프를 연다(402–403). AH·AHU·AHULPF·AHV·AHVLPF·AHC=AHO, AQ=AVO(405–411). 회전 계수, 부력·농도 작업값, 이류(advection)·힘·유량 작업 배열을 0으로 초기화한다(412–447). |
| 448–478 | 시작 시 6행 AINIT·402행 K·403행 L 루프 안. U·V와 두 이전값, UHDY·VHDX와 이전값, 수질용 유량·속도, 입자용 속도, 저주파 통과(low-pass filter)·작업 배열을 0으로 초기화한다(448–476). UDBDXI·VDBDYI 대입은 주석이며 UUU·VVV로 대체했다고 적는다(477–478). |
| 479–516 | 시작 시 6행 AINIT·402행 K·403행 L 루프 안. SAL·SAL1, SFL·SFL2, CWQ·CWQ2, DYE·DYE1, QSUM·QSUMLPF·QWSEDA 및 TVAR1/2 방향 배열을 0으로 초기화한다(479–499). TEM·TEM1=TEMO(485–486), CTURBB1=CTURB, CTURBB2=CTURB2B(500–501). SUB·SVB·SBX·SBY·SDX·SDY를 대응 3차원 마스크에 복사한다(502–509). LGVCP/U/V=.TRUE.(510–512). 두 루프 종료와 주석(513–516). |
| 517–538 | 시작 시 6행 AINIT 안. `NTMPC=MAX(NSED,1)` (517). NS=1..NTMPC, K=1..KC, L=1..LC에서 SED·SED1=SEDO(NS), SEDLPF=0(518–526). NS=1로 고정(528). K=1..KC, L=2..LA 루프(529–537)에서 `FLOCDIA(L,K)=0.0004  !  initialized in cm equivalent to 4 um` (532), `WSETFLOC(L,K)=80.E-6` (533), `SEDFLOCDIA(L,K)=172.*SED(L,K,NS)/` (534), `&                        (FLOCDIA(L,K)*WSETFLOC(L,K))` (535). FLOCDIA=0.001 대입은 주석(531). 끝 주석(538). |
| 539–562 | 시작 시 6행 AINIT 안. `NTMPN=MAX(NSND,1)` (539), NX=1..NTMPN 루프(540)에서 `NS=NX+NTMPC` (541). K=1..KC, L=1..LC에서 SND·SND1=SEDO(NS), SNDLPF=0(542–549). 별도 NT=1..NTOX, K=1..KC, L=1..LC에서 TOX·TOX1=TOXINTW(NT), TOXLPF=0(551–559). 끝 구분 주석(560–562). |
| 563–591 | 시작 시 6행 AINIT 안. K=0..KC, L=1..LC 루프(563–588). W·W1·W2와 수질·입자·저주파·힘 작업 배열=0(566–573), QQ·QQ1·QQ2=QQMIN(574–576), VPX·VPY·WWW·BBT 및 이전값=0(577–582). SWB3D·SWB3DO에 SWB를 복사한다(583–584). WDBDZI 대입은 WWW로 대체했다는 주석(585). 끝 구분 주석(589–591). |
| 592–630 | 시작 시 6행 AINIT 안. K=1..KB, L=1..LC에서 VOLBW2·VOLBW3·PARTMIXZ=0(592–598). `IF(MDCHH.GE.1)THEN` (602)이면 NMD=1..MDCHH에서 호스트·x/y 수로 인덱스를 가져온다(604–607). `IF(PMDCH(NMD).LT.0.0) PMDCH(NMD)=HWET` (609). `IF(MDCHTYP(NMD).EQ.1)THEN` (611) 안에서 `IF(CHANLEN(NMD).LT.0.0)THEN` (612)이면 `CHANLEN(NMD)=0.25*DYP(LHOST)` (613), `ELSE` (614)이면 `CHANLEN(NMD)=CHANLEN(NMD)-0.5*DYP(LCHNU)` (615). 독립 `IF(MDCHTYP(NMD).EQ.2)THEN` (619) 안에서 `IF(CHANLEN(NMD).LT.0.0)THEN` (620)이면 `CHANLEN(NMD)=0.25*DXP(LHOST)` (621), `ELSE` (622)이면 `CHANLEN(NMD)=CHANLEN(NMD)-0.5*DXP(LCHNV)` (623). 각 분기·루프 종료(616–628), 구분 주석(629–630). |
| 631–667 | 시작 시 6행 AINIT 안. 퇴적물·독성물질 유기탄소(organic carbon) 초기화 주석(632). IVAL=0(634), NT=1..NTOX에서 `IF(ISTOC(NT).GT.0)IVAL=1` (636). `IF(IVAL.EQ.0)THEN` (639)이면 K=1..KB, L=1..LC에서 STDOCB·STPOCB=0(640–645), NS=1..NSED+NSND의 같은 K·L 범위에서 STFPOCB=1(646–652). 수층 K=1..KC, L=1..LC에서 STDOCW·STPOCW=0(653–658), NS=1..NSED+NSND의 같은 수층 범위에서 STFPOCW=1(659–665). 분기 종료와 주석(666–667). |
| 668–695 | 시작 시 6행 AINIT 안. `IF(IVAL.EQ.1)THEN` (668)을 연다. `IF(ISTDOCB.EQ.0)THEN` (670)이면 K=1..KB, L=1..LC에서 STDOCB=STDOCBC(671–676). 별도 `IF(ISTPOCB.EQ.0)THEN` (678)이면 같은 범위에서 STPOCB=STPOCBC(679–684). 별도 `IF(ISTPOCB.EQ.2)THEN` (686)이면 NS=1..NSED+NSND, K=1..KB, L=1..LC에서 STFPOCB=FPOCBST(NS,1)(687–694). 끝 주석(695). |
| 696–723 | 시작 시 6행 AINIT·668행 IVAL=1 참 분기 안. `IF(ISTDOCW.EQ.0)THEN` (696)이면 K=1..KC, L=1..LC에서 STDOCW=STDOCWC(697–702). 독립 `IF(ISTPOCW.EQ.0)THEN` (704)이면 같은 범위에서 STPOCW=STPOCWC(705–710). 독립 `IF(ISTPOCW.EQ.2)THEN` (712)이면 NS=1..NSED+NSND, K=1..KC, L=1..LC에서 STFPOCW=FPOCWST(NS,1)(713–720). IVAL 분기 종료·주석(721–723). |
| 724–763 | 시작 시 6행 AINIT 안. Housatonic 먹이사슬(food chain) 초기화 및 Fortran 90 전용 주석(726–728). ATOXPF·ATOXFDF·ATOXCDF 계열, 바닥 교환·부피·유입·유출, ASEDF 계열 배열을 배열 전체 대입으로 0 초기화한다(730–762). ATOXCDFBWAD·ATOXCDFBWADP·ATOXCDFBWADN의 0 대입이 반복된다(753–758). 끝 주석(763). |
| 764–832 | 시작 시 6행 AINIT 안. 앞 배열 전체 초기화와 대응하는 NT·NS·L 반복문 형태의 옛 초기화는 모두 cjah 주석 처리되어 있다(764–826). 그 주석은 ATOXPFWX/WY/BW/BWP/BWN, ATOXPFBLX/BLY, ATOXFDF·ATOXCDF·바닥 교환·부피·유입·유출 및 ASEDFWX/WY/BLX/BLY의 0 대입을 담는다. 끝 구분 주석(827–830), `RETURN` (831), `END` (832). 호출하는 외부 루틴은 이 파일에 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 142–163: P·P1의 초기식에는 PDGINIT가 없다. HP·HU·HV와 여러 이전 시각 깊이의 초기식에는 PDGINIT가 있다.
- 153–162·381–382: 깊이와 AVO의 역수를 계산한다. 이 초기화 블록에는 해당 분모의 0 검사 조건이 없다.
- 286–294: NSND 바닥 초기화 루프는 NX=NS+NSED를 대입한다. 그 루프 본문에서 NX를 참조하지 않는다.
- 517–545: SED 초기화 반복 상한은 MAX(NSED,1)이다. SND 초기값의 SEDO 인덱스는 NX+NTMPC이다.
- 528–535: 응집체(floc) 초기화는 NS=1을 사용한다. FLOCDIA=0.0004, WSETFLOC=80.E-6, 계수 172.를 고정한다. 이 블록에는 NSED 조건 검사가 없다.
- 753–758: ATOXCDFBWAD·ATOXCDFBWADP·ATOXCDFBWADN의 0 대입이 각각 두 번 연속된 묶음으로 나타난다.
