---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/glb_comm/bctset0.f
lines: 14
sha256: d191326468926b054b8c24e61ee441282e9513d5dfa0c696ea9e7c8cd062ba43
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# bctset0.f — 판독 구간 기록

구간은 1행부터 14행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–14 | BCTSET0는 M_VAL을 사용한다. 실수 IMPLICIT와 KK(*)를 선언한다. NICRG=KK(92)를 읽는다. 송신원 1에서 ICTB의 NICRG*NICRG개 정수, FRTB의 3*NICRG*NICRG개 실수, KK(96)의 정수 한 개를 순서대로 받는다. 통신 호출과 인수를 아래에 그대로 적었다. 원문: `      SUBROUTINE BCTSET0(KK)` (1); `      USE M_VAL` (3); `      IMPLICIT REAL*8 (A-H,O-Z)` (5); `      DIMENSION KK(*)` (6); `      NICRG = KK(92)` (8); `      CALL M_MPI_RECV_I(ICTB,NICRG*NICRG,1)` (10); `      CALL M_MPI_RECV_D(FRTB,3*NICRG*NICRG,1)` (11); `      CALL M_MPI_RECV_I(KK(96),1,1)` (12); `      END` (14) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
