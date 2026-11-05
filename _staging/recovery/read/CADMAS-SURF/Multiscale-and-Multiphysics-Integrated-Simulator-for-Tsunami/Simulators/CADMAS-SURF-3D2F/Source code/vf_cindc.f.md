---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D2F/Source code/vf_cindc.f
lines: 62
sha256: 0a2ed4ae651eae8433204ff783c9b705883bad997a607ef0c20afc5c2daa224a
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# vf_cindc.f — 판독 구간 기록

구간은 1행부터 62행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–23 | 셀 계산 상태 INDC 설정 루틴의 선언이다(1–20).<br>`      SUBROUTINE VF_CINDC(NF,INDC)` (1).<br>`CD=== 概要 ===========================================================` (3) (개요).<br>`CDT   VF_CINDC:セルの計算状態を示すインデックスINDCを設定する` (5) (VF_CINDC:셀 계산 상태 인덱스 INDC를 설정한다).<br>`C==== 宣言 ===========================================================` (7) (선언).<br>`C     -- 大域型 --` (9) (전역 형).<br>`      IMPLICIT INTEGER(I-N),DOUBLE PRECISION(A-H,O-Z)` (10).<br>`C     -- 大域変数 --` (12) (전역 변수).<br>`      INCLUDE 'VF_A0PRM.h'` (13).<br>`      INCLUDE 'VF_ANUMBI.h'` (14).<br>`      INCLUDE 'VF_APARAI.h'` (15).<br>`CD    -- 引数 --` (17) (인수).<br>`CD    NF(@FOR-3D@)   : IN  : I*4 : セルの状態を示すインデックス` (18) (NF(@FOR-3D@)   : IN  : I*4 : 셀 상태를 나타내는 인덱스).<br>`CD    INDC(@FOR-3D@) : I/O : I*4 : セルの計算状態を示すインデックス` (19) (INDC(@FOR-3D@) : I/O : I*4 : 셀 계산 상태 인덱스).<br>`      DIMENSION NF(NUMI,NUMJ,NUMK),INDC(NUMI,NUMJ,NUMK)` (20).<br>`C==== 実行 ===========================================================` (22) (실행). |
| 24–33 | 시작 시 1행 SUBROUTINE VF_CINDC 루틴 안. 병렬 경계 플래그에 따라 I/J 범위를 조정한다(25–32).<br>`CD    -- 並列時の範囲変更 --` (24) (병렬 실행 시 범위 변경).<br>`      IA=1` (25).<br>`      IB=NUMI` (26).<br>`      JA=1` (27).<br>`      JB=NUMJ` (28).<br>`      IF (MYMIS.EQ.1) IA=2` (29).<br>`      IF (MYMIE.EQ.1) IB=NUMI-1` (30).<br>`      IF (MYMJS.EQ.1) JA=2` (31).<br>`      IF (MYMJE.EQ.1) JB=NUMJ-1` (32). |
| 34–62 | 시작 시 1행 SUBROUTINE VF_CINDC 루틴 안. NF=0·NF=8과 나머지 표면 셀은 INDC=0으로 설정한다(39–49). NF<=-1이면 INDC=-1이다(45–46). K=2..NUMK-1을 순회하고 반환한다(35–62).<br>`CD    -- INDCを設定 --` (34) (INDC 설정).<br>`      DO 120 K=2,NUMK-1` (35).<br>`        DO 110 J=JA,JB` (36).<br>`          DO 100 I=IA,IB` (37).<br>`C           * 流体セルが最も多いと仮定` (38) (* 유체 셀이 가장 많다고 가정).<br>`            IF     (NF(I,J,K).EQ. 0) THEN` (39).<br>`              INDC(I,J,K)=0` (40).<br>`C           * 気体セルが次に多いと仮定` (41) (* 기체 셀이 다음으로 많다고 가정).<br>`            ELSEIF (NF(I,J,K).EQ. 8) THEN` (42).<br>`              INDC(I,J,K)=0` (43).<br>`C           * そして、障害物セルならば` (44) (* 그다음 장애물 셀이면).<br>`            ELSEIF (NF(I,J,K).LE.-1) THEN` (45).<br>`              INDC(I,J,K)=-1` (46).<br>`C           * でなければ、表面セル` (47) (* 그렇지 않으면 표면 셀).<br>`            ELSE` (48).<br>`              INDC(I,J,K)=0` (49).<br>`            ENDIF` (50).<br>` 100      CONTINUE` (51).<br>` 110    CONTINUE` (52).<br>` 120  CONTINUE` (53).<br>`C     -- 実行文の終了 --` (55) (실행문 종료).<br>`      GOTO 9999` (56).<br>`C==== 終了 ===========================================================` (58) (종료).<br>` 9999 CONTINUE` (60).<br>`      RETURN` (61).<br>`      END` (62). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
