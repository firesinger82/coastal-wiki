---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Source code/vf_cnu00.f
lines: 73
sha256: da22e701643526133a6b29b991b71b2b5936028269469d23c50a3fee7107b4d9
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# vf_cnu00.f — 판독 구간 기록

구간은 1행부터 73행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–26 | 분자 동점성 계수(kinematic viscosity)와 와동 점성 계수(eddy viscosity) 합 계산의 인수·배열·헤더를 선언한다. 원문: `      SUBROUTINE VF_CNU00(ANUT,ANU,NF)` (1). `CD=== 概要 ===========================================================` (3) (개요). `CDT   VF_CNUT0:分子動粘性係数と渦動粘性係数の和を計算する` (5) (VF_CNUT0:분자 동점성 계수(kinematic viscosity)와 와동 점성 계수(eddy viscosity)의 합 계산). `C==== 宣言 ===========================================================` (7) (선언). `C     -- 大域型 --` (9) (전역 형). `      IMPLICIT INTEGER(I-N),DOUBLE PRECISION(A-H,O-Z)` (10). `C     -- 大域変数 --` (12) (전역 변수). `      INCLUDE 'VF_A0PRM.h'` (13). `      INCLUDE 'VF_ANUMBI.h'` (14). `      INCLUDE 'VF_APARAI.h'` (15). `      INCLUDE 'VF_APHYSR.h'` (16). `CD    -- 引数 --` (18) (인수). `CD    ANUT(@FOR-3D@) : IN  : R*8 : 渦動粘性係数νt` (19) (ANUT(@FOR-3D@) : IN  : R*8 : 와동 점성 계수(eddy viscosity) νt). `CD    ANU(@FOR-3D@)  : I/O : R*8 : 分子動粘性係数と渦動粘性係数の和` (20) (ANU(@FOR-3D@)  : I/O : R*8 : 분자 동점성 계수(kinematic viscosity)와 와동 점성 계수(eddy viscosity)의 합). `CD    NF(@FOR-3D@)   : IN  : I*4 : セルの状態を示すインデックス` (21) (NF(@FOR-3D@)   : IN  : I*4 : 셀 상태 지표(index)). `      DIMENSION ANUT(NUMI,NUMJ,NUMK),ANU(NUMI,NUMJ,NUMK)` (22). `      DIMENSION NF  (NUMI,NUMJ,NUMK)` (23). `C==== 実行 ===========================================================` (25) (실행). |
| 27–50 | 시작 시 `      SUBROUTINE VF_CNU00(ANUT,ANU,NF)` (1) 블록 안. 병렬 경계 범위를 정한다. LEQK=0이면 비장애물 셀의 ANU=ANU0,장애물은 0으로 설정한다. NF의 유체·기체·장애물 구분 근거는 vf_cindc.f:38–49의 주석과 조건이다. 원문: `CD    -- 並列時の範囲変更 --` (27) (병렬 처리 시 범위 변경). `      IA=1` (28). `      IB=NUMI` (29). `      JA=1` (30). `      JB=NUMJ` (31). `      IF (MYMIS.EQ.1) IA=2` (32). `      IF (MYMIE.EQ.1) IB=NUMI-1` (33). `      IF (MYMJS.EQ.1) JA=2` (34). `      IF (MYMJE.EQ.1) JB=NUMJ-1` (35). `CD    -- 乱流モデルを使用しない場合 --` (37) (난류 모델(turbulence model)을 사용하지 않을 때). `      IF (LEQK.EQ.0) THEN` (38). `        DO 120 K=2,NUMK-1` (39). `          DO 110 J=JA,JB` (40). `            DO 100 I=IA,IB` (41). `              IF (NF(I,J,K).NE.-1) THEN` (42). `                ANU(I,J,K)=ANU0` (43). `              ELSE` (44). `                ANU(I,J,K)=0.0D0` (45). `              ENDIF` (46). ` 100        CONTINUE` (47). ` 110      CONTINUE` (48). ` 120    CONTINUE` (49). [11-04 전수 검증 보완] |
| 51–73 | 시작 시 `      SUBROUTINE VF_CNU00(ANUT,ANU,NF)` (1), `      IF (LEQK.EQ.0) THEN` (38) 블록 안에서 시작한다. 52행 ELSE는 LEQK가 0이 아닌 분기이다. 38행 IF는 64행 ENDIF에서 닫힌다. 난류 모델 사용 시 비장애물 셀의 ANU=ANU0+ANUT,장애물은 0으로 설정한다. 공통 경로로 반환한다. NF의 유체·기체·장애물 구분 근거는 vf_cindc.f:38–49의 주석과 조건이다. 원문: `CD    -- 乱流モデルを使用する場合 --` (51) (난류 모델(turbulence model)을 사용할 때). `      ELSE` (52). `        DO 220 K=2,NUMK-1` (53). `          DO 210 J=JA,JB` (54). `            DO 200 I=IA,IB` (55). `              IF (NF(I,J,K).NE.-1) THEN` (56). `                ANU(I,J,K)=ANU0+ANUT(I,J,K)` (57). `              ELSE` (58). `                ANU(I,J,K)=0.0D0` (59). `              ENDIF` (60). ` 200        CONTINUE` (61). ` 210      CONTINUE` (62). ` 220    CONTINUE` (63). `      ENDIF` (64). `C     -- 実行文の終了 --` (66) (실행문 종료). `      GOTO 9999` (67). `C==== 終了 ===========================================================` (69) (종료). ` 9999 CONTINUE` (71). `      RETURN` (72). `      END` (73). [11-04 전수 검증 정정] [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 1·5: 루틴 선언 이름은 VF_CNU00이며 목적 주석의 이름은 VF_CNUT0이다.
