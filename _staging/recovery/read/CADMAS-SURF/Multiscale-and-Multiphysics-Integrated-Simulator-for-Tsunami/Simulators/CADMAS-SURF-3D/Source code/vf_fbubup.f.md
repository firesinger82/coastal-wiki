---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Source code/vf_fbubup.f
lines: 77
sha256: 53ab181d418715fbfcb6dbed1b793dee32d24b92824e16014e00f508067b0401
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# vf_fbubup.f — 판독 구간 기록

구간은 1행부터 77행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–33 | TimerDoor 방법(TimerDoor method)으로 기포(bubble)를 상승시킨다. 격자·VOF 함수·공극률(porosity)·층별 최종 처리 시각과 통신 버퍼를 선언한다. 원문: `      SUBROUTINE VF_FBUBUP(ZZ,FF,GGV,TBUB,DBUF,NF)` (1) `CD=== 概要 ===========================================================` (3) (개요) `CDT   VF_FBUBUP:TimerDoor法による気泡の上昇` (5) (TimerDoor 방법에 의한 기포 상승) `C==== 宣言 ===========================================================` (7) (선언) `C     -- 大域型 --` (9) (전역 자료형) `      IMPLICIT INTEGER(I-N),DOUBLE PRECISION(A-H,O-Z)` (10) `C     -- 大域変数 --` (12) (전역 변수) `      INCLUDE 'VF_A0PRM.h'` (13) `      INCLUDE 'VF_ACOMPR.h'` (14) `      INCLUDE 'VF_ANUMBI.h'` (15) `      INCLUDE 'VF_APARAI.h'` (16) `      INCLUDE 'VF_APHYSR.h'` (17) `      INCLUDE 'VF_ATIMER.h'` (18) `CD    -- 引数 --` (20) (인수) `CD    ZZ(MAXG1,NUMK)   : IN  : R*8 : z方向格子座標等` (21) (z방향 격자 좌표 등) `CD    FF(@FOR-3D@)     : I/O : R*8 : VOF関数F` (22) (VOF 함수) `CD    GGV(@FOR-3D@)    : IN  : R*8 : 空隙率` (23) (공극률(porosity)) `CD    TBUB(NUMK)       : I/O : R*8 : 気泡上昇処理を最後に行った時間` (24) (기포 상승 처리를 마지막으로 수행한 시간) `CD    DBUF(NUMBUF*MAXBUF) : OUT :R*8 : 並列用のバッファ` (25) (병렬 통신 버퍼(buffer)) `CD    NF(@FOR-3D@)     : IN : I*4 : セルの状態を示すインデックス` (26) (셀(cell) 상태 인덱스(index)) `      DIMENSION ZZ(MAXG1,NUMK),FF(NUMI,NUMJ,NUMK)` (27) `      DIMENSION GGV(NUMI,NUMJ,NUMK),TBUB(NUMK)` (28) `      DIMENSION DBUF(NUMBUF*MAXBUF)` (29) `      DIMENSION NF(NUMI,NUMJ,NUMK)` (30) `C==== 実行 ===========================================================` (32) (실행) |
| 34–57 | 시작 시 1행 VF_FBUBUP 루틴 안이며 조건·루프 밖. K=NUMK-2부터 2까지 감소시키며 `DTBUB=ZZ(2,K)/WBUB`를 계산한다. `TNOW-TBUB(K).GT.DTBUB` 안에서 `FF(I,J,K).LT.FUPPER .AND. NF(I,J,K ).EQ. 0 .AND. NF(I,J,K1).NE.-1`인 셀만 FF를 갱신한다. `FF(I,J,K1)`에서 FMOVE/V1을 빼고 `FF(I,J,K)`에 FMOVE/V0을 더한다. 해석: ZZ(2,K)를 층 두께로 읽으면 DTBUB는 통과 시간에 해당하지만 이 구간에는 ZZ(2,K)의 정의가 없다. TBUB를 통과 시간만큼 더하고 VF_P3SRD2로 FF를 교환한다. 원문: `CD    -- 気泡セルの抽出と気泡の上昇 --` (34) (기포 셀 추출과 기포 상승) `      DO 120 K=NUMK-2,2,-1` (35) `        DTBUB=ZZ(2,K)/WBUB` (36) `        IF (TNOW-TBUB(K).GT.DTBUB) THEN` (37) `          K1=K+1` (38) `          DO 110 J=MYJS,MYJE` (39) `            DO 100 I=MYIS,MYIE` (40) 연속문: `              IF (FF(I,J,K).LT.FUPPER .AND. NF(I,J,K ).EQ. 0` (41); `     &                                .AND. NF(I,J,K1).NE.-1) THEN` (42) `                V0=ZZ(2,K )*GGV(I,J,K )` (43) `                V1=ZZ(2,K1)*GGV(I,J,K1)` (44) `                FMOVE=MIN((1.0D0-FF(I,J,K))*V0,FF(I,J,K1)*V1)` (45) `                FF(I,J,K1)=FF(I,J,K1)-FMOVE/V1` (46) `                FF(I,J,K )=FF(I,J,K )+FMOVE/V0` (47) `              ENDIF` (48) ` 100        CONTINUE` (49) ` 110      CONTINUE` (50) `          TBUB(K)=TBUB(K)+DTBUB` (51) `        ENDIF` (52) ` 120  CONTINUE` (53) `      CALL VF_P3SRD2(FF,DBUF,0)` (55) `C     TBUB(K)はプロセス単位で良い` (56) (TBUB(K)는 프로세스 단위여도 됨) [11-04 전수 검증 정정] |
| 58–77 | 시작 시 1행 VF_FBUBUP 루틴 안이며 조건·루프 밖. 기포 셀 디버그 출력 루프는 전부 주석이다. 실행 경로는 반환한다. 원문: `C     * デバッグ出力` (58) (디버그 출력) 주석: `C     DO 220 K=2,NUMK-1` (59) 주석: `C       DO 210 J=MYJS,MYJE` (60) 주석: `C         DO 200 I=MYIS,MYIE` (61) 주석: `C           IF (FF(I,J,K).LT.FUPPER .AND. NF(I,J,K).EQ.0) THEN` (62) 주석: `C             WRITE(*,*) 'FBUBUP',MYRANK,TNOW,` (63) 주석: `C    &                   0.5D0*(ZZ(1,K)+ZZ(1,K+1)),FF(I,J,K)` (64) 주석: `C           ENDIF` (65) 주석: `C200      CONTINUE` (66) 주석: `C210    CONTINUE` (67) 주석: `C220  CONTINUE` (68) `C     -- 実行文の終了 --` (70) (실행문 종료) `      GOTO 9999` (71) `C==== 終了 ===========================================================` (73) (종료) ` 9999 CONTINUE` (75) `      RETURN` (76) `      END` (77) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 36: DTBUB=ZZ(2,K)/WBUB를 계산하며 이 루틴에는 WBUB=0 검사가 없다.
- 37–52: 한 호출의 각 K에 대해 통과 시간 조건을 한 번 검사하고 TBUB(K)에 DTBUB를 한 번 더한다.
- 43–47: V0·V1을 분모로 사용하며 별도 0 검사는 없다.
