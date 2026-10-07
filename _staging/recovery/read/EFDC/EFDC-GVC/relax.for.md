---
file: models/EFDC/raw/source_code/EFDC-GVC/relax.for
lines: 195
sha256: 1e8783820fbf62ab126ed605b5bce60a43aaffb2ca3d35dabf0274fb9d282077
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# relax.for — 판독 구간 기록

구간은 1행부터 195행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–37 | 구분 주석과 RELAX(ISTL) 선언(1–6). EFDC-FULL 1.0a·수정일·변경 기록 머리말(8–17). 주석은 유사 헬름홀츠(pseudo Helmholtz) 방정식의 유한 차분(finite difference)을 적흑(red-black) 정렬의 연속 과이완(successive over relaxation; SOR)으로 푼다고 설명한다(19–29). 주석의 방정식은 `CS(L)*P(LS)+CW(L)*P(L-1)` (22), `+CC(L)*P(L)+CE(L)*P(L+1)` (23), `+CN(L)*P(LN) = FP(L)` (24). 수렴 척도는 전역 제곱 오차 RSQ이다(27). EFDC.PAR·EFDC.CMN 포함(33–34). |
| 38–64 | 시작 시 6행 RELAX 루틴 안. LRC·LBC 매핑으로 P를 PRED·PBLK에 복사한다(40–48). ISTL=3이면 250 표지로 이동한다(54). 나머지 경로의 주석은 두 시간 수준 Crank–Nicolson 절차이다(58). ITER를 1로 시작하고 200 표지에서 RSQ를 0으로 둔다(60–63). 원문: `DO LR=1,NRC` (40) / `L=LRC(LR)` (41) / `PRED(LR)=P(L)` (42) / `DO LB=1,NBC` (45) / `L=LBC(LB)` (46) / `PBLK(LB)=P(L)` (47) / `IF(ISTL.EQ.3) GOTO 250` (54) / `ITER=1` (60) / `RSQ=0.` (63). |
| 65–94 | 시작 시 6행 RELAX 루틴 안. 두 시간 수준의 적색 셀 루프는 흑색 이웃 인덱스와 CCSR·CCWR·CCER·CCNR·FPR로 RSD를 계산하고 PRED를 보정하며 RSD 제곱을 RSQ에 누적한다(69–78). 흑색 셀 루프는 갱신된 PRED와 CCSB·CCWB·CCEB·CCNB·FPB로 RSD·PBLK·RSQ를 계산한다(84–93). 원문: `DO L=1,NRC` (69) / `LN=LBNRC(L)` (70) / `LS=LBSRC(L)` (71) / `LE=LBERC(L)` (72) / `LW=LBWRC(L)` (73) / `RSD=PRED(L)+CCSR(L)*PBLK(LS)+CCWR(L)*PBLK(LW)+CCER(L)*PBLK(LE)` (74); `&   +CCNR(L)*PBLK(LN)-FPR(L)` (75) / `PRED(L)=PRED(L)-RP*RSD` (76) / `RSQ=RSQ+RSD*RSD` (77) / `DO L=1,NBC` (84) / `LN=LRNBC(L)` (85) / `LS=LRSBC(L)` (86) / `LE=LREBC(L)` (87) / `LW=LRWBC(L)` (88) / `RSD=PBLK(L)+CCSB(L)*PRED(LS)+CCWB(L)*PRED(LW)+CCEB(L)*PRED(LE)` (89); `&   +CCNB(L)*PRED(LN)-FPB(L)` (90) / `PBLK(L)=PBLK(L)-RP*RSD` (91) / `RSQ=RSQ+RSD*RSD` (92). |
| 95–118 | 시작 시 6행 RELAX 루틴 안. RSQ가 RSQM 이하이면 400 표지로 이동한다(99). 그렇지 않고 ITER가 ITERM 이상이면 장치 6에 최대 반복 메시지를 쓰고 STOP한다(103–106). 나머지는 ITER를 증가시켜 200 표지로 돌아간다(108–109). 구분 주석과 250 표지를 포함한다(111–118). 원문: `IF(RSQ .LE. RSQM) GOTO 400` (99) / `IF(ITER .GE. ITERM)THEN` (103) / `ITER=ITER+1` (108). |
| 119–155 | 시작 시 6행 RELAX 루틴 안. 세 시간 수준의 도약법(leap-frog) 절차라는 주석이다(119). ITER를 1로 시작하고 300 표지에서 RSQ를 0으로 둔다(121–124). 적색 셀은 CSR·CWR·CER·CNR, 흑색 셀은 CSB·CWB·CEB·CNB를 사용하여 RSD·PRED/PBLK·RSQ를 계산한다(130–154). 원문: `ITER=1` (121) / `RSQ=0.` (124) / `DO L=1,NRC` (130) / `LN=LBNRC(L)` (131) / `LS=LBSRC(L)` (132) / `LE=LBERC(L)` (133) / `LW=LBWRC(L)` (134) / `RSD=PRED(L)+CSR(L)*PBLK(LS)+CWR(L)*PBLK(LW)+CER(L)*PBLK(LE)` (135); `&   +CNR(L)*PBLK(LN)-FPR(L)` (136) / `PRED(L)=PRED(L)-RP*RSD` (137) / `RSQ=RSQ+RSD*RSD` (138) / `DO L=1,NBC` (145) / `LN=LRNBC(L)` (146) / `LS=LRSBC(L)` (147) / `LE=LREBC(L)` (148) / `LW=LRWBC(L)` (149) / `RSD=PBLK(L)+CSB(L)*PRED(LS)+CWB(L)*PRED(LW)+CEB(L)*PRED(LE)` (150); `&   +CNB(L)*PRED(LN)-FPB(L)` (151) / `PBLK(L)=PBLK(L)-RP*RSD` (152) / `RSQ=RSQ+RSD*RSD` (153). |
| 156–171 | 시작 시 6행 RELAX 루틴 안. 세 시간 수준의 수렴 조건은 RSQ≤RSQM이며 성립하면 400 표지로 이동한다(160). ITER≥ITERM이면 메시지 출력 후 STOP한다(164–167). 나머지는 ITER를 증가시켜 300 표지로 돌아간다(169–170). 원문: `IF(RSQ .LE. RSQM) GOTO 400` (160) / `IF(ITER .GE. ITERM)THEN` (164) / `ITER=ITER+1` (169). |
| 172–195 | 시작 시 6행 RELAX 루틴 안. 400 표지에서 LRC·LBC 매핑으로 PRED·PBLK를 P에 복사한다(176–186). 최대 반복 초과 메시지의 600 FORMAT과 구분 주석을 포함한다(188–193). RETURN·END로 루틴을 끝낸다(194–195). 원문: `DO LR=1,NRC` (178) / `L=LRC(LR)` (179) / `P(L)=PRED(LR)` (180) / `DO LB=1,NBC` (183) / `L=LBC(LB)` (184) / `P(L)=PBLK(LB)` (185). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 74–77·89–92·135–138·150–153: RSQ에 더하는 RSD는 해당 셀의 PRED·PBLK 보정 전에 계산한 값이다. 두 색의 보정이 끝난 뒤 모든 셀의 잔차(residual)를 다시 계산하는 별도 루프는 이 파일에 없다.
- 99–106·160–167: 각 반복의 수렴 검사는 최대 반복 수 검사보다 먼저 실행된다. 두 반복 경로 모두 수렴 검사에 통과하면 ITER≥ITERM 검사를 거치지 않고 400 표지로 이동한다.
