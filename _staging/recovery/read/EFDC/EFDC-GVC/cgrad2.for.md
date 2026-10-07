---
file: models/EFDC/raw/source_code/EFDC-GVC/cgrad2.for
lines: 244
sha256: ec60958845ac59f4bc1ee10c7b1934af2ad43ab4381a475cb787f0c152f9827f
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# cgrad2.for — 판독 구간 기록

구간은 1행부터 244행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–30 | 구분 주석과 `SUBROUTINE CGRAD2 (ISTL)` 입구(6). 외부 모드(external mode)를 영역 분할(domain decomposition) 병렬 공액기울기법(conjugate gradient scheme)으로 푼다는 설명(19–20). 버전·수정일·변경 기록 주석, `EFDC.PAR`·`EFDC.CMN` 포함(8–25). RSDTMP·RPCTMP·PAPTMP를 각각 길이 16으로 선언한다(27). |
| 31–63 | 시작 시 6행 CGRAD2 루틴 안. ISCRAY=0이면 SECNDS, ELSE(33)는 SECOND와 `CALL TIMEF(WT1TMP)`로 시작 시각을 구한다(31–36). ND=1..NDM의 세 부분합을 0으로 초기화한다(38–42). 영역 범위는 LF=2+(ND-1)×LDM, LL=LF+LDM-1이다(44–47·55–58). 이웃 P를 TVAR3S·W·E·N에 복사한 뒤 계수 CCC·CCS·CCW·CCE·CCN과 FPTMP로 잔차(residual) RCG를 계산한다(48–60). 원문: `IF(ISCRAY.EQ.0)THEN` (31); `DO ND=1,NDM` (38); `DO ND=1,NDM` (44); `LF=2+(ND-1)*LDM` (45); `LL=LF+LDM-1` (46); `DO L=LF,LL` (47); `TVAR3W(L)=P(L-1   )` (49); `TVAR3E(L)=P(L+1   )` (50); `DO ND=1,NDM` (55); `LF=2+(ND-1)*LDM` (56); `LL=LF+LDM-1` (57); `DO L=LF,LL` (58); `RCG(L)=-CCC(L)*P(L)-CCS(L)*TVAR3S(L)-CCW(L)*TVAR3W(L)` (59); `&               -CCE(L)*TVAR3E(L)-CCN(L)*TVAR3N(L)+FPTMP(L)` (60). |
| 64–82 | 시작 시 6행 CGRAD2 루틴 안. RPCG=0에서 시작한다(64). 각 영역의 L=LF..LL에서 대각 전처리(diagonal preconditioning) PCG=RCG×CCCI와 RCG²×CCCI 부분합을 만든다(66–73). ND 부분합을 RPCG에 더하고 ITER=0으로 시작한다(75–79). 원문: `DO ND=1,NDM` (66); `LF=2+(ND-1)*LDM` (67); `LL=LF+LDM-1` (68); `DO L=LF,LL` (69); `PCG(L)=RCG(L)*CCCI(L)` (70); `RPCTMP(ND)=RPCTMP(ND)+RCG(L)*RCG(L)*CCCI(L)` (71); `DO ND=1,NDM` (75); `RPCG=RPCG+RPCTMP(ND)` (76). |
| 83–112 | 시작 시 6행 CGRAD2 루틴 안. 100번 표지에서 ITER를 증가시키고 ND별 부분합을 0으로 초기화한다(83–91). PCG 이웃을 TVAR3에 저장하고 계수 행렬(matrix)과 PCG의 곱 APCG를 계산한다(93–111). 영역 범위와 이웃 관계는 초기 잔차 블록과 같다. 원문: `ITER=ITER+1` (85); `DO ND=1,NDM` (87); `DO ND=1,NDM` (93); `LF=2+(ND-1)*LDM` (94); `LL=LF+LDM-1` (95); `DO L=LF,LL` (96); `TVAR3W(L)=PCG(L-1   )` (98); `TVAR3E(L)=PCG(L+1   )` (99); `DO ND=1,NDM` (104); `LF=2+(ND-1)*LDM` (105); `LL=LF+LDM-1` (106); `DO L=LF,LL` (107); `APCG(L)=CCC(L)*PCG(L)+CCS(L)*TVAR3S(L)+CCW(L)*TVAR3W(L)` (108); `&       +CCE(L)*TVAR3E(L)+CCN(L)*TVAR3N(L)` (109). |
| 113–137 | 시작 시 6행 CGRAD2 루틴 안. ND별 APCG×PCG 합을 PAPTMP에 누적한다(113–119). PAPCG=0에서 영역 부분합을 모은다(121–124). ALPHA=RPCG/PAPCG로 계산하고 각 영역 P에 ALPHA×PCG를 더한다(126–134). 원문: `DO ND=1,NDM` (113); `LF=2+(ND-1)*LDM` (114); `LL=LF+LDM-1` (115); `DO L=LF,LL` (116); `PAPTMP(ND)=PAPTMP(ND)+APCG(L)*PCG(L)` (117); `DO ND=1,NDM` (122); `PAPCG=PAPCG+PAPTMP(ND)` (123); `ALPHA=RPCG/PAPCG` (126); `DO ND=1,NDM` (128); `LF=2+(ND-1)*LDM` (129); `LL=LF+LDM-1` (130); `DO L=LF,LL` (131); `P(L)=P(L)+ALPHA*PCG(L)` (132). |
| 138–174 | 시작 시 6행 CGRAD2 루틴 안. ND 부분합을 다시 0으로 설정한다(138–142). 각 영역에서 RCG를 RCG-ALPHA×APCG로 갱신하고 RCG²×CCCI 및 RCG²를 각각 RPCTMP·RSDTMP에 누적한다(144–159). RPCGN·RSQ를 영역 합으로 만든다(161–166). RSQ<=RSQM이면 200번 표지로 이동한다(168). 수렴하지 않고 ITER>=ITERM이면 오류 출력 후 STOP한다(170–173). 원문: `DO ND=1,NDM` (138); `DO ND=1,NDM` (144); `LF=2+(ND-1)*LDM` (145); `LL=LF+LDM-1` (146); `DO L=LF,LL` (147); `RCG(L)=RCG(L)-ALPHA*APCG(L)` (148); `DO ND=1,NDM` (152); `LF=2+(ND-1)*LDM` (153); `LL=LF+LDM-1` (154); `DO L=LF,LL` (155); `RPCTMP(ND)=RPCTMP(ND)+RCG(L)*RCG(L)*CCCI(L)` (156); `RSDTMP(ND)=RSDTMP(ND)+RCG(L)*RCG(L)` (157); `DO ND=1,NDM` (163); `RPCGN=RPCGN+RPCTMP(ND)` (164); `RSQ=RSQ+RSDTMP(ND)` (165); `IF(RSQ .LE. RSQM) GOTO 200` (168); `IF(ITER .GE. ITERM)THEN` (170). |
| 175–191 | 시작 시 6행 CGRAD2 루틴 안. BETA=RPCGN/RPCG를 계산하고 RPCG에 새 값을 복사한다(175–176). 각 영역 PCG=CCCI×RCG+BETA×PCG로 다음 탐색 방향(search direction)을 갱신한다(178–184). GOTO 100으로 반복한다(186). 최대 반복 횟수 오류 FORMAT(188). 원문: `BETA=RPCGN/RPCG` (175); `DO ND=1,NDM` (178); `LF=2+(ND-1)*LDM` (179); `LL=LF+LDM-1` (180); `DO L=LF,LL` (181); `PCG(L)=CCCI(L)*RCG(L)+BETA*PCG(L)` (182). |
| 192–219 | 시작 시 6행 CGRAD2 루틴 안. 200번 표지에서 ND별 RSDTMP=0으로 설정한다(194–198). 각 영역의 최종 P 이웃을 저장한다(200–209). (계수 행렬×P-FPTMP)×CCCI를 PCG에 저장한다(211–219). 원문: `DO ND=1,NDM` (196); `DO ND=1,NDM` (200); `LF=2+(ND-1)*LDM` (201); `LL=LF+LDM-1` (202); `DO L=LF,LL` (203); `TVAR3W(L)=P(L-1   )` (205); `TVAR3E(L)=P(L+1   )` (206); `DO ND=1,NDM` (211); `LF=2+(ND-1)*LDM` (212); `LL=LF+LDM-1` (213); `DO L=LF,LL` (214); `PCG(L)=( CCC(L)*P(L)+CCS(L)*TVAR3S(L)+CCW(L)*TVAR3W(L)` (215); `&                     +CCE(L)*TVAR3E(L)` (216); `&                     +CCN(L)*TVAR3N(L)-FPTMP(L) )*CCCI(L)` (217). |
| 220–244 | 시작 시 6행 CGRAD2 루틴 안. 영역별 PCG²를 RSDTMP에 누적하고 RSQ에 전체 합을 저장한다(221–232). ISCRAY=0이면 SECNDS 경과 시간을 TCONG에 더한다(234–235). ELSE(236)는 SECOND 및 `CALL TIMEF(WT2TMP)`를 사용하여 TCONG와 0.001 환산의 WTCONG를 갱신한다(237–240). RETURN·END(243–244). 원문: `DO ND=1,NDM` (221); `LF=2+(ND-1)*LDM` (222); `LL=LF+LDM-1` (223); `DO L=LF,LL` (224); `RSDTMP(ND)=RSDTMP(ND)+PCG(L)*PCG(L)` (225); `DO ND=1,NDM` (230); `RSQ=RSQ+RSDTMP(ND)` (231); `IF(ISCRAY.EQ.0)THEN` (234); `TCONG=TCONG+SECNDS(TTMP)` (235); `TCONG=TCONG+T2TMP-T1TMP` (239); `WTCONG=WTCONG+(WT2TMP-WT1TMP)*0.001` (240). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 27·38–41: RSDTMP·RPCTMP·PAPTMP의 선언 크기는 16이다. 접근 루프의 상한은 NDM이며 이 파일에는 NDM<=16 검사가 없다.
- 44–62·178–184: 영역 상한 LL은 LF+LDM-1이다. 영역 루프에는 LL을 LA로 제한하는 MIN이나 나머지 영역 분기가 없다.
- 6: 인수 ISTL은 이 파일의 실행문에서 참조하지 않는다.
- 64–79·126·168·175: 초기 잔차 수렴 검사는 반복 진입 전에 없다. ALPHA 계산은 RSQ 검사보다 먼저 실행한다. PAPCG·RPCG의 0 여부를 검사하는 조건이 없다.
- 156–168·215–231: 반복 수렴 검사의 RSQ는 RCG² 합이다. 종료 뒤 RSQ는 (계수 행렬×P-FPTMP)×CCCI의 제곱합으로 다시 설정한다.

