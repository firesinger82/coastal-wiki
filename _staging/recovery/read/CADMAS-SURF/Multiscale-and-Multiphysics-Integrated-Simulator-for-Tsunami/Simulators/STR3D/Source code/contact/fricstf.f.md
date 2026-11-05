---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/contact/fricstf.f
lines: 48
sha256: 2c7957a1a94252bcf21c69784e44151488c12d23f0e903cc6868c1d6fc272561
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# fricstf.f — 판독 구간 기록

구간은 1행부터 48행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–13 | 루틴·암시적 자료형과 인수 및 작업 배열 차원을 선언한다(1–12). 원문: `      SUBROUTINE FRICSTF(STF,RHV,NESTF,NCRMAX,NRAMAX,NINDC,ISLV,INDC` `     &                  ,IEDG,IELC,IELQ,IEDQ,IFCQ,IFRIC,U0,RL0,FRIC,UG` `     &                  ,DUG,INDOF,INDMPC,MPCF,RMPC,IDSK,IDCG,ISOLV` `     &                  ,IFMDL,MITER0,IDYN,BETA,DT,ITER,ITER2,ITO)` (1–4, 하나의 고정형식 연속문); `      IMPLICIT REAL*8(A-H,O-Z)` (6); `      DIMENSION U0(3,4,NINDC),RL0(3,NINDC),ISLV(2,NINDC),INDC(NINDC)` `     &         ,IEDG(6,*),IELC(3,*),UG(6,*),IFRIC(10,NINDC)` `     &         ,FRIC(10,NINDC),KN(5),ESTF(NESTF),INDOF(6,*)` `     &         ,INDMPC(2,6,*),MPCF(2,*),RMPC(*),IDCR(2,NCRMAX),RHV(*)` `     &         ,DUG(6,*),STF(*),IDSK(*),IDCG(*),IELQ(4,*),IFCQ(*)` `     &         ,IEDQ(*),RAMBDA(NRAMAX),WK(NRAMAX)` (7–12, 하나의 고정형식 연속문). [11-04 전수 검증 정정] |
| 14–48 | 시작 시 1행 FRICSTF 루틴 안이다. 비활성 마찰은 건너뛰고 상태 2는 ESTFEDGE, 상태 3은 ESTFFACE를 호출한다(14–31). IDYN=1이면 상삼각 저장 길이를 계산하여 ESTF에 BETA를 곱한다(33–36). MPCTRNS를 호출한다(38–39). ITER와 ITER2가 모두 1일 때 SPCDRHV를 호출한다(41–42). CGADM에 STF·ESTF 등을 전달한다(44). 해석: MPCTRNS 호출은 구속 변환에 해당하고 CGADM 호출은 전역 행렬 조립에 해당한다. 루프·루틴을 닫는다(46–48). 원문: `      DO I = 1, NINDC` (14); `        IF( IFRIC(1,I) == 0 ) CYCLE` (16); `        NS = INDC(I)` (18); `        IST = ISLV(1,I)` (19); `        MA  = ISLV(2,I)` (20); `        IF( IST == 2 ) THEN` (22); `          CALL ESTFEDGE(ND,KN,ESTF,NS,IEDG(1,MA),IEDQ(MA),IELQ,U0(1,1,I)` `     &                 ,RL0(1,I),FRIC(1,I),FRIC(2,I),FRIC(3,I),FRIC(6,I)` `     &                 ,UG,DT,IFMDL)` (23–25, 하나의 고정형식 연속문); `        ELSEIF( IST == 3 ) THEN` (26); `          CALL ESTFFACE(ND,KN,ESTF,NS,IELC(1,MA),IFCQ(MA),IELQ,U0(1,1,I)` `     &                 ,RL0(1,I),IFRIC(2,I),IFRIC(3,I),IFRIC(9,I)` `     &                 ,FRIC(1,I),FRIC(2,I),FRIC(3,I),FRIC(6,I),UG,DT` `     &                 ,IFMDL,MITER0,IDYN,ITER)` (27–30, 하나의 고정형식 연속문); `        IF( IDYN == 1 ) THEN` (33); `          N = 3*ND * ( 3*ND + 1 ) / 2` (34); `          ESTF(1:N) = BETA * ESTF(1:N)` (35); `        CALL MPCTRNS(1,KN,ND,3,ND*3,RAMBDA,NRAMAX,INDOF,INDMPC,MPCF,RMPC` `     &              ,WK,ESTF,IDCR,NCR)` (38–39, 하나의 고정형식 연속문); `        IF( ITER == 1 .AND. ITER2 == 1 ) ` `     &    CALL SPCDRHV(RHV,ESTF,IDCR,NCR,INDOF,DUG)` (41–42, 하나의 고정형식 연속문); `        CALL CGADM(STF,ESTF,IDCR,NCR,IDSK,IDCG,INDOF,ISOLV,ITO)` (44). [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 22–31·33–44: 상태 2·3 이외의 ELSE는 없으며, 강성 계산 호출 뒤의 변환·조립은 상태 분기 밖에 있다.
