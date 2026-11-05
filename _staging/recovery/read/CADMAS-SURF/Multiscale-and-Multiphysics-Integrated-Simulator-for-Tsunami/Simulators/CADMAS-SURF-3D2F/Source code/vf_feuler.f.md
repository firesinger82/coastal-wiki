---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D2F/Source code/vf_feuler.f
lines: 67
sha256: 20b71a56f17c320176f34e773dbf9968c896f6de47ec19b77973b070c8f179a1
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# vf_feuler.f — 판독 구간 기록

구간은 1행부터 67행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–40 | VF_FEULER는 VOF 함수(volume of fluid function)의 오일러법(Euler method) 시간 적분 루틴이다. 공극률(porosity) GGV·GGV0와 방향별 유량 및 생성 소멸항을 인수로 받는다. 배열 범위와 INCLUDE를 아래에 인용한다.<br>`      SUBROUTINE VF_FEULER(XX,YY,ZZ,FF,GGV,GGV0,DBUF,` (1)<br>`     &                     FLFU,FLFV,FLFW,QF,NF)` (2) (앞 행에서 이어지는 같은 문장)<br>`CD=== 概要 ===========================================================` (4) (개요)<br>`CDT   VF_FEULER:VOF関数Fの時間積分を計算(Euler法)` (6) (VOF 함수 F의 시간 적분 계산, 오일러법)<br>`C==== 宣言 ===========================================================` (8) (선언)<br>`C     -- 大域型 --` (10) (전역 형)<br>`      IMPLICIT INTEGER(I-N),DOUBLE PRECISION(A-H,O-Z)` (11)<br>`C     -- 大域変数 --` (13) (전역 변수)<br>`      INCLUDE 'VF_A0PRM.h'` (14)<br>`      INCLUDE 'VF_ANUMBI.h'` (15)<br>`      INCLUDE 'VF_APARAI.h'` (16)<br>`      INCLUDE 'VF_ATIMEI.h'` (17)<br>`      INCLUDE 'VF_ATIMER.h'` (18)<br>`CD    -- 引数 --` (20) (인수)<br>`CD    XX(MAXG1,NUMI)   : IN  : R*8 : x方向格子座標等` (21) (x방향 격자 좌표 등)<br>`CD    YY(MAXG1,NUMJ)   : IN  : R*8 : y方向格子座標等` (22) (y방향 격자 좌표 등)<br>`CD    ZZ(MAXG1,NUMK)   : IN  : R*8 : z方向格子座標等` (23) (z방향 격자 좌표 등)<br>`CD    FF(@FOR-3D@)     : I/O : R*8 : VOF関数F` (24) (VOF 함수 F)<br>`CD    GGV(@FOR-3D@)    : IN  : R*8 : 空隙率` (25) (공극률)<br>`CD    GGV0(@FOR-3D@)   : IN  : R*8 : 空隙率(時間依存用)` (26) (공극률, 시간 의존용)<br>`CD    DBUF(NUMBUF*MAXBUF) : OUT :R*8 : 並列用のバッファ` (27) (병렬용 버퍼)<br>`CD    FLFU(@FOR-3D@)   : IN  : R*8 : VOF関数Fのx方向フラックス` (28) (VOF 함수 F의 x방향 플럭스(flux))<br>`CD    FLFV(@FOR-3D@)   : IN  : R*8 : VOF関数Fのy方向フラックス` (29) (VOF 함수 F의 y방향 플럭스)<br>`CD    FLFW(@FOR-3D@)   : IN  : R*8 : VOF関数Fのz方向フラックス` (30) (VOF 함수 F의 z방향 플럭스)<br>`CD    QF(@FOR-3D@)     : IN  : R*8 : VOF関数Fの生成消滅` (31) (VOF 함수 F의 생성 소멸)<br>`CD    NF(@FOR-3D@)     : IN  : I*4 : セルの状態を示すインデックス` (32) (셀 상태 인덱스)<br>`      DIMENSION XX(MAXG1,NUMI),YY(MAXG1,NUMJ),ZZ(MAXG1,NUMK)` (33)<br>`      DIMENSION FF  (NUMI,NUMJ,NUMK),GGV (NUMI,NUMJ,NUMK)` (34)<br>`      DIMENSION GGV0(NUMI,NUMJ,NUMK),DBUF(NUMBUF*MAXBUF)` (35)<br>`      DIMENSION FLFU(NUMI,NUMJ,NUMK),FLFV(NUMI,NUMJ,NUMK)` (36)<br>`      DIMENSION FLFW(NUMI,NUMJ,NUMK),QF  (NUMI,NUMJ,NUMK)` (37)<br>`      DIMENSION NF  (NUMI,NUMJ,NUMK)` (38)<br>`C==== 実行 ===========================================================` (40) (실행) |
| 41–67 | 시작 시 1행 VF_FEULER 안. 43–45행 루프에서 NF>-1인 셀의 G0와 DF를 계산하고 FF를 갱신한다. G0는 47행 식에 따라 LOOPS=0이면 GGV이고 LOOPS=1이면 GGV0이다. 48–51행은 하나의 DF 대입문이다. VF_P3SRD2로 FF를 교환하고 반환한다.<br>`CD    -- 時間積分 --` (42) (시간 적분)<br>`      DO 120 K=2,NUMK-1` (43)<br>`        DO 110 J=MYJS,MYJE` (44)<br>`          DO 100 I=MYIS,MYIE` (45)<br>`            IF (NF(I,J,K).GT.-1) THEN` (46)<br>`              G0=GGV(I,J,K)-(GGV(I,J,K)-GGV0(I,J,K))*DBLE(LOOPS)` (47)<br>`              DF=( XX(4,I)*(FLFU(I+1,J,K)-FLFU(I,J,K))` (48)<br>`     &            +YY(4,J)*(FLFV(I,J+1,K)-FLFV(I,J,K))` (49) (앞 행에서 이어지는 같은 문장)<br>`     &            +ZZ(4,K)*(FLFW(I,J,K+1)-FLFW(I,J,K))` (50) (앞 행에서 이어지는 같은 문장)<br>`     &            +DTNOW*QF(I,J,K)                    )` (51) (앞 행에서 이어지는 같은 문장)<br>`              FF(I,J,K)=(G0*FF(I,J,K)+DF)/GGV(I,J,K)` (52)<br>`            ENDIF` (53)<br>` 100      CONTINUE` (54)<br>` 110    CONTINUE` (55)<br>` 120  CONTINUE` (56)<br>`      CALL VF_P3SRD2(FF,DBUF,0)` (58)<br>`C     -- 実行文の終了 --` (60) (실행문 종료)<br>`      GOTO 9999` (61)<br>`C==== 終了 ===========================================================` (63) (종료)<br>` 9999 CONTINUE` (65)<br>`      RETURN` (66)<br>`      END` (67) [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 47: G0 계산에는 DBLE(LOOPS)가 사용된다. LOOPS 값의 범위 검사는 이 루틴에 없다.
- 52: FF 갱신식의 분모는 GGV(I,J,K)이다. 해당 IF 조건은 NF(I,J,K).GT.-1이며 GGV의 0 여부를 직접 검사하지 않는다.
