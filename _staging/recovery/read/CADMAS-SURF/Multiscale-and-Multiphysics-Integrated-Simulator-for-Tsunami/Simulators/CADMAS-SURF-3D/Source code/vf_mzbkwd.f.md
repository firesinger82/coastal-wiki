---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Source code/vf_mzbkwd.f
lines: 56
sha256: 5b59bf4808400e8d5aa5cddbfe09bd96a41dc6fa2a8135f9e82ead09b7e3ab05
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# vf_mzbkwd.f — 판독 구간 기록

구간은 1행부터 56행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–33 | 후진 대입(back substitution) 루틴의 형식·포함 파일·역대각 성분과 상삼각 성분·벡터 배열 범위를 선언한다. 원문: `      SUBROUTINE VF_MZBKWD(DD,AUI,AUJ,AUK,X,Y,INDC,MI,MJ,MK,NI,NJ,NK)` (1). `CD=== 概要 ===========================================================` (3) (개요). `CDT   VF_MZBKWD:後退代入で(D+U)*x=yを解く` (5) (후진 대입(back substitution)으로 (D+U)*x=y를 푼다). `C==== 宣言 ===========================================================` (7) (선언). `C     -- 大域型 --` (9) (전역 형식). `      IMPLICIT INTEGER(I-N),DOUBLE PRECISION(A-H,O-Z)` (10). `C     -- 大域変数 --` (12) (전역 변수). `      INCLUDE 'VF_A0PRM.h'` (13). `      INCLUDE 'VF_APARAI.h'` (14). `CD    -- 引数 --` (16) (인수). `CD    DD(MI,MJ,MK)   : IN  : R*8 : 前処理用対角行列(逆数)` (17) (전처리용 대각 행렬의 역수). `CD    AUI(MI,MJ,MK)  : IN  : R*8 : 非対称行列AのI+1に関する成分` (18) (비대칭 행렬 A의 I+1 성분). `CD    AUJ(MI,MJ,MK)  : IN  : R*8 : 非対称行列AのJ+1に関する成分` (19) (비대칭 행렬 A의 J+1 성분). `CD    AUK(MI,MJ,MK)  : IN  : R*8 : 非対称行列AのK+1に関する成分` (20) (비대칭 행렬 A의 K+1 성분). `CD    X(MI,MJ,MK)    : OUT : R*8 : ベクトルX(解)` (21) (해 벡터 X). `CD    Y(MI,MJ,MK)    : IN  : R*8 : ベクトルY(右辺)` (22) (우변 벡터 Y). `CD    INDC(MI,MJ,MK) : IN  : I*4 : インデックス` (23) (인덱스(index)). `CD    MI             : IN  : I*4 : x方向最大格子数+1` (24) (x방향 최대 격자 수+1). `CD    MJ             : IN  : I*4 : y方向最大格子数+1` (25) (y방향 최대 격자 수+1). `CD    MK             : IN  : I*4 : z方向最大格子数+1` (26) (z방향 최대 격자 수+1). `CD    NI             : IN  : I*4 : x方向格子数+1` (27) (x방향 격자 수+1). `CD    NJ             : IN  : I*4 : y方向格子数+1` (28) (y방향 격자 수+1). `CD    NK             : IN  : I*4 : z方向格子数+1` (29) (z방향 격자 수+1). `      DIMENSION DD  (MI,MJ,MK),AUI (MI,MJ,MK),AUJ (MI,MJ,MK)` (30). `      DIMENSION AUK (MI,MJ,MK),X   (MI,MJ,MK),Y   (MI,MJ,MK)` (31). `      DIMENSION INDC(MI,MJ,MK)` (32). |
| 34–56 | 시작 시 1행 루틴 `SUBROUTINE VF_MZBKWD` 안. K,J,I를 각각 역순으로 순회한다. INDC=-1을 제외하고 상방 세 이웃 성분을 우변에서 뺀 뒤 DD를 곱하여 X를 계산하고 반환한다. 원문: `C==== 実行 ===========================================================` (34) (실행). `CD    -- (D+U)*x=yを解く --` (36) ((D+U)*x=y를 푼다). `      DO 120 K=NK-1,2,-1` (37). `        DO 110 J=MYJE,MYJS,-1` (38). `          DO 100 I=MYIE,MYIS,-1` (39). `            IF (INDC(I,J,K).NE.-1) THEN` (40). 연속문: `              X(I,J,K)=(Y(I,J,K)-AUI(I,J,K)*X(I+1,J  ,K  )` (41); `     &                          -AUJ(I,J,K)*X(I  ,J+1,K  )` (42); `     &                          -AUK(I,J,K)*X(I  ,J  ,K+1))*DD(I,J,K)` (43). `            ENDIF` (44). `  100     CONTINUE` (45). `  110   CONTINUE` (46). `  120 CONTINUE` (47). `C     -- 実行文の終了 --` (49) (실행문 종료). `      GOTO 9999` (50). `C==== 終了 ===========================================================` (52) (종료). ` 9999 CONTINUE` (54). `      RETURN` (55). `      END` (56). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
