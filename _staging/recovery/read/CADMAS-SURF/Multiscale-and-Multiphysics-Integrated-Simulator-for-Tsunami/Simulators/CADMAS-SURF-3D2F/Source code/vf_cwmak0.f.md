---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D2F/Source code/vf_cwmak0.f
lines: 69
sha256: 127324b53250b2012a0979f7858e4583452a25e3bc00688956ea87aa27cb9bf4
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# vf_cwmak0.f — 판독 구간 기록

구간은 1행부터 69행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–27 | 조파(wave generation) 함수 초기화 루틴이다. 파형 번호와 단정밀도(single precision) 작업 변수 및 R4A(24)를 선언한다(13–24).<br>`      SUBROUTINE VF_CWMAK0(WVDPTH,WVPERI,WVHEIG,WVLENG,IWVTYP)` (1).<br>`CD=== 概要 ===========================================================` (3) (개요).<br>`CDT   VF_CWMAK0:造波のための関数の初期化` (5) (VF_CWMAK0:조파(wave generation)를 위한 함수 초기화).<br>`C==== 宣言 ===========================================================` (7) (선언).<br>`C     -- 大域型 --` (9) (전역 형).<br>`      IMPLICIT INTEGER(I-N),DOUBLE PRECISION(A-H,O-Z)` (10).<br>`CD    -- 引数 --` (12) (인수).<br>`CD    WVDPTH : IN  : R*8 : 水深` (13) (WVDPTH : IN  : R*8 : 수심).<br>`CD    WVPERI : IN  : R*8 : 周期` (14) (WVPERI : IN  : R*8 : 주기).<br>`CD    WVHEIG : IN  : R*8 : 波高` (15) (WVHEIG : IN  : R*8 : 파고).<br>`CD    WVLENG : OUT : R*8 : 波長` (16) (WVLENG : OUT : R*8 : 파장).<br>`CD    IWVTYP : IN  : I*4 : 造波波形の種別` (17) (IWVTYP : IN  : I*4 : 조파 파형 종류).<br>`CD                         =-2:Stokes波(第5次近似解)` (18) (-2:Stokes 파(Stokes wave)(5차 근사해)).<br>`CD                         =-1:Cnoidal波(第3次近似解)` (19) (-1:크노이드파(cnoidal wave)(3차 근사해)).<br>`CD                         > 0:流れ関数法Bとその次数` (20) (> 0:흐름함수법 B(stream function method B) 및 차수).<br>`CD    -- 局所変数 --` (22) (지역 변수).<br>`      REAL*4 R4D,R4T,R4H,R4W1,R4E1,R4K,R4L,R4C,R4CC` (23).<br>`      REAL*4 R4U,R4A(24),R4HH` (24).<br>`C==== 実行 ===========================================================` (26) (실행). [11-04 전수 검증 정정] |
| 28–42 | 시작 시 1행 SUBROUTINE VF_CWMAK0 루틴 안. IWVTYP=-2는 길이를 100배 변환하고 5차 VF_STK0를 호출한다(29–35). -1은 같은 변환으로 3차 VF_CND0를 호출한다(36–42). 파장은 0.01배로 복원한다(35·42).<br>`CD    -- 初期化ルーチンを呼び出す --` (28) (초기화 루틴 호출).<br>`      IF     (IWVTYP.EQ.-2) THEN` (29).<br>`        R4D=REAL(WVDPTH*100.0D0)` (30).<br>`        R4T=REAL(WVPERI)` (31).<br>`        R4H=REAL(WVHEIG*100.0D0)` (32).<br>`        N=5` (33).<br>`        CALL VF_STK0(N,R4D,R4T,R4H,R4W1,R4E1,R4K,R4L,R4C,R4CC)` (34).<br>`        WVLENG=DBLE(R4L)*0.01D0` (35).<br>`      ELSEIF (IWVTYP.EQ.-1) THEN` (36).<br>`        R4D=REAL(WVDPTH*100.0D0)` (37).<br>`        R4T=REAL(WVPERI)` (38).<br>`        R4H=REAL(WVHEIG*100.0D0)` (39).<br>`        N=3` (40).<br>`        CALL VF_CND0(N,R4D,R4T,R4H,R4W1,R4E1,R4K,R4L,R4C,R4CC)` (41).<br>`        WVLENG=DBLE(R4L)*0.01D0` (42). |
| 43–69 | 시작 시 29행 `IF     (IWVTYP.EQ.-2) THEN`으로 시작한 분기 사슬의 다음 ELSEIF 경계이다. 직전 분기는 36행 `ELSEIF (IWVTYP.EQ.-1) THEN`이다. 43행 `ELSEIF (IWVTYP.GE. 1) THEN`으로 분기가 바뀐다. 전체 IF는 60행에서 닫힌다. IWVTYP>=1이면 흐름함수법(stream function method) vf_sfmb02C를 호출하고 수렴 코드를 검사한다(43–55). -3은 파장 0, 나머지는 오류이다(56–60).<br>`      ELSEIF (IWVTYP.GE. 1) THEN` (43).<br>`        R4D=REAL(WVDPTH)` (44).<br>`        R4T=REAL(WVPERI)` (45).<br>`        R4H=REAL(WVHEIG)` (46).<br>`        R4U=0.0` (47).<br>`        N  =IWVTYP` (48).<br>`        ICN=0` (49).<br>`        MSG=0` (50).<br>연속행 문장: `        CALL vf_sfmb02C(N,R4D,R4T,R4H,R4U,R4A,` (51); `     &                  R4L,R4K,R4HH,ICN,R4E1,MSG)` (52).<br>`        WVLENG=DBLE(R4L)` (53).<br>연속행 문장: `        IF (ICN.NE.0)` (54); `     &      CALL VF_A2ERR('VF_CSETUP','(VF_SFMB02C) NOT CONVERGED.')` (55).<br>`      ELSEIF (IWVTYP.EQ.-3) THEN` (56).<br>`        WVLENG=0.0D0` (57).<br>`      ELSE` (58).<br>`        CALL VF_A2ERR('VF_CWMAK0','P.G ERROR.')` (59).<br>`      ENDIF` (60).<br>`C     -- 実行文の終了 --` (62) (실행문 종료).<br>`      GOTO 9999` (63).<br>`C==== 終了 ===========================================================` (65) (종료).<br>` 9999 CONTINUE` (67).<br>`      RETURN` (68).<br>`      END` (69).<br>`ICN.NE.0`이면 55행에서 VF_A2ERR에 `'VF_CSETUP'`과 `'(VF_SFMB02C) NOT CONVERGED.'`를 전달한다. 58행 ELSE에서는 59행 `CALL VF_A2ERR('VF_CWMAK0','P.G ERROR.')`를 실행한다. 63행 GOTO의 대상은 67행이다. [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 24·48·51–52: R4A의 길이는 24이다. IWVTYP는 N에 복사되지만 이 루틴에는 N과 24를 대조하는 검사가 없다.
- 54–55: 비수렴 오류 호출의 루틴명 문자열은 VF_CSETUP이다. 이 서브루틴 이름은 VF_CWMAK0이다(1).
