---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/mpi_comm/recv_kk.f
lines: 9
sha256: ac5ed0b11a9f59ea077d6365a7e34c6a299aa5a8b942debf6e514371921ae180
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# recv_kk.f — 판독 구간 기록

구간은 1행부터 9행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | RECV_KK는 KK(*)를 선언한다(1–3). 모델 랭크 1로부터 인덱스 N과 정수 값 KX를 순서대로 M_MPI_RECV_I로 받고 KK(N)에 대입한다(5–7). 수신 통신자와 송신자 인수의 근거는 `mpi_comm/m_mpi_recv_i.f:1–9`이다. 이 루틴 자체에는 수신 실행 랭크를 제한하는 조건이 없다. 원문(연속행은 앞 문장에 이어짐): `      SUBROUTINE RECV_KK(KK)` (1); `      DIMENSION KK(*)` (3); `      CALL M_MPI_RECV_I(N,1,1)` (5); `      CALL M_MPI_RECV_I(KX,1,1)` (6); `      KK(N) = KX` (7); `      END` (9) [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 3·5–7: KK는 가정 크기 배열(assumed-size array)이다. 수신한 N의 범위를 검사하는 문장은 없다.
