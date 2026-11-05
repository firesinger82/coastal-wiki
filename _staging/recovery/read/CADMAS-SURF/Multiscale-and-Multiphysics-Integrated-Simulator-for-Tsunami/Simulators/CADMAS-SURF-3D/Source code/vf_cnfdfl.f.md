---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Source code/vf_cnfdfl.f
lines: 61
sha256: c5c18586247c7bf9e58b0b342672a90da82e7c7d9faf0628400dc74b76ad35dd
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# vf_cnfdfl.f — 판독 구간 기록

구간은 1행부터 61행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–24 | NF 기본값(default value) 설정 목적과 가상 셀(ghost cell)·내부 셀의 상태 의미를 선언한다. 원문: `      SUBROUTINE VF_CNFDFL(NF)` (1). `CD=== 概要 ===========================================================` (3) (개요). `CDT   VF_CNFDLF:NFへデフォルト値を設定する` (5) (VF_CNFDLF:NF에 기본값(default value) 설정). `CD      (1)仮想セルを障害物セル(-1)とする` (6) ((1)가상 셀(ghost cell)을 장애물 셀(-1)로 설정). `CD      (2)内部セルを流体セル(0)とする` (7) ((2)내부 셀을 유체 셀(0)로 설정). `C==== 宣言 ===========================================================` (9) (선언). `C     -- 大域型 --` (11) (전역 형). `      IMPLICIT INTEGER(I-N),DOUBLE PRECISION(A-H,O-Z)` (12). `C     -- 大域変数 --` (14) (전역 변수). `      INCLUDE 'VF_A0PRM.h'` (15). `      INCLUDE 'VF_ANUMBI.h'` (16). `      INCLUDE 'VF_APARAI.h'` (17). `CD    -- 引数 --` (19) (인수). `CD    NF(@FOR-3D@) : OUT : I*4 : セルの状態を示すインデックス` (20) (NF(@FOR-3D@) : OUT : I*4 : 셀 상태 지표(index)). `      DIMENSION NF(NUMI,NUMJ,NUMK)` (21). `C==== 実行 ===========================================================` (23) (실행). |
| 25–33 | 시작 시 `      SUBROUTINE VF_CNFDFL(NF)` (1) 블록 안. 전체 배열을 순회하여 NF=0 유체 셀로 초기화한다. 원문: `CD    -- 全てを流体セルとする --` (25) (모든 셀을 유체 셀로 설정). `      DO 120 K=1,NUMK` (26). `        DO 110 J=1,NUMJ` (27). `          DO 100 I=1,NUMI` (28). `            NF(I,J,K)=0` (29). ` 100      CONTINUE` (30). ` 110    CONTINUE` (31). ` 120   CONTINUE` (32). |
| 34–53 | 시작 시 `      SUBROUTINE VF_CNFDFL(NF)` (1) 블록 안. z 양 끝을 장애물 -1로 한다. x,y는 해당 병렬 영역이 전역 물리 경계에 닿을 때만 끝 셀을 -1로 설정한다. 원문: `CD    -- 仮想セルを障害物セルとする --` (34) (가상 셀(ghost cell)을 장애물 셀로 설정). `      DO 210 J=1,NUMJ` (35). `        DO 200 I=1,NUMI` (36). `          NF(I,J,1   )=-1` (37). `          NF(I,J,NUMK)=-1` (38). ` 200    CONTINUE` (39). ` 210  CONTINUE` (40). `      DO 310 K=1,NUMK` (41). `        DO 300 I=1,NUMI` (42). `          IF (MYGJS.EQ.1    ) NF(I,1   ,K)=-1` (43). `          IF (MYGJE.EQ.NUMJ0) NF(I,NUMJ,K)=-1` (44). ` 300    CONTINUE` (45). ` 310  CONTINUE` (46). `      DO 410 K=1,NUMK` (47). `        DO 400 J=1,NUMJ` (48). `          IF (MYGIS.EQ.1    ) NF(1   ,J,K)=-1` (49). `          IF (MYGIE.EQ.NUMI0) NF(NUMI,J,K)=-1` (50). ` 400    CONTINUE` (51). ` 410  CONTINUE` (52). |
| 54–61 | 시작 시 `      SUBROUTINE VF_CNFDFL(NF)` (1) 블록 안. 공통 종료 경로다. 원문: `C     -- 実行文の終了 --` (54) (실행문 종료). `      GOTO 9999` (55). `C==== 終了 ===========================================================` (57) (종료). ` 9999 CONTINUE` (59). `      RETURN` (60). `      END` (61). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 1·5: 루틴 선언 이름은 VF_CNFDFL이며 목적 주석의 이름은 VF_CNFDLF이다.
