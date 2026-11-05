---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/mpi_comm/send_kk.f
lines: 9
sha256: 31fce3c34c1d208f7eda474318707d9327789854224735b06e91aab063be9b10
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# send_kk.f — 판독 구간 기록

구간은 1행부터 9행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | SEND_KK는 KK(*)를 선언한다(1–3). M_MPI_SEND_I를 세 번 호출하여 명령 1, 인덱스 N, KK(N)의 정수 값을 모델 랭크 0으로 보낸다(5–7). 원문(연속행은 앞 문장에 이어짐): `      SUBROUTINE SEND_KK(KK,N)` (1); `      DIMENSION KK(*)` (3); `      CALL M_MPI_SEND_I(1,1,0)  ! SEND IOP=1 TO GLB_COMM` (5); `      CALL M_MPI_SEND_I(N,1,0)` (6); `      CALL M_MPI_SEND_I(KK(N),1,0)` (7); `      END` (9) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
