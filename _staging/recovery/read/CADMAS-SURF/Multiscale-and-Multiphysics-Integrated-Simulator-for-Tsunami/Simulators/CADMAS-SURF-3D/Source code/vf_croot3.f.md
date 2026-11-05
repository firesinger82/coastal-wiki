---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Source code/vf_croot3.f
lines: 83
sha256: a8cd80a41605934c955de8b652d12a9260bb62bb44c74397f367d2ff901fe851
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# vf_croot3.f — 판독 구간 기록

구간은 1행부터 83행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–26 | Cardano 방법(Cardano method)으로 3차 이하 방정식의 실근을 구한다. 계수·근·근 개수 인수를 선언한다. VF_A0PRM.h를 포함한다. 원문: `      SUBROUTINE VF_CROOT3(AA,BB,CC,DD,XX1,XX2,XX3,NRT)` (1) `CD=== 概要 ===========================================================` (3) (개요) `CDT   VF_CROOT3:3次以下の方程式の根を計算する(CARDANOの方法)` (5) (3차 이하 방정식의 근 계산. Cardano 방법) `C==== 宣言 ===========================================================` (7) (선언) `C     -- 大域型 --` (9) (전역 자료형) `      IMPLICIT INTEGER(I-N),DOUBLE PRECISION(A-H,O-Z)` (10) `C     -- 大域変数 --` (12) (전역 변수) `      INCLUDE 'VF_A0PRM.h'` (13) `CD    -- 引数 --` (15) (인수) `CD    AA  : IN  : R*8 : 係数(AA*X3+BB*X2+CC*X+DD=0)` (16) (AA*X3+BB*X2+CC*X+DD=0의 계수) `CD    BB  : IN  : R*8 : 係数(AA*X3+BB*X2+CC*X+DD=0)` (17) (AA*X3+BB*X2+CC*X+DD=0의 계수) `CD    CC  : IN  : R*8 : 係数(AA*X3+BB*X2+CC*X+DD=0)` (18) (AA*X3+BB*X2+CC*X+DD=0의 계수) `CD    DD  : IN  : R*8 : 係数(AA*X3+BB*X2+CC*X+DD=0)` (19) (AA*X3+BB*X2+CC*X+DD=0의 계수) `CD    XX1 : OUT : R*8 : 根1` (20) (근 1) `CD    XX2 : OUT : R*8 : 根2` (21) (근 2) `CD    XX3 : OUT : R*8 : 根3` (22) (근 3) `CD    NRT : OUT : R*8 : 根の数` (23) (근의 수) `C==== 実行 ===========================================================` (25) (실행) |
| 27–58 | 시작 시 1행 VF_CROOT3 루틴 안이며 조건·루프 밖. AA=0이면 VF_CROOT2를 호출한다. 그 외에는 3차식을 정규화하고 Y³+3PY+Q=0으로 변형한다. D>0 분기에서 Q 부호에 따라 R1을 정하고 부호를 보존한 세제곱근으로 실근 하나를 구한다. 원문: `CD    -- 2次以下の方程式ならば --` (27) (2차 이하 방정식이면) `      IF (AA.EQ.0.0D0) THEN` (28) `        CALL VF_CROOT2(BB,CC,DD,XX1,XX2,NRT)` (29) `        XX3=0.0D0` (30) `CD    -- 3次方程式ならば --` (32) (3차 방정식이면) `      ELSE` (33) `C       * X3+AX2+BX+C=0に変形` (34) (X3+AX2+BX+C=0으로 변형) `        C=1.0D0/AA` (35) `        A=BB*C` (36) `        B=CC*C` (37) `        C=DD*C` (38) `C       * Y3+3PY+Q=0に変形` (39) (Y3+3PY+Q=0으로 변형) `        P=B/3.0D0-A*A/9.0D0` (40) `        Q=C-A*B/3.0D0+2.0D0*A*A*A/27.0D0` (41) `        D=Q*Q+4.0D0*P*P*P` (42) `C       * 実根` (43) (실근) `        IF (D.GT.0.0D0) THEN` (44) `          IF (Q.LE.0.0D0) THEN` (45) `            R1=0.5D0*(-Q+SQRT(D))` (46) `          ELSE` (47) `            R1=0.5D0*(-Q-SQRT(D))` (48) `          ENDIF` (49) `          R2=-P*P*P/R1` (50) `          R13=(ABS(R1))**(1.0D0/3.0D0)` (51) `          IF (R1.LT.0.0D0) R13=-R13` (52) `          R23=(ABS(R2))**(1.0D0/3.0D0)` (53) `          IF (R2.LT.0.0D0) R23=-R23` (54) `          XX1=R13+R23-A/3.0D0` (55) `          XX2=0.0D0` (56) `          XX3=0.0D0` (57) `          NRT=1` (58) |
| 59–83 | 시작 시 `IF (AA.EQ.0.0D0) THEN`(28)의 `ELSE`(33) 안이다. 이 바깥 IF는 74행 `ENDIF`에서 닫힌다. 시작 시 `IF (D.GT.0.0D0) THEN`(44) 안이다. 이 IF는 60행 `ELSE`를 거쳐 73행 `ENDIF`에서 닫힌다. 60행 ELSE는 D>0 불성립 분기다. Q에 따라 각도 T를 구하고 세 실근을 코사인으로 계산한다. 원문: `C       * 3実根` (59) (실근 3개) `        ELSE` (60) `          IF (Q.NE.0.0D0) THEN` (61) `            T=ATAN(SQRT(-D)/(-Q))` (62) `          ELSE` (63) `            T=PI/2.0D0` (64) `          ENDIF` (65) `          IF (Q.GT.0.0D0) T=PI+T` (66) `          R=2.0D0*SQRT(-P)` (67) `          S=-A/3.0D0` (68) `          XX1= R*COS(    T /3.0D0)+S` (69) `          XX2=-R*COS((PI-T)/3.0D0)+S` (70) `          XX3=-R*COS((PI+T)/3.0D0)+S` (71) `          NRT=3` (72) `        ENDIF` (73) `      ENDIF` (74) `C     -- 実行文の終了 --` (76) (실행문 종료) `      GOTO 9999` (77) `C==== 終了 ===========================================================` (79) (종료) ` 9999 CONTINUE` (81) `      RETURN` (82) `      END` (83) [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 23·10: NRT의 인수 설명은 R*8이다. IMPLICIT INTEGER(I-N)에 의해 NRT는 정수형이다.
- 44·59–72: D=0도 세 실근 분기로 들어가 NRT=3을 대입한다. 중복된 근을 합치는 문장은 이 분기에 없다.
