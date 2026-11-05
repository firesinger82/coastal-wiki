---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Source code/vf_mzax.f
lines: 65
sha256: b1b9530a207ec3617a5e2d2db4558c9504597f3b23d137a740f2916df62ffc9f
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# vf_mzax.f — 판독 구간 기록

구간은 1행부터 65행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–38 | 행렬곱(matrix-vector product) 루틴의 형식·포함 파일과 행렬 7성분 및 벡터 배열 범위를 선언한다. 원문: 연속문: `      SUBROUTINE VF_MZAX(AD,ALI,ALJ,ALK,AUI,AUJ,AUK,X,Y,` (1); `     &                   INDC,MI,MJ,MK,NI,NJ,NK)` (2). `CD=== 概要 ===========================================================` (4) (개요). `CDT   VF_MZIP:非対象行列Aとベクトルxの積yを計算する(A*x=y)` (6) (비대칭 행렬 A와 벡터 x의 곱 y를 계산한다(A*x=y); 원문은 非対象로 표기한다). `C==== 宣言 ===========================================================` (8) (선언). `C     -- 大域型 --` (10) (전역 형식). `      IMPLICIT INTEGER(I-N),DOUBLE PRECISION(A-H,O-Z)` (11). `C     -- 大域変数 --` (13) (전역 변수). `      INCLUDE 'VF_A0PRM.h'` (14). `      INCLUDE 'VF_APARAI.h'` (15). `CD    -- 引数 --` (17) (인수). `CD    AD(MI,MJ,MK)   : IN  : R*8 : 非対称行列Aの対角成分` (18) (비대칭 행렬 A의 대각 성분). `CD    ALI(MI,MJ,MK)  : IN  : R*8 : 非対称行列AのI-1に関する成分` (19) (비대칭 행렬 A의 I-1 성분). `CD    ALJ(MI,MJ,MK)  : IN  : R*8 : 非対称行列AのJ-1に関する成分` (20) (비대칭 행렬 A의 J-1 성분). `CD    ALK(MI,MJ,MK)  : IN  : R*8 : 非対称行列AのK-1に関する成分` (21) (비대칭 행렬 A의 K-1 성분). `CD    AUI(MI,MJ,MK)  : IN  : R*8 : 非対称行列AのI+1に関する成分` (22) (비대칭 행렬 A의 I+1 성분). `CD    AUJ(MI,MJ,MK)  : IN  : R*8 : 非対称行列AのJ+1に関する成分` (23) (비대칭 행렬 A의 J+1 성분). `CD    AUK(MI,MJ,MK)  : IN  : R*8 : 非対称行列AのK+1に関する成分` (24) (비대칭 행렬 A의 K+1 성분). `CD    X(MI,MJ,MK)    : IN  : R*8 : ベクトルX` (25) (벡터(vector) X). `CD    Y(MI,MJ,MK)    : OUT : R*8 : ベクトルY` (26) (벡터(vector) Y). `CD    INDC(MI,MJ,MK) : IN  : I*4 : インデックス` (27) (인덱스(index)). `CD    MI             : IN  : I*4 : x方向最大格子数+1` (28) (x방향 최대 격자 수+1). `CD    MJ             : IN  : I*4 : y方向最大格子数+1` (29) (y방향 최대 격자 수+1). `CD    MK             : IN  : I*4 : z方向最大格子数+1` (30) (z방향 최대 격자 수+1). `CD    NI             : IN  : I*4 : x方向格子数+1` (31) (x방향 격자 수+1). `CD    NJ             : IN  : I*4 : y方向格子数+1` (32) (y방향 격자 수+1). `CD    NK             : IN  : I*4 : z方向格子数+1` (33) (z방향 격자 수+1). `      DIMENSION AD  (MI,MJ,MK),ALI (MI,MJ,MK),ALJ (MI,MJ,MK)` (34). `      DIMENSION ALK (MI,MJ,MK),AUI (MI,MJ,MK),AUJ (MI,MJ,MK)` (35). `      DIMENSION AUK (MI,MJ,MK),X   (MI,MJ,MK),Y   (MI,MJ,MK)` (36). `      DIMENSION INDC(MI,MJ,MK)` (37). |
| 39–65 | 시작 시 1행 루틴 `SUBROUTINE VF_MZAX` 안. K 내부 범위와 소유 I,J 범위에서 INDC가 -1이 아닌 셀의 중심 및 여섯 이웃 성분을 합산하여 Y를 구하고 반환한다. 원문: `C==== 実行 ===========================================================` (39) (실행). `CD    -- A*xを計算 --` (41) (A*x 계산). `      DO 120 K=2,NK-1` (42). `        DO 110 J=MYJS,MYJE` (43). `          DO 100 I=MYIS,MYIE` (44). `            IF (INDC(I,J,K).NE.-1) THEN` (45). 연속문: `              Y(I,J,K)= AD (I,J,K)*X(I  ,J  ,K  )` (46); `     &                 +ALI(I,J,K)*X(I-1,J  ,K  )` (47); `     &                 +ALJ(I,J,K)*X(I  ,J-1,K  )` (48); `     &                 +ALK(I,J,K)*X(I  ,J  ,K-1)` (49); `     &                 +AUI(I,J,K)*X(I+1,J  ,K  )` (50); `     &                 +AUJ(I,J,K)*X(I  ,J+1,K  )` (51); `     &                 +AUK(I,J,K)*X(I  ,J  ,K+1)` (52). `            ENDIF` (53). `  100     CONTINUE` (54). `  110   CONTINUE` (55). `  120 CONTINUE` (56). `C     -- 実行文の終了 --` (58) (실행문 종료). `      GOTO 9999` (59). `C==== 終了 ===========================================================` (61) (종료). ` 9999 CONTINUE` (63). `      RETURN` (64). `      END` (65). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 1·6: 실제 서브루틴명은 VF_MZAX이다. 개요 주석에는 VF_MZIP와 非対象行列이라는 표기가 있다.
- 45–53: INDC=-1인 셀의 Y에는 이 루프에서 값을 대입하지 않는다.
