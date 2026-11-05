---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/util/rmult3.f
lines: 11
sha256: 63e3de00df662f280b3d7f04d0ffba90b5821fd39d25f85cc052e5d7ed16c108
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# rmult3.f — 판독 구간 기록

구간은 1행부터 11행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–11 | RMULT3의 인수와 암시적 형(implicit typing), A(*)·B(*)를 선언한다(1–4). I=1..N에서 A(I)에 R*B(I)*B(I)를 더한다(6–8). 주석·RETURN·END까지 포함한다. 원문: `      SUBROUTINE RMULT3(A,B,R,N)` (1); `      IMPLICIT REAL*8(A-H,O-Z)` (3); `      DIMENSION A(*),B(*)` (4); `      DO 8000 I=1,N` (6); `      A(I)=A(I)+R*B(I)*B(I)` (7); ` 8000 CONTINUE` (8); `      RETURN` (10); `      END` (11). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
