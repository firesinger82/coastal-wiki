---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/geo/velte1.f
lines: 10
sha256: 81135d9a0a77fd76479bd11afb788886d47b81d851b6a8cfbdcb7f41a9b93e2b
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# velte1.f — 판독 구간 기록

구간은 1행부터 10행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–10 | VELTE1은 실수 IMPLICIT와 VEL(3,4)·VELG(3)를 선언한다. I=1,4 루프에서 VELG의 세 성분을 VEL의 네 열에 복사한다. 해석: 한 적분점의 값을 네 절점으로 복사하는 용도로 보인다. 원문: `      SUBROUTINE VELTE1(VEL,VELG)` (1); `      IMPLICIT REAL*8(A-H,O-Z)` (3); `      DIMENSION VEL(3,4),VELG(3)` (4); `      DO I = 1, 4` (6); `        VEL(:,I) = VELG(:)` (7); `      ENDDO` (8); `      END` (10) [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
