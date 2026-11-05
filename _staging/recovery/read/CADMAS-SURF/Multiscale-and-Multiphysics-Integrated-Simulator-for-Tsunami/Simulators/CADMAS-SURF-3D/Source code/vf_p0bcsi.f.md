---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Source code/vf_p0bcsi.f
lines: 38
sha256: 5aa1e053833d7d799fde3bcd523586854638596f93540852c5bd46539a5678f3
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# vf_p0bcsi.f — 판독 구간 기록

구간은 1행부터 38행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–24 | 정수 브로드캐스트(broadcast) 루틴의 형식·포함 파일·인수 의미와 IBUF(N)을 선언한다. 원문: `      SUBROUTINE VF_P0BCSI(IBUF,N,IROOT)` (1). `CD=== 概要 ===========================================================` (3) (개요). `CDT   VF_P0BCSI:irootからその他へ送信する/整数` (5) (iroot에서 다른 프로세스로 정수를 브로드캐스트(broadcast)한다). `C==== 宣言 ===========================================================` (7) (선언). `C     -- 大域型 --` (9) (전역 형식). `      IMPLICIT INTEGER(I-N),DOUBLE PRECISION(A-H,O-Z)` (10). `C     -- 大域変数 --` (12) (전역 변수). `      INCLUDE 'VF_A0PRM.h'` (13). `      INCLUDE 'VF_ACPUTR.h'` (14). `      INCLUDE 'VF_APARAI.h'` (15). `CD    -- 引数 --` (17) (인수). `CD    IBUF(N) : I/O : I*4 : 転送するデータ` (18) (전송할 데이터). `CD    N       : IN  : I*4 : データの要素数` (19) (데이터 원소 수). `CD    IROOT   : IN  : I*4 : 送信元のランク` (20) (송신원 랭크(rank)). `      DIMENSION IBUF(N)` (21). `C==== 実行 ===========================================================` (23) (실행). |
| 25–38 | 시작 시 1행 루틴 `SUBROUTINE VF_P0BCSI` 안. CPU 계측을 시작한다. MGPROC!=1이면 VF_ZXMG_BCASTI에 IBUF,N,IROOT,IERR를 전달한다. 계측을 종료하고 반환한다. 원문: `      CALL VF_A2CPUT(0,ICPUST,KCP9PL)` (25). `C     -- irootからその他へ送信する --` (27) (iroot에서 다른 프로세스로 송신한다). `      IF (MGPROC.NE.1) CALL VF_ZXMG_BCASTI(IBUF,N,IROOT,IERR)` (28). `C     -- 実行文の終了 --` (30) (실행문 종료). `      CALL VF_A2CPUT(0,ICPUEN,KCP9PL)` (31). `      GOTO 9999` (32). `C==== 終了 ===========================================================` (34) (종료). ` 9999 CONTINUE` (36). `      RETURN` (37). `      END` (38). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
