---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/util/harfta2.f
lines: 22
sha256: 77e1efcdb98de0ea930d829db5f0e3efae9bf0b02c8dec6361a3dc8acbfa4e03
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# harfta2.f — 판독 구간 기록

구간은 1행부터 22행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–8 | HARFTA2는 B와 C의 전치(transpose)의 곱을 A에 압축 저장(packed storage)한다는 주석을 갖는다(1–3). 여기서 3행의 CT는 C의 전치를 뜻한다. 암시적 형과 A(1)·B(N1,N2)·C(N1,N2)를 선언한다(5–6). IC를 0으로 둔다(8). 원문: `      SUBROUTINE  HARFTA2( A,B,C, N1,N2 )` (1); `C     A = B X CT  ( A MATRIX IS HARF MATRIX )` (3); `      IMPLICIT REAL*8 (A-H,O-Z)` (5); `      DIMENSION  A(1),B(N1,N2),C(N1,N2)` (6); `      IC = 0` (8). |
| 9–22 | 시작 시 1행 HARFTA2 루틴 안. I=1..N1, J=I..N1마다 IC를 증가시키고 A(IC)를 0으로 둔다(9–12). K=1..N2에서 B(I,K)*C(J,K)를 누적한다(14–16). 루프 종료·주석·RETURN·END를 포함한다. 원문: `      DO 3000 I=1,N1` (9); `      DO 2000 J=I,N1` (10); `         IC    = IC + 1` (11); `         A(IC) = 0.0D0` (12); `         DO 1000 K=1,N2` (14); `            A(IC) = A(IC) + B(I,K)*C(J,K)` (15); ` 1000    CONTINUE` (16); ` 2000 CONTINUE` (17); ` 3000 CONTINUE` (18); `      RETURN` (21); `      END` (22). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 6·11–15: A의 선언은 A(1)이며, 실제 접근 첨자는 누적하는 IC이다.
