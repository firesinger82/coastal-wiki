---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/glb_comm/scatter_surface.f
lines: 24
sha256: 1cc33c322bca4597b51e19ddd5ca28575759f6c9773523c1e64b114a81bea7a5
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# scatter_surface.f — 판독 구간 기록

구간은 1행부터 24행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–15 | MPI_PARAM·M_PART·암시적 배정밀도와 X(NDF,*)를 선언한다(3–10). MN=MAXVAL(NPF)로 배정밀도 버퍼 W(NDF,MN)를 할당한다(12–14). 원문: `      SUBROUTINE SCATTER_SURFACE(X,NDF)` (1); `      USE MPI_PARAM` (3); `      USE M_PART` (4); `      IMPLICIT REAL*8(A-H,O-Z)` (6); `      DIMENSION X(NDF,*)` (8); `      REAL(8), POINTER :: W(:,:)` (10); `      MN = MAXVAL( NPF )` (12); `      ALLOCATE( W(NDF,MN) )` (14). |
| 16–24 | 시작 시 1행 scatter_surface 루틴 안. IP 루프에서 NPF(IP)개 표면에 대응하는 전역 값을 IPF로 모은다(16–18). NDF*N개 값을 보내고 W를 해제한다(19–24). 원문: `      DO IP = 1, NPROCS - 1` (16); `        N = NPF(IP)` (17); `        W(:,1:N) = X(:,IPF(1:N,IP))` (18); `        CALL M_MPI_SEND_D(W,NDF*N,IP)` (19); `      ENDDO` (20); `      DEALLOCATE( W )` (22); `      END` (24). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
