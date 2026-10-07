---
file: models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/MPI_Domain_Decomp/Congrad_MPI.f90
lines: 194
sha256: 9cdcd8d2ba9f9b9be958853ffb7848375dcf26f07fc25c9567ea4252a2dcc9fe
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Congrad_MPI.f90 — 판독 구간 기록

구간은 1행부터 194행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–47 | EFDC+·저작권·GPLv2 머리말과 수정 공액경사법(conjugate gradient method)·작성자·날짜 주석(1–15). `CONGRAD_MPI()`를 시작한다(17). GLOBAL·EFDCOUT·MPI·MPI 변수·고스트 셀(ghost cell) 통신·전체 축약(all-reduce)·매핑·EE 이진 출력 모듈을 사용한다(19–29). 인수 선언은 주석이다(31). 정수·기본 real의 ALPHA/BETA·내적·잔차와 real(8)의 축약 결과·시간 변수를 선언한다(34–42). PCG·RCG·TMPCG는 save allocatable 실수 1차원 배열이다(44–46). |
| 48–87 | 시작 시 17행 CONGRAD_MPI 안. `if( .not. allocated(PCG) )then` (48)이면 PCG·RCG·TMPCG를 LCM 크기로 할당하고 0으로 초기화한다(49–55). 시작 시간 저장과 통신·축약 시간 0 초기화(59–61). L=2..LA에서 `RCG(L) = FPTMP(L) - CCC(L)*P(L) - CCN(L)*P(LNC(L)) - CCS(L)*P(LSC(L)) - CCW(L)*P(LWC(L)) - CCE(L)*P(LEC(L))` (64), `PCG(L) = RCG(L)*CCCI(L)` (68). `Communicate_1D2(RCG, PCG)` 호출(73) 뒤 `TMPCOMM = TMPCOMM + (DSTIME(0)-TTDS2)` (74). RPCG=0(76) 후 L=2..LA에서 `RPCG = RPCG + GhostMask(L)*RCG(L)*PCG(L)` (78). `DSI_All_Reduce(RPCG, RPCG_OUT, MPI_SUM, TTDS, 0, TWAIT)`를 호출한다(82). `TMPALLREDUCE = TMPALLREDUCE + TTDS` (83), 축약 결과 복사(84). `if( RPCG == 0.0 ) return   ! *** DSI SINGLE LINE` (86). 빈 줄을 포함한다. |
| 88–110 | 시작 시 17행 CONGRAD_MPI 안. 반복해법 주석 뒤 `do ITER = 1,ITERM` (90). PAPCG·RPCGN·RSQ=0(92–94). L=2..LA에서 `APCG(L) = CCC(L)*PCG(L) + CCS(L)*PCG(LSC(L)) + CCN(L)*PCG(LNC(L)) + CCW(L)*PCG(LWC(L)) + CCE(L)*PCG(LEC(L))` (97). 별도 같은 범위 루프에서 `PAPCG = PAPCG + GhostMask(L)*APCG(L)*PCG(L)` (101). `DSI_All_Reduce(PAPCG, PAPCG_OUT, MPI_SUM, TTDS, 0, TWAIT)`를 호출한다(105). `TMPALLREDUCE = TMPALLREDUCE + TTDS` (106), 결과 복사(107), `ALPHA = RPCG/PAPCG` (109). |
| 111–137 | 시작 시 17행 CONGRAD_MPI·90행 ITER 루프 안. L=2..LA에서 `P(L)     = P(L) + ALPHA*PCG(L)` (113), `RCG(L)   = RCG(L) - ALPHA*APCG(L)` (114), `TMPCG(L) = CCCI(L)*RCG(L)` (115). 별도 L 루프에서 `RPCGN = RPCGN + GhostMask(L)*RCG(L)*TMPCG(L)` (119), 또 다른 L 루프에서 `RSQ   = RSQ   + GhostMask(L)*RCG(L)*RCG(L)` (123). RPCGN·RSQ를 각각 MPI_SUM·iWait=0으로 DSI_All_Reduce에 전달한다(127·131). `TMPALLREDUCE = TMPALLREDUCE + TTDS` (128·132) 후 결과를 기본 real 변수에 복사한다(129·133). `BETA = RPCGN/RPCG` (135), RPCG=RPCGN 복사(136). |
| 138–156 | 시작 시 17행 CONGRAD_MPI·90행 ITER 루프 안. `if( RSQ > RSQM )then` (138)일 때 L=2..LA에서 `PCG(L) = TMPCG(L) + BETA*PCG(L)` (141). 별도 `if( RSQ <= RSQM )then` (146)은 반복 루프를 exit한다(147). exit하지 않은 경로는 `MPI_barrier(DSIcomm, IERR)`를 호출한다(150). 시작 시간 저장 뒤 `Communicate_Ghost_Cells(PCG, 'PCG')`를 호출하고 `TMPCOMM = TMPCOMM + (DSTIME(0)-TTDS2)` (153)를 누적한다. ITER 루프 종료와 빈 줄(155–156). |
| 157–187 | 시작 시 17행 CONGRAD_MPI 안이며 ITER 루프 밖. `if( RSQ > RSQM )then` (157)일 때 `L = MAXLOC(RCG,DIM = 1 )` (158). 전역 셀 번호·process_id를 화면과 STATUS='OLD' 오류 파일에 출력한다(159–163). L=2..LA의 전역·지역 셀 번호·격자 인덱스·행렬 계수·우변·잔차를 기록하고 파일을 닫는다(165–169). `if( ISPPH == 1 )then` (172) 안에서 저장 안내를 출력하고 `Map_Write_EE_Binary`를 호출한다(173–174). 그 안 `if( process_id == master_id )then` (175)은 `EE_LINKAGE(-1)`을 호출한다(176). ISPPH 조건 밖이지만 RSQ>RSQM 분기 안에서 `STOPP('')`를 호출한다(180). 최대 반복 초과·열 제목·수치 출력 FORMAT을 정의한다(182–184). 조건 종료와 빈 줄(186–187). |
| 188–194 | 시작 시 17행 CONGRAD_MPI 안이며 비수렴 조건 밖. `TCONG = TCONG + (DSTIME(0)-TTDS1) - TMPCOMM - TMPALLREDUCE` (188)로 통신·축약 시간을 뺀 해법 시간을 누적한다. `DSITIMING(1)  = DSITIMING(1)  + TMPCOMM` (189), `DSITIMING(12) = DSITIMING(12) + TMPALLREDUCE` (190). return·빈 줄·루틴 종료(191–194). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 34: ND·LL·LF·LE·LS·LN·LW·I·J는 선언 이후 사용되지 않는다.
- 38–39·82–84·105–107·127–133: 축약 출력은 real(8)이다. 출력값은 기본 real인 RPCG·PAPCG·RPCGN·RSQ에 다시 대입된다.
- 59–86·188–190: RPCG==0.0의 return은 TCONG와 DSITIMING 누적 앞에 있다.
- 105–109·135: ALPHA는 PAPCG로 나누고 BETA는 RPCG로 나눈다. 해당 대입 바로 앞에는 두 분모의 0 검사 문장이 없다. 초기 RPCG 검사만 86행에 있다.
- 90–94·157: RSQ의 초기화는 ITER 루프 안에 있다. 이 파일에는 ITERM이 양수인지 확인하는 분기가 없다. 루프 뒤에는 RSQ를 비교하는 문장이 있다.
- 158–159·166–167: 오류 위치는 RCG 전체 배열의 MAXLOC로 선택한다. 이 호출은 abs(RCG)를 사용하지 않으며 L=2..LA로 배열 슬라이스를 제한하지 않는다.
- 145–153: 수렴 exit는 MPI_barrier와 PCG 고스트 셀 통신 앞에 있다. barrier 호출 시간은 그 뒤 시작하는 TTDS2 기반 TMPCOMM 측정에 포함하지 않는다.
