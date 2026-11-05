---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Source code/vf_comak0.f
lines: 61
sha256: af317596489856e30fc66c1ee40e1d5b98402ff4014632f9fc64aeef7f945347
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# vf_comak0.f — 판독 구간 기록

구간은 1행부터 61행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–31 | 미소진폭파(small-amplitude wave)의 방사경계(radiation boundary)용 파장을 구한다. 암시적 자료형과 인수를 설명한다. Newton 방법(Newton method)의 최대 반복 횟수는 10이며 수렴 기준은 1.0D-10이다. 원문: `      SUBROUTINE VF_COMAK0(WVDPTH,WVPERI,PI,GG,WVLENG,IWVTYP)` (1) `CD=== 概要 ===========================================================` (3) (개요) `CDT   VF_COMAK0:微小振幅波の波速の計算(微小振幅波による放射境界用)` (5) (미소진폭파의 파속 계산. 미소진폭파 방사경계용) `C==== 宣言 ===========================================================` (7) (선언) `C     -- 大域型 --` (9) (전역 자료형) `      IMPLICIT INTEGER(I-N),DOUBLE PRECISION(A-H,O-Z)` (10) `CD    -- 引数 --` (12) (인수) `CD    WVDPTH : IN  : R*8 : 水深` (13) (수심) `CD    WVPERI : IN  : R*8 : 周期` (14) (주기) `CD    PI     : IN  : R*8 : 円周率` (15) (원주율) `CD    GG     : IN  : R*8 : 重力加速度` (16) (중력가속도) `CD    WVLENG : OUT : R*8 : 波長` (17) (파장) `CD    IWVTYP : IN  : I*4 : 開境界の種別` (18) (개방경계 종류) `CD                         = 0:放射境界(微小振幅波の波速)` (19) (0: 방사경계. 미소진폭파의 파속) `C==== 実行 ===========================================================` (21) (실행) `CD    -- 初期設定 --` (23) (초기 설정) `C     * Newton法の最大反復回数` (24) (Newton 방법의 최대 반복 횟수) `      MI=10` (25) `C     * 収束判定のための微小量` (26) (수렴 판정용 작은 값) `      EPS=1.0D-10` (27) `C     * エラーチェッカー用のダミー` (28) (오류 검사기용 더미) `      IDMY=IWVTYP` (29) `      IDMY=IDMY` (30) |
| 32–61 | 시작 시 1행 VF_COMAK0 루틴 안이며 조건·루프 밖. 무차원 수심 D에 따라 초기값을 정한다. Newton 반복에서 상대 변화가 EPS 이하면 빠져나온다. 최종 X로 파장을 계산한다. 원문: `CD    -- 初期値の計算 --` (32) (초기값 계산) `      D=4.0D0*PI*PI*WVDPTH/GG/WVPERI/WVPERI` (33) `      IF (D.GE.1.0D0) THEN` (34) `        X=D` (35) `      ELSE` (36) `        X=SQRT(D)` (37) `      ENDIF` (38) `CD    -- Newton法による収束計算 --` (40) (Newton 방법에 의한 수렴 계산) `      DO 10 ITR=1,MI` (41) `        EXPX =EXP(X)` (42) `        EXPXI=1.0D0/EXPX` (43) `        COTHX=(EXPX+EXPXI)/(EXPX-EXPXI)` (44) `        DX=(X-D*COTHX)/(1.0D0+D*(COTHX*COTHX-1.0D0))` (45) `        X =X-DX` (46) `        IF (ABS(DX/X).LE.EPS) GOTO 20` (47) ` 10   CONTINUE` (48) ` 20   CONTINUE` (49) `CD    -- 波長の計算 --` (51) (파장 계산) `      WVLENG=2.0D0*PI*WVDPTH/X` (52) `C     -- 実行文の終了 --` (54) (실행문 종료) `      GOTO 9999` (55) `C==== 終了 ===========================================================` (57) (종료) ` 9999 CONTINUE` (59) `      RETURN` (60) `      END` (61) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 25·27·41–52: MI=10을 소진한 경우에도 별도 오류 호출 없이 파장 계산으로 진행한다.
- 29–30: IWVTYP는 IDMY에 복사한 뒤 IDMY 자기 대입에만 쓰인다.
