---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/src/loadtr2.f
lines: 68
sha256: 177c0c92f7d4e08842e5f6fe24b0dcbafa33081597dfc75c5acdea399059532e
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# loadtr2.f — 판독 구간 기록

구간은 1행부터 68행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–22 | LOADTR2의 6절점 배열과 네 적분점 DATA 선언이다. SHIFT1으로 XYZ를 채운다. VECML1에 RNORM·DIR·DIR·3을 전달한다. RNORM이 0이 아니면 DIRCOS를 호출한다. 해석: XYZ는 절점 좌표이고 RNORM은 DIR의 제곱 노름(norm)이다. FC를 0으로 한다. 원문: `      SUBROUTINE LOADTR2(GRID,NOD,PRESS,DIR,ID,ICRD,TR,FC,ITO)` (1)； `      IMPLICIT REAL*8(A-H,O-Z)` (3)； 연속문(4–6): `      DIMENSION WGT(4),RL(3,4),XYZ(3,6),GRID(3,*),NOD(6),FC(3,6)` (4)； `     &         ,R1(3),R2(3),P(2,6),H(6),DIR(3),E(3),XYZG(3),TRG(3,3)` (5)； `     &         ,TR(12,*),E0(3),ICRD(*),PRESS(6)` (6)； `      DATA WGT / -0.28125D0, 3*0.260416666666667D0 /` (7)； 연속문(8–12): `      DATA RL  / ` (8)； `     &    0.333333333333333D0, 0.333333333333333D0, 0.333333333333333D0` (9)； `     &  , 0.6D0, 0.2D0, 0.2D0` (10)； `     &  , 0.2D0, 0.6D0, 0.2D0` (11)； `     &  , 0.2D0, 0.2D0, 0.6D0 /` (12)； `      DO 100 I=1,6` (14)； `        CALL SHIFT1(XYZ(1,I),GRID(1,NOD(I)),3)` (15)； `  100 CONTINUE` (16)； `      CALL VECML1(RNORM,DIR,DIR,3)` (18)； `      IF(RNORM.NE.0.) CALL DIRCOS(E,DIR,3)` (19)； `      CALL CLEAR1(FC,18)` (21)。 [11-04 전수 검증 정정] |
| 23–43 | 시작 시 1행 LOADTR2 루틴 안이다. IG=1..4에서 DERTR2를 호출한다. P와 XYZ의 곱을 R1·R2에 누적한다. VECML1 호출 뒤 FAC를 구한다. SFNTR2와 VECML1을 호출한다. 해석: R1·R2는 접선 벡터(tangent vector)이다. 해석: EE·FF·GG는 내적이고 PRESG는 적분점 압력이다. 원문: `      DO 200 IG=1,4` (23)； `        CALL DERTR2(RL(1,IG),P,6)` (25)； `        CALL CLEAR1(R1,3)` (26)； `        CALL CLEAR1(R2,3)` (27)； `        DO 300 I=1,6` (28)； `          DO 400 J=1,3` (29)； `            R1(J)=R1(J)+P(1,I)*XYZ(J,I)` (30)； `            R2(J)=R2(J)+P(2,I)*XYZ(J,I)` (31)； `  400     CONTINUE` (32)； `  300   CONTINUE` (33)； `        CALL VECML1(EE,R1,R1,3)` (35)； `        CALL VECML1(FF,R1,R2,3)` (36)； `        CALL VECML1(GG,R2,R2,3)` (37)； `        FAC=DSQRT(EE*GG-FF*FF)*WGT(IG)` (38)； `        CALL SFNTR2(RL(1,IG),H,6)` (40)； `        CALL VECML1(PRESG,H,PRESS,6)` (42)。 [11-04 전수 검증 정정] |
| 44–68 | 시작 시 1행 LOADTR2 루틴과 23행 `DO 200 IG=1,4` 안이다. 이 루프는 65행 `200 CONTINUE`에서 닫힌다. RNORM이 0이면 CROSS2를 호출한다. RNORM이 0이 아니고 ID > 0이면 CLEAR1·RMULT2·TRNSMTX6·AXB를 호출한다. RNORM이 0이 아니고 ID가 양수가 아니면 SHIFT1을 호출한다. FC에 `H(I)*PRESG*E0(J)*FAC`를 누적한다. 해석: XYZG는 적분점 좌표이다. 해석: ID > 0 경로는 지정 방향을 변환한다. 해석: FC에는 압력 하중을 누적한다. 원문: `        IF(RNORM.EQ.0.) THEN` (44)； `          CALL CROSS2(R1,R2,E0)` (45)； `        ELSE` (46)； `          IF( ID .GT. 0 ) THEN` (47)； `            CALL CLEAR1(XYZG,3)` (48)； `            DO 700 I=1,6` (49)； `              CALL RMULT2(XYZG,XYZ(1,I),H(I),3)` (50)； `  700       CONTINUE` (51)； `            CALL TRNSMTX6(TRG,ICRD(ID),XYZG,TR(1,ID),ITO)` (52)； `            CALL AXB(E0,TRG,E,3,3,1)` (53)； `          ELSE` (54)； `            CALL SHIFT1(E0,E,3)` (55)； `          ENDIF` (56)； `        ENDIF` (57)； `        DO 500 I=1,6` (59)； `          DO 600 J=1,3` (60)； `            FC(J,I)=FC(J,I)+H(I)*PRESG*E0(J)*FAC` (61)； `  600     CONTINUE` (62)； `  500   CONTINUE` (63)； `  200 CONTINUE` (65)； `      RETURN` (67)； `      END` (68)。 [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 7: WGT의 네 값 중 첫 값은 -0.28125D0이다. [11-04 전수 검증 정정]
- 38: 제곱근의 인수 EE*GG-FF*FF에 대한 하한 보정이나 검사 조건은 이 파일에 없다.
