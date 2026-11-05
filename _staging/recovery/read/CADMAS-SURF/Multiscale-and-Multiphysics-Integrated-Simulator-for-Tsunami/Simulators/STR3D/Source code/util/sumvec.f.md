---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/util/sumvec.f
lines: 12
sha256: 706a3d0e07de6cbf0573e6e31ba0100df13c6c743f7c3983ab0e0d2b3562d706
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# sumvec.f — 판독 구간 기록

구간은 1행부터 12행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–12 | SUMVEC의 인수와 암시적 형(implicit typing), A(N)을 선언한다(1–4). R을 0으로 두고 I=1..N 루프에서 A(I)를 누적한다(6–9). 주석·RETURN·END까지 포함한다. 원문: `      SUBROUTINE SUMVEC(R,A,N)` (1); `      IMPLICIT REAL*8(A-H,O-Z)` (3); `      DIMENSION A(N)` (4); `      R=0.` (6); `      DO 1000 I=1,N` (7); `        R=R+A(I)` (8); ` 1000 CONTINUE` (9); `      RETURN` (11); `      END` (12). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
