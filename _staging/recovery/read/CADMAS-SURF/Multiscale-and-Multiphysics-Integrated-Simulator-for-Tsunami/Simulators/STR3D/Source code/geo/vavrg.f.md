---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/geo/vavrg.f
lines: 13
sha256: 4cf186e61170154cff784e5f2dd49f548f74e4b2fc8994869ea70497be34b3e2
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# vavrg.f — 판독 구간 기록

구간은 1행부터 13행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–13 | VAVRG는 절점별 세 성분 값을 순차 평균(running average)으로 병합한다. 실수 IMPLICIT와 KN(ND)·N(*)·VG(3,*)·VE(3,ND)를 선언한다. 요소의 각 절점에서 N을 1 증가시키고 A=1/DBLE(N)을 계산한다. VG의 이전 평균에 1-A를, 새 VE에 A를 곱하여 더한다. 원문: `      SUBROUTINE VAVRG(VG,VE,KN,ND,N)` (1); `      IMPLICIT REAL*8(A-H,O-Z)` (3); `      DIMENSION KN(ND),N(*),VG(3,*),VE(3,ND)` (4); `      DO I = 1, ND` (6); `        NODE = KN(I)` (7); `        N(NODE) = N(NODE) + 1` (8); `        A = 1.D0 / DBLE( N(NODE) )` (9); `        VG(:,NODE) = VG(:,NODE) * ( 1.D0 - A ) + VE(:,I) * A` (10); `      ENDDO` (11); `      END` (13) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 8–10: 평균 계수는 이 루틴에서 증가시킨 누적 횟수의 역수이다. N의 초기화는 이 루틴에 없다.
