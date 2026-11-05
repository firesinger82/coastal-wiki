---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Source code/vf_cwmak0.f
lines: 71
sha256: 0af042c1352783b1abbc5f2c375e3514a0efe5f43e21668729ec8c745a85c7e8
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# vf_cwmak0.f — 판독 구간 기록

구간은 1행부터 71행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–27 | 조파(wave generation) 함수의 초기화 루틴이다. 인수와 REAL*4 작업 배열을 선언한다. 원문: `      SUBROUTINE VF_CWMAK0(WVDPTH,WVPERI,WVHEIG,WVLENG,IWVTYP)` (1) `CD=== 概要 ===========================================================` (3) (개요) `CDT   VF_CWMAK0:造波のための関数の初期化` (5) (조파용 함수 초기화) `C==== 宣言 ===========================================================` (7) (선언) `C     -- 大域型 --` (9) (전역 자료형) `      IMPLICIT INTEGER(I-N),DOUBLE PRECISION(A-H,O-Z)` (10) `CD    -- 引数 --` (12) (인수) `CD    WVDPTH : IN  : R*8 : 水深` (13) (수심) `CD    WVPERI : IN  : R*8 : 周期` (14) (주기) `CD    WVHEIG : IN  : R*8 : 波高` (15) (파고) `CD    WVLENG : OUT : R*8 : 波長` (16) (파장) `CD    IWVTYP : IN  : I*4 : 造波波形の種別` (17) (조파(wave generation) 파형 종류) `CD                         =-2:Stokes波(第5次近似解)` (18) (-2: Stokes 파(Stokes wave). 5차 근사해) `CD                         =-1:Cnoidal波(第3次近似解)` (19) (-1: 크노이드파(cnoidal wave). 3차 근사해) `CD                         > 0:流れ関数法Bとその次数` (20) (양수: 흐름함수법 B(stream function method B)와 그 차수) `CD    -- 局所変数 --` (22) (지역 변수) `      REAL*4 R4D,R4T,R4H,R4W1,R4E1,R4K,R4L,R4C,R4CC` (23) `      REAL*4 R4U,R4A(24),R4HH` (24) `C==== 実行 ===========================================================` (26) (실행) |
| 28–71 | 시작 시 1행 VF_CWMAK0 루틴 안이며 조건·루프 밖. -2는 VF_STK0를 N=5로, -1은 VF_CND0를 N=3으로 호출한다. 두 분기는 길이를 100배 변환하고 파장을 0.01배로 복구한다. 양수는 vf_sfmb02C를 IWVTYP 차수로 호출하고 ICN을 검사한다. -3과 -4는 파장 0을 반환한다. 나머지는 `CALL VF_A2ERR('VF_CWMAK0','P.G ERROR.')`를 실행한다. 원문: `CD    -- 初期化ルーチンを呼び出す --` (28) (초기화 루틴 호출) `      IF     (IWVTYP.EQ.-2) THEN` (29) `        R4D=REAL(WVDPTH*100.0D0)` (30) `        R4T=REAL(WVPERI)` (31) `        R4H=REAL(WVHEIG*100.0D0)` (32) `        N=5` (33) `        CALL VF_STK0(N,R4D,R4T,R4H,R4W1,R4E1,R4K,R4L,R4C,R4CC)` (34) `        WVLENG=DBLE(R4L)*0.01D0` (35) `      ELSEIF (IWVTYP.EQ.-1) THEN` (36) `        R4D=REAL(WVDPTH*100.0D0)` (37) `        R4T=REAL(WVPERI)` (38) `        R4H=REAL(WVHEIG*100.0D0)` (39) `        N=3` (40) `        CALL VF_CND0(N,R4D,R4T,R4H,R4W1,R4E1,R4K,R4L,R4C,R4CC)` (41) `        WVLENG=DBLE(R4L)*0.01D0` (42) `      ELSEIF (IWVTYP.GE. 1) THEN` (43) `        R4D=REAL(WVDPTH)` (44) `        R4T=REAL(WVPERI)` (45) `        R4H=REAL(WVHEIG)` (46) `        R4U=0.0` (47) `        N  =IWVTYP` (48) `        ICN=0` (49) `        MSG=0` (50) 연속문: `        CALL vf_sfmb02C(N,R4D,R4T,R4H,R4U,R4A,` (51); `     &                  R4L,R4K,R4HH,ICN,R4E1,MSG)` (52) `        WVLENG=DBLE(R4L)` (53) 연속문: `        IF (ICN.NE.0)` (54); `     &      CALL VF_A2ERR('VF_CSETUP','(VF_SFMB02C) NOT CONVERGED.')` (55) `      ELSEIF (IWVTYP.EQ.-3) THEN` (56) `        WVLENG=0.0D0` (57) `      ELSEIF (IWVTYP.EQ.-4) THEN` (58) `        WVLENG=0.0D0` (59) `      ELSE` (60) `        CALL VF_A2ERR('VF_CWMAK0','P.G ERROR.')` (61) `      ENDIF` (62) `C     -- 実行文の終了 --` (64) (실행문 종료) `      GOTO 9999` (65) `C==== 終了 ===========================================================` (67) (종료) ` 9999 CONTINUE` (69) `      RETURN` (70) `      END` (71) [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 54–55: 비수렴 오류 호출의 첫 문자열은 'VF_CSETUP'이다.
- 17–20·56–59: 파형 종류 주석에는 -3과 -4가 없지만 실행부에는 두 분기가 있다.
- 24·48·51–52: R4A 배열 크기는 24이다. N에는 IWVTYP를 그대로 넣으며 상한 검사는 없다.
