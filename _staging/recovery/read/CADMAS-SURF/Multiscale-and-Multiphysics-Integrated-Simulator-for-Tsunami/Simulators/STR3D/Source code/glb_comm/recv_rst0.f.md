---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/glb_comm/recv_rst0.f
lines: 11
sha256: fbead3eeb5ad5d9909ff902e7213aaa75a618e55bf4f01da686255ecfc88109e
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# recv_rst0.f — 판독 구간 기록

구간은 1행부터 11행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–11 | MPI_PARAM을 사용한다(3). IROOTC에서 IRSTYP·IRETYP를 수신한다(5–6). 해석: 두 값은 재시작 유형 정보이다. 두 값을 각각 M_MPI_BCAST_I로 방송한다(8–9). 원문: `      SUBROUTINE RECV_RST0()` (1); `      USE MPI_PARAM` (3); `      CALL C_MPI_RECV_I(IRSTYP,1,IROOTC)` (5); `      CALL C_MPI_RECV_I(IRETYP,1,IROOTC)` (6); `      CALL M_MPI_BCAST_I(IRSTYP,1)` (8); `      CALL M_MPI_BCAST_I(IRETYP,1)` (9); `      END` (11). [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
