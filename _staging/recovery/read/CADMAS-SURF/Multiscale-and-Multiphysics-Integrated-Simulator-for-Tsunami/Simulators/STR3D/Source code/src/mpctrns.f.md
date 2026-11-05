---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/src/mpctrns.f
lines: 69
sha256: a4aaeaa8b648618b5bec5da6e553b30835f9b4a8e566c917419ab712ccd25d29
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# mpctrns.f — 판독 구간 기록

구간은 1행부터 69행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–22 | MPCTRNS의 배열 선언과 절점·자유도 목록 생성이다. IMPC==0이면 900으로 이동한다. 그 외에는 RAMBDA를 CLEAR1로 초기화하고 NC개 대각 성분을 1로 한다. 원문: 연속문(1–2): `      SUBROUTINE MPCTRNS(IMPC,KN,ND,NDF,NC,RAMBDA,NRAMAX,INDOF,INDMPC` (1)； `     &                  ,MPCF,RMPC,WK,ESTF,IDCR,NCR)` (2)； `      IMPLICIT REAL*8(A-H,O-Z)` (4)； 연속문(5–6): `      DIMENSION KN(ND),IDCR(2,*),RAMBDA(NC,*),INDOF(6,*),INDMPC(2,6,*)` (5)； `     &         ,MPCF(2,*),RMPC(*),WK(NC,*),ESTF(*)` (6)； `      NCR=0` (8)； `      DO 100 I=1,ND` (9)； `      DO 100 J=1,NDF` (10)； `        NCR=NCR+1` (11)； `        IDCR(1,NCR)=KN(I)` (12)； `        IDCR(2,NCR)=J` (13)； `  100 CONTINUE` (14)； `      IF(IMPC .EQ. 0) GOTO 900` (16)； `      CALL CLEAR1(RAMBDA,NRAMAX)` (18)； `      DO 200 I=1,NC` (19)； `        RAMBDA(I,I)=1.D0` (20)； `  200 CONTINUE` (21)。 |
| 23–51 | 시작 시 1행 MPCTRNS 루틴 안이다. 16행 `IF(IMPC .EQ. 0) GOTO 900`에서 이동하지 않았으므로 IMPC가 0이 아니다. 레이블 900은 68행 RETURN이다. INDOF(J,KN(I)) == -2인 항목에서 `IROW=NDF*(I-1)+J`를 계산한다. IS와 IE는 INDMPC(1,J,KN(I))와 INDMPC(2,J,KN(I))이다. MPCF의 절점·자유도 조합이 IDCR에 있으면 해당 RAMBDA에 RMPC를 저장한다. 없으면 IDCR에 추가하여 저장한다. INDOF(J,KN(I))가 -2인 항목을 하나도 만나지 않아 IRAMFLG가 0이면 68행 레이블 900으로 이동한다. 원문: `      IRAMFLG=0` (23)； `      DO 300 I=1,ND` (24)； `        DO 310 J=1,NDF` (25)； `          IF(INDOF(J,KN(I)) .NE. -2) GOTO 310` (26)； `          IRAMFLG=1` (27)； `          IROW=NDF*(I-1)+J` (28)； `          IS=INDMPC(1,J,KN(I))` (29)； `          IE=INDMPC(2,J,KN(I))` (30)； `          DO 320 IAD=IS,IE` (32)； `            NODE=MPCF(1,IAD)` (33)； `            IFR =MPCF(2,IAD)` (34)； `            DO 330 K=1,NCR` (35)； `              IF(NODE .EQ. IDCR(1,K) .AND. IFR .EQ. IDCR(2,K)) THEN` (36)； `                RAMBDA(IROW,K)=RMPC(IAD)` (37)； `                GOTO 320` (38)； `              ENDIF` (39)； `  330       CONTINUE` (40)； `            NCR=NCR+1` (41)； `            IDCR(1,NCR)=NODE` (42)； `            IDCR(2,NCR)=IFR` (43)； `            RAMBDA(IROW,NCR)=RMPC(IAD)` (44)； `  320     CONTINUE` (45)； `  310   CONTINUE` (47)； `  300 CONTINUE` (48)； `      IF(IRAMFLG .EQ. 0) GOTO 900` (50)。 [11-04 전수 검증 보완] [11-04 전수 검증 정정] |
| 52–69 | 시작 시 1행 MPCTRNS 루틴 안이다. 16행 `IF(IMPC .EQ. 0) GOTO 900`과 50행 `IF(IRAMFLG .EQ. 0) GOTO 900`에서 이동하지 않은 경로이다. INDOF(J,KN(I)) == -2이면 SHIFT0에 IDCR의 IP열·IP+1열과 2*(NCR-IP)를 전달한다. SHIFT1에는 RAMBDA의 IP열·IP+1열과 NC*(NCR-IP)를 전달한다. NCR을 1 감소시킨다. 해석: 이 두 호출은 원래 항목에 대응하는 열을 제거한다. HARFB·HARFTA를 호출하여 ESTF를 변환하고 900에서 반환한다. 원문: `      IP=1` (52)； `      DO 400 I=1,ND` (53)； `        DO 410 J=1,NDF` (54)； `          IF(INDOF(J,KN(I)) .EQ. -2) THEN` (55)； `            CALL SHIFT0(IDCR(1,IP),IDCR(1,IP+1),2*(NCR-IP))` (56)； `            CALL SHIFT1(RAMBDA(1,IP),RAMBDA(1,IP+1),NC*(NCR-IP))` (57)； `            NCR=NCR-1` (58)； `          ELSE` (59)； `            IP=IP+1` (60)； `          ENDIF` (61)； `  410   CONTINUE` (62)； `  400 CONTINUE` (63)； `      CALL HARFB(WK,ESTF,RAMBDA,NC,NC,NCR)` (65)； `      CALL HARFTA(ESTF,RAMBDA,WK,NC,NCR)` (66)； `  900 RETURN` (68)； `      END` (69)。 [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 18·37·44: 동일 IROW·열을 다시 찾는 경우 RAMBDA에 RMPC를 대입한다. 해당 대입식에는 기존 값과의 덧셈이 없다.
- 5–6·41–44: IDCR·RAMBDA의 마지막 차원은 가정 크기이다. NCR 증가 전에 저장 용량을 확인하는 조건은 이 파일에 없다.
