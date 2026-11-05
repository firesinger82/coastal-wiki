---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Source code/vf_clm00.f
lines: 74
sha256: 279040e337185a2d468f96d2f8ef37bca1c2a9e97871382a2c476da1505d460e
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# vf_clm00.f — 판독 구간 기록

구간은 1행부터 74행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–26 | 열전도율(thermal conductivity)과 난류 열전도율 합 계산 루틴의 배열과 헤더를 선언한다. 원문: `      SUBROUTINE VF_CLM00(ANUT,ALM,NF)` (1). `CD=== 概要 ===========================================================` (3) (개요). `CDT   VF_CLM00:熱伝導率と乱流熱伝導率の和を計算する` (5) (VF_CLM00:열전도율과 난류 열전도율의 합 계산). `C==== 宣言 ===========================================================` (7) (선언). `C     -- 大域型 --` (9) (전역 형). `      IMPLICIT INTEGER(I-N),DOUBLE PRECISION(A-H,O-Z)` (10). `C     -- 大域変数 --` (12) (전역 변수). `      INCLUDE 'VF_A0PRM.h'` (13). `      INCLUDE 'VF_ANUMBI.h'` (14). `      INCLUDE 'VF_APARAI.h'` (15). `      INCLUDE 'VF_APHYSR.h'` (16). `CD    -- 引数 --` (18) (인수). `CD    ANUT(@FOR-3D@) : IN  : R*8 : 渦動粘性係数νt` (19) (ANUT(@FOR-3D@) : IN  : R*8 : 와동 점성 계수(eddy viscosity) νt). `CD    ALM(@FOR-3D@)  : I/O : R*8 : 熱伝導率と乱流熱伝導率の和` (20) (ALM(@FOR-3D@)  : I/O : R*8 : 열전도율과 난류 열전도율의 합). `CD    NF(@FOR-3D@)   : IN  : I*4 : セルの状態を示すインデックス` (21) (NF(@FOR-3D@)   : IN  : I*4 : 셀 상태 지표(index)). `      DIMENSION ANUT(NUMI,NUMJ,NUMK),ALM(NUMI,NUMJ,NUMK)` (22). `      DIMENSION NF  (NUMI,NUMJ,NUMK)` (23). `C==== 実行 ===========================================================` (25) (실행). |
| 27–50 | 시작 시 `      SUBROUTINE VF_CLM00(ANUT,ALM,NF)` (1) 블록 안. 병렬 범위를 정한다. 난류 모델을 쓰지 않으면 비장애물 셀의 ALM은 TCN0,장애물은 0이다. NF의 유체·기체·장애물 구분 근거는 vf_cindc.f:38–49의 주석과 조건이다. 원문: `CD    -- 並列時の範囲変更 --` (27) (병렬 처리 시 범위 변경). `      IA=1` (28). `      IB=NUMI` (29). `      JA=1` (30). `      JB=NUMJ` (31). `      IF (MYMIS.EQ.1) IA=2` (32). `      IF (MYMIE.EQ.1) IB=NUMI-1` (33). `      IF (MYMJS.EQ.1) JA=2` (34). `      IF (MYMJE.EQ.1) JB=NUMJ-1` (35). `CD    -- 乱流モデルを使用しない場合 --` (37) (난류 모델(turbulence model)을 사용하지 않을 때). `      IF (LEQK.EQ.0) THEN` (38). `        DO 120 K=2,NUMK-1` (39). `          DO 110 J=JA,JB` (40). `            DO 100 I=IA,IB` (41). `              IF (NF(I,J,K).NE.-1) THEN` (42). `                ALM(I,J,K)=TCN0` (43). `              ELSE` (44). `                ALM(I,J,K)=0.0D0` (45). `              ENDIF` (46). ` 100        CONTINUE` (47). ` 110      CONTINUE` (48). ` 120    CONTINUE` (49). [11-04 전수 검증 보완] |
| 51–74 | 시작 시 `      SUBROUTINE VF_CLM00(ANUT,ALM,NF)` (1), `      IF (LEQK.EQ.0) THEN` (38) 블록 안에서 시작한다. 52행 ELSE는 LEQK가 0이 아닌 분기이다. 38행 IF는 65행 ENDIF에서 닫힌다. 난류 모델을 쓰면 RHO0*TCP0/AKPR을 계산하고 ANUT에 곱한 값을 TCN0에 더한다. 장애물은 0으로 설정하고 반환한다. NF의 유체·기체·장애물 구분 근거는 vf_cindc.f:38–49의 주석과 조건이다. 원문: `CD    -- 乱流モデルを使用する場合 --` (51) (난류 모델(turbulence model)을 사용할 때). `      ELSE` (52). `        W=RHO0*TCP0/AKPR` (53). `        DO 220 K=2,NUMK-1` (54). `          DO 210 J=JA,JB` (55). `            DO 200 I=IA,IB` (56). `              IF (NF(I,J,K).NE.-1) THEN` (57). `                ALM(I,J,K)=TCN0+ANUT(I,J,K)*W` (58). `              ELSE` (59). `                ALM(I,J,K)=0.0D0` (60). `              ENDIF` (61). ` 200        CONTINUE` (62). ` 210      CONTINUE` (63). ` 220    CONTINUE` (64). `      ENDIF` (65). `C     -- 実行文の終了 --` (67) (실행문 종료). `      GOTO 9999` (68). `C==== 終了 ===========================================================` (70) (종료). ` 9999 CONTINUE` (72). `      RETURN` (73). `      END` (74). [11-04 전수 검증 정정] [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 53: AKPR을 분모로 사용하며 이 루틴에는 AKPR=0 검사문이 없다.
