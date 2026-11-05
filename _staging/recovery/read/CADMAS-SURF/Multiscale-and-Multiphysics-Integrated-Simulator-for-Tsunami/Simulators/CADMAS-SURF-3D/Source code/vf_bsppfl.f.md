---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Source code/vf_bsppfl.f
lines: 78
sha256: 73a4cbc03c90aad261bcef2c6f8379c592ed10e28f71af61320a7d8fa761428d
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# vf_bsppfl.f — 판독 구간 기록

구간은 1행부터 78행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–29 | VF_BSPPFL은 기체에서 유체로 바뀐 셀의 압력을 설정한다. IMPLICIT·INCLUDE·배열 선언을 둔다. PP0는 갱신 전 압력 작업 배열, NF0는 갱신 전 셀 상태이다. 원문: `      SUBROUTINE VF_BSPPFL(PP,FF,DBUF,PP0,NF,NF0)` (1); `CD=== 概要 ===========================================================` (3) (개요); `CDT   VF_BSPPFL:気体セルから流体セルへ変化したセルの圧力を設定する` (5) (기체 셀에서 유체 셀로 바뀐 셀의 압력 설정); `C==== 宣言 ===========================================================` (7) (선언); `C     -- 大域型 --` (9) (전역 형); `      IMPLICIT INTEGER(I-N),DOUBLE PRECISION(A-H,O-Z)` (10); `C     -- 大域変数 --` (12) (전역 변수); `      INCLUDE 'VF_A0PRM.h'` (13); `      INCLUDE 'VF_ANUMBI.h'` (14); `      INCLUDE 'VF_APARAI.h'` (15); `CD    -- 引数 --` (17) (인수); `CD    PP(@FOR-3D@)  : I/O : R*8 : 圧力` (18) (압력); `CD    FF(@FOR-3D@)  : IN  : R*8 : VOF関数F` (19) (VOF 함수); `CD    DBUF(NUMBUF*MAXBUF) : OUT :R*8 : 並列用のバッファ` (20) (병렬용 버퍼); `CD    PP0(@FOR-3D@) : OUT : R*8 : ワーク(更新前の圧力)` (21) (작업 배열, 갱신 전 압력); `CD    NF(@FOR-3D@)  : IN  : I*4 : セルの状態を示すインデックス` (22) (셀 상태 첨자); `CD    NF0(@FOR-3D@) : IN  : I*4 : 更新前のNF` (23) (갱신 전 NF); `      DIMENSION PP (NUMI,NUMJ,NUMK),FF (NUMI,NUMJ,NUMK)` (24); `      DIMENSION DBUF(NUMBUF*MAXBUF),PP0(NUMI,NUMJ,NUMK)` (25); `      DIMENSION NF (NUMI,NUMJ,NUMK),NF0(NUMI,NUMJ,NUMK)` (26); `C==== 実行 ===========================================================` (28) (실행). |
| 30–58 | 1행 VF_BSPPFL 안. 전체 격자의 PP를 PP0에 복사한다. 현재 NF=0·이전 NF0=8인 담당 내부 셀만 3×3×3 이웃을 순회하여 현재 NF=0인 값의 FF와 FF*PP0를 누적한다. 49·55행 중심 제외 조건은 C@@@@ 주석 코드이다. 원문: `CD    -- 更新前の圧力を退避する --` (30) (갱신 전 압력 보관); `      DO 120 K=1,NUMK` (31); `        DO 110 J=1,NUMJ` (32); `          DO 100 I=1,NUMI` (33); `            PP0(I,J,K)=PP(I,J,K)` (34); ` 100      CONTINUE` (35); ` 110    CONTINUE` (36); ` 120  CONTINUE` (37); `CD    -- 圧力を更新する(単純な平均とする) --` (39) (압력 갱신, 단순 평균이라는 주석); `      DO 320 K=2,NUMK-1` (40); `        DO 310 J=MYJS,MYJE` (41); `          DO 300 I=MYIS,MYIE` (42); `            IF (NF(I,J,K).EQ.0 .AND. NF0(I,J,K).EQ.8) THEN` (43); `              SUMF=0.0D0` (44); `              SUMP=0.0D0` (45); `              DO 220 KP=-1,1` (46); `                DO 210 JP=-1,1` (47); `                  DO 200 IP=-1,1` (48); `C@@@@                    IF (IP.NE.0 .OR. JP.NE.0 .OR. KP.NE.0) THEN` (49); `                      IF (NF(I+IP,J+JP,K+KP).EQ.0) THEN` (50); `                        F   =FF(I+IP,J+JP,K+KP)` (51); `                        SUMF=SUMF+F` (52); `                        SUMP=SUMP+F*PP0(I+IP,J+JP,K+KP)` (53); `                      ENDIF` (54); `C@@@@                    ENDIF` (55); ` 200              CONTINUE` (56); ` 210            CONTINUE` (57); ` 220          CONTINUE` (58). |
| 59–78 | 시작 시 1행 VF_BSPPFL·40행 `DO 320 K=2,NUMK-1`, 41행 `DO 310 J=MYJS,MYJE`, 42행 `DO 300 I=MYIS,MYIE` 루프와 43행 `IF (NF(I,J,K).EQ.0 .AND. NF0(I,J,K).EQ.8) THEN` 안. SUMF.LT.ZERO이면 PP=0, ELSE는 SUMP/SUMF이다. 조건과 루프를 닫은 뒤 VF_P3SRD2(PP,DBUF,0)를 호출하고 반환한다. 원문: `              IF (SUMF.LT.ZERO) THEN` (59); `                PP(I,J,K)=0.0D0` (60); `              ELSE` (61); `                PP(I,J,K)=SUMP/SUMF` (62); `              ENDIF` (63); `            ENDIF` (64); ` 300      CONTINUE` (65); ` 310    CONTINUE` (66); ` 320  CONTINUE` (67); `      CALL VF_P3SRD2(PP,DBUF,0)` (69); `C     -- 実行文の終了 --` (71) (실행문 종료); `      GOTO 9999` (72); `C==== 終了 ===========================================================` (74) (종료); ` 9999 CONTINUE` (76); `      RETURN` (77); `      END` (78). 43행 IF는 64행 ENDIF에서 닫힌다. I·J·K 루프는 각각 65행 300, 66행 310, 67행 320 CONTINUE에서 닫힌다. [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 49·55: IP·JP·KP가 모두 0인 중심 셀을 제외하는 IF와 ENDIF는 주석 처리되었다. 50행 현재 NF=0 조건을 만족하는 중심도 합산된다.
- 39·51–53·62: 주석은 단순 평균이라고 적지만 계산은 FF 가중 SUMP/SUMF이다.
- 50·43: 합산 이웃은 현재 NF만 검사한다. 이전 NF0 조건은 갱신 대상 셀에서만 검사한다.
