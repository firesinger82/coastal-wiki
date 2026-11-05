---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Source code/vf_cwmtb2.f
lines: 73
sha256: 0bb42f861761bd57658d1da66aab46b57fa4d5fefbaa92e7e5ce8051d8b70771
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# vf_cwmtb2.f — 판독 구간 기록

구간은 1행부터 73행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–29 | 행렬 자료(matrix data)의 법선·접선 유속을 구한다. 수직 검색 시작 위치와 위상 방향 가중치 및 속도 표 배열을 선언한다. 원문: `      SUBROUTINE VF_CWMTB2(KM,WT1,WT2,ZC,UN,UT,DMTBZZ,DMTBUN,DMTBUT)` (1) `CD=== 概要 ===========================================================` (3) (개요) `CDT   VF_CWMTB2:マトリクスデータの流速の計算` (5) (행렬 자료의 유속 계산) `C==== 宣言 ===========================================================` (7) (선언) `C     -- 大域型 --` (9) (전역 자료형) `      IMPLICIT INTEGER(I-N),DOUBLE PRECISION(A-H,O-Z)` (10) `C     -- 大域変数 --` (12) (전역 변수) `      INCLUDE 'VF_A0PRM.h'` (13) `      INCLUDE 'VF_AFILEI.h'` (14) `CD    -- 引数 --` (16) (인수) `CD    KM                  : I/O : I*4 : k方向検索開始位置` (17) (k방향 검색 시작 위치) `CD    WT1                 : IN  : R*8 : 位相方向補間の重み` (18) (위상 방향 보간 가중치) `CD    WT2                 : IN  : R*8 : 位相方向補間の重み` (19) (위상 방향 보간 가중치) `CD    ZC                  : IN  : R*8 : 鉛直座標(静面を基準)` (20) (정수면 기준 수직 좌표) `CD    UN                  : OUT : R*8 : 法線方向流速` (21) (법선 방향 유속) `CD    UT                  : OUT : R*8 : 接線方向流速` (22) (접선 방향 유속) `CD    DMTBZZ(MTBZZ)       : IN : R*8 : マトリクスデータのz座標` (23) (행렬 자료의 z좌표) `CD    DMTBUN(MTBZZ,MTBTT) : IN : R*8 : マトリクスデータの水平方向流速` (24) (행렬 자료의 수평 유속) `CD    DMTBUT(MTBZZ,MTBTT) : IN : R*8 : マトリクスデータの鉛直方向流速` (25) (행렬 자료의 수직 유속) `      DIMENSION DMTBZZ(MTBZZ),DMTBUN(MTBZZ,MTBTT),DMTBUT(MTBZZ,MTBTT)` (26) `C==== 実行 ===========================================================` (28) (실행) |
| 30–54 | 시작 시 1행 VF_CWMTB2 루틴 안이며 조건·루프 밖. 첫 z좌표 이하이거나 마지막 z좌표 이상이면 끝점 가중치를 쓴다. 내부 좌표는 KM부터 증가 방향으로 검색하고 선형 보간(linear interpolation) 가중치를 구한다. 검색 실패 시 VF_A2ERR를 호출한다. 원문: `CD    -- 位置の検索(部分サーチ) --` (30) (위치 검색. 부분 검색) `      IF     (ZC.LE.DMTBZZ(1)    ) THEN` (31) `        KM=1` (32) `        W1=1.0D0` (33) `        W2=0.0D0` (34) `      ELSEIF (ZC.GE.DMTBZZ(MTBZZ)) THEN` (35) `        KM=MTBZZ-1` (36) `        W1=0.0D0` (37) `        W2=1.0D0` (38) `      ELSE` (39) `        KP=0` (40) `        DO 100 K=KM,MTBZZ-1` (41) `          IF (DMTBZZ(K).LE.ZC .AND. ZC.LE.DMTBZZ(K+1)) THEN` (42) `            KP=K` (43) `            W2=1.0D0/(DMTBZZ(K+1)-DMTBZZ(K))` (44) `            W1=(DMTBZZ(K+1)-ZC)*W2` (45) `            W2=(ZC-DMTBZZ(K  ))*W2` (46) `            GOTO 110` (47) `          ENDIF` (48) ` 100    CONTINUE` (49) ` 110    CONTINUE` (50) `        IF (KP.EQ.0) CALL VF_A2ERR('VF_CWMTB2','P.G ERROR.')` (51) `        KM=KP` (52) `      ENDIF` (53) [11-04 전수 검증 정정] |
| 55–73 | 시작 시 1행 VF_CWMTB2 루틴 안이며 조건·루프 밖. 수직 방향 가중치 W1·W2로 두 위상의 유속을 각각 구한다. 그 결과를 WT1·WT2로 보간하여 UN·UT를 반환한다. 원문: `CD    -- 流速の計算 --` (55) (유속 계산) `      KM1=KM+1` (56) `      IM =MTBNOW` (57) `      IM1=MTBNOW+1` (58) `      P1=W1*DMTBUN(KM,IM )+W2*DMTBUN(KM1,IM )` (59) `      P2=W1*DMTBUN(KM,IM1)+W2*DMTBUN(KM1,IM1)` (60) `      UN=WT1*P1+WT2*P2` (61) `      P1=W1*DMTBUT(KM,IM )+W2*DMTBUT(KM1,IM )` (62) `      P2=W1*DMTBUT(KM,IM1)+W2*DMTBUT(KM1,IM1)` (63) `      UT=WT1*P1+WT2*P2` (64) `C     -- 実行文の終了 --` (66) (실행문 종료) `      GOTO 9999` (67) `C==== 終了 ===========================================================` (69) (종료) ` 9999 CONTINUE` (71) `      RETURN` (72) `      END` (73) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 41–52: 내부 좌표 검색은 KM 이상만 방문한다. KM보다 작은 구간을 재검색하는 루프는 없다.
