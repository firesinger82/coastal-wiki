---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D2F/Source code/vf_cnu00.f
lines: 77
sha256: a55017e160f8a3f3608e170a20559887911667b4a761d4edb6c2e25fcbf2d67c
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# vf_cnu00.f — 판독 구간 기록

구간은 1행부터 77행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–28 | 분자 동점성과 와동점성의 합 계산 루틴 및 VOF 함수 인수 선언이다(1–25).<br>`      SUBROUTINE VF_CNU00(ANUT,ANU,NF,FF)` (1).<br>`CD=== 概要 ===========================================================` (3) (개요).<br>`CDT   VF_CNUT0:分子動粘性係数と渦動粘性係数の和を計算する` (5) (VF_CNUT0:분자 동점성계수와 와동점성계수 합 계산).<br>`C==== 宣言 ===========================================================` (7) (선언).<br>`C     -- 大域型 --` (9) (전역 형).<br>`      IMPLICIT INTEGER(I-N),DOUBLE PRECISION(A-H,O-Z)` (10).<br>`C     -- 大域変数 --` (12) (전역 변수).<br>`      INCLUDE 'VF_A0PRM.h'` (13).<br>`      INCLUDE 'VF_ANUMBI.h'` (14).<br>`      INCLUDE 'VF_APARAI.h'` (15).<br>`      INCLUDE 'VF_APHYSR.h'` (16).<br>`CD    -- 引数 --` (18) (인수).<br>`CD    ANUT(@FOR-3D@) : IN  : R*8 : 渦動粘性係数νt` (19) (ANUT(@FOR-3D@) : IN  : R*8 : 와동점성계수 νt).<br>`CD    ANU(@FOR-3D@)  : I/O : R*8 : 分子動粘性係数と渦動粘性係数の和` (20) (ANU(@FOR-3D@)  : I/O : R*8 : 분자 동점성계수와 와동점성계수의 합).<br>`CD    NF(@FOR-3D@)   : IN  : I*4 : セルの状態を示すインデックス` (21) (NF(@FOR-3D@)   : IN  : I*4 : 셀 상태를 나타내는 인덱스).<br>`CD    FF(@FOR-3D@)   : IN  : R*8 : VOF関数F` (22) (FF(@FOR-3D@)   : IN  : R*8 : VOF 함수).<br>`      DIMENSION ANUT(NUMI,NUMJ,NUMK),ANU(NUMI,NUMJ,NUMK)` (23).<br>`      DIMENSION NF  (NUMI,NUMJ,NUMK)` (24).<br>`      DIMENSION FF  (NUMI,NUMJ,NUMK)` (25).<br>`C==== 実行 ===========================================================` (27) (실행). |
| 29–53 | 시작 시 1행 SUBROUTINE VF_CNU00 루틴 안. 난류 비사용 경로에서 유효 셀의 두 상 분자 점성을 VOF 함수로 혼합하고 장애물 셀은 0으로 설정한다(40–52).<br>`CD    -- 並列時の範囲変更 --` (29) (병렬 실행 시 범위 변경).<br>`      IA=1` (30).<br>`      IB=NUMI` (31).<br>`      JA=1` (32).<br>`      JB=NUMJ` (33).<br>`      IF (MYMIS.EQ.1) IA=2` (34).<br>`      IF (MYMIE.EQ.1) IB=NUMI-1` (35).<br>`      IF (MYMJS.EQ.1) JA=2` (36).<br>`      IF (MYMJE.EQ.1) JB=NUMJ-1` (37).<br>`CD    -- 乱流モデルを使用しない場合 --` (39) (난류모델을 사용하지 않는 경우).<br>`      IF (LEQK.EQ.0) THEN` (40).<br>`        DO 120 K=2,NUMK-1` (41).<br>`          DO 110 J=JA,JB` (42).<br>`            DO 100 I=IA,IB` (43).<br>`              IF (NF(I,J,K).GT.-1) THEN` (44).<br>`                ANU2=FF(I,J,K)*ANU0(1)+(1.D0-FF(I,J,K))*ANU0(2)` (45).<br>`              ELSE` (46).<br>`                ANU2=0.0D0` (47).<br>`              ENDIF` (48).<br>`              ANU(I,J,K)=ANU2` (49).<br>` 100        CONTINUE` (50).<br>` 110      CONTINUE` (51).<br>` 120    CONTINUE` (52). |
| 54–77 | 시작 시 1행 SUBROUTINE VF_CNU00 루틴·40행 조건 안. 난류 사용 경로도 같은 분자 점성 혼합식을 적용한다(59–63). NF 조건 밖에서 ANUT를 더해 ANU에 넣는다(64).<br>`CD    -- 乱流モデルを使用する場合 --` (54) (난류모델을 사용하는 경우).<br>`      ELSE` (55).<br>`        DO 220 K=2,NUMK-1` (56).<br>`          DO 210 J=JA,JB` (57).<br>`            DO 200 I=IA,IB` (58).<br>`              IF (NF(I,J,K).GT.-1) THEN` (59).<br>`                ANU2=FF(I,J,K)*ANU0(1)+(1.D0-FF(I,J,K))*ANU0(2)` (60).<br>`              ELSE` (61).<br>`                ANU2=0.0D0` (62).<br>`              ENDIF` (63).<br>`              ANU(I,J,K)=ANU2+ANUT(I,J,K)` (64).<br>` 200        CONTINUE` (65).<br>` 210      CONTINUE` (66).<br>` 220    CONTINUE` (67).<br>`      ENDIF` (68).<br>`C     -- 実行文の終了 --` (70) (실행문 종료).<br>`      GOTO 9999` (71).<br>`C==== 終了 ===========================================================` (73) (종료).<br>` 9999 CONTINUE` (75).<br>`      RETURN` (76).<br>`      END` (77).<br>바깥 조건은 40행 `IF (LEQK.EQ.0) THEN`이다. 55행 ELSE는 `LEQK.NE.0` 경로이다. 이 IF는 68행에서 닫힌다. [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 1·5: 서브루틴 이름은 VF_CNU00이다. 설명 머리말은 VF_CNUT0라고 적는다.
- 59–64: NF<=-1이면 ANU2=0이다. ANUT를 더하는 ANU 대입은 이 NF 조건 밖에서 실행된다.
