---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Source code/vf_cwmtb22.f
lines: 74
sha256: 1277081b7f6bedefa39e1d9ab05ae8e66507097e7af85a5b8498ac6ac3f9ad9b
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# vf_cwmtb22.f — 판독 구간 기록

구간은 1행부터 74행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–30 | 행렬 자료(matrix data)의 법선·접선 유속을 구한다. 수직 검색 시작 위치와 위상 방향 가중치 및 속도 표 배열을 선언한다. 원문: `      SUBROUTINE VF_CWMTB22(KM,WT1,WT2,ZC,UN,UT,DMTBZZ,DMTBUN,DMTBUT)` (1) `CD=== 概要 ===========================================================` (3) (개요) `CDT   VF_CWMTB22:マトリクスデータ-2の流速の計算` (5) (두 번째 행렬 자료의 유속 계산) `C==== 宣言 ===========================================================` (7) (선언) `C     -- 大域型 --` (9) (전역 자료형) `      IMPLICIT INTEGER(I-N),DOUBLE PRECISION(A-H,O-Z)` (10) `C     -- 大域変数 --` (12) (전역 변수) `      INCLUDE 'VF_A0PRM.h'` (13) `      INCLUDE 'VF_AFILEI.h'` (14) `CD    -- 引数 --` (16) (인수) `CD    KM                  : I/O : I*4 : k方向検索開始位置` (17) (k방향 검색 시작 위치) `CD    WT1                 : IN  : R*8 : 位相方向補間の重み` (18) (위상 방향 보간 가중치) `CD    WT2                 : IN  : R*8 : 位相方向補間の重み` (19) (위상 방향 보간 가중치) `CD    ZC                  : IN  : R*8 : 鉛直座標(静面を基準)` (20) (정수면 기준 수직 좌표) `CD    UN                  : OUT : R*8 : 法線方向流速` (21) (법선 방향 유속) `CD    UT                  : OUT : R*8 : 接線方向流速` (22) (접선 방향 유속) `CD    DMTBZZ(MTBZZ)       : IN : R*8 : マトリクスデータのz座標` (23) (행렬 자료의 z좌표) `CD    DMTBUN(MTBZZ,MTBTT) : IN : R*8 : マトリクスデータの水平方向流速` (24) (행렬 자료의 수평 유속) `CD    DMTBUT(MTBZZ,MTBTT) : IN : R*8 : マトリクスデータの鉛直方向流速` (25) (행렬 자료의 수직 유속) `      DIMENSION DMTBZZ(MTBZZ2),DMTBUN(MTBZZ2,MTBTT2)` (26) `      DIMENSION DMTBUT(MTBZZ2,MTBTT2)` (27) `C==== 実行 ===========================================================` (29) (실행) |
| 31–55 | 시작 시 1행 VF_CWMTB22 루틴 안이며 조건·루프 밖. 첫 z좌표 이하이거나 마지막 z좌표 이상이면 끝점 가중치를 쓴다. 내부 좌표는 KM부터 증가 방향으로 검색하고 선형 보간(linear interpolation) 가중치를 구한다. 검색 실패 시 VF_A2ERR를 호출한다. 원문: `CD    -- 位置の検索(部分サーチ) --` (31) (위치 검색. 부분 검색) `      IF     (ZC.LE.DMTBZZ(1)    ) THEN` (32) `        KM=1` (33) `        W1=1.0D0` (34) `        W2=0.0D0` (35) `      ELSEIF (ZC.GE.DMTBZZ(MTBZZ2)) THEN` (36) `        KM=MTBZZ2-1` (37) `        W1=0.0D0` (38) `        W2=1.0D0` (39) `      ELSE` (40) `        KP=0` (41) `        DO 100 K=KM,MTBZZ2-1` (42) `          IF (DMTBZZ(K).LE.ZC .AND. ZC.LE.DMTBZZ(K+1)) THEN` (43) `            KP=K` (44) `            W2=1.0D0/(DMTBZZ(K+1)-DMTBZZ(K))` (45) `            W1=(DMTBZZ(K+1)-ZC)*W2` (46) `            W2=(ZC-DMTBZZ(K  ))*W2` (47) `            GOTO 110` (48) `          ENDIF` (49) ` 100    CONTINUE` (50) ` 110    CONTINUE` (51) `        IF (KP.EQ.0) CALL VF_A2ERR('VF_CWMTB22','P.G ERROR.')` (52) `        KM=KP` (53) `      ENDIF` (54) [11-04 전수 검증 정정] |
| 56–74 | 시작 시 1행 VF_CWMTB22 루틴 안이며 조건·루프 밖. 수직 방향 가중치 W1·W2로 두 위상의 유속을 각각 구한다. 그 결과를 WT1·WT2로 보간하여 UN·UT를 반환한다. 원문: `CD    -- 流速の計算 --` (56) (유속 계산) `      KM1=KM+1` (57) `      IM =MTBNOW2` (58) `      IM1=MTBNOW2+1` (59) `      P1=W1*DMTBUN(KM,IM )+W2*DMTBUN(KM1,IM )` (60) `      P2=W1*DMTBUN(KM,IM1)+W2*DMTBUN(KM1,IM1)` (61) `      UN=WT1*P1+WT2*P2` (62) `      P1=W1*DMTBUT(KM,IM )+W2*DMTBUT(KM1,IM )` (63) `      P2=W1*DMTBUT(KM,IM1)+W2*DMTBUT(KM1,IM1)` (64) `      UT=WT1*P1+WT2*P2` (65) `C     -- 実行文の終了 --` (67) (실행문 종료) `      GOTO 9999` (68) `C==== 終了 ===========================================================` (70) (종료) ` 9999 CONTINUE` (72) `      RETURN` (73) `      END` (74) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 42–53: 내부 좌표 검색은 KM 이상만 방문한다. KM보다 작은 구간을 재검색하는 루프는 없다.
- 23–27: 인수 설명은 MTBZZ·MTBTT를 쓰지만 실제 DIMENSION은 MTBZZ2·MTBTT2를 쓴다.
