---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/src/dertr2.f
lines: 40
sha256: bdba3ba470708e7e5c1de788913b5b3a1c852c7f4c45405ab10b7f01a85e6a9f
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# dertr2.f — 판독 구간 기록

구간은 1행부터 40행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | DERTR2의 P(2,ND)와 RL(3)를 선언한다. 4행 주석은 P(i,j)를 ∂Nj/∂ξi로 표시한다. 해석: N을 형상함수로 보면 P는 형상함수 미분이다. `面積座標`는 면적좌표(area coordinate), `節点数`는 절점 수(number of nodes)를 뜻한다. 원문: `      SUBROUTINE DERTR2(RL,P,ND)` (1); 주석 원문 `C     RL : IN  : 面積座標` (3); 주석 원문 `C     P  : OUT : P(i,j) = ∂Nj/∂ξi` (4); 주석 원문 `C     ND : IN  : 節点数` (5); `      IMPLICIT REAL*8(A-H,O-Z)` (7); `      DIMENSION P(2,ND),RL(3)` (8). [11-04 전수 검증 정정] |
| 10–23 | 시작 시 1행 DERTR2 루틴 안. 먼저 6개 절점의 두 방향 미분을 계산한다. 원문: `      P( 1, 1) = 4.*RL(1)-1.` (10); `      P( 1, 2) = 0.` (11); `      P( 1, 3) = -(4.*RL(3)-1.)` (12); `      P( 1, 4) = 4.*RL(2)` (13); `      P( 1, 5) = -4.*RL(2)` (14); `      P( 1, 6) = 4.*(RL(3)-RL(1))` (15); `      P( 2, 1) = 0.` (17); `      P( 2, 2) = 4.*RL(2)-1.` (18); `      P( 2, 3) = -(4.*RL(3)-1.)` (19); `      P( 2, 4) = 4.*RL(1)` (20); `      P( 2, 5) = 4.*(RL(3)-RL(2))` (21); `      P( 2, 6) = -4.*RL(1)` (22). |
| 24–40 | 시작 시 1행 DERTR2 루틴 안. ND가 7이면 계수 27을 사용하여 P의 7열을 계산한다. I·J 루프는 1–3열에는 7열의 1/3을 더한다. 같은 루프는 4–6열에는 7열의 -2/3을 더한다. 해석: 7열은 중앙 절점에 해당한다. 분기 종료·반환문·루틴 끝을 포함한다. 원문: `      IF( ND .EQ. 7 ) THEN` (24); `        P(1,7) = 27.*RL(2)*(RL(3)-RL(1))` (25); `        P(2,7) = 27.*RL(1)*(RL(3)-RL(2))` (26); `        DO I = 1, 6` (27); `          DO J = 1, 2` (28); `            IF( I .LE. 3 ) THEN` (29); `              FAC = 1.D0/3.D0` (30); `            ELSE` (31); `              FAC = -2.D0/3.D0` (32); `            ENDIF` (33); `            P(J,I) = P(J,I) + FAC*P(J,7)` (34); `          ENDDO` (35); `        ENDDO` (36); `      ENDIF` (37); `      RETURN` (39); `      END` (40). [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 8·10–22: P의 두 번째 크기는 ND다. 1–6번 성분 대입 앞에는 ND>=6 검사가 없다.
