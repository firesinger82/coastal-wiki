---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Source code/vf_p1sumi.f
lines: 40
sha256: 5b7ee0b5acd6804e5af214bda13b860d420b8d10f43ca3b021baf44413b43d58
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# vf_p1sumi.f — 판독 구간 기록

구간은 1행부터 40행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–22 | 정수 총합 축약(reduction) 루틴의 형식·포함 파일과 송수신 인수 의미를 선언한다. 원문: `      SUBROUTINE VF_P1SUMI(ISEND,IRECV)` (1). `CD=== 概要 ===========================================================` (3) (개요). `CDT   VF_P1SUMI:データの総和を求める/整数` (5) (정수 데이터 총합을 구한다). `C==== 宣言 ===========================================================` (7) (선언). `C     -- 大域型 --` (9) (전역 형식). `      IMPLICIT INTEGER(I-N),DOUBLE PRECISION(A-H,O-Z)` (10). `C     -- 大域変数 --` (12) (전역 변수). `      INCLUDE 'VF_A0PRM.h'` (13). `      INCLUDE 'VF_ACPUTR.h'` (14). `      INCLUDE 'VF_APARAI.h'` (15). `CD    -- 引数 --` (17) (인수). `CD    ISEND : IN  : I*4 : 送信するデータ` (18) (송신할 데이터). `CD    IRECV : OUT : I*4 : データの総和` (19) (데이터 총합). `C==== 実行 ===========================================================` (21) (실행). |
| 23–40 | 시작 시 1행 루틴 `SUBROUTINE VF_P1SUMI` 안. CPU 계측을 시작한다. NPROCS!=1이면 VF_ZXMP_ALLSMI를 호출한다. 단일 프로세스이면 IRECV=ISEND로 복사한다. 계측을 종료하고 반환한다. 원문: `      CALL VF_A2CPUT(0,ICPUST,KCP9PL)` (23). `C     -- 総和をとる --` (25) (총합을 구한다). `      IF (NPROCS.NE.1) THEN` (26). `        CALL VF_ZXMP_ALLSMI(ISEND,IRECV,IERR)` (27). `      ELSE` (28). `        IRECV=ISEND` (29). `      ENDIF` (30). `C     -- 実行文の終了 --` (32) (실행문 종료). `      CALL VF_A2CPUT(0,ICPUEN,KCP9PL)` (33). `      GOTO 9999` (34). `C==== 終了 ===========================================================` (36) (종료). ` 9999 CONTINUE` (38). `      RETURN` (39). `      END` (40). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
