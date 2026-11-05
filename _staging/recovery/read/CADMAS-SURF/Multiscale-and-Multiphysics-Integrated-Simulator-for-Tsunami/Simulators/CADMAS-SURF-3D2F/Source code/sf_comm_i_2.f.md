---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D2F/Source code/sf_comm_i_2.f
lines: 24
sha256: 809b588c932785bb160fcc37caa021e94066f635034d08625fa4eb1cc711ee79
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# sf_comm_i_2.f — 판독 구간 기록

구간은 1행부터 24행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–24 | SF_COMM_I_2 선언과 배열 범위(1–6). 모든 상대에게 M*NS개 정수를 송신한다(8–10). 자신의 배열을 수신 배열 첫 NS열에 복사한다(12). IP=NS+1부터 상대별 NR(I)열을 받아 누적 이동한다(14–19). 송신·수신 요청을 각각 SF_MPI_WAITALL로 기다린다(21–22). 원문: `      SUBROUTINE SF_COMM_I_2(IRECV,NR,ISEND,M,NS,IPE,NPE)` (1)<br>`      IMPLICIT REAL*8(A-H,O-Z)` (3)<br>연속문: `      DIMENSION ISEND(M,NS),IRECV(M,*),IPE(NPE),NR(NPE),IREQ1(NPE)` (5); `     &         ,IREQ2(NPE)` (6)<br>`      DO I = 1, NPE` (8)<br>`        CALL SF_MPI_ISEND_I(ISEND,M*NS,IPE(I),IREQ1(I))` (9)<br>`      ENDDO` (10)<br>`      IRECV(:,1:NS) = ISEND(:,:)` (12)<br>`      IP = NS + 1` (14)<br>`      DO I = 1, NPE` (16)<br>`        CALL SF_MPI_IRECV_I(IRECV(1,IP),M*NR(I),IPE(I),IREQ2(I))` (17)<br>`        IP = IP + NR(I)` (18)<br>`      ENDDO` (19)<br>`      CALL SF_MPI_WAITALL(NPE,IREQ1)` (21)<br>`      CALL SF_MPI_WAITALL(NPE,IREQ2)` (22)<br>`      END` (24) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
