---
file: models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/MPI_Domain_Decomp/Allocate_Domain_Decomp.f90
lines: 422
sha256: 804c1bd03ae7ca50eef1cecc7e860a79a6abebb0a2bba6f9aaae13586f89039b
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Allocate_Domain_Decomp.f90 — 판독 구간 기록

구간은 1행부터 422행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–38 | EFDC+·저작권·GPLv2 머리말과 영역 분할(domain decomposition) 배열 할당 목적·작성자·변경 이력·빈 줄(1–23). `Allocate_Domain_Decomp`를 시작한다(24). GLOBAL·Allocate_Initialize·수질·RPEM·MPI·매핑·출력 변수 모듈을 사용한다(26–32). implicit none과 정수 L·NMAX를 선언한다(34–37). |
| 39–99 | 시작 시 24행 Allocate_Domain_Decomp 안. IL2IG·IG2IL은 `-2:global_max_width_x+2`, JL2JG·JG2JL은 `-2:global_max_width_y+2`로 직접 할당하고 0으로 초기화한다(40–47). CLTMSR_GL은 MLTMSRM 크기의 문자 배열이다(50). GRPID_GL 할당은 주석이다(51). `AllocateDSI`를 호출하여 서·동 연결 배열은 NPEWBP 크기·0(54–55), GWCSER_Global은 NDGWSER·NGWSERM·NSTVM2 크기·0.0(57), NGWSL·건조 상태 배열은 LCM_Global 크기·0(58–62)으로 요청한다. BELV·DXP·DYP·HP·H1P·H2P·HWQ·H2WQ·ZBR은 전역 셀 크기·0.0, MVEG는 0을 요청한다(64–73). 전단(shear)의 전역 두 배열은 LCM_Global, 지역 두 배열은 LCM 크기·0.0이다(75–78). 증발·지하수·강우·사방 경계·수송량·SUB/SVB 전역 배열은 LCM_Global 크기·0.0이다(80–98). |
| 100–127 | 시작 시 24행 Allocate_Domain_Decomp 안. `AllocateDSI`로 U·V·U1·V1·W를 LCM_Global·KCM·0.0으로 요청한다(100–104). QQ·QQ1·QQL·QQL1·DML은 두 번째 크기 인수에 -KCM을 전달한다(106–110). QSUM은 LCM_Global·KCM, QSUME는 LCM_Global, VHDX2·UHDY2는 LCM_Global·KCM이며 초기화 인수는 0.0이다(112–116). TBX·TBY·TSX·TSY와 각 1 시점 배열은 LCM_Global·0.0이다(118–126). 음수 크기 인수의 실제 하한 처리는 호출 대상 내부이므로 이 파일만으로 정하지 않는다. |
| 128–163 | 시작 시 24행 Allocate_Domain_Decomp 안. `if( ISGOTM > 0 )then` (128)은 TKE3D·EPS3D·GL3D를 LCM_Global·-KCM·0.0으로 요청한다(129–131). `if( ISTRAN(1) > 0 )then` (134)은 SAL·SAL1을 LCM_Global·KCM·0.0으로 요청한다(135–136). `if( ISTRAN(2) > 0 )then` (139)은 TEM·TEM1을 LCM_Global·KCM, TEMB·SHAD를 LCM_Global 크기·0.0으로 요청한다(140–143). 그 안 `if( ISICE > 0 )then` (144)은 ICETHICK·ICETEMP를 전역 셀 크기·0.0으로 요청한다(145–146). `if( ISTRAN(3) > 0 )then` (149)은 DYE·DYE1을 LCM_Global·KCM·NDYM·0.0으로 요청한다(150–151). `if( ISTRAN(4) > 0 )then` (153)은 SFL을 LCM_Global·KCM·0.0으로 요청한다(154). `if( ISTRAN(5) > 0 )then` (157)은 TOX·TOX1을 LCM_Global·KCM·NTXM, TOXB·TOXB1을 LCM_Global·KBM·NTXM 크기·0.0으로 요청한다(158–161). 각 조건 종료와 빈 줄을 포함한다. |
| 164–202 | 시작 시 24행 Allocate_Domain_Decomp 안. `if( ISTRAN(6) > 0 .or. ISTRAN(7) > 0 )then` (164) 안에서 HBED·HBED1, BDENBED·PORBED·VDRBED·VDRBED1은 LCM_Global·KBM·0.0, BEDMAP·KBT는 LCM_Global·0을 요청한다(165–174). `if( ISTRAN(7) > 0 .and. ICALC_BL > 0 .and. NSND > 0 )then` (176)은 QSBDLDX·QSBDLDY의 두 번째 크기로 NSND를 쓴다(177–178). `elseif( ICALC_BL > 0 )then` (179)은 같은 배열에 NSEDS를 쓴다(180–181). `if( NSEDFLUME > 0 )then` (184)은 LAYERACTIVE를 KB·LCM_Global·0, 침식·퇴적 플럭스(flux)를 LCM_Global·NSEDS2·0.0, TAU·D50AVG를 LCM_Global·0.0으로 요청한다(185–189). BULKDENS·TSED·TSED0은 KB·LCM_Global, PERSED는 NSEDS·KB·LCM_Global 크기·0.0이다(190–193). 그 안 `if( ICALC_BL > 0 )then` (194)은 CBL을 LCM_Global·NSEDS·0.0으로 요청하고, 다시 `if( ISTRAN(5) > 0 )then` (196)은 CBLTOX를 LCM_Global·NTXM·0.0으로 요청한다(197). 모든 조건을 닫는다(198–201). |
| 203–217 | 시작 시 24행 Allocate_Domain_Decomp 안. `if( ISTRAN(6) > 0 )then` (203)은 SED·SED1을 LCM_Global·KCM·NSEDS2, SEDB·SEDB1을 LCM_Global·KBM·NSEDS 크기·0.0으로 요청한다(204–207). 프로펠러 세척류(propwash)의 빠른 침강용 SDF 할당은 주석이다(208–209). `if( ISTRAN(7) > 0 )then` (211)은 SND·SND1을 LCM_Global·KCM·NSNM, SNDB·SNDB1을 LCM_Global·KBM·NSNM 크기·0.0으로 요청한다(212–215). 조건 종료와 빈 줄(216–217). |
| 218–260 | 시작 시 24행 Allocate_Domain_Decomp 안. `if( ISTRAN(8) > 0 )then` (219)은 WQV_Global에 LCM_Global·KCM·-NWQVM·0.0을 전달한다(220). 그 안 `if( ISRPEM > 0 )then` (222)은 WQRPS·WQRPR·WQRPE·WQRPD를 전역 셀 크기·0.0, LMASKRPEM을 전역 셀 크기·.false.로 요청한다(223–227). 이 내부 조건 밖에서 퇴적층 속성작용(sediment diagenesis) 주석과 SMPON·SMPOP·SMPOC·SMDFN·SMDFP·SMDFC의 LCM_Global·NSMGM·0.0 요청을 포함한다(230–236). SM1/SM2의 NH4·NO3·PO4·H2S·SI, SMPSI·SMBST·SMT·SMCSOD·SMNSOD, WQBFNH4·WQBFNO3·WQBFO2·WQBFCOD·WQBFPO4D·WQBFSAD는 전역 셀 크기·0.0이다(238–258). 수질 조건 종료와 빈 줄(259–260). |
| 261–294 | 시작 시 24행 Allocate_Domain_Decomp 안. WVHUU·WVHVV·WVHUV는 LCM_Global·KCM·0.0, QQWV3는 LCM_Global·0.0이다(261–264). 기본값 요청은 `call AllocateDSI( KSZ_Global,    LCM_Global,    1)` (266). 사방 연결 배열은 전역 셀 크기·0(268–271), UMASK·VMASK는 -LCM_Global·0을 전달한다(273–274). `if( ISWAVE > 0 )then` (276)은 FXWAVE·FYWAVE를 LCM_Global·KCM·0.0, WV_HEIGHT·WV_PERIOD·WV_DIR·WV_DISSIPA를 전역 셀 크기·0.0으로 요청한다(278–283). WV_Global을 LCM_Global 크기로 직접 할당하고 `do L = 1, LCM_Global` (286)에서 각 DISSIPA를 KCM·0.0으로 요청한다(285–288). 조건 종료 뒤 IJCT_GLOBAL·IJCTLT_GLOBAL·LIJ_Global은 global_max_width_x·global_max_width_y·0이다(291–293). |
| 295–345 | 시작 시 24행 Allocate_Domain_Decomp 안. 개방 경계(open boundary)의 남·서·동·북별 배열에 `AllocateDSI`를 호출한다. IPB·JPB·LPB·ISPB·ISPR·NPSER·NPSER1 계열은 각각 NPBSM·NPBWM·NPBEM·NPBNM 크기·0이다(296–329). PCB·PSB 계열은 해당 경계 크기·MTM·0.0이다(331–339). TPCOORD 계열은 해당 경계 크기·0.0이다(341–344). 주석·빈 줄도 포함한다. |
| 346–397 | 시작 시 24행 Allocate_Domain_Decomp 안. 농도 경계의 IC·JC·NTSCR 계열은 각 방향 NBBSM·NBBWM·NBBEM·NBBNM 크기·0이다(347–366). NCSER 계열은 각 방향 크기·NSTVM2·0, CBS·CBW·CBE·CBN은 각 방향 크기·2·NSTVM2·0.0이다(350–366). ILTMSR·JLTMSR·NTSSSS와 MTMSRP·MTMSRC·MTMSRA·MTMSRUE·MTMSRUT·MTMSRU·MTMSRQE·MTMSRQ·MLTM은 MLTMSRM·0이다(367–379). NLOS·NLOE·NLOW·NLON은 각 방향 농도 경계 크기·KCM·NSTVM2·0, CLOS·CLOE·CLOW·CLON은 같은 크기·0.0이다(381–389). CUE·CUN·CVN·CVE는 전역 셀 크기·0.0, DZC는 LCM_Global·KCM·0.0이다(391–396). |
| 398–422 | 시작 시 24행 Allocate_Domain_Decomp 안. `if(NCDFOUT > 0 )then` (399)은 TAUBSED·TAUBSND·TAUB·WNDVELE·WNDVELN에 LCM_GLOBAL·0.0을 전달한다(400–404). 대기압 기본값 요청은 `call AllocateDSI( PATMT_Global,    LCM_GLOBAL, 1010.)` (405). 조건 종료(406). `If(MPI_Write_Flag )then` (408)은 경계·유량·변수·시계열 배열 크기를 로그에 출력한다(409–416). 조건 밖에서 완료 로그를 쓰고 `WriteBreak(mpi_log_unit)`를 호출한다(419–420). 빈 줄·루틴 종료(421–422). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 37: NMAX는 선언 이후 사용되지 않는다.
- 50: CLTMSR_GL은 직접 할당한다. 이 루틴에는 CLTMSR_GL의 내용 초기화 문장이 없다.
- 51·208–209: GRPID_GL과 SDF_Global의 할당문은 주석 처리되어 있다.
- 399–405: PATMT_Global의 초기화 인수는 하드코딩된 1010.이다. 이 호출 행에는 단위 주석이 없다.
- 408–420: 배열 크기 출력에는 MPI_Write_Flag 조건이 있다. 마지막 완료 로그와 WriteBreak 호출은 그 조건 밖에 있다.
