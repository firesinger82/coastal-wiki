---
file: models/EFDC/raw/source_code/EFDC-GVC/bal2t3b.for
lines: 229
sha256: 93438ce2101e89918fdac0c6419de1b458bb3ee2e3491ece685b932a3890c795
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# bal2t3b.for — 판독 구간 기록

구간은 1행부터 229행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–51 | 구분 주석과 `SUBROUTINE BAL2T3B(IBALSTDT)` 입구(1–7). EFDC-FULL 1.0a·수정일·두 시각 단계(two time-level) 수지(balance), 소류사(bed load) 유출 및 QDWASTE 추가 기록(9–27). `INCLUDE 'EFDC.PAR'` (31), `INCLUDE 'EFDC.CMN'` (32). `IF(ISDYNSTP.EQ.0)THEN` (36)이면 DELT=DT(37), `ELSE` (38)이면 DELT=DTDYN(39), 분기 종료(40). CONT 선언은 주석(44). 내부 생성·소멸원(source and sink) 안내 및 구분 주석(41–51). 포함 파일 내부는 이번 판독 대상이 아니다. |
| 52–63 | 시작 시 7행 BAL2T3B 안. `IF(IBALSTDT.EQ.1)THEN` (52)이면 L=2..LA에서 `WVOLOUT=WVOLOUT-DTSED*QMORPH(L)` (54), `BVOLOUT=BVOLOUT+DTSED*QMORPH(L)` (55), `VOLMORPH2T=VOLMORPH2T+DTSED*QMORPH(L)` (56). QWTRBEDA·QWTRBEDA1·QWTRBED의 대체 WVOLOUT 식은 주석(57–58). 루프·분기 종료와 구분 주석(59–63). |
| 64–91 | 시작 시 7행 BAL2T3B 안. `IF(ISTRAN(5).GE.1)THEN` (64)과 NT=1..NTOX 루프(66)를 연다. M=MSVTOX(NT)(67), 출력은 주석(68). K=1..KC, L=2..LC에서 CONT에 TOX(L,K,NT) 복사(70–74). 독성물질 소류사 유출 안내(77–78). `IF(IBALSTDT.EQ.1)THEN` (80)을 열고 `IF(NSBDLDBC.GT.0) THEN` (81)이면 `TOXBLB2T(NT)=TOXBLB2T(NT)+DTSED*TOXBLB(NT)` (82), 내부 분기 종료(83). 독성물질 수층 측·바닥 측 부유사(suspended load) 플럭스(flux), 공극수 이류·확산(pore-water advection and diffusion) 플럭스 및 소류사 플럭스의 부호 안내(85–91). |
| 92–124 | 시작 시 7행 BAL2T3B·64행 ISTRAN(5) 참 분기·66행 NT 루프·80행 IBALSTDT=1 참 분기 안. L=2..LA에서 TOXFTMP·DELT의 옛 식은 주석(93–97). 실행식은 `TOXFLUXW2T(NT)=TOXFLUXW2T(NT)+DTSED*DXYP(L)*TOXF(L,0,NT)` (98), `TOXFLUXB2T(NT)=TOXFLUXB2T(NT)+DTSED*DXYP(L)*TOXFB(L,KBT(L),NT)` (99), `TADFLUX2T(NT)=TADFLUX2T(NT)+DTSED*DXYP(L)*TADFLUX(L,NT)` (100). 셀별 TOXFBL2T 대체식은 주석(101), L 루프 종료(102). `TOXFBL2T(NT)=TOXFBL2T(NT)+DTSED*TOXFBLT(NT)` (104). `IF(ISBKERO.GE.1)THEN` (106)이면 NP=1..NBEPAIR에서 LIJ로 둑(bank) 셀 LBANK와 수로(channel) 셀 LCHAN을 찾는다(107–109). `TOXFLUXB2T(NT)=TOXFLUXB2T(NT)` (110), `&                    +DTSED*DXYP(LBANK)*TOXFBEBKB(LBANK,NT)` (111), `TOXFLUXB2T(NT)=TOXFLUXB2T(NT)` (112), `&                    +DTSED*DXYP(LCHAN)*TOXFBECHB(LCHAN,NT)` (113). NP 루프·둑 침식(bank erosion) 분기·IBALSTDT 분기·NT 루프·ISTRAN(5) 분기 종료(114–121), 구분 주석(122–124). |
| 125–163 | 시작 시 7행 BAL2T3B 안. `IF(ISTRAN(6).GE.1)THEN` (125), NSX=1..NSED 루프(127), M=MSVSED(NSX)(128). K=1..KC, L=2..LC에서 CONT에 SED(L,K,NSX) 복사(130–134). 바닥에서 수층으로 양의 점착성(cohesive) 플럭스 안내(136–137). `IF(IBALSTDT.EQ.1)THEN` (139)이면 L=2..LA에서 `SEDFLUX2T(NSX)=SEDFLUX2T(NSX)+DTSED*DXYP(L)*SEDF(L,0,NSX)` (142). L 루프 종료(143). 같은 IBALSTDT 분기 안에서 `IF(ISBKERO.GE.1)THEN` (145)이면 NP=1..NBEPAIR에서 LBANK·LCHAN을 찾는다(146–148). `SEDFLUX2T(NSX)=SEDFLUX2T(NSX)` (149), `&                    +DTSED*DXYP(LBANK)*SEDFBEBKB(LBANK,NSX)` (150), `SEDFLUX2T(NSX)=SEDFLUX2T(NSX)` (151), `&                    +DTSED*DXYP(LCHAN)*SEDFBECHB(LCHAN,NSX)` (152). NP 루프·둑 침식 분기·IBALSTDT 분기·NSX 루프·ISTRAN(6) 분기 종료(153–160), 구분 주석(161–163). |
| 164–196 | 시작 시 7행 BAL2T3B 안. `IF(ISTRAN(7).GE.1)THEN` (164), NSX=1..NSND 루프(166), M=MSVSND(NSX)(167). K=1..KC, L=2..LC에서 CONT에 SND(L,K,NSX) 복사(169–173). 비점착성(noncohesive) 퇴적물 소류사 유출 안내(175–176). `IF(IBALSTDT.EQ.1)THEN` (178), `IF(NSBDLDBC.GT.0) THEN` (179)이면 NSB=1..NSBDLDBC에서 LUTMP·LDTMP를 가져온다(180–182). `IF(LDTMP.EQ.0) THEN` (183)이면 `SBLOUT2T(NSX)=SBLOUT2T(NSX)+` (184), `&        DTSED*QSBDLDOT(LUTMP,NSX)` (185). 세 분기·NSB 루프 종료(186–189). 수층으로 양의 부유사 플럭스 및 소류사 바닥 플럭스 안내(191–194), TMPVAL 대입은 주석(196). |
| 197–229 | 시작 시 7행 BAL2T3B·164행 ISTRAN(7) 참 분기·166행 NSX 루프 안. `IF(IBALSTDT.EQ.1)THEN` (197)이면 L=2..LA에서 `SNDFLUX2T(NSX)=SNDFLUX2T(NSX)+DTSED*DXYP(L)*(SNDF(L,0,NSX)` (200), `&                -SNDFBL(L,NSX))` (201), `SNDFBL2T(NSX)=SNDFBL2T(NSX)+DTSED*DXYP(L)*SNDFBL(L,NSX)` (202). L 루프 종료(203). 같은 IBALSTDT 분기에서 `IF(ISBKERO.GE.1)THEN` (205)이면 NP=1..NBEPAIR에서 LBANK·LCHAN을 찾는다(206–208). `SNDFLUX2T(NSX)=SNDFLUX2T(NSX)` (209), `&                    +DTSED*DXYP(LBANK)*SNDFBEBKB(LBANK,NSX)` (210), `SNDFLUX2T(NSX)=SNDFLUX2T(NSX)` (211), `&                    +DTSED*DXYP(LCHAN)*SNDFBECHB(LCHAN,NSX)` (212). NP 루프·둑 침식 분기·IBALSTDT 분기 종료(213–216), TMPVAL 차와 WRITE는 주석(217–218). NSX 루프·ISTRAN(7) 분기 종료(220·222), FORMAT 800(224), 구분 주석(223·225–227), `RETURN` (228), `END` (229). 외부 루틴 호출은 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 36–40·93–101: DELT를 설정한다. 이 파일에서 DELT를 사용하는 계산식은 주석 처리되어 있다. 실행 플럭스 식은 DTSED를 사용한다.
- 67·128·167: M을 MSVTOX·MSVSED·MSVSND에서 가져온다. 이 파일의 실행 계산식은 M을 참조하지 않는다.
- 70–74·130–134·169–173: CONT를 TOX·SED·SND에서 복사한다. 이 파일에는 CONT를 읽는 실행문이 없다.
- 106–115·145–154·205–214: 둑 침식 분기는 TOXFLUXB2T·SEDFLUX2T·SNDFLUX2T에 둑 및 수로의 바닥 측 교환을 더한다. 이 분기들에는 TOXFBECHW·SEDFBECHW·SNDFBECHW를 사용하는 식이 없다.
- 218·224: FORMAT 800은 남아 있다. 이를 참조하는 WRITE 문장은 주석 처리되어 있다.
