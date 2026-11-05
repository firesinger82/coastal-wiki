---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D2F/Source code/vf_cdd00.f
lines: 78
sha256: 16ac6590486c1aed55c1dc273a794f591c0b2fb2bd1b6daefe4f968f671360c7
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# vf_cdd00.f — 판독 구간 기록

구간은 1행부터 78행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–25 | 확산계수 합 계산 루틴과 4차원 DD 배열 선언이다(1–23).<br>`      SUBROUTINE VF_CDD00(ANUT,DD,NF)` (1).<br>`CD=== 概要 ===========================================================` (3) (개요).<br>`CDT   VF_CDD00:拡散係数と乱流拡散係数の和を計算する` (5) (VF_CDD00:확산계수와 난류 확산계수의 합을 계산한다).<br>`C==== 宣言 ===========================================================` (7) (선언).<br>`C     -- 大域型 --` (9) (전역 형).<br>`      IMPLICIT INTEGER(I-N),DOUBLE PRECISION(A-H,O-Z)` (10).<br>`C     -- 大域変数 --` (12) (전역 변수).<br>`      INCLUDE 'VF_A0PRM.h'` (13).<br>`      INCLUDE 'VF_ANUMBI.h'` (14).<br>`      INCLUDE 'VF_APARAI.h'` (15).<br>`      INCLUDE 'VF_APHYSR.h'` (16).<br>`CD    -- 引数 --` (18) (인수).<br>`CD    ANUT(@FOR-3D@)    : IN  : R*8 : 渦動粘性係数νt` (19) (ANUT(@FOR-3D@)    : IN  : R*8 : 와동점성계수 νt).<br>`CD    DD(@FOR-3D@,LEQC) : I/O : R*8 : 拡散係数と乱流拡散係数の和` (20) (DD(@FOR-3D@,LEQC) : I/O : R*8 : 확산계수와 난류 확산계수의 합).<br>`CD    NF(@FOR-3D@)      : IN  : I*4 : セルの状態を示すインデックス` (21) (NF(@FOR-3D@)      : IN  : I*4 : 셀 상태를 나타내는 인덱스).<br>`      DIMENSION ANUT(NUMI,NUMJ,NUMK),DD(NUMI,NUMJ,NUMK,LEQC)` (22).<br>`      DIMENSION NF  (NUMI,NUMJ,NUMK)` (23).<br>`C==== 実行 ===========================================================` (25) (실행). |
| 26–52 | 시작 시 1행 SUBROUTINE VF_CDD00 루틴 안. 병렬 경계 여부에 따라 I/J 범위를 좁힌다(28–35). `LEQK.EQ.0`이면 `NF(I,J,K).GT.-1`인 셀의 DD를 CDF0로 채운다(38–44). 같은 루프에서 그 밖의 셀은 0으로 채운다(45–46).<br>`CD    -- 並列時の範囲変更 --` (27) (병렬 실행 시 범위 변경).<br>`      IA=1` (28).<br>`      IB=NUMI` (29).<br>`      JA=1` (30).<br>`      JB=NUMJ` (31).<br>`      IF (MYMIS.EQ.1) IA=2` (32).<br>`      IF (MYMIE.EQ.1) IB=NUMI-1` (33).<br>`      IF (MYMJS.EQ.1) JA=2` (34).<br>`      IF (MYMJE.EQ.1) JB=NUMJ-1` (35).<br>`CD    -- 乱流モデルを使用しない場合 --` (37) (난류모델을 사용하지 않는 경우).<br>`      IF (LEQK.EQ.0) THEN` (38).<br>`        DO 130 LC=1,LEQC` (39).<br>`          DO 120 K=2,NUMK-1` (40).<br>`            DO 110 J=JA,JB` (41).<br>`              DO 100 I=IA,IB` (42).<br>`                IF (NF(I,J,K).GT.-1) THEN` (43).<br>`                  DD(I,J,K,LC)=CDF0(LC)` (44).<br>`                ELSE` (45).<br>`                  DD(I,J,K,LC)=0.0D0` (46).<br>`                ENDIF` (47).<br>` 100          CONTINUE` (48).<br>` 110        CONTINUE` (49).<br>` 120      CONTINUE` (50).<br>` 130    CONTINUE` (51). [11-04 전수 검증 정정] |
| 53–78 | 시작 시 38행 `IF (LEQK.EQ.0) THEN` 안이다. 54행 ELSE는 `LEQK.NE.0`인 경로이다. 이 IF는 69행에서 닫힌다. 난류모델 경로는 AKSM 계수의 역수를 적용한 ANUT를 더한다(54–68). 55행 `DO 230 LC=1,LEQC`는 68행에서 닫힌다. 72행 `GOTO 9999`는 76행으로 이동한다. 77행 RETURN으로 복귀한다.<br>`CD    -- 乱流モデルを使用する場合 --` (53) (난류모델을 사용하는 경우).<br>`      ELSE` (54).<br>`        DO 230 LC=1,LEQC` (55).<br>`          W=1.0D0/AKSM(LC)` (56).<br>`          DO 220 K=2,NUMK-1` (57).<br>`            DO 210 J=JA,JB` (58).<br>`              DO 200 I=IA,IB` (59).<br>`                IF (NF(I,J,K).GT.-1) THEN` (60).<br>`                  DD(I,J,K,LC)=CDF0(LC)+ANUT(I,J,K)*W` (61).<br>`                ELSE` (62).<br>`                  DD(I,J,K,LC)=0.0D0` (63).<br>`                ENDIF` (64).<br>` 200          CONTINUE` (65).<br>` 210        CONTINUE` (66).<br>` 220      CONTINUE` (67).<br>` 230    CONTINUE` (68).<br>`      ENDIF` (69).<br>`C     -- 実行文の終了 --` (71) (실행문 종료).<br>`      GOTO 9999` (72).<br>`C==== 終了 ===========================================================` (74) (종료).<br>` 9999 CONTINUE` (76).<br>`      RETURN` (77).<br>`      END` (78). [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 56·61: AKSM(LC)의 역수를 직접 계산한다. 이 파일에는 AKSM이 0인지 검사하는 문장이 없다.
