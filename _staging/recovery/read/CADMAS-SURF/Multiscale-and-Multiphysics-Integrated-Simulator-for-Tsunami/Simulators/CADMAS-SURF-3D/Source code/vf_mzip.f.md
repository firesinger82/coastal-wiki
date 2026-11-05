---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Source code/vf_mzip.f
lines: 52
sha256: 7180fccd16cf5d5774d6de0cb1296240d8c94271974c3f7f68b36020f6dd13a7
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# vf_mzip.f — 판독 구간 기록

구간은 1행부터 52행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–30 | 내적(inner product) 루틴의 형식·포함 파일과 벡터·인덱스 배열 범위를 선언한다. 원문: `      SUBROUTINE VF_MZIP(X,Y,S,INDC,MI,MJ,MK,NI,NJ,NK)` (1). `CD=== 概要 ===========================================================` (3) (개요). `CDT   VF_MZIP:ベクトルXとベクトルYの内積Sを計算する(x*y=s)` (5) (벡터 X와 Y의 내적(inner product) S를 계산한다(x*y=s)). `C==== 宣言 ===========================================================` (7) (선언). `C     -- 大域型 --` (9) (전역 형식). `      IMPLICIT INTEGER(I-N),DOUBLE PRECISION(A-H,O-Z)` (10). `C     -- 大域変数 --` (12) (전역 변수). `      INCLUDE 'VF_A0PRM.h'` (13). `      INCLUDE 'VF_APARAI.h'` (14). `CD    -- 引数 --` (16) (인수). `CD    X(MI,MJ,MK)    : IN  : R*8 : ベクトルX` (17) (벡터(vector) X). `CD    Y(MI,MJ,MK)    : IN  : R*8 : ベクトルY` (18) (벡터(vector) Y). `CD    S              : OUT : R*8 : 内積S` (19) (내적 S). `CD    INDC(MI,MJ,MK) : IN  : I*4 : インデックス` (20) (인덱스(index)). `CD    MI             : IN  : I*4 : x方向最大格子数+1` (21) (x방향 최대 격자 수+1). `CD    MJ             : IN  : I*4 : y方向最大格子数+1` (22) (y방향 최대 격자 수+1). `CD    MK             : IN  : I*4 : z方向最大格子数+1` (23) (z방향 최대 격자 수+1). `CD    NI             : IN  : I*4 : x方向格子数+1` (24) (x방향 격자 수+1). `CD    NJ             : IN  : I*4 : y方向格子数+1` (25) (y방향 격자 수+1). `CD    NK             : IN  : I*4 : z方向格子数+1` (26) (z방향 격자 수+1). `      DIMENSION X(MI,MJ,MK),Y(MI,MJ,MK),INDC(MI,MJ,MK)` (27). `C==== 実行 ===========================================================` (29) (실행). |
| 31–52 | 시작 시 1행 루틴 `SUBROUTINE VF_MZIP` 안. S를 0으로 시작한다. 내부 K 및 소유 I,J 범위의 INDC=-1 제외 셀에서 X*Y를 누적한다. VF_P1SUMD로 전체 합을 구하고 반환한다. 합산 의미의 근거는 같은 원문 디렉터리의 `vf_p1sumd.f:5,18–19,25–30`이다. 원문: `CD    -- x*yを計算 --` (31) (x*y 계산). `      S=0.0D0` (32). `      DO 120 K=2,NK-1` (33). `        DO 110 J=MYJS,MYJE` (34). `          DO 100 I=MYIS,MYIE` (35). `            IF (INDC(I,J,K).NE.-1) THEN` (36). `              S=S+X(I,J,K)*Y(I,J,K)` (37). `            ENDIF` (38). `  100     CONTINUE` (39). `  110   CONTINUE` (40). `  120 CONTINUE` (41). `      W=S` (42). `      CALL VF_P1SUMD(W,S)` (43). `C     -- 実行文の終了 --` (45) (실행문 종료). `      GOTO 9999` (46). `C==== 終了 ===========================================================` (48) (종료). ` 9999 CONTINUE` (50). `      RETURN` (51). `      END` (52). [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
