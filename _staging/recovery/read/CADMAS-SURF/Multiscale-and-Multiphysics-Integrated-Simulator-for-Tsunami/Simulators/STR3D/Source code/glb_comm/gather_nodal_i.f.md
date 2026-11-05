---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/glb_comm/gather_nodal_i.f
lines: 24
sha256: aa7dc356059e363882a4ca1227d2d74220da9ee7ab64193e77a5d4dce6c3217a
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# gather_nodal_i.f — 판독 구간 기록

구간은 1행부터 24행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–15 | MPI_PARAM·M_PART와 암시적 배정밀도를 사용한다(3–6). 정수 결과 K(NDF,*)와 정수 수신 버퍼 KW를 선언한다(8–10). MAXVAL(NN_INT)로 KW(NDF,MN)를 할당한다(12–14). 원문: `      SUBROUTINE GATHER_NODAL_I(K,NDF)` (1); `      USE MPI_PARAM` (3); `      USE M_PART` (4); `      IMPLICIT REAL*8(A-H,O-Z)` (6); `      DIMENSION K(NDF,*)` (8); `      INTEGER, POINTER :: KW(:,:)` (10); `      MN = MAXVAL( NN_INT )` (12); `      ALLOCATE( KW(NDF,MN) )` (14). |
| 16–24 | 시작 시 1행 gather_nodal_i 루틴 안. IP 루프에서 NN_INT(IP)에 해당하는 NDF*N 정수를 수신한다(16–18). NOD(1:N,IP)의 전역 위치에 K를 채우고 KW를 해제한다(19–24). 원문: `      DO IP = 1, NPROCS - 1` (16); `        N = NN_INT(IP)` (17); `        CALL M_MPI_RECV_I(KW,NDF*N,IP)` (18); `        K(:,NOD(1:N,IP)) = KW(:,1:N)` (19); `      ENDDO` (20); `      DEALLOCATE( KW )` (22); `      END` (24). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
