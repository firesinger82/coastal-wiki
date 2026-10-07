---
file: models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/Waves/mod_getswan.f90
lines: 411
sha256: 8308338e46b1ae7d300a299813c1037118c7187e0072ff7ba304e408a9cfb58a
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# mod_getswan.f90 — 판독 구간 기록

구간은 1행부터 411행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–31 | EFDC+·GPLv2 머리말(1–8). GETSWANMOD는 SWAN FRM/GRP 또는 LOC 대응 TBL 출력을 직접 읽는다는 주석이다(9–12). 소산(dissipation)을 W/m²로 받기 위한 INRHOG=1과 IFWAVE·SWANGRP 입력 카드 안내(13–16), 작성자(17). GLOBAL·INFOMOD·WAVELENGTH·XYIJCONV·WINDWAVE의 SHLIM/WHMI·MPI 출력/변수·Broadcast_Routines 사용, implicit none·contains·빈 줄(19–31). |
| 32–56 | GETSWAN_GRP 입구·전체 격자 출력 요청 예와 출력 셀 범위 L=2:LA 주석(32–40). 문자열·정수·save 격자 범위/열 번호·VAL(20)·파향/주기/소산·방향 변환 변수 선언(42–50). `if( .not. allocated(LWVCELL_Global) )then` (51)은 LWVCELL_Global·LWVMASK_Global을 LCM_Global 크기로 할당하고 마스크를 .false.로 초기화한다(52–54). 조건 종료·빈 줄(55–56). |
| 57–80 | 시작 시 32행 GETSWAN_GRP 안. `if( JSWAVE == 0 )then` (57) 안의 `if( process_id == master_id )then` (60)에서 UNIT 99로 SWAN.EE를 연다(61). 문자열을 읽고 `IPOS = SCAN(STR, "=", BACK = .TRUE.)` (64·67·70·73)로 마지막 등호를 찾은 뒤 SWAN_M1/N1/M2/N2를 내부 read한다(65·68·71·74). master 조건 밖에서 Broadcast_Scalar로 네 범위를 전파한다(76–79). JSWAVE 조건 종료(80). |
| 81–113 | 시작 시 32행 GETSWAN_GRP 안. `if( process_id == master_id )then` (81)은 swan_grp.inp를 UGRP로 연다(82–83). 내부 `if( JSWAVE == 0 )then` (84)에서 5행을 읽는다(85–86). `if( ISO > 0 ) STOP 'SWAN_GRP.INP: READING ERROR'` (87). `STR  = ADJUSTL(STR)` (89), `TERM = ADJUSTL(STR(2:))` (90), `STR = READSTR(UGRP)` (91), `NCOL = NUMCOL(TERM)` (92). NHS/NPK/NRT/NWL/NHP/NDI는 FINDSTR로 Hsi/PkD/RTp/Wle/Dep/Dis 열을 찾는다(95–100). 내부 조건 종료(101). IWVCOUNT 이전 자료를 읽는 버퍼(buffer) 루프 전체는 주석이다(103–112). |
| 114–143 | 시작 시 32행 GETSWAN_GRP·81행 master 조건 안. NWVCELLS=0(114). `LOOPJ: DO J = SWAN_N1+1, SWAN_N2+1` (115), `do I = SWAN_M1+1, SWAN_M2+1` (116)에서 VAL(1:NCOL)을 읽는다(117). `if( ISO > 0 ) STOP 'SWAN_GRP.INP: READING ERROR'` (118). LIJ_GLOBAL로 LG 조회(120), `if( LG <= 1 .or. LG > LA_Global ) CYCLE` (121). `NWVCELLS = NWVCELLS+1` (123), 전역 셀 목록·마스크·HEISIG 복사(124–128). `if( MVEG_Global(LG) /= MVEGOW  )then` (129)은 HEISIG=0(130). `else` (131)의 다중행 조건은 `if( (MVEG_Global(LWC_Global(LG)) /= MVEGOW) .or. &` (132); `(MVEG_Global(LEC_Global(LG)) /= MVEGOW) .or. &` (133); `(MVEG_Global(LSC_Global(LG)) /= MVEGOW) .or. &` (134); `(MVEG_Global(LNC_Global(LG)) /= MVEGOW)      )  WV_Global(LG).HEISIG = 0.5*WV_Global(LG).HEISIG` (135). 조건 밖에서 WDIR/WPRD/LENGTH/EDIS를 해당 열에서 복사한다(138–141). 주석 파향은 진동쪽에서 반시계 방향 0–360도이고 주기는 s, 파장은 m이다. EDIS/RHO 소산 대입은 주석이다(142). |
| 144–163 | 시작 시 32행 GETSWAN_GRP·81행 master 조건·115행 J·116행 I 루프 안. `if( WV_Global(LG).HEISIG >= WHMI )then` (144)은 `WVDX= COS(WDIR*PI/180)` (145), `WVDY= SIN(WDIR*PI/180)` (146), `WVCX =  CVN_Global(LG)*WVDX - CVE_Global(LG)*WVDY` (147), `WVCY = -CUN_Global(LG)*WVDX + CUE_Global(LG)*WVDY` (148), `WV_Global(LG).DIR  = ATAN2(WVCY,WVCX)` (149), `WV_Global(LG).FREQ = 2.*PI/WPRD` (150). 주석은 DIR이 셀 동쪽 기준 반시계 방향 −pi..pi라고 적는다(149). 소산 대체식은 주석이다(151). `else` (152)는 DIR/LENGTH/HEISIG/DISSIPA(KC)=0(153–154·156–157), `WV_Global(LG).FREQ  = 1.` (155). 조건·I/J 루프 종료(158–160), 전역 HEISIG를 HEIGHT에 복사(161). master 조건 종료·빈 줄(162–163). |
| 164–200 | 시작 시 32행 GETSWAN_GRP 안이며 master 조건 밖. 셀 목록·마스크·HEIGHT/DIR/LENGTH/FREQ/HEISIG를 Broadcast_Array로 전파한다(165–171). NWVCELLS=0(174), LG=2:LA_Global 루프(175)에서 Map2Local(LG).LL을 L에 복사(177). `if(L > 0 )then` (179)은 `NWVCELLS = NWVCELLS + 1` (181), 지역 목록·마스크·파 속성 복사(183–189), `WV(L).DISSIPA(KC) = 0.25*g*WV(L).HEIGHT**2*WV(L).FREQ/(2.*PI)` (192). 조건·루프 종료 뒤 `if( IWVCOUNT == NWVTIM )then` (196)은 UGRP를 닫고 기록 끝 메시지를 쓴다(197–198). 조건·루틴 종료(199–200). |
| 201–240 | 빈 줄·GETSWAN_LOC 입구·LOC/TBL 요청 예·선언(201–220). `if( JSWAVE == 0 )then` (222) 안의 `if( process_id == master_id )then` (224)은 swan_loc.inp를 열고 READSTR를 호출한다(227–228). NP=0(229), `do while(.TRUE.)` (230)에서 문자열 read의 end=250(231), `NP = NP+1` (232). 레이블 250의 rewind와 NLOC=NP 복사(234–235), master 조건 종료(236). 여전히 JSWAVE 조건 안에서 SWNLOC의 ICEL/JCEL/XCEL/YCEL을 NLOC 크기로 할당한다(238–239). |
| 241–289 | 시작 시 202행 GETSWAN_LOC·222행 JSWAVE==0 조건 안. `if( process_id == master_id )then` (241)은 READSTR와 N=1:NLOC 좌표 read, ULOC close, `call XY2IJ(SWNLOC)`를 수행한다(242–247). UTBL로 swan_tbl.inp를 연다(249–250). 5행 읽기(251–252)의 `if( ISO > 0 )then` (253)은 STOP(254), `elseif( ISO < 0 )then` (255)은 파일 끝 메시지(256). `STR  = ADJUSTL(STR)` (259), `TERM = ADJUSTL(STR(2:))` (260), `STR = READSTR(UTBL)   !NUMBER` (261), `NCOL = NUMCOL(STR)` (262). 열·단위 주석(264–265), Hsi/PkD/RTp/Wle/Dep/Dis에 대한 FINDSTR 호출(267–272). NW=1:IWVCOUNT-1·N=1:NLOC 버퍼 루프(275–276)에서 read(277), `if( ISO > 0 ) STOP 'SWAN_TBL.INP: READING ERROR'` (278). 루프·master 조건 종료(279–281). 네 SWNLOC 배열의 Broadcast_Array 호출은 주석이다(283–286). JSWAVE 조건 종료·빈 줄(288–289). |
| 290–314 | 시작 시 202행 GETSWAN_LOC 안이며 JSWAVE 조건 밖. NWVCELLS=0(290), N=1:NLOC 루프(291), UTBL read(292), `if( ISO > 0 ) STOP 'SWAN_TBL.INP: READING ERROR'` (293). LIJ로 L 조회(295), `if( L <= 1 .or. L>LA) CYCLE` (296), `NWVCELLS = NWVCELLS+1` (298), 셀 목록·마스크·HEISIG 복사(299–301). `if( ISVEG > 0 )then` (304) 안의 `if( MVEGL(L) /= MVEGOW  )then` (305)은 HEIGHT=0(306). `else` (307)의 원문은 `if( (MVEGL(LWC(L)) /= MVEGOW) .or. &` (308); `(MVEGL(LEC(L)) /= MVEGOW) .or. &` (309); `(MVEGL(LSC(L)) /= MVEGOW) .or. &` (310); `(MVEGL(LNC(L)) /= MVEGOW)      )  WV(L).HEIGHT = 0.5*WV(L).HEIGHT` (311). 두 조건 종료·빈 줄(312–314). |
| 315–344 | 시작 시 202행 GETSWAN_LOC·291행 N 루프 안이며 식생 조건 밖. WDIR/WPRD/LENGTH/EDIS 복사와 단위 주석(315–318), EDIS/RHO 대입 주석(319). `if( WV(L).HEISIG >= WHMI .and. WVPRD > 0 )then` (320)은 `WVDX= COS(WDIR*PI/180)` (321), `WVDY= SIN(WDIR*PI/180)` (322), `WVCX =  CVN(L)*WVDX - CVE(L)*WVDY` (323), `WVCY = -CUN(L)*WVDX + CUE(L)*WVDY` (324), `WV(L).DIR= ATAN2(WVCY,WVCX)` (325), `WV(L).FREQ = 2.*PI/WPRD` (326), `WV(L).DISSIPA(KC) = 0.25*g*WV(L).HEISIG**2/WPRD` (327). `else` (328)는 DIR/LENGTH/HEISIG/DISSIPA(KC)=0(329–330·332–333), `WV(L).FREQ  = 1.` (331). 조건·루프 종료 뒤 HEIGHT에 HEISIG를 복사한다(337). `if( IWVCOUNT == NWVTIM )then` (339)은 UTBL close·기록 끝 출력(340–341). 조건·루틴 종료·빈 줄(342–344). |
| 345–372 | STRPROC는 입력 STR·출력 TERM(:)/N과 지역 정수·길이 120 SSTR를 선언한다(345–350). `SSTR = ADJUSTL(STR)` (352), `STRL = LEN_TRIM(SSTR)` (353), SSTR에 2:STRL 복사(354), N=0(355). `do while(.TRUE.)` (356)에서 `SSTR = ADJUSTL(SSTR)` (357), `STRL = LEN_TRIM(SSTR)` (358). `if( STRL > 0 )then` (359)은 `N = N+1` (360), I=1:STRL 루프(361)의 `if( ICHAR(SSTR(I:I)) == 32) EXIT` (362)로 공백을 찾고 `TERM(N) = SSTR(1:I-1)` (364), `SSTR = SSTR(I:STRL)` (365). `else` (366)는 EXIT(367). 조건·루프·루틴 종료·빈 줄(368–372). |
| 373–398 | GETWAVEDAY 안내·선언·빈 줄(373–380). `if( process_id == master_id )then` (382)은 wavetime.inp를 UNIT 1로 열고 READSTR 호출·NP=0(383–386). `do while(.TRUE.)` (387)에서 end=100·IOSTAT=IOS로 문자열을 읽는다(388). `if( IOS > 0 ) STOP 'WAVETIME.INP: READING ERROR'` (389), `NP = NP + 1` (390). rewind·NWVTIM=NP·조건 종료(392–394). `call Broadcast_Scalar(NWVTIM, master_id)` (395), `allocate(WAVEDAY(NWVTIM+1))` (397). |
| 399–411 | 시작 시 373행 GETWAVEDAY 안. `if( process_id == master_id )then` (399)은 READSTR 호출(400), NP=1:NWVTIM 루프에서 WAVEDAY를 읽고 UNIT 1을 닫는다(401–404). 조건 밖에서 `Call Broadcast_Array (WAVEDAY, master_id)` (407). 빈 줄·루틴·모듈 종료(408–411). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 61–80: GETSWAN_GRP는 UNIT 99로 SWAN.EE를 연다. 이 파일에는 UNIT 99 close가 없다.
- 81–112·196–199: GETSWAN_GRP의 UGRP open은 매 호출 경로에 있다. 처음 다섯 행의 판독은 JSWAVE==0 조건 안에 있으며 이전 레코드를 읽는 버퍼 루프는 주석이다. UGRP close는 IWVCOUNT==NWVTIM 조건 안에 있다.
- 47·92–100·117 및 217·262–272·292: VAL의 크기는 20이고 판독 슬라이스는 1:NCOL이다. 찾은 열 번호와 NCOL을 VAL 범위에 맞는지 확인하는 조건은 해당 사용 앞에 없다.
- 99–100·141·192 및 271–272·318–327: NHP는 FINDSTR 결과를 받지만 VAL(NHP)는 사용하지 않는다. EDIS는 VAL(NDI)를 받지만 활성 소산 계산식에 사용되지 않는다.
- 175–192: 지역 NWVCELLS 증가는 Map2Local(LG).LL>0만으로 결정한다. LWVMASK_Global(LG)가 참인지 확인하는 조건은 이 매핑 루프에 없다.
- 224–239: NLOC=NP는 master 조건 안에 있다. NLOC 크기의 SWNLOC 할당 전에 NLOC를 Broadcast_Scalar로 전파하는 호출은 이 루틴에 없다.
- 241–286·291–295: UTBL open·SWNLOC 좌표 read·XY2IJ 호출은 master 조건 안에 있다. SWNLOC 전파 호출은 주석이며 이후 UTBL read·SWNLOC 인덱스 조회는 master 조건 밖에 있다.
- 304–313·337: 식생 분기는 WV(L).HEIGHT를 바꾼다. 루프 뒤 337행에서 전체 HEIGHT를 HEISIG로 다시 복사한다.
- 316·320·326–327: 주기 입력을 복사하는 지역 변수는 WPRD이다. 320행 조건은 WVPRD>0을 검사하고, 주파수·소산 식의 분모는 WPRD이다.
- 397·401–407: WAVEDAY는 NWVTIM+1 크기로 할당하고 1:NWVTIM만 읽는다. 마지막 원소에 대입하는 문장 없이 배열 전체를 전파한다.
