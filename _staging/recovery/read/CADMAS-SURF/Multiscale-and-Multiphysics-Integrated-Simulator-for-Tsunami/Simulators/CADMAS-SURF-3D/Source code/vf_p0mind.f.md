---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Source code/vf_p0mind.f
lines: 40
sha256: 344302e818bb24d50c2d7b5fa0e95cac48f40a3b8a83c1ee3af8471b4004f247
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# vf_p0mind.f — 판독 구간 기록

구간은 1행부터 40행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–22 | 실수 최솟값 축약(reduction) 루틴의 형식·포함 파일과 송수신 스칼라의 의미를 선언한다. 원문: `      SUBROUTINE VF_P0MIND(DSEND,DRECV)` (1). `CD=== 概要 ===========================================================` (3) (개요). `CDT   VF_P0MIND:データの最小値を求める/実数` (5) (실수 데이터 최솟값을 구한다). `C==== 宣言 ===========================================================` (7) (선언). `C     -- 大域型 --` (9) (전역 형식). `      IMPLICIT INTEGER(I-N),DOUBLE PRECISION(A-H,O-Z)` (10). `C     -- 大域変数 --` (12) (전역 변수). `      INCLUDE 'VF_A0PRM.h'` (13). `      INCLUDE 'VF_ACPUTR.h'` (14). `      INCLUDE 'VF_APARAI.h'` (15). `CD    -- 引数 --` (17) (인수). `CD    DSEND : IN  : R*8 : 送信するデータ` (18) (송신할 데이터). `CD    DRECV : OUT : R*8 : データの最小値` (19) (데이터 최솟값). `C==== 実行 ===========================================================` (21) (실행). |
| 23–40 | 시작 시 1행 루틴 `SUBROUTINE VF_P0MIND` 안. CPU 계측을 시작한다. MGPROC!=1이면 VF_ZXMG_ALLMND를 호출한다. 단일 프로세스이면 DRECV=DSEND로 복사한다. 계측을 종료하고 반환한다. 원문: `      CALL VF_A2CPUT(0,ICPUST,KCP9PL)` (23). `C     -- 最小値をとる --` (25) (최솟값을 취한다). `      IF (MGPROC.NE.1) THEN` (26). `        CALL VF_ZXMG_ALLMND(DSEND,DRECV,IERR)` (27). `      ELSE` (28). `        DRECV=DSEND` (29). `      ENDIF` (30). `C     -- 実行文の終了 --` (32) (실행문 종료). `      CALL VF_A2CPUT(0,ICPUEN,KCP9PL)` (33). `      GOTO 9999` (34). `C==== 終了 ===========================================================` (36) (종료). ` 9999 CONTINUE` (38). `      RETURN` (39). `      END` (40). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
