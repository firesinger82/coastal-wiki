---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D2F/Source code/vf_cglv.f
lines: 49
sha256: a92e7e2718825f6e35e9b10b84818aaede750da92382b2a147df3d07fad2a7af
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# vf_cglv.f — 판독 구간 기록

구간은 1행부터 49행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–26 | 시간 의존 GLV 계산 루틴과 관성력 계수(inertia coefficient), 공극률(porosity), 셀 상태 인수 선언이다(1–24).<br>`      SUBROUTINE VF_CGLV(CM0,GGV,GLV,NF)` (1).<br>`CD=== 概要 ===========================================================` (3) (개요).<br>`CDT   VF_CGLV:時間依存型のGLVを設定する` (5) (VF_CGLV:시간 의존 GLV를 설정한다).<br>`C==== 宣言 ===========================================================` (7) (선언).<br>`C     -- 大域型 --` (9) (전역 형).<br>`      IMPLICIT INTEGER(I-N),DOUBLE PRECISION(A-H,O-Z)` (10).<br>`C     -- 大域変数 --` (12) (전역 변수).<br>`      INCLUDE 'VF_A0PRM.h'` (13).<br>`      INCLUDE 'VF_ANUMBI.h'` (14).<br>`      INCLUDE 'SF_STRUCT.h'` (15).<br>`CD    -- 引数 --` (17) (인수).<br>`CD    CM0(@FOR-3D@)  : IN  : R*8 : 慣性力係数` (18) (CM0(@FOR-3D@)  : IN  : R*8 : 관성력 계수(inertia coefficient)).<br>`CD    GGV(@FOR-3D@)  : IN  : R*8 : 空隙率` (19) (GGV(@FOR-3D@)  : IN  : R*8 : 공극률(porosity)).<br>주석 원문(실행하지 않음): `CD    GLV(@FOR-3D@)  : OUT : R*8 : =GGV+(1-GGV)*CM` (20).<br>`CD    NF(@FOR-3D@)   : IN  : I*4 : セルの状態を示すインデックス` (21) (NF(@FOR-3D@)   : IN  : I*4 : 셀 상태를 나타내는 인덱스).<br>`      DIMENSION CM0(NUMI,NUMJ,NUMK),GGV(NUMI,NUMJ,NUMK)` (22).<br>`      DIMENSION GLV(NUMI,NUMJ,NUMK)` (23).<br>`      DIMENSION NF (NUMI,NUMJ,NUMK)` (24).<br>`C==== 実行 ===========================================================` (26) (실행). |
| 27–49 | 시작 시 1행 SUBROUTINE VF_CGLV 루틴 안. 전체 격자를 순회한다(29–31). `NF(I,J,K).LE.-1 .AND. ICPL.EQ.0 .AND. ISTM.EQ.0`이면 GLV=1이다(33–34). 그 밖에는 공극률과 관성력 계수를 결합한다(35–37).<br>`CD    -- GLVを設定する --` (28) (GLV 설정).<br>`      DO 120 K=1,NUMK` (29).<br>`        DO 110 J=1,NUMJ` (30).<br>`          DO 100 I=1,NUMI` (31).<br>주석 원문(실행하지 않음): `CSTR        IF (NF(I,J,K).LE.-1) THEN` (32).<br>`            IF (NF(I,J,K).LE.-1 .AND. ICPL.EQ.0 .AND. ISTM.EQ.0) THEN` (33).<br>`              GLV(I,J,K)=1.0D0` (34).<br>`            ELSE` (35).<br>`              GLV(I,J,K)=GGV(I,J,K)+(1.0D0-GGV(I,J,K))*CM0(I,J,K)` (36).<br>`            ENDIF` (37).<br>` 100      CONTINUE` (38).<br>` 110    CONTINUE` (39).<br>` 120  CONTINUE` (40).<br>`C     -- 実行文の終了 --` (42) (실행문 종료).<br>`      GOTO 9999` (43).<br>`C==== 終了 ===========================================================` (45) (종료).<br>` 9999 CONTINUE` (47).<br>`      RETURN` (48).<br>`      END` (49). [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 32–36: NF만 검사하는 조건은 CSTR 주석이다. 실행 조건은 NF<=-1과 ICPL=0 및 ISTM=0을 함께 요구한다.
