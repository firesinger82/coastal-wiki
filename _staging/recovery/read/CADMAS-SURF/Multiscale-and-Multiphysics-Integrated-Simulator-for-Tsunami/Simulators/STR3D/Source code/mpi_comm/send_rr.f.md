---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/mpi_comm/send_rr.f
lines: 10
sha256: a698c87f6b19efdca629fbce8db451c22a2935c580a8207deb6461ff4f84e05f
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# send_rr.f — 판독 구간 기록

구간은 1행부터 10행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–10 | SEND_RR는 REAL*8 암묵 선언과 RR(*)를 사용한다(1–4). M_MPI_SEND_I로 명령 2와 인덱스 N을 모델 랭크 0으로 보내고 M_MPI_SEND_D로 RR(N)을 보낸다(6–8). 원문(연속행은 앞 문장에 이어짐): `      SUBROUTINE SEND_RR(RR,N)` (1); `      IMPLICIT REAL*8(A-H,O-Z)` (3); `      DIMENSION RR(*)` (4); `      CALL M_MPI_SEND_I(2,1,0)  ! SEND IOP=2 TO GLB_COMM` (6); `      CALL M_MPI_SEND_I(N,1,0)` (7); `      CALL M_MPI_SEND_D(RR(N),1,0)` (8); `      END` (10) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
