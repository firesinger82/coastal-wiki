---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Source code/vf_cwlvl.f
lines: 67
sha256: ef6cdbe077b02187d8ba8cf591e8c51a4af60f3652202b5bf2c407c0aa68aac4
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# vf_cwlvl.f — 판독 구간 기록

구간은 1행부터 67행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–34 | VOF 함수의 z방향 합산으로 초기 수면 기준 수위 변동을 구한다(같은 원문 38–49행). 인수·배열을 선언하고 IIN·JIN을 지역 인덱스로 옮긴다. 원문: `      SUBROUTINE VF_CWLVL(ZZ,FF,VAL,NF,IIN,JIN)` (1) `CD=== 概要 ===========================================================` (3) (개요) `CDT   VF_CWLVL:水位変動を計算する` (5) (수위 변동 계산) `C==== 宣言 ===========================================================` (7) (선언) `C     -- 大域型 --` (9) (전역 자료형) `      IMPLICIT INTEGER(I-N),DOUBLE PRECISION(A-H,O-Z)` (10) `C     -- 大域変数 --` (12) (전역 변수) `      INCLUDE 'VF_A0PRM.h'` (13) `      INCLUDE 'VF_ANUMBI.h'` (14) `      INCLUDE 'VF_APARAI.h'` (15) `      INCLUDE 'VF_APHYSR.h'` (16) `CD    -- 引数 --` (18) (인수) `CD    ZZ(MAXG1,NUMK) : IN  : R*8 : z方向格子座標等` (19) (z방향 격자 좌표 등) `CD    FF(@FOR-3D@)   : IN  : R*8 : VOF関数F` (20) (VOF 함수) `CD    VAL            : OUT : R*8 : 水面の高さ` (21) (수면 높이) `CD    NF(@FOR-3D@)   : IN  : I*4 : セルの状態を示すインデックス` (22) (셀(cell) 상태 인덱스(index)) `CD    IIN            : IN  : I*4 : x方向セル番号` (23) (x방향 셀 번호) `CD    JIN            : IN  : I*4 : y方向セル番号` (24) (y방향 셀 번호) `      DIMENSION ZZ(MAXG1,NUMK)` (25) `      DIMENSION FF(NUMI,NUMJ,NUMK)` (26) `      DIMENSION NF(NUMI,NUMJ,NUMK)` (27) `C==== 実行 ===========================================================` (29) (실행) `CD    -- 並列時のシフト分等 --` (31) (병렬 계산 시 이동량 등) `      IP=IIN-(MYGIS-1)` (32) `      JP=JIN-(MYGJS-1)` (33) [11-04 전수 검증 정정] |
| 35–67 | 시작 시 1행 VF_CWLVL 루틴 안이며 조건·루프 밖. 담당 수평 범위에서 K=2부터 NUMK-1까지 적분한다. `NF(IP,JP,K).EQ.-1`이면 `ZZ(2,K)*1.0D0`을 더한다. 나머지는 `ZZ(2,K)*FF(IP,JP,K)`를 더한다. 해석: ZZ(2,K)를 셀 두께로 읽으면 각각 전체 두께와 FF 비율을 곱한 두께에 해당하지만 이 구간에는 ZZ(2,K)의 정의가 없다. 초기 수면 위치를 빼고 VF_P1SUMD로 집계한다. 원문: 연속문: `      IF (MYIS.LE.IP .AND. IP.LE.MYIE .AND.` (35); `     &    MYJS.LE.JP .AND. JP.LE.MYJE      ) THEN` (36) `CD      -- VOF関数Fをz方向に加える --` (38) (VOF 함수를 z방향으로 합산) `        SF=0.0D0` (39) `        DO 100 K=2,NUMK-1` (40) `          IF (NF(IP,JP,K).EQ.-1) THEN` (41) `            SF=SF+ZZ(2,K)*1.0D0` (42) `          ELSE` (43) `            SF=SF+ZZ(2,K)*FF(IP,JP,K)` (44) `          ENDIF` (45) ` 100    CONTINUE` (46) `CD      -- 初期水面の位置を基準とする --` (48) (초기 수면 위치를 기준으로 함) `        VAL=SF-(WVLVL-ZZ(1,2))` (49) `      ELSE` (51) `        VAL=0.0D0` (53) `      ENDIF` (55) `      W=VAL` (57) `      CALL VF_P1SUMD(W,VAL)` (58) `C     -- 実行文の終了 --` (60) (실행문 종료) `      GOTO 9999` (61) `C==== 終了 ===========================================================` (63) (종료) ` 9999 CONTINUE` (65) `      RETURN` (66) `      END` (67) [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 41–45: NF=-1인 셀은 FF 대신 1.0D0를 사용해 수직 합계에 포함한다.
