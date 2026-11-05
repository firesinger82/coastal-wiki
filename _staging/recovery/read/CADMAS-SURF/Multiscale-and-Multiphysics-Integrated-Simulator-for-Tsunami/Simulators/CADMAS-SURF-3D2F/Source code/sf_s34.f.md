---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D2F/Source code/sf_s34.f
lines: 21
sha256: 05c0223a0e2fcf04615b7b2186c7a07965a855270c97295f9d61cf35d29bacd2
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# sf_s34.f — 판독 구간 기록

구간은 1행부터 21행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–21 | N=3이면 두 변의 이차원 외적으로 부호 있는 면적을 구한다(7–10). N=4이면 두 삼각형의 부호 있는 면적을 더한다(11–16). S<0일 때 VF_A2ERR를 호출하는 문장은 주석 처리되어 있다(19). 원문(연속 표시는 앞 문장에 이어짐): `      SUBROUTINE SF_S34(S,X,N)` (1); `      IMPLICIT REAL*8(A-H,O-Z)` (3); `      DIMENSION X(2,N),R12(2),R13(2),R14(2)` (5); `      IF( N == 3 ) THEN` (7); `        R12(:) = X(:,2) - X(:,1)` (8); `        R13(:) = X(:,3) - X(:,1)` (9); `        S = .5D0 * ( R12(1)*R13(2) - R12(2)*R13(1) )` (10); `      ELSEIF( N == 4 ) THEN` (11); `        R12(:) = X(:,2) - X(:,1)` (12); `        R13(:) = X(:,3) - X(:,1)` (13); `        R14(:) = X(:,4) - X(:,1)` (14); `        S = .5D0 * ( R12(1)*R13(2) - R12(2)*R13(1) )` (15); `     &    + .5D0 * ( R13(1)*R14(2) - R13(2)*R14(1) )` (16); `      ENDIF` (17); 주석 처리된 코드: `!     IF( S < 0. ) CALL VF_A2ERR('SF_S34','P.G ERROR.')` (19); `      END` (21). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 7–17: N이 3·4가 아닌 경우의 ELSE와 S 대입이 없다.
- 10·15–16·19: 면적 식은 절댓값을 취하지 않는다. 음수 면적 오류 검사는 주석 처리되어 있다.
