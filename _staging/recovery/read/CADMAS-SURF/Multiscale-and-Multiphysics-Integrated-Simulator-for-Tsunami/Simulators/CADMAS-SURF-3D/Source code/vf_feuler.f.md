---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Source code/vf_feuler.f
lines: 67
sha256: 1a3cd5a7e7da0b3aa5e58000caa75bee3af5762d9efe21a0a4b21f65c6c5fac9
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# vf_feuler.f — 판독 구간 기록

구간은 1행부터 67행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–41 | Euler 방법(Euler method)으로 VOF 함수를 시간 적분한다. 현재·시간 의존 공극률(porosity), 플럭스(flux), 생성량과 셀 상태 배열을 선언한다. 원문: 연속문: `      SUBROUTINE VF_FEULER(XX,YY,ZZ,FF,GGV,GGV0,DBUF,` (1); `     &                     FLFU,FLFV,FLFW,QF,NF)` (2) `CD=== 概要 ===========================================================` (4) (개요) `CDT   VF_FEULER:VOF関数Fの時間積分を計算(Euler法)` (6) (VOF 함수 시간 적분 계산. Euler 방법) `C==== 宣言 ===========================================================` (8) (선언) `C     -- 大域型 --` (10) (전역 자료형) `      IMPLICIT INTEGER(I-N),DOUBLE PRECISION(A-H,O-Z)` (11) `C     -- 大域変数 --` (13) (전역 변수) `      INCLUDE 'VF_A0PRM.h'` (14) `      INCLUDE 'VF_ANUMBI.h'` (15) `      INCLUDE 'VF_APARAI.h'` (16) `      INCLUDE 'VF_ATIMEI.h'` (17) `      INCLUDE 'VF_ATIMER.h'` (18) `CD    -- 引数 --` (20) (인수) `CD    XX(MAXG1,NUMI)   : IN  : R*8 : x方向格子座標等` (21) (x방향 격자 좌표 등) `CD    YY(MAXG1,NUMJ)   : IN  : R*8 : y方向格子座標等` (22) (y방향 격자 좌표 등) `CD    ZZ(MAXG1,NUMK)   : IN  : R*8 : z方向格子座標等` (23) (z방향 격자 좌표 등) `CD    FF(@FOR-3D@)     : I/O : R*8 : VOF関数F` (24) (VOF 함수) `CD    GGV(@FOR-3D@)    : IN  : R*8 : 空隙率` (25) (공극률(porosity)) `CD    GGV0(@FOR-3D@)   : IN  : R*8 : 空隙率(時間依存用)` (26) (시간 의존 공극률(porosity)) `CD    DBUF(NUMBUF*MAXBUF) : OUT :R*8 : 並列用のバッファ` (27) (병렬 통신 버퍼(buffer)) `CD    FLFU(@FOR-3D@)   : IN  : R*8 : VOF関数Fのx方向フラックス` (28) (VOF 함수의 x방향 플럭스(flux)) `CD    FLFV(@FOR-3D@)   : IN  : R*8 : VOF関数Fのy方向フラックス` (29) (VOF 함수의 y방향 플럭스(flux)) `CD    FLFW(@FOR-3D@)   : IN  : R*8 : VOF関数Fのz方向フラックス` (30) (VOF 함수의 z방향 플럭스(flux)) `CD    QF(@FOR-3D@)     : IN  : R*8 : VOF関数Fの生成消滅` (31) (VOF 함수 생성·소멸) `CD    NF(@FOR-3D@)     : IN  : I*4 : セルの状態を示すインデックス` (32) (셀(cell) 상태 인덱스(index)) `      DIMENSION XX(MAXG1,NUMI),YY(MAXG1,NUMJ),ZZ(MAXG1,NUMK)` (33) `      DIMENSION FF  (NUMI,NUMJ,NUMK),GGV (NUMI,NUMJ,NUMK)` (34) `      DIMENSION GGV0(NUMI,NUMJ,NUMK),DBUF(NUMBUF*MAXBUF)` (35) `      DIMENSION FLFU(NUMI,NUMJ,NUMK),FLFV(NUMI,NUMJ,NUMK)` (36) `      DIMENSION FLFW(NUMI,NUMJ,NUMK),QF  (NUMI,NUMJ,NUMK)` (37) `      DIMENSION NF  (NUMI,NUMJ,NUMK)` (38) `C==== 実行 ===========================================================` (40) (실행) |
| 42–67 | 시작 시 1–2행 VF_FEULER 루틴 안이며 조건·루프 밖. NF=-1이 아닌 담당 셀에서 LOOPS에 따라 G0를 정한다. 각 방향 플럭스 차에 XX(4,I)·YY(4,J)·ZZ(4,K)를 각각 곱한 값과 DTNOW*QF를 더해 DF를 구한다. 해석: 이 계수를 격자 역폭으로 볼 수 있지만 이 구간에는 배열의 네 번째 성분 정의가 없다. (G0*FF+DF)/GGV로 갱신한 뒤 VF_P3SRD2를 호출한다. 원문: `CD    -- 時間積分 --` (42) (시간 적분) `      DO 120 K=2,NUMK-1` (43) `        DO 110 J=MYJS,MYJE` (44) `          DO 100 I=MYIS,MYIE` (45) `            IF (NF(I,J,K).NE.-1) THEN` (46) `              G0=GGV(I,J,K)-(GGV(I,J,K)-GGV0(I,J,K))*DBLE(LOOPS)` (47) 연속문: `              DF=( XX(4,I)*(FLFU(I+1,J,K)-FLFU(I,J,K))` (48); `     &            +YY(4,J)*(FLFV(I,J+1,K)-FLFV(I,J,K))` (49); `     &            +ZZ(4,K)*(FLFW(I,J,K+1)-FLFW(I,J,K))` (50); `     &            +DTNOW*QF(I,J,K)                    )` (51) `              FF(I,J,K)=(G0*FF(I,J,K)+DF)/GGV(I,J,K)` (52) `            ENDIF` (53) ` 100      CONTINUE` (54) ` 110    CONTINUE` (55) ` 120  CONTINUE` (56) `      CALL VF_P3SRD2(FF,DBUF,0)` (58) `C     -- 実行文の終了 --` (60) (실행문 종료) `      GOTO 9999` (61) `C==== 終了 ===========================================================` (63) (종료) ` 9999 CONTINUE` (65) `      RETURN` (66) `      END` (67) [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 47: G0는 DBLE(LOOPS)를 직접 곱한 선형식으로 정한다.
- 52: FF 갱신은 GGV로 나누며 이 루틴에는 GGV=0 검사가 없다.
