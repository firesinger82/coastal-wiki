---
file: models/EFDC/raw/source_code/EFDC-GVC/cbalev3.for
lines: 186
sha256: 010dd0eee7f28dd84125243684761a2458d4ef2a309da229ad33c36c153557e6
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# cbalev3.for — 판독 구간 기록

구간은 1행부터 186행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–36 | 구분 주석과 CBALEV3 선언을 포함한다(1–6). 머리말은 EFDC-FULL 1.0a와 2001-11-01 수정일을 적는다(8–10). CBALEV 루틴들이 전체 체적(volume)·질량(mass)·운동량(momentum)·에너지(energy) 수지(balance)를 계산한다는 주석이 있다(19–20). EFDC.PAR와 EFDC.CMN을 포함한다(24–25). 포함 파일 내부는 이 기록의 판독 대상이 아니다. CONT의 DIMENSION은 주석이다(29). 내부 생성·소멸(source–sink) 누적을 안내한다(33–35). |
| 37–54 | 시작 시 6행 CBALEV3 루틴 안. L=2..LA에서 QSUME를 VOLOUTE에서 뺀다(37–39). K=1..KC와 LL=1..NQSIJ에서 LQS 셀을 가져온다(43–45). QSS·G와 L 및 L-1의 BELV·HP·H2P 및 층 높이로 PPEOUTE를 갱신한다(47–51). 원문 실행문: `DO L=2,LA` (37); `VOLOUTE=VOLOUTE-QSUME(L)` (38); `DO K=1,KC` (43); `DO LL=1,NQSIJ` (44); `L=LQS(LL)` (45); `PPEOUTE=PPEOUTE-QSS(K,LL)*G*( 0.5*(BELV(L)+BELV(L-1))` (47); `&       +0.125*(HP(L)+H2P(L)+HP(L-1)+H2P(L-1))*(Z(K)+Z(K-1)) )` (48). |
| 55–75 | 시작 시 6행 CBALEV3 루틴 안. ISTRAN(1)>=1의 염분(salt) 분기를 연다(55). K=1..KC와 L=2..LC에서 SAL을 CONT에 복사한다(57–61). NS=1..NQSIJ의 유량 시계열(time series)과 농도 시계열 번호를 가져온다(63–66). QSS와 QSERT의 양수 부분은 CQS 또는 CSERT를 사용하고 음수 부분은 셀의 SAL을 사용해 SALOUTE에서 뺀다(67–74). 원문 실행문: `IF(ISTRAN(1).GE.1)THEN` (55); `DO K=1,KC` (57); `DO L=2,LC` (58); `CONT(L,K)=SAL(L,K)` (59); `DO NS=1,NQSIJ` (63); `L=LQS(NS)` (64); `NQSTMP=NQSERQ(NS)` (65); `NCSTMP=NCSERQ(NS,1)` (66); `DO K=1,KC` (67); `SALOUTE=SALOUTE` (68); `&           -MAX(QSS(K,NS),0.)*CQS(K,NS,1)` (69); `&           -MIN(QSS(K,NS),0.)*SAL(L,K)` (70); `&           -MAX(QSERT(K,NQSTMP),0.)*CSERT(K,NCSTMP,1)` (71); `&           -MIN(QSERT(K,NQSTMP),0.)*SAL(L,K)` (72). |
| 76–95 | 시작 시 6행 CBALEV3 루틴·55행 염분 분기 안. NCTL=1..NQCTL에서 상류·하류 좌표와 LU를 구한다(76–82). RQWD의 초기값은 1이다(77). 하류 ID=0 및 JD=0이면 LD=LC와 RQWD=0을 설정하고 ELSE는 LIJ로 LD를 구한다(83–88). K=1..KC에서 QCTLT*CONT(LU,K)를 더한 뒤 RQWD를 곱한 같은 항을 뺀다(89–93). 원문 실행문: `DO NCTL=1,NQCTL` (76); `RQWD=1.` (77); `IU=IQCTLU(NCTL)` (78); `JU=JQCTLU(NCTL)` (79); `LU=LIJ(IU,JU)` (80); `ID=IQCTLD(NCTL)` (81); `JD=JQCTLD(NCTL)` (82); `IF(ID.EQ.0.AND.JD.EQ.0)THEN` (83); `LD=LC` (84); `RQWD=0.` (85); `ELSE` (86); `LD=LIJ(ID,JD)` (87); `DO K=1,KC` (89); `SALOUTE=SALOUTE+QCTLT(K,NCTL)*CONT(LU,K)` (90); `&         -RQWD*QCTLT(K,NCTL)*CONT(LU,K)` (91). |
| 96–120 | 시작 시 6행 CBALEV3 루틴·55행 염분 분기 안. NWR=1..NQWR에서 상류·하류 좌표 및 층과 셀 인덱스를 구한다(96–104). NQSTMP와 NCSTMP에는 모두 NQWRSERQ를 대입한다(105–106). QWR+QWRSERT에 CONT(LU,KU)를 곱해 SALOUTE에 더한다(107–108). LD 조건이 참이면 CQWR 및 CQWRSERT를 포함하는 반환 항을 뺀다(109–113). NWR 루프와 염분 분기를 닫는다(114·117). 원문 실행문: `DO NWR=1,NQWR` (96); `IU=IQWRU(NWR)` (97); `JU=JQWRU(NWR)` (98); `KU=KQWRU(NWR)` (99); `ID=IQWRD(NWR)` (100); `JD=JQWRD(NWR)` (101); `KD=KQWRD(NWR)` (102); `LU=LIJ(IU,JU)` (103); `LD=LIJ(ID,JD)` (104); `NQSTMP=NQWRSERQ(NWR)` (105); `NCSTMP=NQWRSERQ(NWR)` (106); `SALOUTE=SALOUTE+` (107); `&   ( (QWR(NWR)+QWRSERT(NQSTMP))*CONT(LU,KU) )` (108); `IF(LD.NE.1.OR.LD.NE.LC)THEN` (109); `SALOUTE=SALOUTE-` (110); `&     ( QWR(NWR)*(CONT(LU,KU)+CQWR(NWR,1))` (111); `&      +QSERT(K,NQSTMP)*(CONT(LU,KU)+CQWRSERT(NCSTMP,1)) )` (112). |
| 121–141 | 시작 시 6행 CBALEV3 루틴 안. ISTRAN(3)>=1의 염료(dye) 분기를 연다(121). K=1..KC와 L=2..LC에서 DYE를 CONT에 복사한다(123–127). NS=1..NQSIJ에서 NQSTMP와 NCSTMP를 구한다(129–132). QSS와 QSERT의 양수 부분은 CQS와 CSERT의 성분 3을 사용한다(134–138). 음수 부분은 셀의 DYE를 사용한다(136·138). 두 루프를 닫는다(139–140). 원문 실행문: `IF(ISTRAN(3).GE.1)THEN` (121); `DO K=1,KC` (123); `DO L=2,LC` (124); `CONT(L,K)=DYE(L,K)` (125); `DO NS=1,NQSIJ` (129); `L=LQS(NS)` (130); `NQSTMP=NQSERQ(NS)` (131); `NCSTMP=NCSERQ(NS,1)` (132); `DO K=1,KC` (133); `DYEOUTE=DYEOUTE` (134); `&           -MAX(QSS(K,NS),0.)*CQS(K,NS,3)` (135); `&           -MIN(QSS(K,NS),0.)*DYE(L,K)` (136); `&           -MAX(QSERT(K,NQSTMP),0.)*CSERT(K,NCSTMP,3)` (137); `&           -MIN(QSERT(K,NQSTMP),0.)*DYE(L,K)` (138). |
| 142–160 | 시작 시 6행 CBALEV3 루틴·121행 염료 분기 안. NCTL=1..NQCTL에서 RQWD를 1로 시작한다(142–148). 하류 ID=0 및 JD=0이면 LD=LC와 RQWD=0을 설정한다(149–154). K=1..KC에서 QCTLT*CONT(LU,K)를 더한 뒤 RQWD를 곱한 같은 항을 뺀다(155–159). 원문 실행문: `DO NCTL=1,NQCTL` (142); `RQWD=1.` (143); `IU=IQCTLU(NCTL)` (144); `JU=JQCTLU(NCTL)` (145); `LU=LIJ(IU,JU)` (146); `ID=IQCTLD(NCTL)` (147); `JD=JQCTLD(NCTL)` (148); `IF(ID.EQ.0.AND.JD.EQ.0)THEN` (149); `LD=LC` (150); `RQWD=0.` (151); `ELSE` (152); `LD=LIJ(ID,JD)` (153); `DO K=1,KC` (155); `DYEOUTE=DYEOUTE+QCTLT(K,NCTL)*CONT(LU,K)` (156); `&        -RQWD*QCTLT(K,NCTL)*CONT(LU,K)` (157). |
| 161–182 | 시작 시 6행 CBALEV3 루틴·121행 염료 분기 안. NWR=1..NQWR에서 상류·하류 좌표·층·셀 인덱스를 구한다(161–169). NQSTMP와 NCSTMP에 NQWRSERQ를 대입한다(170–171). QWR+QWRSERT에 CONT(LU,KU)를 곱해 DYEOUTE에 더한다(172–173). LD 조건이 참이면 CQWR와 CQWRSERT의 성분 3을 사용한 반환 항을 뺀다(174–178). NWR 루프와 염료 분기를 닫는다(179·181). 원문 실행문: `DO NWR=1,NQWR` (161); `IU=IQWRU(NWR)` (162); `JU=JQWRU(NWR)` (163); `KU=KQWRU(NWR)` (164); `ID=IQWRD(NWR)` (165); `JD=JQWRD(NWR)` (166); `KD=KQWRD(NWR)` (167); `LU=LIJ(IU,JU)` (168); `LD=LIJ(ID,JD)` (169); `NQSTMP=NQWRSERQ(NWR)` (170); `NCSTMP=NQWRSERQ(NWR)` (171); `DYEOUTE=DYEOUTE+` (172); `&   ( (QWR(NWR)+QWRSERT(NQSTMP))*CONT(LU,KU) )` (173); `IF(LD.NE.1.OR.LD.NE.LC)THEN` (174); `DYEOUTE=DYEOUTE-` (175); `&     ( QWR(NWR)*(CONT(LU,KU)+CQWR(NWR,3))` (176); `&      +QSERT(K,NQSTMP)*(CONT(LU,KU)+CQWRSERT(NCSTMP,3)) )` (177). |
| 183–186 | 시작 시 6행 CBALEV3 루틴 안. 구분 주석과 RETURN·END를 포함한다(183–186). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 78–91·144–157: 제어 유량 블록은 LD를 계산하지만 수지 식의 두 항은 모두 CONT(LU,K)를 사용한다. RQWD=1이면 두 항은 같은 값으로 상쇄된다.
- 109·174: 반환 항 조건은 `IF(LD.NE.1.OR.LD.NE.LC)THEN`이다. LC가 1이 아닌 경우 이 OR 조건은 모든 LD에 대해 참이다. LC의 실제 값은 포함 파일에서 확인하지 않았다.
- 66·132·135–138: 염분과 염료 블록의 NCSTMP는 모두 NCSERQ(NS,1)에서 가져온다. 염료 블록의 CQS와 CSERT 성분 인덱스는 3이다.
- 105–106·170–171: NQSTMP와 NCSTMP는 모두 NQWRSERQ(NWR)에서 가져온다.
- 107–112·172–177: 인출 항은 QWRSERT(NQSTMP)를 사용한다. 반환 항은 QSERT(K,NQSTMP)를 사용한다. 두 NWR 루프에는 K 대입문이 없으며 상류 층 KU를 별도로 읽는다.
- 102·167 및 107–112·172–177: KD에는 KQWRD(NWR)를 대입한다. 이 파일의 이후 계산식은 KD를 참조하지 않는다.
