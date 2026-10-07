---
file: models/EFDC/raw/source_code/EFDC-GVC/relaxv.for
lines: 270
sha256: 2be3b9fb47230416fd5072db8abd52b772bf05abb1a5a98add7712f738f48018
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# relaxv.for — 판독 구간 기록

구간은 1행부터 270행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–40 | 구분 주석·RELAXV(ISTL) 선언·버전·수정일·변경 기록 머리말(1–17). 모으기·흩뿌리기(gather-scatter)로 벡터화(vectorization) 가능한 판본이라는 주석이다(19). 유사 헬름홀츠(pseudo Helmholtz) 방정식의 유한 차분(finite difference)을 적흑(red-black) 정렬의 연속 과이완(successive over relaxation; SOR)으로 푸는 설명이다(20–30). 주석의 방정식은 `CS(L)*P(LS)+CW(L)*P(L-1)` (23), `+CC(L)*P(L)+CE(L)*P(L+1)` (24), `+CN(L)*P(LN) = FP(L)` (25). EFDC.PAR·EFDC.CMN 포함(34–35). RSDR·RSDB의 DIMENSION은 주석이다(37). |
| 41–66 | 시작 시 6행 RELAXV 루틴 안. LRC·LBC 매핑으로 P를 PRED·PBLK에 복사한다(43–51). ISTL=3이면 250 표지로 이동한다(57). 나머지 경로는 두 시간 수준 Crank–Nicolson 절차라는 주석과 ITER=1 설정·200 표지를 포함한다(61–65). 원문: `DO LR=1,NRC` (43) / `L=LRC(LR)` (44) / `PRED(LR)=P(L)` (45) / `DO LB=1,NBC` (48) / `L=LBC(LB)` (49) / `PBLK(LB)=P(L)` (50) / `IF(ISTL.EQ.3) GOTO 250` (57) / `ITER=1` (63). |
| 67–98 | 시작 시 6행 RELAXV 루틴 안. 두 시간 수준의 적색 잔차(residual) RSDR을 PRED−FPR로 초기화한다(71–73). 남·서·동·북 이웃의 CCSR·CCWR·CCER·CCNR 항을 별도 루프에서 차례로 더한다(75–93). 마지막 별도 루프에서 RP·RSDR로 PRED를 보정한다(95–97). 원문: `DO L=1,NRC` (71) / `RSDR(L)=PRED(L)-FPR(L)` (72) / `DO L=1,NRC` (75) / `LS=LBSRC(L)` (76) / `RSDR(L)=RSDR(L)+CCSR(L)*PBLK(LS)` (77) / `DO L=1,NRC` (80) / `LW=LBWRC(L)` (81) / `RSDR(L)=RSDR(L)+CCWR(L)*PBLK(LW)` (82) / `DO L=1,NRC` (85) / `LE=LBERC(L)` (86) / `RSDR(L)=RSDR(L)+CCER(L)*PBLK(LE)` (87) / `DO L=1,NRC` (90) / `LN=LBNRC(L)` (91) / `RSDR(L)=RSDR(L)+CCNR(L)*PBLK(LN)` (92) / `DO L=1,NRC` (95) / `PRED(L)=PRED(L)-RP*RSDR(L)` (96). |
| 99–130 | 시작 시 6행 RELAXV 루틴 안. 두 시간 수준의 흑색 잔차 RSDB를 PBLK−FPB로 초기화한다(103–105). 남·서·동·북 이웃의 CCSB·CCWB·CCEB·CCNB 항과 갱신된 PRED를 별도 루프에서 더한다(107–125). 마지막 별도 루프에서 RP·RSDB로 PBLK를 보정한다(127–129). 원문: `DO L=1,NBC` (103) / `RSDB(L)=PBLK(L)-FPB(L)` (104) / `DO L=1,NBC` (107) / `LS=LRSBC(L)` (108) / `RSDB(L)=RSDB(L)+CCSB(L)*PRED(LS)` (109) / `DO L=1,NBC` (112) / `LW=LRWBC(L)` (113) / `RSDB(L)=RSDB(L)+CCWB(L)*PRED(LW)` (114) / `DO L=1,NBC` (117) / `LE=LREBC(L)` (118) / `RSDB(L)=RSDB(L)+CCEB(L)*PRED(LE)` (119) / `DO L=1,NBC` (122) / `LN=LRNBC(L)` (123) / `RSDB(L)=RSDB(L)+CCNB(L)*PRED(LN)` (124) / `DO L=1,NBC` (127) / `PBLK(L)=PBLK(L)-RP*RSDB(L)` (128). |
| 131–159 | 시작 시 6행 RELAXV 루틴 안. RSQ를 0으로 두고 RSDR·RSDB 제곱합을 누적한다(135–141). RSQ가 RSQM 이하이면 400 표지로 이동한다(143). ITER가 ITERM 이상이면 STOP한다(147). 나머지는 ITER를 증가시켜 200 표지로 돌아간다(149–150). 구분 주석과 250 표지를 포함한다(152–159). 원문: `RSQ=0.` (135) / `DO L=1,NRC` (136) / `RSQ=RSQ+RSDR(L)*RSDR(L)` (137) / `DO L=1,NBC` (139) / `RSQ=RSQ+RSDB(L)*RSDB(L)` (140) / `IF(RSQ .LE. RSQM) GOTO 400` (143) / `IF(ITER .GE. ITERM) STOP` (147) / `ITER=ITER+1` (149). |
| 160–197 | 시작 시 6행 RELAXV 루틴 안. 세 시간 수준의 도약법(leap-frog) 절차를 시작하고 ITER=1·300 표지를 둔다(160–164). 적색 RSDR을 PRED−FPR로 초기화한다(170–172). CSR·CWR·CER·CNR 이웃 항을 별도 루프로 누적한 뒤 RP·RSDR로 PRED를 보정한다(174–196). 원문: `ITER=1` (162) / `DO L=1,NRC` (170) / `RSDR(L)=PRED(L)-FPR(L)` (171) / `DO L=1,NRC` (174) / `LS=LBSRC(L)` (175) / `RSDR(L)=RSDR(L)+CSR(L)*PBLK(LS)` (176) / `DO L=1,NRC` (179) / `LW=LBWRC(L)` (180) / `RSDR(L)=RSDR(L)+CWR(L)*PBLK(LW)` (181) / `DO L=1,NRC` (184) / `LE=LBERC(L)` (185) / `RSDR(L)=RSDR(L)+CER(L)*PBLK(LE)` (186) / `DO L=1,NRC` (189) / `LN=LBNRC(L)` (190) / `RSDR(L)=RSDR(L)+CNR(L)*PBLK(LN)` (191) / `DO L=1,NRC` (194) / `PRED(L)=PRED(L)-RP*RSDR(L)` (195). |
| 198–229 | 시작 시 6행 RELAXV 루틴 안. 세 시간 수준의 흑색 RSDB를 PBLK−FPB로 초기화한다(202–204). CSB·CWB·CEB·CNB 이웃 항과 갱신된 PRED를 별도 루프로 누적한 뒤 RP·RSDB로 PBLK를 보정한다(206–228). 원문: `DO L=1,NBC` (202) / `RSDB(L)=PBLK(L)-FPB(L)` (203) / `DO L=1,NBC` (206) / `LS=LRSBC(L)` (207) / `RSDB(L)=RSDB(L)+CSB(L)*PRED(LS)` (208) / `DO L=1,NBC` (211) / `LW=LRWBC(L)` (212) / `RSDB(L)=RSDB(L)+CWB(L)*PRED(LW)` (213) / `DO L=1,NBC` (216) / `LE=LREBC(L)` (217) / `RSDB(L)=RSDB(L)+CEB(L)*PRED(LE)` (218) / `DO L=1,NBC` (221) / `LN=LRNBC(L)` (222) / `RSDB(L)=RSDB(L)+CNB(L)*PRED(LN)` (223) / `DO L=1,NBC` (226) / `PBLK(L)=PBLK(L)-RP*RSDB(L)` (227). |
| 230–250 | 시작 시 6행 RELAXV 루틴 안. RSQ를 0으로 두고 두 색의 잔차 제곱합을 누적한다(234–240). RSQ가 RSQM 이하이면 400 표지로 이동한다(242). ITER가 ITERM 이상이면 STOP한다(246). 나머지는 ITER를 증가시켜 300 표지로 돌아간다(248–249). 원문: `RSQ=0.` (234) / `DO L=1,NRC` (235) / `RSQ=RSQ+RSDR(L)*RSDR(L)` (236) / `DO L=1,NBC` (238) / `RSQ=RSQ+RSDB(L)*RSDB(L)` (239) / `IF(RSQ .LE. RSQM) GOTO 400` (242) / `IF(ITER .GE. ITERM) STOP` (246) / `ITER=ITER+1` (248). |
| 251–270 | 시작 시 6행 RELAXV 루틴 안. 400 표지에서 LRC·LBC 매핑으로 PRED·PBLK를 P에 복사한다(255–265). 구분 주석·RETURN·END로 루틴을 끝낸다(267–270). 원문: `DO LR=1,NRC` (257) / `L=LRC(LR)` (258) / `P(L)=PRED(LR)` (259) / `DO LB=1,NBC` (262) / `L=LBC(LB)` (263) / `P(L)=PBLK(LB)` (264). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 72–96·104–128·135–140·171–195·203–227·234–239: 수렴에 쓰는 RSDR·RSDB는 해당 색의 PRED·PBLK 보정 전에 만들어진 값이다. 보정 이후 잔차 배열을 재계산하는 별도 루프는 이 파일에 없다.
- 143–150·242–249: 수렴 검사는 최대 반복 수 검사보다 먼저 실행된다. 최대 반복 수 조건이 성립하면 직접 STOP하며 이 두 분기에는 WRITE 문장이 없다.
