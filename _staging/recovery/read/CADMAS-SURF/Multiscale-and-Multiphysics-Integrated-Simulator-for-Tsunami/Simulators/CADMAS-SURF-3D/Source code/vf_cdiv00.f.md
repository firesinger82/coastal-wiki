---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Source code/vf_cdiv00.f
lines: 65
sha256: 63d5ce0bfd138a06115cd9a285d2fbcb96566bd0535134b36123dc84a707a07d
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# vf_cdiv00.f — 판독 구간 기록

구간은 1행부터 65행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–36 | 발산(divergence) 관련 2 노름(norm)의 목적·유속·면적 투과율·계산 셀 상태 배열을 선언한다. 원문: `      SUBROUTINE VF_CDIV00(VAL,XX,YY,ZZ,UU,VV,WW,GGX,GGY,GGZ,INDC)` (1). `CD=== 概要 ===========================================================` (3) (개요). `CDT   VF_CDIV00:(発散×面積)の2乗ノルムを計算する` (5) (VF_CDIV00:(발산(divergence)×면적)의 2 노름(norm) 계산). `C==== 宣言 ===========================================================` (7) (선언). `C     -- 大域型 --` (9) (전역 형). `      IMPLICIT INTEGER(I-N),DOUBLE PRECISION(A-H,O-Z)` (10). `C     -- 大域変数 --` (12) (전역 변수). `      INCLUDE 'VF_A0PRM.h'` (13). `      INCLUDE 'VF_ANUMBI.h'` (14). `      INCLUDE 'VF_APARAI.h'` (15). `CD    -- 引数 --` (17) (인수). `CD    VAL               : OUT : R*8 : (発散*面積)の2乗ノルム` (18) (VAL               : OUT : R*8 : (발산(divergence)*면적)의 2 노름(norm)). `CD    XX(MAXG1,NUMI)    : IN  : R*8 : x方向格子座標等` (19) (XX(MAXG1,NUMI)    : IN  : R*8 : x 방향 격자 좌표 등). `CD    YY(MAXG1,NUMJ)    : IN  : R*8 : y方向格子座標等` (20) (YY(MAXG1,NUMJ)    : IN  : R*8 : y 방향 격자 좌표 등). `CD    ZZ(MAXG1,NUMK)    : IN  : R*8 : z方向格子座標等` (21) (ZZ(MAXG1,NUMK)    : IN  : R*8 : z 방향 격자 좌표 등). `CD    UU(@FOR-3D@)      : IN  : R*8 : x方向流速` (22) (UU(@FOR-3D@)      : IN  : R*8 : x 방향 유속). `CD    VV(@FOR-3D@)      : IN  : R*8 : y方向流速` (23) (VV(@FOR-3D@)      : IN  : R*8 : y 방향 유속). `CD    WW(@FOR-3D@)      : IN  : R*8 : z方向流速` (24) (WW(@FOR-3D@)      : IN  : R*8 : z 방향 유속). `CD    GGX(@FOR-3D@)     : IN  : R*8 : x方向面積透過率` (25) (GGX(@FOR-3D@)     : IN  : R*8 : x 방향 면적 투과율(area transmissivity)). `CD    GGY(@FOR-3D@)     : IN  : R*8 : y方向面積透過率` (26) (GGY(@FOR-3D@)     : IN  : R*8 : y 방향 면적 투과율(area transmissivity)). `CD    GGZ(@FOR-3D@)     : IN  : R*8 : z方向面積透過率` (27) (GGZ(@FOR-3D@)     : IN  : R*8 : z 방향 면적 투과율(area transmissivity)). `CD    INDC(@FOR-3D@)    : IN  : I*4 : セルの計算状態を示すインデックス` (28) (INDC(@FOR-3D@)    : IN  : I*4 : 셀 계산 상태 지표). `      DIMENSION XX(MAXG1,NUMI),YY(MAXG1,NUMJ),ZZ(MAXG1,NUMK)` (29). `      DIMENSION UU  (NUMI,NUMJ,NUMK),VV  (NUMI,NUMJ,NUMK)` (30). `      DIMENSION WW  (NUMI,NUMJ,NUMK),GGX (NUMI,NUMJ,NUMK)` (31). `      DIMENSION GGY (NUMI,NUMJ,NUMK),GGZ (NUMI,NUMJ,NUMK)` (32). `      DIMENSION INDC(NUMI,NUMJ,NUMK)` (33). `C==== 実行 ===========================================================` (35) (실행). |
| 37–57 | 시작 시 `      SUBROUTINE VF_CDIV00(VAL,XX,YY,ZZ,UU,VV,WW,GGX,GGY,GGZ,INDC)` (1) 블록 안. INDC가 -1이 아닌 내부 셀에서 여섯 면 유량 차를 합산한 VD의 제곱을 누적한다. VF_P1SUMD로 합한 뒤 제곱근을 취한다. 원문: `CD    -- (発散*面積)の2乗ノルム --` (37) ((발산(divergence)*면적)의 2 노름(norm)). `      VAL=0.0D0` (38). `      DO 120 K=2,NUMK-1` (39). `        DO 110 J=MYJS,MYJE` (40). `          DO 100 I=MYIS,MYIE` (41). `            IF (INDC(I,J,K).NE.-1) THEN` (42). 연속문: `              VD= YY(2,J)*ZZ(2,K)*( GGX(I+1,J,K)*UU(I+1,J,K)` (43); `     &                             -GGX(I  ,J,K)*UU(I  ,J,K))` (44); `     &           +XX(2,I)*ZZ(2,K)*( GGY(I,J+1,K)*VV(I,J+1,K)` (45); `     &                             -GGY(I,J  ,K)*VV(I,J  ,K))` (46); `     &           +XX(2,I)*YY(2,J)*( GGZ(I,J,K+1)*WW(I,J,K+1)` (47); `     &                             -GGZ(I,J,K  )*WW(I,J,K  ))` (48). `              VAL=VAL+VD*VD` (49). `            ENDIF` (50). ` 100      CONTINUE` (51). ` 110    CONTINUE` (52). ` 120  CONTINUE` (53). `      W=VAL` (54). `      CALL VF_P1SUMD(W,VAL)` (55). `      VAL=SQRT(VAL)` (56). |
| 58–65 | 시작 시 `      SUBROUTINE VF_CDIV00(VAL,XX,YY,ZZ,UU,VV,WW,GGX,GGY,GGZ,INDC)` (1) 블록 안. 공통 종료 경로다. 원문: `C     -- 実行文の終了 --` (58) (실행문 종료). `      GOTO 9999` (59). `C==== 終了 ===========================================================` (61) (종료). ` 9999 CONTINUE` (63). `      RETURN` (64). `      END` (65). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
