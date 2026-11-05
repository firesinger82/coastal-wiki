---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Source code/vf_cnut0.f
lines: 62
sha256: a4b277aa9e5c918ca8e6d0d717756a0b586fdd45f12f40a6057263172df627c0
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# vf_cnut0.f — 판독 구간 기록

구간은 1행부터 62행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–28 | k-ε 2방정식 모델(two equation model)의 와동 점성 계수(eddy viscosity) 계산 목적과 AK,AE,ANUT,NF 배열을 선언한다. 원문: `      SUBROUTINE VF_CNUT0(AK,AE,ANUT,NF)` (1). `CD=== 概要 ===========================================================` (3) (개요). `CDT   VF_CNUT0:渦動粘性係数を計算する(k-ε2方程式モデル)` (5) (VF_CNUT0:와동 점성 계수(eddy viscosity) 계산(k-ε 2방정식 모델(two equation model))). `C==== 宣言 ===========================================================` (7) (선언). `C     -- 大域型 --` (9) (전역 형). `      IMPLICIT INTEGER(I-N),DOUBLE PRECISION(A-H,O-Z)` (10). `C     -- 大域変数 --` (12) (전역 변수). `      INCLUDE 'VF_A0PRM.h'` (13). `      INCLUDE 'VF_ANUMBI.h'` (14). `      INCLUDE 'VF_APARAI.h'` (15). `      INCLUDE 'VF_APHYSR.h'` (16). `CD    -- 引数 --` (18) (인수). `CD    AK(@FOR-3D@)   : IN  : R*8 : 乱流エネルギ` (19) (AK(@FOR-3D@)   : IN  : R*8 : 난류 운동 에너지(turbulent kinetic energy)). `CD    AE(@FOR-3D@)   : IN  : R*8 : 乱流エネルギ散逸` (20) (AE(@FOR-3D@)   : IN  : R*8 : 난류 에너지 소산율(turbulent dissipation rate)). `CD    ANUT(@FOR-3D@) : I/O : R*8 : 渦動粘性係数νt` (21) (ANUT(@FOR-3D@) : I/O : R*8 : 와동 점성 계수(eddy viscosity) νt). `CD    NF(@FOR-3D@)   : IN  : I*4 : セルの状態を示すインデックス` (22) (NF(@FOR-3D@)   : IN  : I*4 : 셀 상태 지표(index)). `      DIMENSION AK  (NUMI,NUMJ,NUMK),AE(NUMI,NUMJ,NUMK)` (23). `      DIMENSION ANUT(NUMI,NUMJ,NUMK)` (24). `      DIMENSION NF  (NUMI,NUMJ,NUMK)` (25). `C==== 実行 ===========================================================` (27) (실행). |
| 29–40 | 시작 시 `      SUBROUTINE VF_CNUT0(AK,AE,ANUT,NF)` (1) 블록 안. LEQK=0이면 VF_A2ERR를 호출한다. 병렬 경계에 따라 x,y 계산 범위를 조정한다. 원문: `      IF (LEQK.EQ.0) CALL VF_A2ERR('VF_CNUT0','P.G ERROR.')` (29). `CD    -- 並列時の範囲変更 --` (31) (병렬 처리 시 범위 변경). `      IA=1` (32). `      IB=NUMI` (33). `      JA=1` (34). `      JB=NUMJ` (35). `      IF (MYMIS.EQ.1) IA=2` (36). `      IF (MYMIE.EQ.1) IB=NUMI-1` (37). `      IF (MYMJS.EQ.1) JA=2` (38). `      IF (MYMJE.EQ.1) JB=NUMJ-1` (39). |
| 41–54 | 시작 시 `      SUBROUTINE VF_CNUT0(AK,AE,ANUT,NF)` (1) 블록 안. 비장애물 셀은 소산율과 AKMINE 중 큰 값을 분모로 삼아 AKCMU*AK*AK/W를 계산한다. 장애물은 0으로 한다. NF의 유체·기체·장애물 구분 근거는 vf_cindc.f:38–49의 주석과 조건이다. 원문: `CD    -- 渦動粘性係数νt=Cμ・k2/εを計算 --` (41) (와동 점성 계수(eddy viscosity) νt=Cμ·k2/ε 계산). `      DO 120 K=2,NUMK-1` (42). `        DO 110 J=JA,JB` (43). `          DO 100 I=IA,IB` (44). `            IF (NF(I,J,K).NE.-1) THEN` (45). `              W=MAX(AE(I,J,K),AKMINE)` (46). `              ANUT(I,J,K)=AKCMU*AK(I,J,K)*AK(I,J,K)/W` (47). `            ELSE` (48). `              ANUT(I,J,K)=0.0D0` (49). `            ENDIF` (50). ` 100      CONTINUE` (51). ` 110    CONTINUE` (52). ` 120  CONTINUE` (53). [11-04 전수 검증 보완] |
| 55–62 | 시작 시 `      SUBROUTINE VF_CNUT0(AK,AE,ANUT,NF)` (1) 블록 안. 공통 종료 경로다. 원문: `C     -- 実行文の終了 --` (55) (실행문 종료). `      GOTO 9999` (56). `C==== 終了 ===========================================================` (58) (종료). ` 9999 CONTINUE` (60). `      RETURN` (61). `      END` (62). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 45–47: ANUT 계산 대상은 NF.NE.-1이며,기체 NF=8을 제외하는 별도 조건은 없다.
- 46–47: AE에는 AKMINE 하한을 적용한다. 같은 식에서 AK 자체에 하한을 적용하는 문장은 없다.
