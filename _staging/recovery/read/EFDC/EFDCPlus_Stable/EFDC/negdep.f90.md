---
file: models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/negdep.f90
lines: 311
sha256: fff56313b7f08b7098d0ad2ae4b896544e6698de6a3357e81b863cd1c6fd1287
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# negdep.f90 — 판독 구간 기록

구간은 1행부터 311행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–36 | 저작권・GNU GPLv2・배포처 주석(1–8). `SUBROUTINE NEGDEP(NOPTIMAL1, LDMOPT1, QCHANUT, QCHANVT, SUB1, SVB1)` (9)는 외부 해(external solution)의 음수 수심(depth)을 점검한다는 목적/2014-12 수정 주석(11–20). GLOBAL・RESTART_MODULE・EFDCOUT・Mod_Map_Write_EE_Binary를 사용하며 implicit none(22–27). 입력 최적 영역 수/크기, LCM 크기 SUB1/SVB1, 지역 인덱스・NCHANM 크기 임시 수로 유량・수면 고도/반 시간 간격 변수를 선언(29–35). |
| 37–66 | 시작 시 9행 NEGDEP 루틴 안. INEGFLG=0 초기화(37). OpenMP `DEFAULT(SHARED) PRIVATE(ND,LF,LL,L)` (40)의 `do ND = 1,NOPTIMAL1` (41)에서 `LF = 2+(ND-1)*LDMOPT1` (42), `LL = min(LF+LDMOPT1-1,LA)` (43). `do L = LF,LL` (44)의 `if( HP(L) <=  0. )then` (45)이면 INEGFLG=1・안쪽 루프 EXIT(46–47). 병렬 루프 종료(49–51). `if( INEGFLG == 0 )then` (53)이면 return(54). 그렇지 않으면 NNEG=0(58), `do L = 2,LA` (59)의 `if( HP(L) <=  0. )then` (60)에서 `NNEG = NNEG + 1` (61). 해당 수와 TIMEDAY를 화면 출력(65). |
| 67–99 | 시작 시 9행 NEGDEP 루틴 안. OUTDIR//mpi_error_file을 추가 쓰기(APPEND)로 열고 `do L = 2,LA` (69)의 `if( HP(L) <= 0.0 )then` (70)에서 북/남/서/동 이웃 인덱스 복사(71–74). 화면에 전역 셀 번호/좌표・프로세스・중심/면 현재/이전 수심・순유입・면 마스크 출력(75–82). `if( IEVAP > 0 )then` (83)이면 강우/증발 출력(84), 별도 `if( ISICE > 0 )then` (86)이면 얼음 두께/이전 두께・상층 수온・기온・태양복사 출력(87). `if( ISDYNSTP == 0 )then` (90)은 DELT=DT 복사(91)와 `DELTD2 = 0.5*DT` (92), `else` (93)는 DELT=DTDYN 복사(94)와 `DELTD2 = 0.5*DTDYN` (95). 오류 파일에 시간/반복/셀/프로세스 표제 출력(98). 셀 조건과 L 루프는 이어진다. |
| 100–137 | 시작 시 9행 NEGDEP 루틴・69행 L 루프・70행 비양수 중심 수심 참 분기 안. 오류 파일에 중앙/서/동/남/북 전역 셀 번호와 현재/이전 수심, 바닥 고도+수심의 수면 고도(water surface elevation), 서/동/남/북 면 수심・현재/이전/초기 마스크, 유량을 면 수심과 폭으로 나눈 현재/이전 수심평균 유속(depth-averaged velocity), 바닥 전단 관련 코너 속도・유량/운동량/순유입 항을 출력(100–136). 독립 단일행 조건 `if( IS2TIM == 0 )` (105・110・132)일 때만 각각 H2P・두 시각 전 수면・UHDY2E/VHDX2E를 출력. 이 구간은 로그 출력이며 배열 값 갱신은 없다. |
| 138–164 | 시작 시 9행 NEGDEP 루틴・69행 L 루프・70행 비양수 중심 수심 참 분기 안. X 운동량 참고식은 주석 처리된 `! ***                       FUHDYE(L) = UHDYE(L)-DELTD2*SUB(L)*HRUO(L)*HU(L)*(P(L)-P(LW))+SUB(L)*DELT*DXIU(L)*(DXYU(L)*(TSX(L)-RITB1*TBX(L))+FCAXE(L)+FPGXE(L)-SNLT*FXE(L))` (138). 서/동 X 압력 경사(pressure gradient)・전체/상하 전단・FCAXE/FPGXE/FXE 항을 출력(140–146). Y 참고식도 주석 처리된 `! ***                       FVHDXE(L) = VHDXE(L)-DELTD2*SVB(L)*HRVO(L)*HV(L)*(P(L)-P(LS ))+SVB(L)*DELT*DYIV(L)*(DXYV(L)*(TSY(L)-RITB1*TBY(L))-FCAYE(L)+FPGYE(L)-SNLT*FYE(L))` (148). 남/북 Y 압력 경사・전체/상하 전단・FCAYE/FPGYE/FYE 항 출력(150–156). `!RCX(L) = 1./( 1.+DELT*FXVEGE(L) )` (158), `!RCY(L) = 1./( 1.+DELT*FYVEGE(L) )` (159)는 주석이며 실행하지 않음. `if( ISVEG > 0 )then` (160)이면 식생(vegetation) 힘과 1/(1+DELT×힘) 항력 저항(drag resistance) 값을 출력(161–162). |
| 165–195 | 시작 시 9행 NEGDEP 루틴・69행 L 루프・70행 비양수 중심 수심 참 분기 안. `if( ISICE > 0 )then` (165)에서 상층 수온/기온/복사/얼음 온도/frazil ice/체적과 현재/이전 얼음 두께를 출력(166–170). 얼음 조건・중심 수심 조건・L 루프 종료(171–173). 별도 `do L = 2,LA` (175)의 `if( (HU(L) < 0. .and. SUBO(L) > 0.5) .or. (HV(L) < 0. .and. SVBO(L) > 0.5 ) )then` (176)이면 북 이웃 LN 복사(177), 화면과 오류 파일에 1112 표제와 중심/사방 면 수심・순유입 이력을 출력(178–192). 면 수심 조건・루프 종료(193–194). |
| 196–209 | 시작 시 9행 NEGDEP 루틴 안. `if( ISPPH == 1 .and. num_Processors == 1 )then` (196)이면 저장 안내 출력(197)과 `call Map_Write_EE_Binary` (199). 그 안의 `if( process_id == master_id )then` (200)이면 연결 저장 로그와 `call EE_LINKAGE(-1)` (201–202). 두 조건 종료(203–204). 별도 `if( ISRESTO == 0 .or. ISGREGOR > 0 )then` (206)이면 `call Restart_Out(TIMEDAY, 1)` (207). 호출 루틴 내부는 이 파일 판독 범위에 포함하지 않았다. |
| 210–233 | 시작 시 9행 NEGDEP 루틴 안. `if( MDCHH > 0 )then` (210)이면 수로 표제 출력(211), `do NMD = 1,MDCHH` (212)에서 호스트(host) L/I/J와 U/V 연결 L 복사(213–217). X 수로 검사 `if( HP(LHOST) < 0.0 .or. HP(LCHNU) < 0.0 )then` (220) 안의 `if( MDCHTYP(NMD) == 1 )then` (221)이면 U 연결 I/J 복사(222–223), `SRFCHAN = HP(LCHNU)+BELV(LCHNU)` (224), `SRFHOST = HP(LHOST)+BELV(LHOST)` (225), `SRFCHAN1 = H1P(LCHNU)+BELV(LCHNU)` (226), `SRFHOST1 = H1P(LHOST)+BELV(LHOST)` (227). 오류 파일에 N・수로/호스트 유형/좌표/건조 상태/현재 수면/수심/P1/H1P와 QCHANU/QCHANUT・상호작용 계수를 출력(228–230). 두 안쪽 조건 종료(231–232). |
| 234–251 | 시작 시 9행 NEGDEP 루틴・210행 MDCHH>0 참 분기・212행 NMD 루프 안. Y 수로 `if( HP(LHOST) < 0.0 .or. HP(LCHNV) < 0.0 )then` (235) 안의 `if( MDCHTYP(NMD) == 2 )then` (236)이면 V 연결 I/J 복사(237–238), `SRFCHAN = HP(LCHNV)+BELV(LCHNV)` (239), `SRFHOST = HP(LHOST)+BELV(LHOST)` (240), `SRFCHAN1 = H1P(LCHNV)+BELV(LCHNV)` (241), `SRFHOST1 = H1P(LHOST)+BELV(LHOST)` (242). 오류 파일에 NITER・수로/호스트 정보・현재/이전 수면/수심과 QCHANV/QCHANVT・상호작용 계수를 출력(243–245). 두 내부 조건 종료 뒤에도 NMD 루프 안에서 8004 라벨을 출력(246–248). 루프・MDCHH 조건 종료(249–250). |
| 252–280 | 시작 시 9행 NEGDEP 루틴 안. 장치 1을 닫고 OUTDIR//'EQTERM.OUT'을 열어 DELETE로 닫은 뒤 APPEND로 재개방(252–255). 반복 수/단계 수준을 쓰고 `do L = 2,LA` (257)에서 셀 I/J・SUB/SVB・HRUO/HRVO・HU/HV를 출력하고 파일 닫음(256–260). `if( ISINWV == 1 )then` (262)이면 OUTDIR//'CFLMAX.OUT'을 열어 DELETE/재개방(263–265), `do L = 2,LA` (266)에서 K=1..KC의 CFLUUU/CFLWWW/CFLCAC/CFLVVV를 출력・닫음(267–272). 오류 파일 닫음(275). 전처리기 `#ifdef GNU` (276)는 `STOP 'ABORTING RUN DUE TO NEGATIVE DEPTHS'` (277), `#else` (278)는 `ERROR STOP('ABORTING RUN DUE TO NEGATIVE DEPTHS')` (279), `#endif` (280). 이 파일을 실행한 기록은 작성하지 않았다. |
| 281–311 | 시작 시 9행 NEGDEP 루틴 안. 출력 FORMAT 1001/1002는 정수+지수 형식, 1991/1992는 층별 12개 F8.3 반복 형식(282–285). 1111은 중심 수심 진단의 시간・반복/단계/셀/프로세스 표제이고 1112/1113은 서/남 면 표제(286–290). 6060–6068은 수심・면 수심・순유입・강우/증발・마스크・얼음/열 상태, 6069는 파일/EE 저장 안내 형식(291–303). 8001/8002/8003은 수로 정보 수치 형식, 8000/8004는 수로 머리말/유량 이름(304–308). 빈 줄・`END` (310)・마지막 빈 줄(311). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 37–51: OpenMP 루프는 INEGFLG를 SHARED로 사용한다. PRIVATE 목록은 ND/LF/LL/L이다(40). HP<=0인 각 스레드는 INEGFLG=1을 쓴다(45–46). 이 병렬 블록에 ATOMIC・CRITICAL・REDUCTION 지시문은 없다.
- 45・53–63・175–194: 첫 점검과 개수 집계는 HP<=0을 사용하여 수심 0도 포함한다. INEGFLG=0이면 즉시 return한다(53–54). 음수 HU/HV의 면 점검은 이 return 뒤에 있다(175–194).
- 176–178・186・289–290: HU 조건과 HV 조건을 OR로 묶은 분기는 둘 다 1112(서쪽 면) 형식을 출력한다. 1113(남쪽 면) 형식은 선언되어 있지만 이 파일의 WRITE에서 사용하지 않는다.
- 161–162: FXVEGE X/Y 로그의 앞 두 값은 모두 FXVEGE(L)이다(161). RCX/RCY 로그는 L의 X・L의 Y・LE의 X・LN의 Y 순서로 식을 출력한다(162).
- 101–109・169–170: 앞쪽 CWESN 진단 값은 L,LW,LE,LS,LN 순서이다. 얼음 두께의 라벨도 CWESN이지만 값은 L,LE,LW,LS,LN 순서이다(169–170).
- 224–245・307–308: X 수로는 첫 값으로 N과 이전 압력 P1을 출력한다(228–229). Y 수로는 NITER와 계산된 SRFCHAN1/SRFHOST1을 출력한다(243–244). 8000의 표제는 NITER・P1이고, 8004의 유량 라벨은 U 방향 이름만 적는다(307–308).
- 35・226–229: SURFTMP는 선언 뒤 이 파일에 사용되지 않는다. X 수로에서 계산한 SRFCHAN1/SRFHOST1은 해당 X 로그 인수에 쓰이지 않는다. Y 수로는 이 변수들을 다시 계산하여 로그 인수에 쓴다(241–244).
- 252–280: EQTERM.OUT은 삭제 후 재생성한다. ISINWV=1이면 CFLMAX.OUT도 삭제 후 재생성한다. 종료 경로는 GNU의 STOP 또는 그 밖의 ERROR STOP이다. 이 판독에서는 해당 입출력과 종료를 실행하지 않았다.
