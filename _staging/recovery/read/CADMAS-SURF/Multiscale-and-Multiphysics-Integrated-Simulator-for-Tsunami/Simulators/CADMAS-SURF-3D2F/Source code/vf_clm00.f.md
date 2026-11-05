---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D2F/Source code/vf_clm00.f
lines: 78
sha256: baefa98d47a0f9313a26562d880cb2f93a6aac8121b4a999147e9530a69e41e0
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# vf_clm00.f — 판독 구간 기록

구간은 1행부터 78행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–28 | 열전도율 합 계산 루틴과 VOF 함수·난류 점성 인수 선언이다(1–25).<br>`      SUBROUTINE VF_CLM00(ANUT,ALM,NF,FF)` (1).<br>`CD=== 概要 ===========================================================` (3) (개요).<br>`CDT   VF_CLM00:熱伝導率と乱流熱伝導率の和を計算する` (5) (VF_CLM00:열전도율과 난류 열전도율의 합을 계산한다).<br>`C==== 宣言 ===========================================================` (7) (선언).<br>`C     -- 大域型 --` (9) (전역 형).<br>`      IMPLICIT INTEGER(I-N),DOUBLE PRECISION(A-H,O-Z)` (10).<br>`C     -- 大域変数 --` (12) (전역 변수).<br>`      INCLUDE 'VF_A0PRM.h'` (13).<br>`      INCLUDE 'VF_ANUMBI.h'` (14).<br>`      INCLUDE 'VF_APARAI.h'` (15).<br>`      INCLUDE 'VF_APHYSR.h'` (16).<br>`CD    -- 引数 --` (18) (인수).<br>`CD    ANUT(@FOR-3D@) : IN  : R*8 : 渦動粘性係数νt` (19) (ANUT(@FOR-3D@) : IN  : R*8 : 와동점성계수 νt).<br>`CD    ALM(@FOR-3D@)  : I/O : R*8 : 熱伝導率と乱流熱伝導率の和` (20) (ALM(@FOR-3D@)  : I/O : R*8 : 열전도율과 난류 열전도율의 합).<br>`CD    NF(@FOR-3D@)   : IN  : I*4 : セルの状態を示すインデックス` (21) (NF(@FOR-3D@)   : IN  : I*4 : 셀 상태를 나타내는 인덱스).<br>`CD    FF(@FOR-3D@)   : IN  : R*8 : VOF関数F` (22) (FF(@FOR-3D@)   : IN  : R*8 : VOF 함수).<br>`      DIMENSION ANUT(NUMI,NUMJ,NUMK),ALM(NUMI,NUMJ,NUMK)` (23).<br>`      DIMENSION FF  (NUMI,NUMJ,NUMK)` (24).<br>`      DIMENSION NF  (NUMI,NUMJ,NUMK)` (25).<br>`C==== 実行 ===========================================================` (27) (실행). |
| 29–52 | 시작 시 1행 SUBROUTINE VF_CLM00 루틴 안. 병렬 범위를 조정하고 난류모델을 사용하지 않으면 유효 셀 ALM에 TCN0를 설정한다(30–51).<br>`CD    -- 並列時の範囲変更 --` (29) (병렬 실행 시 범위 변경).<br>`      IA=1` (30).<br>`      IB=NUMI` (31).<br>`      JA=1` (32).<br>`      JB=NUMJ` (33).<br>`      IF (MYMIS.EQ.1) IA=2` (34).<br>`      IF (MYMIE.EQ.1) IB=NUMI-1` (35).<br>`      IF (MYMJS.EQ.1) JA=2` (36).<br>`      IF (MYMJE.EQ.1) JB=NUMJ-1` (37).<br>`CD    -- 乱流モデルを使用しない場合 --` (39) (난류모델을 사용하지 않는 경우).<br>`      IF (LEQK.EQ.0) THEN` (40).<br>`        DO 120 K=2,NUMK-1` (41).<br>`          DO 110 J=JA,JB` (42).<br>`            DO 100 I=IA,IB` (43).<br>`              IF (NF(I,J,K).GT.-1) THEN` (44).<br>`                ALM(I,J,K)=TCN0` (45).<br>`              ELSE` (46).<br>`                ALM(I,J,K)=0.0D0` (47).<br>`              ENDIF` (48).<br>` 100        CONTINUE` (49).<br>` 110      CONTINUE` (50).<br>` 120    CONTINUE` (51). |
| 53–78 | 시작 시 1행 SUBROUTINE VF_CLM00 루틴·40행 조건 안. 난류 경로에서는 VOF 함수로 밀도를 혼합하고 RI·TCP0/AKPR를 ANUT에 곱해 TCN0에 더한다(59–62). NF=-1이면 ALM=0이다(63–64).<br>`CD    -- 乱流モデルを使用する場合 --` (53) (난류모델을 사용하는 경우).<br>`      ELSE` (54).<br>주석 원문(실행하지 않음): `C2F     W=RHO0*TCP0/AKPR` (55).<br>`        DO 220 K=2,NUMK-1` (56).<br>`          DO 210 J=JA,JB` (57).<br>`            DO 200 I=IA,IB` (58).<br>`              IF (NF(I,J,K).NE.-1) THEN` (59).<br>`                RI=FF(I,J,K)*RHO0(1)+(1.0D0-FF(I,J,K))*RHO0(2)` (60).<br>`                W=RI*TCP0/AKPR` (61).<br>`                ALM(I,J,K)=TCN0+ANUT(I,J,K)*W` (62).<br>`              ELSE` (63).<br>`                ALM(I,J,K)=0.0D0` (64).<br>`              ENDIF` (65).<br>` 200        CONTINUE` (66).<br>` 210      CONTINUE` (67).<br>` 220    CONTINUE` (68).<br>`      ENDIF` (69).<br>`C     -- 実行文の終了 --` (71) (실행문 종료).<br>`      GOTO 9999` (72).<br>`C==== 終了 ===========================================================` (74) (종료).<br>` 9999 CONTINUE` (76).<br>`      RETURN` (77).<br>`      END` (78).<br>바깥 조건은 40행 `IF (LEQK.EQ.0) THEN`이다. 54행 ELSE는 `LEQK.NE.0` 경로이다. 이 IF는 69행에서 닫힌다. 59행 조건은 `NF(I,J,K).NE.-1`이므로 NF=-2도 혼합식 계산 경로에 들어간다. [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 44·59: 난류 비사용 경로는 NF>-1을 검사한다. 난류 경로는 NF가 -1과 다른지를 검사한다.
