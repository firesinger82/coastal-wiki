---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/glb_comm/scatter_nodal_i.f
lines: 24
sha256: 1889d6f0eb052db845b4e5fdbd1676632a795546891bd845601f5f8317705e17
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# scatter_nodal_i.f — 판독 구간 기록

구간은 1행부터 24행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–15 | MPI_PARAM·M_PART·암시적 배정밀도와 K(NDF,*)를 선언한다(3–10). MN=MAXVAL(NN_EXT)로 정수 버퍼 KW(NDF,MN)를 할당한다(12–14). 원문: `      SUBROUTINE SCATTER_NODAL_I(K,NDF)` (1); `      USE MPI_PARAM` (3); `      USE M_PART` (4); `      IMPLICIT REAL*8(A-H,O-Z)` (6); `      DIMENSION K(NDF,*)` (8); `      INTEGER, POINTER :: KW(:,:)` (10); `      MN = MAXVAL( NN_EXT )` (12); `      ALLOCATE( KW(NDF,MN) )` (14). |
| 16–24 | 시작 시 1행 scatter_nodal_i 루틴 안. IP 루프에서 NN_EXT(IP)개 절점에 대응하는 전역 정수를 NOD로 모은다(16–18). NDF*N개 정수를 보내고 KW를 해제한다(19–24). 원문: `      DO IP = 1, NPROCS - 1` (16); `        N = NN_EXT(IP)` (17); `        KW(:,1:N) = K(:,NOD(1:N,IP))` (18); `        CALL M_MPI_SEND_I(KW,NDF*N,IP)` (19); `      ENDDO` (20); `      DEALLOCATE( KW )` (22); `      END` (24). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
