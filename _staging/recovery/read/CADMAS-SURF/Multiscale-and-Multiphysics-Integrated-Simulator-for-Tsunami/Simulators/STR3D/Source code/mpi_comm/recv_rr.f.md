---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/mpi_comm/recv_rr.f
lines: 10
sha256: 9dad1b989de9fdb992f3a6a9b180cb71ed85832c1aa9b7f65e34ee100445cc11
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# recv_rr.f — 판독 구간 기록

구간은 1행부터 10행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–10 | RECV_RR는 REAL*8 암묵 선언과 RR(*)를 선언한다(1–4). 모델 랭크 1로부터 인덱스 N은 M_MPI_RECV_I로 받고 값 X는 M_MPI_RECV_D로 받은 뒤 RR(N)에 대입한다(6–8). 수신 통신자와 송신자 인수의 근거는 `mpi_comm/m_mpi_recv_i.f:1–9`와 `mpi_comm/m_mpi_recv_d.f:1–12`이다. 이 루틴 자체에는 수신 실행 랭크를 제한하는 조건이 없다. 원문(연속행은 앞 문장에 이어짐): `      SUBROUTINE RECV_RR(RR)` (1); `      IMPLICIT REAL*8(A-H,O-Z)` (3); `      DIMENSION RR(*)` (4); `      CALL M_MPI_RECV_I(N,1,1)` (6); `      CALL M_MPI_RECV_D(X,1,1)` (7); `      RR(N) = X` (8); `      END` (10) [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 4·6–8: RR는 가정 크기 배열이다. 수신한 N의 범위를 검사하는 문장은 없다.
