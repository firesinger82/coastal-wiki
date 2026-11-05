---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Source code/vf_bsss.f
lines: 77
sha256: ae1fc2693378f6c36ba367a40a04ba949e463bbd9a6c400281c6c9e21e8b3d3c
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# vf_bsss.f — 판독 구간 기록

구간은 1행부터 77행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–26 | VF_BSSS는 기체 셀 스칼라(scalar)를 0으로 하고 표면 셀 값을 설정한다. IMPLICIT·INCLUDE·SC·DBUF·NF 배열을 선언한다. 원문: `      SUBROUTINE VF_BSSS(SC,DBUF,NF)` (1); `CD=== 概要 ===========================================================` (3) (개요); `CDT   VF_BSSS:気体セルをゼロとし、表面セルのスカラ量を設定する` (5) (기체 셀을 0으로 하고 표면 셀 스칼라 설정); `C==== 宣言 ===========================================================` (7) (선언); `C     -- 大域型 --` (9) (전역 형); `      IMPLICIT INTEGER(I-N),DOUBLE PRECISION(A-H,O-Z)` (10); `C     -- 大域変数 --` (12) (전역 변수); `      INCLUDE 'VF_A0PRM.h'` (13); `      INCLUDE 'VF_ANUMBI.h'` (14); `      INCLUDE 'VF_APARAI.h'` (15); `CD    -- 引数 --` (17) (인수); `CD    SC(@FOR-3D@) : I/O : R*8 : スカラ量` (18) (스칼라); `CD    DBUF(NUMBUF*MAXBUF) : OUT :R*8 : 並列用のバッファ` (19) (병렬용 버퍼); `CD    NF(@FOR-3D@) : IN  : I*4 : セルの状態を示すインデックス` (20) (셀 상태 첨자); `      DIMENSION SC(NUMI,NUMJ,NUMK)` (21); `      DIMENSION DBUF(NUMBUF*MAXBUF)` (22); `      DIMENSION NF(NUMI,NUMJ,NUMK)` (23); `C==== 実行 ===========================================================` (25) (실행). |
| 27–66 | 1행 VF_BSSS 안. 내부 K와 담당 J·I를 순회한다. NF=8은 SC=0, ELSEIF NF.GE.1은 6방향 인접 셀 중 NF=0인 값만 N·S에 누적하고 SC=S/DBLE(N)으로 산술 평균(arithmetic mean)을 설정한다. 모든 인접 조건과 누적식은 아래 원문 그대로이다. 원문: `CD    -- スカラー量を設定する --` (27) (스칼라 설정); `      DO 120 K=2,NUMK-1` (28); `        DO 110 J=MYJS,MYJE` (29); `          DO 100 I=MYIS,MYIE` (30); `CD          * 気体セルはゼロ` (31) (기체 셀은 0); `            IF     (NF(I,J,K).EQ.8) THEN` (32); `              SC(I,J,K)=0.0D0` (33); `CD          * 表面セルは近傍の流体セルの算術平均` (34) (표면 셀은 인근 유체 셀의 산술 평균); `            ELSEIF (NF(I,J,K).GE.1) THEN` (35); `              N=0` (36); `              S=0.0D0` (37); `              IF (NF(I-1,J,K).EQ.0) THEN` (38); `                N=N+1` (39); `                S=S+SC(I-1,J,K)` (40); `              ENDIF` (41); `              IF (NF(I+1,J,K).EQ.0) THEN` (42); `                N=N+1` (43); `                S=S+SC(I+1,J,K)` (44); `              ENDIF` (45); `              IF (NF(I,J-1,K).EQ.0) THEN` (46); `                N=N+1` (47); `                S=S+SC(I,J-1,K)` (48); `              ENDIF` (49); `              IF (NF(I,J+1,K).EQ.0) THEN` (50); `                N=N+1` (51); `                S=S+SC(I,J+1,K)` (52); `              ENDIF` (53); `              IF (NF(I,J,K-1).EQ.0) THEN` (54); `                N=N+1` (55); `                S=S+SC(I,J,K-1)` (56); `              ENDIF` (57); `              IF (NF(I,J,K+1).EQ.0) THEN` (58); `                N=N+1` (59); `                S=S+SC(I,J,K+1)` (60); `              ENDIF` (61); `              SC(I,J,K)=S/DBLE(N)` (62); `            ENDIF` (63); ` 100      CONTINUE` (64); ` 110    CONTINUE` (65); ` 120  CONTINUE` (66). 32–63행의 IF·ELSEIF 사슬에는 ELSE가 없다. NF가 8도 아니고 1 이상도 아니면 이 구간에서 SC를 대입하지 않는다. [11-04 전수 검증 보완] |
| 67–77 | 1행 VF_BSSS 안이며 셀 루프 밖. VF_P3SRD2(SC,DBUF,0) 뒤 RETURN한다. 원문: `      CALL VF_P3SRD2(SC,DBUF,0)` (68); `C     -- 実行文の終了 --` (70) (실행문 종료); `      GOTO 9999` (71); `C==== 終了 ===========================================================` (73) (종료); ` 9999 CONTINUE` (75); `      RETURN` (76); `      END` (77). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 36–62: 이웃 유체 셀 수 N은 0부터 누적한다. SC=S/DBLE(N) 앞에는 N=0 예외 분기가 없다.
- 32·35: NF=8은 첫 IF에서 처리한다. 다음 ELSEIF는 NF.GE.1이며 1–6으로 상한을 제한하지 않는다.
