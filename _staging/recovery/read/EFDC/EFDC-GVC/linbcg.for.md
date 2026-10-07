---
file: models/EFDC/raw/source_code/EFDC-GVC/linbcg.for
lines: 112
sha256: aa68136de0d73c114883272f25f21e42a9b16dc0c1420889e6c4dd786271277a
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# linbcg.for — 판독 구간 기록

구간은 1행부터 112행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–31 | 구분 주석과 `SUBROUTINE LINBCG (N,B,X,ITOL,TOL,ITMAX,ITER,ERR,IRVEC)` 입구(1–6). EFDC-FULL 1.0a 및 2001-11-01 수정 주석, 변경 기록란(8–17). 호출 인수 대응 예시 주석(21), `INCLUDE 'EFDC.PAR'` (23), `PARAMETER (EPS=1.D-14)` (25). ATIMES·ASOLVE·SNRM 사용 주석(27), 작업 벡터(vector) P·PP·R·RR·Z·ZZ 및 인수 B·X를 LCM 크기로 선언(29–30). |
| 32–53 | 시작 시 6행 LINBCG 루틴 안. ITER=0(32), `CALL ATIMES(X,R)` (33), J=1..N에서 잔차(residual) `R(J)=B(J)-R(J)` (35), RR에 복사(36). `IF(IRVEC.GE.50) CALL ATIMES(R,RR)` (38). `ZNRM=1.D0` (39). `IF(ITOL.EQ.1)THEN` (40)은 `BNRM=SNRM(N,B,ITOL)` (41). 병렬 `ELSE IF(ITOL.EQ.2)THEN` (42)은 `CALL ASOLVE(B,Z)` (43), `BNRM=SNRM(N,Z,ITOL)` (44). 병렬 `ELSE IF(ITOL.EQ.3.OR.ITOL.EQ.4)THEN` (45)은 `CALL ASOLVE(B,Z)` (46), `BNRM=SNRM(N,Z,ITOL)` (47), `CALL ASOLVE(R,Z)` (48), `ZNRM=SNRM(N,Z,ITOL)` (49). `ELSE` (50)는 잘못된 ITOL이라는 PAUSE(51). 분기 종료 뒤 `CALL ASOLVE(R,Z)` (53). ASOLVE 내부의 전처리(preconditioning) 방식은 이 파일에 제시되지 않는다. |
| 54–87 | 시작 시 6행 LINBCG 루틴 안. 반복 레이블의 원문은 `100   IF(ITER.LE.ITMAX)THEN` (54). `ITER=ITER+1` (55), 이전 ZNRM 복사(56), `CALL ASOLVE(RR,ZZ)` (57). BKNUM=0, J 루프에서 `BKNUM=BKNUM+Z(J)*RR(J)` (60). `IF(ITER.EQ.1)THEN` (62)은 P=Z·PP=ZZ 복사(63–66). `ELSE` (67)는 `BK=BKNUM/BKDEN` (68), J 루프의 `P(J)=BK*P(J)+Z(J)` (70), `PP(J)=BK*PP(J)+ZZ(J)` (71). 분기 뒤 BKDEN에 BKNUM 복사(74), `CALL ATIMES(P,Z)` (75), AKDEN=0, J 루프에서 `AKDEN=AKDEN+Z(J)*PP(J)` (78), `AK=BKNUM/AKDEN` (80), `CALL ATIMES(PP,ZZ)` (81). 해(solution)·두 잔차 갱신은 `X(J)=X(J)+AK*P(J)` (83), `R(J)=R(J)-AK*Z(J)` (84), `RR(J)=RR(J)-AK*ZZ(J)` (85). `CALL ASOLVE(R,Z)` (87). 54행 반복 분기는 다음 구간까지 열린다. |
| 88–107 | 시작 시 6행 LINBCG·54행 ITER<=ITMAX 분기 안. `IF(ITOL.EQ.1.OR.ITOL.EQ.2)THEN` (88)은 `ZNRM=1.D0` (89), `ERR=SNRM(N,R,ITOL)/BNRM` (90). 병렬 `ELSE IF(ITOL.EQ.3.OR.ITOL.EQ.4)THEN` (91)은 `ZNRM=SNRM(N,Z,ITOL)` (92). 그 안 `IF(ABS(ZM1NRM-ZNRM).GT.EPS*ZNRM)THEN` (93)은 `DXNRM=ABS(AK)*SNRM(N,P,ITOL)` (94), `ERR=ZNRM/ABS(ZM1NRM-ZNRM)*DXNRM` (95). `ELSE` (96)는 `ERR=ZNRM/BNRM` (97) 및 `GOTO 100` (98). 이 조건 밖에서 `XNRM=SNRM(N,X,ITOL)` (100). `IF(ERR.LE.0.5D0*XNRM)THEN` (101)은 `ERR=ERR/XNRM` (102). `ELSE` (103)는 `ERR=ZNRM/BNRM` (104) 및 `GOTO 100` (105). 오차(error) 분기 종료(106–107). |
| 108–112 | 시작 시 6행 LINBCG·54행 ITER<=ITMAX 분기 안. ITER·ERR 진단 WRITE는 주석(108). `IF(ERR.GT.TOL) GOTO 100` (109)으로 허용 오차(tolerance)를 초과하면 반복한다. 54행 분기 종료(110), RETURN·END(111–112). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 32·54–55·109–110: 반복 진입 조건은 ITER<=ITMAX이다. 조건 안에서 ITER를 먼저 증가시킨다. 반복이 계속되면 ITER=ITMAX에서 들어가 ITER=ITMAX+1인 계산을 수행한다.
- 68·80·90·95·97·102·104: BKDEN·AKDEN·BNRM·XNRM을 분모에 사용한다. 각 나눗셈 앞에 해당 분모의 0 검사는 없다. 95행의 ZM1NRM-ZNRM은 93행 조건을 거친다.
- 42–44·88–90: ITOL=2의 BNRM은 ASOLVE(B,Z) 결과의 SNRM이다. 같은 ITOL의 ERR 분자는 ASOLVE 결과 Z가 아닌 R의 SNRM이다.
- 93–105·109: 두 오차 추정의 else 경로는 ERR을 설정한 뒤 곧바로 GOTO 100을 실행한다. 이 경로는 109행의 ERR>TOL 검사를 건너뛴다.
- 32·54·88–110: 이 루틴은 ITER를 0으로 설정하지만 ERR의 초기 대입은 반복 안에 있다. 최초 54행 조건이 불성립하면 ERR에 대입하는 실행문을 거치지 않고 RETURN한다.

