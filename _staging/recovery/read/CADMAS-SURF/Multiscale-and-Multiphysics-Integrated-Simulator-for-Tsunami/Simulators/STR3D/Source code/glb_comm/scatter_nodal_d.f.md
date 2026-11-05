---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/glb_comm/scatter_nodal_d.f
lines: 24
sha256: b5419b80d3590db686cdc53b2fd208198f217dcfc17e1b08024c6ba76442842c
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# scatter_nodal_d.f — 판독 구간 기록

구간은 1행부터 24행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–15 | MPI_PARAM·M_PART·암시적 배정밀도와 X(NDF,*)를 선언한다(3–10). MN=MAXVAL(NN_EXT)로 배정밀도 버퍼 W(NDF,MN)를 할당한다(12–14). 원문: `      SUBROUTINE SCATTER_NODAL_D(X,NDF)` (1); `      USE MPI_PARAM` (3); `      USE M_PART` (4); `      IMPLICIT REAL*8(A-H,O-Z)` (6); `      DIMENSION X(NDF,*)` (8); `      REAL(8), POINTER :: W(:,:)` (10); `      MN = MAXVAL( NN_EXT )` (12); `      ALLOCATE( W(NDF,MN) )` (14). |
| 16–24 | 시작 시 1행 scatter_nodal_d 루틴 안. IP 루프에서 NN_EXT(IP)개 절점을 대상으로 한다(16–17). NOD(1:N,IP)의 전역 값을 W(:,1:N)에 모아 NDF*N개를 보내고 W를 해제한다(18–24). 원문: `      DO IP = 1, NPROCS - 1` (16); `        N = NN_EXT(IP)` (17); `        W(:,1:N) = X(:,NOD(1:N,IP))` (18); `        CALL M_MPI_SEND_D(W,NDF*N,IP)` (19); `      ENDDO` (20); `      DEALLOCATE( W )` (22); `      END` (24). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
