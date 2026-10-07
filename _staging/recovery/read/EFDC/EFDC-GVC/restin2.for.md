---
file: models/EFDC/raw/source_code/EFDC-GVC/restin2.for
lines: 260
sha256: 9f571e65c4d091c2476cb0fac0e4e3552d85954ad3e7aa4a4419db3e1f961a29
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# restin2.for — 판독 구간 기록

구간은 1행부터 260행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–30 | 구분 주석·RESTIN2 선언·EFDC-FULL 1.0a·수정일·변경 기록 머리말(1–17). 주석은 RESTINP라는 이름으로 KC/2층 재시작 파일(restart file)을 읽어 KC층으로 초기화한다고 설명한다(21–22). EFDC.PAR·EFDC.CMN을 포함한다(26–27). |
| 31–59 | 시작 시 6행 RESTIN2 루틴 안. RESTART.INP를 열고 908 FORMAT으로 NREST를 읽는다(31–35). L=2..LA에서 수심 4개와 수심 적분(depth integrated) 유량 4개를 읽는다(37–39). U·U1·V·V1은 K=2..KC의 짝수 층, QQ·QQ1·QQL·QQL1·DML은 K=0..KC의 짝수 층을 읽는다(40–48). K=1..KS의 홀수 층에서 속도는 다음 짝수 층 값을 복사하고 나머지 다섯 배열은 양쪽 짝수 층 평균으로 보간(interpolation)한다(49–59). 원문: `DO L=2,LA` (37) / `DO K=1,KS,2` (49) / `U(L,K)=U(L,K+1)` (50) / `U1(L,K)=U1(L,K+1)` (51) / `V(L,K)=V(L,K+1)` (52) / `V1(L,K)=V1(L,K+1)` (53) / `QQ(L,K)=0.5*(QQ(L,K-1)+QQ(L,K+1))` (54) / `QQ1(L,K)=0.5*(QQ1(L,K-1)+QQ1(L,K+1))` (55) / `QQL(L,K)=0.5*(QQL(L,K-1)+QQL(L,K+1))` (56) / `QQL1(L,K)=0.5*(QQL1(L,K-1)+QQL1(L,K+1))` (57) / `DML(L,K)=0.5*(DML(L,K-1)+DML(L,K+1))` (58). |
| 60–101 | 시작 시 6행 RESTIN2 루틴 안. 시작 시 37행 L 루프 안. ISCI(1..5)=1의 독립 조건으로 염분(salinity)·수온(temperature)·염료(dye)·퇴적물(sediment) 첫 성분·SFL의 현재·이전 값을 짝수 층에 읽는다(60–99). 퇴적물은 SEDB·SEDB1의 바닥 인덱스 1·성분 인덱스 1도 읽는다(85–86). 각 선택 분기에서 K=1..KS의 홀수 층은 다음 짝수 층 값을 복사한다. L 루프를 닫는다(100). 원문: `IF(ISCI(1).EQ.1)THEN` (60) / `DO K=1,KS,2` (63) / `SAL(L,K)=SAL(L,K+1)` (64) / `SAL1(L,K)=SAL1(L,K+1)` (65) / `IF(ISCI(2).EQ.1)THEN` (68) / `DO K=1,KS,2` (71) / `TEM(L,K)=TEM(L,K+1)` (72) / `TEM1(L,K)=TEM1(L,K+1)` (73) / `IF(ISCI(3).EQ.1)THEN` (76) / `DO K=1,KS,2` (79) / `DYE(L,K)=DYE(L,K+1)` (80) / `DYE1(L,K)=DYE1(L,K+1)` (81) / `IF(ISCI(4).EQ.1)THEN` (84) / `DO K=1,KS,2` (87) / `SED(L,K,1)=SED(L,K+1,1)` (88) / `SED1(L,K,1)=SED1(L,K+1,1)` (89) / `IF(ISCI(5).EQ.1)THEN` (92) / `DO K=1,KS,2` (95) / `SFL(L,K)=SFL(L,K+1)` (96) / `SFL2(L,K)=SFL2(L,K+1)` (97). |
| 102–127 | 시작 시 6행 RESTIN2 루틴 안. M=1..5에서 ISCI(M)=1인 성분만 남·서·동·북 경계의 NLO·CLO 배열을 K=2..KC의 짝수 층에 읽는다(102–126). 방향별 경계 수는 NCBS·NCBW·NCBE·NCBN이고 입력 오류 표지는 1000이다(105–123). 원문: `DO M=1,5` (102) / `IF(ISCI(M).EQ.1)THEN` (103) / `DO LL=1,NCBS` (105) / `DO LL=1,NCBW` (110) / `DO LL=1,NCBE` (115) / `DO LL=1,NCBN` (120). |
| 128–155 | 시작 시 6행 RESTIN2 루틴 안. M=1..5·K=1..KS의 홀수 층에서 네 방향 NLO·CLO에 다음 짝수 층 값을 복사한다(128–152). 이 복사 루프에는 ISCI 선택 조건이 없다. RESTART.INP를 닫는다(154). 원문: `DO M=1,5` (128) / `DO K=1,KS,2` (129) / `DO LL=1,NCBS` (131) / `NLOS(LL,K,M)=NLOS(LL,K+1,M)` (132) / `CLOS(LL,K,M)=CLOS(LL,K+1,M)` (133) / `DO LL=1,NCBW` (136) / `NLOW(LL,K,M)=NLOW(LL,K+1,M)` (137) / `CLOW(LL,K,M)=CLOW(LL,K+1,M)` (138) / `DO LL=1,NCBE` (141) / `NLOE(LL,K,M)=NLOE(LL,K+1,M)` (142) / `CLOE(LL,K,M)=CLOE(LL,K+1,M)` (143) / `DO LL=1,NCBN` (146) / `NLON(LL,K,M)=NLON(LL,K+1,M)` (147) / `CLON(LL,K,M)=CLON(LL,K+1,M)` (148). |
| 156–196 | 시작 시 6행 RESTIN2 루틴 안. K=1..KC에서 경계 인덱스 1·LC의 SAL·TEM·DYE·SED 첫 성분·SFL·CWQ와 현재·이전 수평 유량·수질 유량을 0으로 둔다(156–193). 구분 주석까지 포함한다(194–196). 원문: `DO K=1,KC` (156) / `SAL(1,K)=0.` (157) / `TEM(1,K)=0.` (158) / `DYE(1,K)=0.` (159) / `SED(1,K,1)=0.` (160) / `SFL(1,K)=0.` (161) / `CWQ(1,K)=0.` (162) / `VHDX(1,K)=0.` (163) / `UHDY(1,K)=0.` (164) / `SAL1(1,K)=0.` (165) / `TEM1(1,K)=0.` (166) / `DYE1(1,K)=0.` (167) / `SED1(1,K,1)=0.` (168) / `SFL2(1,K)=0.` (169) / `CWQ2(1,K)=0.` (170) / `VHDX1(1,K)=0.` (171) / `UHDY1(1,K)=0.` (172) / `VHDXWQ(1,K)=0.` (173) / `UHDYWQ(1,K)=0.` (174) / `SAL(LC,K)=0.` (175) / `TEM(LC,K)=0.` (176) / `DYE(LC,K)=0.` (177) / `SED(LC,K,1)=0.` (178) / `SFL(LC,K)=0.` (179) / `CWQ(LC,K)=0.` (180) / `VHDX(LC,K)=0.` (181) / `UHDY(LC,K)=0.` (182) / `SAL1(LC,K)=0.` (183) / `TEM1(LC,K)=0.` (184) / `DYE1(LC,K)=0.` (185) / `SED1(LC,K,1)=0.` (186) / `SFL2(LC,K)=0.` (187) / `CWQ2(LC,K)=0.` (188) / `VHDX1(LC,K)=0.` (189) / `UHDY1(LC,K)=0.` (190) / `VHDXWQ(LC,K)=0.` (191) / `UHDYWQ(LC,K)=0.` (192). |
| 197–211 | 시작 시 6행 RESTIN2 루틴 안. LS=LSC(L)를 사용하여 H1P·HP의 이웃 산술 평균(arithmetic mean)으로 H1U·H1V·HU·HV를 계산한다(197–203). P1·P는 G와 셀 수심·BELV로 계산한다(201·204). HPI·HUI·HVI·H1UI·H1VI를 역수로 계산한다(205–210). 원문: `DO L=2,LA` (197) / `LS=LSC(L)` (198) / `H1U(L)=0.5*(H1P(L)+H1P(L-1))` (199) / `H1V(L)=0.5*(H1P(L)+H1P(LS))` (200) / `P1(L)=G*(H1P(L)+BELV(L))` (201) / `HU(L)=0.5*(HP(L)+HP(L-1))` (202) / `HV(L)=0.5*(HP(L)+HP(LS))` (203) / `P(L)=G*(HP(L)+BELV(L))` (204) / `HPI(L)=1./HP(L)` (205) / `HUI(L)=1./HU(L)` (206) / `HVI(L)=1./HV(L)` (207) / `H1UI(L)=1./H1U(L)` (208) / `H1VI(L)=1./H1V(L)` (209). |
| 212–240 | 시작 시 6행 RESTIN2 루틴 안. 면 길이·면 수심·속도로 현재·이전 UHDY·VHDX를 계산하고 SAL·SAL1을 MAX로 0 이상으로 제한한다(212–221). N을 0으로 두고 CALQVS(2)를 호출한다(223–224). K=1..KS에서 DZC·층별 및 수심 적분 유량 차이·QSUM·QSUME로 W·W1을 계산한다(226–239). 원문: `DO K=1,KC` (212) / `DO L=2,LA` (213) / `UHDY1(L,K)=DYU(L)*H1U(L)*U1(L,K)` (214) / `VHDX1(L,K)=DXV(L)*H1V(L)*V1(L,K)` (215) / `UHDY(L,K)=DYU(L)*HU(L)*U(L,K)` (216) / `VHDX(L,K)=DXV(L)*HV(L)*V(L,K)` (217) / `SAL(L,K)=MAX(SAL(L,K),0.)` (218) / `SAL1(L,K)=MAX(SAL1(L,K),0.)` (219) / `N=0` (223) / `CALL CALQVS (2)` (224) / `DO K=1,KS` (226) / `RDZC=DZC(K)` (227) / `DO L=2,LA` (228) / `LN=LNC(L)` (229) / `W(L,K)=SWB(L)*(W(L,K-1)` (230); `&       -RDZC*(UHDY(L+1,K)-UHDY(L,K)-UHDYE(L+1)+UHDYE(L)` (231); `&       +VHDX(LN,K)-VHDX(L,K)-VHDXE(LN)+VHDXE(L))*DXYIP(L))` (232); `&        +SWB(L)*( QSUM(L,K)-RDZC*QSUME(L) )*DXYIP(L)` (233) / `W1(L,K)=SWB(L)*(W1(L,K-1)` (234); `&       -RDZC*(UHDY1(L+1,K)-UHDY1(L,K)-UHDY1E(L+1)+UHDY1E(L)` (235); `&       +VHDX1(LN,K)-VHDX1(L,K)-VHDX1E(LN)+VHDX1E(L))*DXYIP(L))` (236); `&        +SWB(L)*( QSUM(L,K)-RDZC*QSUME(L) )*DXYIP(L)` (237). |
| 241–260 | 시작 시 6행 RESTIN2 루틴 안. 정상 경로는 1002 표지로 이동한다(245·249). ERR=1000 경로는 장치 6에 RESTART.INP 읽기 오류 메시지를 쓰고 STOP한다(246–248). 906·907·908 FORMAT과 구분 주석·RETURN·END를 포함한다(251–260). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 40–59·63–98: 입력은 짝수 수직층을 사용하고 보충 루프는 홀수 K에서 K+1 층을 참조한다. KC의 짝수 여부 또는 K+1≤KC를 검사하는 분기는 이 파일에 없다.
- 102–126·128–152: 경계 입력은 ISCI(M)=1에 한정한다. 홀수 층 복사는 ISCI를 검사하지 않고 M=1..5의 모든 성분에 실행한다.
- 85–89: 퇴적물 입력은 바닥 인덱스 1·성분 인덱스 1에 고정되어 있다. 이 블록에는 NSED 성분 루프가 없다.
- 205–209: 다섯 수심 역수는 HP·HU·HV·H1U·H1V를 분모로 사용한다. 이 블록에는 0 수심을 검사하는 분기가 없다.
- 35·223: NREST를 읽는다. 이 파일의 이후 활성 문장은 NREST를 참조하지 않으며 N을 0으로 설정한다.
