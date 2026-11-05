---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/glb_comm/send_cont0.f
lines: 34
sha256: caab2e5a55e16b86b2d4e976eb9115fb5cc11d760c40804f49188c5341ac40dc
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# send_cont0.f — 판독 구간 기록

구간은 1행부터 34행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–18 | M_VAL·MPI_PARAM·암시적 배정밀도와 작업 포인터를 선언한다(3–8). NICRG=KK(92), NNCRG=KK(93)로 정한다(10–11). 프로세스 1에서 I_BCT를 받아 IROOTC로 보내고 값이 0이면 반환한다(13–17). 원문: `      SUBROUTINE SEND_CONT0(KK)` (1); `      USE M_VAL` (3); `      USE MPI_PARAM` (4); `      IMPLICIT REAL*8(A-H,O-Z)` (6); `      DIMENSION KK(*)` (7); `      INTEGER, POINTER :: ICRG2(:),ICSF2(:,:)` (8); `      NICRG = KK(92)` (10); `      NNCRG = KK(93)` (11); `      CALL M_MPI_RECV_I(I_BCT,1,1)` (13); `      CALL C_MPI_SEND_I(I_BCT,1,IROOTC)` (15); `      IF( I_BCT == 0 ) RETURN` (17). |
| 19–34 | 시작 시 1행 send_cont0 루틴 안. ICRG2(NICRG)·ICSF2(5,NNCRG)를 할당하고 ICRG 둘째 행·ICSF의 2:6행을 복사한다(19–22). 수량 두 개·압축 목록 두 개·ICTB의 NICRG*NICRG 정수를 IROOTC로 보낸 뒤 작업 배열을 해제한다(24–34). 원문: `      ALLOCATE( ICRG2(NICRG) )` (19); `      ALLOCATE( ICSF2(5,NNCRG) )` (20); `      ICRG2(:) = ICRG(2,:)` (21); `      ICSF2(:,:) = ICSF(2:6,:)` (22); `      CALL C_MPI_SEND_I(NICRG,1,IROOTC)` (24); `      CALL C_MPI_SEND_I(NNCRG,1,IROOTC)` (25); `      CALL C_MPI_SEND_I(ICRG2,NICRG,IROOTC)` (27); `      CALL C_MPI_SEND_I(ICSF2,5*NNCRG,IROOTC)` (28); `      CALL C_MPI_SEND_I(ICTB,NICRG*NICRG,IROOTC)` (29); `      DEALLOCATE( ICRG2 )` (31); `      DEALLOCATE( ICSF2 )` (32); `      END` (34). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
