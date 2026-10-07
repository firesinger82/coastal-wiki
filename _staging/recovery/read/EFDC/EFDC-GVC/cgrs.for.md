---
file: models/EFDC/raw/source_code/EFDC-GVC/cgrs.for
lines: 251
sha256: fea02f82db452298af23c9f8e9f73c5edb6e8225b021b3814ec91c23d33dea65
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# cgrs.for — 판독 구간 기록

구간은 1행부터 251행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–42 | 구분 주석과 `SUBROUTINE CGRS (ISTL)` 입구(6). 적색·흑색 순서(red/black ordering)의 축소 시스템(reduced system) 공액기울기법(conjugate gradient scheme)으로 외부 모드(external mode)를 푼다는 설명(19–20). `EFDC.PAR`·`EFDC.CMN` 포함(24–25). 지역 배열 선언은 주석 처리(27–30). ISCRAY=0이면 SECNDS, ELSE(36)는 SECOND와 `CALL TIMEF(WT1TMP)`로 시작 시각을 구한다(34–39). 원문: `IF(ISCRAY.EQ.0)THEN` (34). |
| 43–76 | 시작 시 6행 CGRS 루틴 안. ISTL=2이면 L=1..LC의 CCSR·CCWR·CCER·CCNR·CCSB·CCWB·CCEB·CCNB를 CG 계수에 복사한다(43–53). ELSE(54)는 CSR·CWR·CER·CNR·CSB·CWB·CEB·CNB를 복사한다(55–65). 적색 L=1..NRC의 흑색 이웃 LN·LS·LE·LW를 구하고 FPR에서 흑색 FPB의 네 계수곱을 뺀 FPRT를 만든다(67–74). 원문: `IF(ISTL.EQ.2)THEN` (43); `DO L=1,LC` (44); `DO L=1,LC` (55); `DO L=1,NRC` (67); `FPRT(L)=FPR(L)-CGSR(L)*FPB(LS)-CGWR(L)*FPB(LW)` (72); `&              -CGER(L)*FPB(LE)-CGNR(L)*FPB(LN)` (73). |
| 77–114 | 시작 시 6행 CGRS 루틴 안. LRC·LBC로 원래 P를 PRED·PBLK에 각각 복사한다(80–88). L=1..NBC에서 적색 이웃 PRED의 계수곱을 PBTMP에 저장한다(92–99). L=1..NRC에서 축소 시스템 잔차(residual) RSD를 계산하고 RCG·PCG=-RSD로 시작한다(101–110). ITER=0(112). 원문: `DO LR=1,NRC` (80); `DO LB=1,NBC` (85); `DO L=1,NBC` (92); `PBTMP(L)=CGSB(L)*PRED(LS)+CGWB(L)*PRED(LW)` (97); `&        +CGEB(L)*PRED(LE)+CGNB(L)*PRED(LN)` (98); `DO L=1,NRC` (101); `RSD=PRED(L)-CGSR(L)*PBTMP(LS)-CGWR(L)*PBTMP(LW)` (106); `&           -CGER(L)*PBTMP(LE)-CGNR(L)*PBTMP(LN)-FPRT(L)` (107); `RCG(L)=-RSD` (108); `PCG(L)=-RSD` (109). |
| 115–152 | 시작 시 6행 CGRS 루틴 안. 100번 표지에서 ITER를 증가시킨다(116–118). 흑색 L=1..NBC에서 PCG 계수곱을 PBTMP에 계산한다(120–127). 적색 L=1..NRC에서 PCG와 흑색 이웃 PBTMP를 이용해 APCG를 만든다(129–136). PAPCG·RPCG=0에서 APCG×PCG와 RCG×PCG를 누적하고 ALPHA=RPCG/PAPCG로 PRED를 갱신한다(138–150). 원문: `ITER=ITER+1` (118); `DO L=1,NBC` (120); `PBTMP(L)=CGSB(L)*PCG(LS)+CGWB(L)*PCG(LW)` (125); `&        +CGEB(L)*PCG(LE)+CGNB(L)*PCG(LN)` (126); `DO L=1,NRC` (129); `APCG(L)=PCG(L)-CGSR(L)*PBTMP(LS)-CGWR(L)*PBTMP(LW)` (134); `&              -CGER(L)*PBTMP(LE)-CGNR(L)*PBTMP(LN)` (135); `DO L=1,NRC` (141); `PAPCG=PAPCG+APCG(L)*PCG(L)` (142); `RPCG=RPCG+RCG(L)*PCG(L)` (143); `ALPHA=RPCG/PAPCG` (146); `DO L=1,NRC` (148); `PRED(L)=PRED(L)+ALPHA*PCG(L)` (149). |
| 153–186 | 시작 시 6행 CGRS 루틴 안. RCG-=ALPHA×APCG 뒤 적색 잔차 제곱합 RSQ를 계산한다(154–162). RSQ<=RSQM이면 200번 표지로 이동한다(164). 수렴하지 않고 ITER>=ITERM이면 오류 출력·STOP(166–169). BETA는 RCG×APCG의 음수 합/PAPCG이다(171–177). PCG=RCG+BETA×PCG로 탐색 방향(search direction)을 갱신하고 GOTO 100(179–183). 원문: `DO L=1,NRC` (156); `RCG(L)=RCG(L)-ALPHA*APCG(L)` (157); `DO L=1,NRC` (160); `RSQ=RSQ+RCG(L)*RCG(L)` (161); `IF(RSQ .LE. RSQM) GOTO 200` (164); `IF(ITER .GE. ITERM)THEN` (166); `DO L=1,NRC` (173); `BETA=BETA+RCG(L)*APCG(L)` (174); `BETA=-BETA/PAPCG` (177); `DO L=1,NRC` (179); `PCG(L)=RCG(L)+BETA*PCG(L)` (180). |
| 187–224 | 시작 시 6행 CGRS 루틴 안. 200번 표지에서 흑색 PBLK를 FPB-적색 이웃 PRED의 네 계수곱으로 복원한다(189–198). RSQ=0에서 흑색 원 시스템 잔차와 적색 원 시스템 잔차의 제곱을 각각 더한다(200–220). 원문: `DO L=1,NBC` (191); `PBLK(L)=FPB(L)-CGSB(L)*PRED(LS)-CGWB(L)*PRED(LW)` (196); `&              -CGEB(L)*PRED(LE)-CGNB(L)*PRED(LN)` (197); `DO L=1,NBC` (202); `RSD=PBLK(L)+CGSB(L)*PRED(LS)+CGWB(L)*PRED(LW)` (207); `&           +CGEB(L)*PRED(LE)+CGNB(L)*PRED(LN)-FPB(L)` (208); `RSQ=RSQ+RSD*RSD` (209); `DO L=1,NRC` (212); `RSD=PRED(L)+CGSR(L)*PBLK(LS)+CGWR(L)*PBLK(LW)` (217); `&           +CGER(L)*PBLK(LE)+CGNR(L)*PBLK(LN)-FPR(L)` (218); `RSQ=RSQ+RSD*RSD` (219). |
| 225–251 | 시작 시 6행 CGRS 루틴 안. LR=1..NRC·LB=1..NBC에서 PRED·PBLK를 LRC·LBC에 따라 원래 P에 복사한다(227–235). ISCRAY=0이면 SECNDS 경과 시간을 TCGRS에 더한다(237–238). ELSE(239)는 SECOND와 `CALL TIMEF(WT2TMP)`로 TCGRS·WTCGRS를 계산한다(240–243). 오류 FORMAT·RETURN·END(248–251). 원문: `DO LR=1,NRC` (227); `DO LB=1,NBC` (232); `IF(ISCRAY.EQ.0)THEN` (237); `TCGRS=TCGRS+SECNDS(TTMP)` (238); `TCGRS=TCGRS+T2TMP-T1TMP` (242); `WTCGRS=WTCGRS+(WT2TMP-WT1TMP)*0.001` (243). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 80–110·120–136·191–219: PRED·PBLK·PBTMP·PCG 값을 쓰는 셀 루프는 각각 1..NRC 또는 1..NBC이다. 이웃 매핑이 가리키는 범위를 검사하거나 NRC+1·NBC+1 원소를 이 파일에서 별도로 초기화하는 문장은 없다.
- 106–118·146·164: 초기 잔차의 수렴 검사는 첫 반복 전에 없다. PAPCG=0인지 검사하지 않고 ALPHA=RPCG/PAPCG를 계산한다.
- 160–164·200–219: 반복 종료 판단은 적색 RCG 제곱합을 사용한다. 종료 후 RSQ는 흑색과 적색의 원 시스템 잔차 제곱합으로 다시 계산한다.
- 177: BETA=-BETA/PAPCG를 계산하기 전에 PAPCG의 0 여부를 검사하는 조건은 없다.

