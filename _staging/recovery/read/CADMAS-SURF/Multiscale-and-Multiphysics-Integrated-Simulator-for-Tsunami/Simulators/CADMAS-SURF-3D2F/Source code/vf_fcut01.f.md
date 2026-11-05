---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D2F/Source code/vf_fcut01.f
lines: 67
sha256: 314f96f2342dd8a14f2c3fde05176156658bf1703447257c70bbe0ac67e2f6d9
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# vf_fcut01.f — 판독 구간 기록

구간은 1행부터 67행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–32 | VOF 함수 절단(cutoff) 및 공간 적분 루틴과 공극률(porosity)·병렬 버퍼(buffer) 배열 선언이다(1–29).<br>`      SUBROUTINE VF_FCUT01(XX,YY,ZZ,FF,GGV,DBUF,NF)` (1).<br>`CD=== 概要 ===========================================================` (3) (개요).<br>`CDT   VF_FCUT01:VOF関数Fのカットオフ(0.0=<F=<1.0)と空間積分の計算` (5) (VF_FCUT01:VOF 함수 절단(cutoff)(0.0=<F=<1.0) 및 공간 적분 계산).<br>`C==== 宣言 ===========================================================` (7) (선언).<br>`C     -- 大域型 --` (9) (전역 형).<br>`      IMPLICIT INTEGER(I-N),DOUBLE PRECISION(A-H,O-Z)` (10).<br>`C     -- 大域変数 --` (12) (전역 변수).<br>`      INCLUDE 'VF_A0PRM.h'` (13).<br>`      INCLUDE 'VF_ACOMPR.h'` (14).<br>`      INCLUDE 'VF_ANUMBI.h'` (15).<br>`      INCLUDE 'VF_APARAI.h'` (16).<br>`CD    -- 引数 --` (18) (인수).<br>`CD    XX(MAXG1,NUMI)   : IN  : R*8 : x方向格子座標等` (19) (XX(MAXG1,NUMI)   : IN  : R*8 : x방향 격자 좌표 등).<br>`CD    YY(MAXG1,NUMJ)   : IN  : R*8 : y方向格子座標等` (20) (YY(MAXG1,NUMJ)   : IN  : R*8 : y방향 격자 좌표 등).<br>`CD    ZZ(MAXG1,NUMK)   : IN  : R*8 : z方向格子座標等` (21) (ZZ(MAXG1,NUMK)   : IN  : R*8 : z방향 격자 좌표 등).<br>`CD    FF(@FOR-3D@)     : I/O : R*8 : VOF関数F` (22) (FF(@FOR-3D@)     : I/O : R*8 : VOF 함수).<br>`CD    GGV(@FOR-3D@)    : IN  : R*8 : 空隙率` (23) (GGV(@FOR-3D@)    : IN  : R*8 : 공극률(porosity)).<br>`CD    DBUF(NUMBUF*MAXBUF) : OUT :R*8 : 並列用のバッファ` (24) (DBUF(NUMBUF*MAXBUF) : OUT :R*8 : 병렬 처리용 버퍼(buffer)).<br>`CD    NF(@FOR-3D@)     : IN  : I*4 : セルの状態を示すインデックス` (25) (NF(@FOR-3D@)     : IN  : I*4 : 셀 상태를 나타내는 인덱스).<br>`      DIMENSION XX(MAXG1,NUMI),YY(MAXG1,NUMJ),ZZ(MAXG1,NUMK)` (26).<br>`      DIMENSION FF(NUMI,NUMJ,NUMK),GGV(NUMI,NUMJ,NUMK)` (27).<br>`      DIMENSION DBUF(NUMBUF*MAXBUF)` (28).<br>`      DIMENSION NF(NUMI,NUMJ,NUMK)` (29).<br>`C==== 実行 ===========================================================` (31) (실행). |
| 33–52 | 시작 시 1행 SUBROUTINE VF_FCUT01 루틴 안. FSUM과 FCUT를 0으로 시작한다(34–35). 유효 셀의 공극 부피를 계산하고 FUPPER 초과는 F=1, FLOWER 미만은 F=0으로 바꾼다(39–47). FCUT에는 절단 전 F에서 절단 후 F를 뺀 값에 V를 곱해 누적한다(42·45). FSUM에는 절단 후 F에 V를 곱해 누적한다(48).<br>`CD    -- F値のカットオフと空間積分 --` (33) (F값 절단 및 공간 적분).<br>`      FSUM=0.0D0` (34).<br>`      FCUT=0.0D0` (35).<br>`      DO 220 K=2,NUMK-1` (36).<br>`        DO 210 J=MYJS,MYJE` (37).<br>`          DO 200 I=MYIS,MYIE` (38).<br>`            IF (NF(I,J,K).GT.-1) THEN` (39).<br>`              V=XX(2,I)*YY(2,J)*ZZ(2,K)*GGV(I,J,K)` (40).<br>`              IF     (FF(I,J,K).GT.FUPPER) THEN` (41).<br>`                FCUT=FCUT+(FF(I,J,K)-1.0D0)*V` (42).<br>`                FF(I,J,K)=1.0D0` (43).<br>`              ELSEIF (FF(I,J,K).LT.FLOWER) THEN` (44).<br>`                FCUT=FCUT+(FF(I,J,K)-0.0D0)*V` (45).<br>`                FF(I,J,K)=0.0D0` (46).<br>`              ENDIF` (47).<br>`              FSUM=FSUM+FF(I,J,K)*V` (48).<br>`            ENDIF` (49).<br>` 200      CONTINUE` (50).<br>` 210    CONTINUE` (51).<br>` 220  CONTINUE` (52).<br>41–47행 분기 사슬에는 ELSE가 없다. 두 조건이 모두 거짓이면 F를 바꾸지 않는다. [11-04 전수 검증 보완] |
| 53–67 | 시작 시 1행 SUBROUTINE VF_FCUT01 루틴 안. W에 FSUM을 복사하고 `CALL VF_P1SUMD(W,FSUM)`을 실행한다(53–54). 이어 W에 FCUT를 복사하고 `CALL VF_P1SUMD(W,FCUT)`을 실행한다(55–56). 그 뒤 `CALL VF_P3SRD2(FF,DBUF,0)`을 실행한다(58). 해석: 앞 두 호출은 합산을 위한 것으로 보인다. 해석: 마지막 호출은 FF의 병렬 교환을 위한 것으로 보인다.<br>`      W=FSUM` (53).<br>`      CALL VF_P1SUMD(W,FSUM)` (54).<br>`      W=FCUT` (55).<br>`      CALL VF_P1SUMD(W,FCUT)` (56).<br>`      CALL VF_P3SRD2(FF,DBUF,0)` (58).<br>`C     -- 実行文の終了 --` (60) (실행문 종료).<br>`      GOTO 9999` (61).<br>`C==== 終了 ===========================================================` (63) (종료).<br>` 9999 CONTINUE` (65).<br>`      RETURN` (66).<br>`      END` (67). [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 41·44: 절단 기준은 1 및 0과의 직접 비교가 아니라 FUPPER 초과·FLOWER 미만이다. 두 임계값과 같은 F는 이 분기에서 바꾸지 않는다.
- 34–35·42·45: FCUT는 매 호출 0으로 초기화하며 절단 전 F에서 절단 후 1 또는 0을 뺀 부피 차를 부호 그대로 누적한다.
