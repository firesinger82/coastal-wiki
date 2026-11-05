---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/partition/partition.f
lines: 33
sha256: 5b280299c56151c332f3cabe9ac8130f8bcfcd431941cdc3c50fafae2d73e8d4
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# partition.f — 판독 구간 기록

구간은 1행부터 33행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–16 | PARTITION의 모듈·암시적 형·배열 선언. MYRANK=0에서 PART를 호출한다. 그 안에서 KK(92)>0이면 PART_C를 호출한다. 전 순위에서 BCAST_TBL을 호출한다. 원문: `      SUBROUTINE PARTITION(KK,RR,IFL,ICK)` (1); `      USE MPI_PARAM` (3); `      IMPLICIT REAL*8(A-H,O-Z)` (5); `      INTEGER*8 MUSED` (7); `      DIMENSION KK(*),RR(*),IFL(*),ICK(*)` (9); `      IF( MYRANK == 0 ) THEN` (11); `        CALL PART(KK,IFL,ICK(4))` (12); `        IF( KK(92) > 0 ) CALL PART_C(KK,IFL(11))` (13); `      ENDIF` (14); `      CALL BCAST_TBL(KK,RR,ICK)` (16). |
| 17–33 | PARTITION 루틴 안. 순위 0은 1부터 NPROCS-1까지 SEND_TBL을 호출한다. 나머지는 RECV_TBL을 호출하고 ICK(1)=1이면 DATA_CHECK를 수행한다. 순위 0은 DEALLOC과 사용 메모리 출력을 수행한다. 원문: `      IF( MYRANK == 0 ) THEN` (18); `        DO IP = 1, NPROCS - 1` (19); `          CALL SEND_TBL(KK,IP)` (20); `        ENDDO` (21); `      ELSE` (22); `        CALL RECV_TBL(KK)` (23); `        IF( ICK(1) == 1 ) CALL DATA_CHECK(KK,RR)` (24); `      ENDIF` (25); `      IF( MYRANK == 0 ) THEN` (27); `        CALL DEALLOC(KK,IFL(11),ICK(3))` (28); 연속문(29–30): `        WRITE(IFL(11),'(/X,A,F8.1,A)')` <br> `     &    'SUB. PARTITION  : ', MUSED()*4.D-6, '(MB) USED.'`; `      ENDIF` (31); `      END` (33). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
