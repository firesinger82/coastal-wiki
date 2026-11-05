---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D2F/Source code/vf_seuler.f
lines: 68
sha256: 1ffd1710c296990e669888b96ec941b5529e360cdc2dc4b08df5225e898acab4
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# vf_seuler.f — 판독 구간 기록

구간은 1행부터 68행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–42 | 스칼라량(scalar quantity)의 오일러법(Euler method) 시간 적분(time integration) 루틴이다. 두 공극률(porosity)·세 플럭스(flux)·생성소멸량과 시간 관련 INCLUDE를 선언한다.<br>원문: `      SUBROUTINE VF_SEULER(XX,YY,ZZ,CC,GGV,GGV0,DBUF,` (1) / `     &                     FLCU,FLCV,FLCW,QC,NF)` (2) (하나의 고정형식 연속문, 1–2행); 주석: `CD=== 概要 ===========================================================` (4) (개요); 주석: `CDT   VF_SEULER:スカラ量の時間積分を計算(Euler法)` (6) (스칼라량의 시간 적분 계산: 오일러법); 주석: `C==== 宣言 ===========================================================` (8) (선언); 주석: `C     -- 大域型 --` (10) (대역형); `      IMPLICIT INTEGER(I-N),DOUBLE PRECISION(A-H,O-Z)` (11); 주석: `C     -- 大域変数 --` (13) (대역변수); `      INCLUDE 'VF_A0PRM.h'` (14); `      INCLUDE 'VF_ANUMBI.h'` (15); `      INCLUDE 'VF_APARAI.h'` (16); `      INCLUDE 'VF_ATIMEI.h'` (17); `      INCLUDE 'VF_ATIMER.h'` (18); 주석: `CD    -- 引数 --` (20) (인수); 주석: `CD    XX(MAXG1,NUMI)   : IN  : R*8 : x方向格子座標等` (21) (x방향 격자 좌표 등); 주석: `CD    YY(MAXG1,NUMJ)   : IN  : R*8 : y方向格子座標等` (22) (y방향 격자 좌표 등); 주석: `CD    ZZ(MAXG1,NUMK)   : IN  : R*8 : z方向格子座標等` (23) (z방향 격자 좌표 등); 주석: `CD    CC(@FOR-3D@)     : I/O : R*8 : スカラ量` (24) (스칼라량(scalar quantity)); 주석: `CD    GGV(@FOR-3D@)    : IN  : R*8 : 空隙率` (25) (공극률(porosity)); 주석: `CD    GGV0(@FOR-3D@)   : IN  : R*8 : 空隙率(時間依存用)` (26) (시간 의존 공극률(porosity)); 주석: `CD    DBUF(NUMBUF*MAXBUF) : OUT :R*8 : 並列用のバッファ` (27) (병렬용 버퍼(buffer)); 주석: `CD    FLCU(@FOR-3D@)   : IN  : R*8 : x方向フラックス` (28) (x방향 플럭스(flux)); 주석: `CD    FLCV(@FOR-3D@)   : IN  : R*8 : y方向フラックス` (29) (y방향 플럭스(flux)); 주석: `CD    FLCW(@FOR-3D@)   : IN  : R*8 : z方向フラックス` (30) (z방향 플럭스(flux)); 주석: `CD    QC(@FOR-3D@)     : IN  : R*8 : 生成消滅` (31) (생성·소멸); 주석: `CD    NF(@FOR-3D@)     : IN  : I*4 : セルの状態を示すインデックス` (32) (셀 상태 인덱스(index)); `      DIMENSION XX(MAXG1,NUMI),YY(MAXG1,NUMJ),ZZ(MAXG1,NUMK)` (33); `      DIMENSION CC  (NUMI,NUMJ,NUMK)` (34); `      DIMENSION GGV (NUMI,NUMJ,NUMK),GGV0(NUMI,NUMJ,NUMK)` (35); `      DIMENSION DBUF(NUMBUF*MAXBUF)` (36); `      DIMENSION FLCU(NUMI,NUMJ,NUMK),FLCV(NUMI,NUMJ,NUMK)` (37); `      DIMENSION FLCW(NUMI,NUMJ,NUMK),QC  (NUMI,NUMJ,NUMK)` (38); `      DIMENSION NF  (NUMI,NUMJ,NUMK)` (39); 주석: `C==== 実行 ===========================================================` (41) (실행). |
| 43–58 | 시작 시 1행 루틴 안. 내부 격자에서 NF>-1일 때 갱신한다. G0에는 LOOPS를 사용한 공극률 차 보정을 적용한다. DS는 세 플럭스 차의 격자별 가중 합과 QC이며 CC=(G0*CC+DTNOW*DS)/GGV로 갱신한다. NF=0 조건은 C2F 주석이다.<br>원문: 주석: `CD    -- 時間積分 --` (43) (시간 적분); `      DO 120 K=2,NUMK-1` (44); `        DO 110 J=MYJS,MYJE` (45); `          DO 100 I=MYIS,MYIE` (46); 주석: `C2F         IF (NF(I,J,K).EQ.0) THEN` (47); `            IF (NF(I,J,K).GT.-1) THEN` (48); `              G0=GGV(I,J,K)-(GGV(I,J,K)-GGV0(I,J,K))*DBLE(LOOPS)` (49); `              DS=( XX(4,I)*(FLCU(I+1,J,K)-FLCU(I,J,K))` (50) / `     &            +YY(4,J)*(FLCV(I,J+1,K)-FLCV(I,J,K))` (51) / `     &            +ZZ(4,K)*(FLCW(I,J,K+1)-FLCW(I,J,K))+QC(I,J,K))` (52) (하나의 고정형식 연속문, 50–52행); `              CC(I,J,K)=(G0*CC(I,J,K)+DTNOW*DS)/GGV(I,J,K)` (53); `            ENDIF` (54); ` 100      CONTINUE` (55); ` 110    CONTINUE` (56); ` 120  CONTINUE` (57). |
| 59–68 | 시작 시 1행 루틴 안. VF_P3SRD2(CC,DBUF,0)를 호출하여 병렬 경계 자료를 교환한 뒤 반환한다. 호출 기능의 근거는 같은 원문 디렉터리의 `vf_p3srd2.f:5,19–21,30–42`이다. 그 파일의 주석은 3차원 실수 자료 두 층의 송수신과 ISW=0의 C 정의 위치를 명시한다.<br>원문: `      CALL VF_P3SRD2(CC,DBUF,0)` (59); 주석: `C     -- 実行文の終了 --` (61) (실행문 종료); `      GOTO 9999` (62); 주석: `C==== 終了 ===========================================================` (64) (종료); ` 9999 CONTINUE` (66); `      RETURN` (67); `      END` (68). [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 47–48: NF=0 조건은 주석이다. 실행 조건은 NF>-1이다.
- 49·53: G0에는 DBLE(LOOPS)를 곱한 공극률 차가 포함된다. 최종 CC 대입은 GGV로 나누며 이 블록에는 GGV=0 검사가 없다.
