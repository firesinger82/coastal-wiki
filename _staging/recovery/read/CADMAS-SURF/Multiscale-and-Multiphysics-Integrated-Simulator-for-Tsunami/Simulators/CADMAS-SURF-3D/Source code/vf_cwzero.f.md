---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Source code/vf_cwzero.f
lines: 86
sha256: 60ff562e13f303538451a80a09c71986403ebbe04f87bb37a4519179bbfe208b
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# vf_cwzero.f — 판독 구간 기록

구간은 1행부터 86행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–34 | 조파(wave generation) 수위가 0이 되는 무차원 위상을 구한다. 구간 검색 분할 수 NB=100, 이분법(bisection method) 최대 반복 NI=20이다. 기본 EPS는 1.0E-8이며 양수 파형 종류에서는 1.0E-6이다. 기본 해는 0.5이다. 원문: `      SUBROUTINE VF_CWZERO(WVZERO,IWVTYP)` (1) `CD=== 概要 ===========================================================` (3) (개요) `CDT   VF_CWZERO:水位変動がゼロになるときの無次元位相を求める` (5) (수위 변동이 0이 되는 무차원 위상 계산) `C==== 宣言 ===========================================================` (7) (선언) `C     -- 大域型 --` (9) (전역 자료형) `      IMPLICIT INTEGER(I-N),DOUBLE PRECISION(A-H,O-Z)` (10) `CD    -- 引数 --` (12) (인수) `CD    WVZERO : OUT : R*8 : 水位変動がゼロになるときの無次元位相` (13) (수위 변동이 0이 되는 무차원 위상) `CD    IWVTYP : IN  : I*4 : 造波波形の種別` (14) (조파(wave generation) 파형 종류) `CD                         =-2:Stokes波(第5次近似解)` (15) (-2: Stokes 파(Stokes wave). 5차 근사해) `CD                         =-1:Cnoidal波(第3次近似解)` (16) (-1: 크노이드파(cnoidal wave). 3차 근사해) `CD                         > 0:流れ関数法Bとその次数` (17) (양수: 흐름함수법 B(stream function method B)와 그 차수) `CD    -- 局所変数 --` (19) (지역 변수) `      REAL*4 R4TN,R4Z,R4TN1,R4Z1,R4TN2,R4Z2,EPS` (20) `C==== 実行 ===========================================================` (22) (실행) `CD    -- 初期設定 --` (24) (초기 설정) `C     * 初期区間検索時の分割数` (25) (초기 구간 검색 분할 수) `      NB=100` (26) `C     * 2分法の最大反復回数` (27) (이분법 최대 반복 횟수) `      NI=20` (28) `C     * 収束判定のための微小量` (29) (수렴 판정용 작은 값) `      EPS=1.0E-8` (30) `      IF (IWVTYP.GT.0) EPS=1.0E-6` (31) `C     * 解のデフォルト値(解が求まらないとき)` (32) (해를 구하지 못한 경우의 기본값) `      WVZERO=0.5D0` (33) |
| 35–59 | 시작 시 1행 VF_CWZERO 루틴 안이며 조건·루프 밖. 위상 1에서 시작하고 0.5까지 감소시키며 VF_CWMAK1을 호출해 영점 또는 부호 변화 구간을 찾는다. 앞의 수위 절댓값 검사에서 빠져나가지 않고 `R4TN1.EQ.R4TN2`이면 `GOTO 9000`으로 79행 `9000 CONTINUE`에 이동한다. 이 경우 WVZERO는 33행의 기본값을 유지한다. 42·56행의 `GOTO 9000`도 같은 레이블로 이동한다. 원문: `CD    -- 初期区間の検索(無次元位相1.0から不方向へ) --` (35) (초기 구간 검색. 무차원 위상 1.0에서 원문 '不方向' 방향으로. 실행식은 감소 방향) `      R4TN1=1.0E0` (36) `      WVT=DBLE(R4TN1)` (37) `      CALL VF_CWMAK1(WVT,WVZ,IWVTYP)` (38) `      R4Z1=REAL(WVZ)` (39) `      IF (ABS(R4Z1).LT.EPS) THEN` (40) `        WVZERO=DBLE(R4TN1)` (41) `        GOTO 9000` (42) `      ENDIF` (43) `      DO 100 L=1,NB` (44) `        R4TN2=1.0E0-0.5E0*REAL(L)/REAL(NB)` (45) `        WVT=DBLE(R4TN2)` (46) `        CALL VF_CWMAK1(WVT,WVZ,IWVTYP)` (47) `        R4Z2=REAL(WVZ)` (48) `        IF (R4Z1*R4Z2.LE.0.0E0) GOTO 110` (49) `        R4TN1=R4TN2` (50) `        R4Z1 =R4Z2` (51) ` 100  CONTINUE` (52) ` 110  CONTINUE` (53) `      IF (ABS(R4Z2).LT.EPS) THEN` (54) `        WVZERO=DBLE(R4TN2)` (55) `        GOTO 9000` (56) `      ENDIF` (57) `      IF (R4TN1.EQ.R4TN2) GOTO 9000` (58) [11-04 전수 검증 보완] |
| 60–86 | 시작 시 1행 VF_CWZERO 루틴 안이며 조건·루프 밖. 최대 NI회 구간 중점을 평가한다. 수위 절댓값이 EPS 미만이면 종료하며 그렇지 않으면 부호에 따라 끝점을 교체한다. 원문: `CD    -- 2分法により解を求める --` (60) (이분법으로 해 계산) `      DO 200 L=1,NI` (61) `        R4TN=(R4TN1+R4TN2)*0.5E0` (62) `        WVZERO=DBLE(R4TN)` (63) `        WVT=WVZERO` (64) `        CALL VF_CWMAK1(WVT,WVZ,IWVTYP)` (65) `        R4Z=REAL(WVZ)` (66) `        IF (ABS(R4Z).LT.EPS) GOTO 210` (67) `        IF (R4Z1*R4Z.GE.0.0E0) THEN` (68) `          R4TN1=R4TN` (69) `          R4Z1 =R4Z` (70) `        ELSE` (71) `          R4TN2=R4TN` (72) `          R4Z2 =R4Z` (73) `        ENDIF` (74) ` 200  CONTINUE` (75) ` 210  CONTINUE` (76) `C     -- 実行文の終了 --` (78) (실행문 종료) ` 9000 CONTINUE` (79) `      GOTO 9999` (80) `C==== 終了 ===========================================================` (82) (종료) ` 9999 CONTINUE` (84) `      RETURN` (85) `      END` (86) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 61–76: NI=20을 소진해도 별도 오류 호출 없이 마지막 중점 WVZERO를 반환한다.
- 35·44–45: 검색 방향 주석에는 '不方向'이라고 적혀 있다. 실행식은 1.0에서 0.5로 감소한다.
