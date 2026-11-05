---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Source code/vf_fgene.f
lines: 79
sha256: 05a4446f3da2b36ed209d46847cea51c1f742311a18d8d7caa68e7121809ae64
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# vf_fgene.f — 판독 구간 기록

구간은 1행부터 79행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–40 | 조파(wave generation) 소스에 의한 VOF 함수 생성·소멸항을 계산한다. ISCTYP(1)의 부호로 x 또는 y방향 지역 소스 면을 정한다. 35–39행의 IF 사슬에는 ELSE가 없다. ISCTYP(1)=0이면 IWS와 JWS는 초기값 0을 유지한다. 원문: `      SUBROUTINE VF_FGENE(XX,YY,FF,SRCUV,QF,NF)` (1) `CD=== 概要 ===========================================================` (3) (개요) `CDT   VF_FEULER:VOF関数Fの生成消滅項を計算` (5) (원문 루틴명은 VF_FEULER. VOF 함수 생성·소멸항 계산) `C==== 宣言 ===========================================================` (7) (선언) `C     -- 大域型 --` (9) (전역 자료형) `      IMPLICIT INTEGER(I-N),DOUBLE PRECISION(A-H,O-Z)` (10) `C     -- 大域変数 --` (12) (전역 변수) `      INCLUDE 'VF_A0PRM.h'` (13) `      INCLUDE 'VF_ANUMBI.h'` (14) `      INCLUDE 'VF_APARAI.h'` (15) `      INCLUDE 'VF_APHYSI.h'` (16) `CD    -- 引数 --` (18) (인수) `CD    XX(MAXG1,NUMI)   : IN  : R*8 : x方向格子座標等` (19) (x방향 격자 좌표 등) `CD    YY(MAXG1,NUMJ)   : IN  : R*8 : y方向格子座標等` (20) (y방향 격자 좌표 등) `CD    FF(@FOR-3D@)     : I/O : R*8 : VOF関数F` (21) (VOF 함수) `CD    SRCUV(NUMIJ,NUMK) : IN  : R*8 : 造波ソースのための流速` (22) (조파 소스용 유속) `CD    QF(@FOR-3D@)     : IN  : R*8 : VOF関数Fの生成消滅` (23) (VOF 함수 생성·소멸) `CD    NF(@FOR-3D@)     : IN  : I*4 : セルの状態を示すインデックス` (24) (셀(cell) 상태 인덱스(index)) `      DIMENSION XX(MAXG1,NUMI),YY(MAXG1,NUMJ)` (25) `      DIMENSION FF(NUMI,NUMJ,NUMK),SRCUV(NUMIJ,NUMK)` (26) `      DIMENSION QF(NUMI,NUMJ,NUMK)` (27) `      DIMENSION NF(NUMI,NUMJ,NUMK)` (28) `C==== 実行 ===========================================================` (30) (실행) `CD    -- 造波ソースのための定数 --` (32) (조파 소스용 상수) `      IWS=0` (33) `      JWS=0` (34) `      IF     (ISCTYP(1).GT.0) THEN` (35) `        IWS= ISCTYP(1)-(MYGIS-1)` (36) `      ELSEIF (ISCTYP(1).LT.0) THEN` (37) `        JWS=-ISCTYP(1)-(MYGJS-1)` (38) `      ENDIF` (39) [11-04 전수 검증 보완] |
| 41–79 | 시작 시 1행 VF_FGENE 루틴 안이며 조건·루프 밖. 담당 수평 셀을 수직 순회한다. `IWS.EQ.I`이면 NF=0에서 `Q=2.0D0*XX(4,I)*SRCUV(J,K)`와 `QF(I,J,K)=QF(I,J,K)+FF(I,J,K)*Q`를 계산한다. `JWS.EQ.J`이면 NF=0에서 `Q=2.0D0*YY(4,J)*SRCUV(I,K)`와 같은 QF 누적식을 계산한다. 각 조건 안에서 NF가 -1·0·8 이외이면 해당 방향의 같은 식을 계산한 뒤 `GOTO 110`으로 68행에 이동하여 K 루프를 벗어난다. 두 NF 조건 사슬에는 ELSE가 없다. NF=-1과 8에서는 QF에 더하지 않는다. 원문: `CD    -- 時間積分 --` (41) (시간 적분) `      DO 210 J=MYJS,MYJE` (42) `        DO 200 I=MYIS,MYIE` (43) `          DO 100 K=2,NUMK-1` (44) `            IF (IWS.EQ.I) THEN` (45) `              IF     (NF(I,J,K).EQ.-1) THEN` (46) `              ELSEIF (NF(I,J,K).EQ. 0) THEN` (47) `                Q=2.0D0*XX(4,I)*SRCUV(J,K)` (48) `                QF(I,J,K)=QF(I,J,K)+FF(I,J,K)*Q` (49) `              ELSEIF (NF(I,J,K).NE.8) THEN` (50) `                Q=2.0D0*XX(4,I)*SRCUV(J,K)` (51) `                QF(I,J,K)=QF(I,J,K)+FF(I,J,K)*Q` (52) `                GOTO 110` (53) `              ENDIF` (54) `            ENDIF` (55) `            IF (JWS.EQ.J) THEN` (56) `              IF     (NF(I,J,K).EQ.-1) THEN` (57) `              ELSEIF (NF(I,J,K).EQ. 0) THEN` (58) `                Q=2.0D0*YY(4,J)*SRCUV(I,K)` (59) `                QF(I,J,K)=QF(I,J,K)+FF(I,J,K)*Q` (60) `              ELSEIF (NF(I,J,K).NE.8) THEN` (61) `                Q=2.0D0*YY(4,J)*SRCUV(I,K)` (62) `                QF(I,J,K)=QF(I,J,K)+FF(I,J,K)*Q` (63) `                GOTO 110` (64) `              ENDIF` (65) `            ENDIF` (66) ` 100      CONTINUE` (67) ` 110      CONTINUE` (68) ` 200    CONTINUE` (69) ` 210  CONTINUE` (70) `C     -- 実行文の終了 --` (72) (실행문 종료) `      GOTO 9999` (73) `C==== 終了 ===========================================================` (75) (종료) ` 9999 CONTINUE` (77) `      RETURN` (78) `      END` (79) [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 1·5: 루틴 선언은 VF_FGENE이나 개요 주석의 루틴명은 VF_FEULER이다.
- 23·49·52·60·63: QF 인수 주석은 IN이지만 실행문은 QF에 누적 대입한다.
- 21·25–26·49·52·60·63: FF 인수 주석은 I/O이나 이 파일 실행부는 FF를 읽기만 한다.
