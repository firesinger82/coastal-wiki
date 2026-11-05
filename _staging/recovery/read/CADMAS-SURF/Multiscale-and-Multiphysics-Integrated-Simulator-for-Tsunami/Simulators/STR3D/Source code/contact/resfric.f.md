---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/contact/resfric.f
lines: 71
sha256: ea4b6422bbfb9459f0785f8ceb939698238905da046f3214b108c8d440be3851
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# resfric.f — 판독 구간 기록

구간은 1행부터 71행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–29 | RESFRIC는 MPI_PARAM 모듈을 사용한다(4). EPSA,EPSR을 RR 값의 1.D-1배로 설정하고 FNRM1을 FNRM에 복사한다(10–13). 마찰 활성 절점 중 NS<=NNODI이며 INDOF>0인 세 방향의 RES 제곱을 물체 쌍별 RNRM에 누적한다(15–28). DATA ICHK=0과 배열 선언을 포함한다. 원문: 연속문(1–2): `      SUBROUTINE RESFRIC(IFRIC,NNODI,NBDY,NINDC,INDOF,INDC,RES,FNRM1` (1); `     &                  ,RR,ISTEP,ITER2,ITER)` (2). `      USE MPI_PARAM` (4). `      IMPLICIT REAL*8(A-H,O-Z)` (5). 연속문(6–7): `      DIMENSION RNRM(NBDY,NBDY),IFRIC(10,NINDC),INDC(NINDC),INDOF(6,*)` (6); `     &         ,RES(*),NCONV(NBDY,NBDY),DSUM(NBDY,NBDY),RR(*)` (7). `      DATA ICHK / 0 /` (8). `      EPSA = RR(3) * 1.D-1` (10). `      EPSR = RR(6) * 1.D-1` (11). `      FNRM = FNRM1` (13). `      RNRM(:,:) = 0.D0` (15). `      DO I = 1, NINDC` (17). `        IF( IFRIC(1,I) == 0 ) CYCLE` (18). `        NS = INDC(I)` (19). `        IF( NS > NNODI ) CYCLE` (20). `        IBDY = IFRIC(5,I)` (21). `        JBDY = IFRIC(6,I)` (22). `        DO J = 1, 3` (23). `          IFR = INDOF(J,NS)` (24). 연속문(25–26): `          IF( IFR > 0 )` (25); `     &      RNRM(IBDY,JBDY) = RNRM(IBDY,JBDY) + RES(IFR) * RES(IFR)` (26). `        ENDDO` (27). `      ENDDO` (28). |
| 30–37 | 시작 시 1–2행 RESFRIC 루틴 안. MYRANK>0이면 FNRM의 제곱을 CG_MPI_ALLREDUCE_D(FNRM,DUM,1,0)로 모으고 제곱근을 취한다(30–33). RNRM은 CG_MPI_ALLREDUCE_D(RNRM,DSUM,NBDY*NBDY,0)로 모아 복사한다(34–35). MPI 래퍼(wrapper)의 호출 인수는 아래 원문과 같다. 원문: `      IF( MYRANK > 0 ) THEN` (30). `        FNRM = FNRM * FNRM` (31). `        CALL CG_MPI_ALLREDUCE_D(FNRM,DUM,1,0)` (32). `        FNRM = DSQRT(DUM)` (33). `        CALL CG_MPI_ALLREDUCE_D(RNRM,DSUM,NBDY*NBDY,0)` (34). `        RNRM(:,:) = DSUM(:,:)` (35). `      ENDIF` (36). |
| 38–59 | 시작 시 1–2행 RESFRIC 루틴 안. ITER>1일 때만 RNRM의 제곱근을 취하고 상대 잔차(residual) 또는 절대 잔차 조건으로 NCONV를 0 또는 1로 정한다(38–51). 마찰 활성 접촉마다 해당 물체 쌍의 NCONV를 IFRIC(7,I)에 복사한다(53–58). 원문: `      IF( ITER > 1 ) THEN` (38). `        DO I = 1, NBDY` (40). `          DO J = 1, NBDY` (41). `            RNRM(I,J) = DSQRT( RNRM(I,J) )` (42). `            IF( RNRM(I,J) / FNRM < EPSR .OR. RNRM(I,J) < EPSA ) THEN` (43). `              NCONV(I,J) = 0` (44). `            ELSE` (45). `              NCONV(I,J) = 1` (46). `            ENDIF` (47). `          ENDDO` (48). `        ENDDO` (49). `      ENDIF` (51). `      DO I = 1, NINDC` (53). `        IF( IFRIC(1,I) == 0 ) CYCLE` (54). `        IBDY = IFRIC(5,I)` (55). `        JBDY = IFRIC(6,I)` (56). `        IFRIC(7,I) = NCONV(IBDY,JBDY)` (57). `      ENDDO` (58). |
| 60–71 | 시작 시 1–2행 RESFRIC 루틴 안. ICHK=0이면 반환한다(60). 그 밖에는 단계·반복 번호를 53번 장치에 쓰고 양수 RNRM만 출력한다(62–69). END를 포함한다. 원문: `      IF( ICHK == 0 ) RETURN` (60). `      WRITE(53,'(A,I6,2I3)') 'STEP, ITER2, ITER = ',ISTEP,ITER2,ITER` (62). `      DO I = 1, NBDY` (64). `        DO J = 1, NBDY` (65). 연속문(66–67): `          IF( RNRM(I,J) > 0.D0 )` (66); `     &      WRITE(53,'(2I3,1PE10.2)') I,J,RNRM(I,J)` (67). `        ENDDO` (68). `      ENDDO` (69). `      END` (71). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 38–57: NCONV는 ITER>1 조건 안에서만 설정되지만 IFRIC(7,I)로 복사하는 루프는 이 조건 밖에 있다.
- 43: RNRM/FNRM을 계산하기 전에 FNRM=0 검사는 없다.
- 8·60: ICHK는 DATA에서 0으로 설정되며 이 파일에 다른 ICHK 대입은 없다.
