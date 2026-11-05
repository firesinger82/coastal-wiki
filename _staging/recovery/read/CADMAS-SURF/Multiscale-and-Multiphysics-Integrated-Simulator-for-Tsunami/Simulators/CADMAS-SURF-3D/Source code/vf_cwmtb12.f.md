---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Source code/vf_cwmtb12.f
lines: 79
sha256: d4761d10da14a196176790f27e55a065ef3cbc86c90bd32994660352922a1b6f
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# vf_cwmtb12.f — 판독 구간 기록

구간은 1행부터 79행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–26 | 두 번째 행렬 자료(matrix data)의 위상으로 수위를 구한다. 배열과 보간 가중치(interpolation weight) 인수를 선언한다. 원문: `      SUBROUTINE VF_CWMTB12(WVT,W1,W2,WVZ,DMTBTT,DMTBHH)` (1) `CD=== 概要 ===========================================================` (3) (개요) `CDT   VF_CWMTB12:マトリクスデータ-2の水位の計算` (5) (두 번째 행렬 자료의 수위 계산) `C==== 宣言 ===========================================================` (7) (선언) `C     -- 大域型 --` (9) (전역 자료형) `      IMPLICIT INTEGER(I-N),DOUBLE PRECISION(A-H,O-Z)` (10) `C     -- 大域変数 --` (12) (전역 변수) `      INCLUDE 'VF_A0PRM.h'` (13) `      INCLUDE 'VF_AFILEI.h'` (14) `CD    -- 引数 --` (16) (인수) `CD    WVT            : IN  : R*8 : 無次元位相` (17) (무차원 위상) `CD    W1             : OUT : R*8 : 補間の重み(f=W1*f(i)+W2*f(i+1))` (18) (보간 가중치(interpolation weight). f=W1*f(i)+W2*f(i+1)) `CD    W2             : OUT : R*8 : 補間の重み(f=W1*f(i)+W2*f(i+1))` (19) (보간 가중치(interpolation weight). f=W1*f(i)+W2*f(i+1)) `CD    WVZ            : OUT : R*8 : 水位変動` (20) (수위 변동) `CD    DMTBTT(MTBTT2) : IN : R*8 : マトリクスデータの無次元位相` (21) (행렬 자료(matrix data)의 무차원 위상) `CD    DMTBHH(MTBTT2) : IN : R*8 : マトリクスデータの水位` (22) (행렬 자료의 수위) `      DIMENSION DMTBTT(MTBTT2),DMTBHH(MTBTT2)` (23) `C==== 実行 ===========================================================` (25) (실행) |
| 27–64 | 시작 시 1행 VF_CWMTB12 루틴 안이며 조건·루프 밖. 첫 위상 이하이거나 마지막 위상 이상이면 끝점 가중치를 쓴다. 내부에서는 MTBNOW2부터 역방향으로 구간을 찾고 실패하면 나머지 구간을 역방향 검색한다. 구간 폭으로 W1·W2를 정하고 검색 실패 시 VF_A2ERR를 호출한다. 원문: `CD    -- 位置の検索(全サーチ) --` (27) (위치 검색. 전체 검색) `      IF (MTBNOW2.LE.0) MTBNOW2=MTBTT2-1` (28) `      IF     (WVT.LE.DMTBTT(1)     ) THEN` (29) `        MTBNOW2=1` (30) `        W1=1.0D0` (31) `        W2=0.0D0` (32) `      ELSEIF (WVT.GE.DMTBTT(MTBTT2)) THEN` (33) `        MTBNOW2=MTBTT2-1` (34) `        W1=0.0D0` (35) `        W2=1.0D0` (36) `      ELSE` (37) `        IP=0` (38) `        DO 100 I=MTBNOW2,1,-1` (39) `          IF (DMTBTT(I).LE.WVT .AND. WVT.LE.DMTBTT(I+1)) THEN` (40) `            IP=I` (41) `            W2=1.0D0/(DMTBTT(I+1)-DMTBTT(I))` (42) `            W1=(DMTBTT(I+1)-WVT)*W2` (43) `            W2=(WVT-DMTBTT(I  ))*W2` (44) `            GOTO 110` (45) `          ENDIF` (46) ` 100    CONTINUE` (47) ` 110    CONTINUE` (48) `        IF (IP.EQ.0) THEN` (49) `          DO 200 I=MTBTT2-1,MTBNOW2+1,-1` (50) `            IF (DMTBTT(I).LE.WVT .AND. WVT.LE.DMTBTT(I+1)) THEN` (51) `              IP=I` (52) `              W2=1.0D0/(DMTBTT(I+1)-DMTBTT(I))` (53) `              W1=(DMTBTT(I+1)-WVT)*W2` (54) `              W2=(WVT-DMTBTT(I  ))*W2` (55) `              GOTO 210` (56) `            ENDIF` (57) ` 200      CONTINUE` (58) ` 210      CONTINUE` (59) `        ENDIF` (60) `        IF (IP.EQ.0) CALL VF_A2ERR('VF_CWMTB12','P.G ERROR.')` (61) `        MTBNOW2=IP` (62) `      ENDIF` (63) [11-04 전수 검증 정정] |
| 65–79 | 시작 시 1행 VF_CWMTB12 루틴 안이며 조건·루프 밖. 자료 종류가 2이면 수위 0을 반환한다. 그 외에는 두 시점 수위를 W1·W2로 선형 보간(linear interpolation)한다. 원문: `CD    -- 水位の計算 --` (65) (수위 계산) `      IF (MTBTYP2.NE.2) THEN` (66) `        WVZ=W1*DMTBHH(MTBNOW2)+W2*DMTBHH(MTBNOW2+1)` (67) `      ELSE` (68) `        WVZ=0.0D0` (69) `      ENDIF` (70) `C     -- 実行文の終了 --` (72) (실행문 종료) `      GOTO 9999` (73) `C==== 終了 ===========================================================` (75) (종료) ` 9999 CONTINUE` (77) `      RETURN` (78) `      END` (79) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 28–62: MTBNOW2의 비양수 값은 보정하지만 양수 상한을 검사하는 문장은 없다.
- 42·53: 인접 위상 차의 역수를 계산한다. 두 위상이 같은지 검사하는 문장은 이 블록에 없다.
