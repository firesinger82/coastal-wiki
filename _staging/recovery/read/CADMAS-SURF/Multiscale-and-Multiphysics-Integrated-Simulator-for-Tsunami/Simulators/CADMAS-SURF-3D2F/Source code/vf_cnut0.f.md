---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D2F/Source code/vf_cnut0.f
lines: 62
sha256: 92d8c531e264a45ed582544035b3c903f1786da92b194304f37f27d302b16c64
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# vf_cnut0.f — 판독 구간 기록

구간은 1행부터 62행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–30 | k-ε 2방정식 모델의 와동점성계수 계산 루틴과 선언이다(1–25). LEQK=0이면 VF_A2ERR를 호출한다(29).<br>`      SUBROUTINE VF_CNUT0(AK,AE,ANUT,NF)` (1).<br>`CD=== 概要 ===========================================================` (3) (개요).<br>`CDT   VF_CNUT0:渦動粘性係数を計算する(k-ε2方程式モデル)` (5) (VF_CNUT0:와동점성계수 계산(k-ε 2방정식 모델)).<br>`C==== 宣言 ===========================================================` (7) (선언).<br>`C     -- 大域型 --` (9) (전역 형).<br>`      IMPLICIT INTEGER(I-N),DOUBLE PRECISION(A-H,O-Z)` (10).<br>`C     -- 大域変数 --` (12) (전역 변수).<br>`      INCLUDE 'VF_A0PRM.h'` (13).<br>`      INCLUDE 'VF_ANUMBI.h'` (14).<br>`      INCLUDE 'VF_APARAI.h'` (15).<br>`      INCLUDE 'VF_APHYSR.h'` (16).<br>`CD    -- 引数 --` (18) (인수).<br>`CD    AK(@FOR-3D@)   : IN  : R*8 : 乱流エネルギ` (19) (AK(@FOR-3D@)   : IN  : R*8 : 난류 에너지(turbulent kinetic energy)).<br>`CD    AE(@FOR-3D@)   : IN  : R*8 : 乱流エネルギ散逸` (20) (AE(@FOR-3D@)   : IN  : R*8 : 난류 에너지 소산(turbulent dissipation)).<br>`CD    ANUT(@FOR-3D@) : I/O : R*8 : 渦動粘性係数νt` (21) (ANUT(@FOR-3D@) : I/O : R*8 : 와동점성계수 νt).<br>`CD    NF(@FOR-3D@)   : IN  : I*4 : セルの状態を示すインデックス` (22) (NF(@FOR-3D@)   : IN  : I*4 : 셀 상태를 나타내는 인덱스).<br>`      DIMENSION AK  (NUMI,NUMJ,NUMK),AE(NUMI,NUMJ,NUMK)` (23).<br>`      DIMENSION ANUT(NUMI,NUMJ,NUMK)` (24).<br>`      DIMENSION NF  (NUMI,NUMJ,NUMK)` (25).<br>`C==== 実行 ===========================================================` (27) (실행).<br>`      IF (LEQK.EQ.0) CALL VF_A2ERR('VF_CNUT0','P.G ERROR.')` (29). |
| 31–40 | 시작 시 1행 SUBROUTINE VF_CNUT0 루틴 안. 병렬 플래그에 따라 I/J 범위를 설정한다(32–39).<br>`CD    -- 並列時の範囲変更 --` (31) (병렬 실행 시 범위 변경).<br>`      IA=1` (32).<br>`      IB=NUMI` (33).<br>`      JA=1` (34).<br>`      JB=NUMJ` (35).<br>`      IF (MYMIS.EQ.1) IA=2` (36).<br>`      IF (MYMIE.EQ.1) IB=NUMI-1` (37).<br>`      IF (MYMJS.EQ.1) JA=2` (38).<br>`      IF (MYMJE.EQ.1) JB=NUMJ-1` (39). |
| 41–62 | 시작 시 1행 SUBROUTINE VF_CNUT0 루틴 안. 유효 셀은 AE와 AKMINE 중 큰 값을 분모로 사용하여 AKCMU·AK²/분모를 계산한다(45–47). 장애물 셀의 ANUT는 0이다(48–49).<br>`CD    -- 渦動粘性係数νt=Cμ・k2/εを計算 --` (41) (와동점성계수 νt=Cμ·k2/ε 계산).<br>`      DO 120 K=2,NUMK-1` (42).<br>`        DO 110 J=JA,JB` (43).<br>`          DO 100 I=IA,IB` (44).<br>`            IF (NF(I,J,K).GT.-1) THEN` (45).<br>`              W=MAX(AE(I,J,K),AKMINE)` (46).<br>`              ANUT(I,J,K)=AKCMU*AK(I,J,K)*AK(I,J,K)/W` (47).<br>`            ELSE` (48).<br>`              ANUT(I,J,K)=0.0D0` (49).<br>`            ENDIF` (50).<br>` 100      CONTINUE` (51).<br>` 110    CONTINUE` (52).<br>` 120  CONTINUE` (53).<br>`C     -- 実行文の終了 --` (55) (실행문 종료).<br>`      GOTO 9999` (56).<br>`C==== 終了 ===========================================================` (58) (종료).<br>` 9999 CONTINUE` (60).<br>`      RETURN` (61).<br>`      END` (62). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
