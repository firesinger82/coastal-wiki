---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/glb_comm/send_pos0.f
lines: 20
sha256: d08eff6e4408a42e4f5c07c6f0971d372f4bd2cc575f67e0f08ac37019354661
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# send_pos0.f — 판독 구간 기록

구간은 1행부터 20행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–13 | MPI_PARAM·암시적 배정밀도와 POS·FLUX 포인터를 선언한다(3–7). POS(3,NNOD)를 수집하여 IROOTC로 보내고 해제한다(9–12). 원문: `      SUBROUTINE SEND_POS0(NNOD,NELM,IGEO)` (1); `      USE MPI_PARAM` (3); `      IMPLICIT REAL*8(A-H,O-Z)` (5); `      REAL(8), POINTER :: POS(:,:),FLUX(:,:)` (7); `      ALLOCATE( POS(3,NNOD) )` (9); `      CALL GATHER_NODAL_D(POS,3)` (10); `      CALL C_MPI_SEND_D(POS,3*NNOD,IROOTC)` (11); `      DEALLOCATE( POS )` (12). |
| 14–20 | 시작 시 1행 send_pos0 루틴 안. IGEO 양수 분기에서 FLUX(3,NELM)를 할당하여 3*NELM개 값을 IROOTC로 보내고 해제한다(14–18). 원문: `      IF( IGEO > 0 ) THEN` (14); `        ALLOCATE( FLUX(3,NELM) )` (15); `        CALL C_MPI_SEND_D(FLUX,3*NELM,IROOTC)` (16); `        DEALLOCATE( FLUX )` (17); `      ENDIF` (18); `      END` (20). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 14–17: FLUX는 할당 후 바로 C_MPI_SEND_D에 전달된다. 이 파일의 해당 구간에는 FLUX 값 대입이나 수집 호출이 없다.
