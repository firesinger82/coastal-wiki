---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Source code/vf_p1bcsd.f
lines: 38
sha256: 88d8cfd91bb2d01d232ad3b7118ddcf3f97737da0afa1720ae22376e39b72914
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# vf_p1bcsd.f — 판독 구간 기록

구간은 1행부터 38행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–24 | 배정도 실수(double precision) 브로드캐스트(broadcast) 루틴의 형식·포함 파일과 BUF(N)을 선언한다. 원문: `      SUBROUTINE VF_P1BCSD(BUF,N,IROOT)` (1). `CD=== 概要 ===========================================================` (3) (개요). `CDT   VF_P1BCSD:irootからその他へ送信する/実数` (5) (iroot에서 다른 프로세스로 실수를 브로드캐스트(broadcast)한다). `C==== 宣言 ===========================================================` (7) (선언). `C     -- 大域型 --` (9) (전역 형식). `      IMPLICIT INTEGER(I-N),DOUBLE PRECISION(A-H,O-Z)` (10). `C     -- 大域変数 --` (12) (전역 변수). `      INCLUDE 'VF_A0PRM.h'` (13). `      INCLUDE 'VF_ACPUTR.h'` (14). `      INCLUDE 'VF_APARAI.h'` (15). `CD    -- 引数 --` (17) (인수). `CD    BUF(N)  : I/O : R*8 : 転送するデータ` (18) (전송할 데이터). `CD    N       : IN  : I*4 : データの要素数` (19) (데이터 원소 수). `CD    IROOT   : IN  : I*4 : 送信元のランク` (20) (송신원 랭크(rank)). `      DIMENSION BUF(N)` (21). `C==== 実行 ===========================================================` (23) (실행). |
| 25–38 | 시작 시 1행 루틴 `SUBROUTINE VF_P1BCSD` 안. CPU 계측을 시작한다. NPROCS!=1이면 VF_ZXMP_BCASTD에 BUF,N,IROOT,IERR를 전달한다. 계측을 종료하고 반환한다. 원문: `      CALL VF_A2CPUT(0,ICPUST,KCP9PL)` (25). `C     -- irootからその他へ送信する --` (27) (iroot에서 다른 프로세스로 송신한다). `      IF (NPROCS.NE.1) CALL VF_ZXMP_BCASTD(BUF,N,IROOT,IERR)` (28). `C     -- 実行文の終了 --` (30) (실행문 종료). `      CALL VF_A2CPUT(0,ICPUEN,KCP9PL)` (31). `      GOTO 9999` (32). `C==== 終了 ===========================================================` (34) (종료). ` 9999 CONTINUE` (36). `      RETURN` (37). `      END` (38). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
