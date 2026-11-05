---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Source code/vf_fcut01.f
lines: 67
sha256: 5d8662134aa00fb52f0ebfac1ec0a727c321e9d9baa79992f931cc7e251dfd6e
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# vf_fcut01.f — 판독 구간 기록

구간은 1행부터 67행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–32 | VOF 함수 절단(cutoff) 및 공간 적분 루틴이다. 격자·공극률(porosity)·통신 버퍼와 셀 상태 배열을 선언한다. 원문: `      SUBROUTINE VF_FCUT01(XX,YY,ZZ,FF,GGV,DBUF,NF)` (1) `CD=== 概要 ===========================================================` (3) (개요) `CDT   VF_FCUT01:VOF関数Fのカットオフ(0.0=<F=<1.0)と空間積分の計算` (5) (VOF 함수의 0.0=<F=<1.0 절단 및 공간 적분 계산) `C==== 宣言 ===========================================================` (7) (선언) `C     -- 大域型 --` (9) (전역 자료형) `      IMPLICIT INTEGER(I-N),DOUBLE PRECISION(A-H,O-Z)` (10) `C     -- 大域変数 --` (12) (전역 변수) `      INCLUDE 'VF_A0PRM.h'` (13) `      INCLUDE 'VF_ACOMPR.h'` (14) `      INCLUDE 'VF_ANUMBI.h'` (15) `      INCLUDE 'VF_APARAI.h'` (16) `CD    -- 引数 --` (18) (인수) `CD    XX(MAXG1,NUMI)   : IN  : R*8 : x方向格子座標等` (19) (x방향 격자 좌표 등) `CD    YY(MAXG1,NUMJ)   : IN  : R*8 : y方向格子座標等` (20) (y방향 격자 좌표 등) `CD    ZZ(MAXG1,NUMK)   : IN  : R*8 : z方向格子座標等` (21) (z방향 격자 좌표 등) `CD    FF(@FOR-3D@)     : I/O : R*8 : VOF関数F` (22) (VOF 함수) `CD    GGV(@FOR-3D@)    : IN  : R*8 : 空隙率` (23) (공극률(porosity)) `CD    DBUF(NUMBUF*MAXBUF) : OUT :R*8 : 並列用のバッファ` (24) (병렬 통신 버퍼(buffer)) `CD    NF(@FOR-3D@)     : IN  : I*4 : セルの状態を示すインデックス` (25) (셀(cell) 상태 인덱스(index)) `      DIMENSION XX(MAXG1,NUMI),YY(MAXG1,NUMJ),ZZ(MAXG1,NUMK)` (26) `      DIMENSION FF(NUMI,NUMJ,NUMK),GGV(NUMI,NUMJ,NUMK)` (27) `      DIMENSION DBUF(NUMBUF*MAXBUF)` (28) `      DIMENSION NF(NUMI,NUMJ,NUMK)` (29) `C==== 実行 ===========================================================` (31) (실행) |
| 33–67 | 시작 시 1행 VF_FCUT01 루틴 안이며 조건·루프 밖. NF=-1을 제외한다. `V=XX(2,I)*YY(2,J)*ZZ(2,K)*GGV(I,J,K)`를 계산한다. FF>FUPPER이면 1로 바꾼다. 앞 조건이 거짓이고 FF<FLOWER이면 0으로 바꾼다. 이 IF 사슬에는 ELSE가 없다. FCUT에는 변경 전 FF에서 변경 후 FF를 뺀 값에 V를 곱하여 더한다. FSUM에는 변경 후 FF*V를 더한다. 해석: XX·YY·ZZ의 두 번째 성분을 셀 폭으로 읽으면 V는 공극 부피이며 FSUM은 물 체적의 합이지만 이 구간에는 해당 성분 정의가 없다. VF_P1SUMD로 두 합을 집계하고 VF_P3SRD2로 FF를 교환한다. 원문: `CD    -- F値のカットオフと空間積分 --` (33) (VOF 함수 값 절단과 공간 적분) `      FSUM=0.0D0` (34) `      FCUT=0.0D0` (35) `      DO 220 K=2,NUMK-1` (36) `        DO 210 J=MYJS,MYJE` (37) `          DO 200 I=MYIS,MYIE` (38) `            IF (NF(I,J,K).NE.-1) THEN` (39) `              V=XX(2,I)*YY(2,J)*ZZ(2,K)*GGV(I,J,K)` (40) `              IF     (FF(I,J,K).GT.FUPPER) THEN` (41) `                FCUT=FCUT+(FF(I,J,K)-1.0D0)*V` (42) `                FF(I,J,K)=1.0D0` (43) `              ELSEIF (FF(I,J,K).LT.FLOWER) THEN` (44) `                FCUT=FCUT+(FF(I,J,K)-0.0D0)*V` (45) `                FF(I,J,K)=0.0D0` (46) `              ENDIF` (47) `              FSUM=FSUM+FF(I,J,K)*V` (48) `            ENDIF` (49) ` 200      CONTINUE` (50) ` 210    CONTINUE` (51) ` 220  CONTINUE` (52) `      W=FSUM` (53) `      CALL VF_P1SUMD(W,FSUM)` (54) `      W=FCUT` (55) `      CALL VF_P1SUMD(W,FCUT)` (56) `      CALL VF_P3SRD2(FF,DBUF,0)` (58) `C     -- 実行文の終了 --` (60) (실행문 종료) `      GOTO 9999` (61) `C==== 終了 ===========================================================` (63) (종료) ` 9999 CONTINUE` (65) `      RETURN` (66) `      END` (67) [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 41–46: 절단 조건은 1 및 0과의 직접 비교가 아니라 FUPPER·FLOWER와의 비교다.
- 42·45: FCUT는 FF에서 절단 후 값을 뺀 부호 있는 체적 차를 누적한다.
