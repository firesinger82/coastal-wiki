---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Source code/vf_cglv.f
lines: 47
sha256: b19938c94faaab1b71d857dea04f8e575f742f24dc04b9ed750252499eddcd87
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# vf_cglv.f — 판독 구간 기록

구간은 1행부터 47행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–26 | 공극률(porosity)과 관성력 계수(inertia coefficient)로 GLV를 설정하는 루틴과 배열 선언이다. 원문: `      SUBROUTINE VF_CGLV(CM0,GGV,GLV,NF)` (1). `CD=== 概要 ===========================================================` (3) (개요). `CDT   VF_CGLV:時間依存型のGLVを設定する` (5) (VF_CGLV:시간 의존 GLV 설정). `C==== 宣言 ===========================================================` (7) (선언). `C     -- 大域型 --` (9) (전역 형). `      IMPLICIT INTEGER(I-N),DOUBLE PRECISION(A-H,O-Z)` (10). `C     -- 大域変数 --` (12) (전역 변수). `      INCLUDE 'VF_A0PRM.h'` (13). `      INCLUDE 'VF_ANUMBI.h'` (14). `CD    -- 引数 --` (16) (인수). `CD    CM0(@FOR-3D@)  : IN  : R*8 : 慣性力係数` (17) (CM0(@FOR-3D@)  : IN  : R*8 : 관성력 계수(inertia coefficient)). `CD    GGV(@FOR-3D@)  : IN  : R*8 : 空隙率` (18) (GGV(@FOR-3D@)  : IN  : R*8 : 공극률(porosity)). 주석: `CD    GLV(@FOR-3D@)  : OUT : R*8 : =GGV+(1-GGV)*CM` (19). `CD    NF(@FOR-3D@)   : IN  : I*4 : セルの状態を示すインデックス` (20) (NF(@FOR-3D@)   : IN  : I*4 : 셀 상태 지표(index)). `      DIMENSION CM0(NUMI,NUMJ,NUMK),GGV(NUMI,NUMJ,NUMK)` (21). `      DIMENSION GLV(NUMI,NUMJ,NUMK)` (22). `      DIMENSION NF (NUMI,NUMJ,NUMK)` (23). `C==== 実行 ===========================================================` (25) (실행). |
| 27–39 | 시작 시 `      SUBROUTINE VF_CGLV(CM0,GGV,GLV,NF)` (1) 블록 안. 모든 셀을 순회한다. 장애물은 GLV=1,그 외는 GGV+(1-GGV)*CM0를 적용한다. NF의 유체·기체·장애물 구분 근거는 vf_cindc.f:38–49의 주석과 조건이다. 원문: `CD    -- GLVを設定する --` (27) (GLV 설정). `      DO 120 K=1,NUMK` (28). `        DO 110 J=1,NUMJ` (29). `          DO 100 I=1,NUMI` (30). `            IF (NF(I,J,K).EQ.-1) THEN` (31). `              GLV(I,J,K)=1.0D0` (32). `            ELSE` (33). `              GLV(I,J,K)=GGV(I,J,K)+(1.0D0-GGV(I,J,K))*CM0(I,J,K)` (34). `            ENDIF` (35). ` 100      CONTINUE` (36). ` 110    CONTINUE` (37). ` 120  CONTINUE` (38). [11-04 전수 검증 보완] |
| 40–47 | 시작 시 `      SUBROUTINE VF_CGLV(CM0,GGV,GLV,NF)` (1) 블록 안. 공통 종료 경로다. 원문: `C     -- 実行文の終了 --` (40) (실행문 종료). `      GOTO 9999` (41). `C==== 終了 ===========================================================` (43) (종료). ` 9999 CONTINUE` (45). `      RETURN` (46). `      END` (47). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
