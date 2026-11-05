---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D2F/Source code/sf_comm_d_2.f
lines: 24
sha256: fa99ded6b47afb2caa81805d8bc20990d52d999dd3f40648515200f1fb7b0d78
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# sf_comm_d_2.f — 판독 구간 기록

구간은 1행부터 24행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–7 | 암시적 배정밀도(double precision)·송신 DSEND(M,NS)·가정 크기(assumed-size) 수신 DRECV(M,*)·대상 IPE(NPE)·수신 수 NR(NPE)·요청 IREQ1/IREQ2를 선언한다. 원문: `      SUBROUTINE SF_COMM_D_2(DRECV,NR,DSEND,M,NS,IPE,NPE)` (1); `      IMPLICIT REAL*8(A-H,O-Z)` (3); `      DIMENSION DSEND(M,NS),DRECV(M,*),IPE(NPE),NR(NPE),IREQ1(NPE)` (5); `     &         ,IREQ2(NPE)` (6) |
| 8–15 | 시작 시 1행 SF_COMM_D_2 루틴 안이다. 대상 I=1..NPE마다 같은 DSEND를 M*NS개 비차단(nonblocking) 송신 등록한다. DRECV의 첫 NS열에는 자기 자료를 복사하고 원격 수신 시작 열 IP=NS+1을 계산한다. 원문: `      DO I = 1, NPE` (8); `        CALL SF_MPI_ISEND_D(DSEND,M*NS,IPE(I),IREQ1(I))` (9); `      ENDDO` (10); `      DRECV(:,1:NS) = DSEND(:,:)` (12); `      IP = NS + 1` (14) |
| 16–24 | 시작 시 1행 SF_COMM_D_2 루틴 안이다. SF_MPI_IRECV_D의 첫째 인수로 `DRECV(1,IP)`를 전달한다. 둘째 인수로 `M*NR(I)`를 전달한다. 해석: 이 호출은 대상별 비차단 수신 등록으로 보인다. 이 파일에는 실제 수신된 원소 수를 확인하는 호출이 없다. IP에 NR(I)를 누적하여 다음 구간으로 옮긴다. SF_MPI_WAITALL로 송신 요청과 수신 요청을 각각 완료 대기한다. 원문: `      DO I = 1, NPE` (16); `        CALL SF_MPI_IRECV_D(DRECV(1,IP),M*NR(I),IPE(I),IREQ2(I))` (17); `        IP = IP + NR(I)` (18); `      ENDDO` (19); `      CALL SF_MPI_WAITALL(NPE,IREQ1)` (21); `      CALL SF_MPI_WAITALL(NPE,IREQ2)` (22); `      END` (24) [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 5·12–19: DRECV의 둘째 차원은 가정 크기이다. 이 루틴에는 NS와 NR 합에 대한 수신 배열 용량 검사문이 없다.
