---
file: models/EFDC/raw/source_code/EFDC-GVC/calbal3.for
lines: 184
sha256: 82553593803e6324003b2ddfd7d5ab3fb35fd0137747f657e98a7134539d565e
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# calbal3.for — 판독 구간 기록

구간은 1행부터 184행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–37 | 구분 주석과 `SUBROUTINE CALBAL3` (7) 입구. 버전·수정일·변경 이력 머리말과 체적(volume)·질량(mass)·운동량(momentum)·에너지(energy) 수지 목적 주석이다(9–21). `INCLUDE 'EFDC.PAR'` (25); `INCLUDE 'EFDC.CMN'` (26)로 공통 선언을 포함한다. 30행 CONT 배열 선언은 주석이다. 내부 유입원(source)·유출원(sink) 누적 주석이다(34). |
| 38–55 | 시작 시 7행 CALBAL3 루틴 안. L=2..LA(38)의 체적 유출 누적은 `VOLOUT=VOLOUT-QSUME(L)` (39). K=1..KC·LL=1..NQSIJ(44–45)의 L=LQS(LL)(46) 위치에너지(potential energy) 유량(flux)은 `PPEOUT=PPEOUT-QSS(K,LL)*G*( 0.5*(BELV(L)+BELV(L-1))` (48); `&       +0.125*(HP(L)+H2P(L)+HP(L-1)+H2P(L-1))*(Z(K)+Z(K-1)) )` (49). 두 루프를 닫는다(51–52). |
| 56–76 | 시작 시 7행 CALBAL3 루틴 안. `IF(ISTRAN(1).GE.1)THEN` (56)이면 K=1..KC·L=2..LC(58–59)에서 CONT=SAL을 복사한다(60). NS=1..NQSIJ(64)의 L=LQS(NS)·NQSTMP=NQSERQ(NS)·NCSTMP=NCSERQ(NS,1)를 복사한다(65–67). K=1..KC(68)의 염 질량(salt mass) 누적은 `SALOUT=SALOUT` (69); `&           -MAX(QSS(K,NS),0.)*CQS(K,NS,1)` (70); `&           -MIN(QSS(K,NS),0.)*SAL(L,K)` (71); `&           -MAX(QSERT(K,NQSTMP),0.)*CSERT(K,NCSTMP,1)` (72); `&           -MIN(QSERT(K,NQSTMP),0.)*SAL(L,K)` (73). 양수 유량에는 지정 농도·시계열(time series) 농도, 음수 유량에는 SAL을 곱한다. |
| 77–95 | 시작 시 7행 루틴·56행 ISTRAN(1) 분기 안. NCTL=1..NQCTL(77)에서 `RQWD=1.` (78)을 설정한다. 상류 격자 IU·JU·LU와 하류 격자 ID·JD를 얻는다(79–83). `IF(ID.EQ.0.AND.JD.EQ.0)THEN` (84)이면 LD=LC·RQWD=0(85–86), `ELSE` (87)이면 LD=LIJ(ID,JD)(88). K=1..KC(90)의 제어 유량 누적은 `SALOUT=SALOUT+QCTLT(K,NCTL)*CONT(LU,K)` (91); `&         -RQWD*QCTLT(K,NCTL)*CONT(LU,K)` (92). 두 루프를 닫는다(93–94). |
| 96–119 | 시작 시 7행 루틴·56행 ISTRAN(1) 분기 안. NWR=1..NQWR(96)의 상류·하류 좌표·층 번호 KU/KD와 LU/LD를 얻는다(97–104). NQSTMP·NCSTMP 모두 NQWRSERQ(NWR)를 복사한다(105–106). 취수·환수(withdrawal/return) 누적식은 `SALOUT=SALOUT+` (107); `&   ( (QWR(NWR)+QWRSERT(NQSTMP))*CONT(LU,KU) )` (108). `IF(LD.NE.1.OR.LD.NE.LC)THEN` (109)이면 `SALOUT=SALOUT-` (110); `&     ( QWR(NWR)*(CONT(LU,KU)+CQWR(NWR,1))` (111); `&      +QSERT(K,NQSTMP)*(CONT(LU,KU)+CQWRSERT(NCSTMP,1)) )` (112)로 환수 농도 항을 뺀다. 조건·NWR 루프·56행 조건을 닫는다(113–116). |
| 120–140 | 시작 시 7행 CALBAL3 루틴 안. `IF(ISTRAN(3).GE.1)THEN` (120)이면 K=1..KC·L=2..LC(122–123)에서 CONT=DYE를 복사한다(124). NS=1..NQSIJ(128)의 L=LQS(NS)·NQSTMP=NQSERQ(NS)·NCSTMP=NCSERQ(NS,3)를 복사한다(129–131). K=1..KC(132)의 염료 질량(dye mass) 누적은 `DYEOUT=DYEOUT` (133); `&           -MAX(QSS(K,NS),0.)*CQS(K,NS,3)` (134); `&           -MIN(QSS(K,NS),0.)*DYE(L,K)` (135); `&           -MAX(QSERT(K,NQSTMP),0.)*CSERT(K,NCSTMP,3)` (136); `&           -MIN(QSERT(K,NQSTMP),0.)*DYE(L,K)` (137). 양수 유량에는 지정·시계열 농도, 음수 유량에는 DYE를 곱한다. |
| 141–159 | 시작 시 7행 루틴·120행 ISTRAN(3) 분기 안. NCTL=1..NQCTL(141)에서 `RQWD=1.` (142)을 설정한다. 상류 격자 IU·JU·LU와 하류 격자 ID·JD를 얻는다(143–147). `IF(ID.EQ.0.AND.JD.EQ.0)THEN` (148)이면 LD=LC·RQWD=0(149–150), `ELSE` (151)이면 LD=LIJ(ID,JD)(152). K=1..KC(154)의 제어 유량 누적은 `DYEOUT=DYEOUT+QCTLT(K,NCTL)*CONT(LU,K)` (155); `&        -RQWD*QCTLT(K,NCTL)*CONT(LU,K)` (156). 두 루프를 닫는다(157–158). |
| 160–184 | 시작 시 7행 루틴·120행 ISTRAN(3) 분기 안. NWR=1..NQWR(160)의 상류·하류 좌표·층 번호 KU/KD와 LU/LD를 얻는다(161–168). NQSTMP·NCSTMP 모두 NQWRSERQ(NWR)를 복사한다(169–170). 취수·환수 누적식은 `DYEOUT=DYEOUT+` (171); `&   ( (QWR(NWR)+QWRSERT(NQSTMP))*CONT(LU,KU) )` (172). `IF(LD.NE.1.OR.LD.NE.LC)THEN` (173)이면 `DYEOUT=DYEOUT-` (174); `&     ( QWR(NWR)*(CONT(LU,KU)+CQWR(NWR,3))` (175); `&      +QSERT(K,NQSTMP)*(CONT(LU,KU)+CQWRSERT(NCSTMP,3)) )` (176)로 환수 농도 항을 뺀다. 조건·NWR 루프·120행 조건을 닫고 RETURN·END로 종료한다(177–184). 실행 CALL 문은 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 84–92·148–156: 하류 LD를 계산하지만 제어 유량 누적의 두 항은 모두 CONT(LU,K)를 사용한다. RQWD=1이면 이 두 항은 서로 상쇄된다.
- 109·173: 환수 조건은 LD.NE.1.OR.LD.NE.LC이다. LC가 1과 다르면 LD 값과 관계없이 이 조건은 참이다.
- 107–112·171–176: 취수 증가항은 QWRSERT(NQSTMP)를 사용한다. 환수 감소항은 QSERT(K,NQSTMP)를 사용한다.
- 96–114·160–178: NWR 루프에는 K 대입이나 K 루프가 없다. 해당 루프의 환수 식은 QSERT(K,NQSTMP)를 참조한다(112·176). 앞의 K 루프는 이미 종료된 위치이다(93·157).
- 99–112·163–176: KU는 CONT(LU,KU)에 사용된다. KD는 KQWRD에서 복사한 뒤 이 파일의 계산식에서 참조되지 않는다.
- 105–106·169–170: NQSTMP와 NCSTMP는 모두 NQWRSERQ(NWR)를 사용한다. 점 유입원 농도 인덱스 NCSTMP는 NCSERQ(NS,1)·NCSERQ(NS,3)를 사용한다(67·131).
