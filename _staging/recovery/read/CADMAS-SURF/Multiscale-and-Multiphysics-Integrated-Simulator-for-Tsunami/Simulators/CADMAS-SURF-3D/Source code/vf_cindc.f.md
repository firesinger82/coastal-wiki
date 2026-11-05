---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Source code/vf_cindc.f
lines: 62
sha256: b6f64b0281b76abd1d2a6a727fde627cca2184bcebdcdad4054cd165fef2ab2d
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# vf_cindc.f — 판독 구간 기록

구간은 1행부터 62행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–23 | 셀 계산 상태 지표 INDC와 원래 상태 NF를 선언한다. 원문: `      SUBROUTINE VF_CINDC(NF,INDC)` (1). `CD=== 概要 ===========================================================` (3) (개요). `CDT   VF_CINDC:セルの計算状態を示すインデックスINDCを設定する` (5) (VF_CINDC:셀 계산 상태 지표 INDC 설정). `C==== 宣言 ===========================================================` (7) (선언). `C     -- 大域型 --` (9) (전역 형). `      IMPLICIT INTEGER(I-N),DOUBLE PRECISION(A-H,O-Z)` (10). `C     -- 大域変数 --` (12) (전역 변수). `      INCLUDE 'VF_A0PRM.h'` (13). `      INCLUDE 'VF_ANUMBI.h'` (14). `      INCLUDE 'VF_APARAI.h'` (15). `CD    -- 引数 --` (17) (인수). `CD    NF(@FOR-3D@)   : IN  : I*4 : セルの状態を示すインデックス` (18) (NF(@FOR-3D@)   : IN  : I*4 : 셀 상태 지표(index)). `CD    INDC(@FOR-3D@) : I/O : I*4 : セルの計算状態を示すインデックス` (19) (INDC(@FOR-3D@) : I/O : I*4 : 셀 계산 상태 지표). `      DIMENSION NF(NUMI,NUMJ,NUMK),INDC(NUMI,NUMJ,NUMK)` (20). `C==== 実行 ===========================================================` (22) (실행). |
| 24–33 | 시작 시 `      SUBROUTINE VF_CINDC(NF,INDC)` (1) 블록 안. 병렬 영역의 물리 경계에 따라 x,y 순회 범위를 조정한다. 원문: `CD    -- 並列時の範囲変更 --` (24) (병렬 처리 시 범위 변경). `      IA=1` (25). `      IB=NUMI` (26). `      JA=1` (27). `      JB=NUMJ` (28). `      IF (MYMIS.EQ.1) IA=2` (29). `      IF (MYMIE.EQ.1) IB=NUMI-1` (30). `      IF (MYMJS.EQ.1) JA=2` (31). `      IF (MYMJE.EQ.1) JB=NUMJ-1` (32). |
| 34–54 | 시작 시 `      SUBROUTINE VF_CINDC(NF,INDC)` (1) 블록 안. NF=0이면 INDC=0,NF=8 또는 -1이면 INDC=-1,그 외 표면 셀은 INDC=0으로 설정한다. 원문: `CD    -- INDCを設定 --` (34) (INDC 설정). `      DO 120 K=2,NUMK-1` (35). `        DO 110 J=JA,JB` (36). `          DO 100 I=IA,IB` (37). `C           * 流体セルが最も多いと仮定` (38) (* 유체 셀이 가장 많다고 가정). `            IF     (NF(I,J,K).EQ. 0) THEN` (39). `              INDC(I,J,K)=0` (40). `C           * 気体セルが次に多いと仮定` (41) (* 기체 셀이 그다음으로 많다고 가정). `            ELSEIF (NF(I,J,K).EQ. 8) THEN` (42). `              INDC(I,J,K)=-1` (43). `C           * そして、障害物セルならば` (44) (* 그리고 장애물 셀이면). `            ELSEIF (NF(I,J,K).EQ.-1) THEN` (45). `              INDC(I,J,K)=-1` (46). `C           * でなければ、表面セル` (47) (* 그 외에는 표면 셀). `            ELSE` (48). `              INDC(I,J,K)=0` (49). `            ENDIF` (50). ` 100      CONTINUE` (51). ` 110    CONTINUE` (52). ` 120  CONTINUE` (53). |
| 55–62 | 시작 시 `      SUBROUTINE VF_CINDC(NF,INDC)` (1) 블록 안. 공통 종료 경로다. 원문: `C     -- 実行文の終了 --` (55) (실행문 종료). `      GOTO 9999` (56). `C==== 終了 ===========================================================` (58) (종료). ` 9999 CONTINUE` (60). `      RETURN` (61). `      END` (62). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
