---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/mpi_comm/send_cont.f
lines: 40
sha256: bde6e0a6c6c65a1100966a201bdd061602832796400ecc7cb493fb65721374d1
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# send_cont.f — 판독 구간 기록

구간은 1행부터 40행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–31 | SEND_CONT는 MPI_PARAM, REAL*8 암묵 선언과 ICRG/ICSF/ICTB 차원을 사용한다(1–9). 모델 랭크 0은 I_BCT를 IROOTC로 보낸 뒤 I_BCT==0이면 반환한다(11–15). ICRG의 둘째 행과 ICSF의 2:6행을 임시 배열로 추출한다(17–20). NICRG/NNCRG, 두 추출 배열 및 ICTB를 IROOTC로 보내고 임시 배열을 해제한다(22–30). 원문(연속행은 앞 문장에 이어짐): `      SUBROUTINE SEND_CONT(I_BCT,NICRG,NNCRG,ICRG,ICSF,ICTB)` (1); `      USE MPI_PARAM` (3); `      IMPLICIT REAL*8(A-H,O-Z)` (5); `      DIMENSION ICRG(2,NICRG),ICSF(6,NNCRG),ICTB(NICRG,NICRG)` (7); `      INTEGER, POINTER :: ICRG2(:),ICSF2(:,:)` (9); `      IF( MYRANK == 0 ) THEN` (11); `        CALL C_MPI_SEND_I(I_BCT,1,IROOTC)` (13); `        IF( I_BCT == 0 ) RETURN` (15); `        ALLOCATE( ICRG2(NICRG) )` (17); `        ALLOCATE( ICSF2(5,NNCRG) )` (18); `        ICRG2(:) = ICRG(2,:)` (19); `        ICSF2(:,:) = ICSF(2:6,:)` (20); `        CALL C_MPI_SEND_I(NICRG,1,IROOTC)` (22); `        CALL C_MPI_SEND_I(NNCRG,1,IROOTC)` (23); `        CALL C_MPI_SEND_I(ICRG2,NICRG,IROOTC)` (25); `        CALL C_MPI_SEND_I(ICSF2,5*NNCRG,IROOTC)` (26); `        CALL C_MPI_SEND_I(ICTB,NICRG*NICRG,IROOTC)` (27); `        DEALLOCATE( ICRG2 )` (29); `        DEALLOCATE( ICSF2 )` (30) |
| 32–40 | 시작 시 1행 SEND_CONT 루틴의 11행 `IF( MYRANK == 0 ) THEN`에 대한 32행 `ELSEIF( MYRANK == 1 ) THEN` 분기. 이 사슬은 38행 `ENDIF`에서 닫힌다. ELSE는 없다. MYRANK가 0도 1도 아니면 이 루틴에서 송신하지 않는다. 모델 랭크 1은 명령 21과 I_BCT를 랭크 0으로 보낸다(34–36). 조건과 루틴을 닫는다(38–40). 원문(연속행은 앞 문장에 이어짐): `      ELSEIF( MYRANK == 1 ) THEN` (32); `        CALL M_MPI_SEND_I(21,1,0)  ! SEND IOP=21 TO GLB_COMM` (34); `        CALL M_MPI_SEND_I(I_BCT,1,0)` (36); `      ENDIF` (38); `      END` (40) [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 18·20·26: 송신용 ICSF2는 ICSF의 2:6행을 보존한다. 열당 정수 개수는 5이다. 해석: 각 열은 한 면의 자료로 읽힌다. [11-04 전수 검증 정정]
