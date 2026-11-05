---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/partition/part_send_tblx.f
lines: 31
sha256: 2ddddb7c43caec5a35c480e0a90289f9c4f210474183efe1f389742b60a3d639
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# part_send_tblx.f — 판독 구간 기록

구간은 1행부터 31행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–19 | PART_SEND_TBLX의 모듈·암시적 형·KK 배열 선언. NPROCS-1개 분할에 대해 외부 절점 배열을 할당하고 PART_SEND_TBLX1을 호출한다. 원문: `      SUBROUTINE PART_SEND_TBLX(KK)` (1); `      USE M_VAL` (3); `      USE MPI_PARAM` (4); `      USE M_PART` (5); `      IMPLICIT REAL*8(A-H,O-Z)` (7); `      DIMENSION KK(*)` (9); `      NPECG = NPROCS - 1` (11); `      ALLOCATE( NN_EXTX(NPECG) )` (13); `      ALLOCATE( NODX(MAXVAL(NN_INT),NPECG) )` (14); `      DO IP = 1, NPECG` (16); `        CALL PART_SEND_TBLX1(KK,IP)` (17); `      ENDDO` (18). |
| 20–31 | PART_SEND_TBLX 루틴 안. RSLV0·IFRIC·FRIC·U0·RL0를 해제한다. PART_SEND_TBLX2를 호출한 뒤 NN_EXTX·NODX를 해제한다. 원문: `      DEALLOCATE( RSLV0 )` (20); `      DEALLOCATE( IFRIC )` (21); `      DEALLOCATE( FRIC )` (22); `      DEALLOCATE( U0 )` (23); `      DEALLOCATE( RL0 )` (24); `      CALL PART_SEND_TBLX2(KK)` (26); `      DEALLOCATE( NN_EXTX )` (28); `      DEALLOCATE( NODX )` (29); `      END` (31). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 14: NODX의 첫 차원을 MAXVAL(NN_INT)로 할당한다.
