---
file: models/EFDC/raw/source_code/EFDC-GVC/relax2t.for
lines: 142
sha256: 80d3dce480463a5c0064828ddc06cdc147d9f94a290307e9e4bf15f40435a738
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# relax2t.for — 판독 구간 기록

구간은 1행부터 142행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–38 | 구분 주석과 RELAX2T 선언(1–6). EFDC-FULL 1.0a 머리말·2001-11-01 수정 표기·2002-02-15 루틴 추가 기록(8–18). 주석은 유사 헬름홀츠(pseudo Helmholtz) 방정식의 유한 차분(finite difference)을 적흑(red-black) 정렬의 연속 과이완(successive over relaxation; SOR)으로 푼다고 적는다(20–30). 주석의 방정식은 `CS(L)*P(LS)+CW(L)*P(L-1)` (23), `+CC(L)*P(L)+CE(L)*P(L+1)` (24), `+CN(L)*P(LN) = FP(L)` (25). EFDC.PAR·EFDC.CMN 포함(34–35). |
| 39–61 | 시작 시 6행 RELAX2T 루틴 안. RJ2에 RP를 복사한다(39). PAVG 계산과 FPTMP·P에서 평균값을 빼는 블록은 주석이다(41–50). FPTMP의 제곱합 FPSQ를 계산한다(52–55). ITER를 1로 시작하고 200 표지에서 RSQ를 0으로 둔다(57–60). 원문: `RJ2=RP` (39) / `FPSQ=0.` (52) / `DO L=2,LA` (53) / `FPSQ=FPSQ+FPTMP(L)*FPTMP(L)` (54) / `ITER=1` (57) / `RSQ=0.` (60). |
| 62–81 | 시작 시 6행 RELAX2T 루틴 안. 적색 셀 처리 주석(64). 첫 반복과 이후 반복에서 RPT를 서로 다른 식으로 설정한다(66–67). L=2..LA에서 IL+JL의 홀짝을 MOD로 구분한다(69–71). IVAL=0인 셀에서 CCC·CCS·CCW·CCE·CCN·FPTMP로 잔차(residual)를 계산하고 CCC로 나눈 보정값을 P에서 빼며 잔차 제곱을 누적한다(72–80). 원문: `IF(ITER.EQ.1) RPT=1.0` (66) / `IF(ITER.GT.1) RPT=1.0/(1.0-0.25*RJ2*RPT)` (67) / `DO L=2,LA` (69) / `K=IL(L)+JL(L)` (70) / `IVAL=MOD(K,2)` (71) / `IF(IVAL.EQ.0)THEN` (72) / `LN=LNC(L)` (73) / `LS=LSC(L)` (74) / `RSD=CCC(L)*P(L)+CCS(L)*P(LS)+CCW(L)*P(L-1)+CCE(L)*P(L+1)` (75); `&        +CCN(L)*P(LN)-FPTMP(L)` (76) / `P(L)=P(L)-RPT*RSD/CCC(L)` (77) / `RSQ=RSQ+RSD*RSD` (78). |
| 82–102 | 시작 시 6행 RELAX2T 루틴 안. 흑색 셀 처리 주석(84). 첫 흑색 처리의 RPT와 이후 RPT를 설정한다(87–88). L=2..LA에서 IL+JL의 홀짝을 구분하고 IVAL이 0이 아닌 셀의 잔차·P·RSQ를 계산한다(90–101). 원문: `IF(ITER.EQ.1) RPT=1.0/(1.0-0.5*RJ2)` (87) / `IF(ITER.GT.1) RPT=1.0/(1.0-0.25*RJ2*RPT)` (88) / `DO L=2,LA` (90) / `K=IL(L)+JL(L)` (91) / `IVAL=MOD(K,2)` (92) / `IF(IVAL.NE.0)THEN` (93) / `LN=LNC(L)` (94) / `LS=LSC(L)` (95) / `RSD=CCC(L)*P(L)+CCS(L)*P(LS)+CCW(L)*P(L-1)+CCE(L)*P(L+1)` (96); `&        +CCN(L)*P(LN)-FPTMP(L)` (97) / `P(L)=P(L)-RPT*RSD/CCC(L)` (98) / `RSQ=RSQ+RSD*RSD` (99). |
| 103–125 | 시작 시 6행 RELAX2T 루틴 안. RSQ를 FPSQ 제곱합에 대한 상대 잔차 크기로 바꾼다(107). RSQ가 RSQM 이하이면 400 표지로 이동한다(108). ITER가 ITERM 이상이면 장치 6·8에 메시지와 RSQ를 쓰고 장치 8에 각 셀의 계수·P·FPTMP를 쓴 뒤 STOP한다(112–122). 나머지는 ITER를 증가시켜 200 표지로 돌아간다(124–125). 원문: `RSQ=SQRT(RSQ)/SQRT(FPSQ)` (107) / `IF(RSQ .LE. RSQM) GOTO 400` (108) / `IF(ITER .GE. ITERM)THEN` (112) / `DO L=2,LA` (117) / `ITER=ITER+1` (124). |
| 126–142 | 시작 시 6행 RELAX2T 루틴 안. 400 표지 뒤 P에 PAVG를 되더하는 블록은 주석이다(127–131). 600·601·800 FORMAT은 최대 반복 초과 메시지·RSQ·셀별 계수 출력 형식을 정의한다(135–137). 구분 주석·RETURN·END를 포함한다(133–142). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 52–55·75–78·96–99·107: FPSQ는 FPTMP 제곱합이고 상대 잔차 계산의 분모는 SQRT(FPSQ)이다. P 보정의 분모는 CCC(L)이다. FPSQ=0 또는 CCC(L)=0을 검사하는 분기는 이 파일에 없다.
- 41–50·129–131: PAVG 계산·P와 FPTMP의 평균 제거·P의 평균 복원 블록은 모두 주석 처리되어 있다.
- 75–78·96–99·107: RSQ에 누적하는 RSD는 각 셀의 P 보정 전에 계산한 값이다. 두 색의 보정이 끝난 뒤 전 셀 잔차를 다시 계산하는 루프는 이 파일에 없다.
