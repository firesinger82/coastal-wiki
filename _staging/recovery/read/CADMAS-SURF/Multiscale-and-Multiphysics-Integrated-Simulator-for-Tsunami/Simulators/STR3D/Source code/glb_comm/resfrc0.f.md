---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/glb_comm/resfrc0.f
lines: 51
sha256: d9152e1fd5e22eea2e98efee17159d0ec0f89604f73010bc38b8bf89c3cf3fc6
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# resfrc0.f — 판독 구간 기록

구간은 1행부터 51행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–24 | 암시적 배정밀도와 3성분 노름(norm) 배열을 선언한다(3–4). 단계·시간·반복 수를 프로세스 1에서 받는다(6–9). 0으로 초기화한 DUM을 M_MPI_REDUCE_D에 전달하여 FNRM·RNRM을 받고 각 성분의 제곱근을 계산한다(11–23). 원문: `      SUBROUTINE RESFRC0(RR,ITO)` (1); `      IMPLICIT REAL*8(A-H,O-Z)` (3); `      DIMENSION RR(*),FNRM(3),RNRM(3),DUM(3)` (4); `      CALL M_MPI_RECV_I(ISTEP,1,1)` (6); `      CALL M_MPI_RECV_D(TIM,1,1)` (7); `      CALL M_MPI_RECV_I(ITER2,1,1)` (8); `      CALL M_MPI_RECV_I(ITER,1,1)` (9); `      DUM(:) = 0.` (11); `      CALL M_MPI_REDUCE_D(DUM,FNRM,3,0)` (12); `      FNRM(1) = DSQRT( FNRM(1) )` (14); `      FNRM(2) = DSQRT( FNRM(2) )` (15); `      FNRM(3) = DSQRT( FNRM(3) )` (16); `      DUM(:) = 0.` (18); `      CALL M_MPI_REDUCE_D(DUM,RNRM,3,0)` (19); `      RNRM(1) = DSQRT( RNRM(1) )` (21); `      RNRM(2) = DSQRT( RNRM(2) )` (22); `      RNRM(3) = DSQRT( RNRM(3) )` (23). |
| 25–33 | 시작 시 1행 resfrc0 루틴 안. ICONV=0으로 시작한다(25). ITER 양수이면 RRES=RNRM(1)/FNRM(1)을 계산하고 상대 기준 RR(6) 또는 절대 기준 RR(3)을 만족할 때 ICONV=1로 설정한다(27–30). 결과를 방송한다(32). 원문: `      ICONV = 0` (25); `      IF( ITER > 0 ) THEN` (27); `        RRES = RNRM(1) / FNRM(1)` (28); `        IF( RRES < RR(6) .OR. RNRM(1) < RR(3) ) ICONV = 1` (29); `      ENDIF` (30); `      CALL M_MPI_BCAST_I(ICONV,1)` (32). |
| 34–51 | 시작 시 1행 resfrc0 루틴 안. ITER=0이면 잔차력(residual force) 머리말을 쓴다(34–42). 해당 분기에서 ITER2=1이면 단계·시간도 쓴다(36–37). ELSE에서는 ITER·RNRM·FNRM·RRES를 출력한다(44–49). 원문: `      IF( ITER == 0 ) THEN` (34); `        IF( ITER2 == 1 ) WRITE(ITO,'(/A,I0,A,1PE10.4,A)')` (36); `     &    ' ***** STEP NO. = ',ISTEP,'   TIME = ',TIM,' *****'` (37); `        WRITE(ITO,'(/A//A,A)') ` (39); `     &    '   * RESIDUAL FORCE',` (40); `     &    '     ITER     RNRM1       FNRM1       RRES        RNRM2  ',` (41); `     &    '     FNRM2       RNRM3       FNRM3'` (42); `      ELSE` (44); `        WRITE(ITO,'(7X,I2,1P7E12.4)') ITER,RNRM(1),FNRM(1),RRES,RNRM(2)` (46); `     &                               ,FNRM(2),RNRM(3),FNRM(3)` (47); `      ENDIF` (49); `      END` (51). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 27–29: RRES를 계산하는 분기 조건은 ITER>0이다. FNRM(1)=0을 검사하는 분기는 해당 나눗셈 앞에 없다.
