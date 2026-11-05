---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/src/loadqu2.f
lines: 78
sha256: e88bf9304afe6a7381b117337a96f06d62fe2d6ee759e96505f05d85421473ad
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# loadqu2.f — 판독 구간 기록

구간은 1행부터 78행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–29 | LOADQU2의 배열과 DATA 적분표 선언이다. SHIFT1으로 XYZ를 채운다. VECML1에 RNORM·DIR·DIR·3을 전달한다. RNORM이 0이 아니면 DIRCOS를 호출한다. 해석: XYZ는 절점 좌표이고 RNORM은 DIR의 제곱 노름(norm)이다. 해석: DIRCOS로 방향을 구한다. FC를 초기화하고 NJ==4이면 방향별 적분점 수 NG=2, ELSE이면 NG=3으로 한다. 원문: `      SUBROUTINE LOADQU2(GRID,NJ,NOD,PRESS,DIR,ID,ICRD,TR,FC,ITO)` (1)； `      IMPLICIT REAL*8(A-H,O-Z)` (3)； 연속문(4–6): `      DIMENSION WGT(3,3),XG(3,3),XYZ(3,9),GRID(3,*),NOD(NJ),FC(3,NJ)` (4)； `     &         ,R1(3),R2(3),P(2,9),H(9),DIR(3),E(3),XYZG(3),TRG(3,3)` (5)； `     &         ,TR(12,*),E0(3),ICRD(*),PRESS(NJ)` (6)； 연속문(7–9): `      DATA  XG   / 3*0.0D0` (7)； `     &           , -.577350269189626D0, .577350269189626D0, 0.0D0` (8)； `     &           , -.774596669241483D0, 0.0D0, .774596669241483D0 /` (9)； 연속문(10–13): `      DATA  WGT  / 2.0D0, 2*0.0D0` (10)； `     &           , 2*1.0D0, 0.0D0` (11)； `     &           , 0.55555555555555556D0, 0.88888888888888889D0` (12)； `     &           , 0.55555555555555556D0 /` (13)； `      DO 100 I=1,NJ` (15)； `        CALL SHIFT1(XYZ(1,I),GRID(1,NOD(I)),3)` (16)； `  100 CONTINUE` (17)； `      CALL VECML1(RNORM,DIR,DIR,3)` (19)； `      IF(RNORM.NE.0.) CALL DIRCOS(E,DIR,3)` (20)； `      CALL CLEAR1(FC,3*NJ)` (22)； `      IF(NJ.EQ.4) THEN` (24)； `        NG=2` (25)； `      ELSE` (26)； `        NG=3` (27)； `      ENDIF` (28)。 [11-04 전수 검증 정정] |
| 30–53 | 시작 시 1행 LOADQU2 루틴 안이다. 두 루프에서 DERQU2를 호출한다. P와 XYZ의 곱을 R1·R2에 누적한다. VECML1 호출 뒤 FAC를 계산한다. SFNQU2와 VECML1을 호출한다. 해석: R1·R2는 접선 벡터(tangent vector)이다. 해석: FAC는 면적 계수와 적분 가중치의 곱이고 PRESG는 적분점 압력이다. 원문: `      DO 200 IG1=1,NG` (30)； `      DO 200 IG2=1,NG` (31)； `        XG1=XG(IG1,NG)` (32)； `        XG2=XG(IG2,NG)` (33)； `        CALL DERQU2(P,XG1,XG2,NOD,NJ)` (35)； `        CALL CLEAR1(R1,3)` (36)； `        CALL CLEAR1(R2,3)` (37)； `        DO 300 I=1,NJ` (38)； `          DO 400 J=1,3` (39)； `            R1(J)=R1(J)+P(1,I)*XYZ(J,I)` (40)； `            R2(J)=R2(J)+P(2,I)*XYZ(J,I)` (41)； `  400     CONTINUE` (42)； `  300   CONTINUE` (43)； `        CALL VECML1(EE,R1,R1,3)` (45)； `        CALL VECML1(FF,R1,R2,3)` (46)； `        CALL VECML1(GG,R2,R2,3)` (47)； `        FAC=DSQRT(EE*GG-FF*FF)*WGT(IG1,NG)*WGT(IG2,NG)` (48)； `        CALL SFNQU2(H,XG1,XG2,NOD,NJ)` (50)； `        CALL VECML1(PRESG,H,PRESS,NJ)` (52)。 [11-04 전수 검증 정정] |
| 54–78 | 시작 시 1행 LOADQU2 루틴과 30행 `DO 200 IG1=1,NG` 및 31행 `DO 200 IG2=1,NG` 안이다. 두 루프의 공통 종료는 75행 `200 CONTINUE`이다. RNORM이 0이면 CROSS2를 호출한다. RNORM이 0이 아니고 ID > 0이면 CLEAR1·RMULT2·TRNSMTX6·AXB를 호출한다. RNORM이 0이 아니고 ID가 양수가 아니면 SHIFT1을 호출한다. FC에 `H(I)*PRESG*E0(J)*FAC`를 누적한다. 해석: XYZG는 적분점 좌표이다. 해석: ID > 0 경로는 지정 방향을 변환한다. 해석: FC 누적항은 형상함수·압력·방향·FAC의 곱이다. 원문: `        IF(RNORM.EQ.0.) THEN` (54)； `          CALL CROSS2(R1,R2,E0)` (55)； `        ELSE` (56)； `          IF( ID .GT. 0 ) THEN` (57)； `            CALL CLEAR1(XYZG,3)` (58)； `            DO 700 I=1,NJ` (59)； `              CALL RMULT2(XYZG,XYZ(1,I),H(I),3)` (60)； `  700       CONTINUE` (61)； `            CALL TRNSMTX6(TRG,ICRD(ID),XYZG,TR(1,ID),ITO)` (62)； `            CALL AXB(E0,TRG,E,3,3,1)` (63)； `          ELSE` (64)； `            CALL SHIFT1(E0,E,3)` (65)； `          ENDIF` (66)； `        ENDIF` (67)； `        DO 500 I=1,NJ` (69)； `          DO 600 J=1,3` (70)； `            FC(J,I)=FC(J,I)+H(I)*PRESG*E0(J)*FAC` (71)； `  600     CONTINUE` (72)； `  500   CONTINUE` (73)； `  200 CONTINUE` (75)； `      RETURN` (77)； `      END` (78)。 [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 24–28: NJ가 4가 아닌 경우에는 모두 NG=3을 선택한다.
- 48: 제곱근의 인수 EE*GG-FF*FF에 대한 하한 보정이나 검사 조건은 이 파일에 없다.
