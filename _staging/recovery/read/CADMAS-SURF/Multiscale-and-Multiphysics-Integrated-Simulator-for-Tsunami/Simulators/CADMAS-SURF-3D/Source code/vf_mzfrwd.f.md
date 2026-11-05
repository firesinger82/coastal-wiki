---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Source code/vf_mzfrwd.f
lines: 57
sha256: 9276b0534a00753cb684d2041e0a4a8fbaae5efe5a924aa314c02e75ad8bb82f
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# vf_mzfrwd.f — 판독 구간 기록

구간은 1행부터 57행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–35 | 전진 대입(forward substitution) 루틴의 형식·포함 파일·역대각 및 하삼각 성분과 벡터 배열 범위를 선언한다. 원문: `      SUBROUTINE VF_MZFRWD(DD,ALI,ALJ,ALK,X,Y,INDC,MI,MJ,MK,NI,NJ,NK)` (1). `CD=== 概要 ===========================================================` (3) (개요). `CDT   VF_MZFRWD:前進代入で(L*DINV+I)*x=yを解く` (5) (전진 대입(forward substitution)으로 (L*DINV+I)*x=y를 푼다). `C==== 宣言 ===========================================================` (7) (선언). `C     -- 大域型 --` (9) (전역 형식). `      IMPLICIT INTEGER(I-N),DOUBLE PRECISION(A-H,O-Z)` (10). `C     -- 大域変数 --` (12) (전역 변수). `      INCLUDE 'VF_A0PRM.h'` (13). `      INCLUDE 'VF_APARAI.h'` (14). `CD    -- 引数 --` (16) (인수). `CD    DD(MI,MJ,MK)   : IN  : R*8 : 前処理用対角行列(逆数)` (17) (전처리용 대각 행렬의 역수). `CD    ALI(MI,MJ,MK)  : IN  : R*8 : 非対称行列AのI-1に関する成分` (18) (비대칭 행렬 A의 I-1 성분). `CD    ALJ(MI,MJ,MK)  : IN  : R*8 : 非対称行列AのJ-1に関する成分` (19) (비대칭 행렬 A의 J-1 성분). `CD    ALK(MI,MJ,MK)  : IN  : R*8 : 非対称行列AのK-1に関する成分` (20) (비대칭 행렬 A의 K-1 성분). `CD    X(MI,MJ,MK)    : OUT : R*8 : ベクトルX(解)` (21) (해 벡터 X). `CD    Y(MI,MJ,MK)    : IN  : R*8 : ベクトルY(右辺)` (22) (우변 벡터 Y). `CD    INDC(MI,MJ,MK) : IN  : I*4 : インデックス` (23) (인덱스(index)). `CD    MI             : IN  : I*4 : x方向最大格子数+1` (24) (x방향 최대 격자 수+1). `CD    MJ             : IN  : I*4 : y方向最大格子数+1` (25) (y방향 최대 격자 수+1). `CD    MK             : IN  : I*4 : z方向最大格子数+1` (26) (z방향 최대 격자 수+1). `CD    NI             : IN  : I*4 : x方向格子数+1` (27) (x방향 격자 수+1). `CD    NJ             : IN  : I*4 : y方向格子数+1` (28) (y방향 격자 수+1). `CD    NK             : IN  : I*4 : z方向格子数+1` (29) (z방향 격자 수+1). `      DIMENSION DD  (MI,MJ,MK),ALI (MI,MJ,MK),ALJ (MI,MJ,MK)` (30). `      DIMENSION ALK (MI,MJ,MK),X   (MI,MJ,MK),Y   (MI,MJ,MK)` (31). `      DIMENSION INDC(MI,MJ,MK)` (32). `C==== 実行 ===========================================================` (34) (실행). |
| 36–57 | 시작 시 1행 루틴 `SUBROUTINE VF_MZFRWD` 안. K,J,I를 정순으로 순회한다. INDC=-1을 제외하고 하방 세 이웃의 계수·DD·X 곱을 우변에서 빼서 X를 구하고 반환한다. 원문: `CD    -- (L*DINV+I)*x=yを解く --` (36) ((L*DINV+I)*x=y를 푼다). `      DO 120 K=2,NK-1` (37). `        DO 110 J=MYJS,MYJE` (38). `          DO 100 I=MYIS,MYIE` (39). `            IF (INDC(I,J,K).NE.-1) THEN` (40). 연속문: `              X(I,J,K)=Y(I,J,K)` (41); `     &                 -ALI(I,J,K)*DD(I-1,J  ,K  )*X(I-1,J  ,K  )` (42); `     &                 -ALJ(I,J,K)*DD(I  ,J-1,K  )*X(I  ,J-1,K  )` (43); `     &                 -ALK(I,J,K)*DD(I  ,J  ,K-1)*X(I  ,J  ,K-1)` (44). `            ENDIF` (45). `  100     CONTINUE` (46). `  110   CONTINUE` (47). `  120 CONTINUE` (48). `C     -- 実行文の終了 --` (50) (실행문 종료). `      GOTO 9999` (51). `C==== 終了 ===========================================================` (53) (종료). ` 9999 CONTINUE` (55). `      RETURN` (56). `      END` (57). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
