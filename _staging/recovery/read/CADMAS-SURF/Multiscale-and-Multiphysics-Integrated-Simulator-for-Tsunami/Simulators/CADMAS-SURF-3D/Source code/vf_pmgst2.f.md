---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Source code/vf_pmgst2.f
lines: 81
sha256: f0cc43128f6c9e737e133ed1932dcfef6f7eef3acfff175c55417d3081dd4bf3
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# vf_pmgst2.f — 판독 구간 기록

구간은 1행부터 81행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–22 | VF_PMGST2의 암시적 자료형·포함 파일과 배열 범위이다. IPF·JPF·KPF는 0번 첨자부터 시작한다. 원문: `      SUBROUTINE VF_PMGST2(XPF,YPF,ZPF,IPF,JPF,KPF)` (1); `CD=== 概要 ===========================================================` (3) (개요); `CDT   VF_PMGST2:マルチグリッド環境の子格子の数の設定` (5) (다중 격자(multigrid) 환경의 자식 격자 수 설정); `C==== 宣言 ===========================================================` (7) (선언); `C     -- 大域型 --` (9) (전역 자료형); `      IMPLICIT INTEGER(I-N),DOUBLE PRECISION(A-H,O-Z)` (10); `C     -- 大域変数 --` (12) (전역 변수); `      INCLUDE 'VF_A0PRM.h'` (13); `      INCLUDE 'VF_ANUMBI.h'` (14); `      INCLUDE 'VF_APARAI.h'` (15); `CD    -- 引数 --` (17) (인수); `      DIMENSION :: XPF(NUMI),YPF(NUMJ),ZPF(NUMK)` (18); `      DIMENSION :: IPF(0:MGPINF(1)),JPF(0:MGPINF(2)),KPF(0:MGPINF(3))` (19); `CD    -- 局所変数 --` (21) (지역 변수). |
| 23–43 | 시작 시 1행 VF_PMGST2 루틴 안. 부모 값이 0이거나 부모 셀 수 세 값이 모두 0이면 반환한다. x 방향에서는 `        II = INT(0.5D0*(XPF(I)+XPF(I+1))) + 1` (35)로 II를 구한다. XPF의 인수 설명은 부모 격자의 x 방향 보간계수이다(`vf_pmgset.f:38`). 각 II의 자식 수를 센 뒤 MYIS-1을 시작점으로 누적합(prefix sum)을 만든다. 원문: `C==== 実行 ===========================================================` (23) (실행); `      IF(MGPARE(MGRANK+1).EQ.0) GO TO 9999` (25); `      if( MGPINF(1).EQ.0.AND.MGPINF(2).EQ.0.AND.MGPINF(3).EQ.0 )` (26); 앞 행에서 이어지는 같은 문장: `     $   GO TO 9999` (27); `C` (28) (주석; 코드·선언도 실행되지 않음); `C X 方向` (29) (x 방향); `      DO 100 II=0,MGPINF(1)` (30); `        IPF(II) = 0` (31); ` 100  CONTINUE` (32); `C` (33) (주석; 코드·선언도 실행되지 않음); `      DO 110 I=MYIS,MYIE` (34); `        II = INT(0.5D0*(XPF(I)+XPF(I+1))) + 1` (35); `        IPF(II) = IPF(II) + 1` (36); ` 110  CONTINUE` (37); `C` (38) (주석; 코드·선언도 실행되지 않음); `      IPF(0) = MYIS-1` (39); `      DO 120 II=1,MGPINF(1)` (40); `        IPF(II) = IPF(II) + IPF(II-1)` (41); ` 120  CONTINUE` (42); `C` (43) (주석; 코드·선언도 실행되지 않음). [11-04 전수 검증 정정] |
| 44–58 | 시작 시 1행 VF_PMGST2 루틴 안. y 방향에서는 `        JJ = INT(0.5D0*(YPF(J)+YPF(J+1))) + 1` (50)로 JJ를 구해 셀 수를 센다. YPF의 인수 설명은 부모 격자의 y 방향 보간계수이다(`vf_pmgset.f:39`). MYJS-1을 시작점으로 JPF 누적합을 만든다. 원문: `C Y 方向` (44) (y 방향); `      DO 200 JJ=0,MGPINF(2)` (45); `        JPF(JJ) = 0` (46); ` 200  CONTINUE` (47); `C` (48) (주석; 코드·선언도 실행되지 않음); `      DO 210 J=MYJS,MYJE` (49); `        JJ = INT(0.5D0*(YPF(J)+YPF(J+1))) + 1` (50); `        JPF(JJ) = JPF(JJ) + 1` (51); ` 210  CONTINUE` (52); `C` (53) (주석; 코드·선언도 실행되지 않음); `      JPF(0) = MYJS-1` (54); `      DO 220 JJ=1,MGPINF(2)` (55); `        JPF(JJ) = JPF(JJ) + JPF(JJ-1)` (56); ` 220  CONTINUE` (57); `C` (58) (주석; 코드·선언도 실행되지 않음). [11-04 전수 검증 정정] |
| 59–81 | 시작 시 1행 VF_PMGST2 루틴 안. z 방향은 K=2:NUMK-1을 세고 KPF(0)=1을 시작점으로 누적합을 만든다. 종료 표지에서 반환한다. 원문: `C Z 方向` (59) (z 방향); `      DO 300 KK=0,MGPINF(3)` (60); `        KPF(KK) = 0` (61); ` 300  CONTINUE` (62); `C` (63) (주석; 코드·선언도 실행되지 않음); `      DO 310 K=2,NUMK-1` (64); `        KK = INT(0.5D0*(ZPF(K)+ZPF(K+1))) + 1` (65); `        KPF(KK) = KPF(KK) + 1` (66); ` 310  CONTINUE` (67); `C` (68) (주석; 코드·선언도 실행되지 않음); `      KPF(0) = 1` (69); `      DO 320 KK=1,MGPINF(3)` (70); `        KPF(KK) = KPF(KK) + KPF(KK-1)` (71); ` 320  CONTINUE` (72); `C     -- 実行文の終了 --` (74) (실행문 종료); `      GOTO 9999` (75); `C==== 終了 ===========================================================` (77) (종료); ` 9999 CONTINUE` (79); `      RETURN` (80); `      END` (81). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 25–27: 조기 반환은 MGPARE=0 또는 MGPINF(1:3)이 모두 0인 조건이다. 일부 방향만 0인 경우를 별도로 처리하는 분기는 없다.
- 35–36·50–51·65–66: XPF·YPF·ZPF의 인접 값 평균에 INT를 적용한 뒤 1을 더하여 II·JJ·KK를 계산한다. 이 루틴은 이들을 배열 첨자로 직접 사용한다. 이 루틴에는 범위 검사 분기가 없다. [11-04 전수 검증 정정]
