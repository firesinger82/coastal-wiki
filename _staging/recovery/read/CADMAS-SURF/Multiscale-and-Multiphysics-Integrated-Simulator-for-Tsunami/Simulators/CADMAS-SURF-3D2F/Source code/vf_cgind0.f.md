---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D2F/Source code/vf_cgind0.f
lines: 59
sha256: dc0e07d0ef23516b75a1462ecadc5d7e976bf9e8bf87164c0992a356759e76ea
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# vf_cgind0.f — 판독 구간 기록

구간은 1행부터 59행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–32 | 공극률(porosity) 수정 이전의 면·경계 인덱스 저장 루틴과 배열 선언이다(1–30).<br>`      SUBROUTINE VF_CGIND0(INDX,INDY,INDZ,INDB,INDX0,INDY0,INDZ0,INDB0)` (1).<br>`CD=== 概要 ===========================================================` (3) (개요).<br>`CDT   VF_CGIND0:空隙率を基に修正する前の面状態インデックスを保存する` (5) (VF_CGIND0:공극률(porosity)로 수정하기 전의 면 상태 인덱스를 저장한다).<br>`C==== 宣言 ===========================================================` (7) (선언).<br>`C     -- 大域型 --` (9) (전역 형).<br>`      IMPLICIT INTEGER(I-N),DOUBLE PRECISION(A-H,O-Z)` (10).<br>`C     -- 大域変数 --` (12) (전역 변수).<br>`      INCLUDE 'VF_A0PRM.h'` (13).<br>`      INCLUDE 'VF_ANUMBI.h'` (14).<br>`      INCLUDE 'VF_APARAI.h'` (15).<br>`      INCLUDE 'VF_AFILEI.h'` (16).<br>`CD    -- 引数 --` (18) (인수).<br>`CD    INDX(@FOR-3D@)    : IN  : I*4 : x面の状態を示すインデックス` (19) (INDX(@FOR-3D@)    : IN  : I*4 : x면 상태 인덱스).<br>`CD    INDY(@FOR-3D@)    : IN  : I*4 : y面の状態を示すインデックス` (20) (INDY(@FOR-3D@)    : IN  : I*4 : y면 상태 인덱스).<br>`CD    INDZ(@FOR-3D@)    : IN  : I*4 : z面の状態を示すインデックス` (21) (INDZ(@FOR-3D@)    : IN  : I*4 : z면 상태 인덱스).<br>`CD    INDB(MAXB1,NUMB)  : IN  : I*4 : 境界面のインデックス` (22) (INDB(MAXB1,NUMB)  : IN  : I*4 : 경계면 인덱스).<br>`CD    INDX0(@FOR-3D@)   : OUT : I*4 : x面の状態を示すインデックス(修正前)` (23) (INDX0(@FOR-3D@)   : OUT : I*4 : x면 상태 인덱스(수정 전)).<br>`CD    INDY0(@FOR-3D@)   : OUT : I*4 : y面の状態を示すインデックス(修正前)` (24) (INDY0(@FOR-3D@)   : OUT : I*4 : y면 상태 인덱스(수정 전)).<br>`CD    INDZ0(@FOR-3D@)   : OUT : I*4 : z面の状態を示すインデックス(修正前)` (25) (INDZ0(@FOR-3D@)   : OUT : I*4 : z면 상태 인덱스(수정 전)).<br>`CD    INDB0(MAXB1,NUMB0): OUT : I*4 : 境界面のインデックス(修正前)` (26) (INDB0(MAXB1,NUMB0): OUT : I*4 : 경계면 인덱스(수정 전)).<br>`      DIMENSION INDX (NUMI,NUMJ,NUMK),INDY (NUMI,NUMJ,NUMK)` (27).<br>`      DIMENSION INDZ (NUMI,NUMJ,NUMK),INDB (MAXB1,NUMB)` (28).<br>`      DIMENSION INDX0(NUMI,NUMJ,NUMK),INDY0(NUMI,NUMJ,NUMK)` (29).<br>`      DIMENSION INDZ0(NUMI,NUMJ,NUMK),INDB0(MAXB1,NUMB0)` (30).<br>`C==== 実行 ===========================================================` (32) (실행). |
| 33–44 | 시작 시 1행 SUBROUTINE VF_CGIND0 루틴 안. 전체 격자의 INDX/INDY/INDZ를 각 보존 배열로 복사한다(35–43).<br>`CD    -- 修正する前の面の状態を示すインデクスを保存 --` (34) (수정 전 면 상태 인덱스를 저장).<br>`      DO 120 K=1,NUMK` (35).<br>`        DO 110 J=1,NUMJ` (36).<br>`          DO 100 I=1,NUMI` (37).<br>`            INDX0(I,J,K)=INDX(I,J,K)` (38).<br>`            INDY0(I,J,K)=INDY(I,J,K)` (39).<br>`            INDZ0(I,J,K)=INDZ(I,J,K)` (40).<br>` 100      CONTINUE` (41).<br>` 110    CONTINUE` (42).<br>` 120  CONTINUE` (43). |
| 45–59 | 시작 시 1행 SUBROUTINE VF_CGIND0 루틴 안. 기존 경계 NUMB0개에 대해 MAXB1개 필드를 복사하고 반환한다(46–59).<br>`CD    -- 修正する前の境界面のインデックスを保存 --` (45) (수정 전 경계면 인덱스를 저장).<br>`      DO 210 IB=1,NUMB0` (46).<br>`        DO 200 I=1,MAXB1` (47).<br>`          INDB0(I,IB)=INDB(I,IB)` (48).<br>` 200    CONTINUE` (49).<br>` 210  CONTINUE` (50).<br>`C     -- 実行文の終了 --` (52) (실행문 종료).<br>`      GOTO 9999` (53).<br>`C==== 終了 ===========================================================` (55) (종료).<br>` 9999 CONTINUE` (57).<br>`      RETURN` (58).<br>`      END` (59). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
