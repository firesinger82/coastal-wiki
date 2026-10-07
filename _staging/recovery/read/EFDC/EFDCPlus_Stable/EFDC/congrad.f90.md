---
file: models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/congrad.f90
lines: 225
sha256: 950215f319eb006fa251b589715520c983ee8de941049a2c6c9c720950731b8e
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# congrad.f90 — 판독 구간 기록

구간은 1행부터 225행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–55 | EFDC+ 저작권·GPLv2·주소와 CONGRAD 입구(1–9). 주석은 켤레기울기법(conjugate gradient scheme)으로 외부 모드(external mode)를 푼다고 적는다(11). F90/OpenMP 변경 이력, GLOBAL·EFDCOUT·할당·MPI 출력 모듈을 포함한다(13–25). 지역 변수·DSTIME·SAVE 작업 및 보고 배열을 선언한다(27–43). PCG 미할당 시 PCG/RCG/TMPCG는 LCM·0으로, ALPHAs/BETAs/RPCGs는 ITERM+1·0으로, RSQs는 ITERM+1·−1로 할당한다(45–55). 원문(조건·반복·대입·호출, 등장 순서): `if( .not. allocated(PCG) )then` (45); `call AllocateDSI(PCG,   LCM, 0.0)` (46); `call AllocateDSI(RCG,   LCM, 0.0)` (47); `call AllocateDSI(TMPCG, LCM, 0.0)` (48); `call AllocateDSI(ALPHAs, ITERM+1,  0.0)` (51); `call AllocateDSI(BETAs,  ITERM+1,  0.0)` (52); `call AllocateDSI(RPCGs,  ITERM+1,  0.0)` (53); `call AllocateDSI(RSQs,   ITERM+1, -1.0)` (54). |
| 56–91 | 시작 시 9행 `SUBROUTINE CONGRAD` 루틴 안. DSTIME으로 시작 시각을 저장한다(58). NOPTIMAL(0)개 OpenMP 스레드의 ND 분할에서 FPTMP−A×P로 초기 잔차(residual) RCG를 계산한다(60–71). CCCI를 곱해 대각 전처리(diagonal preconditioning) PCG를 만든다(73–75). 보고 배열을 다시 0 또는 −1로 초기화한다(79–83). L=2..LA의 RCG×PCG 합이 초기 RPCG다(85–88). RPCG=0이면 즉시 RETURN한다(90). 원문(조건·반복·대입·호출, 등장 순서): `TTDS = DSTIME(0)` (58); `do ND = 1,NOPTIMAL(0)` (61); `LF = 2+(ND-1)*LDMOPT(0)` (62); `LL = min(LF+LDMOPT(0)-1,LA)` (63); `do L = LF,LL` (65); `LN = LNC(L)` (66); `LS = LSC(L)` (67); `LE = LEC(L)` (68); `LW = LWC(L)` (69); `RCG(L) = FPTMP(L) - CCC(L)*P(L) - CCN(L)*P(LN) - CCS(L)*P(LS) - CCW(L)*P(LW) - CCE(L)*P(LE)` (70); `do L = LF,LL` (73); `PCG(L) = RCG(L)*CCCI(L)` (74); `ALPHAs = 0.` (80); `BETAS = 0.` (81); `RPCGs = 0.` (82); `RSQs = -1.` (83); `RPCG = 0.` (85); `do L = 2,LA` (86); `RPCG = RPCG + RCG(L)*PCG(L)` (87); `if( RPCG == 0.0 ) return   ! *** DSI SINGLE LINE` (90). |
| 92–123 | 시작 시 9행 `SUBROUTINE CONGRAD` 루틴 안. ITER=1..ITERM의 반복을 연다(93). OpenMP 병렬 영역은 PAPCG를 PRIVATE로 선언하고 계수·해·잔차·보고 배열을 공유한다(95–97). ND 분할에서 중앙·남북·동서 계수와 PCG로 APCG=A×PCG를 계산한다(100–112). SINGLE에서 L=2..LA의 APCG×PCG를 합산하고 ALPHA=RPCG/PAPCG를 계산해 보고 배열에 저장한다(115–122). 주석은 합산을 영역 루프 밖으로 빼서 반올림 오차(roundoff error)를 방지한다고 적는다(114). 원문(조건·반복·대입·호출, 등장 순서): `do ITER = 1,ITERM` (93); `do ND = 1,NOPTIMAL(0)` (100); `LF = 2+(ND-1)*LDMOPT(0)` (101); `LL = min(LF+LDMOPT(0)-1,LA)` (102); `do L = LF,LL` (104); `LN = LNC(L)` (105); `LS = LSC(L)` (106); `LE = LEC(L)` (107); `LW = LWC(L)` (108); `APCG(L) = CCC(L)*PCG(L) + CCS(L)*PCG(LS) + CCN(L)*PCG(LN) + CCW(L)*PCG(LW) + CCE(L)*PCG(LE)` (109); `PAPCG = 0.` (116); `do L = 2,LA` (117); `PAPCG = PAPCG + APCG(L)*PCG(L)` (118); `ALPHA = RPCG/PAPCG` (120); `ALPHAS(ITER) = ALPHA` (121). |
| 124–175 | 시작 시 9행 `SUBROUTINE CONGRAD` 루틴·93행 `do ITER = 1,ITERM` 루프 안. ND 분할에서 P에 ALPHA×PCG를 더하고 RCG에서 ALPHA×APCG를 뺀 뒤 CCCI×RCG로 TMPCG를 만든다(125–135). SINGLE에서 RPCGN=RCG·TMPCG 합과 RSQ=RCG² 합을 계산한다(138–144). BETA=RPCGN/RPCG·RPCG 갱신·첫 반복의 RSQ0=RSQ×1.E−6을 수행하고 보고 값을 저장한다(145–154). RSQ>RSQM이면 PCG=TMPCG+BETA×PCG를 만든다(156–168). 병렬 영역 종료 뒤 RSQ≤RSQM이면 반복에서 EXIT한다(169–175). 원문(조건·반복·대입·호출, 등장 순서): `do ND = 1,NOPTIMAL(0)` (125); `LF = 2+(ND-1)*LDMOPT(0)` (126); `LL = min(LF+LDMOPT(0)-1,LA)` (127); `do L = LF,LL` (129); `P(L)      = P(L) + ALPHA*PCG(L)` (130); `RCG(L)    = RCG(L) - ALPHA*APCG(L)` (131); `TMPCG(L)  = CCCI(L)*RCG(L)` (132); `RPCGN = 0.` (139); `RSQ = 0.` (140); `do L = 2,LA` (141); `RPCGN = RPCGN + RCG(L)*TMPCG(L)` (142); `RSQ   = RSQ   + RCG(L)*RCG(L)` (143); `BETA = RPCGN/RPCG` (145); `RPCG = RPCGN` (146); `if( ITER == 1 ) RSQ0 = RSQ*1.E-6` (147); `BETAS(ITER) = BETA` (150); `RPCGS(ITER) = RPCG` (151); `RSQs(ITER) = RSQ` (152); `if( RSQ > RSQM )then` (156); `do ND = 1,NOPTIMAL(0)` (159); `LF = 2+(ND-1)*LDMOPT(0)` (160); `LL = min(LF+LDMOPT(0)-1,LA)` (161); `do L = LF,LL` (163); `PCG(L) = TMPCG(L)+BETA*PCG(L)` (164); `if( RSQ <= RSQM )then` (171). |
| 176–212 | 시작 시 9행 `SUBROUTINE CONGRAD` 루틴 안. 반복 뒤 RSQ>RSQM이면 최대 반복 초과를 처리한다(177). MAXLOC(RCG) 셀의 전역 번호와 프로세스를 출력한다(179–180). ITER를 ITERM 이하로 제한하고 CONGRAD.ERR에 반복별 ALPHA/BETA/RPCG/RSQ 이력을 쓴다(183–190). 프로세스별 mpi_error_file에는 계수·우변·잔차를 출력한다(193–200). ISPPH=1이면 Map_Write_EE_Binary를 호출하고 master_id만 EE_LINKAGE(−1)를 호출한다(203–209). STOPP('')를 호출한다(211). 원문(조건·반복·대입·호출, 등장 순서): `if( RSQ > RSQM )then` (177); `L = MAXLOC(RCG,DIM = 1)` (179); `ITER = min(ITER,ITERM)` (183); `do LF = 1,ITER` (187); `do L = 2,LA` (197); `if( ISPPH == 1 )then` (203); `call Map_Write_EE_Binary` (205); `if( process_id == master_id )then` (206); `call EE_LINKAGE(-1)` (207); `call STOPP('')` (211). |
| 213–225 | 시작 시 9행 `SUBROUTINE CONGRAD` 루틴·177행 `if( RSQ > RSQM )then` 분기 안. 오류 메시지·표 머리말·데이터 FORMAT 선언을 포함한다(213–216). 최대 반복 초과 분기를 닫는다(218). TCONG에 DSTIME−시작 시각을 더한다(220). RETURN·END 및 마지막 빈 줄로 끝난다(222–225). 원문(조건·반복·대입·호출, 등장 순서): `TCONG = TCONG + (DSTIME(0)-TTDS)` (220). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 29–30·147: RSQ0는 첫 반복에 RSQ*1.E-6을 대입한다. 이 파일에는 그 값을 비교하거나 계산에 쓰는 문장이 없다. PMC/PMC2도 선언 이후 사용되지 않는다.
- 58·90·220: 초기 RPCG=0 경로는 바로 RETURN한다. 이 경로는 끝의 TCONG 시간 누적 문장을 실행하지 않는다.
- 90·120·145: 초기 RPCG=0 검사는 있다. ALPHA의 PAPCG 분모 및 반복 중 BETA의 RPCG 분모를 0과 비교하는 조건은 이 파일에 없다.
- 179: 최대 오류 위치 선택은 MAXLOC(RCG,DIM=1)이다. 이 호출은 ABS(RCG) 또는 RCG²를 인수로 사용하지 않는다.
- 177–190·192–194: 반복 이력 출력 경로는 모든 프로세스에서 OUTDIR//'CONGRAD.ERR'라는 같은 문자열이다. 후속 상세 로그 경로는 프로세스별 mpi_error_file이다.
- 198·214–216: 상세 데이터 write는 정수 4개와 실수 7개(CCS·CCW·CCC·CCE·CCN·FPTMP·RCG)를 전달한다. FORMAT 머리말에는 RCG^2·P·RCG·TMPCG·PCG도 적혀 있다. 데이터 FORMAT은 4I6,12E13.4다.
