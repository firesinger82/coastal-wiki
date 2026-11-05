---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Source code/vf_cwmak2.f
lines: 55
sha256: 2b7ca9faf2ec1eafa8247240c9b302f9e9de61c0df36615ba0161f6f8768e29b
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# vf_cwmak2.f — 판독 구간 기록

구간은 1행부터 55행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–26 | 위상과 수직 좌표로 조파(wave generation) 유속을 구한다. 인수와 REAL*4 작업 변수를 선언한다. 원문: `      SUBROUTINE VF_CWMAK2(WVT,ZC,WVUN,WVUT,IWVTYP)` (1) `CD=== 概要 ===========================================================` (3) (개요) `CDT   VF_CWMAK2:造波のための流速の計算` (5) (조파용 유속 계산) `C==== 宣言 ===========================================================` (7) (선언) `C     -- 大域型 --` (9) (전역 자료형) `      IMPLICIT INTEGER(I-N),DOUBLE PRECISION(A-H,O-Z)` (10) `CD    -- 引数 --` (12) (인수) `CD    WVT    : IN  : R*8 : 無次元位相` (13) (무차원 위상) `CD    ZC     : IN  : R*8 : 鉛直座標(静面を基準)` (14) (정수면 기준 수직 좌표) `CD    WVUN   : OUT : R*8 : 法線方向流速` (15) (법선 방향 유속) `CD    WVUT   : OUT : R*8 : 接線方向流速` (16) (접선 방향 유속) `CD    IWVTYP : IN  : I*4 : 造波波形の種別` (17) (조파(wave generation) 파형 종류) `CD                         =-2:Stokes波(第5次近似解)` (18) (-2: Stokes 파(Stokes wave). 5차 근사해) `CD                         =-1:Cnoidal波(第3次近似解)` (19) (-1: 크노이드파(cnoidal wave). 3차 근사해) `CD                         > 0:流れ関数法Bとその次数` (20) (양수: 흐름함수법 B(stream function method B)와 그 차수) `CD    -- 局所変数 --` (22) (지역 변수) `      REAL*4 R4TN,R4Z,R4U,R4W,R4P,R4UT,R4WT` (23) `C==== 実行 ===========================================================` (25) (실행) |
| 27–55 | 시작 시 1행 VF_CWMAK2 루틴 안이며 조건·루프 밖. -2와 -1에서 ZC를 100배 변환한 뒤 VF_STK2 또는 VF_CND2를 호출하고 유속을 0.01배 한다. 양수는 vf_sfmb2의 유속을 배정도(double precision)로 옮긴다. 그 외는 `CALL VF_A2ERR('VF_CWMAK2','P.G ERROR.')`를 실행한다. 원문: `CD    -- 流速を求める --` (27) (유속 계산) `      R4TN=REAL(WVT)` (28) `      IF     (IWVTYP.EQ.-2) THEN` (29) `        R4Z =REAL(ZC*100.0D0)` (30) `        CALL VF_STK2(R4TN,R4Z,R4U,R4W,R4P)` (31) `        WVUN=DBLE(R4U)*0.01D0` (32) `        WVUT=DBLE(R4W)*0.01D0` (33) `      ELSEIF (IWVTYP.EQ.-1) THEN` (34) `        R4Z=REAL(ZC*100.0D0)` (35) `        CALL VF_CND2(R4TN,R4Z,R4U,R4W,R4P)` (36) `        WVUN=DBLE(R4U)*0.01D0` (37) `        WVUT=DBLE(R4W)*0.01D0` (38) `      ELSEIF (IWVTYP.GE. 1) THEN` (39) `        R4Z=REAL(ZC)` (40) `        CALL vf_sfmb2(R4TN,R4Z,R4U,R4W,R4UT,R4WT,R4P)` (41) `        WVUN=DBLE(R4U)` (42) `        WVUT=DBLE(R4W)` (43) `      ELSE` (44) `        CALL VF_A2ERR('VF_CWMAK2','P.G ERROR.')` (45) `      ENDIF` (46) `C     -- 実行文の終了 --` (48) (실행문 종료) `      GOTO 9999` (49) `C==== 終了 ===========================================================` (51) (종료) ` 9999 CONTINUE` (53) `      RETURN` (54) `      END` (55) [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 23·31·36·41: R4P·R4UT·R4WT를 호출 인수로 받지만 WVUN·WVUT 계산에는 사용하지 않는다.
