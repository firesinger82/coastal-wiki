---
file: models/EFDC/raw/source_code/EFDC-GVC/congrad.for
lines: 177
sha256: f0d757883358391a33e141fcd39cb11a1e0cc0be22a9da7bb1e242ae6400c8ad
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# congrad.for — 판독 구간 기록

구간은 1행부터 177행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–29 | 구분 주석과 `SUBROUTINE CONGRAD (ISTL)` 입구(6). 외부 모드(external mode)를 공액기울기법(conjugate gradient scheme)으로 푼다는 설명(19–20). 버전·수정일·변경 기록 주석과 `EFDC.PAR`·`EFDC.CMN` 포함(8–25). PNORTH·PSOUTH·TMPCG는 각각 LCM 크기(27). |
| 30–44 | 시작 시 6행 CONGRAD 루틴 안. LA=2이면 P(L)=FPTMP(L)/CCC(L) 계산 후 RETURN한다(31–34). ISCRAY=0이면 SECNDS, ELSE(38)는 SECOND 및 `CALL TIMEF(WT1TMP)`로 시작 시각을 구한다(36–41). 원문: `IF(LA.EQ.2)THEN` (31); `P(L)=FPTMP(L)/CCC(L)` (32); `RETURN` (33); `ENDIF` (34); `IF(ISCRAY.EQ.0)THEN` (36). |
| 45–67 | 시작 시 6행 CONGRAD 루틴 안. L=2..LA의 북·남 P를 PNORTH·PSOUTH에 복사한다(45–48). FPTMP에서 CCC·CCN·CCS·CCW·CCE의 P 계수곱을 빼 RCG를 계산한다(50–53). 대각 전처리(diagonal preconditioning) PCG=RCG×CCCI와 RPCG=ΣRCG×PCG를 계산한다(55–62). ITER=0(64). 원문: `DO L=2,LA` (45); `PNORTH(L)=P(LNC(L))` (46); `PSOUTH(L)=P(LSC(L))` (47); `DO L=2,LA` (50); `RCG(L)=FPTMP(L)-CCC(L)*P(L)-CCN(L)*PNORTH(L)-CCS(L)*PSOUTH(L)` (51); `&        -CCW(L)*P(L-1)-CCE(L)*P(L+1)` (52); `DO L=2,LA` (55); `PCG(L)=RCG(L)*CCCI(L)` (56); `DO L=2,LA` (60); `RPCG=RPCG+RCG(L)*PCG(L)` (61). |
| 68–94 | 시작 시 6행 CONGRAD 루틴 안. 100번 표지에서 ITER를 증가시킨다(68–70). 북·남 PCG를 복사하고 계수 행렬(matrix)과 PCG의 곱 APCG를 만든다(72–80). PAPCG=ΣAPCG×PCG, ALPHA=RPCG/PAPCG로 계산한 뒤 P+=ALPHA×PCG로 갱신한다(82–92). 원문: `ITER=ITER+1` (70); `DO L=2,LA` (72); `PNORTH(L)=PCG(LNC(L))` (73); `PSOUTH(L)=PCG(LSC(L))` (74); `DO L=2,LA` (77); `APCG(L)=CCC(L)*PCG(L)+CCS(L)*PSOUTH(L)+CCN(L)*PNORTH(L)` (78); `&       +CCW(L)*PCG(L-1)+CCE(L)*PCG(L+1)` (79); `DO L=2,LA` (84); `PAPCG=PAPCG+APCG(L)*PCG(L)` (85); `ALPHA=RPCG/PAPCG` (88); `DO L=2,LA` (90); `P(L)=P(L)+ALPHA*PCG(L)` (91). |
| 95–124 | 시작 시 6행 CONGRAD 루틴 안. RCG-=ALPHA×APCG와 TMPCG=CCCI×RCG를 계산한다(96–102). RPCGN=ΣRCG×TMPCG, RSQ=ΣRCG²(104–109). RSQ<=RSQM이면 200번 표지로 이동한다(111). 수렴하지 않고 ITER>=ITERM이면 오류를 출력하고 L=1..LC의 계수합 CDIADOM 및 계수·FPTMP·HU·HV를 장치 8에 기록한다(113–119). CLOSE(8), `CALL RESTOUT(1)`, STOP(120–123). 원문: `DO L=2,LA` (96); `RCG(L)=RCG(L)-ALPHA*APCG(L)` (97); `DO L=2,LA` (100); `TMPCG(L)=CCCI(L)*RCG(L)` (101); `DO L=2,LA` (106); `RPCGN=RPCGN+RCG(L)*TMPCG(L)` (107); `RSQ=RSQ+RCG(L)*RCG(L)` (108); `IF(RSQ .LE. RSQM) GOTO 200` (111); `IF(ITER .GE. ITERM)THEN` (113); `DO L=1,LC` (115); `CDIADOM=CCC(L)+CCE(L)+CCN(L)+CCS(L)+CCW(L)` (116). |
| 125–137 | 시작 시 6행 CONGRAD 루틴 안. BETA=RPCGN/RPCG를 계산하고 RPCG=RPCGN으로 복사한다(125–126). PCG=TMPCG+BETA×PCG를 L=2..LA에서 갱신하고 GOTO 100으로 반복한다(128–132). 최대 반복 횟수 오류 FORMAT(134). 원문: `BETA=RPCGN/RPCG` (125); `DO L=2,LA` (128); `PCG(L)=TMPCG(L)+BETA*PCG(L)` (129). |
| 138–163 | 시작 시 6행 CONGRAD 루틴 안. 200번 표지에서 최종 P의 북·남 이웃을 다시 복사한다(140–145). RSQ=0으로 시작하여 계수 행렬×P-FPTMP를 RCG에 계산하고 CCCI를 곱한다(147–157). 그 RCG 제곱합을 RSQ로 저장한다(158–160). 원문: `DO L=2,LA` (142); `PNORTH(L)=P(LNC(L))` (143); `PSOUTH(L)=P(LSC(L))` (144); `DO L=2,LA` (150); `RCG(L)=CCC(L)*P(L)+CCS(L)*PSOUTH(L)+CCN(L)*PNORTH(L)` (151); `&        +CCW(L)*P(L-1)+CCE(L)*P(L+1)-FPTMP(L)` (152); `DO L=2,LA` (155); `RCG(L)=RCG(L)*CCCI(L)` (156); `DO L=2,LA` (158); `RSQ=RSQ+RCG(L)*RCG(L)` (159). |
| 164–177 | 시작 시 6행 CONGRAD 루틴 안. ISCRAY=0이면 SECNDS 경과 시간을 TCONG에 더한다(164–165). ELSE(166)는 SECOND 및 `CALL TIMEF(WT2TMP)`로 TCONG·WTCONG를 갱신한다(167–170). 800·808 FORMAT·RETURN·END(173–177). 원문: `IF(ISCRAY.EQ.0)THEN` (164); `TCONG=TCONG+SECNDS(TTMP)` (165); `TCONG=TCONG+T2TMP-T1TMP` (169); `WTCONG=WTCONG+(WT2TMP-WT1TMP)*0.001` (170). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 31–34: LA=2 분기에서 P(L)를 사용한다. 이 루틴 입구에서 그 분기 이전에 L을 설정하는 실행문은 없다.
- 6: 인수 ISTL은 이 파일의 실행문에서 참조하지 않는다.
- 51–70·88·111·125: 첫 반복 전에 초기 잔차 수렴 검사가 없다. ALPHA와 BETA 계산 앞에 각각 PAPCG·RPCG의 0 여부를 검사하는 조건이 없다.
- 108–111·151–159: 반복 종료 판단의 RSQ는 전처리하지 않은 RCG² 합이다. 종료 뒤 RSQ는 (계수 행렬×P-FPTMP)×CCCI의 제곱합이다.
- 173–174·117: FORMAT 800은 이 파일의 WRITE에서 참조하지 않는다. 반복 초과 진단은 FORMAT 808을 사용한다.
