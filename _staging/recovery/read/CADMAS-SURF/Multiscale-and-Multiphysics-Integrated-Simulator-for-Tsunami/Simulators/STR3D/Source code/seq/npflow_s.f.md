---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/seq/npflow_s.f
lines: 79
sha256: eaa2988b1afb3548ea9691589b8594175a7851e592c90cfab69c025aa137b639
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# npflow_s.f — 판독 구간 기록

구간은 1행부터 79행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–32 | NPFLOW_S의 연속 인수·모듈·암시적 형·배열 선언. DATA GRAV는 (0,0,-9.8)이다. FLI·FLO·FCP를 0으로 초기화한다. 유형 6 요소만 GNPFLW_S로 계산한다. 원문: 연속문(1–3): `      SUBROUTINE NPFLOW_S(FLI,FLO,FCP,VELG,MGP,VELE,RES,KK,RR,GRID,IELM` <br> `     &                   ,NM,AMAT,INDOP,UG1,UG2,UG3,PG1,PG3,DT1,DT2,IDYN` <br> `     &                   ,ICHK,ITO)`; `      USE MPI_PARAM` (5); `      IMPLICIT REAL*8(A-H,O-Z)` (6); 연속문(7–9): `      DIMENSION FLI(*),FLO(*),FCP(3,*),VELG(3,MGP,*),VELE(3,*),GRID(3,*)` <br> `     &         ,UG1(6,*),UG2(6,*),UG3(6,*),PG1(*),PG3(*),AMAT(33,*)` <br> `     &         ,GRAV(3),IELM(NM,*),KK(*),RR(*),RES(*),INDOP(*)`; `      DATA GRAV / 0.D0, 0.D0, -9.8D0 /` (10); `      NNOD = KK(8)` (12); `      NELM = KK(12)` (13); `      NNODI = KK(26)` (14); `      FLI(1:NNOD) = 0.` (16); `      FLO(1:NNOD) = 0.` (17); `      FCP(:,1:NNOD) = 0.` (18); `      DO I = 1, NELM` (20); `        ITYP = IELM(2,I)` (22); `        ND   = IELM(3,I)` (23); `        IMAT = IELM(4,I)` (24); 연속문(26–29): `        IF( ITYP == 6 )` <br> `     &    CALL  GNPFLW_S(FLI,FLO,FCP,VELG(1,1,I),VELE(1,I),GRID,UG1,UG2` <br> `     &                  ,UG3,PG1,PG3,IELM(8,I),ND,AMAT(1,IMAT),GRAV,DT1` <br> `     &                  ,DT2,RR(7),IDYN,ITO)`; `      ENDDO` (31). |
| 33–58 | NPFLOW_S 루틴 안. 내부 절점의 INDOP>0에 대해 RES=FLO-FLI를 대입한다. ICHK=0이면 반환한다. 나머지는 잔차 제곱합과 INDOP=-1 경계의 유입·유출을 부호별로 누적한다. 원문: `      DO I = 1, NNODI` (33); `        IFR = INDOP(I)` (34); `        IF( IFR > 0 ) RES(IFR) = FLO(I) - FLI(I)` (35); `      ENDDO` (36); `      IF( ICHK == 0 ) RETURN` (38); `      RNRM = 0.` (40); `      DFI = 0.` (42); `      DFO = 0.` (43); `      DO I = 1, NNODI` (45); `        IFR = INDOP(I)` (46); `        IF( IFR > 0 ) THEN` (47); `          RNRM = RNRM + RES(IFR) * RES(IFR)` (48); `        ELSEIF( IFR == -1 ) THEN` (49); `          DF = FLI(I) - FLO(I)` (50); `          IF( DF >= 0 ) THEN` (51); `            DFI = DFI + DF` (52); `          ELSE` (53); `            DFO = DFO - DF` (54); `          ENDIF` (55); `        ENDIF` (56); `      ENDDO` (57). 47·49행의 IF/ELSEIF 사슬에는 ELSE가 없다. [11-04 전수 검증 보완] |
| 59–79 | NPFLOW_S 루틴 안. 순위 0은 잔차 제곱근과 유량 수지를 출력한다. 나머지 순위는 RNRM·DFI·DFO 축약(reduction) 호출을 수행한다. 순위 1은 작업 번호 4를 순위 0에 보낸다. 원문: `      IF( MYRANK == 0 ) THEN` (59); `        RNRM = DSQRT( RNRM )` (61); 연속문(63–65): `        WRITE(ITO,'(/A//A)') ` <br> `     &    '   * FLOW BALANCE',` <br> `     &    '        RNRM       INFLOW      OUTFLOW    IN - OUT'`; `        WRITE(ITO,'(3X,1P4E12.4)') RNRM,DFI,DFO,DFI-DFO` (67); `      ELSE` (69); `        IF( MYRANK == 1 ) CALL M_MPI_SEND_I(4,1,0)  ! SEND IOP=4 TO GLB_COMM` (71); `        CALL M_MPI_REDUCE_D(RNRM,DUM,1,0)` (73); `        CALL M_MPI_REDUCE_D(DFI,DUM,1,0)` (74); `        CALL M_MPI_REDUCE_D(DFO,DUM,1,0)` (75); `      ENDIF` (77); `      END` (79). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 10: DATA GRAV의 세 번째 성분은 -9.8D0이다. 이 선언에는 단위나 좌표축 방향 설명이 없다. [11-04 전수 검증 정정]
