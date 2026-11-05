---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Source code/vf_cwmak1.f
lines: 49
sha256: 97f81a473370fc3c08f151b7cbaf63966f250ce1679cd3ffd11c2028bf27edf4
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# vf_cwmak1.f — 판독 구간 기록

구간은 1행부터 49행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–24 | 무차원 위상으로 조파(wave generation) 수위를 구한다. 인수와 REAL*4 작업 변수를 선언한다. 원문: `      SUBROUTINE VF_CWMAK1(WVT,WVZ,IWVTYP)` (1) `CD=== 概要 ===========================================================` (3) (개요) `CDT   VF_CWMAK1:造波のための水位の計算` (5) (조파용 수위 계산) `C==== 宣言 ===========================================================` (7) (선언) `C     -- 大域型 --` (9) (전역 자료형) `      IMPLICIT INTEGER(I-N),DOUBLE PRECISION(A-H,O-Z)` (10) `CD    -- 引数 --` (12) (인수) `CD    WVT    : IN  : R*8 : 無次元位相` (13) (무차원 위상) `CD    WVZ    : OUT : R*8 : 水位変動` (14) (수위 변동) `CD    IWVTYP : IN  : I*4 : 造波波形の種別` (15) (조파(wave generation) 파형 종류) `CD                         =-2:Stokes波(第5次近似解)` (16) (-2: Stokes 파(Stokes wave). 5차 근사해) `CD                         =-1:Cnoidal波(第3次近似解)` (17) (-1: 크노이드파(cnoidal wave). 3차 근사해) `CD                         > 0:流れ関数法Bとその次数` (18) (양수: 흐름함수법 B(stream function method B)와 그 차수) `CD    -- 局所変数 --` (20) (지역 변수) `      REAL*4 R4TN,R4Z,R4U,R4W,R4P,R4UT,R4WT` (21) `C==== 実行 ===========================================================` (23) (실행) |
| 25–49 | 시작 시 1행 VF_CWMAK1 루틴 안이며 조건·루프 밖. -2는 VF_STK1, -1은 VF_CND1을 호출하고 수위를 0.01배 한다. 양수는 vf_sfmb1 호출 후 vf_sfmb2를 더미 초기화용으로 호출한다. 그 외는 `CALL VF_A2ERR('VF_CWMAK1','P.G ERROR.')`를 실행한다. 원문: `CD    -- 水位変動を求める --` (25) (수위 변동 계산) `      R4TN=REAL(WVT)` (26) `      IF     (IWVTYP.EQ.-2) THEN` (27) `        CALL VF_STK1(R4TN,R4Z)` (28) `        WVZ=DBLE(R4Z)*0.01D0` (29) `      ELSEIF (IWVTYP.EQ.-1) THEN` (30) `        CALL VF_CND1(R4TN,R4Z)` (31) `        WVZ=DBLE(R4Z)*0.01D0` (32) `      ELSEIF (IWVTYP.GE. 1) THEN` (33) `        CALL vf_sfmb1(R4TN,R4Z)` (34) `        WVZ=DBLE(R4Z)` (35) `C       * SFMB2のダミー初期化` (36) (SFMB2의 더미 초기화) `        CALL vf_sfmb2(-1.0,0.0,R4U,R4W,R4UT,R4WT,R4P)` (37) `      ELSE` (38) `        CALL VF_A2ERR('VF_CWMAK1','P.G ERROR.')` (39) `      ENDIF` (40) `C     -- 実行文の終了 --` (42) (실행문 종료) `      GOTO 9999` (43) `C==== 終了 ===========================================================` (45) (종료) ` 9999 CONTINUE` (47) `      RETURN` (48) `      END` (49) [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 21·37: vf_sfmb2에 -1.0과 0.0을 넘긴다. 그 출력 변수들은 이후 참조하지 않는다.
