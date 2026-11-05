---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/geo/mpctrnsg.f
lines: 71
sha256: 5a3f6087efba965d425d0b7023d2dfdcf619688de4794c638a1f5a7b23f576bc
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# mpctrnsg.f — 판독 구간 기록

구간은 1행부터 71행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–22 | MPCTRNSG는 다점 구속(multipoint constraint) 변환을 수행한다. 실수 IMPLICIT 및 배열 선언은 아래와 같다. ND개 절점의 NDF개 자유도(degree of freedom)를 IDCR에 나열하며 NCR을 센다. IMPC=0이면 70행 레이블 900의 `RETURN`으로 이동한다. 나머지는 CLEAR1로 RAMBDA를 비우고 I=1,NC의 대각 값을 1.D0으로 설정한다. 원문: `      SUBROUTINE MPCTRNSG(IMPC,KN,ND,NDF,NC,RAMBDA,NRAMAX,INDOF,INDMPC` (1); `     &                   ,MPCF,RMPC,ELHM12,ELHM21,IDCR,NCR)` (2); `C` (3); `      IMPLICIT REAL*8(A-H,O-Z)` (4); `      DIMENSION KN(ND),IDCR(2,*),RAMBDA(NC,*),INDOF(6,*),INDMPC(2,6,*)` (5); `     &         ,MPCF(2,*),RMPC(*),WK(NC*ND),ELHM12(*),ELHM21(*)` (6); `C-----------------------------------------------------------------------` (7); `      NCR=0` (8); `      DO 100 I=1,ND` (9); `      DO 100 J=1,NDF` (10); `        NCR=NCR+1` (11); `        IDCR(1,NCR)=KN(I)` (12); `        IDCR(2,NCR)=J` (13); `  100 CONTINUE` (14); `C` (15); `      IF(IMPC .EQ. 0) GOTO 900` (16); `C` (17); `      CALL CLEAR1(RAMBDA,NRAMAX)` (18); `      DO 200 I=1,NC` (19); `        RAMBDA(I,I)=1.D0` (20); `  200 CONTINUE` (21); `C` (22) [11-04 전수 검증 보완] |
| 23–49 | ND·NDF 루프에서 INDOF=-2인 자유도만 구속행으로 처리한다. `IROW=NDF*(I-1)+J`로 행 번호를 계산한다. `IS=INDMPC(1,J,KN(I))`와 `IE=INDMPC(2,J,KN(I))`로 범위를 읽는다. 26행 `GOTO 310`의 대상은 47행 `310 CONTINUE`이다. 38행 `GOTO 320`의 대상은 45행 `320 CONTINUE`이다. IAD=IS,IE의 NODE·IFR를 IDCR(1:2,1:NCR)에서 찾는다. 일치하면 RMPC를 RAMBDA에 설정한다. 없으면 NCR을 늘리고 새 자유도를 IDCR에 추가한 뒤 계수를 설정한다. 원문: `      IRAMFLG=0` (23); `      DO 300 I=1,ND` (24); `        DO 310 J=1,NDF` (25); `          IF(INDOF(J,KN(I)) .NE. -2) GOTO 310` (26); `          IRAMFLG=1` (27); `          IROW=NDF*(I-1)+J` (28); `          IS=INDMPC(1,J,KN(I))` (29); `          IE=INDMPC(2,J,KN(I))` (30); `C` (31); `          DO 320 IAD=IS,IE` (32); `            NODE=MPCF(1,IAD)` (33); `            IFR =MPCF(2,IAD)` (34); `            DO 330 K=1,NCR` (35); `              IF(NODE .EQ. IDCR(1,K) .AND. IFR .EQ. IDCR(2,K)) THEN` (36); `                RAMBDA(IROW,K)=RMPC(IAD)` (37); `                GOTO 320` (38); `              ENDIF` (39); `  330       CONTINUE` (40); `            NCR=NCR+1` (41); `            IDCR(1,NCR)=NODE` (42); `            IDCR(2,NCR)=IFR` (43); `            RAMBDA(IROW,NCR)=RMPC(IAD)` (44); `  320     CONTINUE` (45); `C` (46); `  310   CONTINUE` (47); `  300 CONTINUE` (48); `C     ` (49) [11-04 전수 검증 보완] |
| 50–71 | 구속행이 없으면 레이블 900으로 이동한다. 구속행이 있으면 ND·NDF 루프에서 INDOF=-2인 열을 SHIFT0·SHIFT1로 제거하고 NCR을 줄인다. ELSE는 IP를 증가시킨다. ELHM12를 WK에 복사한 뒤 ATXB로 RAMBDA 전치 곱을 적용한다. ELHM21은 WK 복사 뒤 AXB로 RAMBDA를 오른쪽에서 곱한다. RETURN으로 끝낸다. 원문: `      IF(IRAMFLG .EQ. 0) GOTO 900` (50); `C` (51); `      IP=1` (52); `      DO 400 I=1,ND` (53); `        DO 410 J=1,NDF` (54); `          IF(INDOF(J,KN(I)) .EQ. -2) THEN` (55); `            CALL SHIFT0(IDCR(1,IP),IDCR(1,IP+1),2*(NCR-IP))` (56); `            CALL SHIFT1(RAMBDA(1,IP),RAMBDA(1,IP+1),NC*(NCR-IP))` (57); `            NCR=NCR-1` (58); `          ELSE` (59); `            IP=IP+1` (60); `          ENDIF` (61); `  410   CONTINUE` (62); `  400 CONTINUE` (63); `C` (64); `      WK(:) = ELHM12(1:NC*ND)` (65); `      CALL ATXB(ELHM12,RAMBDA,WK,NC,NCR,ND)` (66); `      WK(:) = ELHM21(1:ND*NC)` (67); `      CALL AXB(ELHM21,WK,RAMBDA,ND,NC,NCR)` (68); `C` (69); `  900 RETURN` (70); `      END` (71) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 41–44: 신규 자유도마다 NCR을 증가시키지만 이 루틴에는 NCR 증가에 대한 명시적 용량 검사문이 없다.
- 65–68: 두 변환은 같은 WK(NC*ND) 작업 배열을 순서대로 재사용한다.
