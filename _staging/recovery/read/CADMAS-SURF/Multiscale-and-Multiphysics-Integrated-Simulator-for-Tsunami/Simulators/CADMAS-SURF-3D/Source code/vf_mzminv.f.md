---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Source code/vf_mzminv.f
lines: 50
sha256: 41b472f740f78b58df88ac169d5c169f022989fdc4cd136f793d2264f19d44a6
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# vf_mzminv.f — 판독 구간 기록

구간은 1행부터 50행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–36 | 전처리 행렬(preconditioning matrix)을 푸는 루틴의 형식과 역대각·하삼각·상삼각·벡터 배열 범위를 선언한다. 원문: 연속문: `      SUBROUTINE VF_MZMINV(DD,ALI,ALJ,ALK,AUI,AUJ,AUK,X,Y,` (1); `     &                     INDC,MI,MJ,MK,NI,NJ,NK)` (2). `CD=== 概要 ===========================================================` (4) (개요). `CDT   VF_MZMINV:前処理行列Mに関するM*X=(L*DINV+I)(D+U)*X=Yを解く` (6) (전처리 행렬 M에 대해 M*X=(L*DINV+I)(D+U)*X=Y를 푼다). `C==== 宣言 ===========================================================` (8) (선언). `C     -- 大域型 --` (10) (전역 형식). `      IMPLICIT INTEGER(I-N),DOUBLE PRECISION(A-H,O-Z)` (11). `CD    -- 引数 --` (13) (인수). `CD    DD(MI,MJ,MK)   : IN  : R*8 : 前処理用対角行列(逆数)` (14) (전처리용 대각 행렬의 역수). `CD    ALI(MI,MJ,MK)  : IN  : R*8 : 非対称行列AのI-1に関する成分` (15) (비대칭 행렬 A의 I-1 성분). `CD    ALJ(MI,MJ,MK)  : IN  : R*8 : 非対称行列AのJ-1に関する成分` (16) (비대칭 행렬 A의 J-1 성분). `CD    ALK(MI,MJ,MK)  : IN  : R*8 : 非対称行列AのK-1に関する成分` (17) (비대칭 행렬 A의 K-1 성분). `CD    AUI(MI,MJ,MK)  : IN  : R*8 : 非対称行列AのI+1に関する成分` (18) (비대칭 행렬 A의 I+1 성분). `CD    AUJ(MI,MJ,MK)  : IN  : R*8 : 非対称行列AのJ+1に関する成分` (19) (비대칭 행렬 A의 J+1 성분). `CD    AUK(MI,MJ,MK)  : IN  : R*8 : 非対称行列AのK+1に関する成分` (20) (비대칭 행렬 A의 K+1 성분). `CD    X(MI,MJ,MK)    : OUT : R*8 : ベクトルX(解)` (21) (해 벡터 X). `CD    Y(MI,MJ,MK)    : IN  : R*8 : ベクトルY(右辺)` (22) (우변 벡터 Y). `CD    INDC(MI,MJ,MK) : IN  : I*4 : インデックス` (23) (인덱스(index)). `CD    MI             : IN  : I*4 : x方向最大格子数+1` (24) (x방향 최대 격자 수+1). `CD    MJ             : IN  : I*4 : y方向最大格子数+1` (25) (y방향 최대 격자 수+1). `CD    MK             : IN  : I*4 : z方向最大格子数+1` (26) (z방향 최대 격자 수+1). `CD    NI             : IN  : I*4 : x方向格子数+1` (27) (x방향 격자 수+1). `CD    NJ             : IN  : I*4 : y方向格子数+1` (28) (y방향 격자 수+1). `CD    NK             : IN  : I*4 : z方向格子数+1` (29) (z방향 격자 수+1). `      DIMENSION DD  (MI,MJ,MK),ALI (MI,MJ,MK),ALJ (MI,MJ,MK)` (30). `      DIMENSION ALK (MI,MJ,MK),AUI (MI,MJ,MK),AUJ (MI,MJ,MK)` (31). `      DIMENSION AUK (MI,MJ,MK),X   (MI,MJ,MK),Y   (MI,MJ,MK)` (32). `      DIMENSION INDC(MI,MJ,MK)` (33). `C==== 実行 ===========================================================` (35) (실행). |
| 37–50 | 시작 시 1행 루틴 `SUBROUTINE VF_MZMINV` 안. VF_MZFRWD로 전진 대입(forward substitution)을 수행한다. VF_MZBKWD의 두 벡터 인수에 X를 함께 전달하여 후진 대입(back substitution)을 수행하고 반환한다. 원문: `CD    -- (L*DINV+I)*X=Yを解く --` (37) ((L*DINV+I)*X=Y를 푼다). `      CALL VF_MZFRWD(DD,ALI,ALJ,ALK,X,Y,INDC,MI,MJ,MK,NI,NJ,NK)` (38). `CD    -- (D+U)*X=Xを解く --` (40) ((D+U)*X=X를 푼다). `      CALL VF_MZBKWD(DD,AUI,AUJ,AUK,X,X,INDC,MI,MJ,MK,NI,NJ,NK)` (41). `C     -- 実行文の終了 --` (43) (실행문 종료). `      GOTO 9999` (44). `C==== 終了 ===========================================================` (46) (종료). ` 9999 CONTINUE` (48). `      RETURN` (49). `      END` (50). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 38–41: 후진 대입 호출은 X를 출력과 우변 인수에 중복 전달한다. 이 파일은 별도의 중간 벡터를 선언하지 않는다.
