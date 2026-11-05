---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/glb_comm/gather_surface.f
lines: 24
sha256: f10c77444c774775a8ee895b1bcfb68045dc8eeb85cc1fc09d0165f928c4ab52
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# gather_surface.f — 판독 구간 기록

구간은 1행부터 24행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–15 | MPI_PARAM·M_PART와 암시적 배정밀도를 사용한다(3–6). X(NDF,*)와 W를 선언하고 MAXVAL(NPF)로 W(NDF,MN)를 할당한다(8–14). 원문: `      SUBROUTINE GATHER_SURFACE(X,NDF)` (1); `      USE MPI_PARAM` (3); `      USE M_PART` (4); `      IMPLICIT REAL*8(A-H,O-Z)` (6); `      DIMENSION X(NDF,*)` (8); `      REAL(8), POINTER :: W(:,:)` (10); `      MN = MAXVAL( NPF )` (12); `      ALLOCATE( W(NDF,MN) )` (14). |
| 16–24 | 시작 시 1행 gather_surface 루틴 안. IP 루프에서 NPF(IP)개 표면(surface)의 NDF*N 값을 수신한다(16–18). IPF(1:N,IP)를 전역 표면 위치로 사용하여 X를 채우고 W를 해제한다(19–24). 원문: `      DO IP = 1, NPROCS - 1` (16); `        N = NPF(IP)` (17); `        CALL M_MPI_RECV_D(W,NDF*N,IP)` (18); `        X(:,IPF(1:N,IP)) = W(:,1:N)` (19); `      ENDDO` (20); `      DEALLOCATE( W )` (22); `      END` (24). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
