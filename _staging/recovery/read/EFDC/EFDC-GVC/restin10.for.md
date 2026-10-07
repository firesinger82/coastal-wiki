---
file: models/EFDC/raw/source_code/EFDC-GVC/restin10.for
lines: 336
sha256: deb5e25b9374bbdc183948cc6a7f3cb3029962751e70ea00be6ba1758ca68d34
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# restin10.for — 판독 구간 기록

구간은 1행부터 336행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–30 | 구분 주석·RESTIN10 선언·EFDC-FULL 1.0a·2001-11-01 수정·변경 기록 머리말(1–17). 설명은 RESTINP라는 이름으로 1992-09-08 이전 EFDC.FOR가 만든 재시작 파일(restart file)을 읽는다고 적는다(21–22). EFDC.PAR·EFDC.CMN을 포함한다(26–27). |
| 31–72 | 시작 시 6행 RESTIN10 루틴 안. RESTART.INP를 열고 자유 형식으로 NREST를 읽는다(31–35). L=2..LA에서 P·P1·수심 적분(depth integrated) 유량 4개, U·U1·V·V1의 1..KC 층, W·W1의 1..KS 층, QQ·QQ1·QQL·QQL1·DML의 0..KC 층을 읽는다(37–50). ISCI(1..5)=1의 개별 분기에서 염분(salinity), 수온(temperature), 염료(dye), 첫 퇴적물(sediment) 성분의 바닥·수체 값, SFL·SFL2를 읽고 셀 루프를 닫는다(51–71). 모든 READ 오류는 1000 표지로 이동한다. 원문: `DO L=2,LA` (37) / `IF(ISCI(1).EQ.1)THEN` (51) / `IF(ISCI(2).EQ.1)THEN` (55) / `IF(ISCI(3).EQ.1)THEN` (59) / `IF(ISCI(4).EQ.1)THEN` (63) / `IF(ISCI(5).EQ.1)THEN` (67). |
| 73–107 | 시작 시 6행 RESTIN10 루틴 안. ISCI(1)=1이면 남·서·동·북의 염분 경계 이력 NLO·CLO를 읽는다(73–106). 각 LL에서 L을 LCBS·LCBW·LCBE·LCBN으로 찾는다(75·82·89·98). SAL·SAL1 입력 대상의 첫 인덱스는 LC이다(78–79·85–86·92–93·101–102). 동쪽은 UHDY·UHDY1, 북쪽은 VHDX·VHDX1의 LC 인덱스도 읽는다(94–95·103–104). 원문: `IF(ISCI(1).EQ.1)THEN` (73) / `DO LL=1,NCBS` (74) / `L=LCBS(LL)` (75) / `DO LL=1,NCBW` (81) / `L=LCBW(LL)` (82) / `DO LL=1,NCBE` (88) / `L=LCBE(LL)` (89) / `DO LL=1,NCBN` (97) / `L=LCBN(LL)` (98). |
| 108–142 | 시작 시 6행 RESTIN10 루틴 안. ISCI(2)=1이면 남·서·동·북 경계의 성분 인덱스 2인 NLO·CLO 및 TEM·TEM1을 읽는다(108–141). 각 경계 셀 L을 찾지만 TEM·TEM1 입력은 LC를 사용한다(110–139). 동쪽은 UHDY·UHDY1, 북쪽은 VHDX·VHDX1도 LC에 읽는다(129–130·138–139). 원문: `IF(ISCI(2).EQ.1)THEN` (108) / `DO LL=1,NCBS` (109) / `L=LCBS(LL)` (110) / `DO LL=1,NCBW` (116) / `L=LCBW(LL)` (117) / `DO LL=1,NCBE` (123) / `L=LCBE(LL)` (124) / `DO LL=1,NCBN` (132) / `L=LCBN(LL)` (133). |
| 143–177 | 시작 시 6행 RESTIN10 루틴 안. ISCI(3)=1이면 네 방향 경계의 성분 인덱스 3인 NLO·CLO 및 DYE·DYE1을 읽는다(143–176). 경계 셀 L을 찾지만 DYE·DYE1 입력은 LC를 사용한다(145–174). 동쪽은 UHDY·UHDY1, 북쪽은 VHDX·VHDX1도 LC에 읽는다(164–165·173–174). 원문: `IF(ISCI(3).EQ.1)THEN` (143) / `DO LL=1,NCBS` (144) / `L=LCBS(LL)` (145) / `DO LL=1,NCBW` (151) / `L=LCBW(LL)` (152) / `DO LL=1,NCBE` (158) / `L=LCBE(LL)` (159) / `DO LL=1,NCBN` (167) / `L=LCBN(LL)` (168). |
| 178–212 | 시작 시 6행 RESTIN10 루틴 안. ISCI(4)=1이면 네 방향 경계의 성분 인덱스 4인 NLO·CLO와 퇴적물 첫 성분 SED·SED1을 읽는다(178–211). 경계 셀 L을 찾지만 SED·SED1 입력은 LC를 사용한다(180–209). 동쪽은 UHDY·UHDY1, 북쪽은 VHDX·VHDX1도 LC에 읽는다(199–200·208–209). 원문: `IF(ISCI(4).EQ.1)THEN` (178) / `DO LL=1,NCBS` (179) / `L=LCBS(LL)` (180) / `DO LL=1,NCBW` (186) / `L=LCBW(LL)` (187) / `DO LL=1,NCBE` (193) / `L=LCBE(LL)` (194) / `DO LL=1,NCBN` (202) / `L=LCBN(LL)` (203). |
| 213–249 | 시작 시 6행 RESTIN10 루틴 안. ISCI(5)=1이면 네 방향 경계의 성분 인덱스 5인 NLO·CLO와 SFL·SFL2를 읽는다(213–246). 경계 셀 L을 찾지만 SFL·SFL2는 LC를 사용한다. 동쪽의 두 유량 READ는 모두 UHDYWQ(LC,K), 북쪽의 두 READ는 모두 VHDXWQ(LC,K)를 읽는다(234–235·243–244). RESTART.INP를 닫는다(248). 원문: `IF(ISCI(5).EQ.1)THEN` (213) / `DO LL=1,NCBS` (214) / `L=LCBS(LL)` (215) / `DO LL=1,NCBW` (221) / `L=LCBW(LL)` (222) / `DO LL=1,NCBE` (228) / `L=LCBE(LL)` (229) / `DO LL=1,NCBN` (237) / `L=LCBN(LL)` (238). |
| 250–290 | 시작 시 6행 RESTIN10 루틴 안. K=1..KC에서 인덱스 1·LC의 SAL·TEM·DYE·SED 첫 성분·SFL·CWQ와 현재·이전 수평 유량·수질 유량을 모두 0으로 초기화한다(250–287). 구분 주석까지 포함한다(288–290). 원문: `DO K=1,KC` (250) / `SAL(1,K)=0.` (251) / `TEM(1,K)=0.` (252) / `DYE(1,K)=0.` (253) / `SED(1,K,1)=0.` (254) / `SFL(1,K)=0.` (255) / `CWQ(1,K)=0.` (256) / `VHDX(1,K)=0.` (257) / `UHDY(1,K)=0.` (258) / `SAL1(1,K)=0.` (259) / `TEM1(1,K)=0.` (260) / `DYE1(1,K)=0.` (261) / `SED1(1,K,1)=0.` (262) / `SFL2(1,K)=0.` (263) / `CWQ2(1,K)=0.` (264) / `VHDX1(1,K)=0.` (265) / `UHDY1(1,K)=0.` (266) / `VHDXWQ(1,K)=0.` (267) / `UHDYWQ(1,K)=0.` (268) / `SAL(LC,K)=0.` (269) / `TEM(LC,K)=0.` (270) / `DYE(LC,K)=0.` (271) / `SED(LC,K,1)=0.` (272) / `SFL(LC,K)=0.` (273) / `CWQ(LC,K)=0.` (274) / `VHDX(LC,K)=0.` (275) / `UHDY(LC,K)=0.` (276) / `SAL1(LC,K)=0.` (277) / `TEM1(LC,K)=0.` (278) / `DYE1(LC,K)=0.` (279) / `SED1(LC,K,1)=0.` (280) / `SFL2(LC,K)=0.` (281) / `CWQ2(LC,K)=0.` (282) / `VHDX1(LC,K)=0.` (283) / `UHDY1(LC,K)=0.` (284) / `VHDXWQ(LC,K)=0.` (285) / `UHDYWQ(LC,K)=0.` (286). |
| 291–306 | 시작 시 6행 RESTIN10 루틴 안. LS=LSC(L)를 사용하여 P1·P·GI와 BELV로 이전·현재 면 수심 H1U·H1V·HU·HV 및 셀 수심 H1P·HP를 계산한다(291–298). HPI·HUI·HVI·H1UI·H1VI를 역수로 계산하고 H2WQ에 HP를 복사한다(299–305). 원문: `DO L=2,LA` (291) / `LS=LSC(L)` (292) / `H1U(L)=0.5*GI*(P1(L)+P1(L-1))-0.5*(BELV(L)+BELV(L-1))` (293) / `H1V(L)=0.5*GI*(P1(L)+P1(LS))-0.5*(BELV(L)+BELV(LS))` (294) / `H1P(L)=GI*P1(L)-BELV(L)` (295) / `HU(L)=0.5*GI*(P(L)+P(L-1))-0.5*(BELV(L)+BELV(L-1))` (296) / `HV(L)=0.5*GI*(P(L)+P(LS))-0.5*(BELV(L)+BELV(LS))` (297) / `HP(L)=GI*P(L)-BELV(L)` (298) / `HPI(L)=1./HP(L)` (299) / `HUI(L)=1./HU(L)` (300) / `HVI(L)=1./HV(L)` (301) / `H1UI(L)=1./H1U(L)` (302) / `H1VI(L)=1./H1V(L)` (303) / `H2WQ(L)=HP(L)` (304). |
| 307–317 | 시작 시 6행 RESTIN10 루틴 안. K=1..KC·L=2..LA에서 면 길이·면 수심·속도로 UHDY1·VHDX1·UHDY·VHDX를 계산한다(307–312). SAL·SAL1은 MAX로 0 이상으로 제한한다(313–316). 원문: `DO K=1,KC` (307) / `DO L=2,LA` (308) / `UHDY1(L,K)=DYU(L)*H1U(L)*U1(L,K)` (309) / `VHDX1(L,K)=DXV(L)*H1V(L)*V1(L,K)` (310) / `UHDY(L,K)=DYU(L)*HU(L)*U(L,K)` (311) / `VHDX(L,K)=DXV(L)*HV(L)*V(L,K)` (312) / `SAL(L,K)=MAX(SAL(L,K),0.)` (313) / `SAL1(L,K)=MAX(SAL1(L,K),0.)` (314). |
| 318–336 | 시작 시 6행 RESTIN10 루틴 안. 정상 경로는 오류 처리부를 건너뛰어 1002로 이동한다(322·326). ERR=1000 경로는 장치 6에 읽기 오류 메시지를 쓰고 STOP한다(323–325). 907·908 FORMAT 및 구분 주석을 포함한다(330–334). RETURN·END로 루틴을 끝낸다(335–336). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 75–244: 경계 루프마다 L을 경계 셀 배열에서 대입한다. 해당 경계의 SAL·TEM·DYE·SED·SFL 및 추가 유량 READ는 L 대신 고정 첫 인덱스 LC에 저장한다.
- 78–244·269–286: 경계 READ에서 LC에 저장한 성분 및 층별 유량은 이후 K=1..KC 초기화 루프에서 0으로 다시 설정된다.
- 234–235·243–244: 동쪽 SFL 경계의 연속 두 READ는 같은 UHDYWQ(LC,K)를 읽는다. 북쪽의 연속 두 READ도 같은 VHDXWQ(LC,K)를 읽는다.
- 293–303: 수심을 P·P1·BELV로 계산한 뒤 다섯 수심 역수를 계산한다. 이 계산 블록에는 음수 또는 0 수심을 검사하는 분기가 없다.
- 304: H2WQ(L)에 HP(L)를 복사한다. 이 파일의 활성 문장에는 HWQ(L)를 설정하는 대입문이 없다.
