---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D2F/Source code/sf_comm_i_1.f
lines: 18
sha256: 96059d9946cbf01da7190f4574055f6f2183bfe666c639e0a23f45fbcf8465e6
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# sf_comm_i_1.f — 판독 구간 기록

구간은 1행부터 18행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–18 | SF_COMM_I_1 선언과 배열 범위(1–5). IPE 목록의 각 상대에게 정수 ISEND 한 개를 비차단 송신(nonblocking send)한다(7–9). 각 상대의 정수 한 개를 IRECV에 비차단 수신(nonblocking receive)한 뒤 두 요청 배열을 각각 SF_MPI_WAITALL로 기다린다(11–16). 원문: `      SUBROUTINE SF_COMM_I_1(IRECV,ISEND,IPE,NPE)` (1)<br>`      IMPLICIT REAL*8(A-H,O-Z)` (3)<br>`      DIMENSION IRECV(NPE),IPE(NPE),IREQ1(NPE),IREQ2(NPE)` (5)<br>`      DO I = 1, NPE` (7)<br>`        CALL SF_MPI_ISEND_I(ISEND,1,IPE(I),IREQ1(I))` (8)<br>`      ENDDO` (9)<br>`      DO I = 1, NPE` (11)<br>`        CALL SF_MPI_IRECV_I(IRECV(I),1,IPE(I),IREQ2(I))` (12)<br>`      ENDDO` (13)<br>`      CALL SF_MPI_WAITALL(NPE,IREQ1)` (15)<br>`      CALL SF_MPI_WAITALL(NPE,IREQ2)` (16)<br>`      END` (18) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
